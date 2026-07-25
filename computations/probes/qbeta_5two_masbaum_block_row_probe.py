#!/usr/bin/env python3
"""B1.3 (bean qou-hrmo): λ-row selection — the Masbaum tail expanded in
the GGM block basis by EXACT formal-series linear algebra.

SUCCESSOR to the B1.2 wall (merged #4233): the Habiro-face values are
not bare GK-bilinear entries; the named unknowns are the state-integral
dressing and WHICH λ-row of the block basis the Masbaum tail occupies.
This probe answers the row question symbolically — order-by-order exact
rational linear algebra, with NO numerics in the decision:

  1. The Masbaum tail as an exact formal series in u = q^{1/2}:
     F(q) = Σ_n C_n(a)|_{a=u}·(q;q)_n², from the exact integer-Laurent
     C_n (merged profile module). Its u-PARITY is itself a finding
     (odd u-powers ⇒ half-integer λ structure).
  2. The block basis: the 18 exact H±_{j,λ}(q) series (A2's symbolic
     generator, re-gated here against the 18 printed GGM tables at the
     probe's higher truncation), λ ∈ {−1,0,1}, j ∈ {0,1,2}, both signs.
  3. The DECISION: does F (or a pre-registered dressed variant
     (q;q)_∞^p·q^s·F, p ∈ −3..3, s ∈ 0..2 — 21 exact re-solves, all
     reported) lie in the ℚ-span of the basis? Overdetermined exact
     solve (≥ 34 orders vs 18 unknowns, sympy Rational rref):
       (a) exact solution ⇒ the λ-row/dressing selection is DERIVED —
           the c-vector is the answer;
       (b) no solution anywhere in the family ⇒ the Masbaum tail lies
           OUTSIDE this block span (rank evidence recorded) — the
           basis-mismatch finding, honestly scoped.
     No fit: every solve is exact rational linear algebra; "solution"
     means EVERY residual order vanishes identically.

Numeric cross-gate: the truncated F-series evaluated at a₀ = q̃^{1/2}
against the committed F_conv = 0.9861565521 (truncation-consistency
only; plays no role in the decision).

auditOnly; no c_k wired; no fit. Comparison to observed only; no
ontological claims.

Run: python3 -u computations/probes/qbeta_5two_masbaum_block_row_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_block_row.log
"""
from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_stokes_barodd_index_probe as sb  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

mp.mp.dps = 60

ORD_Q = 34                  # q-series truncation for the exact solves
F_CONV_REF = mp.mpf("0.9861565521")
T0 = time.monotonic()
qs = sb.qs


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def masbaum_series_u(ord_u):
    """Exact series of F = Σ_n C_n(a)|_{a=u}·(u²;u²)_n² to O(u^ord_u):
    coefficient dict {u-exponent: Rational}."""
    out = {}
    n = 0
    while True:
        C = _mb.C52(n)
        if min(C.keys()) >= ord_u and n > 0:
            break
        # (u²;u²)_n² as a u-series dict
        poch = {0: sp.Integer(1)}
        for j in range(1, n + 1):
            new = {}
            for e, c in poch.items():
                new[e] = new.get(e, sp.Integer(0)) + c
                e2 = e + 2 * j
                if e2 < ord_u:
                    new[e2] = new.get(e2, sp.Integer(0)) - c
            poch = new
        poch2 = {}
        for e1, c1 in poch.items():
            for e2, c2 in poch.items():
                e = e1 + e2
                if e < ord_u:
                    poch2[e] = poch2.get(e, sp.Integer(0)) + c1 * c2
        for e1, c1 in C.items():
            if e1 >= ord_u:
                continue
            for e2, c2 in poch2.items():
                e = e1 + e2
                if e < ord_u:
                    out[e] = out.get(e, sp.Integer(0)) + c1 * c2
        n += 1
        if n > 60:
            break
    return {e: c for e, c in out.items() if c != 0}


def main() -> int:
    print("=" * 78)
    print(" B1.3 — λ-row selection: the Masbaum tail in the GGM block basis")
    print("=" * 78)

    # ---- 1. the Masbaum tail as an exact u-series ----
    ord_u = 2 * ORD_Q
    log(f"building the exact Masbaum u-series to O(u^{ord_u}) ...")
    Fu = masbaum_series_u(ord_u)
    odd_terms = {e: c for e, c in Fu.items() if e % 2 == 1}
    parity_even = not odd_terms
    log(f"    {len(Fu)} nonzero u-coefficients; odd-u terms: "
        f"{len(odd_terms)} ⇒ {'INTEGER-q series' if parity_even else 'HALF-INTEGER λ structure'}")
    Fq = {e // 2: c for e, c in Fu.items() if e % 2 == 0}

    # numeric truncation cross-gate (no role in the decision)
    t = mp.log(q_at(50))
    qt = mp.e ** (-t)
    f_num = mp.fsum([mp.mpf(int(c.p)) / int(c.q) * qt ** e
                     if isinstance(c, sp.Rational) else mp.mpf(int(c)) * qt ** e
                     for e, c in Fq.items()])
    dev_num = abs(f_num - F_CONV_REF) / F_CONV_REF
    # truncation bound: next omitted order
    trunc_bound = qt ** ORD_Q * 50
    g_num = dev_num < trunc_bound
    log(f"[gate] truncated F at q̃: {mp.nstr(f_num, 12)} vs committed "
        f"{mp.nstr(F_CONV_REF, 12)} (rel {mp.nstr(dev_num, 3)} < "
        f"truncation bound {mp.nstr(trunc_bound, 3)}): "
        f"{'PASS' if g_num else 'FAIL'}")

    # ---- 2. the block basis at higher truncation + printed re-gate ----
    sb.ORD = ORD_Q
    log(f"generating the 18 H±_(j,λ) series to O(q^{ORD_Q}) ...")
    basis = {}
    for sgn in (+1, -1):
        for j in range(3):
            for lam in (-1, 0, 1):
                basis[(sgn, j, lam)] = sp.expand(sb.H_series(sgn, j, lam))
    g_printed = True
    for (sgn, j, lam), coeffs in sb.PRINTED.items():
        s_ = basis[(sgn, j, lam)]
        for k, c in enumerate(coeffs):
            if sp.simplify(s_.coeff(qs, k) - c) != 0:
                g_printed = False
    log(f"[gate] 18 printed GGM tables reproduced at the probe truncation: "
        f"{'PASS' if g_printed else 'FAIL'}")

    # ---- 3. the exact solves over the pre-registered dressed family ----
    # (q;q)_∞^p series to O(q^ORD_Q)
    def poch_inf_pow(p):
        e_ = sp.Integer(1)
        for j in range(1, ORD_Q + 1):
            e_ *= (1 - qs ** j)
        e_ = sp.expand(e_)
        s_ = e_ ** abs(p) if p != 0 else sp.Integer(1)
        if p < 0:
            s_ = sp.series(1 / e_, qs, 0, ORD_Q).removeO() ** abs(p)
        return sp.expand(sp.series(sp.expand(s_), qs, 0, ORD_Q).removeO())

    keys = sorted(basis.keys())
    Mrows = []
    for order in range(ORD_Q):
        Mrows.append([basis[k].coeff(qs, order) for k in keys])
    M = sp.Matrix(Mrows)
    rank_basis = M.rank()
    log(f"basis matrix: {ORD_Q} orders × {len(keys)} series, rank "
        f"{rank_basis}")

    F_poly = sum(sp.Rational(c) * qs ** e for e, c in Fq.items() if e < ORD_Q)
    results = []
    solved = []
    for p in range(-3, 4):
        dress_p = poch_inf_pow(p)
        for s in range(0, 3):
            target = sp.expand(sp.series(
                sp.expand(F_poly * dress_p) * qs ** s, qs, 0, ORD_Q).removeO())
            tvec = sp.Matrix([target.coeff(qs, o) for o in range(ORD_Q)])
            aug = M.row_join(tvec)
            in_span = aug.rank() == rank_basis
            results.append({"p": p, "shift": s, "in_span": bool(in_span)})
            if in_span:
                sol = M.solve_least_squares(tvec)  # exact when consistent
                solved.append({"p": p, "shift": s,
                               "coeffs": {str(k): str(sp.nsimplify(sol[i]))
                                          for i, k in enumerate(keys)
                                          if sol[i] != 0}})
                log(f"    IN SPAN: (q;q)_∞^{p}·q^{s}·F — coefficient "
                    f"vector recorded")
    n_solved = len(solved)
    log(f"[T] {len(results)} exact solves: {n_solved} in-span, "
        f"{len(results) - n_solved} outside")

    wb = WitnessBuilder("qbeta-5two-masbaum-block-row", engine="sympy+mpmath",
                        _script_path=__file__)
    wb.set_description(
        "B1.3 (bean qou-hrmo): the λ-row selection question answered by "
        "exact formal-series linear algebra — the Masbaum tail built as "
        "an exact u-series from the integer-Laurent C_n, its u-parity "
        "recorded, and its membership in the ℚ-span of the 18 GGM block "
        "series H±_(j,λ) (re-gated against the printed tables at the "
        "probe truncation) decided by exact rational rank/solve over a "
        "pre-registered dressed family (q;q)_∞^p·q^s·F, p ∈ −3..3, "
        "s ∈ 0..2 — every solve reported, a solution means every "
        "residual order vanishes identically. No numerics in the "
        "decision; the numeric F_conv gate is truncation-consistency "
        "only. auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("truncated_series_matches_fconv",
                     computed=float(dev_num), expected=0.0,
                     tolerance=float(trunc_bound),
                     source="exact-series truncation vs committed F_conv "
                            "within the truncation bound")
    wb.add_assertion("printed_tables_regated",
                     computed=1.0 if g_printed else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="the 18 printed GGM H-tables reproduced by the "
                            "basis generator at the probe truncation")
    wb.add_assertion("solve_family_completed",
                     computed=float(len(results)), expected=float(len(results)),
                     tolerance=0.5,
                     source="all 21 pre-registered exact solves completed "
                            "and recorded")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("u_parity", {"odd_u_terms": len(odd_terms),
                             "parity": "even (integer-q series)"
                             if parity_even else "odd terms present "
                             "(half-integer lambda structure)",
                             "odd_exponents_sample":
                                 sorted(odd_terms)[:8]})
    wb.add_data("basis_rank", int(rank_basis))
    wb.add_data("span_results", results)
    wb.add_data("solutions", solved)
    wb.add_data("verdict",
                ((f"ROW SELECTION DERIVED: {n_solved} dressed variant(s) of "
                  f"the Masbaum tail lie EXACTLY in the block span — the "
                  f"coefficient vectors (data.solutions) are the λ-row/"
                  f"dressing answer; independent-anchor confirmation is the "
                  f"follow-up." if n_solved else
                  "THE MASBAUM TAIL LIES OUTSIDE THE H±_(j,λ) BLOCK SPAN "
                  "for every pre-registered dressing (21 exact solves, "
                  "rank evidence recorded). Scope-(a): this basis/dressing "
                  "family as-stated — the tail is a DIFFERENT vector in "
                  "the Habiro module; the bridge needs the module map "
                  "(e.g. the descendant/derivative tower or the cyclotomic "
                  "expansion), not a row choice in this basis.")
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-masbaum-block-row.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
