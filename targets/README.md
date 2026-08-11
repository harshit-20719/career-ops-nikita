# Targets

Companies worth working at, kept separately from the application pipeline. A target is
somewhere you'd say yes to; an application is a target with an open role and a submitted
form.

Keeping this list is what stops the search from being purely reactive to whatever
appeared on a job board this week.

## Column reference

| Column | Meaning |
| --- | --- |
| `company` | Company name |
| `tier` | `A` = would drop other things for it · `B` = solid yes · `C` = would consider |
| `industry` | Rough sector |
| `size` | Headcount band: `<50`, `50-200`, `200-500`, `500-2000`, `2000+` |
| `location` | Where the relevant office is, or `Remote` |
| `careers_url` | Jobs page to check |
| `why` | One line. **Required** — if you can't fill it in, it isn't a target |
| `status` | `watching` / `no-openings` / `applied` / `passed` / `closed-door` |
| `known_contacts` | Names, matching `contacts/contacts.csv` |
| `notes` | Hiring freezes, reorgs, anything that changes the timing |

## Status values

| Status | Means |
| --- | --- |
| `watching` | On the list, checking their postings |
| `no-openings` | Nothing suitable right now — check back monthly |
| `applied` | Has moved into `applications/applications.csv` |
| `passed` | You looked closely and decided against it |
| `closed-door` | They rejected you recently; wait 6–12 months before reapplying |

## Cadence

Check tier A careers pages weekly, tier B every two weeks, tier C monthly. That check is
part of the Friday review in `weekly/`.

Aim for 15–25 live targets. Fewer and there's nothing to apply to in a slow week; many
more and the tiers stop meaning anything.
