#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical shape diagnostic over the
# mass-binding dashboard ratios; no symbolic-q polynomial output.
"""
Δ_λ shape probe — does the dashboard mis-scale collapse under ONE factor?

The low-isotope dashboard (`mass_binding_dashboard.py`) shows the canonical
binding forms (B_sym exact-log-trace, B_qCLT_fac colour-weighted) tracking
the SHAPE of AME binding (right ordering, right p↔n chirality sign) but
uniformly mis-scaled — error ratios r = B_AME/B_model run 0.57–2.4 with no
single global factor.

This probe asks the formalize-first question BEFORE committing a wide Δ_λ
search: is the residual ratio r explained by a SINGLE structural factor
g(K) — A, A−1, #bonds, #pn-bonds, … — i.e. does r/g collapse to a constant?
If yes, the per-isotope binding needs only one per-A correction, not the full
per-partition Δ_λ. If no, the per-partition Δ_λ programme (GAP-A-3/4) is
confirmed necessary — and the just-landed deuteron closure
`Δ_λ = (Wedderburn magnitude)×(icosahedral chirality sign)` (main 6d68481e)
is the right level, not a global per-A factor.

Verdict = the candidate g minimising the coefficient of variation (CV) of
r/g across the isotopes. CV ≈ 0 ⇒ that factor collapses the residual.

Run:  python3 -u computations/delta_lambda_shape_probe.py 2>&1 | tee /tmp/dl.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import math
import statistics as st
import sys

from mass_binding_dashboard import (  # noqa: E402
    _constants, _bond_type_L, _nucleon_msym, _ame_table, _row, GROUPS,
)


def _cv(xs):
    """Coefficient of variation (stdev/mean); 0 ⇒ perfectly collapsed."""
    xs = [x for x in xs if x is not None]
    if len(xs) < 2:
        return None
    m = st.fmean(xs)
    return (st.pstdev(xs) / abs(m)) if m else None


def main() -> int:
    me, q0, E0, g8 = _constants()
    Lbond = _bond_type_L()
    nm = _nucleon_msym(E0)
    ame = _ame_table()
    rows = [_row(n, Z, N, E0, me, g8, Lbond, nm, ame, 21)
            for (n, Z, N) in GROUPS["low"]]

    # structural factors g(K) to test as the single collapsing correction
    def factors(r):
        A, Z, N = r["A"], r["Z"], r["N"]
        npairs = A * (A - 1) // 2
        return {
            "1 (global)":   1.0,
            "A":            A,
            "A-1":          A - 1,
            "n_pn":         r["n_pn"],
            "n_pairs":      npairs,
            "ln A":         math.log(A),
            "sqrt A":       math.sqrt(A),
            "(A-1)/A":      (A - 1) / A,
        }

    for model in ("B_sym", "B_qCLT_fac"):
        print(f"\n### residual r = B_AME / {model}, and r/g collapse test")
        rs, fac_rows = [], []
        for r in rows:
            if r[model] and r["B_AME"]:
                ratio = r["B_AME"] / r[model]
                rs.append(ratio)
                fac_rows.append((r["name"], ratio, factors(r)))
        print(f"  raw r: " + "  ".join(f"{nm_}={rt:.3f}"
                                       for nm_, rt, _ in fac_rows))
        print(f"  CV(r) (no correction) = {_cv(rs):.4f}")
        # for each candidate g, collapse r/g and report CV
        cand = fac_rows[0][2].keys()
        scored = []
        for g in cand:
            collapsed = [rt / f[g] for _, rt, f in fac_rows]
            scored.append((g, _cv(collapsed)))
        scored.sort(key=lambda t: (t[1] is None, t[1]))
        print("  collapse CV by single factor g (smaller = better):")
        for g, cv in scored:
            print(f"    r / ({g:<12}) → CV = {cv:.4f}")
        best_g, best_cv = scored[0]
        verdict = ("COLLAPSES" if best_cv is not None and best_cv < 0.05
                   else "does NOT collapse")
        print(f"  ⇒ best single factor: {best_g}  (CV={best_cv:.4f}) — {verdict}")

    print("\n  Reading: a single structural g with CV ≳ 0.1 means NO per-A "
          "factor linearises the residual — the per-partition Δ_λ programme "
          "(GAP-A-3/4; deuteron closure main 6d68481e) is confirmed needed, "
          "not a global per-A rescale.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
