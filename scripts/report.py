#!/usr/bin/env python3
"""Pipeline summary for applications/applications.csv.

    python3 scripts/report.py                 # full board
    python3 scripts/report.py --due           # overdue and due-today actions
    python3 scripts/report.py --status screen # everything at one stage
    python3 scripts/report.py --stale 21      # live, submitted N+ days ago

Standard library only.
"""

import argparse
import csv
import datetime as dt
import sys
from collections import Counter
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "applications" / "applications.csv"

# Display order, roughly pipeline order. Anything unrecognised sorts to the end.
STATUS_ORDER = [
    "prospect",
    "applied",
    "screen",
    "interview",
    "onsite",
    "offer",
    "rejected",
    "withdrawn",
    "ghosted",
]
LIVE = {"prospect", "applied", "screen", "interview", "onsite", "offer"}
CLOSED = {"rejected", "withdrawn", "ghosted"}


def parse_date(value):
    """Return a date, or None if the field is blank or malformed."""
    value = (value or "").strip()
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def load(path):
    if not path.exists():
        sys.exit(f"No tracker at {path}")
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        sys.exit("Tracker is empty — add an application first.")
    return rows


def status_key(status):
    try:
        return STATUS_ORDER.index(status)
    except ValueError:
        return len(STATUS_ORDER)


def label(row):
    return f"{row.get('id', '?')}  {row.get('company', '?')} — {row.get('role', '?')}"


def show_summary(rows, today):
    counts = Counter(r.get("status", "").strip() for r in rows)
    live = sum(n for s, n in counts.items() if s in LIVE)
    closed = sum(n for s, n in counts.items() if s in CLOSED)

    print(f"Pipeline — {len(rows)} applications, {live} live, {closed} closed\n")

    width = max((len(s) for s in counts), default=0)
    for status in sorted(counts, key=status_key):
        bar = "#" * counts[status]
        print(f"  {status:<{width}}  {counts[status]:>3}  {bar}")

    # Response rate: anything that reached a human conversation, over anything
    # actually submitted. Prospects aren't submitted, so they don't count.
    submitted = [r for r in rows if r.get("status", "").strip() != "prospect"]
    responded = [
        r
        for r in submitted
        if r.get("status", "").strip() in {"screen", "interview", "onsite", "offer"}
    ]
    if submitted:
        pct = 100 * len(responded) / len(submitted)
        print(f"\n  Response rate: {len(responded)}/{len(submitted)} ({pct:.0f}%)")

    recent = [
        r
        for r in rows
        if (d := parse_date(r.get("date_applied"))) and (today - d).days <= 28
    ]
    print(f"  Applied in the last 28 days: {len(recent)}")


def show_due(rows, today):
    pending = []
    for row in rows:
        if row.get("status", "").strip() in CLOSED:
            continue
        due = parse_date(row.get("next_action_date"))
        if due and due <= today:
            pending.append((due, row))

    if not pending:
        print("\nNothing due. ", end="")
        undated = [
            r
            for r in rows
            if r.get("status", "").strip() in LIVE
            and not parse_date(r.get("next_action_date"))
        ]
        print(
            f"{len(undated)} live application(s) have no next action set."
            if undated
            else "Every live application has a dated next action."
        )
        return

    print(f"\nDue or overdue ({len(pending)}):\n")
    for due, row in sorted(pending, key=lambda p: p[0]):
        days = (today - due).days
        when = "today" if days == 0 else f"{days}d overdue"
        print(f"  [{when:>11}]  {label(row)}")
        print(f"                 → {row.get('next_action', '(no action recorded)')}")


def show_stale(rows, today, threshold):
    stale = []
    for row in rows:
        if row.get("status", "").strip() not in LIVE:
            continue
        applied = parse_date(row.get("date_applied"))
        if applied and (today - applied).days >= threshold:
            stale.append(((today - applied).days, row))

    if not stale:
        print(f"\nNothing live has been sitting longer than {threshold} days.")
        return

    print(f"\nSubmitted {threshold}+ days ago, still live ({len(stale)}):\n")
    for days, row in sorted(stale, reverse=True, key=lambda p: p[0]):
        print(f"  [{days:>4}d]  {label(row)}  ({row.get('status', '?')})")


def show_status(rows, status):
    matching = [r for r in rows if r.get("status", "").strip() == status]
    if not matching:
        print(f"\nNothing at status '{status}'.")
        return

    print(f"\n{status} ({len(matching)}):\n")
    for row in matching:
        print(f"  {label(row)}")
        action = row.get("next_action", "").strip()
        if action:
            date = row.get("next_action_date", "").strip() or "no date"
            print(f"      → {action}  [{date}]")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--due", action="store_true", help="only due/overdue actions")
    parser.add_argument("--status", metavar="STATUS", help="list one stage")
    parser.add_argument(
        "--stale",
        nargs="?",
        const=21,
        type=int,
        metavar="DAYS",
        help="live applications submitted DAYS+ ago (default 21)",
    )
    parser.add_argument(
        "--today",
        metavar="YYYY-MM-DD",
        help="treat this date as today (for testing)",
    )
    args = parser.parse_args()

    today = parse_date(args.today) or dt.date.today()
    if args.today and not parse_date(args.today):
        sys.exit(f"Not a valid date: {args.today}")

    rows = load(CSV_PATH)

    if args.status:
        show_status(rows, args.status)
    elif args.due:
        show_due(rows, today)
    elif args.stale is not None:
        show_stale(rows, today, args.stale)
    else:
        show_summary(rows, today)
        show_due(rows, today)


if __name__ == "__main__":
    main()
