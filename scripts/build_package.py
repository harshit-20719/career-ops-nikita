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
                "In 2021 I co-founded Tiff.in, a food and content business incubated at Ashoka University — 3 of 35 teams got funded and we were one of them. I did the commercial side: market sizing, unit economics, the financial model, and the pitch. Then I did the unglamorous half, which was actually getting people to find us. We grew YouTube views 520% and Instagram followers 370% across four channels, by testing far more things than worked. What I learned is the part that's relevant to you: distribution is not a campaign, it's a loop you run until the numbers move, and most of what you try will not move them.",
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
  Scored against applications/RUBRIC.md, from the full job description. Built 17 Aug 2026.
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
