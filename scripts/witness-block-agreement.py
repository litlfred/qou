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
    `conj:q-beta-spectral-bridge` compute a different `z` under the same name and
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

THE REPORT IS PARTITIONED, BECAUSE 27 % OF IT IS RETRACTION PROSE
-----------------------------------------------------------------
A block that quotes a wrong value **in order to retract it** looks exactly like a
block that publishes one. This corpus retracts in Markdown blockquotes, so a
figure occurring only on `>` lines is very likely being disowned rather than
asserted. Measured: **21 of 79** unmatched figures, and three blocks are entirely
this — `thm:markov-trace-factorization` (the deprecated transfer-matrix readout,
quoted to correct it), `prop:markov-pair-z2` (the `1/δ` vs excised `z_C`
conflation it warns about), `prop:wedderburn-weight-canonical` (a table of
`y_λ` values printed to show the Wenzl-bridge premise *fails*).

Unpartitioned, this checker is loudest on exactly the blocks where someone did
the right thing and documented a correction.

**They are labelled, not dropped.** Blockquote is a proxy for retraction and not
a synonym: a live figure can sit only in a callout — `calibration-inputs`
publishes the current CODATA `206.7682827` inside one. Dropping the class
silently would blind the checker to any stale figure that happens to live in a
note, which is the failure mode the discrimination floor below describes.

THREE FURTHER FALSE-POSITIVE CLASSES WORTH KNOWING BEFORE READING A ROW
-----------------------------------------------------------------------
1. **Decimals are not significant figures.** `PUB` selects on decimal count, so a
   residual column printed as `0.000001` is admitted with **one** significant
   figure. The round-to window is then ±5e-7 on a value of 1e-6 — the test has no
   resolving power and its "unmatched" means nothing. `rem:atom-mass-full-hecke`
   is entirely this. Same floor as `qou-i229`'s derived-provenance sweep, where
   two figures at 9 digits could not separate two `q0` vintages differing at the
   11th: in a results table "no match" and "cannot tell" look identical.
2. **A block's producer need not be the witness naming it.** A quantity may be
   computed by a sibling declaring a different block, or in Lean, and the block
   still publishes it correctly. `prop:em-coupling-projection` was the extreme
   case — 6 of 7 rows unmatched, because the `contentBlock` pointer sat on a
   producer computing one of them while the producer of the other six emitted no
   witness at all. Read a near-total miss as a misdirected pointer before reading
   it as a stale table.
3. **A labelled comparison against a superseded convention.** A block may publish
   both the production value and the excised one, side by side and clearly
   marked, so a producer computing the live convention correctly carries none of
   the other column. `prop:frobenius-gram-matrix` prints its Gram spectrum under
   D *and* under C, saying so; four of its five flags were the C column. Unlike
   class 1 in the blockquote partition, this sits in ordinary prose and is not
   mechanically separable — the label is a sentence, not a syntax.

   That block is also the case for reading every row rather than sweeping: its
   **fifth** flag was a genuine digit error, `4.23033920` where no registered
   `q0` produces anything but `4.23033923` (proton) or `4.23033940` (muon).
   Four false positives and one real defect in the same block.

THE WEAKNESS THAT MATTERS MOST: A ROW CAN BE CLOSED WITHOUT PRODUCING ANYTHING
-------------------------------------------------------------------------------
This checker asks whether a witness declaring a block *carries* the block's
numbers. **A witness that transcribes them answers yes without adding any
evidence.** Nothing here can tell a computed value from a copied one.

That is not hypothetical. `witness-float64-padding-audit` is an aggregator that
scrapes numbers from other witnesses, and it surfaced as a top-scoring
"candidate producer" covering 5 of 5 figures of a block it has never computed.
And while triaging `prop:frobenius-gram-matrix` I closed its row by pasting the
block's own convention-C figures into a new witness — accidentally, then
reverted, because a row closed that way is worse than an open one: the figures
still have no producer and the checker has stopped saying so.

So: **the count is a floor on the work remaining, never a measure of it**, and
closing a row means finding or writing the producer, never recording the number
somewhere the checker will look.

HOW MUCH OF A MATCH IS COINCIDENCE — MEASURED, NOT ASSUMED
-----------------------------------------------------------
Matching 50 figures against a pool of ~272 000 witness values will find
coincidences. The floor is measurable: perturb each published figure's last digit
— same magnitude, same decimal count, fabricated — and re-run.

    REAL published figures matched somewhere   80.0 %
    FABRICATED (last digit changed)             9.5 %

**But the average floor is not the floor for any particular figure**, and the
variation is what matters:

    sig figs     floor       what it means
    0-2         100.0 %      zero information. Every fabricated value matches.
    6-8           5.4 %      a match is real evidence
    9-11          2.7 %      strongest discrimination in the corpus
    12+           8.8 %      RISES AGAIN -- see below

The rise at high precision is not an artifact. The hits concentrate on the
corpus's load-bearing constants — `w₋ = 0.247297886748035`, the `q₀` pins
`1.10997859555…`, `z_C = 0.4993203340335613` — which the repo carries at many
precisions and in many registered variants. A perturbed digit lands on a *real
neighbouring variant of the same constant*. So for exactly the figures that
matter most, "it matches something in the repo" is the weakest evidence
available, and attribution there must come from reading the producer.

(Part of that rise WAS an artifact and is now fixed: parsing both sides with
`float()` put the 12+ floor at 11.4 %. See `rounds_to`.)

A THIRD HAZARD, MEASURED AND DELIBERATELY NOT PATCHED
------------------------------------------------------
`rounds_to` rejects a **truncated** publication. `em-coupling-bring-zero-mode`
publishes `136.823219654` for a producer value of `136.823219654561`, which
*rounds* to `…655`; it misses the half-ulp window by 1.12 half-ulps. A
truncation-aware window would be `[c, c + 10^-k)` instead.

**Measured across the whole report, truncation explains 0 of the asserted
unmatched figures**, so the window is left alone. Widening an acceptance test
that rescues nothing while admitting new false negatives is a net loss. Recorded
because the hazard is real and the next person to see a near-miss should not have
to rediscover it.

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
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80          # comfortably past the corpus's 50-dps witnesses

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "folio"
PUB = re.compile(r"\d+\.\d{6,}")      # published figures worth tracing
SRC = re.compile(r"\d+\.\d{3,}")      # witness values, possibly shorter
LABEL = re.compile(r'label:\s*"([^"]+)"')

#: The known positive. A detector with no known positive can report a whole class
#: clean and mean nothing by it, so this pair must stay live.
#:
#: It was `conj:q-beta-spectral-bridge` on `0.4993203340335613`, the convention-C
#: `z` that diverged 21 % from its own producer. That defect was FIXED on
#: 2026-09-05 (the qbeta channel migrated C -> D), and fixing it turned the
#: selftest red -- the third time in one day that "assert the defect" produced a
#: check that fails on success. A selftest still needs a positive, so it is
#: re-pointed rather than deleted, and the replacement is chosen to be STABLE BY
#: DESIGN rather than merely unfixed:
#:
#: `prop:frobenius-gram-matrix` publishes its Gram determinant under the excised
#: convention C as a deliberate, labelled side-by-side comparison against the
#: production convention D. No witness carries it and none should -- closing that
#: row would mean computing an excised convention, which is the wrong direction.
#: So the row stays open on purpose, and 17 significant figures put it far above
#: the discrimination floor.
SELFTEST_BLOCK = "prop:frobenius-gram-matrix"
SELFTEST_FIGURE = "0.18920521914403668"


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


def asserted(figure: str, paths) -> bool:
    """True if `figure` occurs on any line the block is not quoting.

    Retractions in this corpus are Markdown blockquotes, so a figure appearing
    only on `>` lines is most likely being disowned rather than published. A
    proxy, not a synonym — hence partition rather than exclude.
    """
    for p in paths:
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for line in lines:
            if figure in line and not line.lstrip().startswith(">"):
                return True
    return False


def witnesses_by_block() -> dict[str, list[Path]]:
    out: dict[str, list[Path]] = defaultdict(list)
    for w in (ROOT / "computations").rglob("*.witness.json"):
        if ("_deprecated" in str(w) or "fsh-guts" in str(w)):
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        cb = d.get("contentBlock")
        if isinstance(cb, str) and cb:
            out[cb].append(w)
    return out


def rounds_to(c: str, vals: list[Decimal]) -> bool:
    """Does some witness value round to the published figure `c`?

    EXACT DECIMAL, NOT FLOAT. A first version parsed both sides with `float()`
    and was measurably blind at the precision this corpus cares most about: at
    15+ significant digits, float64 spacing (~1.1e-16 near 0.5) is comparable to
    the ±0.5-ulp window, so the window stops discriminating. Measured on
    fabricated figures, `0.508229789376739` matched 31 times in 60 draws under
    float parsing. A repo that forbids float64 by gate deserved better from its
    own checker. `Decimal` is exact from a decimal string, so the comparison is
    the one the docstring claims.
    """
    k = len(c.split(".")[1])
    tol = Decimal(5).scaleb(-k - 1)          # exactly 0.5 * 10^-k
    x = Decimal(c)
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
        pool = sorted({Decimal(x) for x in nums(wits, SRC)})
        missing = sorted(c for c in pub if not (pool and rounds_to(c, pool)))
        if missing:
            live = [c for c in missing if asserted(c, files)]
            quoted = [c for c in missing if c not in live]
            rows.append((block, len(pub), live, quoted, files, wits))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    rows = analyse()
    flagged = {b: live for b, n, live, q, f, w in rows}

    # Selftest: the known positive must be flagged, on the figure we know
    # diverges, and in the ASSERTED partition — a known positive that lands in
    # the quoted bucket would prove the partition eats real findings. Without
    # this a zero here would mean nothing.
    fails = []
    if SELFTEST_BLOCK not in flagged:
        fails.append(f"KNOWN POSITIVE NOT FLAGGED — {SELFTEST_BLOCK} publishes "
                     f"a convention-C figure no witness carries, deliberately "
                     f"and permanently; if this check cannot see that, it can "
                     f"see nothing.")
    elif SELFTEST_FIGURE not in flagged[SELFTEST_BLOCK]:
        fails.append(f"known positive flagged but not on {SELFTEST_FIGURE} as "
                     f"ASSERTED — either the figure that diverges is missed, or "
                     f"the blockquote partition has swallowed it")
    if fails:
        for f in fails:
            print(f"witness-block-agreement SELFTEST FAILED: {f}", file=sys.stderr)
        return 2
    print(f"selftest ok — known positive {SELFTEST_BLOCK} flagged on "
          f"{SELFTEST_FIGURE}")
    if args.selftest:
        return 0

    n_live = sum(len(l) for _b, _n, l, _q, _f, _w in rows)
    n_quoted = sum(len(q) for _b, _n, _l, q, _f, _w in rows)
    live_rows = [r for r in rows if r[2]]
    print(f"\n{len(live_rows)} block(s) ASSERT {n_live} figure(s) their declared "
          f"witness does not carry.")
    print(f"A further {n_quoted} unmatched figure(s) across {len(rows)} block(s) "
          f"occur only inside\nblockquotes — most are values quoted in order to "
          f"be retracted. Shown separately,\nnot dropped: blockquote is a proxy "
          f"for retraction, not a synonym.")
    print("\nCANDIDATES ONLY — a block may legitimately publish an experimental "
          "input, a\nquoted value, or a quantity produced by a sibling that "
          "declares another block.\n")
    for block, npub, live, quoted, files, wits in rows[:args.limit]:
        if not live:
            continue
        print(f"  {block}   ({len(live)}/{npub} asserted-unmatched, "
              f"{len(wits)} witness(es))")
        print(f"      block: {files[0].relative_to(ROOT)}")
        for c in live[:4]:
            print(f"      unmatched: {c}")
        if len(live) > 4:
            print(f"      ... {len(live) - 4} more")
        if quoted:
            print(f"      (+{len(quoted)} blockquote-only, likely retracted)")
    quoted_only = [r for r in rows if not r[2]]
    if quoted_only:
        print("\n  BLOCKQUOTE-ONLY (no asserted figure unmatched):")
        for block, _n, _l, quoted, _f, _w in quoted_only:
            print(f"      {block}  ({len(quoted)})")
    if len(rows) > args.limit:
        print(f"\n  ... {len(rows) - args.limit} more block(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
