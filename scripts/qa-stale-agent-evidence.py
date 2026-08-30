#!/usr/bin/env python3
"""Do agent QA verdicts still quote prose that exists?

An agent `fail`/`warn` survives every `qa-sweep` run, because the sweep re-runs
SCRIPT criteria only. A verdict whose evidence quotes a sentence that has since
been edited away therefore keeps presenting as current, and the only way to
notice is to read the evidence and grep the quote.

This measures how often that has happened. It CANNOT decide whether a verdict
is right -- only whether the text it points at is still there.

MATCHING IS DELIBERATELY LOOSE, because the first version of this script was
wrong in exactly the direction that inflates the answer. Two artifacts it
produced, both verified by hand:

  * a "widest span between the first and last quote" strategy stitched two
    separate short quotes into one -- evidence "grades a -0.6% residual
    'excellent' and +10.3% 'fair'" became the fragment
    "excellent' and $+10.3\\%$ 'fair", which is in no source. Both words are
    present. Strategy dropped.
  * agents render an em dash as "-" inside their quotes, so
    "'- all four readings equal, as they are for $4_1$ -'" failed a literal
    search against prose that contains it. Now every dash, quote and markdown
    emphasis marker is folded away on BOTH sides before comparing, and the
    search runs on the longest wordy core of each quote rather than the whole
    span.

So `vanished` is a floor: anything that still fails this has no textual anchor
left at all.

Outcomes: live / vanished / unquotable (no fragment long enough to search --
e.g. "Closer restated the para-2 roadmap already given"), counted separately
rather than assumed fine.
"""
import json
import glob
import re
import collections
import os
import sys

ROOT = os.environ.get("QOU_ROOT") or os.getcwd()
MIN_FRAG = 25
SPLIT_ELLIPSIS = re.compile(r"\.\.\.|…")
# A "wordy core": letters, digits, spaces and intra-word punctuation only.
CORE = re.compile(r"[A-Za-z0-9][A-Za-z0-9 ]{%d,}" % (MIN_FRAG - 1))


def fold(s: str) -> str:
    """Normalise both sides of the comparison to bare lowercase words."""
    s = s.replace("**", " ").replace("*", " ").replace("`", " ")
    s = re.sub(r"[—–‒\-]", " ", s)      # every dash
    s = re.sub(r"[‘’“”'\"]", " ", s)  # every quote
    s = re.sub(r"[^A-Za-z0-9 ]", " ", s)               # math, punctuation
    return re.sub(r"\s+", " ", s).strip().lower()


def fragments(evidence: str) -> list[str]:
    """Folded wordy cores of each quoted span, longest first."""
    spans: list[str] = []
    for pat in (r"'([^']{%d,})'" % MIN_FRAG,
                r'"([^"]{%d,})"' % MIN_FRAG,
                r"‘([^’]{%d,})’" % MIN_FRAG,
                r"“([^”]{%d,})”" % MIN_FRAG):
        spans += re.findall(pat, evidence)
    out: list[str] = []
    for s in spans:
        for piece in SPLIT_ELLIPSIS.split(s):
            folded = fold(piece)
            for core in CORE.findall(folded):
                c = core.strip()
                if len(c) >= MIN_FRAG:
                    out.append(c)
    return sorted(dict.fromkeys(out), key=len, reverse=True)


def sources(d: dict) -> str:
    buf = []
    for key in ("md", "ts", "lean"):
        p = (d.get("paths") or {}).get(key)
        if not p:
            continue
        try:
            buf.append(open(os.path.join(ROOT, p), encoding="utf-8").read())
        except OSError:
            continue
    return fold("\n".join(buf))


def main() -> int:
    counts = collections.Counter()
    by_crit = collections.defaultdict(collections.Counter)
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content/**/*.qa.json"), recursive=True)):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        entries = []
        for name, es in (d.get("criteria") or {}).items():
            if not es:
                continue
            e = sorted(es, key=lambda x: x.get("reviewed_at") or "")[-1]
            if (e.get("reviewer") or {}).get("kind") != "agent":
                continue
            if e.get("result") in ("fail", "warn"):
                entries.append((name, e))
        if not entries:
            continue
        src = sources(d)
        for name, e in entries:
            frags = fragments(e.get("evidence") or "")
            if not frags:
                counts["unquotable"] += 1
                by_crit[name]["unquotable"] += 1
                continue
            if any(fr in src for fr in frags):
                counts["live"] += 1
                by_crit[name]["live"] += 1
                continue
            # The full quote is absent. Distinguish a sentence that was
            # EDITED (a leading sub-phrase survives, so the flagged construct
            # may well survive with it) from one that is GONE outright. Only
            # the latter leaves the verdict with no anchor at all.
            core = frags[0].split()
            edited = any(len(core) > n and " ".join(core[:n]) in src
                         for n in (12, 9, 6, 4))
            key = "edited" if edited else "gone"
            counts[key] += 1
            by_crit[name][key] += 1
            rows.append((key, name, d.get("label") or os.path.basename(f),
                         e.get("reviewed_at", "")[:10], frags[0][:80]))

    total = sum(counts.values())
    if total == 0:
        print("no agent fail/warn verdicts found — nothing to check")
        return 0
    print(f"agent fail/warn verdicts examined: {total}\n")
    for k in ("live", "edited", "gone", "unquotable"):
        print(f"  {k:11s} {counts[k]:5d}  ({100*counts[k]/total:.1f}%)")
    dec = counts["live"] + counts["edited"] + counts["gone"]
    print(f"\ndecidable: {dec}   verdicts whose sentence is GONE: "
          f"{counts['gone']} ({100*counts['gone']/dec:.1f}% of decidable)")
    print("\nby criterion (most gone first):")
    for name, c in sorted(by_crit.items(), key=lambda kv: -kv[1]["gone"])[:12]:
        if c["live"] + c["edited"] + c["gone"] == 0:
            continue
        print(f"  {name:34s} gone {c['gone']:4d}  edited {c['edited']:4d}"
              f"  live {c['live']:4d}  (+{c['unquotable']} unquotable)")
    if "--list" in sys.argv:
        print("\nGONE verdicts:")
        for r in rows:
            if r[0] == "gone":
                print("  " + "\t".join(str(x) for x in r[1:]))
    # Advisory: this is a measurement, not a gate.
    return 0


if __name__ == "__main__":
    sys.exit(main())
