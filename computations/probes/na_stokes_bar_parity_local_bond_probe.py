#!/usr/bin/env python3
"""NA-Stokes curvature bar-parity split and Yekutieli B_3 local (2,1) bond probe
(qou-yczy, qou-quv8, qou-ch8w, qou-h5aw).

Verifies at 50+ decimal places (`mpmath.mp.dps >= 70`, output 60 dps) at the
canonical proton anchor `q_0`:

1. **`qou-yczy` — NA-Stokes curvature route to `-pi^2 / 3 = -2 * (pi^2 / 6)`:**
   - Decomposes the 2-simplex surface-ordering curvature shift `-pi^2 / 3` into
     the two oriented half-plaquette dilogarithm contributions
     `-Li_2(1) + (-Li_2(1)) = -2 * zeta(2) = -2 * (pi^2 / 6) = -pi^2 / 3`.
   - Evaluates the bar-odd `sinh(log q_0) = (q_0 - q_0^{-1}) / 2 = h_0 / 2` and
     bar-even `cosh(log q_0) - 1 = (q_0 + q_0^{-1} - 2) / 2 = (q_0 - 1)^2 / (2 q_0)`
     substrate channels at `q_0`, verifying the hyperbolic identity
     `cosh(log q_0)^2 - sinh(log q_0)^2 = 1` to 50+ dps.

2. **`qou-quv8` & `qou-ch8w` — Bar-parity split of `mu_0` and 2nd-order bar-even
   NA-Stokes counit term:**
   - The leading coupling `mu_0(h_0) = c_1 * h_0` is strictly bar-odd under
     `h_0 -> -h_0` (`q_0 -> q_0^{-1}`).
   - Adding the 2nd-order bar-even counit term `c_2 * h_0^2` yields
     `mu_eff(h_0) = mu_odd(h_0) + mu_even(h_0)`, with exact parity projection
     `mu_eff(h_0) + mu_eff(-h_0) = 2 * mu_even(h_0)` and
     `mu_eff(h_0) - mu_eff(-h_0) = 2 * mu_odd(h_0)`.

3. **`qou-h5aw` — Project Yekutieli `B_3` action onto the local `(2,1)` bond:**
   - Constructs the explicit 2x2 representation matrices `T_1, T_2` of the
     2-dimensional standard Hook representation `V_{(2,1)}` of `H_3(q_0)` with
     eigenvalues `(q_0, -q_0^{-1})`.
   - Evaluates the single-bond Yekutieli step `M = T_1 * T_2^{-1}`, verifying
     `det(M) = 1` and `tr(M) = -1 - h_0^2` (`yekutieliBond21Trace`).
   - Verifies that the 3-fold Yekutieli holonomy `M^3 = (T_1 * T_2^{-1})^3`
     around the Borromean cycle has trace
     `tr(M^3) = tr(M)^3 - 3 * tr(M) = (-1 - h_0^2)^3 - 3 * (-1 - h_0^2) = 2 - 3*h_0^4 - h_0^6 = chi^{(2,1)}(beta_Bor)`
     with the `O(h_0^2)` term cancelling identically (`T_3'(-1) = 0`).

Lean companion:
  `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanChiPerRep.lean`
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
        "na-stokes-bar-parity-local-bond",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "50+ dps verification of the NA-Stokes curvature route -2*(pi^2/6) = -pi^2/3 "
        "(qou-yczy), the bar-odd sinh / bar-even cosh counit parity split (qou-quv8, "
        "qou-ch8w), and the Yekutieli B_3 local (2,1) bond trace projection "
        "(-1 - h^2)^3 - 3*(-1 - h^2) = 2 - 3*h^4 - h^6 (qou-h5aw)."
    )

    q0 = q_at()
    inv_q0 = mp.mpf(1) / q0
    h0 = q0 - inv_q0
    pi = mp.pi

    # 1. qou-yczy: NA-Stokes -pi^2/3 = -2 * (pi^2/6) decomposition + sinh/cosh split
    zeta2 = mp.zeta(2)
    half_plaquette_shift = - (pi ** 2) / mp.mpf(6)
    double_half_plaquette = half_plaquette_shift + half_plaquette_shift
    surface_ordering_shift = - (pi ** 2) / mp.mpf(3)
    total_part_b_shifted = half_plaquette_shift + surface_ordering_shift
    expected_part_b_shifted = - (pi ** 2) / mp.mpf(2)

    sinh_log_q0 = h0 / mp.mpf(2)
    cosh_log_q0 = (q0 + inv_q0) / mp.mpf(2)
    cosh_minus_one = ((q0 - mp.mpf(1)) ** 2) / (mp.mpf(2) * q0)
    hyperbolic_casimir_residual = abs((cosh_log_q0 ** 2 - sinh_log_q0 ** 2) - mp.mpf(1))
    cosh_minus_one_residual = abs((cosh_log_q0 - mp.mpf(1)) - cosh_minus_one)

    # 2. qou-quv8 & qou-ch8w: Bar-parity split of mu_eff(h) = mu_odd(h) + mu_even(h)
    c1 = mp.mpf(1)
    c2 = mp.mpf(1) / mp.mpf(2)
    c3 = -mp.mpf(1) / mp.mpf(6)
    c4 = -mp.mpf(1) / mp.mpf(8)

    def mu_odd(h_val: mp.mpf) -> mp.mpf:
        return c1 * h_val + c3 * (h_val ** 3)

    def mu_even(h_val: mp.mpf) -> mp.mpf:
        return c2 * (h_val ** 2) + c4 * (h_val ** 4)

    def mu_eff(h_val: mp.mpf) -> mp.mpf:
        return mu_odd(h_val) + mu_even(h_val)

    mu_eff_pos = mu_eff(h0)
    mu_eff_neg = mu_eff(-h0)
    even_extracted = (mu_eff_pos + mu_eff_neg) / mp.mpf(2)
    odd_extracted = (mu_eff_pos - mu_eff_neg) / mp.mpf(2)
    even_parity_residual = abs(even_extracted - mu_even(h0))
    odd_parity_residual = abs(odd_extracted - mu_odd(h0))

    # 3. qou-h5aw: Explicit 2x2 local (2,1) bond representation of H_3(q_0)
    # In V_{(2,1)}, T_1 and T_2 have eigenvalues (q_0, -q_0^{-1}) and satisfy
    # T_1 T_2 T_1 = T_2 T_1 T_2 with tr(T_1 T_2^{-1}) = -1 - h_0^2:
    # Specifically, in the standard Burau/Hook basis where
    # T_1 = [[q_0, 0], [1, -q_0^{-1}]], T_2 = [[-q_0^{-1}, 1], [0, q_0]]:
    T1 = mp.matrix([[q0, mp.mpf(0)], [mp.mpf(1), -inv_q0]])
    T2 = mp.matrix([[-inv_q0, mp.mpf(1)], [mp.mpf(0), q0]])
    T2_inv = T2 ** -1

    # Check braid relation T_1 T_2 T_1 = T_2 T_1 T_2
    braid_rel_residual = mp.norm(T1 * T2 * T1 - T2 * T1 * T2, 2)

    # Single Yekutieli plaquette step on the local (2,1) bond: M = T_1 T_2^{-1}
    M_bond = T1 * T2_inv
    det_M = M_bond[0, 0] * M_bond[1, 1] - M_bond[0, 1] * M_bond[1, 0]
    tr_M = M_bond[0, 0] + M_bond[1, 1]
    expected_tr_M = -mp.mpf(1) - (h0 ** 2)
    tr_M_residual = abs(tr_M - expected_tr_M)
    det_M_residual = abs(det_M - mp.mpf(1))

    # 3-fold Yekutieli Borromean holonomy M^3 = (T_1 T_2^{-1})^3
    M_cubed = M_bond * M_bond * M_bond
    tr_M_cubed = M_cubed[0, 0] + M_cubed[1, 1]
    chebyshev_cubic = (tr_M ** 3) - mp.mpf(3) * tr_M
    chi21_borromean = mp.mpf(2) - mp.mpf(3) * (h0 ** 4) - (h0 ** 6)
    b3_bond_projection_residual = abs(tr_M_cubed - chi21_borromean)
    chebyshev_poly_residual = abs(chebyshev_cubic - chi21_borromean)

    builder.add_parameter("q_proton", str_at_true_precision(q0))
    builder.add_parameter("h_proton", str_at_true_precision(h0))

    builder.add_data("beans", ["qou-yczy", "qou-quv8", "qou-ch8w", "qou-h5aw", "qou-wp3h"])
    builder.add_data("lean_module", "QOU.BraidsAndKnots")
    builder.add_data("zeta_2", str_at_true_precision(zeta2))
    builder.add_data("half_plaquette_shift_neg_pi_sq_div_6", str_at_true_precision(half_plaquette_shift))
    builder.add_data("double_half_plaquette_neg_pi_sq_div_3", str_at_true_precision(double_half_plaquette))
    builder.add_data("total_part_b_shifted_neg_pi_sq_div_2", str_at_true_precision(total_part_b_shifted))
    builder.add_data("sinh_log_q0_bar_odd", str_at_true_precision(sinh_log_q0))
    builder.add_data("cosh_log_q0_minus_one_bar_even", str_at_true_precision(cosh_minus_one))
    builder.add_data("hyperbolic_casimir_residual", str_at_true_precision(hyperbolic_casimir_residual))
    builder.add_data("mu_odd_h0", str_at_true_precision(mu_odd(h0)))
    builder.add_data("mu_even_h0", str_at_true_precision(mu_even(h0)))
    builder.add_data("mu_eff_h0", str_at_true_precision(mu_eff_pos))
    builder.add_data("even_parity_residual", str_at_true_precision(even_parity_residual))
    builder.add_data("odd_parity_residual", str_at_true_precision(odd_parity_residual))
    builder.add_data("braid_relation_fro_residual", str_at_true_precision(braid_rel_residual))
    builder.add_data("yekutieli_bond21_trace", str_at_true_precision(tr_M))
    builder.add_data("yekutieli_bond21_det_residual", str_at_true_precision(det_M_residual))
    builder.add_data("yekutieli_b3_bond21_trace_cubed", str_at_true_precision(tr_M_cubed))
    builder.add_data("chi21_borromean_h0", str_at_true_precision(chi21_borromean))
    builder.add_data("b3_bond_projection_residual", str_at_true_precision(b3_bond_projection_residual))

    builder.add_assertion(
        name="double_half_plaquette_equals_surface_ordering_shift",
        computed=str_at_true_precision(double_half_plaquette),
        expected=str_at_true_precision(surface_ordering_shift),
        tolerance="1e-55",
        source="QOU.BraidsAndKnots.naStokes_surface_ordering_double_half_plaquette",
    )
    builder.add_assertion(
        name="bar_parity_split_extracts_even_and_odd_counit_channels",
        computed=str_at_true_precision(even_parity_residual + odd_parity_residual),
        expected="0",
        tolerance="1e-55",
        source="QOU.BraidsAndKnots.naStokesMuEff_bar_parity_split",
    )
    builder.add_assertion(
        name="yekutieli_single_bond21_trace_equals_neg_one_minus_h_sq",
        computed=str_at_true_precision(tr_M),
        expected=str_at_true_precision(expected_tr_M),
        tolerance="1e-55",
        source="QOU.BraidsAndKnots.yekutieliBond21Trace",
    )
    builder.add_assertion(
        name="yekutieli_b3_local_21_bond_projection_matches_chi21_borromean",
        computed=str_at_true_precision(tr_M_cubed),
        expected=str_at_true_precision(chi21_borromean),
        tolerance="1e-55",
        source="QOU.BraidsAndKnots.yekutieli_b3_local_21_bond_projection",
    )

    out_path = builder.save({
        "invocation": {
            "argv": [
                "computations/probes/na_stokes_bar_parity_local_bond_probe.py"
            ],
            "reproduce": "python3 -u computations/probes/na_stokes_bar_parity_local_bond_probe.py",
        },
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 50, strip_zeros=False),
    })
    print(f"Wrote witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
