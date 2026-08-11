# Weekly review

Copy `TEMPLATE.md` to `YYYY-WW.md` (e.g. `2026-33.md`) every Friday. Thirty minutes,
same time each week.

The review is what keeps a job search from becoming either frantic or invisible. Both
failure modes come from never looking at the whole board.

## What it's for

- Nothing sits in `next_action` past its date
- Silent applications get chased once, then marked `ghosted`
- Tier A companies get their careers pages checked
- The activity numbers stay visible, so a slow week is a fact rather than a feeling

## The routine

```bash
python3 scripts/report.py        # the whole board
python3 scripts/report.py --due  # anything overdue
```

1. Clear or re-date every overdue action.
2. Update statuses from the week's emails and calls.
3. Mark anything silent 21+ days as `ghosted`.
4. Check tier A careers pages, then tier B if it's a fortnight.
5. Set next week's target number of applications and outreach messages.
6. Write down one thing that isn't working, and what you'll change.

## On the numbers

Track outputs, not outcomes. Applications sent and conversations had are yours to
control; interviews and offers aren't. Judge a week on what you did.

Typical shape of a healthy funnel, for calibration when a rejection run feels personal:

- ~15–20% of cold applications get a first response
- referrals convert several times better — which is why `contacts/` exists
- most searches take 2–4 months, and the middle stretch is the demoralizing part

A week with 5 applications and 3 outreach messages is a good week. Compounding beats
sprinting; the searches that stall are the ones that go dark for a fortnight after a
rejection.
