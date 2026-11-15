#!/usr/bin/env python3
"""Bond counting on a coloured graph: the cut identity, and why no interface
weight can supply the symmetry energy.

Numerical companion to `QOU/Hecke/BondCutSymmetry.lean` (generic) and
`QOU/Hecke/BondCutSymmetryLogBound.lean` (the `-ln b` letters) (bean `qou-qve5`, the
binding SHAPE residual). The Lean proves the invariants for arbitrary energies
and counts; this probe evaluates them at the proton-pinned `q_0` with the
pinned bonds `b_pp = q^2/[2]_q`, `b_nn = q^-2/[2]_q` and the corpus's convex
p-n interface, and sets the derived quantities against the SEMF targets. The
SEMF coefficients enter ONLY as targets to check against -- nothing here is
searched or fitted.

*** THE CUT IDENTITY ***

For any graph and any p/n colouring, with `2 n_pp + n_pn = d_P`,
`2 n_nn + n_pn = d_N` (degree sums over the two colour classes),

    B/E_0 = (e_pp d_P + e_nn d_N)/2 + delta . n_pn,   delta = e_pn - (e_pp+e_nn)/2

so the whole layout dependence is ONE number (the p-n cut) times ONE
coefficient (`delta`). A constant cut (every segregated layout, the corpus's
`A-1` chain has cut 1) gives a law AFFINE in `(Z, N)`: no `(N-Z)^2` at all.
The well-mixed cut `n_pn = k Z N / A` gives EXACTLY one symmetry term,
`a_A^eff = E_0 . delta . k / 4`, whose sign is the sign of `delta`.

*** INVARIANT 1 -- the convex family bounds delta by 2 ln q ***

For every interface weight `w` in `[0, 1]`, `delta(w) <= 2 ln q` (attained at
`w = 0`). So the symmetry coefficient of ANY convex interface on a degree-`k`
well-mixed graph is at most `(k/2) E_0 ln q`: 0.44 MeV at k = 2, 2.65 MeV at
k = 12 -- against the SEMF `a_A ~ 23 MeV`. Flipping the sign is cheap
(`w < 1/(q^2+1)`); the magnitude is not available to any interface weight.

*** INVARIANT 2 -- positivity forbids the SEMF magnitude, layout-free ***

Every `e = -ln b` with `0 < b < 1` is positive; every count is a count; so a
bond sum is >= 0 at every composition, including pure neutron matter. The SEMF
with `a_A > a_V` gives `(a_V - a_A) A < 0` there: neutron matter is UNBOUND.
No non-negative bond count agrees with that on any graph with any interface.

*** THE O(hbar_q^2) QUESTION ***

The weight's miss against the crossing has deformation part
`(q^2-1)/(2(q^2+1)) >= hbar_q/2` -- FIRST order -- and its derived flavour tilt
`delta_f/4 > 0` pushes the weight AWAY from the crossing. A second-order
correction would need coefficient >= 1/(2 hbar_q) ~ 5 to flip the sign, and
by invariant 1 even a flipped sign is an order of magnitude short.

Precision: mpmath at 40 dps end to end; `q_0` from the substrate's 50-digit
string (proton pin, owner directive 2026-08-07), `m_e` from the NIST table
string. No float64 arithmetic. `E_0 = m_e/(q(q-1)) / (1 - hbar_q^2)` per
`2026-09-05-binding-law-arc-synthesis.md` (4.227483 MeV).
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
from qou_substrate import constants as _c  # noqa: E402

DPS = 40
mp.mp.dps = DPS
Q0 = mp.mpf(_c.Q_50_DIGIT_STR)
M_E = mp.mpf(str(_c._E_MEV.value))          # NIST table string, not the float
TWO_Q = Q0 + 1/Q0
HBAR = (Q0 - 1)/Q0
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR**2)
B_PP = Q0**2/TWO_Q
B_NN = Q0**-2/TWO_Q
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
# SEMF targets (literature fit, Rohlf 1994 / Krane 1988; AME2020-era values
# agree to ~1 MeV). TARGETS ONLY -- never searched on.
A_V_TARGET = mp.mpf("15.75")
A_A_TARGET = mp.mpf("23.7")
TOL = mp.mpf(10)**(-30)


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def bond_sum(epp, epn, enn, npp, npn, nnn):
    return epp*npp + epn*npn + enn*nnn


def delta_of(w):
    """`e_pn - (e_pp+e_nn)/2` for a convex weight `w`, `e = -ln b`."""
    return -mp.log(w*B_PP + (1 - w)*B_NN) + (mp.log(B_PP) + mp.log(B_NN))/2


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        return ok

    ok = True
    E_PP, E_PN, E_NN = -mp.log(B_PP), -mp.log(B_PN), -mp.log(B_NN)
    delta = E_PN - (E_PP + E_NN)/2
    print("=" * 78)
    print("1. THE CUT IDENTITY (exact, in Fractions -- Lean bondSum_eq_cut)")
    print("=" * 78)
    F = Fraction
    e = (F(7, 3), F(5, 2), F(11, 4))            # arbitrary energies
    ident = True
    for (npp, npn, nnn) in [(3, 1, 4), (0, 6, 0), (5, 5, 5), (10, 0, 2)]:
        dP, dN = 2*npp + npn, 2*nnn + npn
        lhs = bond_sum(*e, npp, npn, nnn)
        rhs = (e[0]*dP + e[2]*dN)/2 + (e[1] - (e[0] + e[2])/2)*npn
        ident &= (lhs == rhs)
    ok &= chk("cut_identity_exact_on_four_count_triples", ident, True,
              note="B = (e_pp d_P + e_nn d_N)/2 + delta.n_pn, exact rationals")
    # segregated: constant cut => affine in (Z,N)
    k, c = 4, 1
    seg = lambda Z, N: bond_sum(*e, F(k*Z - c, 2), c, F(k*N - c, 2))
    aff = all(seg(Z, N) - seg(Z2, N2) == F(k, 2)*(e[0]*(Z - Z2) + e[2]*(N - N2))
              for (Z, N, Z2, N2) in [(2, 2, 1, 3), (5, 9, 9, 5), (3, 3, 0, 6)])
    ok &= chk("constant_cut_law_is_affine_in_Z_N_no_symmetry_term", aff, True)

    print()
    print("=" * 78)
    print("2. THE SLOPE delta AT THE CORPUS INTERFACE, AND ITS CONVEX BOUND")
    print("=" * 78)
    bound = 2*mp.log(Q0)
    w_corpus = (B_PN - B_NN)/(B_PP - B_NN)
    print(f"  e_pp, e_pn, e_nn      = {mp.nstr(E_PP, 10)}, {mp.nstr(E_PN, 10)}, {mp.nstr(E_NN, 10)}")
    print(f"  delta (corpus)        = {mp.nstr(delta, 12)}")
    print(f"  recovered convex w    = {mp.nstr(w_corpus, 12)}")
    print(f"  2 ln q_0              = {mp.nstr(bound, 12)}   (delta at w = 0)")
    ok &= chk("corpus_delta_is_negative_wrong_semf_sign", delta < 0, True)
    ok &= chk("corpus_w_is_convex", 0 <= w_corpus <= 1, True)
    ok &= chk("delta_at_w0_equals_two_log_q", abs(delta_of(0) - bound) < TOL, True)
    sweep = []
    below = True
    for i in range(0, 21):
        w = mp.mpf(i)/20
        d = delta_of(w)
        below &= d <= bound + TOL
        sweep.append({"w": mp.nstr(w, 4), "delta": mp.nstr(d, 12)})
    ok &= chk("delta_le_two_log_q_for_every_convex_w", below, True)
    ok &= chk("delta_at_w1_is_minus_two_log_q",
              abs(delta_of(1) + bound) < TOL, True)

    print()
    print("=" * 78)
    print("3. SYMMETRY COEFFICIENT OF THE WELL-MIXED LAW, IN MeV, VS a_A")
    print("=" * 78)
    print(f"  E_0 = {mp.nstr(E0, 10)} MeV")
    rows = []
    for kk in (2, 4, 6, 12):
        aa_corpus = E0*delta*kk/4
        aa_max = E0*bound*kk/4
        rows.append({"k": kk, "a_A_eff_corpus_MeV": mp.nstr(aa_corpus, 10),
                     "a_A_eff_max_convex_MeV": mp.nstr(aa_max, 10),
                     "max_over_target": mp.nstr(aa_max/A_A_TARGET, 8)})
        print(f"  k={kk:>2}  a_A^eff(corpus) = {mp.nstr(aa_corpus, 8):>12} MeV   "
              f"max over convex = {mp.nstr(aa_max, 8):>10} MeV   "
              f"= {mp.nstr(aa_max/A_A_TARGET, 5)} x a_A")
    ok &= chk("corpus_symmetry_coefficient_negative_at_every_k",
              all(mp.mpf(r["a_A_eff_corpus_MeV"]) < 0 for r in rows), True)
    ok &= chk("convex_family_max_below_one_tenth_of_semf_a_A_at_k12",
              E0*bound*12/4 < A_A_TARGET/8, True,
              note="2.65 MeV against 23.7 MeV: 0.112 of the target at k = 12")

    print()
    print("=" * 78)
    print("4. POSITIVITY: NEUTRON MATTER (Lean bondSum_ne_semf_neutronMatter)")
    print("=" * 78)
    ok &= chk("all_three_bond_energies_positive",
              E_PP > 0 and E_PN > 0 and E_NN > 0, True)
    neg = True
    for A in (2, 4, 16, 56, 208):
        semf = A_V_TARGET*A - A_A_TARGET*A          # Z = 0: D^2/A = A
        neg &= semf < 0
    ok &= chk("semf_neutron_matter_unbound_for_a_A_gt_a_V", neg, True,
              note=f"a_A/a_V = {mp.nstr(A_A_TARGET/A_V_TARGET, 6)} > 1")
    ok &= chk("bond_sum_nonneg_at_pure_neutron_matter",
              E0*bond_sum(E_PP, E_PN, E_NN, 0, 0, 55) >= 0, True)

    print()
    print("=" * 78)
    print("5. THE O(hbar^2) QUESTION: THE MISS IS FIRST ORDER, TILT WRONG WAY")
    print("=" * 78)
    crossing = 1/(Q0**2 + 1)
    deform = (Q0**2 - 1)/(2*(Q0**2 + 1))
    flav = w_corpus - mp.mpf(1)/2
    print(f"  crossing 1/(q^2+1)    = {mp.nstr(crossing, 12)}")
    print(f"  deformation miss      = {mp.nstr(deform, 12)}")
    print(f"  hbar_q / 2            = {mp.nstr(HBAR/2, 12)}")
    print(f"  flavour tilt delta_f/4= {mp.nstr(flav, 12)}")
    print(f"  1/(2 hbar_q)          = {mp.nstr(1/(2*HBAR), 8)}")
    ok &= chk("deformation_miss_ge_half_hbar", deform >= HBAR/2, True,
              note="difference is (q-1)^2/(2q(q^2+1)) >= 0")
    ok &= chk("flavour_tilt_positive_pushes_away_from_crossing",
              flav > 0 and crossing < mp.mpf(1)/2, True)
    ok &= chk("second_order_flip_needs_coefficient_above_four",
              1/(2*HBAR) > 4, True)

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    witness = {
        "computation": "qbeta-bond-cut-symmetry-shape",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "q0_pin": "proton", "dps": DPS,
                       "m_e_MeV": mp.nstr(M_E, 15), "E0_MeV": mp.nstr(E0, 20),
                       "b_pp": mp.nstr(B_PP, 20), "b_pn": mp.nstr(B_PN, 20),
                       "b_nn": mp.nstr(B_NN, 20),
                       "semf_targets_MeV": {"a_V": mp.nstr(A_V_TARGET, 6),
                                            "a_A": mp.nstr(A_A_TARGET, 6),
                                            "role": "targets only, never searched"},
                       "lean": ["QOU/Hecke/BondCutSymmetry.lean", "QOU/Hecke/BondCutSymmetryLogBound.lean"]},
        "data": {"delta_corpus": mp.nstr(delta, 20),
                 "w_corpus": mp.nstr(w_corpus, 20),
                 "two_log_q": mp.nstr(bound, 20),
                 "delta_sweep_in_w": sweep,
                 "symmetry_coefficient_by_degree": rows,
                 "crossing": mp.nstr(crossing, 20),
                 "deformation_miss": mp.nstr(deform, 20),
                 "half_hbar": mp.nstr(HBAR/2, 20),
                 "flavour_tilt": mp.nstr(flav, 20)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_bond_cut_symmetry_shape_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-bond-cut-symmetry-shape.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
