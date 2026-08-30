#!/usr/bin/env python3
"""Compare two vacuity-ledger snapshots and report any LOST keys.

Split out of precommit-ledger-shrink-warn.sh so the comparison is testable on
its own and so the shell never has to carry a ~1 MB payload in argv or the
environment (that route is E2BIG and fails SILENTLY — see the shell header).

Prints exactly one of:
    OK <n> -> <m>
    SHRINK <n> -> <m>  lost=<k>   (plus a category/verdict breakdown)
    SKIP unparseable: <reason>
"""
import collections
import json
import sys


def main(argv):
    try:
        base = json.load(open(argv[1]))["entries"]
        new = json.load(open(argv[2]))["entries"]
    except Exception as exc:  # noqa: BLE001 - any parse failure is a SKIP
        print(f"SKIP unparseable: {exc}")
        return 0
    lost = set(base) - set(new)
    if not lost:
        print(f"OK {len(base)} -> {len(new)}")
        return 0
    cat = collections.Counter(k.split("::")[2] for k in lost)
    ver = collections.Counter(base[k].get("verdict", "?") for k in lost)
    print(f"SHRINK {len(base)} -> {len(new)}  lost={len(lost)}")
    print("  by category: " + ", ".join(f"{k} {v}" for k, v in cat.most_common()))
    print("  by verdict : " + ", ".join(f"{k} {v}" for k, v in ver.most_common()))
    for k in sorted(lost)[:8]:
        print(f"    {base[k].get('verdict','?'):9s} {k.split('::')[1]}")
    if len(lost) > 8:
        print(f"    ... and {len(lost) - 8} more")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
