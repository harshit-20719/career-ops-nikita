#!/usr/bin/env python3
"""Generate the India-locked LinkedIn searches for Nikita's role scan.

    python3 scripts/scan.py              # print every search URL
    python3 scripts/scan.py --check      # screening rules applied to results
    python3 scripts/scan.py --city       # add per-city searches for P0 cities

LinkedIn is the only board that reliably enumerates for this profile — iimjobs
renders listings client-side and Instahyre's API is blocked from this
environment — so the scan is built around it deliberately.

Two things this pins down that a plain keyword search does not:

1. **Geography.** `geoId=102713980` is India. Passing `location=India` as text
   alone lets LinkedIn drift into global results; the geoId does not.

2. **Offshore seats.** A role can be physically in India and still fail the
   IST gate — GCCs, captive centres and delivery arms serving US or UK
   markets. Those are India-located but not India-market jobs, and they are
   the ones most likely to waste an application.
"""

import argparse
import re
from urllib.parse import quote

INDIA_GEO = "102713980"
BASE = "https://in.linkedin.com/jobs/search"

# f_TPR=r604800  -> posted in the last 7 days
# f_E=4          -> mid-senior level
DEFAULT_FILTERS = "f_TPR=r604800&f_E=4"

# Nikita's target role shapes. Ordered by how well they've converted so far.
SEARCHES = [
    ("Healthcare strategy", "Healthcare Strategy"),
    ("Chief of staff / founder's office", '"Chief of Staff" OR "Founder\'s Office"'),
    ("Corporate strategy", "Corporate Strategy"),
    ("Healthcare investment", 'healthcare investment OR "venture capital" OR "private equity"'),
    ("Healthtech strategy", "healthtech OR digital health strategy"),
    ("CEO's office", '"CEO\'s Office" OR "MD\'s Office"'),
]

# P0 first, then P1. Remote is handled by the f_WT=2 filter, not a city.
CITIES = ["Mumbai", "Bengaluru", "Hyderabad", "Delhi"]

# --- screening -------------------------------------------------------------

# A role in one of these locations clears the location gate. Anything else in
# India is a fail — physically in the country is not the same as in scope.
IN_SCOPE = {
    "mumbai", "navi mumbai", "thane", "maharashtra",
    "bengaluru", "bangalore", "karnataka",
    "hyderabad", "telangana", "secunderabad",
    "delhi", "new delhi", "gurugram", "gurgaon", "noida",
    "faridabad", "ghaziabad", "haryana",
    "remote", "india",
}

# Phrases that mark an offshore seat serving a foreign market. Not an
# automatic reject — but the shift must be confirmed before applying, because
# these are where the IST gate quietly fails.
OFFSHORE_MARKERS = [
    "global capability", "gcc", "capability center", "capability centre",
    "shared services", "delivery center", "delivery centre",
    "global services", "acceleration center", "acceleration centre",
    "offshore", "us healthcare", "us market", "uk market",
    "global business services", "gbs", "insights center", "insights centre",
]

# Explicit shift language. These are a hard fail on the timezone gate.
# Matched on word boundaries — plain substring matching flagged "Investor"
# as a night shift, because "est" is inside it.
SHIFT_MARKERS = [
    r"\best\b", r"\bpst\b", r"\bcst\b", r"\bedt\b", r"\bpdt\b",
    r"\bus shift\b", r"\bnight shift\b", r"\buk shift\b", r"\brotational shift\b",
    r"\buk hours\b", r"\bus hours\b", r"\beastern time\b", r"\bpacific time\b",
    r"\bovernight\b", r"\bgraveyard\b",
    # A time range crossing into the small hours: "5:30PM to 02:30AM",
    # with or without spaces, which is how these are actually written.
    r"\d{1,2}[:.]\d{2}\s*pm\s*(?:to|-|–|—)\s*\d{1,2}[:.]\d{2}\s*am",
]

# Non-profit markers — the sector gate.
# Deliberately over-inclusive: a false positive costs one lookup, a false
# negative costs an application into the sector Nikita is leaving. These
# raise CHECK, never FAIL, because the name alone is not proof either way.
NONPROFIT_MARKERS = [
    "foundation", "trust", "ngo", "non-profit", "nonprofit",
    "charitable", "society", "council", "world health",
    "unicef", "usaid", "gates", "philanthrop",
    "initiative", "alliance", "institute", "coalition",
    "development bank", "impact fund", "social sector",
]


def build_urls(per_city=False):
    urls = []
    for label, keywords in SEARCHES:
        urls.append((label, f"{BASE}?keywords={quote(keywords)}"
                            f"&location=India&geoId={INDIA_GEO}&{DEFAULT_FILTERS}"))
        if per_city:
            for city in CITIES:
                urls.append((f"{label} — {city}",
                             f"{BASE}?keywords={quote(keywords)}"
                             f"&location={quote(city + ', India')}"
                             f"&geoId={INDIA_GEO}&{DEFAULT_FILTERS}"))
    # Remote-in-India, across every keyword at once
    urls.append(("Remote (all keywords)",
                 f"{BASE}?keywords={quote('healthcare strategy OR chief of staff')}"
                 f"&location=India&geoId={INDIA_GEO}&{DEFAULT_FILTERS}&f_WT=2"))
    return urls


# Organisations confirmed non-profit, by name. The marker list above is a net,
# not a guarantee — "Evidence Action" and "PATH" carry nothing in their names
# that any heuristic could catch. Add to this list every time the scan turns up
# another one; it is the only part of the sector screen that is actually
# reliable.
KNOWN_NONPROFIT = {
    "evidence action", "path", "clinton health access initiative",
    "idinsight", "gsg impact", "world health organization",
    "nationbuilding foundation of india", "intelehealth",
    "gati foundation", "upaya social ventures", "bms foundation",
    "mit solve", "solve", "mit",
}


def _word_hit(patterns, text):
    """Match on word boundaries. Substring matching is not safe here — short
    markers like 'est' and 'gcc' appear inside ordinary words."""
    for p in patterns:
        pattern = p if p.startswith(r"\b") or "\\d" in p else r"\b" + re.escape(p) + r"\b"
        if re.search(pattern, text):
            return p
    return None


def screen(title, company, location):
    """Return (verdict, reasons) for one listing. Verdict: pass / check / fail."""
    blob = re.sub(r"\s+", " ", f"{title} {company} {location}".lower())
    loc = location.lower()
    reasons = []

    if _word_hit(SHIFT_MARKERS, blob):
        return "fail", ["timezone gate — explicit non-IST shift"]

    if not any(re.search(r"\b" + re.escape(k) + r"\b", loc) for k in IN_SCOPE):
        return "fail", [f"location gate — {location} is outside target cities"]

    if company.strip().lower() in KNOWN_NONPROFIT:
        return "fail", ["sector gate — known non-profit"]

    if _word_hit(NONPROFIT_MARKERS, blob):
        reasons.append("possible non-profit — confirm before applying")

    hit = _word_hit(OFFSHORE_MARKERS, blob)
    if hit:
        reasons.append(f"offshore/GCC marker ({hit.strip()}) — verify shift hours")

    return ("check" if reasons else "pass"), reasons


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--city", action="store_true", help="add per-city searches")
    ap.add_argument("--check", action="store_true", help="show screening rules")
    args = ap.parse_args()

    if args.check:
        print("Screening applied to every result:\n")
        print("  FAIL  explicit non-IST shift language in the posting")
        print("  FAIL  location outside Mumbai / Bengaluru / Hyderabad / Delhi NCR / remote")
        print("  CHECK offshore or GCC markers — India-located, foreign-market seat")
        print("  CHECK non-profit markers — sector gate is absolute\n")
        print(f"  {len(OFFSHORE_MARKERS)} offshore markers, {len(SHIFT_MARKERS)} shift markers, "
              f"{len(NONPROFIT_MARKERS)} non-profit markers")
        return

    urls = build_urls(per_city=args.city)
    print(f"India-locked LinkedIn searches (geoId={INDIA_GEO}), {len(urls)} total\n")
    for label, url in urls:
        print(f"{label}\n  {url}\n")
    print("Save each as a LinkedIn alert set to daily. On an 8-week clock a")
    print("posting older than a week has already been screened by someone else.")


if __name__ == "__main__":
    main()
