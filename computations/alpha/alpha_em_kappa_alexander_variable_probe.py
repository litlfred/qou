#!/usr/bin/env python3
"""Which Alexander variable does the Seifert-pairing kappa use, and is it the corpus's?

Bean qou-gwio (alpha_em CS-tower structural residual), epic qou-myts brief C4.

Background.  The resummed Chern-Simons tower

    1/alpha_EM = bare * (1 + c1 / (1 - c1*kappa)),   bare = q[9]_q[10]_q,

misses CODATA by -467.6 ppb with the shipped Witten Gram ratio kappa_W = 1.7216
(proton pin).  `alpha_em_seifert_kappa_pairing_probe.py` replaced kappa by the
homological Seifert ratio on H_1(Sigma_4) = Z^8,

    kappa(u) = det(V29 - V29^T) det(V35 - V35^T)
               / ( det(V29 - u V29^T) det(V35 - u V35^T) )
             = 1 / ( u^8 * Delta_{T(2,9)}(u) * Delta_{T(3,5)}(u) ),

(Delta balanced, Delta(1) = 1), at the "horizontal Dirac scale" u = q^{-1}, and
got -24.53 ppb (proton pin) / +55.16 ppb (muon pin).  The variable u = q^{-1}
was stated, not derived.

What this probe tests (pre-registered here, before evaluation).  The Alexander
variable is not free in this corpus.  Convention D (owner ruling 2026-08-15) fixes
the Hecke generator by (T - q)(T + q^{-1}) = 0, so T/q has eigenvalues 1 and
-q^{-2}; the Burau representation (eigenvalues 1, -t) is therefore the Hecke
(n-1,1) representation at t = q^{-2} (or t = q^2 for the inverse orientation).
The corpus already uses exactly this variable for the force-carrier torus knot:
`QOU/StandardModel/AlphaEmT35Linchpin.lean` proves the closed form
Delta_{T(3,5)}(q^2) = (q - q^{-1})(q^15 - q^{-15}) / ((q^3 - q^{-3})(q^5 - q^{-5}))
and ties it to the bare factor [9]_q[10]_q.  The variable t = q^{+-1} would need
generator eigenvalues q^{1/2}, -q^{-1/2}: that is the excised convention C.

So the corpus-derived member of the Seifert family is u = q^{-2} (same
orientation as the existing probe, Burau variable of convention D).  Its closed
form, proved symbolically below, is

    kappa_D(q) = q^16 * [2]_q [9]_q [3]_q [5]_q / ( [18]_q [15]_q ),

using Delta_{T(p,r)}(q^2) = [pr]_q / ([p]_q [r]_q).

All four members u in {q^{-1}, q, q^{-2}, q^2} are evaluated and reported at both
registered pins; the verdict concerns u = q^{-2} only, whatever the others give.
No parameter is tuned.  CODATA enters only as the comparison at the end.

Precision: sympy exact for identities, mpmath 80 dps for numbers, no float64.

Run:  python3 -u computations/alpha/alpha_em_kappa_alexander_variable_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from mpmath import mpf

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402
from meson_em_sinh_closed_form import _alpha_em_inv_derived  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

B1 = 8  # b_1(Sigma_4) = 2g, g = 4


def seifert_chain(k: int) -> sp.Matrix:
    """(k-1)x(k-1) Seifert matrix of the (2,k)-type chain: 1 on diagonal, -1 above."""
    n = k - 1
    return sp.Matrix(n, n, lambda i, j: 1 if i == j else (-1 if j == i + 1 else 0))


def qint_sym(n: int, x):
    return (x**n - x**-n) / (x - 1 / x)


def qint(n: int, x: mpf) -> mpf:
    return (x**n - x**-n) / (x - 1 / x)


def delta29(t):
    return (t - 1 + 1 / t) * (t**3 - 1 + t**-3)


def delta35(t):
    return t**4 - t**3 + t - 1 + 1 / t - t**-3 + t**-4


def kappa_of_u(u):
    return 1 / (u**B1 * delta29(u) * delta35(u))


def fmt(x: mpf) -> str:
    return mp.nstr(x, 40)


def main() -> int:
    mp.mp.dps = 80

    # ---- Part 1: exact identities -------------------------------------
    u, q = sp.symbols("u q", positive=True)
    V29 = sp.kronecker_product(seifert_chain(2), seifert_chain(9))
    V35 = sp.kronecker_product(seifert_chain(3), seifert_chain(5))
    det_u = (V29 - u * V29.T).det() * (V35 - u * V35.T).det()
    det_1 = (V29 - V29.T).det() * (V35 - V35.T).det()
    id_family = sp.simplify(sp.cancel(det_1 / det_u - kappa_of_u(u)))
    assert id_family == 0, id_family

    # Delta_{T(p,r)}(q^2) = [pr]/([p][r])  (balanced, convention-D q-integers)
    id_d29 = sp.simplify(sp.cancel(delta29(q**2) - qint_sym(18, q) / (qint_sym(2, q) * qint_sym(9, q))))
    id_d35 = sp.simplify(sp.cancel(delta35(q**2) - qint_sym(15, q) / (qint_sym(3, q) * qint_sym(5, q))))
    assert id_d29 == 0 and id_d35 == 0, (id_d29, id_d35)
    kappa_D_closed = q**16 * qint_sym(2, q) * qint_sym(9, q) * qint_sym(3, q) * qint_sym(5, q) / (
        qint_sym(18, q) * qint_sym(15, q))
    id_kD = sp.simplify(sp.cancel(kappa_of_u(q**-2) - kappa_D_closed))
    assert id_kD == 0, id_kD

    # Convention D Hecke eigenvalues -> Burau variable
    T = sp.Symbol("T")
    roots = sp.solve((T - q) * (T + 1 / q), T)
    ratio = sp.simplify(min(roots, key=lambda r: sp.sign(r)) / max(roots, key=lambda r: sp.sign(r)))
    assert sp.simplify(ratio + q**-2) == 0, ratio  # eigenvalue ratio is -q^{-2}  =>  t = q^{-2}

    # ---- Part 2: numbers at both pins ----------------------------------
    entry = codata("inverse fine-structure constant")
    target = mpf(entry.value_str)
    sigma_ppb = mpf(entry.uncertainty_str) / target * mpf("1e9")

    pins = {"proton": mpf(Q_50_DIGIT_STR), "muon": q_muon_at(80)}
    members = {
        "u=q^-2 (convention D Burau; PRE-REGISTERED)": lambda x: x**-2,
        "u=q^-1 (existing Seifert probe; convention-C variable)": lambda x: 1 / x,
        "u=q": lambda x: x,
        "u=q^2": lambda x: x**2,
    }
    wb = WitnessBuilder("alpha-em-kappa-alexander-variable", engine="sympy")
    wb.set_content_block("rem:em-coupling-chern-simons")
    out = {}
    for pin, qv in pins.items():
        bare = qv * qint(9, qv) * qint(10, qv)
        c1 = mp.pi**2 * (mpf(10) / 9 + mpf(16) / 15) * (qint(2, qv) / 2) * (1 - 1 / qv) ** 2 / bare
        kreq = (1 - c1 / (target / bare - 1)) / c1
        witten = _alpha_em_inv_derived(qv)
        rows = {"witten_resummed_ppb": fmt((witten - target) / target * mpf("1e9")),
                "kappa_required_diagnostic": fmt(kreq)}
        print(f"\n{pin} pin q = {mp.nstr(qv, 20)}  (kappa needed {mp.nstr(kreq, 12)}; "
              f"Witten {mp.nstr((witten - target) / target * mpf('1e9'), 8)} ppb)")
        for name, uf in members.items():
            k = kappa_of_u(uf(qv))
            v = bare * (1 + c1 / (1 - c1 * k))
            ppb = (v - target) / target * mpf("1e9")
            rows[name] = {"kappa": fmt(k), "alpha_inv": fmt(v), "residual_ppb": fmt(ppb),
                          "residual_sigma": fmt(ppb / sigma_ppb)}
            print(f"  {name:55s} kappa={mp.nstr(k, 12):>16s}  {mp.nstr(ppb, 10):>14s} ppb")
        out[pin] = rows
        kD = kappa_of_u(qv**-2)
        kDc = qv**16 * qint(2, qv) * qint(9, qv) * qint(3, qv) * qint(5, qv) / (qint(18, qv) * qint(15, qv))
        assert abs(kD - kDc) < mpf("1e-70")

    wb.add_data("identities", {
        "kappa_family_det_identity": "0", "delta_T29_q2_eq_qint18_over_2_9": "0",
        "delta_T35_q2_eq_qint15_over_3_5": "0", "kappa_D_closed_form": "0",
        "convention_D_eigenvalue_ratio": "-q^-2",
    })
    wb.add_data("pins", out)
    wb.add_data("verdict", {
        "preregistered_member": "u = q^-2",
        "reading": "scope-limited negative (a): the convention-D Burau variable overshoots; "
                   "the -24.5 ppb Seifert figure needs u = q^-1, which convention D does not supply",
    })
    path = wb.save(q0_comparison(
        muon=mp.nstr(pins["muon"], 50), proton=Q_50_DIGIT_STR,
        reason="Seifert-pairing kappa evaluated at the Alexander variable fixed by convention D "
               "(u = q^-2) and at the three other members, both registered pins"))
    print(f"\nWitness written to: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
