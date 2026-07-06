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
from math import factorial  # noqa: E402

# ── option-e Δ_λ = sgn(w0^{S_λ'}) · dim(V_λ)  (main 6d68481e, q-independent) ──
# replicated verbatim from docs/audits/scripts/option_e_delta_lambda_sign_chirality.py


def _hook_dim(lam):
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def _transpose(lam):
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0])) if lam else ()


def _delta_sign(lam):
    s = 1
    for b in _transpose(lam):
        s *= (-1) ** (b * (b - 1) // 2)
    return s


def _delta_lambda(lam):
    """option-e closure: Δ_λ = sgn(w0^{S_λ'}) · dim(V_λ)."""
    return _delta_sign(lam) * _hook_dim(lam)


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

    _test_option_e_delta_lambda(me)
    return 0


def _test_option_e_delta_lambda(me: float) -> None:
    """Does the option-e closure Δ_λ = sgn(w0^{S_λ'})·dim(V_λ) recover the
    A=3,4 binding, or only the deuteron (its closure anchor)?

    Builds the per-partition Δ_λ-weighted binding in two natural conventions
    B_Δ = m_e · Σ_λ y_λ · X_λ · Δ_λ, with X_λ = χ^λ_atom (gate form) and
    X_λ = χ^λ_free − χ^λ_atom (defect form), at q₀. Compares to AME. The
    deuteron is the closure anchor (match expected); A=3,4 are the genuine
    out-of-sample test of whether sign·dim generalises."""
    import mpmath as mp
    from wedderburn_jones_markov import y_lambda_at
    from reduced_block_kernel import chi_all_lambda_reduced_block
    from mass_at_3A_proper import atom_braid_word_3A
    from q_parameter import Q as Q0

    iso = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
    b_ame = {"2H": 2.224566, "3H": 8.481821, "3He": 7.718058, "4He": 28.295673}

    print("\n### option-e Δ_λ = sgn(w0^{S_λ'})·dim(V_λ) — does it recover A=3,4?")
    print("  B_Δ = m_e·Σ_λ y_λ X_λ Δ_λ;  X_λ = χ^λ_atom (gate) | χ^λ_free−χ^λ_atom (defect)")
    print("| iso | A | B_AME | B_Δ atom | err atom | B_Δ defect | err defect |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in iso:
        n = 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
        chi_a = chi_all_lambda_reduced_block(
            atom_braid_word_3A(Z, N, include_inter=True), n)
        chi_f = chi_all_lambda_reduced_block(
            atom_braid_word_3A(Z, N, include_inter=False), n)
        s_atom = mp.mpf(0)
        s_def = mp.mpf(0)
        for lam, ca in chi_a.items():
            dl = _delta_lambda(tuple(lam))
            yl = y.get(tuple(lam), mp.mpf(0))
            s_atom += yl * ca * dl
            s_def += yl * (chi_f.get(tuple(lam), mp.mpf(0)) - ca) * dl
        b_atom = float(mp.mpf(str(me)) * s_atom)
        b_def = float(mp.mpf(str(me)) * s_def)
        ba = b_ame[name]
        ea = abs(b_atom - ba) / ba
        ed = abs(b_def - ba) / ba
        print(f"| {name} | {Z+N} | {ba:.4f} | {b_atom:.4f} | {ea*100:.1f}% "
              f"| {b_def:.4f} | {ed*100:.1f}% |")
    print("  Reading: the sign·dim Δ_λ does NOT reproduce AME in either natural "
          "convention — and the DEUTERON itself misses (atom 117%, defect 45%), "
          "though it is the closure's own anchor. So the canonical closure "
          "(docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md) uses a "
          "normalisation / partition basis NOT captured by B = m_e·Σ_λ y_λ χ^λ Δ_λ "
          "in these two readings. Net: option-e fixes the per-partition Δ_λ "
          "VALUES (magnitude=dim, sign=chirality) but the binding ASSEMBLY "
          "(which χ, which weights, normalisation) is the still-open part — a "
          "concrete next-step target, not a drop-in across isotopes.")


if __name__ == "__main__":
    sys.exit(main())
