#!/usr/bin/env python3
"""teraplectic_z_inadmissibility_80dps_probe.py — 80-dps verification for qou-7y1z.

Certifies at `compute_dps = 95`, `output_dps = 80` (zero float64, canonical
proton pin `q_at(95)`) that the teraplectic / inverse-solved candidate value
`z_teraplectic = 0.99850030` (and the exact affine base root `z*` solving
`|h^2/2 - z*h| * E_0 = Q_beta^CODATA`) is NOT an admissible Markov trace
parameter under the two-row Convention-D framework (`ConventionDAdmissibleRoots`
in Lean):

  1. The unique roots of the 3-row Ocneanu weight `y_{(1^3)}(z) = 0` at `q_0 > 1`
     are `z = q_0` (trivial 1-row augmentation, `y_{(2,1)}(q_0) = 0`) and
     `z_D = q_0^3 / (q_0^2 + 1)` (canonical two-row Temperley-Lieb trace).
  2. `z_teraplectic = 0.99850030` equals neither admissible root:
       |z_teraplectic - q_0| = 0.11147828... > 0.11
       |z_teraplectic - z_D| = 0.38581242... > 0.38
  3. Because `z_teraplectic` lies strictly inside the open interval `(z_D, q_0)`,
     its 3-row Ocneanu weight at `H_3(q_0)` is strictly negative:
       y_{(1^3)}(z_teraplectic) = -0.014130696... < 0,
     violating Markov-trace weight positivity as well as the two-row cap.

Ref: docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md §2b
Ref: docs/audits/2026-11-24-teraplectic-z-inadmissibility-qou-7y1z.md
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_OUTPUT_DPS", "80")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "qbeta"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
)
import qbeta_e0 as _qbeta_e0  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def ocneanu_weights_h3(q: mp.mpf, z: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Exact Ocneanu Markov weights `(y_(3), y_(2,1), y_(1^3))` on `H_3(q)`."""
    q2 = q * q
    q4 = q2 * q2
    cyc3 = q4 + q2 + mp.mpf(1)
    y_111 = q2 * (z - q) * ((q2 + mp.mpf(1)) * z - q2 * q) / ((q2 + mp.mpf(1)) * cyc3)
    y_21 = -q2 * (z - q) * (z + mp.mpf(1) / q) / cyc3
    y_3 = mp.mpf(1) - mp.mpf(2) * y_21 - y_111
    return y_3, y_21, y_111


def main() -> int:
    set_compute_dps()
    with mp.workdps(95):
        q0 = q_at(95)
        qi = mp.mpf(1) / q0
        h0 = q0 - qi
        q2 = q0 * q0
        z_d = (q2 * q0) / (q2 + mp.mpf(1))

        # witness-copy-intentional: 8-digit teraplectic z candidate named in bean qou-7y1z under falsification test.
        z_tera = mp.mpf("0.99850030")

        me = mp.mpf(str(M_E_MEV))
        mp_exp = mp.mpf(str(M_P_MEV_VALIDATION))
        mn_exp = mp.mpf(str(M_N_MEV_VALIDATION))
        q_beta_exp = mn_exp - mp_exp - me

        e0_ord0 = _qbeta_e0.order_zero(q0, me)
        e0_canon = _qbeta_e0.canonical(q0, me)

        # Solve |h^2/2 - z*h| * E_0 = Q_beta^CODATA on the z > h/2 branch:
        # z* = h/2 + (Q_beta^CODATA / E_0) / h
        z_star_ord0 = h0 / mp.mpf(2) + (q_beta_exp / e0_ord0) / h0
        z_star_canon = h0 / mp.mpf(2) + (q_beta_exp / e0_canon) / h0

        y3_t, y21_t, y111_t = ocneanu_weights_h3(q0, z_tera)
        y3_d, y21_d, y111_d = ocneanu_weights_h3(q0, z_d)
        y3_q, y21_q, y111_q = ocneanu_weights_h3(q0, q0)
        _, _, y111_star_ord0 = ocneanu_weights_h3(q0, z_star_ord0)
        _, _, y111_star_canon = ocneanu_weights_h3(q0, z_star_canon)

        # Verify defining Markov moments at z_tera:
        mom0_err = abs((y3_t + mp.mpf(2) * y21_t + y111_t) - mp.mpf(1))
        mom1_err = abs((q0 * y3_t + h0 * y21_t - qi * y111_t) - z_tera)
        mom2_err = abs((q2 * y3_t - y21_t + qi * qi * y111_t) - z_tera * z_tera)
        max_mom_err = max(mom0_err, mom1_err, mom2_err)

        dist_to_q0 = abs(z_tera - q0)
        dist_to_zd = abs(z_tera - z_d)
        two_row_vanishing_err = max(abs(y111_d), abs(y111_q))

        w = WitnessBuilder("teraplectic-z-inadmissibility-80dps", engine="python+mpmath")
        w.set_description(
            "80-dps verification for bean qou-7y1z: teraplectic z = 0.99850030 "
            "(and exact inverse-solved z* on the Delta_S base) lies strictly in "
            "(z_D, q_0), equals neither admissible two-row Markov root {q_0, z_D}, "
            "and forces a strictly negative 3-row Ocneanu weight y_{(1^3)}(z) < 0."
        )
        w.add_parameter("q0", fmt(q0))
        w.add_parameter("z_D", fmt(z_d))
        w.add_parameter("z_teraplectic", fmt(z_tera))

        w.add_data("admissible_two_row_roots", {
            "z_augmentation_q0": fmt(q0),
            "z_D_two_row": fmt(z_d),
            "y_111_at_z_D": fmt(y111_d),
            "y_111_at_q0": fmt(y111_q),
        })
        w.add_data("teraplectic_evaluation", {
            "z_teraplectic": fmt(z_tera),
            "abs_diff_from_q0": fmt(dist_to_q0),
            "abs_diff_from_z_D": fmt(dist_to_zd),
            "strictly_between_z_D_and_q0": bool(z_d < z_tera < q0),
            "y_3": fmt(y3_t),
            "y_21": fmt(y21_t),
            "y_111": fmt(y111_t),
            "max_markov_moment_error": fmt(max_mom_err),
        })
        w.add_data("inverse_solved_z_star_comparison", {
            "Q_beta_CODATA_MeV": fmt(q_beta_exp),
            "z_star_order_zero_E0": fmt(z_star_ord0),
            "y_111_at_z_star_order_zero": fmt(y111_star_ord0),
            "z_star_canonical_tower_E0": fmt(z_star_canon),
            "y_111_at_z_star_canonical_tower": fmt(y111_star_canon),
        })

        w.add_assertion(
            "ocneanu_weights_satisfy_h3_markov_moments_to_1e_85",
            computed=max_mom_err,
            expected=mp.mpf(0),
            tolerance=mp.mpf("1e-85"),
            source="sum f^lam y_lam = 1, sum y_lam chi^lam(sigma_1) = z, sum y_lam chi^lam(sigma_1 sigma_2) = z^2",
        )
        w.add_assertion(
            "two_row_roots_annihilate_y_111_to_1e_85",
            computed=two_row_vanishing_err,
            expected=mp.mpf(0),
            tolerance=mp.mpf("1e-85"),
            source="ConventionDAdmissibleRoots: y_{(1^3)}(z) = 0 iff z in {q_0, q_0^3/(q_0^2+1)}",
        )
        w.add_assertion(
            "teraplectic_z_separated_from_q0_by_gt_0_11",
            computed=bool(dist_to_q0 > mp.mpf("0.11")),
            expected=True,
            source="|0.99850030 - q_0| = 0.11147828... != 0",
        )
        w.add_assertion(
            "teraplectic_z_separated_from_z_D_by_gt_0_38",
            computed=bool(dist_to_zd > mp.mpf("0.38")),
            expected=True,
            source="|0.99850030 - z_D| = 0.38581242... != 0",
        )
        w.add_assertion(
            "teraplectic_z_forces_strictly_negative_three_row_weight",
            computed=bool(y111_t < mp.mpf("-0.014") and y111_star_ord0 < mp.mpf("-0.014") and y111_star_canon < mp.mpf("-0.014")),
            expected=True,
            source="y_{(1^3)}(z) < 0 for all z in (z_D, q_0); at z = 0.99850030, y_{(1^3)} = -0.014130696...",
        )

        w.save({
            "q0Anchor": "proton",
            "q0AnchorReason": "Evaluates admissible Convention-D Markov roots {q_0, q_0^3/(q_0^2+1)} at the canonical proton substrate pin q_at(95).",
            "q0Value": fmt(q0),
        })
        print(f"q0            = {mp.nstr(q0, 25)}")
        print(f"z_D           = {mp.nstr(z_d, 25)}")
        print(f"z_teraplectic = {mp.nstr(z_tera, 25)}")
        print(f"|z - q0|      = {mp.nstr(dist_to_q0, 20)}")
        print(f"|z - z_D|     = {mp.nstr(dist_to_zd, 20)}")
        print(f"y_(1^3)(z)    = {mp.nstr(y111_t, 20)} (< 0 => inadmissible)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
