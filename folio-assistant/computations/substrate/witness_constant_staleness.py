#!/usr/bin/env python3


# polynomial_q_not_applicable: validator, not a q-series compute.
"""Detect witnesses stale with respect to the substrate constant q₀.

**Why this exists.** `run_pipeline.py`'s staleness check keys on the
PRODUCER SCRIPT's `scriptHash` — so it is **blind to changes in imported
constants** like q₀. The 2026-05-28 q₀ re-pin (muon-anchor `m_μ/m_e` →
proton-anchor `m_p/m_e`, commit `01c18125`) shifted q₀ ~1.3e-8 *without
touching any producer script*, leaving ~390 witnesses carrying the
pre-re-pin q₀ that `run_pipeline.py` happily reports as "fresh". See
`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`.

This detector compares each witness's recorded q₀-shaped value(s) against
the *current* q₀ and flags mismatches — the detection half of the systemic
fix. Wire it into the witness-pipeline so any future constant re-pin
auto-flags the affected witnesses (which the `scriptHash` gate cannot).

**Two robustness properties** (added after Copilot review of #1500/#1501):

- The basin prefix is **derived from the live `Q_50_DIGIT_STR`**, never
  hard-coded, so the detector tracks a re-pin without manual edits. A
  re-pin that leaves the basin neighbourhood is caught *loudly* (an
  assertion + a zero-match guard) instead of silently reporting "0 stale".
- **Audit / state-tracking witnesses are exempt** (`*-audit` / `*-scan` /
  `*-compliance`): their convention is to record provenance values —
  sometimes an OLD q₀ on purpose (e.g. `q0-consistency-audit`'s
  `old_muon_q0`) — so a basin mismatch there is intentional, not staleness.
  Mirrors `witness_provenance_audit.AUDIT_SUFFIXES`.

    python3 witness_constant_staleness.py            # report
    python3 witness_constant_staleness.py --strict   # exit 1 if any stale
    python3 witness_constant_staleness.py --list      # full list (for regen)
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import glob
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE), str(HERE.parent.parent.parent / "tools" / "qou-substrate" / "python")):
    if p not in sys.path:
        sys.path.insert(0, p)

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402  current q₀

# q₀-shaped decimals are matched by a basin prefix DERIVED from the live q₀
# (never hard-coded), so the detector auto-tracks a re-pin. The first 5
# significant digits ("1.1099") are wide enough to span an adjacent re-pin
# (the 2026-05-28 muon→proton shift kept all of "1.10997…") yet narrow
# enough to ignore unrelated 1.x high-precision constants. A re-pin that
# leaves this neighbourhood is caught by the assertion + the zero-match
# guard in main(), NOT silently reported as "0 stale".
_BASIN = Q_50_DIGIT_STR[:6]  # e.g. "1.1099"
Q0_SHAPE = re.compile(re.escape(_BASIN) + r"\d{6,}")
assert Q0_SHAPE.match(Q_50_DIGIT_STR), (
    f"q₀ basin drift: current q₀ {Q_50_DIGIT_STR!r} does not match the "
    f"derived basin pattern {Q0_SHAPE.pattern!r}; widen _BASIN.")

# State-tracking witnesses whose convention is to record provenance
# (possibly an intentionally OLD q₀) — exempt from staleness, mirroring
# witness_provenance_audit.AUDIT_SUFFIXES.
AUDIT_SUFFIXES = (
    "-audit.witness.json",
    "-scan.witness.json",
    "-compliance.witness.json",
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any q₀-stale witness is found")
    ap.add_argument("--ndigits", type=int, default=12,
                    help="significant digits of q₀ to compare (default 12)")
    ap.add_argument("--list", action="store_true",
                    help="print every stale witness (for driving the regen)")
    args = ap.parse_args()

    cur = Q_50_DIGIT_STR[: args.ndigits + 2]  # "1." + ndigits sig
    stale: list[tuple[str, list[str]]] = []
    total = 0
    exempt = 0
    matched_any = 0  # witnesses embedding ≥1 q₀-shaped value
    for wf in sorted(glob.glob(str(HERE / "*.witness.json"))):
        name = Path(wf).name
        if name.endswith(AUDIT_SUFFIXES):
            exempt += 1
            continue
        total += 1
        raw = Path(wf).read_text()
        matches = list(Q0_SHAPE.finditer(raw))
        if matches:
            matched_any += 1
        vals = {m.group(0)[: args.ndigits + 2] for m in matches}
        bad = sorted(v for v in vals if v != cur)
        if bad:
            stale.append((name, bad))

    print(f"current q₀ (≈{args.ndigits} sig): {cur}  (basin {Q0_SHAPE.pattern})")
    print(f"scanned {total} witnesses ({exempt} audit-exempt); "
          f"q₀-stale: {len(stale)}")

    # Zero-match guard: normally hundreds of witnesses embed q₀. If NONE do,
    # the basin regex has silently stopped matching (an un-tracked re-pin or
    # a corpus change) — fail loudly rather than report a false "0 stale".
    if total and matched_any == 0:
        print(f"\nERROR: zero witnesses matched the q₀ basin "
              f"{Q0_SHAPE.pattern!r} across {total} scanned — basin/regex "
              f"drift, not '0 stale'. Update _BASIN.")
        return 2

    show = stale if args.list else stale[:20]
    for name, bad in show:
        print(f"  {name}: {bad}")
    if not args.list and len(stale) > 20:
        print(f"  … +{len(stale) - 20} more (use --list)")

    if args.strict and stale:
        print(f"\nSTRICT FAIL: {len(stale)} witnesses carry a stale q₀ "
              f"(re-pin regeneration incomplete).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
