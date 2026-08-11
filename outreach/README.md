# Outreach

Starting points in `templates/`, not scripts to send as-is. A message that reads as a
template gets deleted; the templates exist so you're editing rather than staring at a
blank box at 9pm.

| Template | Use it for |
| --- | --- |
| `cold-email.md` | Someone you don't know, at a company you want |
| `referral-request.md` | Someone you do know, for a specific open role |
| `follow-up.md` | Silence after an application or a conversation |
| `thank-you.md` | After any interview round |

## What makes these work

- **Short.** Under 150 words. Anything longer gets skimmed and then deferred.
- **Specific.** One concrete detail proving you're writing to *them* — their launch,
  their post, their talk. This is the whole game.
- **One ask, small.** "15 minutes" converts. "Can you get me a job" doesn't.
- **Easy to say no to.** Explicitly. It raises the reply rate, counterintuitively.
- **Subject lines are literal.** "Question about the platform team role" beats anything
  clever.

## Timing

Second column is the normal cadence; third is the compressed one currently in effect,
since the search is on a ~2-month clock.

| Situation | Normal | Urgent |
| --- | --- | --- |
| After applying, no response | 7–10 days | 5 days |
| After an interview | Within 24h | Within 24h |
| After a stated timeline passes | 2–3 days past | 1–2 days past |
| After a referral ask, no reply | 1 week, once | 4 days, once |
| No reply at all, ever | `ghosted` at 21 days | `ghosted` at 14 days |

Follow up once. Not twice. The second follow-up almost never converts and it's the one
they remember.

## Recording it

Every outbound message updates `contacts/contacts.csv`: `last_contact`, and a
`next_touch` if you expect to circle back. If it relates to a live application, update
`next_action` and `next_action_date` on that row too.
