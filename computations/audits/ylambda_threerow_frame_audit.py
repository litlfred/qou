#!/usr/bin/env python3
"""ylambda_threerow_frame_audit.py — which y_lambda consumers still reason about a
stratum that convention D annihilates?

THE FACT THE AUDIT RESTS ON, measured rather than assumed (see `--measure`).
Under the canonical trace convention **D** (`z = q^3/(q^2+1)`, owner ruling
2026-08-15) the Wenzl level relation collapses to `Q^r = Q^2`, i.e. `r = 2`.
`schur_principal_mpmath` is then the SU(2) two-row specialisation `s_lambda(1, Q)`,
so `y_lambda = 0` EXACTLY for every partition with three or more rows.  Both halves
are Lean-proved sorry-free on main -- `wenzlLevel_conventionD` and
`schurPrincipal_eq_zero_iff` (all n, all r) -- and `two_row_support_recount.py`
measures what the truncation removes.  Nothing here re-derives them.

WHY A SWEEP.  Code written before the 2026-08-09 ruling can carry a premise the
ruling falsifies, and it does NOT fail loudly when it does:

  * a filter on `y < 0` picks up ROUND-OFF in the zeroed entries and reports it as
    a measured quantity.  Worked case: `mu3_door_budget_probe` printed "the
    negative-weight blocks supply ~1/7.6e39 of what the door needs" from a
    `sum|y_neg|` of 1.04e-42 (PR #4673);
  * a sum over the `ell(lambda) >= 3` stratum evaluates over a set that is now
    identically zero, and any *ratio* built on it is 0/0 or noise/noise;
  * a narrative pinned to C's non-integer level `r(q_0) = 2.5995` keeps printing
    while the code underneath returns `r = 2`.

TWO LAYERS, because a source-only detector cannot decide this.

  1. `--triage` (default): high-recall SOURCE scan.  Names candidates.  It is
     deliberately NOT a verdict -- its own top hit is a FALSE POSITIVE by
     construction, `mu3_door_budget_probe`, whose neg-weight vocabulary is high
     precisely because it now DOCUMENTS the trap and carries the fix.  A file that
     discusses the defect scores like a file that has it.

  2. `--measure`: NUMERIC confirmation, convention-agnostic.  Evaluates the
     `ell >= 3` stratum directly at the proton pin.  A value cannot be stale,
     mislabelled, or re-spelled and still be nonzero.  This is the layer that
     decides; the triage only says where to point it.

`--selftest` fails unless the known instance is detected, so a future narrowing
cannot quietly report a clean tree.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

CONSUMER = re.compile(r"\b(y_lambda_at_q0_mpmath|y_lambda_at|y_lambda_su_n)\b")
SIGN = re.compile(r"(_?[Yy]\w*|weights?)\s*\[\s*\w+\s*\]\s*[<>]\s*0"
                  r"|\bif\s+\w*[yY]\w*\s*[<>]\s*0")
ROWS = re.compile(r"len\s*\(\s*\w+\s*\)\s*(?:>=\s*3|>\s*2)"
                  r"|ell\s*\(?\s*\w*\s*\)?\s*(?:>=\s*3|>\s*2)"
                  r"|three[_-]?row|3[_-]?row|threerow", re.I)
NEGV = re.compile(r"negative[-_ ]?weight|y_neg|yneg|neg_blocks|sign[-_ ]?indefinite", re.I)
# a file that already knows: carries a noise floor, or is an explicit C-vs-D comparison
GUARD = re.compile(r"noise[_ ]?floor|NOISE\b", re.I)
COMPARE = re.compile(r"C[_ ]?vs[_ ]?D|convention[-_ ]?C\b.*convention[-_ ]?D|D[_ ]?vs[_ ]?C", re.I)
# C's level, hard-coded: Q^r = u^3/D(u) with D(u) = -u^6 - u^4 + u^3 + u^2 + 1
C_LEVEL = re.compile(r"-\s*u\s*\*\*\s*6\s*-\s*u\s*\*\*\s*4|2\.5995|1\.7202|1\.13068")


SELF = pathlib.Path(__file__).resolve()


def _files():
    for p in sorted(ROOT.rglob("*.py")):
        s = p.as_posix()
        if "/.claude/" in s or "_deprecated" in s or "/.lake/" in s:
            continue
        # Exclude this file. It quotes C's level (2.5995, 1.7202, u*=1.13068) and
        # the negative-weight vocabulary in order to DESCRIBE the trap, so without
        # this it accuses itself -- the same false-positive-by-construction as
        # mu3_door_budget_probe, which is the point the docstring makes about
        # layer 1. A detector that flags its own explanation is not measuring the
        # corpus.
        if p.resolve() == SELF:
            continue
        yield p


def triage():
    rows = []
    for p in _files():
        try:
            txt = p.read_text(errors="replace")
        except OSError:
            continue
        if not CONSUMER.search(txt):
            continue
        hits = {k: len(rx.findall(txt)) for k, rx in
                (("sign-filter", SIGN), ("row>=3", ROWS), ("neg-vocab", NEGV))}
        hits = {k: v for k, v in hits.items() if v}
        rows.append({
            "path": p.relative_to(ROOT).as_posix(),
            "score": sum(hits.values()),
            "hits": hits,
            "guarded": bool(GUARD.search(txt)),
            "comparison": bool(COMPARE.search(txt)),
            "hardcodes_C_level": bool(C_LEVEL.search(txt)),
        })
    rows.sort(key=lambda r: (-r["score"], r["path"]))
    return rows


def measure(ns=(6, 9, 12)):
    sys.path[:0] = [str(ROOT / "computations"), str(ROOT / "computations" / "substrate")]
    import _path_bridge  # noqa: F401
    import mpmath as mp
    from schur_principal_mpmath import y_lambda_at_q0_mpmath, _wenzl_constants
    from _precision import set_compute_dps
    from q_parameter import Q_MP
    set_compute_dps(40)
    q = Q_MP
    Q, QR = _wenzl_constants(q)
    out = {"q0": mp.nstr(q, 20),
           "Q": mp.nstr(Q, 20),
           "Q_r": mp.nstr(QR, 20),
           "effective_level_r": mp.nstr(mp.log(QR) / mp.log(Q), 12),
           "Q_r_equals_Q_squared": bool(abs(QR - Q ** 2) < mp.mpf("1e-30")),
           "strata": []}
    for n in ns:
        Y = y_lambda_at_q0_mpmath(n, q)
        ge3 = [l for l in Y if len(l) >= 3]
        # Compare against a NOISE FLOOR, never against zero.  The vanishing is a
        # polynomial identity, but it is REACHED BY CANCELLATION in finite
        # precision, so the computed stratum sits at ~1e-42 at 40 dps rather than
        # at a clean 0.  An equality test therefore answers a question about the
        # arithmetic, not about the mathematics -- and it answers it differently
        # for different spellings of the same q: mpf("1.1099785827513808") gives
        # exactly 0.0 where the full-precision Q_MP gives 1.27e-42.  Both are the
        # same structural zero.  (Caught by this file's own --selftest, which is
        # what a selftest is for.)
        floor = max((abs(v) for v in Y.values()), default=mp.mpf(0)) \
            * mp.mpf(10) ** (-(mp.mp.dps - 8))
        tot = sum((abs(Y[l]) for l in ge3), mp.mpf(0))
        mx = max((abs(Y[l]) for l in ge3), default=mp.mpf(0))
        out["strata"].append({
            "n": n,
            "partitions": len(Y),
            "ell_ge_3": len(ge3),
            "sum_abs_y": mp.nstr(tot, 12),
            "max_abs_y": mp.nstr(mx, 12),
            "noise_floor": mp.nstr(floor, 6),
            "is_structural_zero": bool(mx < floor),
            "n_negative_above_floor": sum(1 for v in Y.values() if v < -floor),
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        rows = triage()
        known = "computations/deltalambda/threerow_qcross_trend_probe.py"
        hit = next((r for r in rows if r["path"] == known), None)
        if hit is None or not hit["score"]:
            print(f"SELFTEST FAIL: {known} not detected")
            return 1
        if not hit["hardcodes_C_level"]:
            print(f"SELFTEST FAIL: {known} no longer reads as hard-coding C's level")
            return 1
        m = measure((9,))
        st = m["strata"][0]
        if not st["is_structural_zero"]:
            print(f"SELFTEST FAIL: ell>=3 stratum at n=9 is above the noise floor: "
                  f"max|y| = {st['max_abs_y']} vs floor {st['noise_floor']}")
            return 1
        if st["n_negative_above_floor"]:
            print(f"SELFTEST FAIL: {st['n_negative_above_floor']} genuinely negative "
                  f"y_lambda at n=9 — convention D should leave none")
            return 1
        print("SELFTEST OK")
        return 0

    if a.measure:
        m = measure()
        print("=" * 86)
        print(" NUMERIC LAYER — the >=3-row stratum at the proton pin")
        print("=" * 86)
        print(f"  q0     = {m['q0']}")
        print(f"  Q      = {m['Q']}")
        print(f"  Q^r    = {m['Q_r']}    (== Q^2, i.e. convention D: {m['Q_r_equals_Q_squared']})")
        print(f"  r      = {m['effective_level_r']}")
        print()
        for s in m["strata"]:
            print(f"  n={s['n']:>3}  partitions={s['partitions']:>3}  "
                  f"ell>=3: {s['ell_ge_3']:>3}   "
                  f"max|y| = {s['max_abs_y']}   floor = {s['noise_floor']}   "
                  f"structural zero: {s['is_structural_zero']}   "
                  f"genuinely negative y: {s['n_negative_above_floor']}")
        print()
        print("  Any consumer whose object is a sum, ratio or sign over that stratum")
        print("  is computing on exactly zero. A ratio built on it is noise/noise.")
        return 0

    rows = triage()
    flagged = [r for r in rows if r["score"]]
    print("=" * 86)
    print(" SOURCE TRIAGE — candidates, NOT verdicts (see the module docstring)")
    print("=" * 86)
    print(f"  y_lambda consumers scanned : {len(rows)}")
    print(f"  flagged                    : {len(flagged)}")
    print(f"  clean                      : {len(rows) - len(flagged)}")
    print()
    for r in flagged:
        tags = []
        if r["hardcodes_C_level"]:
            tags.append("HARD-CODES C's LEVEL")
        if r["comparison"]:
            tags.append("declares a C-vs-D comparison")
        if r["guarded"]:
            tags.append("has a noise floor")
        t = ("   [" + "; ".join(tags) + "]") if tags else ""
        print(f"  {r['score']:>3}  {r['path']}{t}")
        print(f"       {r['hits']}")
    print()
    print("  Reading the tags:")
    print("    HARD-CODES C's LEVEL          -- quotes Q^r = u^3/D(u), r = 2.5995,")
    print("                                     Q^r = 1.7202, or u* = 1.13068. On its")
    print("                                     own this is the strongest signal.")
    print("    declares a C-vs-D comparison  -- says so in its own text. Reasoning about")
    print("                                     the annihilated stratum is then CORRECT")
    print("                                     BY DESIGN; both tags together are expected.")
    print("    has a noise floor             -- already distinguishes round-off from a")
    print("                                     measured value. Not a clearance, but it")
    print("                                     cannot make the mu3_door_budget error.")
    print()
    print("  Point --measure at the survivors. The numeric layer decides.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
