#!/usr/bin/env python3
"""Algebraic (q-parameterized) Markov trace  tr_M(q) ∈ ℚ(q).

Resolves the "B_sym is really B_arch — the algebraic object is missing"
observation. The production atom braid word (`atom_braid_word_3A`) bakes the
colour split `flavor_split_subleading(q₀)` **numerically** into the p-n
interface crossing, so the symbolic trace via `build_atom_symbolic` carries an
ugly numerical fraction (e.g. `104458189399543/16000000000000000`) instead of a
clean Laurent object. This module keeps the colour δ **symbolic** (its closed
form in q), giving the genuine algebraic trace `tr_M(q) ∈ ℚ(q)` whose
archimedean realization at the substrate q₀ — `B_sym = E₀·ln(tr_free/tr_atom)` —
is what the mass-binding dashboard reports as the (archimedean) `B_sym`.

The atom word uses only:
  * intra-nucleon crossings  c = 1, d ∈ {0, −h/2, −h}   (h = q − q⁻¹)
  * p-p interface  (1, 0) · n-n interface  (1, −h)
  * p-n interface  (1, −h·(½ − δ(q)/4)),  δ(q) = flavor_split_subleading(q)
so every factor is `σ_g + d·I` with d a symbolic element of ℚ(q): no q₀ bake.

Verified (see __main__ / witness): `tr_M_algebraic(Z,N).subs(q, q₀)` reproduces
the canonical transfer value `tr_m_atom_zn(Z,N)` to ~1e-8 for D/T/³He — the
algebra is exact, the residual is float64 cancellation in evaluating the
degree-O(100) rational at q₀ (the transfer is 50-dps).

This is a generic-q builder ("at least for q like q₀"): pass any `q` (a sympy
Symbol for the full ℚ(q) form, or a numeric value to evaluate there). A true
q-SWEEP of the *observable* still needs Im(q₀)=0 at the archimedean wall — this
module gives the fibre-level algebraic object, not an archimedean continuation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))


def flavor_split_subleading_sym(q):
    """Symbolic `flavor_split_subleading(q)` (colour δ), matching
    `_li_2_q_util.flavor_split_subleading` at any q:

        δ(q) = leading·(1 + ℏ³),  leading = (q−1)²(1−q⁻⁴)/3,  ℏ = (q−1)/q.
    """
    leading = (q - 1) ** 2 * (1 - q ** (-4)) / sp.Integer(3)
    hbar = (q - 1) / q
    return leading * (1 + hbar ** 3)


def build_atom_symbolic_q(Z: int, N: int, q=None, *, include_inter: bool = True,
                          reduce_every: int = 4):
    """q-parameterized atom braid as a reduced `SymbolicHeckeElement`.

    Mirrors `mass_at_3A_proper.atom_braid_word_3A` (canonical
    `bring_color_weighted` convention) but emits symbolic `d` — intra crossings
    mapped by value to {0, −h/2, −h}, interfaces built by TYPE so the p-n colour
    δ stays symbolic (it is numerically indistinguishable from −h/2, so it must
    be placed structurally, not matched).
    """
    from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1)
    from q_parameter import HA as _h_num
    from hecke_symbolic import SymbolicHeckeDivision, SymbolicHeckeElement

    if q is None:
        q = sp.Symbol("q", positive=True)
    h = q - 1 / q
    delta = flavor_split_subleading_sym(q)
    h_num = float(_h_num)

    def _intra_d(dn: float):
        if abs(dn) < 1e-9:
            return sp.Integer(0)
        if abs(dn + h_num) < 1e-5:
            return -h
        if abs(dn + h_num / 2) < 1e-5:
            return -h / 2
        raise ValueError(f"unmapped intra crossing d={dn} (not in 0,−h/2,−h)")

    A = Z + N
    ordering = ["p"] * Z + ["n"] * N
    factors: list[tuple] = []
    for k, nuc in enumerate(ordering):
        g0 = _PROTON_G0 if nuc == "p" else _NEUTRON_G0
        g1 = _PROTON_G1 if nuc == "p" else _NEUTRON_G1
        for _c, d in g0:
            factors.append((_intra_d(float(d)), 3 * k))
        for _c, d in g1:
            factors.append((_intra_d(float(d)), 3 * k + 1))
        if include_inter and k < A - 1:
            nxt = ordering[k + 1]
            if nuc == "p" and nxt == "p":
                dd = sp.Integer(0)                              # p-p: σ
            elif nuc == "n" and nxt == "n":
                dd = -h                                         # n-n: σ − h·I
            else:
                dd = -h * (sp.Rational(1, 2) - delta / 4)       # p-n: colour δ symbolic
            factors.append((dd, 3 * k + 2))

    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since = 0
    for d, g in factors:
        elem = elem * SymbolicHeckeElement({(g,): sp.Integer(1), (): d})
        since += 1
        if since >= reduce_every:
            elem, _ = div.reduce(elem, engine="laurent")
            since = 0
    if since:
        elem, _ = div.reduce(elem, engine="laurent")
    return elem


def tr_M_algebraic(Z: int, N: int, q=None, *, include_inter: bool = True):
    """Algebraic Markov trace `tr_M(q) ∈ ℚ(q)` of the (Z,N) atom braid."""
    from markov_trace_canonical import tr_M_element
    if q is None:
        q = sp.Symbol("q", positive=True)
    elem = build_atom_symbolic_q(Z, N, q, include_inter=include_inter)
    return sp.expand(tr_M_element(elem, 3 * (Z + N), simplify=False))


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true",
                    help="also cross-check ³He (n=9, slower symbolic trace)")
    args = ap.parse_args()

    from q_parameter import Q as Q0
    from tr_m_atom_via_transfer import tr_m_atom_zn
    try:
        from witness_base import WitnessBuilder
    except Exception:
        WitnessBuilder = None

    q = sp.Symbol("q", positive=True)
    q0 = float(Q0)
    atoms = [("D", 1, 1), ("T", 1, 2)] + ([("3He", 2, 1)] if args.full else [])

    rows = []
    print(f"algebraic tr_M(q) ∈ ℚ(q)  — q₀ cross-check vs transfer  (q₀={q0:.6f})")
    for nm, Z, N in atoms:
        ta_q = tr_M_algebraic(Z, N, q, include_inter=True)
        tf_q = tr_M_algebraic(Z, N, q, include_inter=False)
        ta0, tf0 = float(ta_q.subs(q, q0)), float(tf_q.subs(q, q0))
        ta_ref, tf_ref, _, _ = tr_m_atom_zn(Z, N, dps=50)
        ta_ref, tf_ref = float(ta_ref), float(tf_ref)
        d_atom, d_free = abs(ta0 - ta_ref), abs(tf0 - tf_ref)
        rows.append({"atom": nm, "Z": Z, "N": N,
                     "tr_atom_q0_algebraic": ta0, "tr_atom_transfer": ta_ref,
                     "tr_free_q0_algebraic": tf0, "tr_free_transfer": tf_ref,
                     "abs_diff_atom": d_atom, "abs_diff_free": d_free})
        print(f"  {nm:>4}: tr_atom {ta0:.9f} vs {ta_ref:.9f} (Δ={d_atom:.1e})  "
              f"tr_free {tf0:.9f} vs {tf_ref:.9f} (Δ={d_free:.1e})")

    # δ symbolic matches the production helper at q0
    from _li_2_q_util import flavor_split_subleading
    d_delta = abs(float(flavor_split_subleading_sym(q).subs(q, q0))
                  - float(flavor_split_subleading(Q0)))
    print(f"  δ(q₀): symbolic vs _li_2_q_util  Δ={d_delta:.1e}")

    if WitnessBuilder is not None:
        w = WitnessBuilder("tr-m-algebraic-q", engine="sympy")
        w.set_description(
            "Algebraic q-parameterized Markov trace tr_M(q) ∈ ℚ(q): the atom "
            "braid word with the colour split flavor_split_subleading(q) kept "
            "SYMBOLIC (vs the production q₀-baked float), so the trace is a clean "
            "Laurent object. Cross-checked: tr_M_algebraic(Z,N).subs(q,q₀) == the "
            "canonical transfer value tr_m_atom_zn(Z,N) to ~1e-8 for D/T(/³He) "
            "(float64-eval floor of the exact form)."
        )
        w.add_parameter("q0", q0)
        w.add_data("rows", rows)
        worst = max([r["abs_diff_atom"] for r in rows]
                    + [r["abs_diff_free"] for r in rows])
        w.add_assertion(name="algebraic_q0_matches_transfer",
                        computed=worst, expected=0.0, tolerance=1e-7,
                        source="max |tr_M_algebraic(q₀) − tr_m_atom_zn| over D/T(/³He), "
                               "atom & free words; ~1e-8 float64-eval floor of the "
                               "exact ℚ(q) form vs the 50-dps transfer")
        w.add_assertion(name="symbolic_delta_matches_li2q",
                        computed=d_delta, expected=0.0, tolerance=1e-12,
                        source="flavor_split_subleading_sym(q₀) vs _li_2_q_util")
        out = w.save()
        print(f"  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
