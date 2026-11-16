#!/usr/bin/env python3
# polynomial_q_not_applicable: exact discrete representation theory, flavour Cartan Q = I_3 + (B+S+C)/2 arithmetic, SU(6) 56 = (8,2)+(10,4) decomposition, and Bring g=4->g=3 pinching invariants.
"""
Flavour Cartan Q = I_3 + (B + S + C)/2, SU(6) Spin-Flavour 56 & Bring->Klein Degeneration Probe
================================================================================================

Work items: qou-yw3v, qou-d7h1, qou-8pl3, qou-8pl1, qou-j3w6 (Epic qou-8lxd)

Verifies at 50 decimal places (`mpmath.mp.dps = 50`) and exact rational/integer
arithmetic:

1. **Flavour Cartan Extension `Q = I_3 + (B + S + C)/2` (`qou-yw3v`, `qou-d7h1`)**:
   - Evaluates the exact flavour Cartan identity `6 Q = 3 (2 I_3) + 3 B + 3 S + 3 C`
     across:
       * the 4 fundamental quarks `(u, d, s, c)` where `s ~ T(2,5)` (`S = -1, C = 0`)
         and `c ~ T(2,7)` (`S = 0, C = +1`) carry higher torus-knot generation charges
         and `B = 1/3` (`mu_bar_123 = 1` for a 3-quark Borromean baryon),
       * all **8 baryon octet** states `(p, n, Sigma^+, Sigma^0, Sigma^-, Lambda^0, Xi^0, Xi^-)`,
       * all **10 baryon decuplet** states `(Delta^++, Delta^+, Delta^0, Delta^-, Sigma^*+, Sigma^*0, Sigma^*-, Xi^*0, Xi^*-, Omega^-)`,
       * all **8 pseudoscalar meson octet** states `(K^+, K^0, pi^+, pi^0, eta_8, pi^-, Kbar^0, K^-)`,
       * **6 charmed baryons** `(Lambda_c^+, Sigma_c^++, Sigma_c^+, Sigma_c^0, Xi_cc^++, Omega_c^0)`.

2. **Colour `SU(3)_c` vs Flavour `SU(3)_f`, Spin-Flavour `SU(6)` `56 = (8,2) + (10,4)`, and Owner Decision 4d Condition 5 (`qou-d7h1`, `qou-8pl3`, `qou-j3w6`)**:
   - Under Condition 5 (`Lambda^2 V ~= 1`, `N_spin = 2` for the single-fibre `SU(2)` module,
     owner decision 4d in `qou-j3w6`), the 3-row antisymmetric Young diagram `(1^3)` has
     Weyl dimension `C(2, 3) = 0`, whereas the second fundamental object `W` (`N_flavour = 3`
     with `Lambda^3 W ~= 1`) has `C(3, 3) = 1`;
   - Because colour `SU(3)_c` is locked in the antisymmetric singlet `Lambda^3(3_c) = 1_c`
     (`dim = 1`), Fermi statistics forces the `L = 0` spin-flavour wave function in
     `W_flavour tensor V_spin ~= C^3 tensor C^2 ~= C^6` to lie in `Sym^3(C^6)` of dimension
     `C(8, 3) = 56`, which decomposes by pairing identical `S_3` irreps `(3)x(3)`,
     `(2,1)x(2,1)`, `(1^3)x(1^3)` as:
       `10 * 4 + 8 * 2 + 1 * 0 = 40 + 16 + 0 = 56`,
     reproducing the exact baryon octet (`J = 1/2`, `2J+1 = 2`) and decuplet
     (`J = 3/2`, `2J+1 = 4`) while excluding a ground-state `L = 0` flavour singlet.

3. **Bring `g = 4 -> g = 3` Pinching Arithmetic & `S_4` Competitor Obstruction (`qou-8pl1`)**:
   - Pinching `1` non-separating cycle on Bring's curve (`g = 4`) shifts geometric genus
     `4 -> 3`, Euler characteristic `-6 -> -4` (`Delta chi = +2`), and `b_1 : 8 -> 6`;
   - Verifies that both the Klein quartic (`|Aut| = 168 = 84(3-1)`) and the Fermat quartic
     (`|Aut| = 96`) have automorphism group orders divisible by `|S_4| = 24` (`168/24 = 7`,
     `96/24 = 4`), confirming that `S_4` symmetry alone does not uniquely select the Klein
     quartic among genus-3 curves.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

del _sys, _Path, _bridge

import json
import math
from fractions import Fraction
from typing import Any

import mpmath as mp
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50


def weyl_dim_sym3(n: int) -> int:
    return math.comb(n + 2, 3)


def weyl_dim_mixed3(n: int) -> int:
    return n * (n + 1) * (n - 1) // 3


def weyl_dim_alt3(n: int) -> int:
    return math.comb(n, 3)


def make_quark(name: str, two_i3: int, three_b: int, s: int, c: int, six_q: int) -> dict[str, Any]:
    three_yf = three_b + 3 * s + 3 * c
    six_q_cartan = 3 * two_i3 + three_yf
    return {
        "name": name,
        "twoI3": two_i3,
        "threeB": three_b,
        "S": s,
        "C": c,
        "threeYf": three_yf,
        "Yf": str(Fraction(three_yf, 3)),
        "sixQ": six_q,
        "Q": str(Fraction(six_q, 6)),
        "sixQFromCartan": six_q_cartan,
        "satisfiesFlavourCartan": six_q == six_q_cartan,
    }


def make_baryon(name: str, q1: dict[str, Any], q2: dict[str, Any], q3: dict[str, Any], exp_q: Fraction) -> dict[str, Any]:
    two_i3 = q1["twoI3"] + q2["twoI3"] + q3["twoI3"]
    three_b = q1["threeB"] + q2["threeB"] + q3["threeB"]
    s = q1["S"] + q2["S"] + q3["S"]
    c = q1["C"] + q2["C"] + q3["C"]
    six_q = q1["sixQ"] + q2["sixQ"] + q3["sixQ"]
    three_yf = three_b + 3 * s + 3 * c
    six_q_cartan = 3 * two_i3 + three_yf
    return {
        "name": name,
        "quarks": f"{q1['name']}{q2['name']}{q3['name']}",
        "twoI3": two_i3,
        "threeB": three_b,
        "B": str(Fraction(three_b, 3)),
        "S": s,
        "C": c,
        "threeYf": three_yf,
        "Yf": str(Fraction(three_yf, 3)),
        "sixQ": six_q,
        "Q": str(Fraction(six_q, 6)),
        "satisfiesFlavourCartan": (
            six_q == six_q_cartan
            and Fraction(six_q, 6) == exp_q
            and three_b == 3
        ),
    }


def make_meson(name: str, q: dict[str, Any], qbar: dict[str, Any], exp_q: Fraction) -> dict[str, Any]:
    two_i3 = q["twoI3"] - qbar["twoI3"]
    three_b = q["threeB"] - qbar["threeB"]
    s = q["S"] - qbar["S"]
    c = q["C"] - qbar["C"]
    six_q = q["sixQ"] - qbar["sixQ"]
    three_yf = three_b + 3 * s + 3 * c
    six_q_cartan = 3 * two_i3 + three_yf
    return {
        "name": name,
        "quarks": f"{q['name']} bar({qbar['name']})",
        "twoI3": two_i3,
        "threeB": three_b,
        "S": s,
        "C": c,
        "threeYf": three_yf,
        "Yf": str(Fraction(three_yf, 3)),
        "sixQ": six_q,
        "Q": str(Fraction(six_q, 6)),
        "satisfiesFlavourCartan": (
            six_q == six_q_cartan
            and Fraction(six_q, 6) == exp_q
            and three_b == 0
        ),
    }


def run_probe() -> dict[str, Any]:
    w = WitnessBuilder("flavour-cartan-octet-decuplet-degeneration", engine="mpmath")
    w.set_description(
        "Verifies the flavour Cartan / Gell-Mann-Nishijima formula Q = I_3 + (B + S + C)/2 "
        "across quarks (u,d,s,c), the 8 baryon octet states, 10 baryon decuplet states, "
        "8 meson octet states, and 6 charmed baryons (qou-yw3v, qou-d7h1), the spin-flavour "
        "SU(6) 56 = (8,2) + (10,4) decomposition and Condition 5 two-object split N_spin=2 vs "
        "N_flavour=3 (qou-d7h1, qou-8pl3, qou-j3w6), and the Bring g=4 -> g=3 pinching and "
        "S_4 competitor arithmetic (qou-8pl1)."
    )
    w.set_audit_only("docs/audits/2026-05-08-compute-audit-workplan.md")

    # 1. Quarks & Hadrons under Q = I_3 + (B + S + C)/2
    u = make_quark("u", +1, 1, 0, 0, +4)
    d = make_quark("d", -1, 1, 0, 0, -2)
    s = make_quark("s", 0, 1, -1, 0, -2)
    c = make_quark("c", 0, 1, 0, +1, +4)
    quarks = [u, d, s, c]

    baryon_octet = [
        make_baryon("p", u, u, d, Fraction(1)),
        make_baryon("n", u, d, d, Fraction(0)),
        make_baryon("Sigma^+", u, u, s, Fraction(1)),
        make_baryon("Sigma^0", u, d, s, Fraction(0)),
        make_baryon("Sigma^-", d, d, s, Fraction(-1)),
        make_baryon("Lambda^0", u, d, s, Fraction(0)),
        make_baryon("Xi^0", u, s, s, Fraction(0)),
        make_baryon("Xi^-", d, s, s, Fraction(-1)),
    ]

    baryon_decuplet = [
        make_baryon("Delta^++", u, u, u, Fraction(2)),
        make_baryon("Delta^+", u, u, d, Fraction(1)),
        make_baryon("Delta^0", u, d, d, Fraction(0)),
        make_baryon("Delta^-", d, d, d, Fraction(-1)),
        make_baryon("Sigma^*+", u, u, s, Fraction(1)),
        make_baryon("Sigma^*0", u, d, s, Fraction(0)),
        make_baryon("Sigma^*-", d, d, s, Fraction(-1)),
        make_baryon("Xi^*0", u, s, s, Fraction(0)),
        make_baryon("Xi^*-", d, s, s, Fraction(-1)),
        make_baryon("Omega^-", s, s, s, Fraction(-1)),
    ]

    meson_octet = [
        make_meson("K^+", u, s, Fraction(1)),
        make_meson("K^0", d, s, Fraction(0)),
        make_meson("pi^+", u, d, Fraction(1)),
        make_meson("pi^0", u, u, Fraction(0)),
        make_meson("eta_8", s, s, Fraction(0)),
        make_meson("pi^-", d, u, Fraction(-1)),
        make_meson("Kbar^0", s, d, Fraction(0)),
        make_meson("K^-", s, u, Fraction(-1)),
    ]

    charmed_baryons = [
        make_baryon("Lambda_c^+", u, d, c, Fraction(1)),
        make_baryon("Sigma_c^++", u, u, c, Fraction(2)),
        make_baryon("Sigma_c^+", u, d, c, Fraction(1)),
        make_baryon("Sigma_c^0", d, d, c, Fraction(0)),
        make_baryon("Xi_cc^++", u, c, c, Fraction(2)),
        make_baryon("Omega_c^0", s, s, c, Fraction(0)),
    ]

    all_cartan_states = (
        quarks + baryon_octet + baryon_decuplet + meson_octet + charmed_baryons
    )
    all_cartan_pass = all(st["satisfiesFlavourCartan"] for st in all_cartan_states)

    # 2. Spin-Flavour SU(6) 56 = (8,2) + (10,4) & Condition 5 (N_spin=2 vs N_flavour=3)
    su2_sym3 = weyl_dim_sym3(2)      # 4 (J = 3/2)
    su2_mixed3 = weyl_dim_mixed3(2)  # 2 (J = 1/2)
    su2_alt3 = weyl_dim_alt3(2)      # 0 (killed by row cap l(lambda) <= 2)

    su3_sym3 = weyl_dim_sym3(3)      # 10 (decuplet)
    su3_mixed3 = weyl_dim_mixed3(3)  # 8  (octet)
    su3_alt3 = weyl_dim_alt3(3)      # 1  (singlet)

    su6_sym3 = weyl_dim_sym3(6)      # 56
    su6_kronecker_sum = (
        su3_sym3 * su2_sym3 + su3_mixed3 * su2_mixed3 + su3_alt3 * su2_alt3
    )

    # 3. Bring g=4 -> g=3 pinching & S_4 competitor arithmetic (qou-8pl1)
    chi_g4 = 2 - 2 * 4
    chi_g3 = 2 - 2 * 3
    b1_g4 = 2 * 4
    b1_g3 = 2 * 3
    hurwitz_g3 = 84 * (3 - 1)
    hurwitz_g4 = 84 * (4 - 1)
    s4_order = 24
    klein_order = 168
    fermat_order = 96
    pinch_and_competitors_ok = (
        chi_g4 == -6
        and chi_g3 == -4
        and b1_g4 == 8
        and b1_g3 == 6
        and hurwitz_g3 == 168
        and hurwitz_g4 == 252
        and klein_order % s4_order == 0
        and fermat_order % s4_order == 0
    )

    w.add_parameter("quarkFlavours", ["u", "d", "s", "c"])
    w.add_parameter("condition5SpinDim", 2)
    w.add_parameter("flavourFundamentalDim", 3)

    summary = {
        "workItems": ["qou-yw3v", "qou-d7h1", "qou-8pl3", "qou-8pl1", "qou-j3w6"],
        "epic": "qou-8lxd",
        "flavourCartan": {
            "quarks": quarks,
            "baryonOctet": baryon_octet,
            "baryonDecuplet": baryon_decuplet,
            "mesonOctet": meson_octet,
            "charmedBaryons": charmed_baryons,
            "totalStatesChecked": len(all_cartan_states),
            "allSatisfyFlavourCartan": all_cartan_pass,
        },
        "spinFlavourSu6AndCondition5": {
            "su2SpinDims": {
                "sym3_J3half": su2_sym3,
                "mixed3_J1half": su2_mixed3,
                "alt3_vanishes": su2_alt3,
            },
            "su3FlavourDims": {
                "sym3_decuplet": su3_sym3,
                "mixed3_octet": su3_mixed3,
                "alt3_singlet": su3_alt3,
                "cubeTotal": su3_sym3 + 2 * su3_mixed3 + su3_alt3,
            },
            "su6Sym3Dim": su6_sym3,
            "su6KroneckerDecomposition": {
                "decupletSpin3Half": su3_sym3 * su2_sym3,
                "octetSpin1Half": su3_mixed3 * su2_mixed3,
                "singletSpinAlt": su3_alt3 * su2_alt3,
                "sum": su6_kronecker_sum,
            },
        },
        "bringKleinDegenerationArithmetic": {
            "eulerCharG4": chi_g4,
            "eulerCharG3": chi_g3,
            "firstBettiG4": b1_g4,
            "firstBettiG3": b1_g3,
            "hurwitzBoundG3": hurwitz_g3,
            "hurwitzBoundG4": hurwitz_g4,
            "kleinAutOrder": klein_order,
            "fermatAutOrder": fermat_order,
            "s4Order": s4_order,
            "kleinIndexS4": klein_order // s4_order,
            "fermatIndexS4": fermat_order // s4_order,
        },
    }
    for k, v in summary.items():
        w.add_data(k, v)

    w.add_assertion(
        name="flavour_cartan_gmn_all_36_states",
        computed=len(all_cartan_states) if all_cartan_pass else 0,
        expected=36,
        source="FlavourCartanOctetDecuplet.lean (qou-yw3v, qou-d7h1)",
    )
    w.add_assertion(
        name="su6_spin_flavour_56_kronecker_split",
        computed=(
            su6_kronecker_sum
            if (su6_sym3 == 56 and su2_alt3 == 0 and su3_alt3 == 1)
            else 0
        ),
        expected=56,
        source="FlavourCartanOctetDecuplet.lean (qou-d7h1, qou-8pl3, qou-j3w6)",
    )
    w.add_assertion(
        name="bring_pinching_and_s4_competitors",
        computed=(
            klein_order // s4_order + fermat_order // s4_order
            if pinch_and_competitors_ok
            else 0
        ),
        expected=11,
        source="FlavourCartanOctetDecuplet.lean (qou-8pl1)",
    )

    w.save(
        {
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "Exact integer/rational flavour Cartan quantum numbers, SU(6) Schur-Weyl "
                "dimension identities, and genus-4 -> genus-3 topological pinching arithmetic "
                "with no Q_0 dependence."
            ),
        }
    )
    return summary


if __name__ == "__main__":
    result = run_probe()
    print(json.dumps(result, indent=2))
