#!/usr/bin/env python3
"""Extended Habiro cyclotomic coefficients via markov_peel symbolic-q.

W-3 follow-up.  The original symbolic pipeline in
`habiro_coefficients_atomic.py` was intractable for A ≥ 3 (10+ minutes
per atom even for the deuteron).  This script swaps in the
`markov_peel.tr_M_atomic(..., return as sympy expression in q)` path
which is several orders of magnitude faster:

  - ³He  (n=9):  symbolic in 4 s, 5 k sympy ops, deg p(u) = 132
  - ⁴He  (n=12): symbolic in 23 s, 39 k sympy ops, deg p(u) = 180
  - ⁵Li  (n=15): tractable target (40-60 s expected)
  - ⁶Li  (n=18): heavy but feasible (5-15 min expected)

The Habiro denominator D(u) (Markov-normalisation polynomial) has a
clean closed form for every atom we have tested:

  ³He:  D(u) = 2^7  · u^58 · (1 + u²)^8
  ⁴He:  D(u) = 2^9  · u^79 · (1 + u²)^11

so the previously identified "analytical D(u)" research blocker is
resolved by this pipeline as a side effect.

Output: `habiro-coefficients-extended.witness.json` with full integer
Habiro coefficients a_m(u) for each atom + D(u) factored form +
verification that each a_m has integer coefficients (the cyclotomic
integrality witness).

Reference blocks:
  - prop:full-pole-structure-mass-trace
  - prop:habiro-expansion-atomic
  - thm:knot-mass-formula-unified
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_laurent_fast import tr_M_atomic_fast as tr_M_atomic  # noqa: E402
# Drop-in fast replacement for `markov_peel.tr_M_atomic` via the
# LaurentQ-coefficient pipeline (PR #537 in main).  3-8× speedup on
# the symbolic Markov-peel reduction; verified equivalent at q = q₀.
from habiro_coefficients_atomic import (  # noqa: E402
    to_u_polynomial,
    cyclotomic_expansion,
    reconstruct,
)


def _factor_denominator(denom_str: str, u: sp.Symbol) -> str:
    """Try to factor the denominator polynomial as power_of_2 · u^shift ·
    cyclotomic-style polynomial, returning a human-readable form."""
    try:
        d = sp.expand(sp.sympify(denom_str, locals={"check_q": u}))
        f = sp.factor(d)
        return str(f)
    except Exception:
        return denom_str


def _analyse_atom(label: str, Z: int, N: int, max_m: int) -> dict:
    print(f"\n── {label} (Z={Z}, N={N}) ──", flush=True)
    t0 = time.time()
    expr = tr_M_atomic(Z, N, include_inter=True)
    t_sym = time.time() - t0
    n_ops = sp.count_ops(expr)
    print(f"  symbolic tr_M:  {t_sym:.1f} s  (ops = {n_ops})")

    t1 = time.time()
    combined = sp.together(expr)
    t_tog = time.time() - t1
    print(f"  sp.together:    {t_tog:.1f} s")

    free = list(combined.free_symbols)
    if not free:
        return {"error": "no free symbol in tr_M expression"}
    q = next((s for s in free if str(s) == "q"), free[0])
    u = sp.Symbol("u", positive=True, real=True)

    t2 = time.time()
    p_u, shift, denom = to_u_polynomial(combined, q, u)
    t_to_u = time.time() - t2
    deg_p = int(sp.Poly(p_u, u).degree()) if p_u != 0 else 0
    factored = _factor_denominator(denom, u)
    print(f"  to_u_polynomial:{t_to_u:.1f} s  (deg p(u) = {deg_p})")
    print(f"  D(u) factored = {factored}")

    t3 = time.time()
    coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)
    t_cyc = time.time() - t3
    all_int = all(c["integral"] for c in coeffs)
    print(f"  cyclotomic_expansion: {t_cyc:.1f} s  ({len(coeffs)} terms,"
          f" all integral = {all_int})")

    # Reconstruction sanity check (cheap)
    t4 = time.time()
    recon = reconstruct(coeffs, u, max_m=max_m)
    matches_recon = (p_u - recon).equals(0)
    t_rec = time.time() - t4
    print(f"  reconstruction check: {t_rec:.1f} s  matches = {matches_recon}")

    return {
        "Z": Z,
        "N": N,
        "A": Z + N,
        "deg_p_u": deg_p,
        "shift": shift,
        "denom_in_u": denom,
        "denom_factored": factored,
        "p_in_u_degree": deg_p,
        "habiro_coefficients": coeffs,
        "all_integral": all_int,
        "reconstruction_matches": bool(matches_recon),
        "timings_sec": {
            "symbolic_trace": round(t_sym, 2),
            "together": round(t_tog, 2),
            "to_u_poly": round(t_to_u, 2),
            "cyclotomic": round(t_cyc, 2),
            "reconstruction_check": round(t_rec, 2),
        },
        "sympy_ops_raw": int(n_ops),
    }


def main() -> int:
    print("Habiro coefficients via markov_peel symbolic-q pipeline")
    print("=" * 72)

    # A=2..4 are quick.  A=5 is heavier but feasible (~1 min).  A=6 is
    # heavy (5-15 min) — gated by an env var so the default invocation
    # stays fast for CI.  Run with HABIRO_EXT_INCLUDE_LI=1 to enable.
    cases = [
        ("D (deuteron, A=2)",    1, 1, 18),
        ("T (triton, A=3)",      1, 2, 18),
        ("³He (helion, A=3)",    2, 1, 18),
        ("⁴He (alpha, A=4)",     2, 2, 22),
    ]
    import os
    if os.environ.get("HABIRO_EXT_INCLUDE_LI") == "1":
        cases.append(("⁵Li (A=5)", 3, 2, 25))
        cases.append(("⁶Li (A=6)", 3, 3, 28))
    # A=7..8 — heavier atoms gated by a separate env var. These take
    # ~10-30 min each on the symbolic markov_peel pipeline at single
    # thread. Extends the 4-way 1ppb gate to ⁷Li / ⁷Be / ⁸Be.
    if os.environ.get("HABIRO_EXT_INCLUDE_HIGHER") == "1":
        cases.append(("⁷Li (A=7)", 3, 4, 32))
        cases.append(("⁷Be (A=7)", 4, 3, 32))
        cases.append(("⁸Be (A=8)", 4, 4, 35))

    results: dict[str, dict] = {}
    for label, Z, N, max_m in cases:
        try:
            results[label] = _analyse_atom(label, Z, N, max_m)
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            results[label] = {"error": f"{type(exc).__name__}: {exc}"}

    out = {
        "computation": "habiro-coefficients-extended",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Cyclotomic Habiro coefficients a_m(u) of tr_M(T_w, q) for "
            "atomic braids A = 2..6 via the markov_peel symbolic-q "
            "pipeline (vs the original habiro_coefficients_atomic.py "
            "Hoefsmit-symbolic pipeline which was intractable for A ≥ 3). "
            "Each row contains the full integer expansion p(u) = "
            "Σ_m a_m(u) · (u; u)_m together with D(u) (the Markov-"
            "normalisation denominator, factored) and verification that "
            "every a_m has integer coefficients (the cyclotomic "
            "integrality witness).  Resolves the D(u) blocker noted in "
            "habiro-coefficients-interpolate.witness.json."
        ),
        "reference_blocks": [
            "def:habiro-ring",
            "prop:habiro-expansion-atomic",
            "prop:full-pole-structure-mass-trace",
            "thm:knot-mass-formula-unified",
        ],
        "engine": "python+sympy+markov_peel",
        "results": results,
    }
    out_path = HERE / "habiro-coefficients-extended.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="sympy")
    out["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWitness: {out_path}")

    # Exit non-zero when any atom errored. This returned 0 unconditionally,
    # and the errors are recorded INSIDE the witness (`results[label] =
    # {"error": ...}`, above), so a total failure was indistinguishable from a
    # clean run to anything reading the exit code.
    #
    # It is not hypothetical. As of 2026-08-21 this script fails on ALL FOUR
    # atoms — `ValueError: LaurentQ.from_sympy: non-Laurent factor
    # -(1 - 1/q**4)*(q - 1)**2/12 + 1/2` — and still exited 0. The witness it
    # writes here is 4/4 errors; the good copy the corpus actually consumes is
    # a separate file at `computations/` that this script no longer reaches
    # (bean qou-kcii) and, given the failure, can no longer reproduce.
    #
    # So any sweep that "re-runs producers" would overwrite good data with
    # error stubs and report success. That is the specific accident this
    # guards, and it nearly happened here: the fix proposed for the L1 gate's
    # pin straddle (bean qou-3zby) was "regenerate this witness", which would
    # have destroyed the only working copy.
    _errored = sorted(k for k, v in results.items()
                      if isinstance(v, dict) and "error" in v)
    if _errored:
        print(f"\n✗ {len(_errored)} of {len(results)} atoms ERRORED: "
              f"{', '.join(_errored)}\n"
              "  The witness above records the errors and is NOT a usable "
              "result. Do not treat it as a regeneration, and do not copy it "
              "over a good witness.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
