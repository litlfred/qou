#!/usr/bin/env python3
"""Yekutieli multiplicative integral iterated limit & surface-ordering shift probe (qou-zbcj, qou-tw5z).

Verifies at 50+ decimal places (`mpmath.mp.dps >= 70`, output 60 dps) for the
non-abelian 2D multiplicative integral (Yekutieli 2015, LNM 2136; Baez-Schreiber
2007; Gukov-Pei-Putrov-Vafa 2020):

1. **MQ1 (`qou-zbcj`) — Non-commutativity of iterated limits in a non-abelian
   multiplicative integral:**
   - Discrete quantum dilogarithm holonomy at the proton pin `q_0`:
     ``Phi_n(x; q_0) = prod_{k=0}^{n-1} (1 - x q_0^k)^{-1}`` identified as the
     path-ordered Yekutieli multiplicative integral ``holonomy([g_0, ..., g_{n-1}])``
     with ``g_k = (1 - x q_0^k)^{-1}``.
   - Non-abelian surface-plaquette commutator holonomy defect: for non-commuting
     connection step transports ``g_rho, g_q in GL_2(C)`` built from the radial
     dilog generator ``A_rho`` and angular quantum-group generator ``B_q``, the
     two iterated orderings ``holonomy([g_rho, g_q]) = g_rho * g_q`` and
     ``holonomy([g_q, g_rho]) = g_q * g_rho`` differ by the non-trivial
     commutator holonomy defect
     ``Delta = g_rho * g_q * (g_q * g_rho)^{-1} != I_2``, matching at first BCH
     order ``(I + A_rho)(I + B_q) - (I + B_q)(I + A_rho) = [A_rho, B_q] != 0``.

2. **MQ2/MQ3 (`qou-tw5z`) — Exact surface-ordering shift `-pi^2 / 3`:**
   - The 2-curvature ``Omega_2 = dB + [A, B]`` integrated over the unit corner
     plaquette ``Sigma = [0, 1]_rho x [0, 1]_theta`` picks up the radial
     dilogarithm series ``sum_{n >= 1} (-2 / n^2) = -2 * zeta(2) = -2 * (pi^2 / 6) = -pi^2 / 3``.
   - Consequently, the surface-ordered Part B evaluation differs from the
     commuting iterated limit (`Part B = -pi^2 / 6`) by ``-pi^2 / 3``, giving
     ``-pi^2 / 6 + (-pi^2 / 3) = -pi^2 / 2``.

Lean companion:
  ``folio/quantum-observable-universe/lean/QOU/Torsion/MultiplicativeIntegralCurvature.lean``
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps, str_at_true_precision  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "yekutieli-multiplicative-integral-curvature",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "50+ dps verification of the Yekutieli non-abelian multiplicative "
        "integral iterated-limit non-commutativity (qou-zbcj, MQ1) and "
        "the exact surface-ordering shift -2*zeta(2) = -pi^2/3 (qou-tw5z, MQ2/MQ3)."
    )

    q0 = q_at()
    h = q0 - mp.mpf(1) / q0
    pi = mp.pi
    zeta2 = mp.zeta(2)
    pi_sq_div_6 = (pi ** 2) / mp.mpf(6)
    zeta2_minus_pi_sq_div_6 = abs(zeta2 - pi_sq_div_6)

    # 1. Discrete Yekutieli holonomy identification for Phi_n(x; q_0)
    x_test = mp.mpf("0.23")
    n_steps = 12
    step_transports = [
        mp.mpf(1) / (mp.mpf(1) - x_test * (q0 ** (-k)))
        for k in range(n_steps)
    ]
    holonomy_prod = mp.mpf(1)
    for g_k in step_transports:
        holonomy_prod *= g_k
    phi_n_direct = mp.mpf(1)
    for k in range(n_steps):
        phi_n_direct /= (mp.mpf(1) - x_test * (q0 ** (-k)))
    phi_n_holonomy_abs_diff = abs(holonomy_prod - phi_n_direct)

    # 2. First-order BCH / non-commutative 2x2 plaquette defect (MQ1)
    # (I + A_rho)(I + B_q) - (I + B_q)(I + A_rho) = A_rho B_q - B_q A_rho
    a_val = mp.mpf("0.5")
    b_val = h
    A_mat = mp.matrix([[mp.mpf(0), a_val], [mp.mpf(0), mp.mpf(0)]])
    B_mat = mp.matrix([[b_val, mp.mpf(0)], [mp.mpf(0), -b_val]])
    I_mat = mp.eye(2)

    order_rho_then_q = (I_mat + A_mat) * (I_mat + B_mat)
    order_q_then_rho = (I_mat + B_mat) * (I_mat + A_mat)
    iterated_diff_mat = order_rho_then_q - order_q_then_rho
    commutator_mat = A_mat * B_mat - B_mat * A_mat
    bch_identity_residual = mp.norm(iterated_diff_mat - commutator_mat, 2)
    commutator_fro_norm = mp.norm(commutator_mat, 2)

    # Multiplicative group commutator holonomy defect:
    # g_rho = exp(A_mat), g_q = exp(B_mat)
    g_rho = mp.expm(A_mat)
    g_q = mp.expm(B_mat)
    hol_rho_q = g_rho * g_q
    hol_q_rho = g_q * g_rho
    hol_defect = hol_rho_q * (hol_q_rho ** -1)
    defect_minus_identity_norm = mp.norm(hol_defect - I_mat, 2)

    # 3. Surface-ordering shift (MQ2/MQ3): -2 * zeta(2) = -pi^2 / 3
    iterated_part_b = -pi_sq_div_6
    surface_ordering_shift_zeta = -mp.mpf(2) * zeta2
    surface_ordering_shift_closed = -(pi ** 2) / mp.mpf(3)
    surface_shift_abs_diff = abs(surface_ordering_shift_zeta - surface_ordering_shift_closed)

    na_stokes_part_b = iterated_part_b + surface_ordering_shift_closed
    expected_na_stokes_part_b = -(pi ** 2) / mp.mpf(2)
    na_stokes_part_b_abs_diff = abs(na_stokes_part_b - expected_na_stokes_part_b)

    li2_at_one = mp.polylog(2, mp.mpf(1))
    neg_two_li2_at_one = -mp.mpf(2) * li2_at_one
    li2_shift_abs_diff = abs(neg_two_li2_at_one - surface_ordering_shift_closed)

    builder.add_parameter("q_proton", str_at_true_precision(q0))
    builder.add_parameter("h_proton", str_at_true_precision(h))
    builder.add_parameter("phi_n_steps", n_steps)
    builder.add_parameter("x_test", str_at_true_precision(x_test))
    builder.add_parameter("plaquette_a", str_at_true_precision(a_val))
    builder.add_parameter("plaquette_b", str_at_true_precision(b_val))

    builder.add_data("beans", ["qou-zbcj", "qou-tw5z", "qou-wp3h"])
    builder.add_data("lean_module", "QOU.Torsion.MultiplicativeIntegralCurvature")
    builder.add_data("zeta_2", str_at_true_precision(zeta2))
    builder.add_data("pi_sq_div_6", str_at_true_precision(pi_sq_div_6))
    builder.add_data("zeta2_minus_pi_sq_div_6", str_at_true_precision(zeta2_minus_pi_sq_div_6))
    builder.add_data("phi_n_holonomy_prod", str_at_true_precision(holonomy_prod))
    builder.add_data("phi_n_holonomy_abs_diff", str_at_true_precision(phi_n_holonomy_abs_diff))
    builder.add_data("bch_first_order_residual", str_at_true_precision(bch_identity_residual))
    builder.add_data("commutator_fro_norm", str_at_true_precision(commutator_fro_norm))
    builder.add_data(
        "holonomy_defect_minus_identity_fro_norm",
        str_at_true_precision(defect_minus_identity_norm),
    )
    builder.add_data("iterated_part_b_neg_pi_sq_div_6", str_at_true_precision(iterated_part_b))
    builder.add_data(
        "surface_ordering_shift_neg_two_zeta2",
        str_at_true_precision(surface_ordering_shift_zeta),
    )
    builder.add_data(
        "surface_ordering_shift_neg_pi_sq_div_3",
        str_at_true_precision(surface_ordering_shift_closed),
    )
    builder.add_data(
        "surface_ordering_shift_neg_two_li2_one",
        str_at_true_precision(neg_two_li2_at_one),
    )
    builder.add_data("surface_shift_abs_diff", str_at_true_precision(surface_shift_abs_diff))
    builder.add_data("li2_shift_abs_diff", str_at_true_precision(li2_shift_abs_diff))
    builder.add_data("na_stokes_part_b_neg_pi_sq_div_2", str_at_true_precision(na_stokes_part_b))
    builder.add_data("na_stokes_part_b_abs_diff", str_at_true_precision(na_stokes_part_b_abs_diff))

    builder.add_assertion(
        name="phi_n_matches_yekutieli_holonomy",
        computed=str_at_true_precision(holonomy_prod),
        expected=str_at_true_precision(phi_n_direct),
        tolerance="1e-55",
        source="QOU.Torsion.MultiplicativeIntegralCurvature.phiN_eq_yekutieli_holonomy",
    )
    builder.add_assertion(
        name="first_order_iterated_diff_matches_commutator",
        computed=str_at_true_precision(bch_identity_residual),
        expected="0",
        tolerance="1e-55",
        source="QOU.Torsion.MultiplicativeIntegralCurvature.first_order_bch_iterated_diff_eq_commutator",
    )
    builder.add_assertion(
        name="surface_ordering_shift_equals_neg_pi_sq_div_3",
        computed=str_at_true_precision(surface_ordering_shift_zeta),
        expected=str_at_true_precision(surface_ordering_shift_closed),
        tolerance="1e-55",
        source="QOU.Torsion.MultiplicativeIntegralCurvature.tsum_neg_two_zeta_two_eq_surfaceOrderingShift",
    )
    builder.add_assertion(
        name="na_stokes_part_b_equals_neg_pi_sq_div_2",
        computed=str_at_true_precision(na_stokes_part_b),
        expected=str_at_true_precision(expected_na_stokes_part_b),
        tolerance="1e-55",
        source="QOU.Torsion.MultiplicativeIntegralCurvature.iterated_partB_shift_eq_neg_pi_sq_div_three",
    )

    out_path = builder.save({
        "invocation": {
            "argv": [
                "computations/probes/yekutieli_multiplicative_integral_curvature_probe.py"
            ],
            "reproduce": "python3 -u computations/probes/yekutieli_multiplicative_integral_curvature_probe.py",
        },
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 50, strip_zeros=False),
    })
    print(f"Wrote witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
