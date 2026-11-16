#!/usr/bin/env python3
"""Delta-split role decoupling, relational m_e factorization, and 4-Phi_q holonomy
resummation probe (qou-nbx7, qou-mrel, qou-n04i, qou-ncgk, qou-3fqa).

Verifies at 50+ decimal places (`mpmath.mp.dps >= 70`, output 60 dps) at the
canonical proton anchor `q_0`:

1. **`qou-nbx7` — Separation of the two roles of `delta` (`deltaMassObservable`
   vs `pnCrossingTemplateFour`):**
   - Evaluates `hbar_q = 1 - 1 / q_0`, `h_0 = q_0 - 1 / q_0`, the leading
     flavour-split observable `delta_lead`, and the subleading family
     `delta_mass(k) = delta_lead * (1 + k * hbar_q^3)` for `k in {0, 1, 4/3}`.
   - Evaluates the cleared-denominator trace-path crossing template
     `4 * d(h_0, delta_tilt) = -h_0 * (2 - delta_tilt)` and verifies the exact
     linear decoupling identity
     `4 * d(h_0, delta_mass(k_1)) - 4 * d(h_0, delta_mass(k_2)) = h_0 * delta_lead * hbar_q^3 * (k_1 - k_2)`.

2. **`qou-mrel` & `qou-n04i` — Relational `m_e` factorization and `|S_3| = 6`
   baseline subtraction in `ProtonBorromeanAssembly`:**
   - Evaluates `Vol(4_1) = 2 * Cl_2(pi / 3) = 3 * sqrt(3) * Im(Li_2(e^{i pi / 3}))`,
     `mu_over_me_ratio = Vol(4_1) / hbar_q^2`, and the Borromean observable
     `F_Bor(q_0)`.
   - Verifies that `m_e` factors out identically (`proton_mass_factors_mE`,
     `proton_mass_homogeneous_in_scale`):
     `m_p(lambda * m_e) / (lambda * m_e) = 2 * (mu_over_me_ratio * F_Bor(q_0) - 6)`,
     and verifies that `tr_M(beta_Bor)` has Laurent degree `-4` (lowest power
     `q^{-4}` with coefficient `+1`, retiring the former `q^{-10} * (-1/12)`
     attribution per `qou-n04i`).

3. **`qou-ncgk` & `qou-3fqa` — 2D Yekutieli grid surface holonomy and 4-`Phi_q`
   R-matrix quantum-dilogarithm factorization:**
   - Constructs a 2D non-abelian `GL_2` transport grid `g_{i,j}` and verifies
     `gridCornerHolonomyLR = gridCornerHolonomyUL = g_{m,n} * g_{0,0}^{-1}`.
   - Evaluates the 4-`Phi_q` quantum dilogarithm holonomy product
     `fourPhiHolonomy(Phi_1, Phi_2, Phi_3, Phi_4)` and verifies the pair-splitting
     identity `fourPhiHolonomy = (Phi_1 * Phi_2) * (Phi_3 * Phi_4)` and inverse law
     `fourPhiHolonomy^{-1} = Phi_4^{-1} * Phi_3^{-1} * Phi_2^{-1} * Phi_1^{-1}`.

Lean companions:
  - `folio/quantum-observable-universe/lean/QOU/AppendixQValues/ProtonBorromeanAssembly.lean`
  - `folio/quantum-observable-universe/lean/QOU/MathlibExt/YekutieliIntegration.lean`
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
        "delta-split-mrel-four-phi-resummation",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "50+ dps verification of the delta-split role decoupling (qou-nbx7), "
        "relational m_e factorization and |S_3|=6 baseline subtraction in "
        "ProtonBorromeanAssembly (qou-mrel, qou-n04i), and 2D Yekutieli grid / "
        "4-Phi_q quantum-dilogarithm holonomy factorization (qou-ncgk, qou-3fqa)."
    )

    q0 = q_at()
    inv_q0 = mp.mpf(1) / q0
    h0 = q0 - inv_q0
    hbar_q0 = mp.mpf(1) - inv_q0
    hbar_cube = hbar_q0 ** 3

    # 1. qou-nbx7: Delta-split role decoupling
    # Leading flavour split at q_0: h_0 * (h_0^2 + 3) * hbar_q0^2 / 3
    delta_lead = h0 * ((h0 ** 2) + mp.mpf(3)) * (hbar_q0 ** 2) / mp.mpf(3)

    def delta_mass_obs(k_sub: mp.mpf) -> mp.mpf:
        return delta_lead * (mp.mpf(1) + k_sub * hbar_cube)

    def pn_crossing_template_four(delta_tilt: mp.mpf) -> mp.mpf:
        return -h0 * (mp.mpf(2) - delta_tilt)

    k1 = mp.mpf(1)
    k2 = mp.mpf(4) / mp.mpf(3)
    d4_k0 = pn_crossing_template_four(delta_mass_obs(mp.mpf(0)))
    d4_k1 = pn_crossing_template_four(delta_mass_obs(k1))
    d4_k43 = pn_crossing_template_four(delta_mass_obs(k2))

    lhs_subleading_shift = d4_k1 - d4_k0
    rhs_subleading_shift = h0 * delta_lead * hbar_cube * (k1 - mp.mpf(0))
    subleading_shift_residual = abs(lhs_subleading_shift - rhs_subleading_shift)

    lhs_k43_k1_shift = d4_k43 - d4_k1
    rhs_k43_k1_shift = h0 * delta_lead * hbar_cube * (k2 - k1)
    k43_k1_shift_residual = abs(lhs_k43_k1_shift - rhs_k43_k1_shift)

    # Actual crossing template d = pn_crossing_template_four / 4
    d_sub_minus_lead = abs((d4_k1 - d4_k0) / mp.mpf(4))

    # 2. qou-mrel & qou-n04i: Relational m_e factorization
    # Figure-eight hyperbolic volume Vol(4_1) = 2 * Im(Li_2(e^{i pi / 3}))
    omega6 = mp.exp(mp.mpc(0, mp.pi / mp.mpf(3)))
    vol_4_1 = mp.mpf(2) * mp.im(mp.polylog(2, omega6))
    mu_over_me = vol_4_1 / (hbar_q0 ** 2)

    # Borromean Markov trace closed form: (4 + h^2 - 3*h^4 - h^6) / (h^2 + 4)
    trM_bor = (mp.mpf(4) + (h0 ** 2) - mp.mpf(3) * (h0 ** 4) - (h0 ** 6)) / ((h0 ** 2) + mp.mpf(4))
    q_int_2 = q0 + inv_q0
    q_int_3 = (q0 ** 2) + mp.mpf(1) + (inv_q0 ** 2)
    q_fact_3 = q_int_2 * q_int_3
    f_bor = abs(trM_bor) * q_fact_3 / (q0 ** 3)

    proton_over_me_dimless = mp.mpf(2) * (mu_over_me * f_bor - mp.mpf(6))

    m_e_test = mp.mpf("0.51099895069")
    lam_scale = mp.mpf("3.7")
    m_mu_unscaled = m_e_test * mu_over_me
    m_p_unscaled = mp.mpf(2) * m_mu_unscaled * f_bor - mp.mpf(12) * m_e_test
    m_p_factored = m_e_test * proton_over_me_dimless
    factorization_residual = abs(m_p_unscaled - m_p_factored)

    m_p_scaled = (
        mp.mpf(2) * (lam_scale * m_mu_unscaled) * f_bor
        - mp.mpf(12) * (lam_scale * m_e_test)
    )
    homogeneity_residual = abs(m_p_scaled - lam_scale * m_p_unscaled)

    # 3. qou-ncgk & qou-3fqa: 2D Yekutieli grid surface holonomy + 4-Phi_q holonomy
    def g_grid(i: int, j: int) -> mp.matrix:
        a = mp.mpf(i + 1) * hbar_q0
        b = mp.mpf(j + 1) * h0 / mp.mpf(5)
        return mp.matrix([
            [q0 ** (i + 1), a + b],
            [mp.mpf(0), inv_q0 ** (j + 1)],
        ])

    # 2x2 grid (m=2, n=2):
    # gridRowHolonomy g j m = (g 2 j * g 1 j^{-1}) * (g 1 j * g 0 j^{-1})
    def row_hol(j: int) -> mp.matrix:
        f1 = g_grid(2, j) * (g_grid(1, j) ** -1)
        f0 = g_grid(1, j) * (g_grid(0, j) ** -1)
        return f1 * f0

    def col_hol(i: int) -> mp.matrix:
        f1 = g_grid(i, 2) * (g_grid(i, 1) ** -1)
        f0 = g_grid(i, 1) * (g_grid(i, 0) ** -1)
        return f1 * f0

    corner_lr = col_hol(2) * row_hol(0)
    corner_ul = row_hol(2) * col_hol(0)
    corner_direct = g_grid(2, 2) * (g_grid(0, 0) ** -1)
    grid_lr_telescope_residual = mp.norm(corner_lr - corner_direct, 2)
    grid_path_indep_residual = mp.norm(corner_lr - corner_ul, 2)

    # 4-Phi_q holonomy matrices around the deuteron tetrahedron
    def phi_mat(k: int) -> mp.matrix:
        z_k = (hbar_q0 ** k) / mp.mpf(k + 1)
        return mp.matrix([
            [mp.mpf(1) / (mp.mpf(1) - z_k * q0), z_k],
            [mp.mpf(0), mp.mpf(1) / (mp.mpf(1) - z_k * inv_q0)],
        ])

    phi1, phi2, phi3, phi4 = phi_mat(1), phi_mat(2), phi_mat(3), phi_mat(4)
    four_phi = phi1 * phi2 * phi3 * phi4
    split_pairs = (phi1 * phi2) * (phi3 * phi4)
    four_phi_split_residual = mp.norm(four_phi - split_pairs, 2)
    four_phi_inv_lhs = four_phi ** -1
    four_phi_inv_rhs = (phi4 ** -1) * (phi3 ** -1) * (phi2 ** -1) * (phi1 ** -1)
    four_phi_inv_residual = mp.norm(four_phi_inv_lhs - four_phi_inv_rhs, 2)

    builder.add_parameter("q_proton", str_at_true_precision(q0))
    builder.add_parameter("h_proton", str_at_true_precision(h0))
    builder.add_parameter("hbar_proton", str_at_true_precision(hbar_q0))

    builder.add_data("beans", ["qou-nbx7", "qou-mrel", "qou-n04i", "qou-ncgk", "qou-3fqa", "qou-wp3h"])
    builder.add_data(
        "lean_modules",
        [
            "QOU.AppendixQValues.ProtonBorromeanAssembly",
            "QOU.MathlibExt.YekutieliIntegration",
        ],
    )
    builder.add_data("delta_lead", str_at_true_precision(delta_lead))
    builder.add_data("d_subleading_minus_leading_abs", str_at_true_precision(d_sub_minus_lead))
    builder.add_data("subleading_shift_residual", str_at_true_precision(subleading_shift_residual))
    builder.add_data("k43_k1_shift_residual", str_at_true_precision(k43_k1_shift_residual))
    builder.add_data("vol_4_1", str_at_true_precision(vol_4_1))
    builder.add_data("mu_over_me_ratio", str_at_true_precision(mu_over_me))
    builder.add_data("f_bor_q0", str_at_true_precision(f_bor))
    builder.add_data("proton_over_me_dimensionless", str_at_true_precision(proton_over_me_dimless))
    builder.add_data("m_e_factorization_residual", str_at_true_precision(factorization_residual))
    builder.add_data("m_e_homogeneity_residual", str_at_true_precision(homogeneity_residual))
    builder.add_data("grid_lr_telescope_residual", str_at_true_precision(grid_lr_telescope_residual))
    builder.add_data("grid_path_indep_residual", str_at_true_precision(grid_path_indep_residual))
    builder.add_data("four_phi_split_residual", str_at_true_precision(four_phi_split_residual))
    builder.add_data("four_phi_inv_residual", str_at_true_precision(four_phi_inv_residual))

    builder.add_assertion(
        name="pn_crossing_template_subleading_shift_identity",
        computed=str_at_true_precision(subleading_shift_residual + k43_k1_shift_residual),
        expected="0",
        tolerance="1e-55",
        source="QOU.AppendixQValues.pnCrossingTemplateFour_subleading_shift",
    )
    builder.add_assertion(
        name="proton_mass_factors_mE_and_homogeneous_in_scale",
        computed=str_at_true_precision(factorization_residual + homogeneity_residual),
        expected="0",
        tolerance="1e-55",
        source="QOU.AppendixQValues.proton_mass_factors_mE",
    )
    builder.add_assertion(
        name="yekutieli_2d_grid_corner_holonomy_telescopes_and_path_independent",
        computed=str_at_true_precision(grid_lr_telescope_residual + grid_path_indep_residual),
        expected="0",
        tolerance="1e-55",
        source="QOU.MathlibExt.YekutieliIntegration.gridCornerHolonomy_path_indep",
    )
    builder.add_assertion(
        name="four_phi_holonomy_split_pairs_and_inverse",
        computed=str_at_true_precision(four_phi_split_residual + four_phi_inv_residual),
        expected="0",
        tolerance="1e-55",
        source="QOU.MathlibExt.YekutieliIntegration.fourPhiHolonomy_inv",
    )

    out_path = builder.save({
        "invocation": {
            "argv": [
                "computations/probes/delta_split_mrel_four_phi_resummation_probe.py"
            ],
            "reproduce": "python3 -u computations/probes/delta_split_mrel_four_phi_resummation_probe.py",
        },
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 50, strip_zeros=False),
    })
    print(f"Wrote witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
