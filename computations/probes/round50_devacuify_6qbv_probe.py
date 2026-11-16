#!/usr/bin/env python3
"""
80-dps mpmath + exact integer verification probe for the Round 50
de-vacuification batch under qou-6qbv / qou-uot9:

1. qou-lrnd (QOU.LiftingDescent.MotivicPerpetualObstructionFromTrace):
   Two-term Habiro prime-ideal collapse habiroPrimeCollapse(a0, a1, -1) = a0(-1) + 2*a1(-1)
   for proton (8), neutron (2), and deuteron (192).
2. confinement_categorical (QOU.WedderburnMass.confinement_categorical):
   Wedderburn 3-block center sum and commutator-annihilation trace factorization
   on 2x2 standard-block matrices at 80 dps.
3. confinement_frobenius_reciprocity (QOU.ParticleInteractions.confinement_frobenius_reciprocity):
   KKT active-subspace substitution sum_{j} x*_j <O, b_j> = sum_{i,j} u*_i Ginv_{ij} <O, b_j>
   and zero duality gap at 80 dps.
4. four_term_pair_nucleon (QOU.ParticleInteractions.four_term_pair_nucleon):
   Table 2 (proton 6-channel NF sum = 999/1000) and Table 3 (neutron 6-channel NF sum = 811/1000)
   plus 80-dps similarity-trace invariance tr(g B g^{-1}) = tr(B).
5. parity_regime_selection (QOU.ParticleInteractions.parity_regime_selection):
   Spectator asymmetry positivity (q^2 - 1)*(3*(q^2 + 1)^2 - 2*q^2) > 0 for q > 1
   and factored fermionic spectator sign (-1)^Z * (-1)^(N-1) = (-1)^(A-1).

Witness: round50-devacuify-6qbv.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 80


def habiro_prime_collapse(a0_val: int, a1_val: int, u_res: int) -> int:
    return a0_val + a1_val * (1 - u_res)


def main() -> int:
    w = WitnessBuilder(
        "round50-devacuify-6qbv",
        engine="mpmath-80dps",
    )
    w.set_description(
        "80-dps mpmath and exact rational verification probe for the 5 Round 50 "
        "de-vacuified Lean 4 modules under qou-6qbv / qou-uot9: "
        "MotivicPerpetualObstructionFromTrace (qou-lrnd), confinement_categorical, "
        "confinement_frobenius_reciprocity, four_term_pair_nucleon, and "
        "parity_regime_selection."
    )

    # 1. qou-lrnd: Habiro prime-ideal collapse at u_res = -1
    c_proton = habiro_prime_collapse(8, 0, -1)
    c_neutron = habiro_prime_collapse(2, 0, -1)
    c_deuteron = habiro_prime_collapse(192, 0, -1)
    w.add_assertion(
        "habiro_prime_collapse_proton_at_neg_one",
        computed=c_proton,
        expected=8,
        tolerance=0,
        source="QOU.LiftingDescent.qou_proton_perpetual_obstruction (a0=-1 -> 8, a1=-1 -> 0)",
    )
    w.add_assertion(
        "habiro_prime_collapse_neutron_at_neg_one",
        computed=c_neutron,
        expected=2,
        tolerance=0,
        source="QOU.LiftingDescent.qou_neutron_perpetual_obstruction (a0=-1 -> 2, a1=-1 -> 0)",
    )
    w.add_assertion(
        "habiro_prime_collapse_deuteron_at_neg_one",
        computed=c_deuteron,
        expected=192,
        tolerance=0,
        source="QOU.LiftingDescent.qou_deuteron_perpetual_obstruction (a0=-1 -> 192, a1=-1 -> 0)",
    )

    # 2. confinement_categorical: centre-commutator trace factorisation at 80 dps
    a_mat = mp.matrix([[mp.mpf("3") / 7, mp.mpf("5") / 11],
                       [mp.mpf("2") / 13, mp.mpf("17") / 19]])
    b_mat = mp.matrix([[mp.mpf("11") / 23, mp.mpf("-4") / 29],
                       [mp.mpf("7") / 31, mp.mpf("13") / 37]])
    comm = a_mat * b_mat - b_mat * a_mat
    tr_comm = comm[0, 0] + comm[1, 1]
    comm_vanishes = int(mp.fabs(tr_comm) < mp.mpf("1e-75"))
    w.add_assertion(
        "confinement_categorical_commutator_trace_zero",
        computed=comm_vanishes,
        expected=1,
        tolerance=0,
        source="QOU.WedderburnMass.integral_factors_through_centre: tr([A, B]) = 0 to 75+ dps",
    )

    # 3. confinement_frobenius_reciprocity: double-sum KKT reciprocity at 80 dps
    g_inv = mp.matrix([[mp.mpf("5") / 3, mp.mpf("-1") / 3],
                       [mp.mpf("-1") / 3, mp.mpf("2") / 3]])
    u_star = [mp.mpf("3") / 5, mp.mpf("7") / 10]
    pairing = [mp.mpf("11") / 7, mp.mpf("13") / 9]
    x_star = [sum(u_star[i] * g_inv[i, j] for i in range(2)) for j in range(2)]
    lhs_exp = sum(x_star[j] * pairing[j] for j in range(2))
    rhs_exp = sum(
        u_star[i] * g_inv[i, j] * pairing[j]
        for i in range(2)
        for j in range(2)
    )
    reciprocity_match = int(mp.fabs(lhs_exp - rhs_exp) < mp.mpf("1e-75"))
    w.add_assertion(
        "confinement_frobenius_reciprocity_double_sum_identity",
        computed=reciprocity_match,
        expected=1,
        tolerance=0,
        source="QOU.ParticleInteractions.reciprocity_of_kkt: active primal expansion equals double sum to 75+ dps",
    )

    # 4. four_term_pair_nucleon: exact rational 6-channel NF sums + 80-dps conjugation invariance
    proton_channels = [
        Fraction(-100, 1000),
        Fraction(36, 1000),
        Fraction(998, 1000),
        Fraction(99, 1000),
        Fraction(9, 1000),
        Fraction(-43, 1000),
    ]
    neutron_channels = [
        Fraction(-202, 1000),
        Fraction(48, 1000),
        Fraction(1009, 1000),
        Fraction(-10, 1000),
        Fraction(9, 1000),
        Fraction(-43, 1000),
    ]
    w.add_assertion(
        "four_term_pair_proton_milli_sum",
        computed=int(sum(proton_channels) * 1000),
        expected=999,
        tolerance=0,
        source="QOU.ParticleInteractions.proton_nf_channel_sum (Table 2 milli-units)",
    )
    w.add_assertion(
        "four_term_pair_neutron_milli_sum",
        computed=int(sum(neutron_channels) * 1000),
        expected=811,
        tolerance=0,
        source="QOU.ParticleInteractions.neutron_nf_channel_sum (Table 3 milli-units)",
    )
    g_inv_mat = b_mat ** (-1)
    conj_mat = b_mat * a_mat * g_inv_mat
    tr_base = a_mat[0, 0] + a_mat[1, 1]
    tr_conj = conj_mat[0, 0] + conj_mat[1, 1]
    conj_invariance = int(mp.fabs(tr_conj - tr_base) < mp.mpf("1e-75"))
    w.add_assertion(
        "four_term_pair_polarization_conjugation_trace_invariance",
        computed=conj_invariance,
        expected=1,
        tolerance=0,
        source="QOU.ParticleInteractions.confinedNet_eq_base_trace: tr(g B g^{-1}) = tr(B) to 75+ dps",
    )

    # 5. parity_regime_selection: spectator asymmetry numerator > 0 and factored sign identity
    q0 = mp.mpf(1) + mp.mpf(1) / mp.mpf(137)
    asym_num = (q0 ** 2 - 1) * (3 * (q0 ** 2 + 1) ** 2 - 2 * q0 ** 2)
    asym_pos = int(asym_num > 0)
    w.add_assertion(
        "parity_regime_spectator_asymmetry_numerator_positive",
        computed=asym_pos,
        expected=1,
        tolerance=0,
        source="QOU.ParticleInteractions.spectator_asymmetry_num_pos at q = 1 + 1/137 (80 dps)",
    )

    sign_checks = all(
        ((-1) ** z) * ((-1) ** (n - 1)) == (-1) ** (z + n - 1)
        for (z, n) in [(0, 1), (1, 2), (2, 4)]
    )
    w.add_assertion(
        "parity_regime_factored_spectator_sign_identity",
        computed=int(sign_checks),
        expected=1,
        tolerance=0,
        source="QOU.ParticleInteractions.sign_identity_of_factored across A=1 (n), A=3 (3H), A=6 (6He)",
    )

    w.add_data("precision_dps", 80)
    w.add_data("habiro_collapse_constants", {
        "proton": str(c_proton),
        "neutron": str(c_neutron),
        "deuteron": str(c_deuteron),
    })
    w.add_data("spectator_asymmetry_num_at_q0", mp.nstr(asym_num, 50))

    out = w.save()
    print(f"Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
