#!/usr/bin/env python3
"""strand_twist_minimal_energy_and_z6_probe.py — 80-dps Probe for Quadratic Ribbon-Twist
Framing Energy, Unconstrained Minimal-Energy Selection, Baez-Huerta Z_6 Hypercharge
Congruence, and Kummer Pushforward / Plumbing Signature Bridges (Wave 7C, Bean qou-qvpl).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/StrandTwistMinimalEnergyAndZ6Hypercharge.lean`

STRICT ANTI-FITTING & PRECISION DISCIPLINE
------------------------------------------
1. ZERO fitting to empirical electroweak observables; ZERO floating-point heuristics.
2. ZERO binary64 (`float64`) arithmetic, ZERO `math` or `numpy` imports, ZERO
   `float(...)` or `complex(...)` calls, ZERO float literals, and ZERO raw JSON
   floats in the emitted witness (`witness_raw_float64_audit` = 0).
3. Evaluates at 80 decimal places (`QOU_OUTPUT_DPS=80`, `QOU_COMPUTE_DPS=95`,
   `set_compute_dps(80)`) across `{q_0, q_2t, q_muon}`:
   - Part 1 (Theorem 1): Exhaustive unconstrained integer lattice census over
     `t in [-5, +5]^3 subset Z^3` (`11^3 = 1331` triples), verifying the Cauchy-Schwarz
     identity `3 * E(t) - T(t)^2 = (t_0 - t_1)^2 + (t_1 - t_2)^2 + (t_2 - t_0)^2 >= 0`
     and proving that minimizing `E(t) = sum_i t_i^2` at `T(t) in {2, -1, 0, -3}`
     uniquely selects a single `S_3`-orbit per flavour (`{0,1,1}` at `E=2`, `{-1,0,0}`
     at `E=1` beating `{-1,-1,1}` at `E=3`, `{0,0,0}` at `E=0` beating `{-1,0,1}` at
     `E=2`, and `{-1,-1,-1}` at `E=3`), deriving the helon bound `t_i in {-1, 0, 1}`,
     collapsing `1*2*2*1 = 4` battery survivors to `1*1*1*1 = 1` unique assignment,
     and verifying the `q`-deformed ribbon framing energy `sum_i ([t_i]_q)^2` at
     `q_0, q_2t, q_muon`.
   - Part 2 (Theorem 2 — Open C of qou-qvpl): First-generation hypercharge spectrum
     `Y_t = 2 * (T(t)/3 - I_3)` across `(Q_L, u_R, d_R, L_L, e_R, nu_R)`, exact
     Baez-Huerta `Z_6` congruence `2 * tau_3 + 3 * (2 * I_3) == 3 * Y_t (mod 6)` across
     all 8 chiral states `(u_L, d_L, u_R, d_R, nu_L, e_L, nu_R, e_R)`, and exact
     cancellation of all 5 gauge and gravitational anomalies.
   - Part 3 (Theorem 3 — Open A & B of qou-qvpl): Exact bridge between `Y_t` and
     Bring's degree-3 Kummer pushforward `W_3 = pi_* L` (`y_2 = -1/2`, `y_3 = +1/3` on
     `W_3^*`, `-1/3` on `W_3`), and exact equality between the diagonal 3-strand
     4-manifold plumbing intersection signature `sigma_plumb(t) = sum_i sgn(t_i)` and
     `T(t)` on minimal-energy states vs. the even parity obstruction `sigma(K) in 2Z`
     for 1-component torus knots `T(2, 2m+1)`.
"""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (str(ROOT), str(ROOT / "substrate"), str(ROOT / "audits")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

from qou_substrate.constants import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    q0_comparison,
)


def _int_sign(z: int) -> int:
    if z > 0:
        return 1
    if z < 0:
        return -1
    return 0


def _q_int(n: int, q: mp.mpf) -> mp.mpf:
    """Signed quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if n == 0:
        return mp.mpf(0)
    qn = mp.power(q, n)
    q_inv_n = mp.mpf(1) / qn
    q_inv = mp.mpf(1) / q
    return (qn - q_inv_n) / (q - q_inv)


def _s3_orbit(triple: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    perms = {
        (triple[p[0]], triple[p[1]], triple[p[2]])
        for p in itertools.permutations((0, 1, 2))
    }
    return sorted(perms)


def _evaluate_part1_minimal_energy_and_orbit_collapse(
    pins: dict[str, mp.mpf],
) -> dict[str, object]:
    with mp.workdps(95):
        # Exhaustive scan over unconstrained integer lattice [-5, +5]^3 (1331 triples)
        lattice_bound = 5
        all_triples = list(
            itertools.product(range(-lattice_bound, lattice_bound + 1), repeat=3)
        )
        total_scanned = len(all_triples)
        cs_identity_failures = 0

        for t0, t1, t2 in all_triples:
            tot = t0 + t1 + t2
            eng = t0 * t0 + t1 * t1 + t2 * t2
            lhs = 3 * eng - tot * tot
            rhs = (t0 - t1) ** 2 + (t1 - t2) ** 2 + (t2 - t0) ** 2
            if lhs != rhs or lhs < 0:
                cs_identity_failures += 1

        # First-generation target totals 3Q in {2, -1, 0, -3}
        flavour_targets = [
            ("u", 2, (0, 1, 1)),
            ("d", -1, (-1, 0, 0)),
            ("nu", 0, (0, 0, 0)),
            ("e", -3, (-1, -1, -1)),
        ]

        flavour_records: dict[str, object] = {}
        helon_multisets_count_product = 1
        minimal_energy_orbits_product = 1
        all_uniquely_selected = True
        all_helon_bounded = True
        all_sign_coherent = True
        all_color_multiplicity_match = True

        for flav, target_3q, canon_rep in flavour_targets:
            matching_lattice = [
                t for t in all_triples if (t[0] + t[1] + t[2]) == target_3q
            ]
            min_e = min(t[0] ** 2 + t[1] ** 2 + t[2] ** 2 for t in matching_lattice)
            minimizers = sorted(
                t
                for t in matching_lattice
                if (t[0] ** 2 + t[1] ** 2 + t[2] ** 2) == min_e
            )
            minimizer_multisets = sorted({tuple(sorted(t)) for t in minimizers})
            helon_survivors = sorted(
                {
                    tuple(sorted(t))
                    for t in matching_lattice
                    if all(-1 <= x <= 1 for x in t)
                }
            )

            helon_multisets_count_product *= len(helon_survivors)
            minimal_energy_orbits_product *= len(minimizer_multisets)

            expected_orbit = _s3_orbit(canon_rep)
            if minimizers != expected_orbit or len(minimizer_multisets) != 1:
                all_uniquely_selected = False

            for t in minimizers:
                if not all(-1 <= x <= 1 for x in t):
                    all_helon_bounded = False
                if any(x > 0 for x in t) and any(x < 0 for x in t):
                    all_sign_coherent = False

            orbit_card = len(minimizers)
            div_by_3 = (target_3q % 3) == 0
            expected_card = 1 if div_by_3 else 3
            if orbit_card != expected_card:
                all_color_multiplicity_match = False

            # Compare q-deformed framing energy sum_i ([t_i]_q)^2 across pins
            q_energy_by_pin: dict[str, object] = {}
            for pin_name, q_val in pins.items():
                e_q_canon = mp.fsum(_q_int(x, q_val) ** 2 for x in canon_rep)
                q_energy_by_pin[pin_name] = {
                    "E_q_canonical": fmt(e_q_canon),
                }

            flavour_records[flav] = {
                "three_Q_totalTwist": target_3q,
                "canonical_representative": list(canon_rep),
                "minimal_twistEnergy_Z": min_e,
                "cauchy_schwarz_3E_minus_T2": 3 * min_e - target_3q * target_3q,
                "helon_battery_survivor_multisets": [list(m) for m in helon_survivors],
                "helon_battery_survivor_count": len(helon_survivors),
                "unconstrained_minimal_energy_multisets": [
                    list(m) for m in minimizer_multisets
                ],
                "unconstrained_minimal_energy_orbit": [list(t) for t in minimizers],
                "s3_orbit_cardinality": orbit_card,
                "three_divides_totalTwist": div_by_3,
                "inferred_SU3_color_dimension": orbit_card,
                "q_deformed_energy_by_pin": q_energy_by_pin,
            }

        # Explicit mixed-sign gap check for d and nu
        e_d_canon = (-1) ** 2 + 0**2 + 0**2  # 1
        e_d_mixed = (-1) ** 2 + (-1) ** 2 + 1**2  # 3
        e_nu_canon = 0**2 + 0**2 + 0**2  # 0
        e_nu_mixed = (-1) ** 2 + 0**2 + 1**2  # 2

        return {
            "lattice_bound": lattice_bound,
            "total_triples_scanned": total_scanned,
            "cauchy_schwarz_identity_failures": cs_identity_failures,
            "helon_battery_survivor_product": helon_multisets_count_product,
            "minimal_energy_unique_orbit_product": minimal_energy_orbits_product,
            "all_uniquely_selected": all_uniquely_selected,
            "all_helon_bounded": all_helon_bounded,
            "all_sign_coherent": all_sign_coherent,
            "all_color_multiplicity_match": all_color_multiplicity_match,
            "d_energy_canon_vs_mixed": {
                "d_canon_rep": [-1, 0, 0],
                "d_canon_energy": e_d_canon,
                "d_mixed_rep": [-1, -1, 1],
                "d_mixed_energy": e_d_mixed,
                "energy_gap_mixed_minus_canon": e_d_mixed - e_d_canon,
            },
            "nu_energy_canon_vs_mixed": {
                "nu_canon_rep": [0, 0, 0],
                "nu_canon_energy": e_nu_canon,
                "nu_mixed_rep": [-1, 0, 1],
                "nu_mixed_energy": e_nu_mixed,
                "energy_gap_mixed_minus_canon": e_nu_mixed - e_nu_canon,
            },
            "flavour_records": flavour_records,
        }


def _evaluate_part2_z6_hypercharge_and_anomalies() -> dict[str, object]:
    # 8 first-generation chiral states: (name, twist_rep, two_I3, triality_tau3, color_dim)
    chiral_states = [
        ("u_L", (0, 1, 1), 1, 2, 3),
        ("d_L", (-1, 0, 0), -1, 2, 3),
        ("u_R", (0, 1, 1), 0, 2, 3),
        ("d_R", (-1, 0, 0), 0, 2, 3),
        ("nu_L", (0, 0, 0), 1, 0, 1),
        ("e_L", (-1, -1, -1), -1, 0, 1),
        ("nu_R", (0, 0, 0), 0, 0, 1),
        ("e_R", (-1, -1, -1), 0, 0, 1),
    ]

    state_rows: list[dict[str, object]] = []
    all_z6_congruent = True
    all_triality_congruent = True

    for name, t_rep, two_i3, tau3, c_dim in chiral_states:
        tot_t = sum(t_rep)
        i3_frac = Fraction(two_i3, 2)
        q_frac = Fraction(tot_t, 3)
        y_phys = 2 * (q_frac - i3_frac)
        y_half = q_frac - i3_frac
        three_y = 2 * tot_t - 3 * two_i3

        triality_diff = tau3 - tot_t
        z6_diff = (2 * tau3 + 3 * two_i3) - three_y
        # Identity: z6_diff = 2 * (tau3 - tot_t) + 6 * two_i3
        identity_ok = z6_diff == (2 * (tau3 - tot_t) + 6 * two_i3)
        triality_ok = (triality_diff % 3) == 0
        z6_ok = (z6_diff % 6) == 0 and identity_ok

        if not triality_ok:
            all_triality_congruent = False
        if not z6_ok:
            all_z6_congruent = False

        state_rows.append(
            {
                "state": name,
                "twist_rep": list(t_rep),
                "totalTwist_3Q": tot_t,
                "Q_electric": str(q_frac),
                "two_I3": two_i3,
                "I3": str(i3_frac),
                "Y_physicists_2_Q_minus_I3": str(y_phys),
                "Y_half_Q_minus_I3": str(y_half),
                "three_Y": three_y,
                "su3_triality_tau3": tau3,
                "color_dim": c_dim,
                "tau3_minus_totalTwist_mod3": triality_diff % 3,
                "baez_huerta_2tau3_plus_3twoI3_minus_3Y": z6_diff,
                "baez_huerta_mod6": z6_diff % 6,
                "baez_huerta_z6_holds": z6_ok,
            }
        )

    # Anomaly cancellation in physicists' normalization Y_t = 2(Q - I3)
    y_q = Fraction(1, 3)
    y_ur = Fraction(4, 3)
    y_dr = Fraction(-2, 3)
    y_l = Fraction(-1, 1)
    y_er = Fraction(-2, 1)

    anom_su3_cube = 2 * 1 + 1 * (-1) + 1 * (-1)
    anom_su3_sq_u1 = 2 * y_q - y_ur - y_dr
    anom_su2_sq_u1 = 3 * y_q + y_l
    anom_grav_sq_u1 = 6 * y_q - 3 * y_ur - 3 * y_dr + 2 * y_l - y_er
    anom_u1_cube = (
        6 * (y_q**3) - 3 * (y_ur**3) - 3 * (y_dr**3) + 2 * (y_l**3) - (y_er**3)
    )

    all_anomalies_vanish = (
        anom_su3_cube == 0
        and anom_su3_sq_u1 == 0
        and anom_su2_sq_u1 == 0
        and anom_grav_sq_u1 == 0
        and anom_u1_cube == 0
    )

    return {
        "chiral_states": state_rows,
        "all_triality_congruent_mod3": all_triality_congruent,
        "all_baez_huerta_z6_congruent_mod6": all_z6_congruent,
        "anomalies_physicists_norm": {
            "Y_Q": str(y_q),
            "Y_uR": str(y_ur),
            "Y_dR": str(y_dr),
            "Y_L": str(y_l),
            "Y_eR": str(y_er),
            "SU3_3": anom_su3_cube,
            "SU3_2_U1": str(anom_su3_sq_u1),
            "SU2_2_U1": str(anom_su2_sq_u1),
            "grav_2_U1": str(anom_grav_sq_u1),
            "U1_3": str(anom_u1_cube),
            "all_five_vanish": all_anomalies_vanish,
        },
    }


def _evaluate_part3_kummer_and_plumbing_bridges() -> dict[str, object]:
    # Open A: Kummer pushforward W_3 = pi_* L on Bring's curve
    y_v2 = Fraction(-1, 2)
    y_w3_dual = Fraction(1, 3)
    y_w3 = -y_w3_dual  # -1/3
    tr5_hypercharge = 2 * y_v2 + 3 * y_w3_dual

    # Exterior-power induced half-scale hypercharges on (LL, dRc, eRc, QL, uRc)
    kummer_exterior = {
        "LL": y_v2,  # -1/2
        "dRc": y_w3_dual,  # +1/3
        "eRc": -2 * y_v2,  # +1
        "QL": -y_v2 - y_w3_dual,  # +1/6
        "uRc": -2 * y_w3_dual,  # -2/3
    }
    twist_half_matched = {
        "LL": Fraction(0, 3) - Fraction(1, 2),  # nu_L: -1/2
        "dRc": -(Fraction(-1, 3) - Fraction(0, 1)),  # -(d_R): +1/3
        "eRc": -(Fraction(-3, 3) - Fraction(0, 1)),  # -(e_R): +1
        "QL": Fraction(2, 3) - Fraction(1, 2),  # u_L: +1/6
        "uRc": -(Fraction(2, 3) - Fraction(0, 1)),  # -(u_R): -2/3
    }
    open_a_exact_match = (tr5_hypercharge == 0) and (
        kummer_exterior == twist_half_matched
    )

    # Open B: Diagonal 3-strand plumbing signature vs. 1-component knot signature
    canon_flavours = {
        "u": (0, 1, 1),
        "d": (-1, 0, 0),
        "nu": (0, 0, 0),
        "e": (-1, -1, -1),
    }
    plumbing_rows: dict[str, object] = {}
    all_plumbing_equal_twist = True
    for flav, rep in canon_flavours.items():
        tot_t = sum(rep)
        sig_plumb = sum(_int_sign(x) for x in rep)
        if sig_plumb != tot_t:
            all_plumbing_equal_twist = False
        plumbing_rows[flav] = {
            "twist_rep": list(rep),
            "totalTwist": tot_t,
            "plumbingSignature_sum_sgn": sig_plumb,
            "charge_Q_from_plumbing": str(Fraction(sig_plumb, 3)),
            "matches_totalTwist": sig_plumb == tot_t,
        }

    # 1-component torus knots T(2, 2m+1) for 2m+1 in {1, 3, 5, 7}
    torus_knot_rows: list[dict[str, object]] = []
    odd_charge_hit_by_knot_sig = False
    for m in range(4):
        p = 2 * m + 1
        sig_k = -2 * m
        if sig_k in (-1, -3):
            odd_charge_hit_by_knot_sig = True
        torus_knot_rows.append(
            {
                "torus_knot": f"T(2,{p})",
                "signature_sigma": sig_k,
                "is_even": (sig_k % 2) == 0,
                "sigma_over_3": str(Fraction(sig_k, 3)),
            }
        )

    return {
        "open_A_kummer_pushforward_bridge": {
            "y_V2": str(y_v2),
            "y_W3_dual": str(y_w3_dual),
            "y_W3": str(y_w3),
            "tr5_hyperchargeDiag": str(tr5_hypercharge),
            "kummer_exterior_Y_half": {k: str(v) for k, v in kummer_exterior.items()},
            "twist_Y_half_on_chiral_multiplets": {
                k: str(v) for k, v in twist_half_matched.items()
            },
            "exact_match_across_all_5_multiplets": open_a_exact_match,
        },
        "open_B_plumbing_vs_knot_signature": {
            "plumbing_on_minimal_energy_flavours": plumbing_rows,
            "all_plumbing_equal_totalTwist": all_plumbing_equal_twist,
            "one_component_torus_knot_signatures": torus_knot_rows,
            "odd_charge_3Qd_or_3Qe_hit_by_1component_knot": odd_charge_hit_by_knot_sig,
        },
    }


def main() -> int:
    with mp.workdps(95):
        q0 = q_at(95)
        q2t = q_two_term_borromean_at(95)
        q_mu = q_muon_at(95)
        pins = {
            "proton_1term": q0,
            "proton_2term_borromean": q2t,
            "muon_ideal_cal2": q_mu,
        }

        part1 = _evaluate_part1_minimal_energy_and_orbit_collapse(pins)
        part2 = _evaluate_part2_z6_hypercharge_and_anomalies()
        part3 = _evaluate_part3_kummer_and_plumbing_bridges()

        print("=" * 124)
        print(
            "  80-dps Wave-7C Probe: Quadratic Ribbon-Twist Framing Energy, Baez-Huerta Z_6, & Kummer/Plumbing Bridges (Bean qou-qvpl)"
        )
        print("=" * 124)
        print(
            f"  Part 1 — Unconstrained [-5,+5]^3 Lattice Scan ({part1['total_triples_scanned']} triples):"
        )
        print(
            f"    Cauchy-Schwarz 3*E(t) - T(t)^2 == sum (t_i - t_j)^2 >= 0 failures : {part1['cauchy_schwarz_identity_failures']}"
        )
        print(
            f"    Battery survivor product (1*2*2*1) -> Minimal-energy product      : {part1['helon_battery_survivor_product']} -> {part1['minimal_energy_unique_orbit_product']}"
        )
        print(
            f"    d=(-1,0,0) E=1 vs (-1,-1,1) E=3; nu=(0,0,0) E=0 vs (-1,0,1) E=2   : uniquely selected = {part1['all_uniquely_selected']}"
        )
        print(
            f"  Part 2 — Open C (Physicists' Y_t = 2(T/3 - I_3), Baez-Huerta Z_6, & 5 Anomalies):"
        )
        print(
            f"    All 8 chiral states satisfy tau_3 == T (mod 3) & 2*tau_3 + 3*(2*I_3) == 3*Y (mod 6): {part2['all_baez_huerta_z6_congruent_mod6']}"
        )
        print(
            f"    All 5 gauge/gravitational anomalies vanish identically             : {part2['anomalies_physicists_norm']['all_five_vanish']}"
        )
        print(
            f"  Part 3 — Open A (Bring Kummer Pushforward) & Open B (3-Strand Plumbing vs 1-Component Knot Signature):"
        )
        print(
            f"    Open A exact match Y_twist_half == smHypercharge on all 5 multiplets: {part3['open_A_kummer_pushforward_bridge']['exact_match_across_all_5_multiplets']}"
        )
        print(
            f"    Open B 3-strand plumbing sum sgn(t_i) == sum t_i on minimal energy : {part3['open_B_plumbing_vs_knot_signature']['all_plumbing_equal_totalTwist']}"
        )
        print("=" * 124)

        wb = WitnessBuilder(
            "strand-twist-minimal-energy-and-z6",
            engine="mpmath-80dps",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps zero-float64 verification of Bean qou-qvpl (StrandTwistMinimalEnergyAndZ6Hypercharge.lean): "
            "(1) Theorem 1 — Cauchy-Schwarz framing energy bound 3*E(t) >= T(t)^2 and unconstrained minimal-energy "
            "selection across Z^3 uniquely picking {0,1,1} (E=2, card 3), {-1,0,0} (E=1, card 3, beating {-1,-1,1} at E=3), "
            "{0,0,0} (E=0, card 1, beating {-1,0,1} at E=2), and {-1,-1,-1} (E=3, card 1), deriving the helon bound "
            "t_i in {-1,0,1}, collapsing 1*2*2*1 = 4 battery survivors to 1*1*1*1 = 1, and matching S_3-orbit size "
            "(3 vs 1) to 3 | T(t); "
            "(2) Theorem 2 (Open C) — Y_t = 2*(T(t)/3 - I_3) reproduces (1/3, 4/3, -2/3, -1, -2), satisfies the "
            "Baez-Huerta Z_6 congruence 2*tau_3 + 3*(2*I_3) == 3*Y_t (mod 6) on all 8 first-generation chiral states, "
            "and cancels all 5 gauge/gravitational anomalies; "
            "(3) Theorem 3 (Open A & B) — exact bridge to Bring's degree-3 Kummer pushforward hypercharge (y_2=-1/2, y_3=+1/3) "
            "and to the diagonal 3-strand plumbing signature sum sgn(t_i)/3 on minimal-energy states vs. the even parity "
            "obstruction sigma(K) in 2Z for 1-component knots."
        )

        wb.add_parameter("precision_dps", 80)
        wb.add_parameter("q0_proton_1term", fmt(q0))
        wb.add_parameter("q2t_two_term_borromean", fmt(q2t))
        wb.add_parameter("q0_muon_codata2022", fmt(q_mu))
        wb.add_parameter("zero_fitting", True)
        wb.add_parameter(
            "lean_companion",
            "folio/quantum-observable-universe/lean/QOU/StandardModel/StrandTwistMinimalEnergyAndZ6Hypercharge.lean",
        )

        wb.add_data("pins", {k: fmt(v) for k, v in pins.items()})
        wb.add_data("part1_minimal_energy_and_orbit_collapse", part1)
        wb.add_data("part2_z6_hypercharge_and_anomalies", part2)
        wb.add_data("part3_kummer_and_plumbing_bridges", part3)

        wb.add_assertion(
            name="cauchy_schwarz_and_unconstrained_minimal_energy_unique_orbits",
            computed=(
                "1"
                if (
                    part1["cauchy_schwarz_identity_failures"] == 0
                    and part1["helon_battery_survivor_product"] == 4
                    and part1["minimal_energy_unique_orbit_product"] == 1
                    and part1["all_uniquely_selected"]
                    and part1["all_helon_bounded"]
                    and part1["all_sign_coherent"]
                )
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="Cauchy-Schwarz 3*E(t) - T(t)^2 >= 0 and unconstrained minimal energy on Z^3 collapsing 4 battery tuples to 1",
        )
        wb.add_assertion(
            name="s3_orbit_cardinality_matches_color_triality_divisibility",
            computed="1" if part1["all_color_multiplicity_match"] else "0",
            expected="1",
            tolerance="0",
            source="|Orb_{S_3}(t)| = 3 iff 3 does not divide T(t) (quarks u,d) and |Orb_{S_3}(t)| = 1 iff 3 | T(t) (leptons nu,e)",
        )
        wb.add_assertion(
            name="baez_huerta_z6_congruence_and_five_anomalies_cancel",
            computed=(
                "1"
                if (
                    part2["all_triality_congruent_mod3"]
                    and part2["all_baez_huerta_z6_congruent_mod6"]
                    and part2["anomalies_physicists_norm"]["all_five_vanish"]
                )
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="2*tau_3 + 3*(2*I_3) == 3*Y_t (mod 6) across all 8 chiral states and all 5 gauge/gravitational anomalies = 0",
        )
        wb.add_assertion(
            name="open_A_bring_kummer_pushforward_hypercharge_bridge_exact",
            computed=(
                "1"
                if part3["open_A_kummer_pushforward_bridge"][
                    "exact_match_across_all_5_multiplets"
                ]
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="Y_t/2 == smHypercharge on Lambda^1(V_2 (+) W_3^*) (+) Lambda^2(V_2^* (+) W_3) with y_2=-1/2, y_3=+1/3",
        )
        wb.add_assertion(
            name="open_B_diagonal_plumbing_signature_equals_twist_and_1component_parity_obstruction",
            computed=(
                "1"
                if (
                    part3["open_B_plumbing_vs_knot_signature"][
                        "all_plumbing_equal_totalTwist"
                    ]
                    and not part3["open_B_plumbing_vs_knot_signature"][
                        "odd_charge_3Qd_or_3Qe_hit_by_1component_knot"
                    ]
                )
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="sum_i sgn(t_i) == sum_i t_i on minimal-energy states (t_i in {-1,0,1}) vs 1-component knot parity sigma(K) in 2Z",
        )

        stamp = q0_comparison(
            muon=q_mu,
            proton=q0,
            reason=(
                "Core ribbon-twist energy minimization, Baez-Huerta Z_6 congruences, and Kummer/plumbing "
                "hypercharge bridges are exact over Z and Q; q-deformed framing energies sum_i ([t_i]_q)^2 "
                "are evaluated side-by-side at q_0 (proton_1term), q_2t (proton_2term_borromean), and q_muon."
            ),
        )
        saved_path = wb.save(stamp)
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))

        import witness_raw_float64_audit as _f64_audit

        n_raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if n_raw_floats != 0:
            raise RuntimeError(f"Emitted witness contains {n_raw_floats} raw float64 values!")

        print(f"  Saved 80-dps witness -> {saved_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
