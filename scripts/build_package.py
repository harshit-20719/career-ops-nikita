#!/usr/bin/env python3
"""Build a self-contained application package: one HTML file per role.

    python3 scripts/build_package.py            # build every package
    python3 scripts/build_package.py ferty9     # build one

Each output file carries everything needed to apply — the route, the tailored
resume embedded as a downloadable PDF, the cover note with a copy button,
interview prep, and a pre-send checklist. No network, no external assets.

Open the file in a browser and the resume downloads. That only works from a
local file: a published artifact runs sandboxed and blocks page-initiated
downloads, data URIs included.

Role content lives in ROLES below. To add a role, add an entry and point
`resume` at its built PDF.
"""

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "applications" / "packages"

ROLES = {
    "ferty9": {
        "title": "Senior Manager / AGM — Strategy, CEO's Office",
        "company": "Ferty9 Fertility Center",
        "place": "Hyderabad",
        "tier": "Tier 1",
        "fit": "4.3", "odds": "4.0",
        "resume": "resume/build/Nikita-Sachanandani-Strategy-CEO-Office.pdf",
        "resume_name": "Nikita-Sachanandani-Strategy-CEO-Office.pdf",
        "verdict": "The best role on the board and the only surviving tier 1. The core of the job — deciding which markets and centres earn capital — is the geospatial ROI analysis you already built and ran at portfolio scale.",
        "route": [
            ("Send to", "ramya.kannuri@ferty9.com", True),
            ("Subject line", "Application - Strategy | CEO's Office", True),
            ("Required", "Write-up, max 300 words, on fit and unique value", False),
            ("Hiring principal", "Sukesh Chandra Gain, CEO — started July 2026", False),
            ("Backing", "Verlinvest. 11 centres across AP and Telangana", False),
        ],
        "route_note": "Use the subject line exactly — it is almost certainly a mail filter. Send Mon–Thu morning.",
        "letters": [
            ("Email body", [
                "Dear Ms. Kannuri,",
                "I'm applying for the Senior Manager / AGM role in the CEO's Office. My write-up is below and my CV is attached.",
                "Briefly: I currently manage a ₹450 crore ($51M) healthcare portfolio at Tata Trusts, where I built the geospatial ROI analysis that decided where our capital went across India. Deciding which markets and centres earn investment is the work I already do — I'd like to do it for a network that is actually expanding.",
                "Happy to share more detail at any point. Thank you for your time.",
                "Warm regards,<br>Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
            ("The 300-word write-up", [
                "When Ferty9 decides where its next centre goes, that is a geography-level capital allocation question — and it is the question I spent two years answering at Tata Trusts.",
                "I built a geospatial investment heat map covering every rupee the Trusts deployed across India, measuring how identical interventions produced materially different returns depending on geography and terrain. It shaped portfolio allocation from 2022 to 2024. Applied to a clinic network, the discipline is the same: which markets justify a centre, what returns to expect there, and where capital is better held back.",
                "The rest maps closely too. I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes, screening 30–50 proposals a month and taking recommendations directly to the CEO and Board. I assess founders and institutional leaders on whether they can genuinely execute and deploy capital — the same judgement a network applies to the doctors and partners it bets on. And I built the Trusts' climate-health vertical from nothing: the thesis, the first programmes, and the funding to stand it up. I know what it takes to start a line of business inside an organisation that did not previously have one.",
                "What I'd bring that is less common: I've evaluated healthcare delivery in the field, including in districts that barely appear on the map — not from a deck. I've assessed a district hospital and an AI diagnostics founder in the same month. That range means I can move between a clinical conversation and a growth model without a translator.",
                "I am deliberately moving from philanthropic capital into commercial healthcare, because I want the feedback loop that comes with it. Ferty9 — investor-backed, expanding, and a month into a new CEO — is where that decision compounds fastest.",
            ]),
        ],
        "questions": [
            ("\"Why leave Tata Trusts?\"", "Forward-looking, no criticism, 30 seconds. Full script in private/exit-narrative.md."),
            ("\"You've worked in philanthropy — why believe you'll adapt to a commercial P&amp;L?\"", "You already allocate capital against returns; you measured return as impact. The heat map <em>is</em> ROI analysis. Add Tiff.in unit economics as evidence you've modelled a commercial business."),
            ("\"How would you decide where we open our next centre?\"", "Almost certain, and it's your question. Demand and demographics, competitive density, doctor availability, referral catchment, payer mix, cannibalisation, payback period. Then say what you'd need to see before committing — the restraint is what separates a strategist from an analyst."),
            ("\"Current and expected compensation?\"", "The JD says compensation isn't a constraint, so don't anchor first. \"My current fixed is ₹16 lakh, which is a philanthropic-sector band rather than a market one. What range have you budgeted?\""),
        ],
        "ask": [
            "What does the CEO want to be true in 12 months that isn't true today?",
            "Is the growth thesis new centres, or more throughput from the existing eleven?",
            "How does Verlinvest's involvement shape the decision-making cadence?",
            "What's the hardest strategic call the leadership team is sitting on right now?",
        ],
        "checklist": [
            "Subject line matches exactly",
            "Resume attached, filename is your name",
            "Write-up under 300 words",
            "Checked LinkedIn for anyone at Ferty9, Verlinvest or Birla Fertility",
            "Tracker updated with a follow-up date 5 days out",
        ],
        "flags": [
            "CEO is one month in — ask what happened to his predecessor and what he's been asked to deliver.",
            "Verlinvest is a growth investor, so there's an exit horizon. Ask about the timeline being worked to.",
            "One Glassdoor review — culture is unassessable from outside. Ask to speak with someone in the CEO's office.",
            "India's ART Act reshaped compliance for fertility clinics. Informed questions here land well with a CEO from Birla Fertility.",
            "Fertility care is where commercial incentives meet patients at their most vulnerable. Form your view before you're inside being asked to grow the number.",
        ],
    },

    "entrepreneurs-first": {
        "title": "Talent Investor — Associate",
        "company": "Entrepreneurs First",
        "place": "Bengaluru",
        "tier": "Tier 2",
        "fit": "4.2", "odds": "3.0",
        "resume": "resume/build/Nikita-Sachanandani-Talent-Investor.pdf",
        "resume_name": "Nikita-Sachanandani-Talent-Investor.pdf",
        "verdict": "EF's entire model is judging whether someone can build before there's a company to diligence — which is the founder-assessment muscle you've been using for four years, and the one thing on your CV no consulting candidate can claim.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4422616061", True),
            ("Band", "0–4 years — you're at 4y2m, at the ceiling", False),
            ("Competition", "200+ applicants, most younger and cheaper", False),
            ("Requirements", "No degree requirement stated", False),
            ("Seniority", "Mid-Senior level, full-time, Bengaluru", False),
        ],
        "route_note": "Lead with judgement, not tenure — and don't open with healthcare. It's the least relevant fact about you here.",
        "letters": [
            ("Cover note", [
                "EF's bet is that you can identify who will build something before there is anything to diligence. I have spent four years doing the institutional version of that.",
                "At Tata Trusts I screen 30–50 proposals a month and take the survivors through three to four months of design work. The written proposal decides almost nothing. What decides it is the assessment I run on the people — whether a founder or programme lead actually understands their own constraint, whether they have the judgement to spend capital they have never had before, and whether their conviction survives contact with a field visit. I have backed people whose plans were weak and declined people whose decks were immaculate, and I have been right often enough to be trusted with a ₹450 crore portfolio at four years in.",
                "I know that is not the same as backing pre-idea technical founders. My universe is institutions and my sector is healthcare; yours is individuals and frontier technology. What transfers is the specific muscle — a mental model for exceptional operators built by making real decisions with real money behind them, and by seeing which of those decisions aged well.",
                "I am moving out of philanthropic capital deliberately, because I want the feedback loop that comes with commercial outcomes. Judging talent for a living, at the point where the judgement is the entire product, is the version of that I want most.",
            ]),
        ],
        "questions": [
            ("\"Tell me about someone you backed who others wouldn't have.\"", "The whole interview is this question in different clothes. Have two ready — one you backed against the grain that worked, one you declined despite a strong pitch. Name what you saw that the paper didn't."),
            ("\"How do you know your judgement is good?\"", "You have a feedback loop most people at your level don't — you see programmes run for years after the decision. Cite one where you were wrong and what changed in your model afterwards."),
            ("\"Why not stay in healthcare investing?\"", "Because the assessment skill is the part you want to do full-time, and healthcare is the domain you happened to learn it in."),
            ("\"You're at the top of our experience band.\"", "Don't apologise for it. Four years of deploying real capital means you arrive with a calibrated model rather than building one from scratch."),
        ],
        "ask": [
            "What separates the associates here whose judgement gets trusted fastest?",
            "How has the India cohort's founder profile changed over the last two years?",
            "What's the most common way you get a talent call wrong?",
            "How much of the role is sourcing versus advising once a founder is in?",
        ],
        "checklist": [
            "Read two or three EF founder stories, be able to name one specifically",
            "Two founder-judgement stories rehearsed — one backed, one declined",
            "Checked LinkedIn for anyone in EF's Bangalore cohort or team",
            "Cover note pasted, resume attached, tracker updated",
        ],
        "flags": [
            "Sector-agnostic and tech-weighted — your healthcare depth counts for less here than anywhere else on the board.",
            "\"Associate\" is a lateral title at best. The trajectory is the reason to take it, not the title.",
            "Intense, fast-paced, in-person in Bangalore. Confirm you're happy relocating from Mumbai before you invest in the process.",
        ],
    },

    "good-health": {
        "title": "Chief of Staff",
        "company": "Good Health Company",
        "place": "Hyderabad",
        "tier": "Tier 3 — best odds on the board",
        "fit": "3.6", "odds": "4.0",
        "resume": "resume/build/Nikita-Sachanandani-Chief-of-Staff.pdf",
        "resume_name": "Nikita-Sachanandani-Chief-of-Staff.pdf",
        "verdict": "The only posting scanned that states both its hours and its notice-period tolerance — and both fit you exactly. No degree gate, 4+ years wanted against your 4y2m, and a named recruiter reading applications.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4452364760", True),
            ("Recruiter", "Dhinesh M — message directly after applying", False),
            ("Requirements", "4+ years. No degree requirement", False),
            ("Hours", "10 AM – 7 PM, onsite 5 days. IST confirmed in the JD", False),
            ("Notice", "15–30 days accepted. Yours is 30", False),
            ("Reports to", "CEO. 181 applicants", False),
        ],
        "route_note": "Messaging the recruiter directly is worth more here than at any large employer on the list — a real human is reading.",
        "letters": [
            ("Cover note", [
                "A chief of staff role is mostly three things: deciding what the CEO should be looking at, making sure the thing that was decided actually happens, and being trusted with the parts of the business nobody else is allowed to see. I have been doing versions of all three for four years.",
                "At Tata Trusts I hold two mandates rather than one — Program Officer and Grants Manager — which is unusual on a fourteen-person team and is the closest thing to a chief of staff role the organisation has. I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes, prepare the analysis and dashboards the CEO and Board use to decide, and act as the financial gate on every partner budget in the health theme before anything reaches approval. I also built the geospatial ROI analysis that shaped where the Trusts deployed capital between 2022 and 2024 — the kind of work that only matters if someone acts on it, which is the test a CEO's office is judged by.",
                "What draws me to Good Health specifically is stage. You are past proving the model and into the part where operating discipline decides how far it scales, and a founder needs someone whose only job is holding the whole picture. I am also making a deliberate move from philanthropic capital into commercial healthcare — I want the feedback loop that comes with revenue rather than impact reports.",
                "Practically: I am serving a 30-day notice and can start accordingly, and I am ready to be in Hyderabad.",
            ]),
        ],
        "questions": [
            ("\"You've worked in philanthropy. This is a D2C business with revenue targets.\"", "You already allocate capital against returns, measured as impact. Say plainly you'll need to learn consumer unit economics fast, and cite Tiff.in as evidence you've modelled a commercial business."),
            ("\"Why a chief of staff role rather than a strategy role?\"", "Because you want the whole picture rather than one function — and you've already been doing the dual-mandate version of it."),
            ("\"Comfortable in Hyderabad, onsite, five days?\"", "Answer cleanly, no hedging. Hesitation reads as flight risk for a founder-adjacent hire."),
            ("\"What's your notice period?\" — expect this in the first five minutes", "\"30 days, and I'm already serving it.\" Their tolerance is 15–30 days, so this is a pass — but only if you say it without hesitating."),
        ],
        "ask": [
            "What does the CEO spend time on now that he shouldn't be?",
            "Which part of the business does the leadership team have least visibility into?",
            "Is the next phase about new categories or depth in the existing ones?",
            "What would make you say this hire worked, six months in?",
        ],
        "checklist": [
            "Use the product for twenty minutes before applying — a founder will notice",
            "Applied on LinkedIn, then messaged Dhinesh M directly",
            "Notice period stated up front — it's a screening question here",
            "Tracker updated",
        ],
        "flags": [
            "Series A, $15.2M raised, Khosla Ventures and Left Lane. Founded 2021 by Samarth Sindhi.",
            "D2C consumer health — hair, skin, weight, sexual health. Not health systems, which is exactly why fit scores 3.6.",
            "Be honest about the domain gap in the room. A founder will respect naming it more than pretending the domains are the same.",
            "Series A means less stability than Ferty9 and a smaller safety net. Worth weighing against the speed.",
        ],
    },
}

CSS = """
:root{--paper:#fbfcfb;--surface:#f1f5f4;--surface-2:#e7edeb;--ink:#0f1f1c;--ink-2:#3d514d;
--muted:#6b7d79;--line:#d9e2df;--line-strong:#b9c9c5;--accent:#0d6553;--accent-ink:#0a4c3e;
--accent-wash:#dcece7;--gold:#8a6410;--gold-wash:#f5ecd8}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0c1513;--surface:#131e1b;
--surface-2:#1a2724;--ink:#e6eeeb;--ink-2:#aebfba;--muted:#879994;--line:#243330;--line-strong:#334541;
--accent:#5cc2a8;--accent-ink:#8ad9c3;--accent-wash:#14302a;--gold:#d9ad5a;--gold-wash:#2e2617}}
:root[data-theme="dark"]{--paper:#0c1513;--surface:#131e1b;--surface-2:#1a2724;--ink:#e6eeeb;
--ink-2:#aebfba;--muted:#879994;--line:#243330;--line-strong:#334541;--accent:#5cc2a8;
--accent-ink:#8ad9c3;--accent-wash:#14302a;--gold:#d9ad5a;--gold-wash:#2e2617}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:820px;margin:0 auto;padding:40px 22px 90px}
h1,h2,h3{font-family:Georgia,"Iowan Old Style","Times New Roman",serif;text-wrap:balance}
h1{font-size:clamp(27px,4.2vw,38px);line-height:1.15;margin:0 0 8px;letter-spacing:-.015em}
h2{font-size:21px;margin:0;letter-spacing:-.01em}
h3{font-size:16px;margin:0 0 8px}
p{margin:0 0 12px}
.eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
header{border-bottom:1px solid var(--line);padding-bottom:22px;margin-bottom:8px}
.co{color:var(--ink-2);font-size:17px;margin:0}
.verdict{display:flex;align-items:center;gap:20px;margin-top:20px;background:var(--accent-wash);
border-radius:12px;padding:18px 20px;flex-wrap:wrap}
.scores{display:flex;gap:16px;flex:none}
.sc{text-align:center}
.sc b{display:block;font-family:Georgia,serif;font-size:32px;line-height:1;color:var(--accent-ink);font-variant-numeric:tabular-nums}
.sc span{display:block;font-size:9.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--accent-ink);opacity:.7;font-weight:700;margin-top:4px}
.verdict p{margin:0;color:var(--accent-ink);font-size:15px;flex:1 1 300px}
section{margin-top:34px}
.sec-head{display:flex;align-items:baseline;gap:12px;margin-bottom:15px;padding-bottom:9px;border-bottom:1px solid var(--line)}
.sec-head .n{font-size:12px;font-weight:700;color:var(--muted);letter-spacing:.08em;flex:none;font-variant-numeric:tabular-nums}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:20px}
.scroll{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:14.5px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}
td:first-child{white-space:nowrap;color:var(--muted);width:150px}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13.5px;word-break:break-all}
.dl{display:flex;gap:14px;align-items:center;flex-wrap:wrap;background:var(--surface);
border:1px solid var(--line);border-radius:12px;padding:18px 20px}
.dl-info{flex:1 1 240px}
.dl-info b{display:block;font-size:15px}
.dl-info span{font-size:13.5px;color:var(--muted)}
a.btn,button.btn{font:inherit;font-size:14px;font-weight:600;cursor:pointer;background:var(--accent);
color:#fff;border:0;border-radius:8px;padding:10px 18px;text-decoration:none;display:inline-block}
a.btn:hover,button.btn:hover{opacity:.87}
a.btn:focus-visible,button.btn:focus-visible{outline:2px solid var(--accent-ink);outline-offset:2px}
button.ghost{background:transparent;color:var(--accent-ink);border:1px solid var(--line-strong)}
iframe.pv{width:100%;height:800px;border:1px solid var(--line);border-radius:10px;margin-top:14px;background:#fff}
.block{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--surface);margin-bottom:14px}
.block-top{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:11px 16px;
background:var(--surface-2);border-bottom:1px solid var(--line)}
.block-top .label{font-size:12px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2)}
.block-body{padding:18px;font-size:15px}
.block-body p:last-child{margin-bottom:0}
button.copy{font:inherit;font-size:12.5px;font-weight:600;cursor:pointer;background:var(--accent);
color:#fff;border:0;border-radius:7px;padding:6px 13px}
button.copy:hover{opacity:.85}
.count{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
.qa{border-left:2px solid var(--line-strong);padding-left:15px;margin-bottom:15px}
.qa:last-child{margin-bottom:0}
.qa .q{font-weight:650;margin-bottom:4px}
.qa .a{color:var(--ink-2);font-size:14.5px;margin:0}
ul,ol{margin:0;padding-left:20px}
li{margin-bottom:8px}
li:last-child{margin-bottom:0}
.check{list-style:none;padding:0}
.check li{display:flex;gap:11px;align-items:flex-start}
.check input{margin-top:4px;accent-color:var(--accent);width:16px;height:16px;flex:none}
.note{font-size:14px;color:var(--muted)}
.flags{background:var(--gold-wash);border-radius:12px;padding:18px 20px;font-size:14.5px}
.flags li{color:var(--gold)}
.flags li span{color:var(--ink-2)}
footer{margin-top:46px;padding-top:20px;border-top:1px solid var(--line);font-size:13.5px;color:var(--muted)}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""


def build(key, role):
    pdf_path = ROOT / role["resume"]
    if not pdf_path.exists():
        sys.exit(f"Missing resume PDF for {key}: {pdf_path}")
    b64 = base64.b64encode(pdf_path.read_bytes()).decode()
    kb = len(pdf_path.read_bytes()) // 1024

    rows = "".join(
        '<tr><td>{}</td><td{}>{}</td></tr>'.format(
            k, ' class="mono"' if mono else "", v
        )
        for k, v, mono in role["route"]
    )

    letters = ""
    for i, (label, paras) in enumerate(role["letters"]):
        body = "".join(f"<p>{p}</p>" for p in paras)
        letters += (
            f'<div class="block"><div class="block-top"><span class="label">{label}</span>'
            f'<span style="display:flex;gap:12px;align-items:center">'
            f'<span class="count" id="wc{i}"></span>'
            f'<button class="copy" data-target="L{i}">Copy</button></span></div>'
            f'<div class="block-body" id="L{i}">{body}</div></div>'
        )

    qa = "".join(
        f'<div class="qa"><p class="q">{q}</p><p class="a">{a}</p></div>'
        for q, a in role["questions"]
    )
    ask = "".join(f"<li>{q}</li>" for q in role["ask"])
    checks = "".join(
        f'<li><input type="checkbox" id="c{i}"><label for="c{i}">{c}</label></li>'
        for i, c in enumerate(role["checklist"])
    )
    flags = "".join(f"<li><span>{f}</span></li>" for f in role["flags"])

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{role['company']} — Application Package</title>
<style>{CSS}</style></head><body>
<div class="wrap">

<header>
  <p class="eyebrow">Application package · {role['tier']}</p>
  <h1>{role['title']}</h1>
  <p class="co">{role['company']} · {role['place']}</p>
  <div class="verdict">
    <div class="scores">
      <div class="sc"><b>{role['fit']}</b><span>fit</span></div>
      <div class="sc"><b>{role['odds']}</b><span>odds</span></div>
    </div>
    <p>{role['verdict']}</p>
  </div>
</header>

<section>
  <div class="sec-head"><span class="n">01</span><h2>Resume</h2></div>
  <div class="dl">
    <div class="dl-info">
      <b>{role['resume_name']}</b>
      <span>Tailored to this JD · one page · ATS verified · {kb} KB</span>
    </div>
    <a class="btn" download="{role['resume_name']}" href="data:application/pdf;base64,{b64}">Download resume</a>
    <button class="btn ghost" id="pv">Preview</button>
  </div>
  <div id="pvhost"></div>
</section>

<section>
  <div class="sec-head"><span class="n">02</span><h2>How to apply</h2></div>
  <div class="card scroll"><table>{rows}</table></div>
  <p class="note" style="margin-top:11px">{role['route_note']}</p>
</section>

<section>
  <div class="sec-head"><span class="n">03</span><h2>What to send</h2></div>
  {letters}
</section>

<section>
  <div class="sec-head"><span class="n">04</span><h2>They will ask</h2></div>
  <div class="card">{qa}</div>
</section>

<section>
  <div class="sec-head"><span class="n">05</span><h2>Ask them</h2></div>
  <div class="card"><ol>{ask}</ol>
  <p class="note" style="margin:14px 0 0">Hold two back for a later round — they will ask again.</p></div>
</section>

<section>
  <div class="sec-head"><span class="n">06</span><h2>Know before the interview</h2></div>
  <div class="flags"><ul>{flags}</ul></div>
</section>

<section>
  <div class="sec-head"><span class="n">07</span><h2>Before you send</h2></div>
  <div class="card"><ul class="check">{checks}</ul></div>
</section>

<footer>
  Scored against applications/RUBRIC.md, from the full job description. Built 13 Aug 2026.
  The resume is embedded in this file — it downloads with no network connection.
</footer>

</div>
<script>
var PDF = "data:application/pdf;base64,{b64}";
document.getElementById("pv").addEventListener("click", function () {{
  var host = document.getElementById("pvhost");
  if (host.firstChild) {{ host.innerHTML = ""; this.textContent = "Preview"; return; }}
  var f = document.createElement("iframe");
  f.className = "pv"; f.src = PDF; f.title = "Resume preview";
  host.appendChild(f); this.textContent = "Hide preview";
}});
document.querySelectorAll("button.copy").forEach(function (b) {{
  b.addEventListener("click", function () {{
    var el = document.getElementById(b.dataset.target);
    var t = Array.from(el.querySelectorAll("p")).map(function (p) {{ return p.innerText.trim(); }}).join("\\n\\n");
    navigator.clipboard.writeText(t).then(function () {{
      var w = b.textContent; b.textContent = "Copied";
      setTimeout(function () {{ b.textContent = w; }}, 1800);
    }});
  }});
}});
document.querySelectorAll('[id^="wc"]').forEach(function (el) {{
  var src = document.getElementById("L" + el.id.slice(2));
  if (src) el.textContent = src.innerText.trim().split(/\\s+/).length + " words";
}});
</script>
</body></html>"""


def main():
    keys = sys.argv[1:] or list(ROLES)
    OUT.mkdir(parents=True, exist_ok=True)
    for k in keys:
        if k not in ROLES:
            sys.exit(f"Unknown role '{k}'. Known: {', '.join(ROLES)}")
        path = OUT / f"{k}-package.html"
        path.write_text(build(k, ROLES[k]), encoding="utf-8")
        print(f"  {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
