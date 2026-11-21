#!/usr/bin/env python3
"""crossing_covariant_qed_probe.py — numerical companion to
`QOU.BraidsAndKnots.CrossingCovariantQED` (owner-authorised front, option 4, 2026-11-20).

Evaluates, at the proton-pinned q₀ and 70 dps, every quantity the Lean file derives:

  * the first-order variation of tr(V³), V³ = (σ₁σ₂⁻¹)³ on the proton (2,1) weight space,
    under the strand-labelled crossing insertion σ^e ↦ σ^e(1 + ε·e·Q_aQ_b·Y), for
      - Y = 1                (the covariant scalar insertion: colored writhe),
      - Y = Z                (the global commutant element; also covariant),
      - Y = Q₁₂ / Q₂₃        (the fixed-position insertion; NOT covariant — comparison only);
  * the Hopf control σ₁² (colored writhe nonzero);
  * the classification of first-order covariant insertions inside the full crossing commutant
    (exact rational arithmetic at q = 2: solution space = span{1, Z} per label pair);
  * the derived scale c_em = α_em(q₀)·E₀_tower, with α_em from the dashboard's
    `alpha_em_inv_derived` — CONDITIONAL on the open Witten-κ Gram-determinant `sorry`;
  * M_p^QED and Δm_QED = M_n^QED − M_p^QED from this operator.

No quantity is chosen against a target. The μ–p gap (0.2288 keV, two-term arc) is printed only
as a comparison point. The even three-body term c₃·Q₁Q₂Q₃·μ̄² has an underived c₃; this probe
prints the value c₃/c_em would have to take to reach the gap, as a DIAGNOSTIC, and adopts none.

Run:  python3 -u computations/crossing_covariant_qed_probe.py
"""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent
sys.path.insert(0, str(COMPUTE_DIR))
sys.path.insert(0, str(COMPUTE_DIR / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

mp.mp.dps = 70

from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402

MU_P_GAP_KEV = mp.mpf("0.2288")  # comparison point only (two-term arc, PR #8549/#8554)


# --------------------------------------------------------------------------------------------
# Exact 3×3 matrix helpers over any number type (mpf or Fraction)
# --------------------------------------------------------------------------------------------
def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]


def msc(c, A):
    return [[c * A[i][j] for j in range(3)] for i in range(3)]


def eye(one, zero):
    return [[one if i == j else zero for j in range(3)] for i in range(3)]


def tr(A):
    return A[0][0] + A[1][1] + A[2][2]


def gens(q, one, zero):
    qi = one / q
    h = q - qi
    A1 = [[q, zero, zero], [zero, zero, one], [zero, one, h]]
    A2 = [[zero, one, zero], [one, h, zero], [zero, zero, q]]
    A1i = [[qi, zero, zero], [zero, -h, one], [zero, one, zero]]
    A2i = [[-h, one, zero], [one, zero, zero], [zero, zero, qi]]
    return {(0, 1): A1, (1, 1): A2, (0, -1): A1i, (1, -1): A2i}


def swap(pos, i):
    p = list(pos)
    p[i], p[i + 1] = p[i + 1], p[i]
    return p


BOR = [(0, 1), (1, -1), (0, 1), (1, -1), (0, 1), (1, -1)]
HOPF = [(0, 1), (0, 1)]
PROTON_Q = [Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)]
NEUTRON_Q = [Fraction(2, 3), Fraction(-1, 3), Fraction(-1, 3)]


def first_order(word, G, charges, Ymaker, one, zero):
    """Exact ε-coefficient of tr Π σ^e(1+ε e Q_aQ_b Y): Leibniz sum over letters."""
    labels = [0, 1, 2]
    pairs = []
    for (i, e) in word:
        pairs.append((labels[i], labels[i + 1]))
        labels = swap(labels, i)
    total = zero
    for k in range(len(word)):
        M = eye(one, zero)
        for j, (i, e) in enumerate(word):
            M = mmul(M, G[(i, e)])
            if j == k:
                a, b = pairs[k]
                c = e * charges[a] * charges[b]
                c = one * c.numerator / c.denominator if isinstance(one, mp.mpf) else c
                Y = Ymaker(i)
                # σ⁻¹ ↦ (1 − εY)σ⁻¹ = σ⁻¹(1 − εY) since every Y used here commutes with its
                # own crossing (scalar, central Z, and Q12/Q23 locally), so σ^e·(e·c·Y) covers both.
                M = mmul(M, msc(c, Y))
        total += tr(M)
    return total, pairs


def colored_writhe(word, charges):
    labels = [0, 1, 2]
    s = Fraction(0)
    for (i, e) in word:
        a, b = labels[i], labels[i + 1]
        s += e * charges[a] * charges[b]
        labels = swap(labels, i)
    return s


def commutant_classification():
    """Exact rational: dim of the first-order covariant insertions inside the crossing
    commutants, at q = 2. Returns (unknowns, solution_dim, nonscalar_is_global_commutant)."""
    import sympy as sp

    q = sp.Rational(2)
    h = q - 1 / q
    A = [sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]]), sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])]

    def cbasis(X):
        syms = sp.symbols("m0:9")
        M = sp.Matrix(3, 3, syms)
        sol = sp.solve(list(M * X - X * M), syms, dict=True)[0]
        Mg = M.subs(sol)
        free = sorted(Mg.free_symbols, key=str)
        return [Mg.subs({f: (1 if f == g else 0) for f in free}) for g in free]

    CB = [cbasis(X) for X in A]
    vars_ = {}

    def Y(i, a, b):
        key = (i, tuple(sorted((a, b))))
        if key not in vars_:
            vars_[key] = sp.symbols(f"c_{i}_{key[1][0]}{key[1][1]}_0:{len(CB[i])}")
        return sum((c * B for c, B in zip(vars_[key], CB[i])), sp.zeros(3))

    eqs = []
    for (a, b, c) in itertools.permutations(range(3)):
        L = A[0] * Y(0, a, b) * A[1] * A[0] + A[0] * A[1] * Y(1, a, c) * A[0] + A[0] * A[1] * A[0] * Y(0, b, c)
        R = A[1] * Y(1, b, c) * A[0] * A[1] + A[1] * A[0] * Y(0, a, c) * A[1] + A[1] * A[0] * A[1] * Y(1, a, b)
        eqs += list(sp.expand(L - R))
    allv = [v for vs in vars_.values() for v in vs]
    Mx = sp.Matrix([[sp.diff(e, v) for v in allv] for e in eqs])
    ns = Mx.nullspace()
    glob = True
    for v in ns:
        sol = dict(zip(allv, v))
        for key, vs in vars_.items():
            Mm = sum((sol[c] * B for c, B in zip(vs, CB[key[0]])), sp.zeros(3))
            if (Mm * A[0] - A[0] * Mm) != sp.zeros(3) or (Mm * A[1] - A[1] * Mm) != sp.zeros(3):
                glob = False
    return len(allv), len(ns), glob, [len(c) for c in CB]


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    one, zero = mp.mpf(1), mp.mpf(0)
    G = gens(q0, one, zero)
    I3 = eye(one, zero)
    qi = 1 / q0
    # global commutant element Z (= sibling NucleonQEDCovariance.M)
    Z = [[-q0 + qi ** 3, qi ** 2, qi], [qi ** 2, -q0 + qi, one], [qi, one, zero]]
    for X in (G[(0, 1)], G[(1, 1)]):
        d = madd(mmul(Z, X), msc(-1, mmul(X, Z)))
        assert max(abs(x) for r in d for x in r) < mp.mpf("1e-60"), "Z not central"
    Q12 = [[mp.mpf(4) / 9, 0, 0], [0, mp.mpf(-2) / 9, 0], [0, 0, mp.mpf(-2) / 9]]
    Q23 = [[mp.mpf(-2) / 9, 0, 0], [0, mp.mpf(-2) / 9, 0], [0, 0, mp.mpf(4) / 9]]

    trV3 = tr(mmul(mmul(mmul(G[(0, 1)], G[(1, -1)]), mmul(G[(0, 1)], G[(1, -1)])),
                   mmul(G[(0, 1)], G[(1, -1)])))
    rows = {}
    for name, ch in (("proton", PROTON_Q), ("neutron", NEUTRON_Q)):
        d_scalar, pairs = first_order(BOR, G, ch, lambda i: I3, one, zero)
        d_Z, _ = first_order(BOR, G, ch, lambda i: Z, one, zero)
        d_pos, _ = first_order(BOR, G, ch, lambda i: Q12 if i == 0 else Q23, one, zero)
        rows[name] = {
            "label_pairs_along_V3": pairs,
            "colored_writhe_exact": str(colored_writhe(BOR, ch)),
            "dtr_scalar": d_scalar,
            "dtr_globalZ": d_Z,
            "dtr_fixed_position_NONCOVARIANT": d_pos,
        }
    hopf_cw = colored_writhe(HOPF, PROTON_Q)

    alpha_inv = alpha_em_inv_derived(q0)
    alpha = 1 / alpha_inv
    m_e = mp.mpf(str(M_E_MEV))
    E0_order0 = m_e / (q0 * (q0 - 1))
    hbar = (q0 - 1) / q0
    E0_tower = E0_order0 / (1 - hbar ** 2)
    c_em_keV = alpha * E0_tower * 1000
    # energies: c_em × (first-order coefficient of the normalised trace) for the covariant ops
    Mp = c_em_keV * rows["proton"]["dtr_scalar"] / trV3
    Mn = c_em_keV * rows["neutron"]["dtr_scalar"] / trV3
    MpZ = c_em_keV * rows["proton"]["dtr_globalZ"] / trV3
    MnZ = c_em_keV * rows["neutron"]["dtr_globalZ"] / trV3
    # even three-body diagnostic (NOT adopted): E3 = kappa * c_em * Q1Q2Q3 * mubar^2, mubar^2 = 1
    kappa_needed = MU_P_GAP_KEV / (c_em_keV * mp.mpf(4) / 27)

    nunk, ndim, glob, cdims = commutant_classification()

    print("=" * 78)
    print("crossing_covariant_qed_probe — 70 dps, proton q0 =", mp.nstr(q0, 20))
    print(f"tr(V3) on (2,1)                      = {mp.nstr(trV3, 25)}")
    for k, r in rows.items():
        print(f"[{k}] colored writhe (exact)         = {r['colored_writhe_exact']}")
        print(f"[{k}] d tr/dε, scalar insertion      = {mp.nstr(r['dtr_scalar'], 10)}")
        print(f"[{k}] d tr/dε, global-commutant Z    = {mp.nstr(r['dtr_globalZ'], 10)}")
        print(f"[{k}] d tr/dε, fixed-position (NOT covariant, comparison) = "
              f"{mp.nstr(r['dtr_fixed_position_NONCOVARIANT'], 20)}")
    print(f"Hopf control: colored writhe (proton labels) = {hopf_cw}  (nonzero ⇒ construction live)")
    print(f"commutant classification at q=2: commutant dims {cdims}, unknowns {nunk}, "
          f"covariant solution dim {ndim} (= 3 pairs × span{{1,Z}}), all non-scalar central: {glob}")
    print(f"alpha_em^-1 (derived, CONDITIONAL on Witten-κ sorry) = {mp.nstr(alpha_inv, 20)}")
    print(f"E0_tower = {mp.nstr(E0_tower, 20)} MeV ;  c_em = α_em·E0_tower = {mp.nstr(c_em_keV, 20)} keV")
    print(f"M_p^QED (covariant, 1st order) = {mp.nstr(Mp, 10)} keV ; with Z: {mp.nstr(MpZ, 10)} keV")
    print(f"Δm_QED = M_n − M_p             = {mp.nstr(Mn - Mp, 10)} keV ; with Z: {mp.nstr(MnZ - MpZ, 10)} keV")
    print(f"comparison point: μ–p gap      = {MU_P_GAP_KEV} keV  → NOT reached (operator gives 0)")
    print(f"DIAGNOSTIC (not adopted): even term c3=κ·c_em would need κ = {mp.nstr(kappa_needed, 12)}")
    print("=" * 78)

    tol = mp.mpf("1e-55")
    checks = {
        "scalar_firstorder_zero_proton": abs(rows["proton"]["dtr_scalar"]) < tol,
        "scalar_firstorder_zero_neutron": abs(rows["neutron"]["dtr_scalar"]) < tol,
        "globalZ_firstorder_zero_proton": abs(rows["proton"]["dtr_globalZ"]) < tol,
        "globalZ_firstorder_zero_neutron": abs(rows["neutron"]["dtr_globalZ"]) < tol,
        "colored_writhe_exact_zero": all(r["colored_writhe_exact"] == "0" for r in rows.values()),
        "hopf_control_nonzero": hopf_cw != 0,
        "commutant_solutions_are_central": glob and ndim == 6,
    }
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")

    out = {
        "schema": "witness/v1-lite",
        "producer": "computations/crossing_covariant_qed_probe.py",
        "lean": "QOU.BraidsAndKnots.CrossingCovariantQED",
        "q0Anchor": "proton",
        "q0": fmt(q0, 50),
        "dps": 70,
        "trace_V3_proton_weight_space": fmt(trV3, 50),
        "first_order": {
            k: {
                "colored_writhe_exact": r["colored_writhe_exact"],
                "dtr_scalar": fmt(r["dtr_scalar"], 50),
                "dtr_globalZ": fmt(r["dtr_globalZ"], 50),
                "dtr_fixed_position_NONCOVARIANT": fmt(r["dtr_fixed_position_NONCOVARIANT"], 50),
            } for k, r in rows.items()
        },
        "hopf_control_colored_writhe": str(hopf_cw),
        "commutant_classification_q2": {"commutant_dims": cdims, "unknowns": nunk,
                                        "solution_dim": ndim, "nonscalar_solutions_central": glob},
        "alpha_em_inv_derived": fmt(alpha_inv, 40),
        "alpha_em_status": "conditional on the Witten-kappa Gram-determinant sorry",
        "E0_tower_MeV": fmt(E0_tower, 40),
        "c_em_keV": fmt(c_em_keV, 40),
        "M_p_QED_keV": fmt(Mp, 40),
        "Delta_m_QED_keV": fmt(Mn - Mp, 40),
        "comparison_mu_p_gap_keV": str(MU_P_GAP_KEV),
        "diagnostic_even_term_kappa_needed_NOT_ADOPTED": fmt(kappa_needed, 30),
        "checks": checks,
    }
    (COMPUTE_DIR / "crossing-covariant-qed.witness.json").write_text(json.dumps(out, indent=2) + "\n")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
