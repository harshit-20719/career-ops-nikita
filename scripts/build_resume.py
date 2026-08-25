#!/usr/bin/env python3
"""Render a resume HTML file to PDF, then verify the PDF is ATS-readable.

    python3 scripts/build_resume.py resume/build/base-generalist.html
    python3 scripts/build_resume.py <input.html> -o "Nikita-Sachanandani-Strategy.pdf"

Uses headless Chromium, so the PDF carries a real text layer — which is what an
applicant tracking system parses. A resume rendered as an image scores zero.

The verification step extracts the text back out and checks that the contact
details and section headings survived the round trip. If that check fails, the
PDF should not be sent.
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
]

# Anything an ATS keys on. If one of these is missing from the extracted text,
# the layout has broken it and the PDF is not safe to submit.
REQUIRED = [
    "Nikita Sachanandani",
    "sachanandani.nikita@gmail.com",
    "7698030306",
    "Tata Trusts",
    "EXPERIENCE",
    "EDUCATION",
]


def check_font(html_path):
    """Warn if the first font in the body stack isn't installed.

    A missing font fails silently: the browser substitutes something generic and
    the PDF still renders, just uglier. That happened once already (Calibri fell
    back to DejaVu Sans), so it's checked rather than trusted.
    """
    text = html_path.read_text(encoding="utf-8")
    match = re.search(r"body\s*\{[^}]*font-family:\s*([^;]+);", text, re.S)
    if not match:
        return
    first = match.group(1).split(",")[0].strip().strip("\"'")

    try:
        out = subprocess.run(
            ["fc-match", first], capture_output=True, text=True, timeout=10
        ).stdout
    except (FileNotFoundError, subprocess.SubprocessError):
        return  # no fontconfig — nothing to check against

    resolved = out.split('"')[1] if '"' in out else ""
    if resolved and first.lower() not in resolved.lower():
        print(f"  ! Font '{first}' is NOT installed — falling back to '{resolved}'")
        print("    The PDF will render, but not in the font you designed for.")
    else:
        print(f"  font: {resolved or first}")


def find_chrome():
    for path in CHROME_CANDIDATES:
        if Path(path).exists():
            return path
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No Chromium binary found — cannot render PDF.")


def render(html_path, pdf_path):
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as profile:
        result = subprocess.run(
            [
                chrome,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                f"--user-data-dir={profile}",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                html_path.resolve().as_uri(),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
    if not Path(pdf_path).exists():
        sys.exit(f"Chromium produced no PDF.\n{result.stderr[-1500:]}")


def report_embedded_fonts(pdf_path):
    """Name the fonts actually embedded in the PDF.

    `check_font` above asks fontconfig whether a face is installed, which is not
    the same question as whether Chromium used it. Bitstream Charter is installed
    here only as Type 1 (.pfb), and Chromium dropped Type 1 support — so it
    silently falls back to Liberation Serif and the fontconfig check still says
    everything is fine. That is exactly the failure this file was written to
    catch, so report what is in the PDF rather than what is on the system.
    """
    import re

    data = Path(pdf_path).read_bytes()
    fonts = sorted({m.decode() for m in re.findall(rb"/BaseFont\s*/([A-Za-z0-9+\-,_]+)", data)})
    # Chromium prefixes embedded subsets with six letters and a plus sign.
    families = sorted({f.split("+", 1)[-1] for f in fonts})
    if families:
        print(f"  embedded: {', '.join(families)}")
    if not any("Charter" in f for f in families):
        print("  ! Not set in Charter — Chromium fell back (Charter is Type 1 only here)")


def verify(pdf_path):
    """Extract the text back out and confirm the ATS-critical fields survived."""
    try:
        from pypdf import PdfReader
    except ImportError:
        print("  ! pypdf not installed — skipping verification (pip install pypdf)")
        return True

    reader = PdfReader(pdf_path)
    pages = len(reader.pages)
    text = "\n".join(p.extract_text() or "" for p in reader.pages)

    missing = [field for field in REQUIRED if field.lower() not in text.lower()]
    words = len(text.split())

    print(f"  pages: {pages}   extractable words: {words}")
    report_embedded_fonts(pdf_path)
    if pages > 2:
        print(f"  ! {pages} pages — trim to 1 (2 at the very most)")
    if words < 250:
        print("  ! Very little extractable text — the PDF may not be machine-readable")
    if missing:
        print(f"  ✗ NOT ATS-SAFE — missing from extracted text: {', '.join(missing)}")
        return False

    print("  ✓ ATS check passed — all key fields extractable")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="input HTML file")
    parser.add_argument("-o", "--output", type=Path, help="output PDF path")
    args = parser.parse_args()

    if not args.html.exists():
        sys.exit(f"No such file: {args.html}")

    pdf_path = args.output or args.html.with_suffix(".pdf")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Rendering {args.html} → {pdf_path}")
    check_font(args.html)
    render(args.html, str(pdf_path.resolve()))
    ok = verify(str(pdf_path))
    print(f"  {pdf_path}  ({pdf_path.stat().st_size // 1024} KB)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
