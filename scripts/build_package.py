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

    "hospipal": {
        "title": "Founding Growth &amp; Business Lead — Zero to One",
        "company": "HospiPal.Health",
        "place": "Mumbai / Thane · hybrid",
        "tier": "Best odds on the board",
        "fit": "3.7", "odds": "4.0",
        "resume": "resume/build/Nikita-Sachanandani-Founding-Growth.pdf",
        "resume_name": "Nikita-Sachanandani-Founding-Growth.pdf",
        "verdict": "They ask for a story, not a CV — which is the rarest hiring instruction on the board and the one you can win on. Of 114 applicants, most will attach a resume and lose. Note the honest trade: this is a growth and operations job at a bootstrapped ten-person company, so the portfolio work is not what gets you in. Tiff.in is.",
        "route": [
            ("Email", "contact@hospipalhealth.com", True),
            ("Or WhatsApp", "+91 99872 49625", True),
            ("Posting", "linkedin.com/jobs/view/4450461460", True),
            ("They ask for", "One thing you built from nothing — including if it failed", False),
            ("And for", "Why you'd trade a safe job for this", False),
            ("Band", "3–5 years building from scratch. You're at 4y2m", False),
            ("Healthcare", "Explicitly not required", False),
            ("Competition", "114 applicants, posted 13 Aug", False),
        ],
        "route_note": "\"Do not send just a CV.\" Take that literally — the email below <em>is</em> the application, and the resume is an attachment they may never open. Send it Monday, before the pile grows.",
        "letters": [
            ("Email — subject: The thing I built from nothing", [
                "Hi — this is for the Founding Growth &amp; Business Lead role. You asked for one thing I built from nothing rather than a CV, so here it is.",
                "In 2021 I co-founded Tiff.in, incubated at Ashoka University — 3 of 35 teams got funded and we were one of them. I did the commercial side: market sizing, unit economics, the financial model, and the pitch. Then I did the unglamorous half, which was actually getting people to find us. We grew YouTube views 520% and Instagram followers 370% across four channels, by testing far more things than worked. What I learned is the part that's relevant to you: distribution is not a campaign, it's a loop you run until the numbers move, and most of what you try will not move them.",
                "It also didn't become a large company, and I'd rather say that plainly than let a growth number imply otherwise.",
                "Since then I've spent four years at Tata Trusts on the healthcare portfolio, where I originated and closed 15+ institutional partnerships from a standing start — finding the target, getting the first meeting, and closing the terms myself — and built programmes end-to-end from an idea to something that ran without me. I've also spent a lot of time inside Indian hospitals and district health systems, watching what actually happens to families around an admission. Your description of the problem — that nobody owns what happens after the patient leaves — is not an abstraction to me.",
                "Why I'd trade a safe job for this: because at the Trusts I make recommendations and someone else lives with the consequences. The feedback loop is years long and heavily mediated. I want to own a number, find out weekly whether I was right, and be the person who fixes the thing nobody else will. That's the whole reason I'm looking, and it's why a founding role at a company that is small and already earning is more interesting to me than a bigger title somewhere settled.",
                "Happy to talk whenever suits. CV attached if it's useful, though I take your point about it.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"You've managed a ₹450 crore portfolio. Why would you want this?\"", "The honest answer, and don't dress it up: scale of capital isn't the same as ownership of an outcome. Say you've been recommending and monitoring, and you want to be the one running the loop. Do <em>not</em> lead with the portfolio figure in this room — it makes you sound expensive and over-titled for a ten-person company."),
            ("\"Have you ever run performance marketing?\"", "No, and say so in one sentence rather than stretching Tiff.in into something it wasn't. Then say what you have done: acquisition experiments across four channels, unit economics, and cost-per-beneficiary modelling across a 40-programme portfolio, which is CAC by another name. Offer to walk through how you'd instrument a WhatsApp funnel."),
            ("\"What would you do in your first 30 days?\"", "Certain to come. Don't present a plan — present what you'd need to learn first. Where the last 100 customers actually came from, what a lead costs today if anyone knows, where families drop out of the WhatsApp conversation, and which hospitals already refer informally. Then one channel test, not five."),
            ("\"Compensation?\"", "They've said openly it's a conversation once there's fit, and they're bootstrapped. Expect this to come in below your current fixed. Ask what band they've set and what the equity looks like in writing — for a founding title at a bootstrapped company, the equity is the actual offer."),
        ],
        "ask": [
            "Where did your last hundred customers come from, and do you know which channel?",
            "What's the honest split of your revenue between hospital companionship and home recovery?",
            "Do hospitals refer you already, and if so is anyone owning that relationship?",
            "You've said bootstrapped and deliberately small — what would make you raise?",
            "What does the word \"founding\" mean here in equity terms?",
        ],
        "checklist": [
            "Email is the application — resume attached second, not first",
            "The Tiff.in story names what didn't work, not only the growth numbers",
            "Portfolio figure kept out of the opening — it reads as over-titled here",
            "Sent Monday–Wednesday morning; WhatsApp follow-up only after 4 working days",
            "Tracker updated with a follow-up date",
        ],
        "flags": [
            "Bootstrapped, 1–10 people, no external funding. There is no runway conversation to have — the runway is revenue. Ask what monthly revenue looks like before you resign anything.",
            "LinkedIn tags this <b>Entry level</b> while the JD says founding lead. That mismatch is either a posting error or a signal about the band. Resolve it early rather than at offer stage.",
            "This is a labour-operations business — trained companions, nurses, attendants — not a software business. Growth here means recruiting and quality-controlling humans as much as running channels.",
            "\"Hybrid, open to relocation as the role grows\" is doing quiet work. Confirm what onsite actually means week to week before you accept.",
            "Care for families at their most vulnerable, sold as a paid service. Form your view on how that gets priced and marketed before you're the one owning the growth number.",
        ],
    },

    "clinikally": {
        "title": "Chief of Staff",
        "company": "Clinikally (YC S22)",
        "place": "Gurugram",
        "tier": "Substituted role — see note",
        "fit": "3.6", "odds": "3.7",
        "resume": "resume/build/Nikita-Sachanandani-Chief-of-Staff-Clinikally.pdf",
        "resume_name": "Nikita-Sachanandani-Chief-of-Staff.pdf",
        "verdict": "The role in your tracker — Manager, Category &amp; Retail Expansion — does not exist on Clinikally's board. This is the substitute, and it's a better job than the one you lost: Chief of Staff to the founder, 125-person YC healthtech, comp band published at ₹15–24 lakh. The JD asks for investor communications and cross-functional launches, which is the Board-facing half of your current job.",
        "route": [
            ("Apply at", "ycombinator.com/companies/clinikally/jobs/bq21ts8-chief-of-staff", True),
            ("Founder / CEO", "Arjun Soin — you report to him", False),
            ("Posted band", "₹1.5M – ₹2.4M (₹15–24 lakh)", False),
            ("Bar", "\"At least 2 years in consulting, IB, VC or a high-growth startup\"", False),
            ("Company", "Founded 2022 · YC S22 · 125 people", False),
            ("What they do", "Dermatology, nutrition and wellness — telehealth, AI treatment plans, Rx-grade products", False),
            ("Location", "Gurugram, onsite. Relocation from Mumbai", False),
        ],
        "route_note": "Applying through the YC board goes to the founding team, not an ATS queue. Use the product first — it's a consumer telehealth flow and takes ten minutes.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Chief of Staff role. The short version of why: the part of my current job that looks most like this one is the part I want more of.",
                "At Tata Trusts I hold two mandates rather than one — Program Officer and Grants Manager — on a fourteen-person health team. Practically that means I prepare the analysis, briefs and dashboards the CEO and Board use to decide, I act as the financial gate on every partner budget in the health theme before anything reaches approval, and I run the cross-functional work that turns a decision into something that actually happened. I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes, and I built the geospatial ROI analysis that shaped where that capital went between 2022 and 2024.",
                "Your JD asks for someone who prepares investor communications, leads cross-functional initiatives and product launches, and finds the operational bottleneck nobody has named yet. I've been doing the institutional version of all three. What I haven't done is a consumer P&amp;L, and I'd rather say that up front than let a portfolio number stand in for it — I'd be learning your unit economics quickly, and I've modelled a commercial business before, at Tiff.in, which I co-founded out of Ashoka University's incubator.",
                "What draws me to Clinikally specifically is that the hard problem is a real one: dermatology is where telehealth, prescription compliance and consumer retail all collide, and getting AI treatment plans to hold up against Rx-grade standards is not a marketing problem. I've spent four years deciding which health technologies were ready to be trusted and which weren't, so I'd arrive with a view rather than an opinion.",
                "I'm on a 30-day notice and ready to be in Gurugram.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"Your bar says consulting, IB, VC or high-growth startup. You've been at a philanthropy.\"", "The one question that decides this application. Answer it structurally, not defensively: screening 30–50 proposals a month, diligence on the people behind them, structuring terms, deploying capital, monitoring a portfolio, reporting to a board. Name the pipeline, then say plainly that the wrapper was philanthropic and the work was not."),
            ("\"What would you do in your first 90 days?\"", "For a CoS the answer is not a plan, it's a diagnosis. Say you'd spend the first weeks working out which decisions are actually stuck and why — whether it's missing data, an unowned handoff, or no one having the authority — and that you'd bring back a list of three, ranked, rather than a strategy deck."),
            ("\"Have you written investor updates?\"", "Not to VCs. You've written Board and CEO material for the Tata principals, which is a comparable audience with a lower tolerance for spin. Offer to show the structure you use — the honest version of a bad quarter is the part that transfers."),
            ("\"Why leave now?\"", "Forward-looking, 30 seconds, no criticism of the Trusts. Full script in private/exit-narrative.md."),
        ],
        "ask": [
            "What does Arjun spend time on today that he shouldn't?",
            "Which decision has been open longest, and what's actually blocking it?",
            "How much of the next phase is new categories versus depth in dermatology?",
            "You're 125 people and three years in — what broke most recently as you scaled?",
            "What would make you say this hire worked, six months in?",
        ],
        "checklist": [
            "Used the Clinikally product end-to-end before applying",
            "Read the founder's public posts — this is a founder-adjacent hire, he will notice",
            "\"Investment work in a philanthropic wrapper\" rehearsed as one clean paragraph",
            "Confirmed you're genuinely willing to relocate to Gurugram before applying",
            "Checked LinkedIn for anyone at Clinikally or in the YC S22 batch",
            "Tracker updated with a follow-up date 5 days out",
        ],
        "flags": [
            "The role you were tracking is gone. Also open and worth knowing about: VP of Growth, VP of Brand Marketing, Head of Category &amp; Brand Management. The last of these is the closest to your old tracked role but wants e-commerce or e-pharmacy category experience and treats a B.Pharm as a significant advantage — it's a worse fit than this one.",
            "The posted band tops out at ₹24 lakh. That's a real number, published, which is rare — and it sets the ceiling of the conversation before you start.",
            "YC S22, founded 2022, 125 people. Ask directly about the last raise and current runway; a company hiring three VPs at once is either scaling or replacing.",
            "Dermatology D2C sits close to the line where healthcare becomes cosmetics. Ask how prescription decisions are governed and who signs off on the AI treatment plans.",
            "Gurugram onsite means relocating from Mumbai. Weigh that before you invest in the process, not after an offer.",
        ],
    },

    "indegene": {
        "title": "Associate Manager — Digital Strategy &amp; Solutions",
        "company": "Indegene",
        "place": "Bengaluru",
        "tier": "Weakest of the three — apply only if the week has room",
        "fit": "3.2", "odds": "2.4",
        "resume": "resume/build/Nikita-Sachanandani-Digital-Strategy.pdf",
        "resume_name": "Nikita-Sachanandani-Digital-Strategy.pdf",
        "verdict": "Verified against the live JD, and the honest read is that this is a pre-sales and solutioning job wearing a strategy title. The core of it — RFPs, solution packaging, proposal narratives — is work you have never done, and you'd enter at the floor of a 4–12 year band against 200+ applicants. It clears every gate and the AI mandate is real, so it's worth an hour. It is not worth three.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4451105287", True),
            ("Job poster", "Saptarshi Munshi, Talent Acquisition — message after applying", False),
            ("Band", "4–12 years. You're at 4y2m, at the floor", False),
            ("Degree", "MBA or Engineering preferred — not required", False),
            ("Competition", "200+ applicants, posted 10 Aug", False),
            ("Company", "Listed healthcare-technology services provider, ~5,000 people", False),
            ("Clients", "Global life sciences — verify the shift before you accept", False),
        ],
        "route_note": "Messaging Saptarshi directly after applying is the only lever that moves the odds here; a named recruiter on a 200-applicant post is worth using.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Associate Manager role in Digital Strategy &amp; Solutions. I'll be direct about where I fit and where I don't, because the JD is specific.",
                "Where I fit: the role is about taking an ambiguous client problem and turning it into a scoped solution, a roadmap, and a narrative a senior audience will act on. At Tata Trusts I manage a ₹450 crore ($51M) healthcare portfolio and run that cycle continuously — 30–50 proposals screened a month, then two to three months of structured design work per programme, mapping dependencies across clinical, government and technology stakeholders, then a brief that goes to the CEO and Board. The output is judged the same way yours is: whether the person on the other side of the table can act on it.",
                "On the AI part of the mandate, I'm not coming to it cold. Health-tech and AI diagnostics are sub-themes I own. I've evaluated AI diagnostic tools and the teams building them on technical maturity, deployment readiness and evidence quality, and I've structured technology pilots under a deliberately heavier evidence bar — choosing the conditions and geographies that would actually test the claim rather than flatter it. Data readiness, governance and human oversight are the questions I ask for a living.",
                "Where I don't fit, stated plainly: I have not run an RFP, packaged a service offering, or worked in pre-sales. If that's the non-negotiable core of the role, I'm the wrong candidate and I'd rather you know now. If it's learnable by someone who can structure a problem and write for executives, I'd back myself to pick it up quickly.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"Walk me through an RFP you've responded to.\"", "You can't, and inventing one here is the failure mode that ends the process. Say so, then substitute the closest real thing: a partner proposal you scoped, costed, negotiated and defended to a board. Ask what their proposal cycle actually looks like — curiosity beats a stretched answer."),
            ("\"What's your experience with pharma commercial — CRM, marketing automation, content ops?\"", "Thin, and they'll probe it. Don't bluff. Your healthcare depth is delivery, diagnostics and public health, not pharma brand marketing. Name the gap and pivot to the transferable half: regulated-industry judgement and evidence standards."),
            ("\"You're at four years in a 4–12 band.\"", "Don't apologise. Four years of allocating real capital with board accountability is not four years of execution. Say what you've owned, not how long you've owned it."),
            ("\"What are the shift timings?\" — <em>you</em> ask this, in the first call", "Indegene serves global life sciences clients. The posting says nothing about hours. Ask before you invest a round: which client regions this team covers, and what the working window actually is. This is your hard gate and it is unverified."),
        ],
        "ask": [
            "Which client regions does this team cover, and what does the working day look like?",
            "Is this role closer to pre-sales or to delivery once an engagement is won?",
            "What proportion of the AI and agentic work is live with clients versus still being packaged?",
            "The band is 4 to 12 years — what does the person you hire at the lower end look like?",
            "How does someone move from Associate Manager to Manager here, and on what timeline?",
        ],
        "checklist": [
            "Shift hours asked about in the first conversation — this is the unverified gate",
            "RFP gap named in the cover note rather than discovered in the interview",
            "Applied on LinkedIn, then messaged Saptarshi Munshi directly",
            "One AI-diagnostics evaluation story ready with the evidence standard you applied",
            "Tracker updated — and if the week is full, this is the one to drop",
        ],
        "flags": [
            "Timezone is the open gate. A listed services firm serving global pharma is exactly the shape that fails IST quietly. Do not accept anything before this is answered in writing.",
            "\"Associate Manager\" at a 5,000-person services firm is close to a lateral. The trajectory argument is a defined ladder, not a jump.",
            "A separate US-based Indegene digital strategy posting has already closed after seven months open. Long-open roles in this function suggest either a high bar or high churn — worth asking about the predecessor.",
            "Services businesses bill by the hour. Ask what utilisation expectations look like, because that is the real answer to what the job is.",
            "Preferred qualifications lean MBA and consulting. You have neither and the JD says preferred, not required — but assume the shortlist is full of them.",
        ],
    },

    "iqvia": {
        "title": "Senior Consultant — Healthcare Strategy (Indian Market)",
        "company": "IQVIA India",
        "place": "Mumbai · hybrid",
        "tier": "Highest fit found this week",
        "fit": "4.2", "odds": "2.0",
        "resume": "resume/build/Nikita-Sachanandani-Healthcare-Consulting.pdf",
        "resume_name": "Nikita-Sachanandani-Healthcare-Consulting.pdf",
        "verdict": "FIT 4.2 puts this level with Entrepreneurs First and just behind Ferty9 — and unlike either, it's healthcare strategy, in Mumbai, hybrid, with the timezone answered in the job title. The odds are the worst on the board: they want 6–8 years and you have 4y2m. The rubric is explicit about this case — apply anyway, then put the effort into a referral rather than into more applications.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4448826527", True),
            ("The team", "IQVIA's <b>healthcare strategy practice</b>, inside Consulting Services", False),
            ("Which entity", "IQVIA Consulting &amp; Information Services India Pvt Ltd — the former IMS Health business", False),
            ("The office", "Supreme Business Park, Hiranandani Gardens, Powai, Mumbai", False),
            ("Who's hiring", "<b>Nobody is named on the posting.</b> No job poster, no recruiter — see the note below", False),
            ("Experience asked", "6–8 years. You have 4y2m — this is the gap", False),
            ("Education", "Tier-1 B-school / IIT, marked <em>preferred</em>, not required", False),
            ("Mode", "Hybrid, Mumbai — no relocation, and the only hybrid role on your board", False),
            ("Timezone", "\"Indian Market\" is in the job title. Gate answered", False),
            ("Must-have skills", "Commercial, growth, GTM, brand, portfolio strategy, market expansion", False),
            ("Competition", "200+ applicants, posted 4 Aug", False),
        ],
        "route_note": "<b>The absence of a named contact is the finding.</b> Every other role on your board this week had someone attached — Voy had an HR specialist, Indegene a talent lead, Good Health a recruiter. This one has nobody, which means it goes into an ATS and gets filtered on the six-to-eight-year line before a human reads it. That is why the referral is not optional here. A cold application at a two-year deficit into 200+ people is close to a lottery ticket; one hour finding an IQVIA India consultant through the Young India Fellowship network changes the odds more than everything else in this file combined.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Senior Consultant role in the healthcare strategy practice. I'll be straight about the experience line first: you've asked for six to eight years and I have just over four. I'm applying because the work itself is what I already do, and I'd rather make that case than not make it.",
                "Your must-have list is portfolio strategy, market expansion, growth strategy and commercial strategy. At Tata Trusts I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes, and the analytical spine of that job is the same one: I built a geospatial ROI and market heat map across Indian states, showing how identical interventions produced materially different returns by geography and terrain, and it shaped where capital went from 2022 to 2024. That is a market-expansion and prioritisation analysis; the currency happened to be philanthropic rather than commercial.",
                "The delivery rhythm is also familiar. I screen 30–50 proposals a month using structured triage, run deep-dive analysis on what survives, and take recommendations to the CEO and the Board — an audience with a low tolerance for a conclusion that isn't carried by the analysis. I run end-to-end engagements of two to three months, from problem definition through synthesis, across clinical, government and technology stakeholders.",
                "What I don't have: I have not worked inside a consulting firm, so I'd be learning your engagement model, your quality bar on slides, and how a practice sells itself. I'd also point out one thing in my favour on the India practice specifically — four years of fieldwork in Indian health systems, including the districts that don't appear in the data, and 15+ institutional partnerships I originated and closed myself. That is India-market ground truth rather than a database view of it.",
                "If four years is a hard floor, I understand entirely. If it isn't, I'd welcome a conversation.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"You're two years short. Why should we look past that?\"", "The question, and it comes first. Don't argue the years — reframe what four years contained. Board-level accountability, a $51M portfolio, and 40+ programmes at four years in is not a normal four years. Then name one thing you'd need to learn and say you'd expect to be behind on it for a quarter. Candidates who claim no gap get disbelieved."),
            ("A case: \"A pharma client wants to enter a new Indian state. How do you size it?\"", "Near-certain, and it's your strongest ground. Disease burden and demographics, existing treatment infrastructure and referral pathways, competitor density, payer and out-of-pocket mix, distribution reach, regulatory variation by state. Then say what would change your answer — the heat map taught you that identical interventions don't travel, and that's a real, earned insight."),
            ("\"You haven't consulted before. How do you know you'll like it?\"", "Honest answer: you've done the analysis-to-recommendation loop, not the client-service loop. Say which part you know you'll find hard — the pace of turnaround and working to someone else's problem statement — rather than claiming it'll be seamless."),
            ("\"Tier-1 B-school?\"", "No, and it says preferred. Young India Fellowship is a recognised signal in Indian consulting hiring and belongs in the first line of your CV. Say it once, plainly, and move to the work."),
        ],
        "ask": [
            "What does the India practice's client mix look like — domestic pharma, MNCs, providers, payers?",
            "How much of the work is genuinely India-market versus supporting global teams?",
            "What separates the Senior Consultants who make Engagement Manager quickly?",
            "How does IQVIA's data business change what a consultant here can do that one elsewhere can't?",
            "What's the honest travel load?",
        ],
        "checklist": [
            "<b>Referral first.</b> Search LinkedIn for IQVIA India consultants, filter to Young India Fellowship and Ashoka alumni, then Christ University. One warm intro is worth more than this entire file",
            "Experience gap named in the first paragraph, not hidden",
            "YIF visible on the first line of the CV",
            "Market-entry case rehearsed out loud once, with the heat map as the worked example",
            "Applied even if no referral surfaces within 48 hours — don't let the search block the application",
            "Tracker updated with a follow-up date 7 days out",
        ],
        "flags": [
            "The two-year gap is real and it is the whole risk. Treat this as a referral-dependent application, not a normal one.",
            "IQVIA is the largest healthcare data and consulting firm in the world. As a line on a CV it credentials you into commercial healthcare strategy more decisively than anything else currently on your board.",
            "Consulting hours are consulting hours. The JD says hybrid and standard, not that the work is contained. Ask about travel and the real week before an offer.",
            "\"Indian Market\" in the title is the reason this clears the timezone gate — confirm in the first call that the practice isn't also supporting US or EU teams.",
            "Verify whether the six-to-eight-year band is a screening filter in their ATS. If it is, a referral is not an advantage here — it is the only route in.",
            "<b>The fallback, and its catch.</b> IQVIA is also hiring an <b>Associate Consultant — Commercial Strategy</b> (Bangalore/Gurgaon, hybrid, <b>2–5 years</b>, job id 4439807845). You clear that experience band outright. But it sits in the <b>Commercial Solutions Excellence Centers</b> — a delivery centre supporting global teams, which is the exact shape that fails your timezone gate quietly, and it's a step down in title. It also lists healthcare strategy consulting as <em>required</em>, not preferred. Worth knowing about; not worth taking instead.",
        ],
    },

    "voy": {
        "title": "Strategy &amp; Operations Manager",
        "company": "Voy India (formerly EarlyFit)",
        "place": "Delhi office",
        "tier": "Gate cleared — apply now",
        "fit": "4.0", "odds": "3.7",
        "resume": "resume/build/Nikita-Sachanandani-Strategy-Operations.pdf",
        "resume_name": "Nikita-Sachanandani-Strategy-Operations.pdf",
        "verdict": "The shift-hours question that held this up for a week is answered by the posting itself: Voy India is an India-market business — \"we're now in India to administer evidence-based, science-led medical care\" — run out of a Delhi office, not a UK-serving seat. Score revised up from the provisional 3.6/3.3. Apply. The band is 4–8 years and you are inside it.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4448401025", True),
            ("Then message", "Shreya Jha, HR — job poster on all three Voy postings", False),
            ("Band", "4–8 years in consulting or startups. You're at 4y2m", False),
            ("Degree", "None stated. No gate", False),
            ("Reports into", "\"Work closely with founders on strategic initiatives\"", False),
            ("Company", "Voy: 20 lakh members across Europe, Germany, Brazil since 2019. India entity was EarlyFit", False),
            ("Competition", "200+ applicants, posted 6 Aug", False),
        ],
        "route_note": "Apply to the <b>Manager</b> role, not the other two. Associate wants 3–4 years and is a step down; Director wants 7–15 and you'd be four years light. Applying to more than one signals you don't know which you are.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Strategy &amp; Operations Manager role in Delhi.",
                "What made me look twice: Voy India is doing the thing I've spent four years arguing for from the funding side. I manage a ₹450 crore ($51M) healthcare portfolio at Tata Trusts, and metabolic disease is where the gap between what India needs and what India funds is widest — it is expensive, chronic, largely preventable, and almost entirely absent from public programmes. A full-stack, endocrinologist-led model with GLP-1, diagnostics and behavioural support built into one flow is a serious answer to that, not a wellness product.",
                "On the job itself: your description is breaking ambiguous problems down, driving them to done, tracking the metrics, and picking up whatever else the business needs. That is close to a description of my current week. I screen 30–50 proposals a month, run two-to-three-month design cycles from problem to launch across clinical, government and technology partners, and build the dashboards and briefs the CEO and Board actually decide from. I also hold two mandates rather than one — Program Officer and Grants Manager — which is the only version of that on a fourteen-person team, and is mostly a story about being handed the things that need to get done.",
                "The honest gap is that I've worked inside an institution rather than a startup, so I'd be adjusting to your pace rather than arriving used to it. What I'd bring against that is ground truth — four years of fieldwork in Indian health systems, including districts that barely appear in the data — and a habit of asking what the number is before asking what the plan is.",
                "I'm Mumbai-based and ready to be in Delhi. 30-day notice, already running.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"You've been in philanthropy. This is a consumer subscription business.\"", "Expected, and the honest answer is strong: you already allocate capital against returns, you just measured return as impact. Name what you'd be learning — retention, CAC, cohort economics — rather than claiming the domains are identical. Tiff.in is your evidence you've modelled a commercial business."),
            ("\"What do you think our biggest risk is?\"", "Have a real answer, because GLP-1 businesses have an obvious one: what happens when a member stops paying, and whether the weight comes back. That is a retention question and a clinical-outcomes question at the same time. Saying so shows you understand the model rather than the marketing."),
            ("\"How would you think about which city we expand into next?\"", "Your ground. Disease burden and demographics, endocrinologist density, diagnostic infrastructure, income and out-of-pocket capacity, competitor presence. Then the heat map as the worked example of why identical interventions don't travel."),
            ("\"What are the working hours, and who are the founders you'd be close to?\" — <em>you</em> ask this", "Voy is UK-founded and Voy India was EarlyFit. \"Work closely with founders\" could mean the India leadership or the UK founders. The posting reads India-market and Delhi-office, which is why this now clears the gate — but confirm which founders, and whether there's a standing UK overlap."),
        ],
        "ask": [
            "Which founders would I be working with day to day — the India team or the global one?",
            "How much of the India roadmap is inherited from Europe versus built here?",
            "What happens to members after they hit their goal — what does retention look like?",
            "EarlyFit to Voy India is a real transition. What changed beyond the name?",
            "What would make you say this hire worked, six months in?",
        ],
        "checklist": [
            "Applied to the <b>Manager</b> posting only",
            "Messaged Shreya Jha after applying — she posted all three roles",
            "A view on GLP-1 retention risk prepared, not improvised",
            "Confirmed you're genuinely willing to be in Delhi before applying",
            "Tracker updated — this row has been sitting overdue since 15 Aug",
        ],
        "flags": [
            "Delhi NCR is your P1, not P0, and this one is onsite from the Delhi office. It's the second role on your board asking you to leave Mumbai.",
            "GLP-1 weight loss is a fast-moving, well-funded and ethically live category. Form your view on how it's marketed and to whom before you're inside owning a growth number.",
            "Voy India was EarlyFit — a rebrand or acquisition. Ask what happened to the original team, because that tells you what the India entity actually is.",
            "Three strategy roles posted at once — Associate, Manager, Director — usually means a function being built from scratch. Good for scope, worth asking who the Director will be and whether they're hired yet.",
            "Industry tags on the postings read \"Retail, Wellness and Fitness\" on two and \"Hospitals and Health Care\" on the third. Minor, but ask which one the company thinks it is.",
        ],
    },

    "evidence-action-2ai": {
        "title": "Chief of Staff, AI Access Initiative (2AI India)",
        "company": "Evidence Action / EAII Advisors",
        "place": "Delhi",
        "tier": "Scored under the new carve-out",
        "fit": "3.9", "odds": "3.2",
        "resume": "resume/build/Nikita-Sachanandani-AI-Health-Strategy.pdf",
        "resume_name": "Nikita-Sachanandani-AI-Health-Strategy.pdf",
        "verdict": "Building this kit is you making the carve-out call, so it's now scored rather than flagged. It's the strongest ceiling on your board — an entity spinning out, advised by Michael Kremer, Dario Amodei and Kent Walker — and the only role where four years of deciding which health technologies deserved funding is the literal job description. The cost is real and shows in the number: this is the one role here that does <em>not</em> credential you out of the sector you're leaving.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4446679715", True),
            ("Entity", "2AI India, incubated inside EAII Advisors, \"projected to spin off into an independent entity in the near term\"", False),
            ("Reports to", "The India Country Director, working with the Senior Leadership Team", False),
            ("Bar", "5–6 years in management consulting or international development. You're at 4y2m", False),
            ("Also required", "Working familiarity with how AI and ML systems are built and deployed", False),
            ("Led by", "Kanika Bahl, former Evidence Action CEO", False),
            ("Advised by", "Michael Kremer (Nobel laureate), Dario Amodei, Kent Walker", False),
            ("Competition", "Among the first 25 applicants when scanned — unusually thin", False),
        ],
        "route_note": "Apply early. \"Be among the first 25 applicants\" on a role with this profile will not last, and thin competition is doing more for your odds here than anything you can write.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Chief of Staff role at 2AI India.",
                "The reason I'm writing rather than scrolling past: the job asks for someone who can engage credibly with technical teams on AI without being an ML engineer, run the analysis that decides where to invest and what to stop, and hold relationships with government while doing it. Those three things are what I've been doing for four years, and they are rarely in the same person.",
                "At Tata Trusts I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes. Health-tech and AI diagnostics are sub-themes I own, which in practice means deciding which technologies were ready to be deployed at scale and which were a demo — assessing technical maturity, deployment readiness and evidence quality, and structuring pilots under a deliberately heavier bar: choosing conditions and geographies that would genuinely test a claim rather than flatter it. My partner institutions include IISc, C-CAMP, NIMHANS and the George Institute for Global Health.",
                "On prioritisation: I built a geospatial cost-effectiveness map across Indian states showing how identical interventions produced materially different returns by geography and terrain. It shaped where capital went from 2022 to 2024 — where to invest, what to scale, what to stop. That is the analysis your JD describes, built once already at portfolio scale.",
                "On government: I've built programme linkages deliberately through existing government systems rather than creating parallel infrastructure, which is the difference between a pilot that ends and one a state can absorb. I'm also writing a paper on why preventive care stays underfunded in India, which is the same underlying question 2AI is asking about AI-enabled access — who pays for the thing that obviously works.",
                "On the bar: you've asked for five to six years and I have just over four. I'd rather name that than let it be discovered.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"How would you decide which AI big bet India should run next?\"", "The core question, and it is yours. Walk the structure: burden and reach, whether the AI is actually the binding constraint or just the fashionable part, evidence base and what would need to be proven, delivery infrastructure that already exists, government absorbability, and downside risk. Then say what would make you kill it — the restraint is what separates you from an enthusiast."),
            ("\"What's your technical depth on ML?\"", "Do not overclaim. You evaluate systems, you don't build them — which is exactly what the JD asks for. Give a concrete example of a diagnostics tool you assessed and the specific question that decided it: what population it was validated in, and whether that population matched where it was going."),
            ("\"You're moving from grant-making. Isn't this the same thing?\"", "The trap, and it's fair. The honest distinction: 2AI designs and runs interventions rather than funding others to. Say what you want that's different — proximity to the thing being built, not distance from it. Don't pretend the sectors are unrelated."),
            ("\"You're a year or two short.\"", "Answer it structurally. Board-level accountability on a $51M portfolio at four years in is not a standard four years. Then name one thing you'd expect to be behind on for a quarter."),
        ],
        "ask": [
            "What does the spin-off timeline actually look like, and what changes for this role when it happens?",
            "The cross-sector analysis pointed at weather forecasting for smallholder farmers first. Where has the global health work landed?",
            "How do you think about the risk of AI interventions that work in a trial and not in a system?",
            "How much of this role is India strategy versus coordinating with the US team?",
            "What does the Country Director most need taken off their desk?",
        ],
        "checklist": [
            "Applied early — first-25 status is a real advantage and it expires",
            "Read the Cross-Sector Analysis of AI opportunities in LMICs before any interview; the JD names it",
            "One AI-diagnostics evaluation story ready, with the evidence standard you applied and what you rejected",
            "Experience gap named in the cover note, not left to be discovered",
            "Thought through the honest answer to \"isn't this the sector you're leaving?\" — because it partly is",
            "Tracker updated",
        ],
        "flags": [
            "<b>The gate call, stated plainly.</b> This fails one of your three carve-out tests on the letter: 2AI spans health <em>and</em> agriculture, so healthcare isn't the domain, it's half of one. You've overruled that by asking for the kit, which is a legitimate call — but it should be a decision you made, not one that got made for you.",
            "\"Grant reporting\" is a listed responsibility, and the host entity, EAII Advisors, does technical assistance to state governments on deworming and supplementation. Parts of this job are the job you're leaving.",
            "This is the one role on your board that does <b>not</b> credential you out of the philanthropic sector. That's the whole cost, and it's why transition value scores low here while everything else scores high.",
            "Incubated project inside a non-profit, pre-spin-off. Ask what the funding commitment is, over what horizon, and what happens to this role if the spin-off is delayed.",
            "The advisory names are extraordinary and they are advisors, not colleagues. Don't let them do more work in your head than they'll do in your week.",
            "Delhi, and the JD notes coordination with a US-based global team \"across time zones\". Ask what that means for your evenings before you accept.",
        ],
    },

    "bansal-foundation": {
        "title": "Manager, Founder's Office — Philanthropy",
        "company": "Sachin Bansal (Flipkart co-founder; Navi Group)",
        "place": "Bangalore",
        "tier": "Joint-best position on the board",
        "fit": "4.0", "odds": "4.0",
        "resume": "resume/build/Nikita-Sachanandani-Founders-Office.pdf",
        "resume_name": "Nikita-Sachanandani-Founders-Office.pdf",
        "verdict": "On profile match this is the strongest fit you have — \"identify and assess potential grantees on leadership, programs, governance, finances and operating capacity\" is your job description, and the 3–8 year band is one you clear cleanly rather than scrape into. ODDS 4.0 ties the highest on your board. The cost is real and it's in the number: this does not credential you out of philanthropy. Read the flags before you send.",
        "route": [
            ("<b>How to apply</b>", "<b>Not stated in the JD you have.</b> Find this out before anything else — see the note", False),
            ("Principal", "Sachin Bansal — Flipkart co-founder and CEO/Exec Chairman for a decade; founder of Navi Group", False),
            ("Reports to", "The Founder, directly. Founding team member", False),
            ("Band", "3–8 years. You're at 4y2m — comfortably inside, which is rare on your board", False),
            ("Degree", "Bachelor's or Master's from a reputed institution. Ashoka YIF clears this", False),
            ("Location", "Bangalore. Relocation from Mumbai", False),
            ("The entity", "Does not exist yet. You would be setting it up — registration, governance, systems, brand", False),
        ],
        "route_note": "<b>The application route is missing from the document.</b> If this came to you through a person, that person is your referral and the strongest asset in this file — go back through them rather than finding a form. If it came from a job board or a forward, find the original posting before you send anything, because the route determines whether you're a referred candidate or a cold one, and this role will not be filled from a cold pile.",
        "letters": [
            ("Cover letter", [
                "I'm writing about the Manager role in the Founder's Office.",
                "The core of the job — assessing prospective grantees on leadership, programmes, governance, finances and operating capacity, and turning that into a recommendation someone can act on — is what I do now. At Tata Trusts I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes. I screen 30–50 proposals a month against a 20–30 parameter framework, run deep-dive diligence on what survives, and prepare recommendations with objectives, budgets, milestones and reporting requirements that go to the CEO and Board of Trustees. I also act as the financial gate for the entire health theme rather than only my own programmes: every partner budget is reviewed for whether the numbers genuinely reflect the work before anything advances.",
                "What I think matters more for a role that begins with an empty room is what I've built rather than inherited. The screening framework I run proposals against, and the geospatial ROI analysis that shaped where the Trusts deployed capital between 2022 and 2024, did not exist before I built them — and the 15+ institutional partnerships I've closed each started from a standing start, with me finding the target and getting the first meeting. Before the Trusts I co-founded Tiff.in, which was selected for Ashoka University's incubator as one of three teams from thirty-five, where I did the market sizing, the unit economics and the pitch. None of that is the same as standing up a foundation, but it is the same instinct: the hard part is rarely the strategy document, it's the sequence — what has to be true before anything else can happen, and which decisions you're allowed to defer.",
                "I'll be straightforward about the gaps. I have not led a legal registration or structured an entity from scratch, and I would be leaning on advisers for that. What I have done is build a compliance and reporting discipline inside an institution that is audited seriously, and I know what a governance calendar has to survive.",
                "On why this rather than staying where I am: at the Trusts I inherited a portfolio and a set of systems that were built long before me. My work is to run them well. What I want is the earlier part — deciding what the institution is for, what it will not fund, and how it will decide. Doing that alongside someone who has built and scaled an organisation before, at the point when the questions are still open, is not a job that comes up often.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"You're leaving a foundation. Why join another one?\"", "<b>The question this whole application turns on, and a weak answer ends it.</b> Do not say you're excited about philanthropy — they'll wonder why you're leaving. The true answer is about the seat, not the sector: you have run a portfolio inside a built institution and you want to be at the point where it's being designed. Name what you'd learn that you cannot learn where you are: legal and governance structuring, standing up systems, hiring a founding team, and working next to someone who has built at scale."),
            ("\"Have you set up a foundation, or registered a legal entity?\"", "No. Say it in one sentence and don't stretch adjacent experience to cover it — they will have advisers who can tell. Then say what you'd bring instead: you know what a grants function needs to <em>do</em> on day one, which is the part advisers can't tell them, and you've built compliance and reporting discipline that survives a serious audit."),
            ("\"How would you design the grant-making framework from scratch?\"", "Almost certain, and it's your strongest ground. Walk it as a sequence: what the Founder wants to be true in ten years, what that rules out, then the screening parameters, then the diligence depth by cheque size, then what gets measured and what deliberately doesn't. Cite your 20–30 parameter framework and the 40-parameter one before it. Then say what you'd get wrong first — over-engineering the framework before there's enough deal flow to test it."),
            ("\"What would you do in the first ninety days?\"", "Resist the strategy answer. The real first-90 for a foundation that doesn't exist is: registration path chosen with advisers, a decision-making protocol between you and the Founder, a bank account and disbursement mechanism, one or two anchor grants to learn on, and a compliance calendar. Strategy comes after you've moved money once."),
            ("\"Compensation?\"", "You have no comp floor and money isn't your axis, so don't anchor first. But do not undersell into a founder's office — these roles are frequently under-levelled relative to their scope. \"What band have you set for this?\" and let them go first."),
        ],
        "ask": [
            "What has Sachin already decided about focus areas, and what is genuinely still open?",
            "Is the intent a grant-making foundation, or an operating one that builds programmes itself?",
            "What does the IIT Delhi endowment commitment tell me about how he wants to give?",
            "What size is the founding team meant to be in eighteen months, and who comes next after me?",
            "How much of his time does this actually get — weekly, monthly, or when something breaks?",
            "What would make you say, two years in, that setting this up went well?",
        ],
        "checklist": [
            "<b>Find the application route first.</b> If a person sent you this, apply through them",
            "Build-from-zero evidence in the letter is the screening framework, the heat map, the 15+ partnerships closed from a standing start, and Tiff.in — all of it on the CV and all of it checkable",
            "Read up on the IIT Delhi Global Alumni Endowment Fund before any conversation; the JD names it as the origin of his giving",
            "Answer to \"why leave one foundation for another\" rehearsed out loud, not just thought through",
            "A first-90-days sequence prepared that starts with registration and a bank account, not with strategy",
            "Confirmed you're genuinely willing to relocate to Bangalore",
            "Tracker updated with a follow-up date 7 days out",
        ],
        "flags": [
            "<b>The honest cost, stated once.</b> This is philanthropy, and it does not clear your healthtech/AI carve-out — there is no health or AI focus in the document at all. Two years here and your CV reads Program Officer, Tata Trusts → Manager, Founder's Office (Philanthropy). That is a philanthropy career rather than the transition you set out to make. Transition value is the one dimension scoring low here, and it is what holds FIT at 4.0 instead of 4.6.",
            "<b>Why I still think it's worth applying.</b> Your sector gate exists to stop you taking a lateral into more of the same. This isn't more of the same — you currently run a portfolio inside an institution built decades before you; here you would build the institution. \"Set up a foundation from zero alongside Sachin Bansal\" is a different sentence on a CV from \"managed a grant portfolio,\" and it is the sentence founder's-office, strategy and VC employers actually screen for.",
            "<b>Ask about the path out, before you're in.</b> The strongest non-obvious asset here is proximity to Sachin Bansal and to Navi. Find out, in the room, whether people in his orbit move into his operating companies — because that is the difference between this being a bridge and being a second philanthropy job.",
            "Founder's offices drift toward administration. The JD lists correspondence, meeting notes, board papers, follow-ups and calendar-adjacent work alongside the strategic mandate. Ask what proportion of the first year is genuinely institution-building versus supporting the Founder's existing commitments.",
            "The entity does not exist. There is no team, no track record, no alumni, and no way to check the culture from outside — the company-signal dimension is scored on the principal, not the organisation. Ask who else has been hired and who is advising.",
            "Sachin Bansal is running Navi, a fast-growing financial services company, at the same time. Ask directly how much of his attention this has, because a founder's office with an absent founder is a very different job from the one described.",
        ],
    },

    "piramal": {
        "title": "Chief Manager — Strategy &amp; Special Projects",
        "company": "Piramal Pharma Solutions",
        "place": "Mumbai",
        "tier": "Highest fit currently open",
        "fit": "4.2", "odds": "2.7",
        "resume": "resume/build/Nikita-Sachanandani-CEO-Office.pdf",
        "resume_name": "Nikita-Sachanandani-CEO-Office.pdf",
        "verdict": "A CEO's-office mandate at a listed Indian pharma, in Mumbai, with <b>no degree requirement and no years-of-experience bar stated anywhere in the posting</b> — which, against a search where twelve roles have died on exactly those two lines, is the most valuable thing about it. LinkedIn tags it Mid-Senior, not Director. The open risk is the title band, and one message settles it.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4457230093", True),
            ("Message", "Ranjana Mishra, Manager HR — job poster, direct message enabled", False),
            ("Seniority tag", "<b>Mid-Senior level</b> — not Director", False),
            ("Degree required", "<b>None stated.</b> Anywhere in the posting", False),
            ("Years required", "<b>None stated.</b> Only \"proven experience in a senior leadership or executive support role\"", False),
            ("Reports into", "The CEO's office; collaborates with the Head of Strategy", False),
            ("Company", "Piramal Pharma Solutions — CDMO arm of listed Piramal Pharma. Sites across North America, Europe and Asia", False),
            ("Competition", "200+ applicants", False),
        ],
        "route_note": "Message Ranjana <b>before</b> tailoring anything further. The single unknown is whether \"Chief Manager\" sits above her band, and that is one question, not a research project. If the answer is eight-plus years, this closes cleanly and costs an hour rather than a week.",
        "letters": [
            ("Cover note", [
                "I'm writing about the Chief Manager role in Strategy &amp; Special Projects.",
                "The posting describes establishing a governance rhythm — reviews, dashboards, escalation mechanisms — that drives timely decisions and tracks value realisation across functions. That is the part of my current job I'd most want to keep. At Tata Trusts I manage a ₹450 crore ($51M) healthcare portfolio across 40+ programmes, and I built the review cadence, dashboards and briefing papers the CEO and Board of Trustees use to decide. I also act as the financial gate for the entire health theme rather than only my own programmes: every partner budget is reviewed for whether the numbers genuinely reflect the work before anything advances to approval.",
                "I hold two mandates rather than one — Program Officer and Grants Manager — which is the only such arrangement on a fourteen-person team, and in practice it means I sit between the strategy and the execution of it: defining scope and timelines for two-to-three-month initiatives, mapping dependencies across clinical, government and institutional stakeholders, and surfacing what is off track before it reaches leadership.",
                "Where I'd be learning: I have not worked inside pharmaceutical manufacturing, and a CDMO's execution barriers sit in manufacturing, supply chain and quality — functions I've never owned. I'd be relying on your business leaders for that context for a quarter. What I'd bring against it is four years of healthcare judgement and a habit of building governance that people actually use rather than governance that produces reports.",
                "I'm Mumbai-based, and on a 30-day notice.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"Walk me through your experience in pharma manufacturing or supply chain.\"", "You have none, and this is the sharpest gap. Don't stretch programme delivery into operations — name it in one sentence, then move to what does transfer: cross-functional governance where you had no formal authority, and getting decisions closed between parties with different incentives. Ask what the top three execution barriers across clusters are right now; the question does more for you than an answer would."),
            ("\"Chief Manager is a senior band. Talk me through your years.\"", "Expect this, and don't be defensive. Four years carrying board-level accountability on a $51M portfolio, with financial sign-off across a whole theme, is not a standard four years. Say what you've owned rather than how long you've owned it — then let them decide, because the posting deliberately didn't set a number."),
            ("\"How would you set up a governance rhythm here?\"", "Your ground, and almost certain. Sequence it: what decisions are actually stuck and why, then the smallest cadence that unblocks them, then the dashboard — in that order. Say plainly that most governance fails because it reports rather than decides, and that you'd rather run three reviews that change something than twelve that don't."),
            ("\"Why leave the Trusts?\"", "Forward-looking, 30 seconds, no criticism. Script in private/exit-narrative.md."),
        ],
        "ask": [
            "Is this role closer to strategy development, or to making sure the strategy already set actually lands?",
            "What's the hardest cross-functional decision currently stuck between clusters?",
            "How does the CEO's office relate to the Head of Strategy — who owns what?",
            "The JD mentions change management. What change is underway right now?",
            "What band does Chief Manager sit in here, and who did this role report to before?",
        ],
        "checklist": [
            "<b>Message Ranjana Mishra first</b> and ask the band question before doing anything else",
            "Pharma manufacturing gap named in the cover note rather than discovered in the room",
            "One governance story ready — a cadence you built that changed a decision, not one that produced a report",
            "LinkedIn check on Piramal strategy alumni: where do people go after the CEO's office here?",
            "Applied, tracker updated with a follow-up 7 days out",
        ],
        "flags": [
            "<b>The band is the whole risk.</b> \"Chief Manager\" in Indian corporate hierarchies usually sits above Manager and below AGM — often eight-plus years. The posting states no number and LinkedIn tags it Mid-Senior, so it is genuinely open, but do not build a case around it before Ranjana answers.",
            "A CDMO is a manufacturing business. The execution barriers named in the JD are manufacturing, SCM, finance and commercial — none of which you have worked in. This is a real domain gap and a bigger one than the healthcare label suggests.",
            "Piramal Pharma is listed and Piramal Group is a serious Indian conglomerate; the brand credentials you out of philanthropy decisively. That is why transition value scores 5 here and why the fit is 4.2 despite the domain gap.",
            "\"Proficiency in using AI, productivity tools, project management software\" is in the requirements. Have a real answer about which tools you use and how — your tool proficiency is unestablished in your own materials and this is the second posting to ask.",
            "200+ applicants with a named HR contact. Message her; a role with no stated bar attracts everyone, and the ones who ask a specific question get remembered.",
        ],
    },

    "incresco": {
        "title": "Chief of Staff to the CEO",
        "company": "Incresco",
        "place": "Bengaluru · onsite",
        "tier": "Most balanced of the three",
        "fit": "3.3", "odds": "3.0",
        "resume": "resume/build/Nikita-Sachanandani-Chief-of-Staff-Ops.pdf",
        "resume_name": "Nikita-Sachanandani-Chief-of-Staff.pdf",
        "verdict": "One line in this JD is written around the credential nobody else asks for: <em>\"proven ability to hold people to commitments across teams you do not manage.\"</em> That is your financial-gatekeeper role exactly — budget authority over the whole health theme, not just your own programmes. You also hit four of their five preferred items. The band is 4–8 years and you are at the floor but inside.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4462655960", True),
            ("Band", "4–8 years running operations, a function, or a business unit with its own outcomes", False),
            ("Reports to", "The CEO. Department heads report to the CEO on function, <b>and to you on their numbers</b>", False),
            ("The company", "Three business lines: a technology consulting practice and two product businesses", False),
            ("The risk", "\"MBA <b>or equivalent commercial training</b>\" — softer than required, still a gate", False),
            ("Competition", "200+ applicants", False),
            ("Location", "Bangalore, onsite. Relocation from Mumbai", False),
        ],
        "route_note": "Their JD is unusually well written and states a house style: <em>\"Bring a recommendation, not options.\"</em> Match it. A hedged cover note from a candidate applying to a role about holding people to commitments answers the question before they ask it.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Chief of Staff role.",
                "One line in your posting is the reason: proven ability to hold people to commitments across teams you do not manage. Almost nobody writes that down, and it is the part of my current job I would most want to keep doing.",
                "At Tata Trusts I hold two mandates rather than one, Program Officer and Grants Manager, on a fourteen-person health team. The second one means I am the financial gate for the entire health theme, not only my own programmes: every partner's budget goes through me and is checked against whether the numbers genuinely reflect the work, before anything reaches CEO and Board approval. That is authority over teams that do not report to me, exercised weekly, and telling a colleague their number does not hold up is the job rather than the hard part of it.",
                "I also built the reporting that did not exist before I arrived. The dashboards, the review rhythm and the briefs the CEO and Board decide from are mine, and they surface exceptions rather than status. Alongside that I manage a ₹450 crore ($51M) portfolio across 40+ programmes and run two to three month delivery cycles against stated dates, flagging slippage before the date rather than after.",
                "Two things I will name rather than let you find. I do not have an MBA; my postgraduate qualification is the Young India Fellowship at Ashoka, which is a general one. And my commercial judgement has been exercised on capital deployment and cost efficiency rather than on revenue, so a P&L would be new. I would rather say that than have you discover it in the second conversation.",
                "I am ready to be in Bangalore, and on a 30-day notice.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"Tell me about a time you held someone to a commitment when you had no authority over them.\"", "This is the interview. Have two ready and make them specific: a partner budget you sent back, and a date you flagged three weeks early with what you did about it. Name what it cost you in the relationship, because that detail is what makes the story credible."),
            ("\"You do not have an MBA.\"", "Do not apologise. The line says <em>or equivalent commercial training</em>, so answer the substance: four years of capital allocation with board accountability, cost-per-unit modelling across 40+ programmes, and budget sign-off across a whole function. Then say what you would be learning, which is revenue."),
            ("\"Every metric comes from a system, not a spreadsheet. Where are you on that?\"", "Their JD is emphatic about this. Be honest about your tooling: you built dashboards and reporting, and you should say plainly which tools and how far your Excel and BI depth actually goes. This is the second posting to test it and it remains unestablished in your own materials."),
            ("\"You are at the bottom of our band.\"", "Four years carrying board-level accountability on a $51M portfolio is not four years of execution. Say what you owned, not how long."),
        ],
        "ask": [
            "Which of the three business lines is furthest from where the CEO wants it?",
            "What happens today when a department head misses a date?",
            "Is there a management reporting system already, or would I be building it?",
            "How do the two product businesses relate to the consulting practice commercially?",
            "What would make you say this hire worked, six months in?",
        ],
        "checklist": [
            "Cover note leads with the \"teams you do not manage\" line, because that is the match",
            "Two accountability stories rehearsed, each with a specific number and date",
            "Honest answer prepared on tooling depth: Excel, BI, what you actually use",
            "MBA gap named in the note rather than discovered later",
            "Confirmed you are genuinely willing to relocate to Bangalore",
            "Tracker updated with a follow-up 5 days out",
        ],
        "flags": [
            "<b>Not healthcare.</b> This is the trade the search has now handed you three times, after Cube and Honasa. Taking it spends the domain depth that is currently your sharpest differentiator, in exchange for a real chief-of-staff seat with genuine authority.",
            "Small company across three business lines and no public profile to check. Ask about headcount, revenue and how long the CEO has wanted this seat filled.",
            "\"MBA or equivalent commercial training\" is the one line you fail. Treat it as the thing to overcome in the letter, not something to hope goes unnoticed.",
            "The JD is unusually direct about culture: every commitment carries a date, bring a recommendation rather than options, nothing reaches the CEO as information alone. That is a specific way of working. Decide you want it before you interview, because they will be testing for it from the first email.",
            "Bangalore onsite means relocating from Mumbai for a company you cannot research from outside. Weigh that before you invest.",
        ],
    },

    "weekday": {
        "title": "Chief of Staff, Office of the CEO",
        "company": "Weekday AI (YC W21) — hiring for an undisclosed client",
        "place": "Hyderabad · work from office",
        "tier": "Widest experience band found anywhere",
        "fit": "3.3", "odds": "3.0",
        "resume": "resume/build/Nikita-Sachanandani-Chief-of-Staff-CEO-Office.pdf",
        "resume_name": "Nikita-Sachanandani-Chief-of-Staff.pdf",
        "verdict": "The band is <b>2–10 years</b> with no degree requirement anywhere, which is the widest and least gated posting in this entire search. Their decision-support framework — issue, options, implications, recommendation, decision required — is how you already write for a board. The catch is at the top of the JD: <em>\"This role is for one of the Weekday's clients.\"</em> You would be applying to a company whose name you do not know.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4455586436", True),
            ("<b>Read this first</b>", "Weekday is a recruiting marketplace. <b>The employer is undisclosed</b> — see the flags", False),
            ("Band", "<b>2–10 years.</b> No degree requirement stated anywhere", False),
            ("Reports to", "Co-Founder &amp; CEO", False),
            ("Scope", "Product, Engineering, AI/ML, Partnerships, Operations, Institutional Engagements", False),
            ("Location", "Hyderabad, work from office", False),
        ],
        "route_note": "Because the employer is hidden, treat the first reply as an information-gathering call rather than an interview. Ask who the company is, what stage, and why the CEO wants this seat, before you invest anything further.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Chief of Staff role in the Office of the CEO.",
                "Your description of decision support is the part that made me write: structuring an ambiguous problem as issue, options, implications, recommendation, decision required, and arriving with a point of view rather than escalating. That is how I have written for four years. At Tata Trusts I take 30 to 50 proposals a month through a fixed screening framework, run deep-dive diligence on what survives, and put a recommendation in front of the CEO and Board of Trustees. An audience like that has a low tolerance for a conclusion the analysis does not carry.",
                "On the operating cadence: I built the trackers, review rhythm, decision logs and dashboards the leadership at the Trusts decides from, and I hold two mandates rather than one, which in practice means I am also the financial gate for the entire health theme. Every partner budget in the portfolio is checked by me before it advances. That is coordination across teams I do not manage, which is most of what this role sounds like.",
                "On institutional engagements: I have originated and closed 15+ institutional partnerships from a standing start, and structured programmes to work through government systems rather than around them. Preparing a principal for a meeting with an institution, and then making sure what was agreed actually happens, is familiar work.",
                "Where I would be learning: I have not coordinated engineering or AI/ML delivery, and your JD is clear that visibility into technical milestones matters. I can hold a technical conversation without pretending to be an engineer, and I would rather say that plainly than overstate it.",
                "I am ready to be in Hyderabad, on a 30-day notice.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("<b>\"Who is the company?\"</b> — <em>you</em> ask this, first", "Non-negotiable. The posting hides the employer. Before a second conversation you need the name, the stage, the funding position and why the seat is open. A recruiter who will not say is a reason to stop."),
            ("\"Walk me through how you structure a decision for a CEO.\"", "Their framework is written into the JD, so use your own version of it and then show a real example: a proposal you recommended against, what the options were, and what the board did with it."),
            ("\"How would you handle an engineering milestone slipping?\"", "You have not done this. Do not pretend. Say what you would do instead: understand the dependency, find out who else is blocked, get the date restated honestly, and make sure the CEO hears it before it becomes a surprise. That is the transferable half."),
            ("\"Why leave the Trusts?\"", "Forward-looking, 30 seconds, no criticism. Script in private/exit-narrative.md."),
        ],
        "ask": [
            "Which company is this, and what stage are they at?",
            "Why is the seat open now, and has anyone held it before?",
            "What proportion of the role is technical coordination versus strategic initiatives?",
            "Who are the institutional stakeholders the CEO is engaging with?",
            "How quickly does this process move?",
        ],
        "checklist": [
            "<b>Get the employer's name before the second conversation.</b> Everything else depends on it",
            "One decision-support story ready in their exact framework",
            "Honest position rehearsed on engineering coordination, not an overclaim",
            "Confirmed you are willing to be in Hyderabad",
            "Tracker updated",
        ],
        "flags": [
            "<b>The employer is undisclosed.</b> Weekday is a recruiting marketplace and this role is for a client. You cannot assess the company, its funding, its culture or its alumni, and the company-signal dimension is unscoreable rather than merely unknown.",
            "Recruiter-mediated processes are either fast or a black hole, with little in between. Set your own deadline for getting a name.",
            "The scope is genuinely wide — Product, Engineering, AI/ML, Partnerships, Operations, Institutional Engagements. At an unknown company that could mean real breadth or it could mean nobody owns anything.",
            "Not healthcare, and the domain is unknown, so even the consolation of an adjacent sector is not guaranteed.",
            "2 to 10 years is a very wide band. It usually means either an unusually flexible hiring manager or an unclear brief. Worth asking which.",
        ],
    },

    "darwinbox": {
        "title": "Chief of Staff to the Co-Founder",
        "company": "Darwinbox",
        "place": "Hyderabad",
        "tier": "Best fit, hardest odds",
        "fit": "3.7", "odds": "2.3",
        "resume": "resume/build/Nikita-Sachanandani-Chief-of-Staff-Systems.pdf",
        "resume_name": "Nikita-Sachanandani-Chief-of-Staff.pdf",
        "verdict": "The strongest company of the three by a distance: a genuine Indian SaaS unicorn, reporting to a Co-Founder, with no years bar and no degree gate stated. \"Build the intelligence layer\" and \"build systems, not dependency\" describe what you already did at the Trusts. The odds are the worst because one pillar of the role — <b>hands-on AI and automation fluency</b> — is something you cannot currently evidence.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4459686299", True),
            ("Reports to", "A Co-Founder", False),
            ("Years required", "<b>None stated</b>", False),
            ("Degree required", "<b>None stated</b>", False),
            ("The hard requirement", "<b>Hands-on AI/automation fluency.</b> This is the gap", False),
            ("Backgrounds they name", "Strategy, consulting, product, operations, investment banking — philanthropy is not listed", False),
            ("Location", "Hyderabad", False),
        ],
        "route_note": "Do not apply to this one cold and hope. The AI pillar is explicit and repeated three times in the JD; if you cannot speak to it concretely, the application dies at the first screen. Spend an evening making that answer real before you send anything.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Chief of Staff role with the Co-Founder.",
                "Two lines in your posting describe work I have already done. Build the intelligence layer: at Tata Trusts I synthesise inputs across 40+ programmes into the dashboards and briefs the CEO and Board of Trustees decide from, and the job is separating signal from noise early enough that a problem is still cheap. And build systems, not dependency: I hold two mandates rather than one, which means I am the financial gate for the entire health theme, and the point of building that discipline properly was that the standard holds without me in every review.",
                "I also manage a ₹450 crore ($51M) portfolio and take 30 to 50 proposals a month from a fixed screening framework through to a recommendation. Taking a loosely defined priority and driving it to owners, cadence and a measurable outcome is the shape of my week.",
                "On the AI pillar, I will be straight with you rather than claim fluency I do not have. I am not going to tell you I have redesigned workflows with agents. What I can tell you is that I have spent four years deciding which technologies were ready to be deployed and which demoed well, with health-tech and AI diagnostics as sub-themes I own, and I have structured technology pilots under a deliberately heavier evidence bar. That is judgement about where a technology genuinely changes the work, which is the harder half of making AI operational. The tooling I would be learning quickly, and I would expect to be behind for a quarter.",
                "I am ready to be in Hyderabad, on a 30-day notice.",
                "Nikita Sachanandani<br>+91 7698030306 · sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("<b>\"Show me how you use AI in your own work.\"</b>", "The question that decides this application, and it will be asked. A general answer fails. Before applying, actually build something small and real — a research workflow, a synthesis process, a tracker you automated — and be able to describe what it replaced and what it saved. This is preparation, not framing."),
            ("\"Where would you make Darwinbox AI-native first?\"", "Have a view. Their JD names research, synthesis, preparation, monitoring and follow-through as the targets. Pick one, say why it is first, and say what would make you wrong. Do not attempt an opinion about their product."),
            ("\"Your background is philanthropy. Our list says strategy, consulting, product, operations or banking.\"", "Answer it structurally, as always: screening at volume, diligence on people, capital allocation, portfolio monitoring, board reporting. Then name the honest difference, which is that you have never worked at software pace."),
            ("\"Give me an example of building a system that worked without you.\"", "Your ground. The financial gate across the health theme is exactly this: a standard applied by others because the mechanism held, not because you were in the room."),
        ],
        "ask": [
            "Which Co-Founder, and what does their week look like today?",
            "What does AI-native mean at Darwinbox internally, as opposed to in the product?",
            "Has this role existed before, and what happened to the person who held it?",
            "What is the single decision that has been stuck longest?",
            "How much of this is building mechanisms versus running them once built?",
        ],
        "checklist": [
            "<b>Build a real AI workflow before applying.</b> One you can describe concretely, with what it replaced. Without this the application fails at the first screen",
            "A view prepared on where an enterprise SaaS company should go AI-native internally first",
            "\"Systems not dependency\" story ready: the financial gate across the health theme",
            "Philanthropy-to-software answer rehearsed, including the honest part about pace",
            "Confirmed you are willing to be in Hyderabad",
            "Tracker updated",
        ],
        "flags": [
            "<b>Darwinbox is the best company on this shortlist</b> — a real Indian SaaS unicorn with checkable alumni and a brand that credentials you out of philanthropy decisively. That is why the fit scores 3.7 despite the gap.",
            "<b>The AI fluency requirement is not decorative.</b> It appears three times: build AI-native ways of working, make AI operational, hands-on AI/automation fluency. Treat it as a genuine prerequisite and spend real time on it before applying.",
            "The backgrounds they name do not include philanthropy or the social sector. You are outside the stated pool and have to earn your way in on substance.",
            "Seniority is tagged \"Not Applicable\", which usually means the level is negotiable against the candidate. That can work for you at four years, or against you.",
            "Hyderabad, and this is your second relocation-required role on the same shortlist. Decide the relocation question once rather than three times.",
            "<b>Ask about the shift, even though this posting doesn't mention one.</b> Darwinbox has 13 roles open and <b>three of them say \"US Shift\" in the title</b> — Delivery Assurance Consultant, Engagement Manager, US Functional Consultant. That is a company running US-facing hours for part of its organisation. A chief of staff reporting to a Hyderabad-based co-founder should be IST, but your timezone gate is absolute and this is cheap to confirm in the first call.",
        ],
    },

    "novartis": {
        "title": "Senior Manager &mdash; Market Access",
        "company": "Novartis India",
        "place": "Greater Hyderabad",
        "tier": "Highest fit on the board right now",
        "fit": "3.9", "odds": "2.0",
        "resume": "resume/build/Nikita-Sachanandani-Market-Access.pdf",
        "resume_name": "Nikita-Sachanandani-Market-Access.pdf",
        "verdict": "Decode the jargon and this is the closest functional match to your actual work that anyone has posted. <b>HTA means Health Technology Assessment: deciding whether a health technology delivers enough benefit per rupee to justify paying for it.</b> That is what you have done for four years with real money behind the judgement. The odds are poor because Senior Manager at Novartis is an 8-to-12-year band and the posting's requirements section is broken.",
        "route": [
            ("Apply at", "linkedin.com/jobs/view/4460730223", True),
            ("What it actually is", "Market Access: HTA submissions, payer research, brand pricing, listing agreements", False),
            ("Stated requirements", "<b>None.</b> The \"Essential Requirements\" section lists success metrics, not requirements", False),
            ("Real bar, inferred", "Pfizer's <em>Manager</em> role, one band lower, wants \"Science graduate with MBA, 5&ndash;12 years\"", False),
            ("Scope", "\"Country level\" and \"national patient access\" &mdash; India market, not a global services seat", False),
            ("Competition", "130 applicants", False),
            ("Location", "Greater Hyderabad. Relocation from Mumbai", False),
        ],
        "route_note": "<b>This is referral-dependent, like IQVIA.</b> A cold application into a Senior Manager band you are four years short of will be filtered. Spend the hour finding one person in Novartis India's market access or patient access function before you spend it tailoring further.",
        "letters": [
            ("Cover note", [
                "I'm applying for the Senior Manager role in Market Access.",
                "The reason I think this is worth your time despite an unconventional background: health technology assessment is the work I already do. At Tata Trusts I manage a &#8377;450 crore ($51M) healthcare portfolio, and health-tech and AI diagnostics are sub-themes I own. The decision I make repeatedly is whether a technology delivers enough benefit per rupee to justify public money going into it, at what scale, and on what evidence. I structure technology pilots under a deliberately heavier evidence bar, choosing the conditions and geographies that will genuinely test a claim rather than flatter it, and I build the economic case that decides whether something is funded.",
                "On the payer side: in India the largest payer is government, and I have spent four years working through it rather than around it. My programmes are structured to run through existing government systems and schemes instead of duplicating them, and I deal directly with health departments and public programme managers. I also built a geospatial cost-effectiveness analysis across Indian states showing how identical interventions delivered materially different benefit per rupee by geography, which shaped where the Trusts allocated capital.",
                "One thing that is genuinely mine rather than a stretch: I am writing a paper comparing the US and Indian health economies, arguing for greater investment in preventive care. Health economics is not a function I would be learning from scratch.",
                "Where I would be learning, and I would rather say it than have you find it: I have not built a brand pricing strategy, negotiated a product listing agreement, or made an HTA submission to a P&amp;R body. I know the analysis underneath those things; I do not know the pharma commercial machinery around them. I am also at four years, which I recognise sits below a Senior Manager band.",
                "Nikita Sachanandani<br>+91 7698030306 &middot; sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("\"Talk me through an HTA submission you have worked on.\"", "You have not made one. Say so in a sentence and substitute the closest real thing: a technology you assessed, the evidence standard you applied, what you needed to see before recommending funding, and what you rejected. The analysis is the same; the submission format is not."),
            ("\"What do you know about NPPA, DPCO and state reimbursement?\"", "Almost certainly asked, and largely a gap. Do not bluff on regulatory specifics. What you can speak to credibly is how public health programmes actually procure and deliver at state level, which is the practical half most candidates lack."),
            ("\"How would you build the economic case for a new brand's listing?\"", "Your ground, translated. Burden of disease and eligible population, standard of care today and what it costs, incremental benefit, budget impact on the payer, and where the uncertainty sits. Then say what would make you revise it, because the restraint reads as maturity."),
            ("\"You are at four years and this is a Senior Manager role.\"", "Do not dodge. Four years with board accountability on a $51M portfolio is not a standard four years. Then ask directly what band they have set, because their posting does not say, and if the honest answer is eight years it is better to know in call one."),
        ],
        "ask": [
            "What band is this role actually set at? The posting does not state one",
            "Which therapy areas would I cover, and are any of them in public programmes?",
            "Is this India-market, or does it support other countries as well?",
            "How much of the role is HTA and evidence versus commercial negotiation?",
            "What are the hours? Novartis has a large Hyderabad services presence and I want to understand which side this sits on",
        ],
        "checklist": [
            "<b>Find a referral first.</b> Novartis India market access or patient access, via LinkedIn. This is the lever that matters",
            "Confirm the band in the first conversation, because the posting genuinely does not state one",
            "Confirm it is India-market and IST, not a global services seat",
            "One technology-assessment story ready: what you assessed, the evidence bar, what you rejected",
            "Health economics paper mentioned. It is the most distinctive thing you have here",
            "Tracker updated with a follow-up 7 days out",
        ],
        "flags": [
            "<b>The posting is mis-assembled.</b> Its Essential Requirements section lists success metrics rather than requirements, so no years and no degree are stated. That is a broken JD rather than an open door, and the real bar lives in their ATS.",
            "<b>Pfizer's comparable role is one band lower and gates on a science graduate with an MBA.</b> Assume Novartis is at least as strict. This is the eighteenth credential wall in this search and the reason odds sit at 2.0.",
            "Two lines in the JD, reporting adverse events within 24 hours and distributing marketing samples, are pharmacovigilance and commercial boilerplate. They signal this seat carries regulatory obligations and sits closer to the commercial field than the title suggests.",
            "Novartis has a large Hyderabad global-services operation alongside its India commercial org. This posting reads India-market, but confirm it, because their other Hyderabad market access role is explicitly a global support seat.",
            "<b>Market access is a lane worth entering even if this role fails.</b> Fifteen live roles across Pfizer, Boehringer, MSD, Takeda, Parexel, Syneos and Evalueserve. The likely entry point is the research firms rather than the pharma companies. See applications/evals/2026-09-08-market-access.md.",
            "Budget Impact Models are the core deliverable of this function, and financial modelling has now blocked five separate lanes. If you enter market access seriously, that skill stops being optional.",
        ],
    },
    "lumiere": {
        "title": "Founder's Office",
        "company": "Lumiere Education",
        "place": "Fully remote",
        "tier": "The post is the brief",
        "fit": "3.1", "odds": "3.3",
        "resume": "resume/build/Nikita-Sachanandani-Founders-Office-Lumiere.pdf",
        "resume_name": "Nikita-Sachanandani-Founders-Office.pdf",
        "verdict": "The founder's post is doing the screening, and it screens against your profile: he is filtering out people who would feel above writing SEO blog posts and scraping Instagram handles. <b>Your answer to that is Tiff.in, not Tata Trusts.</b> You co-founded a content business and personally drove 520% YouTube and 370% Instagram growth. That is the exact unglamorous work he described, and it is checkable.",
        "route": [
            ("Apply at", "airtable.com/appR3WCH2LJsjy3M3/shrcw0hx3Oyy4TbmS", True),
            ("Questions asked", "Why Lumiere, plus a cover letter", False),
            ("Location", "<b>Fully remote.</b> Their careers page states all Lumiere positions are remote", False),
            ("Founders", "Stephen Turban (Harvard, ex-McKinsey) and Dhruva Bhat (Harvard, Rhodes Scholar, Oxford PhD)", False),
            ("Final round", "With both co-founders", False),
            ("Scale", "Acquired <b>Immerse Education</b> in Jan 2026, summer programmes at Oxford, Cambridge and 8 other universities", False),
            ("Track record", "13 founder's office members in four years", False),
            ("Contact", "careers@lumiere.education", True),
        ],
        "route_note": "<b>Do not lead with the &#8377;450 crore portfolio.</b> Everything in his post warns against people who will find the work beneath them, and a portfolio number is the fastest way to trigger that suspicion. Lead with Tiff.in and let the Trusts sit underneath.",
        "letters": [
            ("Why Lumiere", [
                "Because I have spent four years deciding which programmes actually change outcomes, and research mentorship is one of the few where the mechanism is not in doubt. Most of what I evaluate depends on a long chain of assumptions holding. Give a seventeen-year-old sustained access to someone who knows how to think about a question, and they learn to think about questions. That is a short chain.",
                "I also have a personal stake in it. My own path ran through the Young India Fellowship, and I published a paper in the Journal of Enterprising Culture on informal networks in the Surat textile market, built from interviews across the whole supply chain from weavers to end consumers. I am writing another now, comparing the US and Indian health economies. Research access changed what I thought I was allowed to attempt, and I got it late. Lumiere gives it to people at the point where it redirects them.",
                "And the less noble half, honestly: your post is the most accurate job description I have read. Most founder's office postings sell proximity to the founder. Yours says you will write dozens of blog posts and collect hundreds of Instagram handles, and that the ceiling only exists if you get the unglamorous part right. I would rather work somewhere that tells me that in advance.",
            ]),
            ("Cover letter", [
                "I am applying for the founder's office role.",
                "Your post described two jobs: writing dozens of SEO blog posts, and collecting hundreds of education influencers on Instagram and reaching out to each one. I want to start there, because I have done that work.",
                "In 2021 I co-founded Tiff.in, incubated at Ashoka University as one of three teams funded out of thirty-five. I did the commercial modelling, and I also wrote the content, published it, and chased the distribution. We grew YouTube views 520% and Instagram followers 370% across four channels, and the honest version is that most of what I tried did not work. There was no team to hand it to. That is the closest thing on my CV to what you are describing, and it is why I did not read your post as a warning.",
                "Since then I have been at Tata Trusts, where I evaluate and fund programmes, first across six sub-themes including education, scored on a 40-parameter framework, and now across a healthcare portfolio. The relevant part is not the size of it. It is that the work has consistently been whatever fell between other people's remits: the analysis nobody had run, the partner conversation nobody owned, the process that did not exist until someone wrote it down. I hold two mandates rather than one because things kept landing on my desk that were not anybody's job.",
                "What I am not going to pretend: I have not run growth for a consumer education business, I do not know your funnel, and I would be learning your market from a standing start. I am also coming from an institution rather than a startup, so I would be adjusting to your pace rather than arriving used to it.",
                "What I would bring is that I am genuinely not precious about the work, I write quickly and well, and I have a four-year habit of asking what the number actually is before asking what the plan is.",
                "Nikita Sachanandani<br>+91 7698030306 &middot; sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("<b>\"You manage a &#8377;450 crore portfolio. Why would you write blog posts?\"</b>", "The question the entire post exists to ask, and a weak answer ends it. Do not say you are excited to learn. Say the true thing: the portfolio is scale, not ownership, and you have been recommending things other people then live with. Then go straight to Tiff.in, where nobody was going to write the content if you did not. Concrete beats sincere here."),
            ("\"Why education, when your background is healthcare?\"", "Answer honestly rather than manufacturing a lifelong passion. Education was in your original remit at the Trusts, evaluated on a 40-parameter framework. And your own route ran through a fellowship and a published paper, so research access is not an abstraction to you."),
            ("\"What would you do in your first month?\"", "Resist the strategy answer entirely, given what they have told you. The right answer is that you would ask what is currently not getting done because it is not anyone's job, take the least appealing item on that list, and finish it."),
            ("\"What is your compensation expectation?\"", "Expect this to sit below your current fixed. Founder-led, largely bootstrapped, associate-shaped seat. Ask what band they have set rather than anchoring, and decide in advance what number you would actually accept."),
        ],
        "ask": [
            "Thirteen founder's office people in four years. How many left for something better, versus left because it did not work?",
            "What is currently falling between teams that this hire would pick up first?",
            "How did the Immerse acquisition change what the founder's office does?",
            "Fully remote across a global team: what hours does the role actually run on?",
            "What does someone need to have got right in six months for this to have worked?",
        ],
        "checklist": [
            "<b>Tiff.in is the centrepiece.</b> The portfolio goes underneath, not on top",
            "Both written answers say plainly what you have not done. His post rewards that",
            "<b>Ask the hours question before accepting anything.</b> Fully remote at a US-founded company is the one open gate",
            "Read one Lumiere blog post and one student research paper before applying",
            "Decide your real comp floor before the conversation, not during it",
            "Tracker updated with a follow-up 5 days out",
        ],
        "flags": [
            "<b>Not healthcare.</b> This spends the domain depth that is your sharpest differentiator. Fourth time this search has handed you that trade, after Cube, Honasa and Incresco.",
            "<b>The scope is genuinely junior at entry.</b> SEO blog posts and influencer lists are the stated starting work. The ceiling is real and documented, but the floor sits a long way below a &#8377;450 crore portfolio, and that gap is where the risk is.",
            "<b>Thirteen founder's office members in four years</b> at a company this size is high turnover. He frames it as graduation and names two genuine successes, Akanksha and Tung. Ask about the other eleven.",
            "<b>Fully remote is a real advantage</b>, only the second remote role on your board, but it is also the open gate. US founders, global students, unstated working window. Your timezone gate is absolute and this is unverified.",
            "Comp is unstated and likely below your current fixed.",
            "The Immerse Education acquisition in January 2026 is a genuine signal of scale, and the best thing to be curious about in an interview.",
        ],
    },
    "2070-health": {
        "title": "Associate, New Ventures",
        "company": "2070 Health",
        "place": "Mumbai",
        "tier": "Best combined score of the search",
        "fit": "4.3", "odds": "4.0",
        "resume": "resume/build/Nikita-Sachanandani-New-Ventures-2070.pdf",
        "resume_name": "Nikita-Sachanandani-New-Ventures.pdf",
        "verdict": "<b>Pankaj Jethwani is CEO of 2070 Health and Managing Partner of W Health Ventures. He is the person you already messaged last month.</b> The DM you sent on 10 September went to the man who runs this team. That is why odds score 4.0 rather than 2.5, and it is why the first move here is a question to him rather than a form. Separately: this is the first posting in a long while with <b>no degree gate at all</b>, and it names healthcare as a qualifying route in its own right.",
        "route": [
            ("Posting", "in.linkedin.com/jobs/view/associate-new-ventures-at-2070-health-4430947462", True),
            ("Live req on their own site", "2070health.com/career/career-detail/?id=D524C2B506", True),
            ("The discrepancy", "LinkedIn lists <b>Associate</b>, their careers page lists <b>Analyst</b> and marks it Urgent. <b>Ask before applying</b>", False),
            ("Referral", "<b>Dr Pankaj Jethwani</b>, CEO of 2070 Health and Managing Partner of W Health Ventures. Connection already accepted", False),
            ("Stated bar", "3&ndash;5 years in consulting, VC, start-ups <b>or healthcare</b>. <b>No degree requirement</b>", False),
            ("Location", "Mumbai. Mid-Senior level, full-time", False),
            ("The platform", "40+ staff. Six ventures launched: Elevate Now, Nivaan, Hoola Health, Reveal HealthTech, Everbright Health, Everhope Oncology", False),
            ("Fund behind it", "W Health: $65M+ deployed, 14 companies, <b>100% raised downstream capital</b>. Fund II closed &#8377;700 crore on 8 Sept", False),
        ],
        "route_note": "<b>Do not open the application form first.</b> The form asks how many years of consulting experience you have and offers only 1, 2, 3 or 4 as answers, and it asks you to self-rate financial modelling. Both are questions to walk into having decided, not to meet mid-form. And one message to Jethwani resolves which req is actually live while turning a cold application into a referred one.",
        "letters": [
            ("Message to Pankaj &middot; 166 characters", [
                "Hi Pankaj, I found the New Ventures opening at 2070. Your careers page lists Analyst, LinkedIn lists Associate. Which one is live? I&rsquo;d like to apply to the right one.",
            ]),
            ("If he never replied to the first message &middot; 175 characters", [
                "Hi Pankaj, I wrote last month about the company creation model. I&rsquo;ve since found the New Ventures opening at 2070. Is the Associate or the Analyst req live? I&rsquo;d like to apply.",
            ]),
            ("Cover note, if you apply cold", [
                "I am applying for the Associate, New Ventures role.",
                "The part of your posting I want to answer directly is pressure-testing a hypothesis before there is a company. For four years at Tata Trusts that has been most of my job. I screen 30 to 50 proposals a month against a 20 to 30 parameter framework, run deep-dive diligence on what survives, and take a recommendation to the CEO and Board of Trustees, who approve every commitment. Health-tech and AI diagnostics are sub-themes I own, so a large share of that is deciding which health technologies were genuinely ready to deploy and which worked once, in one place, with the founder in the room.",
                "The closest thing I have to your rapid-pilot work is how I structured technology pilots. I set a deliberately heavier evidence bar for them: evaluate the technology across varied conditions rather than favourable ones, and choose geographies that limited community risk and stripped out confounding factors, so that what came back was a signal rather than a story. I also built a geospatial map of every rupee the Trusts deployed across Indian states, comparing returns by geography and sub-theme, which showed identical interventions producing materially different results by region. It redirected allocation for two years.",
                "What I cannot claim: I have not built a valuation. My financial work is budgets, utilisation, variance and unit cost across a $51M portfolio, plus market sizing and unit economics modelling for a company I co-founded and pitched to 20+ funds. That is real, and it is not the same as a DCF or a cap table, and I would rather say so here than be found out in round two. It is also the one thing on your list I would be learning rather than bringing.",
                "I am also not a consultant. My four years are healthcare portfolio and diligence work, which your posting names as a qualifying route, and I read that as deliberate.",
                "Nikita Sachanandani<br>+91 7698030306 &middot; sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("<b>\"Rate your financial modelling, 1 to 5.\"</b>", "The form asks this outright, so decide the number before you open it. <b>Do not say 4.</b> Say 3 and define it in the same breath: budgets, utilisation, variance and cost-per-beneficiary across a $51M portfolio, plus market sizing and unit economics from Tiff.in. Then name the gap yourself: you have not built a valuation or a cap table. A defined 3 is more credible than an undefended 4, and this is a firm whose whole model is evidence bars."),
            ("<b>\"How many years in consulting?\" with only 1 to 4 on offer</b>", "There is no zero and the field is required. You do have advisory work that is honestly consulting-shaped: you advised partners on mobilising co-funding and government funding alongside Trust capital, and you wrote policy briefs for senior management. Selecting the lowest option and then correcting it in the first lines of the cover note is defensible. <b>This is your call, not mine</b>, and it is the strongest single argument for going through Jethwani, where the form does not exist."),
            ("\"Why leave a &#8377;450 crore portfolio for an Associate seat?\"", "Answer the title question head on rather than hoping it does not come up. The portfolio is scale without a feedback loop: you recommend, capital goes out, and the signal that comes back is a report rather than a result. Their model has an IC, a launch and a P&amp;L. That is the thing you are buying, and Associate is what the entry to it is called."),
            ("\"Walk us through a whitespace you would back in Indian healthcare.\"", "Near-certain, and it is the real test. Prepare one, with a size, a reason nobody has taken it, and how you would kill it cheaply in eight weeks. Build it out of a sub-theme you owned rather than something read in a report, and bring the pilot design, because their stated method is exactly that."),
            ("\"Which of our ventures would you have argued against?\"", "A studio that spends 12 to 18 months validating will respect a reasoned no far more than enthusiasm. Pick one of the six, form a real view, and say what evidence would change your mind."),
        ],
        "ask": [
            "The New Ventures req has been open a year and is still flagged Urgent. What has made it hard to fill?",
            "Associate on LinkedIn, Analyst on your careers page. Which seat is this, and what is the difference in scope?",
            "How much of the Associate's time is whitespace work versus portfolio support, in practice?",
            "What happens to someone who does this well for two years? Principal, a founding team, or the W Health side?",
            "Of the six ventures launched, which validation process would you run differently now?",
            "How does the studio's budget relate to Fund II's deployment pace?",
        ],
        "checklist": [
            "<b>Message Jethwani first.</b> One question, which req is live. It resolves the discrepancy and makes the application referred",
            "<b>Check the alumni signal before the interview.</b> 2070 Health on LinkedIn &rarr; People &rarr; past employees in New Ventures. Five minutes. It is the one dimension scored on no data",
            "<b>Decide your financial modelling number and your consulting answer before opening the form</b>",
            "Prepare one whitespace thesis with a size, a reason it is open, and a cheap kill test",
            "Read two ventures properly. Everhope Oncology and Hoola Health are the newest",
            "Comp: the form asks current and expected CTC. Decide both in advance, and keep the numbers out of the repo",
            "Tracker updated with a follow-up 5 days out",
        ],
        "flags": [
            "<b>The alumni half of the company signal is unverified.</b> The studio is four years old and no New Ventures leavers were traceable. Company signal is strong and checkable; alumni signal is not established. If that function churns, FIT drops from 4.3 to 4.1.",
            "<b>A New Ventures req open a year and still marked Urgent.</b> Either the bar is very specific or the seat keeps getting filled from inside. Worth asking directly, and a fair question rather than a rude one.",
            "<b>Valuation is the one genuine hole</b>, and financial modelling has now blocked seven lanes: ADB, Artha, Navi, Millennium, Pfizer, Rock Health and Pomoro. The difference here is that it is a skill line rather than a credential line. A skill line can be answered with evidence and an honest self-rating. A credential line cannot be answered at all.",
            "<b>&quot;Associate&quot; reads as a sideways step from Program Officer</b> to anyone outside venture. Inside it, it is the standard entry to the investing track, which is why the two-year trajectory scores 5. Expect to explain the title; do not let it put you off.",
            "<b>The studio is funded by the fund.</b> Fund II closed four weeks ago, so runway is as fresh as it will ever be, but the seat ultimately depends on deployment pace.",
            "<b>This is the highest transition value on your board.</b> Two years here and the philanthropy framing is gone, which is the whole point of the search.",
        ],
    },
    "health-progress-hub": {
        "title": "Research &amp; Scaling Officer",
        "company": "Health Progress Hub",
        "place": "Remote, any time zone &middot; contractor &middot; 8&ndash;40 hrs/week",
        "tier": "Deadline 15 October",
        "fit": "1*", "odds": "&mdash;",
        "resume": "resume/build/Nikita-Sachanandani-Research-Scaling-HPH.pdf",
        "resume_name": "Nikita-Sachanandani-Research-Scaling.pdf",
        "verdict": "<b>Read this before anything else.</b> The form says: &ldquo;You may use AI tools, for example to edit your wording, but the examples and judgements in your answers should be your own&hellip; since we use tools to check for heavily AI-generated text, any undisclosed use we find will disqualify your application.&rdquo; <b>So there are no paste-ready answers in this kit, deliberately.</b> Every block below gives you the question, which of your experiences answers it, the exact facts and numbers to use, and what to leave out. You write the sentences. <b>The *1 on FIT is not a typo:</b> as a full-time job this fails the sector gate and scores 1. As a 12-hour-a-week contract it is the only thing on your board that pays you to build the modelling evidence seven lanes have turned you down for. Take it in that shape and no other.",
        "route": [
            ("Apply at", "forms.gle/bTDqx66pTLh85GWq5", True),
            ("Deadline", "<b>15 October 2026.</b> They review as applications arrive and may offer before it, so early is materially better", False),
            ("Form length", "<b>11 pages, 30&ndash;60 minutes.</b> Every question is listed below, so you can draft offline and paste in once", False),
            ("Process", "Form &rarr; <b>paid</b> 2.5-hour test task &rarr; interview &rarr; live work test &rarr; interview &rarr; references", False),
            ("Speed", "&ldquo;We review every application within 48 hours and may make an offer within a week&rdquo;", False),
            ("Rate", "<b>Pick $16&ndash;25.</b> Their whole team is at $21 and they state a &ldquo;strong focus on cost-efficiency&rdquo;", False),
            ("Hours", "<b>Say 12.</b> Above the floor of 8, so you are not the minimum bidder, and still compatible with a full-time role", False),
            ("Contact", "berke@healthprogresshub.org", True),
            ("Sign-in", "The form saves progress only if you sign in to Google. <b>Do that first</b> &mdash; 11 pages is too far to lose", False),
        ],
        "route_note": "<b>The sentence that decides this application:</b> &ldquo;Several questions ask you to back up your answer with a link to the work or the name and e-mail of someone we could ask about it&hellip; <b>Answers we cannot check carry less weight.</b>&rdquo; Almost everything you have done at the Trusts is internal, so by default your strongest answers are your least checkable ones. <b>The fix is to name a partner-organisation contact rather than a Trusts colleague</b> &mdash; IISc, C-CAMP, the George Institute, NIMHANS, Apollo, St Jude. They sat on the other side of the programmes you designed and the budgets you assessed, they saw the work directly, and naming them costs you nothing internally. That single move converts most of this form from unverifiable to verifiable.",
        "letters": [
            ("Q: The project you are most proud of, and one thing you would do differently now &middot; 120 words", [
                "<b>Use the geospatial heat map.</b> It is your strongest piece of work and it is the closest thing on your CV to what HPH actually sells.",
                "Facts to use: every rupee the Trusts deployed, mapped across Indian states, scored and compared by geography and sub-theme; it showed identical interventions producing materially different results by region and terrain; it directly shaped portfolio allocation from 2022 to 2024, changing where capital went and which programmes were concentrated on.",
                "<b>The &ldquo;differently now&rdquo; half is the half they are actually reading.</b> A weak answer makes it cosmetic. Pick something real and structural: the model scored returns but did not separate how much of the variation came from the intervention versus the delivery conditions around it, so it told you where results differed without fully explaining why. That is an honest limitation of a weighted-factor approach and it is exactly the methodological conversation they want to have.",
                "<b>Checkable by:</b> this one is internal. Name a partner-organisation contact from a programme whose allocation the map changed, or say plainly that the output is internal to the Trusts and offer to walk through the method on a call.",
            ]),
            ("Q: A period with three or more pieces of work at once, how you tracked them, and one moment tracking caught a problem first &middot; 100 words", [
                "<b>The dual mandate is the answer.</b> You hold both Program Officer and Grants Manager responsibilities, the only person on the team carrying two roles, across 40+ programmes.",
                "The tracking facts: portfolio dashboards you built and presented to the CEO; fund utilisation tracking and variance analysis across the whole portfolio; screening 30 to 50 proposals a month against a fixed framework while design cycles of two to three months ran in parallel.",
                "<b>The &ldquo;caught it first&rdquo; moment is the part that needs a specific incident, and only you have it.</b> The natural place to look is your gatekeeping role: you evaluated every partner organisation&rsquo;s budget in the health theme for gaps, and for whether the numbers actually reflected programme activity and intensity, before anything reached CEO and Board approval. There will be a case where variance analysis surfaced a problem before the partner reported it. <b>Use that one, with the detail.</b>",
            ]),
            ("Q: A time you knew in advance your work would be late, and told the person waiting &middot; 100 words", [
                "<b>I cannot draft this one for you and you should be wary of anyone who offers to.</b> It needs a real incident: what you said, how far ahead, and what happened.",
                "What they are testing is named explicitly in the job description: &ldquo;If a project becomes unmanageable or proves more difficult than you envisioned, you don&rsquo;t shy away from re-scoping it or asking for help.&rdquo; So the answer they want is not heroic recovery. It is early, specific escalation and a re-scope.",
                "Where to look in your own record: a design cycle that ran past two to three months because a partner dependency slipped, or a Board-bound recommendation that needed more diligence than the cycle allowed. The strong version names the person, the lead time, and the decision that followed.",
                "<b>Do not pick an example where it turned out fine because you worked a weekend.</b> That answers a different question and a team that publishes its pay rates will read it as the wrong instinct.",
            ]),
            ("Q: Building context on an unfamiliar domain in days, then making a judgement someone acted on &middot; 80 words", [
                "<b>Two candidates, both real. Pick whichever you remember in more detail.</b>",
                "<b>The stronger one, if you have the specifics:</b> your technology pilots. You structured them under a deliberately heavier evidence bar, evaluating the technology across varied conditions rather than favourable ones, and selecting geographies that limited community risk, externalities and confounding factors. Health-tech and AI diagnostics were owned sub-themes, so you were forming views on which technologies were ready to deploy and which worked once, in one place, with the founder present. Name a specific technology, the window you had, and whether the judgement held.",
                "<b>The alternative:</b> your original remit covered six sub-themes &mdash; education, WASH, nutrition, health, rural upliftment, urban poverty &mdash; scored on a 40-parameter framework, with course corrections proposed and Board advice given on which investments were working. Moving between six domains at speed is the same muscle.",
            ]),
            ("Q: Career choices driven by global health or development, and what they cost you &middot; 80 words", [
                "<b>Lead with Tiff.in, because it is the only answer here with a real price attached.</b>",
                "The facts: you co-founded Tiff.in Productions, selected for Ashoka University incubation as one of three teams funded out of thirty-five, did the market sizing and unit economics, built the investor-ready projections, and pitched 20+ VC funds and the founders of a major Indian e-commerce platform. <b>Then you left it, inside a year, for a development portfolio.</b> That is founder status and equity given up for this work, and it is checkable with your co-founder.",
                "The second half, if there is room: your in-progress paper comparing the US and Indian health economies, arguing for preventive healthcare investment, is unpaid work you are doing anyway.",
                "<b>What to leave out:</b> do not frame the cost as what the sector has done to your options since. They are asking what you gave up to get here, not what you want to leave.",
            ]),
            ("Q: Research you managed that other people did &middot; 100 words", [
                "<b>Answer this one honestly as the stretch it is.</b> The question allows it: &ldquo;If you have not managed research, you can describe analysis or project management you have run instead.&rdquo;",
                "You have not managed researchers. You have run the adjacent thing: two-to-three-month design cycles built from the ground up with implementing partners, mapping multi-stakeholder dependencies and anticipating roadblocks, where the partner did the work and you owned whether it landed. Name the output, the deadline, what went wrong, and &mdash; the part they actually asked &mdash; whether you knew before the deadline that it would finish.",
                "<b>Say in one clause that this was programme delivery rather than research management.</b> The job description asks for someone who gives &ldquo;direct, useful feedback&hellip; including to people who know their subject better than you do,&rdquo; and you do have that: you assessed founders and programme leaders on domain knowledge you did not hold yourself. Make that link and let them judge the distance.",
            ]),
            ("Q: Research or analysis in global health, development or health policy that you did yourself &middot; 60 words", [
                "<b>This is the one question where you have a public, linkable artifact. Use it.</b>",
                "&ldquo;Persistence of Informal Social Networks in the Indian Textile Market: A Case Study of Surat&rdquo;, <i>Journal of Enterprising Culture</i>, September 2023, Volume 31 Issue 3. You built a comparative metric for the role of social networks in formal versus informal business from interviews across the entire supply chain, from weavers and manufacturers to end consumers, and <b>applied the World Bank&rsquo;s Doing Business methodology</b> to gauge informality and network dependence.",
                "It is not global health, so say so rather than stretching it. What it demonstrates is the method this role runs on: taking an established cross-country framework and testing what it misses about one specific place. <b>That is the same thing HPH describes as &ldquo;finding what a comparison across countries gets wrong about a specific place.&rdquo;</b> Make that connection in one sentence and link the paper.",
                "Then add the heat map and the in-progress US-versus-India health economies paper as the health-specific work, if the word count allows.",
            ]),
            ("Q: The four-area grid, and the work behind each &middot; 40 words per area", [
                "<b>My read on each, for you to correct. The options are: no experience / read around it / worked in an adjacent field / done applied work with a named output.</b>",
                "<b>Lead exposure &mdash; &ldquo;No experience.&rdquo;</b> You have nothing here and claiming otherwise is pointless when one of their partners is the Lead-Acid Battery Recycling Initiative.",
                "<b>Transformative AI and global health &mdash; &ldquo;applied work with a named output.&rdquo;</b> Health-tech and AI diagnostics were owned sub-themes on a $51M portfolio: you decided which AI diagnostic technologies got funded and structured their pilots under a heavier evidence bar. Name the technology area and say the output is internal to the Trusts.",
                "<b>Market shaping for essential medicines &mdash; probably &ldquo;read around it.&rdquo;</b> Antimicrobial resistance was a secondary lead, which touches antibiotic access and stewardship, but that is adjacent to drug-market mechanics rather than market shaping. <b>Pick &ldquo;adjacent field&rdquo; only if you can name the specific work</b>, because the next field asks you to.",
                "<b>Health systems strengthening, including CHWs &mdash; &ldquo;applied work with a named output&rdquo;</b>, and this is your second-strongest area after prioritisation. Comprehensive primary health was an owned sub-theme, and you deliberately built government linkages so programmes ran through existing systems and schemes rather than creating parallel infrastructure. <b>[VERIFY] Confirm whether any programme you owned worked directly with ASHAs, ANMs or other community health workers</b> &mdash; if so, say it explicitly, because four of their fourteen sprint projects are CHW projects.",
            ]),
            ("Q: Prioritisation research &mdash; say YES. Then: strongest line, weakest line, and the country question", [
                "<b>Yes. This is your lane, it is their largest area of work, they say more organisations ask for it than they can serve, and the AIM cohort arrives from late November.</b>",
                "<b>Strongest line, 80 words:</b> the heat map again, but answer the three things asked &mdash; what the output was, who used it, what they did with it. Output: a scored geospatial comparison of returns by geography and sub-theme. Who used it: the CEO and the portfolio function. What they did: changed allocation across 2022 to 2024, concentrating capital where delivery conditions supported it.",
                "<b>Weakest line, 40 words.</b> Do not manufacture modesty, and do not pick something that disqualifies you. The honest answer is the quantitative depth beneath the scoring: you have built weighted comparisons and variance analysis, not formal statistical modelling of the drivers. Say how you are closing it, concretely, not aspirationally.",
                "<b>And the one that matters most:</b> &ldquo;Pick an intervention and a country you know well. What is a foreign charity running that intervention likely to get wrong in that country?&rdquo; 60 words, and they tell you they will return to it on the call. <b>You can answer this better than almost anyone who applies, and it is the single strongest thing in your whole application.</b> You have the finding, from your own data: identical interventions produced materially different results across Indian regions and terrains. And you have the design response: you built government linkages specifically to avoid creating parallel infrastructure, which is the most common and most expensive thing a foreign charity gets wrong in India. <b>Pick one intervention, name the state, and say what breaks.</b> Concrete beats general here by a wide margin.",
            ]),
            ("Q: Research strategy &mdash; also YES, and the evidence-gap question", [
                "<b>Say yes.</b> It only starts from December, so it sequences after the sprint rather than competing with it, and it is where the build-from-zero value sits: &ldquo;develop HPH&rsquo;s research agenda&hellip; the questions worth answering, who else is working on them.&rdquo;",
                "<b>If you are short on time, this is the section to answer adequately and prioritisation is the section to answer excellently.</b> Do not let a thin research-strategy answer dilute a strong prioritisation one.",
                "<b>The evidence gap, 80 words.</b> You ran into a real one and it came out of your own work: <b>identical health interventions produced materially different returns across Indian geographies, and nobody has systematically explained why.</b> Answer their three parts &mdash; where you hit it (building the heat map, when the pattern showed up and the model could not account for it), why it would unlock other work (every funder and charity choosing where to deploy is guessing at the same question), and why nobody has answered it (the data sits inside individual funders&rsquo; portfolios, is never pooled, and no single organisation has both the data and a reason to publish it).",
                "<b>That last clause is the strong part.</b> &ldquo;Why has nobody answered it&rdquo; is where most applicants will be vague, and you have a structural reason rather than a shrug.",
            ]),
            ("Q: The unscored closing section &mdash; and the one question I will not answer for you", [
                "<b>Which area would you most want to work on:</b> pick <b>&ldquo;Prioritization research and analysis.&rdquo;</b> It is where you are strongest, where their demand is highest, and it keeps your application coherent. Transformative AI is the honest second and the better long-term differentiator &mdash; mention it in the optional free-text rather than splitting your answer.",
                "<b>Considering founding a non-profit or starting your own research project:</b> &ldquo;Maybe&rdquo; is the true answer, and you have the evidence for it &mdash; the in-progress US-versus-India health economies paper. They treat this positively: &ldquo;We also work part-time with people building their own projects.&rdquo;",
                "<b>&ldquo;Name one kind of task we should not assign you&rdquo; &mdash; required, and I am not inventing this one.</b> It asks what you do not enjoy or are not good at, and a fabricated answer here is both dishonest and easy to catch in a live work test. <b>Tell me what it actually is and I will help you phrase it.</b> What it should not be: anything central to the role, and not a humblebrag. What it could honestly be, if true: work with no decision attached to it at the end.",
                "<b>Optional &ldquo;one thing we could help you with&rdquo;:</b> worth using, not skipping. The honest ask is methodological &mdash; formal training in the quantitative side of prioritisation modelling, which is the gap you named as your weakest line. Asking for the thing you already admitted is consistent, and they offered.",
                "<b>Where did you hear about this opportunity:</b> answer plainly and accurately.",
            ]),
            ("Q: AI disclosure &mdash; the exact shape of an honest answer", [
                "<b>Disclose. Undisclosed use found later disqualifies the application, and they say they run detection tools.</b>",
                "The honest description of what happened here: you used an AI assistant to assemble the questions in advance, to identify which of your own experiences answered each one, and to check wording and word counts. <b>The examples, the judgements and the sentences are yours.</b>",
                "<b>Which is why the sentences have to actually be yours.</b> If you paste any block of this kit as prose, the disclosure stops being true and the detection tool is the least of the problems. Use the facts, write the answer.",
                "It is not scored. A short, specific, plainly-true answer is strictly better than a defensive one.",
            ]),
        ],
        "questions": [
            ("<b>&ldquo;What is a foreign charity likely to get wrong in India?&rdquo;</b>", "They tell you in the form that they will come back to this on the call, so treat the written answer as an opening and prepare the long version. Have one intervention, one state, and a specific failure mode, plus what you would have done instead. Your parallel-infrastructure point is the spine: programmes that build their own delivery layer alongside a government system that already exists, then cannot hand over."),
            ("<b>&ldquo;Walk us through the heat map.&rdquo;</b>", "Near-certain, because it is the most relevant thing you have and you will have cited it three or four times across the form. Be ready on method, not just result: what the parameters were, how they were weighted, what the data source was, where the model was weakest. <b>A team whose whole product is prioritisation methodology will probe the method.</b>"),
            ("\"Why a part-time contract, when your CV is a full-time portfolio role?\"", "They will ask, and the honest answer is good: you want to do this specific work, you can commit 12 real hours, and you would rather be accurate about capacity than promise 40 and deliver 15. Their own words are &ldquo;we appreciate honesty over more availability.&rdquo; <b>Do not improvise around your current situation</b> &mdash; decide the sentence in advance and keep it short."),
            ("\"You have not managed researchers. Why should we put you on research management?\"", "Fair question, since it is the one mandatory stream. Answer with the adjacent muscle rather than a denial: you gave direct feedback to founders and programme leaders whose domains you did not hold, on work your recommendation then depended on. Then say what you would need from them in week one, which signals you have thought about the gap rather than hoping they miss it."),
            ("<b>&ldquo;What would you do with the AIM cohort choosing a first country?&rdquo;</b>", "This is their live engagement from late November, so it is the most likely scenario question. Have a method ready: what you would want to know before scoring anything, which parameters you would refuse to weight without local validation, and how you would test the model against one country someone on the ground knows well. That last step is their stated view of what goes wrong, so showing it unprompted lands."),
        ],
        "ask": [
            "The job description says the applied research has been &ldquo;limited and mostly internal&rdquo; so far. What does the first genuinely external output need to look like?",
            "You are three people at about 1.5 FTE and you have just received funding. How many hires does this round cover, and where does this role sit in that?",
            "On prioritisation, how often does your review change an organisation&rsquo;s decision versus confirm it?",
            "The sprint runs to 15 November with mentors across African governments and US-based founders. <b>What does the meeting rhythm actually look like, and what is expected synchronously?</b>",
            "You publish your pay and you review in 48 hours. What else do you do differently from how most non-profits run, and what has that cost you?",
            "If this goes well in six months, what does the extended version look like &mdash; more hours, a different scope, or a different title?",
        ],
        "checklist": [
            "<b>Sign in to Google before starting.</b> 11 pages without saved progress is a bad afternoon",
            "<b>Upload the tailored CV to Drive and set sharing to &lsquo;Anyone with the link can view&rsquo;</b> before you start &mdash; the link is a required field on page 1 and a dead link is a silent fail",
            "<b>Line up two referees with email addresses first.</b> Partner-organisation contacts over Trusts colleagues &mdash; see the note above. This is the hardest item here, so do it before the writing, not after",
            "<b>Check your employment contract for an exclusivity or outside-work clause</b> before you accept anything paid. This is the one risk in the kit that is not about the application",
            "Decide in advance: <b>12 hours, $16&ndash;25, yes to prioritisation, yes to research strategy</b>",
            "<b>Draft the long answers outside the form</b>, in your own words, then paste. Nine of them have word limits between 40 and 120",
            "Have the published paper link to hand: <i>Journal of Enterprising Culture</i>, Sept 2023, Vol 31 Issue 3",
            "<b>Answer the AI disclosure truthfully</b>, which means not pasting prose from this kit",
            "Tell me what belongs in &ldquo;one task we should not assign you&rdquo; and I will help you phrase it",
            "<b>Apply well before 15 October.</b> They may offer before the deadline",
        ],
        "flags": [
            "<b>FIT is 1 as a job, and that is not a formality.</b> Sector gate fails; both carve-out doors close (AI is one of four research areas rather than the substance, the title is &lsquo;Officer&rsquo;, and there is no principal whose orbit is itself a credential). <b>Full-time this is a lateral back into the sector you are leaving.</b> Part-time it is a tool. Nothing about the kit changes that line.",
            "<b>What it builds is analytical modelling, not financial modelling.</b> A weighted factor model is not a DCF, a comparables set or a cap table. This strengthens an answer to &ldquo;strong analytical and quantitative modelling&rdquo; and gives you a second, current, non-Tata reference for it. <b>It does not answer 2070 Health&rsquo;s &ldquo;proficiency in valuation&rdquo; or Artha&rsquo;s buy-side modelling bar.</b> Those still need something else, and claiming otherwise would repeat the Tiff.in error.",
            "<b>Verifiability is the structural problem with your application.</b> Your best material is internal to the Trusts, and they state plainly that unverifiable answers carry less weight. The partner-organisation referee route is the fix, and it needs doing before you write.",
            "<b>Employment contract risk.</b> Paid contract work for another organisation while employed full-time may breach an exclusivity clause. <b>Check before accepting, not before applying</b> &mdash; applying costs you nothing either way.",
            "<b>The process is about six hours</b> &mdash; form, 2.5-hour paid test task, two interviews, a live work test &mdash; for a part-time six-month contract. The test task being paid offsets some of that. Worth going in knowing the price.",
            "<b>&ldquo;Remote, any time zone&rdquo; is a statement about where you sit, not about when the calls are.</b> Ask the meeting-rhythm question. Your timezone constraint has been absolute since day one and this is the only gate still genuinely open.",
            "<b>On a CV, &lsquo;Research &amp; Scaling Officer&rsquo; sitting under &lsquo;Program Officer&rsquo; reads as more of the same</b> to a commercial reader. List it as a contract engagement, with the hours, rather than as your new role.",
            "<b>The team is three people at roughly 1.5 FTE, newly funded, and this is their first hire.</b> That is genuine upside on scope and genuine fragility on stability. The six-month contract is honest about which.",
        ],
    },
    "healthify": {
        "title": "Founder's Office &mdash; Strategy",
        "company": "Healthify",
        "place": "Bengaluru",
        "tier": "Best combined score of the scan",
        "fit": "3.7", "odds": "3.7",
        "resume": "resume/build/Nikita-Sachanandani-Partnerships-Healthify.pdf",
        "resume_name": "Nikita-Sachanandani-Partnerships.pdf",
        "verdict": "<b>The title is misleading in your favour.</b> This is not a founder&rsquo;s office job &mdash; it is a <b>pharma partnerships leadership role</b>, and partnerships is the strongest thing on your CV after the heat map. Two lines make it the pick of the scan: the band is <b>&ldquo;2+ years of experience&rdquo;</b>, the widest of the entire search, and the education line is <b>&ldquo;MBA or equivalent postgraduate degree from a leading institution <i>preferred</i>&rdquo;</b> &mdash; preferred, not required, and your P.G.D. from Ashoka is a postgraduate degree from a leading institution. <b>After nineteen roles killed on a degree line, this is one you arguably satisfy outright.</b>",
        "route": [
            ("Posting", "linkedin.com/jobs/view/4470904210", True),
            ("Referral", "<b>Prerna T.</b>, Strategic Talent Acquisition and HR leader &mdash; she posted it, and LinkedIn offers &ldquo;message the job poster&rdquo;. <b>DM her the same day you apply</b>", False),
            ("Band", "<b>2+ years</b> in strategy consulting, healthcare, pharma, digital health, BD or partnerships", False),
            ("Education", "MBA or equivalent postgraduate from a leading institution, <b>preferred</b>", False),
            ("What they do", "India&rsquo;s leading <b>AI-powered GLP-1 and obesity management platform</b>", False),
            ("Location", "Bengaluru. Mid-Senior level, full-time", False),
            ("The real job", "Own pharma partnerships in obesity, diabetes and metabolic health; lead commercial discussions and contract negotiation; design and run <b>Patient Support Programs</b> for GLP-1 therapies", False),
            ("Competition", "200+ applicants, posted ~1 week ago. <b>The DM is what separates you from the pile</b>", False),
        ],
        "route_note": "<b>Apply and DM Prerna on the same day.</b> With 200+ applicants the application alone is a lottery ticket; a short note to the person who posted the role is the whole edge, and she has explicitly opened that channel. Keep the DM under 200 characters and lead with partnerships, not with the portfolio size.",
        "letters": [
            ("LinkedIn DM to Prerna &middot; 189 characters", [
                "Hi Prerna, I&rsquo;ve just applied for the Founder&rsquo;s Office strategy role. I&rsquo;ve spent four years originating and closing healthcare partnerships at Tata Trusts. Happy to send a short note on fit?",
            ]),
            ("Cover note", [
                "I am applying for the Founder&rsquo;s Office, Strategy role.",
                "The part of the posting I can answer directly is the partnerships half. For four years at Tata Trusts I have been the external-facing owner of institutional relationships across a $51M healthcare portfolio: I originated and closed fifteen-plus partnerships with hospitals, research institutes and clinical networks, found the targets myself, built the relationships, and structured the terms. Then I ran them &mdash; the governance, the reporting cadence, and the performance review against plan.",
                "What makes the Patient Support Program work legible to me is the other half of my job. I screen thirty to fifty proposals a month against a fixed framework and run diligence on what survives, and health-tech and AI diagnostics are the sub-themes I own. So a large part of the last four years has been deciding which health technologies and delivery models actually change behaviour at scale, and which worked once, in one place, with the founder in the room. A GLP-1 adherence programme is that question with a commercial contract attached to it.",
                "What I will not claim: I have not worked inside pharma, and I have not negotiated a pharma commercial contract. My partnership counterparties were hospitals, institutes and government systems rather than pharmaceutical companies, and the terms I structured were grant and co-funding terms rather than commercial ones. I would be learning the pharma side of the table.",
                "What I would bring is the habit of building the operating mechanism before the programme launches rather than after it, which is the thing that usually decides whether a partnership programme delivers. And I have spent four years being the person who asks what the number actually is before asking what the plan is.",
                "Nikita Sachanandani<br>+91 7698030306 &middot; sachanandani.nikita@gmail.com",
            ]),
        ],
        "questions": [
            ("<b>&ldquo;What do you know about GLP-1s and the obesity market in India?&rdquo;</b>", "<b>Prepare this properly or do not apply.</b> It is the one question you cannot improvise, and your portfolio did <b>not</b> include diabetes, obesity or metabolic health &mdash; do not imply otherwise. Learn the actual shape: who the Indian players are, what semaglutide going off-patent in India means for volume, why adherence collapses after month three, and what a pharma company is actually buying when it funds a support programme. Then connect it to what you do know: you have spent four years on why proven interventions fail to reach people."),
            ("\"Have you negotiated a commercial contract?\"", "No, and say so in one clause rather than hedging. You have structured fifteen-plus partnership agreements including co-funding terms, and you were the <b>financial gatekeeper</b> who evaluated every partner budget in the health theme before it reached CEO and Board approval. That is commercial judgement applied from the other side of the table. <b>Then say what you would want in your first month</b> &mdash; sight of two existing pharma contracts and a conversation with whoever has run one."),
            ("<b>&ldquo;Why are you leaving a &#8377;450 crore portfolio for this?&rdquo;</b>", "The honest answer is the strong one: the portfolio is scale without a feedback loop. You recommend, capital goes out, and what comes back is a report rather than a result. A partnership with a pharma company has a contract, a KPI and a renewal decision. <b>Do not dress this up as passion for obesity care</b> &mdash; they will see through it, and the structural answer is better."),
            ("\"Walk us through a partnership you built from nothing.\"", "Near-certain, and you have fifteen to choose from. Pick one where you found the counterparty yourself, name what they wanted that you had to construct, what nearly killed it, and what the governance looked like after signature. <b>The post-signature half is where most candidates stop talking and where this role actually lives.</b>"),
            ("\"How would you design a patient support programme for a new GLP-1 launch?\"", "Scenario question, and your programme-design record answers it. Two-to-three month design cycles built from the ground up with the delivery partner, multi-stakeholder dependency mapping, and designing for continuity beyond the funding period. Say what you would measure in week one and what evidence would make you stop."),
        ],
        "ask": [
            "How many pharma partnerships are live today, and what does the pipeline look like for the next year?",
            "Who owns the commercial relationship today, and what changes when this role exists?",
            "On a patient support programme, what does the pharma partner actually hold you accountable for &mdash; enrolment, adherence, or outcomes?",
            "How do Product and Clinical get involved, and where does that handoff usually break?",
            "The title says founder&rsquo;s office but the job is partnerships. Which is it in practice, and who do I report to?",
            "What has Healthify tried in pharma partnerships that did not work?",
        ],
        "checklist": [
            "<b>Apply and DM Prerna the same day.</b> 200+ applicants makes the DM the edge, not the application",
            "<b>Spend an hour on the GLP-1 market in India before you apply</b>, not before the interview. It will show in the cover note",
            "<b>Say plainly in the note that you have not worked inside pharma.</b> They asked for pharma-ecosystem understanding as <i>preferred</i>, so honesty costs nothing and bluffing costs everything",
            "<b>Lead with partnerships, not the portfolio number.</b> The &#8377;450 crore is context; fifteen partnerships closed is the qualification",
            "Your P.G.D. from Ashoka satisfies the education line &mdash; <b>make sure it is visible, not buried</b>",
            "Do NOT claim diabetes, obesity or metabolic health experience. It was not in your portfolio",
            "Tracker updated with a follow-up 5 days out",
        ],
        "flags": [
            "<b>The degree line is one you meet, which is new.</b> &ldquo;MBA or equivalent postgraduate degree from a leading institution, preferred.&rdquo; Nineteen roles this search died on a harder version of that sentence. Worth noticing which postings are actually open to you.",
            "<b>The metabolic domain is a genuine hole.</b> Your owned sub-themes were health-tech, AI diagnostics, maternal health, geriatric and palliative care, and primary health. <b>Diabetes and obesity were not among them.</b> They ask for that understanding as <i>preferred</i>, so it is survivable &mdash; but only if you close it with reading rather than papering over it.",
            "<b>No pharma-side experience and no commercial contract negotiation.</b> Both are central to the role. Your counterparties were hospitals, institutes and government systems, and your terms were grant and co-funding terms.",
            "<b>200+ applicants.</b> A named recruiter who has opened a DM channel is the only reliable way through that, and it expires &mdash; she will be screening within days.",
            "<b>Alumni signal is unverified (scored 3, no-data).</b> Healthify has pivoted into GLP-1 from a broader health and fitness app. Worth five minutes on LinkedIn to see whether the strategy function churns.",
            "<b>&ldquo;Founder&rsquo;s Office&rdquo; in the title and partnerships in the body is a mismatch worth resolving on the call.</b> If it is really a BD seat, that is fine &mdash; but know it before you accept, because it changes what the next role after it looks like.",
        ],
    },
    "dozee": {
        "title": "Founders Office &mdash; Program Manager",
        "company": "Dozee",
        "place": "Bengaluru",
        "tier": "Highest FIT of the scan",
        "fit": "3.9", "odds": "3.3",
        "resume": "resume/build/Nikita-Sachanandani-Founders-Office-Dozee.pdf",
        "resume_name": "Nikita-Sachanandani-Founders-Office.pdf",
        "verdict": "<b>The work is what you already do.</b> Translate C-suite priorities into structured plans with owners and timelines, own cross-functional programmes and business reviews, run the leadership cadence, synthesise data into leadership dashboards, and represent the CxO&rsquo;s office externally. You present investment briefs and portfolio dashboards <b>directly to the CEO</b>, report to the <b>Board of Trustees</b>, and carry <b>two mandates across 40+ concurrent programmes</b>. The band is 3&ndash;5 years and you are at 4y2m, dead centre. And the education line reads <b>&ldquo;BTech/MBA or any equivalent qualification&rdquo;</b> &mdash; that &ldquo;or any equivalent&rdquo; is a soft gate, not a wall.",
        "route": [
            ("Posting", "linkedin.com/jobs/view/4475582190", True),
            ("Band", "<b>3&ndash;5 years</b> in program management, business operations, consulting, strategy, founder&rsquo;s office or cross-functional project management", False),
            ("Education", "<b>&ldquo;BTech/MBA or any equivalent qualification&rdquo;</b> &mdash; soft, not a wall", False),
            ("What they do", "<b>India&rsquo;s No.1 contactless Remote Patient Monitoring company.</b> AI-powered RPM and early-warning systems", False),
            ("Scale", "<b>300+ hospitals, 16,000+ beds across 4 countries</b>, 1M+ patients monitored, 35,000+ life-saving alerts. World&rsquo;s first non-contact blood pressure monitoring", False),
            ("Location", "Bengaluru, onsite. Relocation from Mumbai", False),
            ("Their own framing", "&ldquo;This is <b>not</b> a traditional Program Manager, Executive Assistant, or strategy-only role. It is a high-trust, high-ownership role&rdquo;", False),
            ("Timing", "<b>Apply immediately.</b> The posting reads two hours old but shows 200+ applicants, so it is likely a repost and older than it looks", False),
        ],
        "route_note": "<b>ODDS is 3.3 and the only thing holding it there is the referral path, scored 2.</b> Everything else is a 4. The rubric is explicit that referral is the dimension you can most change: a warm introduction here moves ODDS from 3.3 to about 4.4, which is more than another application is worth. <b>So apply today, then spend the next hour on LinkedIn looking for a route into Dozee rather than on a second application.</b> They are a Bengaluru health-AI company with 300+ hospital customers, so the YIF network and your Trusts hospital relationships are both plausible doors.",
        "letters": [
            ("Cover note", [
                "I am applying for the Founders Office, Program Manager role.",
                "Your posting says this is not a strategy-only role and not an executive assistant, and that it lives at the point where leadership priorities turn into execution. That is a fair description of what I have done for four years, so I will be specific rather than general.",
                "At Tata Trusts I hold both Program Officer and Grants Manager mandates &mdash; the only person on the team carrying two &mdash; across a $51M healthcare portfolio and 40+ concurrent programmes. Practically, that means I run the cadence: the performance dashboards and investment briefs that go directly to the CEO, the recommendations that go to the Board of Trustees, the utilisation and variance tracking that tells us which programmes are drifting, and the dependency maps that say who owes what to whom before a design cycle starts. I was also the financial gatekeeper for the whole health theme: every partner budget in the portfolio went through my review for whether the numbers reflected what was actually being delivered, before anything reached CEO or Board approval.",
                "The measurable version: a 60% improvement in proactive origination targets and cost-per-beneficiary efficiency across the portfolio. And the piece of work I would most want to show you is a geospatial model of every rupee we deployed across Indian states, scored by geography and sub-theme, which showed identical interventions producing materially different results by region and changed where we put capital for two years.",
                "Health-tech and AI diagnostics are the sub-themes I own, so I have spent four years deciding which health technologies were ready to deploy and which worked once in favourable conditions. Dozee sits on the right side of that line, which is why I am writing rather than applying broadly.",
                "What I would be learning: I have evaluated AI products rather than built or operated them, and I am not going to pretend the distance is zero. I use AI tooling in my own analysis and reporting, and I would want to go deep on your product and roadmap early enough to be useful in a product conversation rather than a spectator in one.",
                "Nikita Sachanandani<br>+91 7698030306 &middot; sachanandani.nikita@gmail.com",
            ]),
            ("LinkedIn note, if you find someone at Dozee &middot; 191 characters", [
                "Hi, I&rsquo;ve applied for the Founders Office role. I run the CEO and Board reporting cadence across 40+ healthcare programmes at Tata Trusts. Would value 10 minutes on what the role really needs.",
            ]),
        ],
        "questions": [
            ("<b>&ldquo;Tell us about your exposure to AI products and AI-led workflow automation.&rdquo;</b>", "<b>This is the one real gap and it is explicitly in the requirements, so it will be asked.</b> Do not overclaim. The honest and still-strong answer: you have spent four years as the person deciding which AI health technologies deserved funding, including AI diagnostics as an owned sub-theme, and you structured their pilots under a deliberately heavier evidence bar. <b>Then be concrete about your own tooling</b> &mdash; what you actually use AI for in analysis, reporting and tracking. Have one real example. A vague answer here is the likeliest way to lose this."),
            ("<b>&ldquo;What was the 60% improvement, and how was it measured?&rdquo;</b>", "<b>They asked for &lsquo;demonstrated ability to deliver measurable improvements&rsquo;, so this number is why your CV gets read &mdash; and it is the one figure on it you cannot currently explain precisely.</b> It is flagged in your own master resume as unverified. Work out before the interview what the baseline was and what was measured, or stop using the number. An unexplainable metric in a role about executive reporting is worse than no metric."),
            ("\"Describe running three or more cross-functional programmes at once.\"", "Their requirement almost verbatim. Your answer is the dual mandate: 40+ concurrent programmes, two roles, screening running alongside design cycles. <b>Name the tracking mechanism, not just the volume</b> &mdash; what the dashboard contained, how often it refreshed, and one case where it surfaced a problem before the partner reported it."),
            ("<b>&ldquo;How do you handle a CxO priority that conflicts with another function&rsquo;s plan?&rdquo;</b>", "The real test of a founder&rsquo;s office seat, and they named &lsquo;resolve dependencies, surface risks&rsquo; in the JD. Answer with a mechanism rather than diplomacy: how you would surface the conflict with a written option set and a recommendation, rather than brokering it quietly. Discretion is also a stated requirement, so show you know the difference between confidential and invisible."),
            ("\"Why move from a philanthropic institution to a startup?\"", "Expect scepticism about pace. Pre-empt it: name that you are coming from an institution rather than a startup, that you would be adjusting to their velocity rather than arriving used to it, and then point at what transfers &mdash; the habit of owning the cadence rather than waiting to be asked."),
        ],
        "ask": [
            "Whose office is this exactly &mdash; the CEO&rsquo;s, or the CxO group collectively? Who sets my priorities when they conflict?",
            "What are the two or three programmes this role would own in the first quarter?",
            "You are in 300+ hospitals across four countries. Which of those markets is the growth priority, and what is the constraint?",
            "What does &ldquo;AI and product fluency&rdquo; look like in practice day to day &mdash; is it using the tools, or engaging with the roadmap?",
            "What happened to the person who did this before, or is it a new seat?",
            "Six months in, what would have to be true for this to have worked?",
        ],
        "checklist": [
            "<b>Apply today.</b> The posting looks like a repost, so the clock is probably older than two hours",
            "<b>Then spend an hour on a referral, not a second application.</b> ODDS moves from 3.3 to ~4.4 on one introduction and nothing else moves it",
            "<b>Resolve the 60% number before any interview</b> &mdash; what the baseline was and what was measured. It is the headline metric and it is unverified in your own notes",
            "<b>Prepare one concrete example of using AI tooling in your own work.</b> This is the stated gap and the likeliest reason to lose it",
            "Read about Dozee&rsquo;s product properly: ballistocardiography, the early-warning system, and Dozee Shravan",
            "<b>Bengaluru onsite means relocating from Mumbai.</b> Decide how you feel about that before the first call, not during the offer",
            "Tracker updated with a follow-up 5 days out",
        ],
        "flags": [
            "<b>AI product exposure is the one genuine gap</b>, and it is written into the requirements twice. Unlike Eka Care&rsquo;s product roles, this asks for <i>credible engagement</i> rather than shipped product, which is answerable &mdash; but only with a prepared, concrete answer.",
            "<b>The 60% figure is unverified in your own master resume</b> and this role is explicitly about executive reporting and measurable improvement. Being unable to explain your own headline number in that context is a bad look. Resolve it or drop it.",
            "<b>Referral path scored 2, and that is the whole reason ODDS is 3.3 rather than 4.4.</b> Every other dimension is a 4. This is the clearest case on your board for spending the marginal hour on an introduction instead of an application.",
            "<b>Bengaluru onsite, relocating from Mumbai.</b> It clears your location gate but it is a real move, and the JD gives no hint of flexibility.",
            "<b>&ldquo;Program Manager&rdquo; reads as a lateral from Program Officer on paper.</b> The scope described is not lateral &mdash; CxO-facing, cross-functional ownership, special projects &mdash; but you will have to explain the title, and you should decide now that you do not mind.",
            "<b>The posting shows 200+ applicants against a two-hour timestamp</b>, which does not add up. Treat it as an older repost and move fast.",
            "<b>Genuinely strong company signal:</b> India&rsquo;s No.1 RPM provider, 300+ hospitals, four countries, Bloomberg coverage, and the world&rsquo;s first non-contact blood pressure monitor. Alumni trajectory is unverified, which is the one thing to check yourself.",
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
  Scored against applications/RUBRIC.md, from the full job description. Built 8 Sep 2026.
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
