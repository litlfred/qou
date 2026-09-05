#!/usr/bin/env python3
"""Check that a block's published figures actually appear in the witness that
declares it.

THE GAP THIS CLOSES
-------------------
A witness JSON carries `contentBlock`, naming the block it is the evidence for.
**Nothing in the repo checks that the block's numbers are the witness's
numbers.** A producer's own assertions compare it against itself, so they stay
green while the publication and the producer drift apart.

Three defects found on 2026-09-05 are all that shape:

  * `tbl:q-beta-spectral-bridge-table-data` and the witness declaring
    `prop:q-beta-spectral-bridge` compute a different `z` under the same name and
    differ by **21 %**, with both witness assertions passing.
  * `thm:markov-trace-factorization` published a transfer-matrix readout copied
    from deprecated code, wrong on every bond, while a merged probe recorded that
    readout as a trap.
  * Six figures across four blocks carried a `q0` vintage the substrate had
    already corrected.

Each is a correction that landed in compute while a block kept the old value.
This is the first thing that looks across that boundary in the direction that
matters: **block → its declared witness**.

WHAT IT DOES
------------
For every witness declaring `contentBlock`, collect the block's own published
decimals (from its `.md` and any name-derived `*-table*-data.md` sibling) and
check each against the pooled numbers of every witness declaring that block. A
figure counts as present if some witness value **rounds to it** at the published
number of decimals — the rounding step is not optional, see below.

WHAT IT IS NOT
--------------
A gate. It is wired into nothing. Output is a **candidate list**: a block may
legitimately publish a figure its witness does not carry (an experimental input,
a value quoted from cited work, a quantity computed in Lean or in a sibling
producer that declares a different block). Deciding any row needs a human reading
it. `scripts/unsourced-published-figures.py` is the companion asking the weaker
question — "does anything in the repo produce this?" — and this one asks the
sharper "does the producer this block NAMES produce it?".

ROUNDING IS THE WHOLE DIFFICULTY. Exact string matching inflates the answer
several-fold: a figure published at one precision and computed at another does
not string-match, and `0.00155060213`, `0.00155060` and `0.0015506` are three
renderings of one quantity. Same lesson as the companion script.

TWO FALSE-POSITIVE CLASSES WORTH KNOWING BEFORE READING A ROW
-------------------------------------------------------------
1. **Decimals are not significant figures.** `PUB` selects on decimal count, so a
   residual column printed as `0.000001` is admitted with **one** significant
   figure. The round-to window is then ±5e-7 on a value of 1e-6 — the test has no
   resolving power and its "unmatched" means nothing. `rem:atom-mass-full-hecke`
   is entirely this. Same floor as `qou-i229`'s derived-provenance sweep, where
   two figures at 9 digits could not separate two `q0` vintages differing at the
   11th: in a results table "no match" and "cannot tell" look identical.
2. **A block's producer need not be the witness naming it.** A quantity may be
   computed by a sibling declaring a different block, or in Lean, and the block
   still publishes it correctly. Several of `prop:confined-knot-binding`'s rows
   are that.

    python3 scripts/witness-block-agreement.py            # report
    python3 scripts/witness-block-agreement.py --selftest # detector only
"""
from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PUB = re.compile(r"\d+\.\d{6,}")      # published figures worth tracing
SRC = re.compile(r"\d+\.\d{3,}")      # witness values, possibly shorter
LABEL = re.compile(r'label:\s*"([^"]+)"')

#: The known positive: this block and its declared witness compute different z.
SELFTEST_BLOCK = "prop:q-beta-spectral-bridge"
SELFTEST_FIGURE = "0.4993203340335613"


def label_to_files() -> dict[str, list[Path]]:
    """`prop:foo` -> [foo.md, foo-table1-data.md, ...] in the same directory."""
    out: dict[str, list[Path]] = {}
    for ts in CONTENT.rglob("*.ts"):
        try:
            m = LABEL.search(ts.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        if not m:
            continue
        stem = ts.with_suffix("").name
        md = ts.with_suffix(".md")
        sibs = [p for p in ts.parent.glob(f"{stem}*table*.md")]
        out[m.group(1)] = [p for p in ([md] + sibs) if p.exists()]
    return out


def nums(paths, rx) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for p in paths:
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in rx.findall(t):
            out[m].add(str(p.relative_to(ROOT)))
    return out


def witnesses_by_block() -> dict[str, list[Path]]:
    out: dict[str, list[Path]] = defaultdict(list)
    for w in (ROOT / "computations").rglob("*.witness.json"):
        if "_deprecated" in str(w):
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        cb = d.get("contentBlock")
        if isinstance(cb, str) and cb:
            out[cb].append(w)
    return out


def rounds_to(c: str, vals: list[float]) -> bool:
    k = len(c.split(".")[1])
    tol = 0.5 * 10 ** (-k) * 1.000001
    x = float(c)
    i = bisect.bisect_left(vals, x - tol)
    return i < len(vals) and vals[i] <= x + tol


def analyse():
    l2f, wbb = label_to_files(), witnesses_by_block()
    rows = []
    for block, wits in sorted(wbb.items()):
        files = l2f.get(block)
        if not files:
            continue
        pub = nums(files, PUB)
        if not pub:
            continue
        pool = sorted({float(x) for x in nums(wits, SRC)})
        missing = sorted(c for c in pub if not (pool and rounds_to(c, pool)))
        if missing:
            rows.append((block, len(pub), missing, files, wits))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    rows = analyse()
    flagged = {b: m for b, n, m, f, w in rows}

    # Selftest: the known positive must be flagged, on the figure we know
    # diverges. Without it a zero here would mean nothing.
    fails = []
    if SELFTEST_BLOCK not in flagged:
        fails.append(f"KNOWN POSITIVE NOT FLAGGED — {SELFTEST_BLOCK} and its "
                     f"declared witness are measured to compute different z "
                     f"(21 %); if this check cannot see that, it can see "
                     f"nothing.")
    elif SELFTEST_FIGURE not in flagged[SELFTEST_BLOCK]:
        fails.append(f"known positive flagged but not on {SELFTEST_FIGURE}, the "
                     f"figure that actually diverges")
    if fails:
        for f in fails:
            print(f"witness-block-agreement SELFTEST FAILED: {f}", file=sys.stderr)
        return 2
    print(f"selftest ok — known positive {SELFTEST_BLOCK} flagged on "
          f"{SELFTEST_FIGURE}")
    if args.selftest:
        return 0

    total = sum(len(m) for _b, _n, m, _f, _w in rows)
    print(f"\n{len(rows)} block(s) publish figures their declared witness does "
          f"not carry ({total} figures).")
    print("CANDIDATES ONLY — a block may legitimately publish an experimental "
          "input,\na quoted value, or a quantity produced elsewhere.\n")
    for block, npub, missing, files, wits in rows[:args.limit]:
        print(f"  {block}   ({len(missing)}/{npub} unmatched, "
              f"{len(wits)} witness(es))")
        print(f"      block: {files[0].relative_to(ROOT)}")
        for c in missing[:4]:
            print(f"      unmatched: {c}")
        if len(missing) > 4:
            print(f"      ... {len(missing) - 4} more")
    if len(rows) > args.limit:
        print(f"\n  ... {len(rows) - args.limit} more block(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
