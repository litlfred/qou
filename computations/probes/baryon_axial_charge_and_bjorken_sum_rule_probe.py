#!/usr/bin/env python3
"""baryon_axial_charge_and_bjorken_sum_rule_probe.py — 80-dps Baryon Spin-Flavour
Antisymmetry Derivation of g_A^(0) = 5/3 and mu_p^(0)/mu_n^(0) = -3/2, Zero-Fitting
H_3(q) Borromean Axial Coupling Census, & Polarized DIS Bjorken Sum-Rule Probe.

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/BaryonSpinFlavourAxialAndBjorkenSumRule.lean`
  (`namespace QOU.StandardModel.BaryonSpinFlavourAxialAndBjorkenSumRule`).

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (95 working guard digits, zero float64 intermediates,
zero `math` module imports, zero fitted parameters, zero CODATA/PDG-proximity assertions)
three linked components of the baryon spin-flavour and polarized deep-inelastic
scattering (DIS) sector:

1. **Part 1 — Exact 64-State Spin-Flavour Tensor Derivation of `g_A^(0) = 5/3` and
   `mu_p^(0) / mu_n^(0) = -3/2` from `Lambda^3 W_3` Colour Antisymmetry**:
   - From `BringPushforwardAndGaugeGroupUnification.lean`, the rank-3 Kummer pushforward
     colour bundle `W_3 = pi_* L` has a unique 1-dimensional totally antisymmetric colour-singlet
     determinant line `Lambda^3 W_3` (`dim Lambda^3 W_3 = C(3,3) = 1`).
   - Fermi-Dirac antisymmetry of the 3-quark state forces the spin-flavour wave function in
     `(V_2^{spin} (x) V_2^{flav})^(x)3 ~= (Q^4)^(x)3` (`4^3 = 64` basis states) to lie in the
     20-dimensional totally `S_3`-symmetric subspace `Sym^3(Q^4)` (`C(6,3) = 20 = 2*2 + 4*4`).
   - Constructs all 64 basis states explicitly over exact rationals (`mp.mpf` integers) and
     verifies for the unique `S_3`-symmetric spin-1/2, isospin-1/2 nucleon states `|p_up>`, `|n_up>`
     and spin-3/2, isospin-3/2 Delta state `|Delta^+_up>`:
       * Exact `S_3` permutation invariance under `tau_12, tau_23, tau_13`,
       * Exact squared norms (`<p_up|p_up> = 18`, `<n_up|n_up> = 18`, `<Delta^+_up|Delta^+_up> = 9`)
         and pairwise orthogonality (`0`),
       * Exact Casimir eigenvalues `S_z = +1/2`, `S^2 = 3/4`, `I_3 = +/-1/2`, `I^2 = 3/4` for
         `|p_up>, |n_up>` and `S^2 = 15/4, I^2 = 15/4` for `|Delta^+_up>`,
       * Exact derived constituent quark spin fractions `Delta_u = 24/18 = 4/3` and
         `Delta_d = -6/18 = -1/3` (`Delta_u + Delta_d = 1 = 2 S_z`),
       * Exact derived tree-level Gamow-Teller axial charge `g_A^(0) = Delta_u - Delta_d = 5/3`,
       * Exact derived tree-level magnetic moments `mu_p^(0) = Q_u Delta_u + Q_d Delta_d = +1`,
         `mu_n^(0) = Q_d Delta_u + Q_u Delta_d = -2/3`, and ratio `mu_p^(0) / mu_n^(0) = -3/2 = -1.5`
         from the Kummer fractional charges `(Q_u, Q_d) = (+2/3, -1/3)` (compared transparently
         against experimental `mu_p^{exp} / mu_n^{exp} = 2.79284734463 / (-1.91304273) = -1.45989805...`,
         relative offset `-2.747%`).

2. **Part 2 — Zero-Fitting Side-by-Side Census of `q`-Deformed Borromean Axial Coupling Branches
   Across `{q_0, q_2t, q_muon}`**:
   - Evaluates side-by-side without post-hoc branch selection across all three substrate pins
     (`q_0` 1-term proton, `q_2t` 2-term QED-subtracted Borromean proton, `q_muon` ideal CAL-2 muon)
     every candidate `q`-deformed Borromean axial-coupling map built from `HeckeH3.lean`,
     `TransferMatrix.lean`, and `AxialCoupling.lean`:
       * `branch_0_tree_su6`: derived tree-level `S_3`-symmetric limit `g_A^(0) = 5/3 = 1.66666666...`,
       * `branch_1a_h3_color_avg_ordinary_trace_conv_q`: `(5/3) |tr_std((h_01 + h_12 + h_02)/3)| / |tr_sym((h_01 + h_12 + h_02)/3)|`
         in the 2D Young seminormal representation of `H_3(q)` with generator eigenvalues `(q, -q^{-1})`
         (`HeckeH3.lean` line 346 `axialCouplingAlgebraic`), reported alongside the three individual
         colour-tube pairings `h_01` (`rg`), `h_12` (`gb`), and `h_02` (`rb`),
       * `branch_1b_h3_color_avg_cleared_markov_vol_conv_q`: `(5/3) |tracedVolCleared((h_01 + h_12 + h_02)/3)|`
         using `tracedVolCleared(M) = M_00 + (q^{1/2} + q^{-1/2}) M_10` (`TransferMatrix.lean` line 191),
         reported alongside the three individual colour-tube pairings `h_01`, `h_12`, `h_02`,
       * `branch_1c_h3_color_avg_ordinary_trace_conv_q2`: ordinary trace ratio evaluated under the
         `t = q => q_{Hecke} = q^2` convention (`HA = q^2 - q^{-2}`),
       * `branch_1d_h3_color_avg_cleared_markov_vol_conv_q2`: `tracedVolCleared` ratio evaluated under
         `t = q => q_{Hecke} = q^2, markov_denom = q + q^{-1}`,
       * `branch_2_h3_full_6crossing_borromean_character`: full 6-crossing Borromean braid
         `beta_Bor = (sigma_0 sigma_1^{-1})^3` normalized character ratio
         `(5/3) (chi^{(2,1)}(beta_Bor) / 2) = (5/3)(1 - (3/2) h^4 - (1/2) h^6)` (`HeckeH3.lean` line 189),
       * `branch_3_spin_flavour_64state_jimbo_r`: 64-state spin-flavour Jimbo `U_q(sl_2)` `R`-matrix
         braided expectation value `<psi_q | O_A | psi_q> / <psi_q | psi_q>` under both the 3-fold
         colour-averaged half-Borromean action and the full 6-crossing Borromean braid action on `|p_up>`,
       * `branch_4_structural_q_scalings`: algebraic `q`-integer and Markov scalings
         `(5/3) / [2]_q`, `(5/3) / [2]_q^2`, `(5/3) z_D` (`z_D = q^3 / (q^2 + 1)`), and `(5/3)(1 - h^2)`.
   - Compares all branches transparently against PDG 2024 neutron beta-decay axial coupling
     `g_A^{exp} = 1.2754 +/- 0.0013` and audits why no single post-hoc branch selection is asserted.

3. **Part 3 — Polarized DIS Bjorken Sum Rule `Gamma_1^{p-n}(Q^2)` at `Q^2 in {3, 5, 10} GeV^2`**:
   - Evaluates the `n_f = 3` MSbar perturbative QCD Bjorken polarized sum rule
     (`BaryonSpinFlavourAxialAndBjorkenSumRule.lean` section 4):
       `Gamma_1^{p-n}(Q^2) = (g_A / 6) [1 - (alpha_s / pi) - (43/12)(alpha_s / pi)^2 - c_3^{Bj}(3)(alpha_s / pi)^3]`
     at 1-loop, 2-loop (`c_2^{Bj}(3) = 43/12`), and 3-loop (`c_3^{Bj}(3) = 115/72 - (1343/144 - 11/2) zeta(3) + ...`
     Larin & Vermaseren 1991 `c_3^{Bj}(3) = 20.21527...`) orders across `Q^2 in {3, 5, 10} GeV^2`
     using QOU's 2-loop running `alpha_s(Q^2)` under both `(3/2) m_pi` threshold interpretations
     (`Lambda^{(5)}` and `Lambda^{(3)}`) as well as empirical PDG `alpha_s(M_Z) = 0.1180`,
     comparing transparently against COMPASS/JLab polarized DIS measurements
     `Gamma_1^{p-n,exp}(3 GeV^2) = 0.181 +/- 0.008` and `Gamma_1^{p-n,exp}(5 GeV^2) = 0.182 +/- 0.007`.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ["QOU_OUTPUT_DPS"] = "80"
os.environ["QOU_COMPUTE_DPS"] = "95"
os.environ["QOU_PRECISION_GUARD"] = "15"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402

set_compute_dps(80)

from codata_constants import (  # noqa: E402
    M_PI_PM_MEV_VALIDATION,
)
from q_parameter import q_at, q_muon_at, q_two_term_borromean_at  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Section 0: Quantum Integer & 2x2 Matrix Helpers ──────────────────────────
def q_int(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - mp.mpf(1) / q)


def mat2_eye() -> list[list[mp.mpf]]:
    """2x2 identity matrix over mp.mpf."""
    return [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def mat2_add(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    """2x2 matrix addition over mp.mpf."""
    return [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]],
    ]


def mat2_scale(c: mp.mpf, a: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    """2x2 scalar multiplication over mp.mpf."""
    return [
        [c * a[0][0], c * a[0][1]],
        [c * a[1][0], c * a[1][1]],
    ]


def mat2_mul(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    """2x2 matrix multiplication over mp.mpf."""
    return [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ],
    ]


def mat2_trace(a: list[list[mp.mpf]]) -> mp.mpf:
    """Ordinary matrix trace tr(A) = A_00 + A_11."""
    return a[0][0] + a[1][1]


def mat2_traced_vol_cleared(a: list[list[mp.mpf]], markov_denom: mp.mpf) -> mp.mpf:
    """Cleared Markov traced volume M_00 + markov_denom * M_10 from TransferMatrix.lean line 191."""
    return a[0][0] + markov_denom * a[1][0]


# ── Section 1: Exact 64-State Spin-Flavour Tensor Derivation ─────────────────
QuarkState = tuple[int, int]  # (flavour: 0=u, 1=d; spin: 0=up, 1=down)
BaryonState64 = tuple[QuarkState, QuarkState, QuarkState]

U_UP: QuarkState = (0, 0)
U_DOWN: QuarkState = (0, 1)
D_UP: QuarkState = (1, 0)
D_DOWN: QuarkState = (1, 1)


def enumerate_baryon_basis_64() -> list[BaryonState64]:
    """Enumerate all 4^3 = 64 3-quark spin-flavour basis states in lexicographic order."""
    single_states: list[QuarkState] = [U_UP, U_DOWN, D_UP, D_DOWN]
    basis: list[BaryonState64] = []
    for q1 in single_states:
        for q2 in single_states:
            for q3 in single_states:
                basis.append((q1, q2, q3))
    return basis


def proton_spin_up_amp(s: BaryonState64) -> mp.mpf:
    """Unnormalized S_3-symmetric spin-1/2 proton |p_up> amplitude on BaryonBasis64."""
    if s in (
        (U_UP, U_UP, D_DOWN),
        (U_UP, D_DOWN, U_UP),
        (D_DOWN, U_UP, U_UP),
    ):
        return mp.mpf(2)
    if s in (
        (U_UP, U_DOWN, D_UP),
        (U_DOWN, U_UP, D_UP),
        (U_UP, D_UP, U_DOWN),
        (U_DOWN, D_UP, U_UP),
        (D_UP, U_UP, U_DOWN),
        (D_UP, U_DOWN, U_UP),
    ):
        return mp.mpf(-1)
    return mp.mpf(0)


def neutron_spin_up_amp(s: BaryonState64) -> mp.mpf:
    """Unnormalized S_3-symmetric spin-1/2 neutron |n_up> amplitude on BaryonBasis64."""
    if s in (
        (D_UP, D_UP, U_DOWN),
        (D_UP, U_DOWN, D_UP),
        (U_DOWN, D_UP, D_UP),
    ):
        return mp.mpf(2)
    if s in (
        (D_UP, D_DOWN, U_UP),
        (D_DOWN, D_UP, U_UP),
        (D_UP, U_UP, D_DOWN),
        (D_DOWN, U_UP, D_UP),
        (U_UP, D_UP, D_DOWN),
        (U_UP, D_DOWN, D_UP),
    ):
        return mp.mpf(-1)
    return mp.mpf(0)


def delta_plus_spin_up_amp(s: BaryonState64) -> mp.mpf:
    """Unnormalized S_3-symmetric spin-3/2, S_z=+1/2 |Delta^+_up> amplitude on BaryonBasis64."""
    if s in (
        (U_UP, U_UP, D_DOWN),
        (U_UP, D_DOWN, U_UP),
        (D_DOWN, U_UP, U_UP),
        (U_UP, U_DOWN, D_UP),
        (U_DOWN, U_UP, D_UP),
        (U_UP, D_UP, U_DOWN),
        (U_DOWN, D_UP, U_UP),
        (D_UP, U_UP, U_DOWN),
        (D_UP, U_DOWN, U_UP),
    ):
        return mp.mpf(1)
    return mp.mpf(0)


def compute_spin_flavour_64state_derivation() -> dict[str, object]:
    """Verify on the 64-state spin-flavour tensor space (Q^4)^(x)3:
    1. S_3 permutation invariance of |p_up>, |n_up>, |Delta^+_up>;
    2. Norms (<p|p> = 18, <n|n> = 18, <Delta|Delta> = 9) and mutual orthogonality;
    3. Total spin S^2 and isospin I^2 Casimir eigenvalues (3/4 for N, 15/4 for Delta);
    4. Constituent spin fractions Delta_u = 4/3, Delta_d = -1/3 and derived tree-level
       axial charge g_A^(0) = Delta_u - Delta_d = 5/3;
    5. Derived magnetic moments mu_p^(0) = +1, mu_n^(0) = -2/3 and ratio
       mu_p^(0) / mu_n^(0) = -3/2 from Kummer charges (Q_u, Q_d) = (+2/3, -1/3).
    """
    with mp.workdps(95):
        basis = enumerate_baryon_basis_64()
        p_vec = {s: proton_spin_up_amp(s) for s in basis}
        n_vec = {s: neutron_spin_up_amp(s) for s in basis}
        d_vec = {s: delta_plus_spin_up_amp(s) for s in basis}

        def sigma_z(q: QuarkState) -> mp.mpf:
            return mp.mpf(1) if q[1] == 0 else mp.mpf(-1)

        def tau_3(q: QuarkState) -> mp.mpf:
            return mp.mpf(1) if q[0] == 0 else mp.mpf(-1)

        def is_up(q: QuarkState) -> mp.mpf:
            return mp.mpf(1) if q[0] == 0 else mp.mpf(0)

        def is_down(q: QuarkState) -> mp.mpf:
            return mp.mpf(1) if q[0] == 1 else mp.mpf(0)

        # 1. S_3 permutation invariance residual across all 64 states
        max_s3_residual = mp.mpf(0)
        for s in basis:
            s12 = (s[1], s[0], s[2])
            s23 = (s[0], s[2], s[1])
            s13 = (s[2], s[1], s[0])
            for vec in (p_vec, n_vec, d_vec):
                for sp in (s12, s23, s13):
                    max_s3_residual = max(max_s3_residual, abs(vec[sp] - vec[s]))

        # 2. Inner products & orthogonality
        norm_p = sum(p_vec[s] * p_vec[s] for s in basis)
        norm_n = sum(n_vec[s] * n_vec[s] for s in basis)
        norm_d = sum(d_vec[s] * d_vec[s] for s in basis)
        inner_pn = sum(p_vec[s] * n_vec[s] for s in basis)
        inner_pd = sum(p_vec[s] * d_vec[s] for s in basis)
        inner_nd = sum(n_vec[s] * d_vec[s] for s in basis)

        # 3. Casimir S^2 and I^2 residuals via Dirac exchange identity
        # S^2 psi = (3/4) psi + P_12^{spin} psi + P_23^{spin} psi + P_13^{spin} psi
        max_casimir_residual = mp.mpf(0)
        three_quarters = mp.mpf(3) / mp.mpf(4)
        fifteen_quarters = mp.mpf(15) / mp.mpf(4)
        half = mp.mpf(1) / mp.mpf(2)

        for s in basis:
            sz_val = (sigma_z(s[0]) + sigma_z(s[1]) + sigma_z(s[2])) / mp.mpf(2)
            i3_val = (tau_3(s[0]) + tau_3(s[1]) + tau_3(s[2])) / mp.mpf(2)

            sp12 = ((s[0][0], s[1][1]), (s[1][0], s[0][1]), s[2])
            sp23 = (s[0], (s[1][0], s[2][1]), (s[2][0], s[1][1]))
            sp13 = ((s[0][0], s[2][1]), s[1], (s[2][0], s[0][1]))

            fl12 = ((s[1][0], s[0][1]), (s[0][0], s[1][1]), s[2])
            fl23 = (s[0], (s[2][0], s[1][1]), (s[1][0], s[2][1]))
            fl13 = ((s[2][0], s[0][1]), s[1], (s[0][0], s[2][1]))

            s2_p = three_quarters * p_vec[s] + p_vec[sp12] + p_vec[sp23] + p_vec[sp13]
            i2_p = three_quarters * p_vec[s] + p_vec[fl12] + p_vec[fl23] + p_vec[fl13]
            s2_n = three_quarters * n_vec[s] + n_vec[sp12] + n_vec[sp23] + n_vec[sp13]
            i2_n = three_quarters * n_vec[s] + n_vec[fl12] + n_vec[fl23] + n_vec[fl13]
            s2_d = three_quarters * d_vec[s] + d_vec[sp12] + d_vec[sp23] + d_vec[sp13]
            i2_d = three_quarters * d_vec[s] + d_vec[fl12] + d_vec[fl23] + d_vec[fl13]

            max_casimir_residual = max(
                max_casimir_residual,
                abs(sz_val * p_vec[s] - half * p_vec[s]),
                abs(i3_val * p_vec[s] - half * p_vec[s]),
                abs(s2_p - three_quarters * p_vec[s]),
                abs(i2_p - three_quarters * p_vec[s]),
                abs(sz_val * n_vec[s] - half * n_vec[s]),
                abs(i3_val * n_vec[s] - (-half) * n_vec[s]),
                abs(s2_n - three_quarters * n_vec[s]),
                abs(i2_n - three_quarters * n_vec[s]),
                abs(s2_d - fifteen_quarters * d_vec[s]),
                abs(i2_d - fifteen_quarters * d_vec[s]),
            )

        # 4. Constituent quark spin fractions & tree-level axial charge g_A^(0)
        unnorm_delta_u_p = sum(
            p_vec[s]
            * (is_up(s[0]) * sigma_z(s[0]) + is_up(s[1]) * sigma_z(s[1]) + is_up(s[2]) * sigma_z(s[2]))
            * p_vec[s]
            for s in basis
        )
        unnorm_delta_d_p = sum(
            p_vec[s]
            * (is_down(s[0]) * sigma_z(s[0]) + is_down(s[1]) * sigma_z(s[1]) + is_down(s[2]) * sigma_z(s[2]))
            * p_vec[s]
            for s in basis
        )
        unnorm_axial_p = sum(
            p_vec[s]
            * (tau_3(s[0]) * sigma_z(s[0]) + tau_3(s[1]) * sigma_z(s[1]) + tau_3(s[2]) * sigma_z(s[2]))
            * p_vec[s]
            for s in basis
        )

        delta_u_p = unnorm_delta_u_p / norm_p
        delta_d_p = unnorm_delta_d_p / norm_p
        g_a_tree = unnorm_axial_p / norm_p

        # 5. Kummer-derived magnetic moments mu_p^(0), mu_n^(0) and ratio -3/2
        q_u = mp.mpf(2) / mp.mpf(3)
        q_d = mp.mpf(-1) / mp.mpf(3)

        def q_charge(q: QuarkState) -> mp.mpf:
            return q_u if q[0] == 0 else q_d

        unnorm_mu_p = sum(
            p_vec[s]
            * (q_charge(s[0]) * sigma_z(s[0]) + q_charge(s[1]) * sigma_z(s[1]) + q_charge(s[2]) * sigma_z(s[2]))
            * p_vec[s]
            for s in basis
        )
        unnorm_mu_n = sum(
            n_vec[s]
            * (q_charge(s[0]) * sigma_z(s[0]) + q_charge(s[1]) * sigma_z(s[1]) + q_charge(s[2]) * sigma_z(s[2]))
            * n_vec[s]
            for s in basis
        )

        mu_p_tree = unnorm_mu_p / norm_p
        mu_n_tree = unnorm_mu_n / norm_n
        mu_ratio_p_over_n_tree = mu_p_tree / mu_n_tree

        # Experimental nucleon magnetic moments in nuclear magnetons (CODATA 2022 / PDG 2024)
        mu_p_exp = mp.mpf("2.79284734463")
        mu_n_exp = mp.mpf("-1.91304273")
        mu_ratio_p_over_n_exp = mu_p_exp / mu_n_exp
        mu_ratio_rel_offset = (mu_ratio_p_over_n_tree - mu_ratio_p_over_n_exp) / abs(mu_ratio_p_over_n_exp)

        return {
            "colour_singlet_dim_lambda3_w3": 1,
            "spin_flavour_total_dim": len(basis),
            "sym3_su4_spin_flavour_dim": 20,
            "octet_spin_half_isospin_half_subspace_dim": 4,
            "decuplet_spin_three_halves_isospin_three_halves_subspace_dim": 16,
            "norm_proton_spin_up_sq": fmt(norm_p),
            "norm_neutron_spin_up_sq": fmt(norm_n),
            "norm_delta_plus_spin_up_sq": fmt(norm_d),
            "inner_proton_neutron": fmt(inner_pn),
            "inner_proton_delta_plus": fmt(inner_pd),
            "inner_neutron_delta_plus": fmt(inner_nd),
            "max_s3_permutation_residual": fmt(max_s3_residual),
            "max_spin_isospin_casimir_residual": fmt(max_casimir_residual),
            "unnormalized_proton_delta_u": fmt(unnorm_delta_u_p),
            "unnormalized_proton_delta_d": fmt(unnorm_delta_d_p),
            "unnormalized_proton_axial_charge": fmt(unnorm_axial_p),
            "derived_proton_delta_u": fmt(delta_u_p),
            "derived_proton_delta_d": fmt(delta_d_p),
            "derived_proton_total_quark_helicity": fmt(delta_u_p + delta_d_p),
            "derived_tree_axial_charge_g_a_0": fmt(g_a_tree),
            "derived_tree_g_a_minus_five_thirds": fmt(g_a_tree - mp.mpf(5) / mp.mpf(3)),
            "kummer_charge_u": fmt(q_u),
            "kummer_charge_d": fmt(q_d),
            "derived_tree_mu_p_dirac_units": fmt(mu_p_tree),
            "derived_tree_mu_n_dirac_units": fmt(mu_n_tree),
            "derived_tree_mu_p_over_mu_n": fmt(mu_ratio_p_over_n_tree),
            "derived_tree_mu_p_over_mu_n_minus_neg_three_halves": fmt(
                mu_ratio_p_over_n_tree - (mp.mpf(-3) / mp.mpf(2))
            ),
            "experimental_mu_p_nuclear_magnetons": fmt(mu_p_exp),
            "experimental_mu_n_nuclear_magnetons": fmt(mu_n_exp),
            "experimental_mu_p_over_mu_n": fmt(mu_ratio_p_over_n_exp),
            "tree_vs_experimental_mu_ratio_relative_offset": fmt(mu_ratio_rel_offset),
            "_raw_g_a_tree": g_a_tree,
            "_raw_mu_ratio_tree": mu_ratio_p_over_n_tree,
            "_raw_max_s3_residual": max_s3_residual,
            "_raw_max_casimir_residual": max_casimir_residual,
        }


# ── Section 2: H_3(q) & 64-State Borromean Axial Coupling Branch Census ──────
def evaluate_h3_hecke_borromean_at_q(
    q_hecke: mp.mpf, markov_denom: mp.mpf
) -> dict[str, mp.mpf]:
    """Evaluate the concrete 2x2 standard (2,1) representation matrices of H_3(q_hecke)
    from HeckeH3.lean lines 51-77 and 260-348:
      sigma_0 = [[q_hecke, 1], [0, -q_hecke^{-1}]],
      sigma_1 = [[-q_hecke^{-1}, 0], [1, q_hecke]],
      sigma_i^{-1} = sigma_i - (q_hecke - q_hecke^{-1}) I_2,
      h_rg = h_01 = sigma_0^{-1} sigma_1 sigma_0 sigma_1^{-1},
      h_gb = h_12 = sigma_1^{-1} sigma_0 sigma_1 sigma_0^{-1},
      h_rb = h_02 = sigma_0^{-1} sigma_1^{-1} sigma_0 sigma_1,
      beta_color = (1/3)(h_01 + h_12 + h_02),
      beta_Bor = (sigma_0 sigma_1^{-1})^3.
    Returns both ordinary matrix traces tr_std(M)/tr_sym(M) and cleared Markov
    traced volumes tracedVolCleared(M) = M_00 + markov_denom * M_10.
    """
    with mp.workdps(95):
        q_inv = mp.mpf(1) / q_hecke
        ha = q_hecke - q_inv

        sigma0 = [[q_hecke, mp.mpf(1)], [mp.mpf(0), -q_inv]]
        sigma1 = [[-q_inv, mp.mpf(0)], [mp.mpf(1), q_hecke]]
        eye2 = mat2_eye()
        sigma0_inv = mat2_add(sigma0, mat2_scale(-ha, eye2))
        sigma1_inv = mat2_add(sigma1, mat2_scale(-ha, eye2))

        # Half-Borromean matrices for the 3 colour tubes (HeckeH3.lean line 260)
        h_rg = mat2_mul(mat2_mul(mat2_mul(sigma0_inv, sigma1), sigma0), sigma1_inv)
        h_gb = mat2_mul(mat2_mul(mat2_mul(sigma1_inv, sigma0), sigma1), sigma0_inv)
        h_rb = mat2_mul(mat2_mul(mat2_mul(sigma0_inv, sigma1_inv), sigma0), sigma1)

        h_sum = mat2_add(mat2_add(h_rg, h_gb), h_rb)
        h_avg = mat2_scale(mp.mpf(1) / mp.mpf(3), h_sum)

        # Full 6-crossing Borromean braid beta_Bor = (sigma_0 sigma_1^{-1})^3 (HeckeH3.lean line 207)
        m_bor = mat2_mul(sigma0, sigma1_inv)
        beta_bor = mat2_mul(mat2_mul(m_bor, m_bor), m_bor)

        # Closed-form check for chi^{(2,1)}(beta_Bor) = 2 - 3 ha^4 - ha^6 (HeckeH3.lean line 189)
        chi_bor_trace = mat2_trace(beta_bor)
        chi_bor_poly = mp.mpf(2) - mp.mpf(3) * (ha ** 4) - (ha ** 6)
        chi_bor_residual = abs(chi_bor_trace - chi_bor_poly)

        # Ordinary matrix traces (tr_sym = 1 for each commutator; dimension of std is 2)
        tr_rg = mat2_trace(h_rg)
        tr_gb = mat2_trace(h_gb)
        tr_rb = mat2_trace(h_rb)
        tr_avg = mat2_trace(h_avg)

        # Cleared Markov traced volumes (TransferMatrix.lean line 191: M_00 + markov_denom * M_10)
        tvc_rg = mat2_traced_vol_cleared(h_rg, markov_denom)
        tvc_gb = mat2_traced_vol_cleared(h_gb, markov_denom)
        tvc_rb = mat2_traced_vol_cleared(h_rb, markov_denom)
        tvc_avg = mat2_traced_vol_cleared(h_avg, markov_denom)
        tvc_bor = mat2_traced_vol_cleared(beta_bor, markov_denom)

        five_thirds = mp.mpf(5) / mp.mpf(3)

        return {
            "tr_std_h_rg": tr_rg,
            "tr_std_h_gb": tr_gb,
            "tr_std_h_rb": tr_rb,
            "tr_std_color_avg": tr_avg,
            "g_a_ordinary_trace_h_rg": five_thirds * abs(tr_rg),
            "g_a_ordinary_trace_h_gb": five_thirds * abs(tr_gb),
            "g_a_ordinary_trace_h_rb": five_thirds * abs(tr_rb),
            "g_a_ordinary_trace_color_avg": five_thirds * abs(tr_avg),
            "g_a_ordinary_trace_color_avg_per_dim": five_thirds * abs(tr_avg) / mp.mpf(2),
            "tvc_h_rg": tvc_rg,
            "tvc_h_gb": tvc_gb,
            "tvc_h_rb": tvc_rb,
            "tvc_color_avg": tvc_avg,
            "g_a_cleared_markov_h_rg": five_thirds * abs(tvc_rg),
            "g_a_cleared_markov_h_gb": five_thirds * abs(tvc_gb),
            "g_a_cleared_markov_h_rb": five_thirds * abs(tvc_rb),
            "g_a_cleared_markov_color_avg": five_thirds * abs(tvc_avg),
            "chi_bor_trace": chi_bor_trace,
            "chi_bor_poly_residual": chi_bor_residual,
            "g_a_full_borromean_char_per_dim": five_thirds * (chi_bor_trace / mp.mpf(2)),
            "g_a_full_borromean_cleared_markov": five_thirds * abs(tvc_bor),
        }


def evaluate_64state_jimbo_r_borromean_at_q(q_val: mp.mpf) -> dict[str, mp.mpf]:
    """Evaluate the Jimbo U_q(sl_2) braided R-matrix action on the 64-state spin-flavour
    space (V_2^{spin} (x) V_2^{flav})^(x)3.

    On a single 2-dimensional factor V_2 (spin or flavour), the Jimbo R-matrix R_check(q)
    acting on V_2 (x) V_2 has eigenvalue +q on Sym^2(V_2) and -q^{-1} on Lambda^2(V_2):
      R_check(e_a (x) e_a) = q (e_a (x) e_a),
      R_check(e_0 (x) e_1) = e_1 (x) e_0,
      R_check(e_1 (x) e_0) = e_0 (x) e_1 + (q - q^{-1}) (e_1 (x) e_0).
    For the diagonal spin-flavour braid generator Sigma_i = R_check^{spin}_i (x) R_check^{flav}_i
    (and for the single-channel spin-only braid generator R_check^{spin}_i (x) P^{flav}_i),
    evaluates the axial-charge expectation value <psi_q | O_A | psi_q> / <psi_q | psi_q>
    after acting on |p_up> with the 3-fold colour-averaged half-Borromean operator and
    the full 6-crossing Borromean operator.
    """
    with mp.workdps(95):
        basis = enumerate_baryon_basis_64()
        q_inv = mp.mpf(1) / q_val
        ha = q_val - q_inv

        def apply_r2_pair(
            q_a: int, q_b: int, inv: bool
        ) -> list[tuple[int, int, mp.mpf]]:
            """Apply 2-state Jimbo R_check(q) (or R_check^{-1}(q)) to (q_a, q_b) in {0,1}^2."""
            if not inv:
                if q_a == q_b:
                    return [(q_a, q_b, q_val)]
                if q_a == 0 and q_b == 1:
                    return [(1, 0, mp.mpf(1))]
                return [(0, 1, mp.mpf(1)), (1, 0, ha)]
            else:
                if q_a == q_b:
                    return [(q_a, q_b, q_inv)]
                if q_a == 0 and q_b == 1:
                    return [(0, 1, -ha), (1, 0, mp.mpf(1))]
                return [(0, 1, mp.mpf(1))]

        def apply_gen_64(
            vec: dict[BaryonState64, mp.mpf],
            strand_idx: int,
            inv: bool,
            deform_flavour: bool,
        ) -> dict[BaryonState64, mp.mpf]:
            """Apply braid generator sigma_{strand_idx}^{+/-1} to a 64-state vector."""
            out = {s: mp.mpf(0) for s in basis}
            for s, amp in vec.items():
                if amp == mp.mpf(0):
                    continue
                if strand_idx == 0:
                    qa, qb, qc = s[0], s[1], s[2]
                else:
                    qa, qb, qc = s[1], s[2], s[0]

                spin_terms = apply_r2_pair(qa[1], qb[1], inv)
                if deform_flavour:
                    flav_terms = apply_r2_pair(qa[0], qb[0], inv)
                else:
                    flav_terms = [(qb[0], qa[0], mp.mpf(1))]

                for sa_new, sb_new, s_coeff in spin_terms:
                    for fa_new, fb_new, f_coeff in flav_terms:
                        qa_new: QuarkState = (fa_new, sa_new)
                        qb_new: QuarkState = (fb_new, sb_new)
                        if strand_idx == 0:
                            s_new: BaryonState64 = (qa_new, qb_new, qc)
                        else:
                            s_new = (qc, qa_new, qb_new)
                        out[s_new] += amp * s_coeff * f_coeff
            return out

        def apply_word_64(
            vec: dict[BaryonState64, mp.mpf],
            word: list[tuple[int, bool]],
            deform_flavour: bool,
        ) -> dict[BaryonState64, mp.mpf]:
            """Apply a sequence of generators [(strand_idx, is_inv), ...] left to right
            (so rightmost operator in the matrix product acts first)."""
            cur = dict(vec)
            for strand_idx, is_inv in reversed(word):
                cur = apply_gen_64(cur, strand_idx, is_inv, deform_flavour)
            return cur

        def axial_expectation(vec: dict[BaryonState64, mp.mpf]) -> mp.mpf:
            norm_sq = sum(vec[s] * vec[s] for s in basis)
            num = mp.mpf(0)
            for s in basis:
                op_a = mp.mpf(0)
                for qk in s:
                    t3 = mp.mpf(1) if qk[0] == 0 else mp.mpf(-1)
                    sz = mp.mpf(1) if qk[1] == 0 else mp.mpf(-1)
                    op_a += t3 * sz
                num += vec[s] * op_a * vec[s]
            return num / norm_sq

        p0 = {s: proton_spin_up_amp(s) for s in basis}

        # word-literal-ok: first-principles half-Borromean tube commutator h_01 = s0^-1 s1 s0 s1^-1 from HeckeH3.lean line 260
        w_rg = [(0, True), (1, False), (0, False), (1, True)]
        # word-literal-ok: first-principles half-Borromean tube commutator h_12 = s1^-1 s0 s1 s0^-1 from HeckeH3.lean line 261
        w_gb = [(1, True), (0, False), (1, False), (0, True)]
        # word-literal-ok: first-principles half-Borromean tube commutator h_02 = s0^-1 s1^-1 s0 s1 from HeckeH3.lean line 262
        w_rb = [(0, True), (1, True), (0, False), (1, False)]
        # word-literal-ok: first-principles 6-crossing Borromean braid (s0 s1^-1)^3 from HeckeH3.lean line 207
        w_bor = [(0, False), (1, True)] * 3

        results: dict[str, mp.mpf] = {}
        for mode_label, deform_flav in (
            ("spin_only_r_check", False),
            ("spin_and_flavour_r_check", True),
        ):
            v_rg = apply_word_64(p0, w_rg, deform_flav)
            v_gb = apply_word_64(p0, w_gb, deform_flav)
            v_rb = apply_word_64(p0, w_rb, deform_flav)
            v_avg = {
                s: (v_rg[s] + v_gb[s] + v_rb[s]) / mp.mpf(3)
                for s in basis
            }
            v_bor = apply_word_64(p0, w_bor, deform_flav)

            results[f"g_a_64state_{mode_label}_color_avg"] = axial_expectation(v_avg)
            results[f"g_a_64state_{mode_label}_full_borromean"] = axial_expectation(v_bor)

        return results


def compute_borromean_axial_coupling_branches() -> dict[str, object]:
    """Evaluate all candidate q-deformed Borromean axial coupling branches side-by-side
    across {q_0, q_2t, q_muon} and compare transparently against PDG g_A^{exp} = 1.2754(13).
    """
    with mp.workdps(95):
        pins = {
            "q_0_one_term_proton": q_at(95),
            "q_2t_two_term_borromean_proton": q_two_term_borromean_at(95),
            "q_muon_ideal_cal2": q_muon_at(95),
        }
        g_a_exp = mp.mpf("1.2754")
        g_a_exp_unc = mp.mpf("0.0013")
        five_thirds = mp.mpf(5) / mp.mpf(3)

        pin_evaluations: dict[str, object] = {}
        raw_q0_branches: dict[str, mp.mpf] = {}

        for pin_name, q_val in pins.items():
            h_val = q_val - mp.mpf(1) / q_val
            q2_int = q_int(2, q_val)
            z_d = (q_val ** 3) / (q_val ** 2 + mp.mpf(1))

            # Convention 1: q_Hecke = q, markov_denom = q^{1/2} + q^{-1/2} (TransferMatrix.lean line 49)
            markov_denom_q = mp.sqrt(q_val) + mp.mpf(1) / mp.sqrt(q_val)
            h3_conv_q = evaluate_h3_hecke_borromean_at_q(q_val, markov_denom_q)

            # Convention 2: t = q => q_Hecke = q^2, markov_denom = q + q^{-1}
            markov_denom_q2 = q_val + mp.mpf(1) / q_val
            h3_conv_q2 = evaluate_h3_hecke_borromean_at_q(q_val ** 2, markov_denom_q2)

            # 64-state Jimbo R-matrix evaluations
            r64 = evaluate_64state_jimbo_r_borromean_at_q(q_val)

            branches = {
                "branch_0_tree_su6_five_thirds": five_thirds,
                "branch_1a_h3_color_avg_ordinary_trace_conv_q": h3_conv_q["g_a_ordinary_trace_color_avg"],
                "branch_1a_single_tube_h_rg_ordinary_trace_conv_q": h3_conv_q["g_a_ordinary_trace_h_rg"],
                "branch_1a_single_tube_h_gb_ordinary_trace_conv_q": h3_conv_q["g_a_ordinary_trace_h_gb"],
                "branch_1a_single_tube_h_rb_ordinary_trace_conv_q": h3_conv_q["g_a_ordinary_trace_h_rb"],
                "branch_1b_h3_color_avg_cleared_markov_vol_conv_q": h3_conv_q["g_a_cleared_markov_color_avg"],
                "branch_1b_single_tube_h_rg_cleared_markov_conv_q": h3_conv_q["g_a_cleared_markov_h_rg"],
                "branch_1b_single_tube_h_gb_cleared_markov_conv_q": h3_conv_q["g_a_cleared_markov_h_gb"],
                "branch_1b_single_tube_h_rb_cleared_markov_conv_q": h3_conv_q["g_a_cleared_markov_h_rb"],
                "branch_1c_h3_color_avg_ordinary_trace_conv_q2": h3_conv_q2["g_a_ordinary_trace_color_avg"],
                "branch_1d_h3_color_avg_cleared_markov_vol_conv_q2": h3_conv_q2["g_a_cleared_markov_color_avg"],
                "branch_2_h3_full_6crossing_borromean_char_per_dim_conv_q": h3_conv_q[
                    "g_a_full_borromean_char_per_dim"
                ],
                "branch_3a_64state_jimbo_r_spin_only_color_avg": r64[
                    "g_a_64state_spin_only_r_check_color_avg"
                ],
                "branch_3b_64state_jimbo_r_spin_only_full_borromean": r64[
                    "g_a_64state_spin_only_r_check_full_borromean"
                ],
                "branch_3c_64state_jimbo_r_spin_and_flavour_color_avg": r64[
                    "g_a_64state_spin_and_flavour_r_check_color_avg"
                ],
                "branch_3d_64state_jimbo_r_spin_and_flavour_full_borromean": r64[
                    "g_a_64state_spin_and_flavour_r_check_full_borromean"
                ],
                "branch_4a_five_thirds_over_q2_int": five_thirds / q2_int,
                "branch_4b_five_thirds_over_q2_int_sq": five_thirds / (q2_int ** 2),
                "branch_4c_five_thirds_times_z_d": five_thirds * z_d,
                "branch_4d_five_thirds_times_one_minus_h_sq": five_thirds * (mp.mpf(1) - h_val ** 2),
            }

            if pin_name == "q_0_one_term_proton":
                raw_q0_branches = dict(branches)
                raw_q0_h3_conv_q = dict(h3_conv_q)

            formatted_branches: dict[str, object] = {}
            for b_name, b_val in branches.items():
                diff_exp = b_val - g_a_exp
                rel_exp = diff_exp / g_a_exp
                sigma_exp = diff_exp / g_a_exp_unc
                formatted_branches[b_name] = {
                    "g_a_value": fmt(b_val),
                    "offset_vs_pdg_2024": fmt(diff_exp),
                    "relative_offset_vs_pdg_2024": fmt(rel_exp),
                    "z_score_sigma_vs_pdg_2024": fmt(sigma_exp),
                }

            pin_evaluations[pin_name] = {
                "q_value": fmt(q_val),
                "hecke_amplitude_h": fmt(h_val),
                "q2_balanced_integer": fmt(q2_int),
                "convention_d_markov_z_d": fmt(z_d),
                "chi_borromean_polynomial_identity_residual": fmt(h3_conv_q["chi_bor_poly_residual"]),
                "branches": formatted_branches,
            }

        return {
            "pdg_2024_g_a_experimental": fmt(g_a_exp),
            "pdg_2024_g_a_uncertainty": fmt(g_a_exp_unc),
            "pin_evaluations": pin_evaluations,
            "transparency_and_anti_fitting_audit": {
                "tree_level_5_over_3_status": (
                    "Derived unconditionally in Lean 4 from Lambda^3 W_3 colour-singlet "
                    "antisymmetry and Sym^3(Q^4) S_3 spin-flavour symmetry on the 64-state "
                    "3-quark basis."
                ),
                "q_deformed_suppression_status": (
                    "All 20 candidate q-deformed Borromean trace and 64-state Jimbo R-matrix "
                    "evaluations are reported side-by-side across {q_0, q_2t, q_muon} without "
                    "post-hoc branch selection. In particular, the three individual colour tubes "
                    "(h_rg, h_gb, h_rb) differ from their 3-fold colour average, and cleared "
                    "Markov volume traces differ from ordinary matrix traces; selecting a "
                    "single q-suppression recipe solely by proximity to PDG 1.2754(13) is "
                    "prohibited by the zero-fitting discipline."
                ),
            },
            "_raw_q0_branches": raw_q0_branches,
            "_raw_q0_h3_conv_q": raw_q0_h3_conv_q,
        }


# ── Section 3: Polarized DIS Bjorken Sum Rule Gamma_1^{p-n}(Q^2) ─────────────
def solve_2loop_alpha_s_from_lambda(q_gev: mp.mpf, lambda_gev: mp.mpf, nf: int) -> mp.mpf:
    """Solve the exact 2-loop implicit RG invariant
      F(alpha_s; n_f) = (4 pi)/(b_0 alpha_s) - (b_1 / b_0^2) ln((4 pi)/(b_0 alpha_s) + b_1 / b_0^2)
                      = ln(Q^2 / Lambda^2)
    by Newton-Raphson iteration at 95 working dps.
    """
    with mp.workdps(95):
        b0 = mp.mpf(11) - (mp.mpf(2) / mp.mpf(3)) * mp.mpf(nf)
        b1 = mp.mpf(102) - (mp.mpf(38) / mp.mpf(3)) * mp.mpf(nf)
        c1 = b1 / (b0 ** 2)
        target = mp.log((q_gev / lambda_gev) ** 2)

        u = max(target + c1 * mp.log(max(target, mp.mpf(2))), mp.mpf(1))
        for _ in range(45):
            f_val = u - c1 * mp.log(u + c1) - target
            df_val = mp.mpf(1) - c1 / (u + c1)
            du = f_val / df_val
            u -= du
            if abs(du) < mp.mpf("1e-90"):
                break
        return (mp.mpf(4) * mp.pi) / (b0 * u)


def lambda_nf3_from_lambda_nf5(lambda5_gev: mp.mpf) -> mp.mpf:
    """Match 2-loop alpha_s continuously down across m_b = 4.18 GeV and m_c = 1.27 GeV
    to obtain Lambda^{(3)} from Lambda^{(5)}.
    """
    with mp.workdps(95):
        m_b = mp.mpf("4.18")
        m_c = mp.mpf("1.27")

        def rg_f(a_s: mp.mpf, nf: int) -> mp.mpf:
            b0 = mp.mpf(11) - (mp.mpf(2) / mp.mpf(3)) * mp.mpf(nf)
            b1 = mp.mpf(102) - (mp.mpf(38) / mp.mpf(3)) * mp.mpf(nf)
            c1 = b1 / (b0 ** 2)
            u = (mp.mpf(4) * mp.pi) / (b0 * a_s)
            return u - c1 * mp.log(u + c1)

        a_mb = solve_2loop_alpha_s_from_lambda(m_b, lambda5_gev, 5)
        lam4 = m_b * mp.exp(-rg_f(a_mb, 4) / mp.mpf(2))
        a_mc = solve_2loop_alpha_s_from_lambda(m_c, lam4, 4)
        lam3 = m_c * mp.exp(-rg_f(a_mc, 3) / mp.mpf(2))
        return lam3


def compute_bjorken_polarized_dis_sum_rule(
    g_a_branches_q0: dict[str, mp.mpf],
) -> dict[str, object]:
    """Evaluate the n_f = 3 MSbar perturbative QCD Bjorken polarized sum rule
      Gamma_1^{p-n}(Q^2) = (g_A / 6) [1 - (alpha_s / pi) - (43/12)(alpha_s / pi)^2 - c_3^{Bj}(3)(alpha_s / pi)^3]
    at Q^2 in {3, 5, 10} GeV^2 across the exact tree-level g_A^(0) = 5/3, the q-deformed
    H_3(q_0) branches, and experimental g_A^{exp} = 1.2754, and across three alpha_s(Q^2)
    scale inputs:
      1. QOU (3/2) m_pi = 209.355 MeV interpreted as Lambda_{MSbar}^{(5)} (giving Lambda^{(3)} = 353.39 MeV),
      2. QOU (3/2) m_pi = 209.355 MeV interpreted directly as Lambda_{MSbar}^{(3)},
      3. Empirical PDG alpha_s(M_Z) = 0.1180 reference (Lambda^{(3)} = 356.95 MeV).
    """
    with mp.workdps(95):
        # Exact n_f = 3 MSbar Bjorken radiative coefficients:
        #   c_1 = (3/4) C_F = 1 (Kodaira et al. 1979)
        #   c_2(n_f) = 55/12 - (1/3) n_f => c_2(3) = 43/12 (Gorishny & Larin 1986)
        #   c_3(n_f) leading-n_f^2 rational part = (115/648) n_f^2 = 115/72 at n_f = 3,
        #   within the full SU(3)_c 3-loop MSbar coefficient
        #   c_3^{Bj}(3) = 6011/144 + (3/2) zeta(3) - (45/2) zeta(5) = 20.215266419569...
        #   (Larin & Vermaseren 1991, Phys. Lett. B 259, 345, Eq. 11;
        #   Baikov, Chetyrkin, & Kuhn 2010, PRL 104, 132004).
        nf = mp.mpf(3)
        c1_bj = mp.mpf(1)
        c2_bj_nf3 = mp.mpf(55) / mp.mpf(12) - (mp.mpf(1) / mp.mpf(3)) * nf
        c3_bj_nf3_nf_sq_part = (mp.mpf(115) / mp.mpf(648)) * (nf ** 2)
        c3_bj_nf3_lv91 = (
            mp.mpf(6011) / mp.mpf(144)
            + (mp.mpf(3) / mp.mpf(2)) * mp.zeta(3)
            - (mp.mpf(45) / mp.mpf(2)) * mp.zeta(5)
        )

        # Three alpha_s(Q^2) scale inputs (all evaluated natively at 95 working dps)
        lambda_3half_mpi_gev = (mp.mpf(3) / mp.mpf(2)) * M_PI_PM_MEV_VALIDATION / mp.mpf(1000)
        lambda3_from_lam5 = lambda_nf3_from_lambda_nf5(lambda_3half_mpi_gev)
        b0_5 = mp.mpf(11) - (mp.mpf(2) / mp.mpf(3)) * mp.mpf(5)
        b1_5 = mp.mpf(102) - (mp.mpf(38) / mp.mpf(3)) * mp.mpf(5)
        c1_5 = b1_5 / (b0_5 ** 2)
        u_mz_pdg = (mp.mpf(4) * mp.pi) / (b0_5 * mp.mpf("0.1180"))
        rg_f5_mz = u_mz_pdg - c1_5 * mp.log(u_mz_pdg + c1_5)
        lam5_pdg = mp.mpf("91.1876") * mp.exp(-rg_f5_mz / mp.mpf(2))
        lambda3_pdg_ref = lambda_nf3_from_lambda_nf5(lam5_pdg)

        scale_inputs = {
            "qou_3half_mpi_as_lambda5": lambda3_from_lam5,
            "qou_3half_mpi_as_lambda3": lambda_3half_mpi_gev,
            "pdg_2024_alpha_s_mz_0p1180": lambda3_pdg_ref,
        }

        g_a_candidates = {
            "derived_tree_su6_five_thirds": mp.mpf(5) / mp.mpf(3),
            "h3_color_avg_ordinary_trace_conv_q": g_a_branches_q0[
                "branch_1a_h3_color_avg_ordinary_trace_conv_q"
            ],
            "h3_color_avg_cleared_markov_vol_conv_q": g_a_branches_q0[
                "branch_1b_h3_color_avg_cleared_markov_vol_conv_q"
            ],
            "h3_color_avg_cleared_markov_vol_conv_q2": g_a_branches_q0[
                "branch_1d_h3_color_avg_cleared_markov_vol_conv_q2"
            ],
            "64state_jimbo_r_spin_only_color_avg": g_a_branches_q0[
                "branch_3a_64state_jimbo_r_spin_only_color_avg"
            ],
            "five_thirds_over_q2_int_sq": g_a_branches_q0[
                "branch_4b_five_thirds_over_q2_int_sq"
            ],
            "pdg_2024_experimental_g_a": mp.mpf("1.2754"),
        }

        q_sq_points_gev2 = [
            ("Q2_3_GeV2", mp.mpf(3)),
            ("Q2_5_GeV2", mp.mpf(5)),
            ("Q2_10_GeV2", mp.mpf(10)),
        ]

        # Experimental COMPASS / JLab Bjorken sum rule benchmarks
        exp_benchmarks = {
            "Q2_3_GeV2": (mp.mpf("0.181"), mp.mpf("0.008"), "COMPASS 2016 / JLab CLAS 3 GeV^2"),
            "Q2_5_GeV2": (mp.mpf("0.182"), mp.mpf("0.007"), "SLAC E143/E155 / COMPASS 5 GeV^2"),
            "Q2_10_GeV2": (mp.mpf("0.186"), mp.mpf("0.007"), "SMC / COMPASS 10 GeV^2"),
        }

        evaluations_by_q2: dict[str, object] = {}
        raw_gamma_2loop_tree_q2_3 = mp.mpf(0)
        raw_gamma_2loop_tree_q2_10 = mp.mpf(0)

        for q2_label, q2_val in q_sq_points_gev2:
            q_gev = mp.sqrt(q2_val)
            exp_val, exp_unc, exp_ref = exp_benchmarks[q2_label]
            scale_table: dict[str, object] = {}

            for scale_name, lam3_gev in scale_inputs.items():
                a_s = solve_2loop_alpha_s_from_lambda(q_gev, lam3_gev, 3)
                a_over_pi = a_s / mp.pi

                corr_1loop = mp.mpf(1) - c1_bj * a_over_pi
                corr_2loop = corr_1loop - c2_bj_nf3 * (a_over_pi ** 2)
                corr_3loop = corr_2loop - c3_bj_nf3_lv91 * (a_over_pi ** 3)

                branch_gammas: dict[str, object] = {}
                for ga_name, ga_val in g_a_candidates.items():
                    uv_parton = ga_val / mp.mpf(6)
                    g1 = uv_parton * corr_1loop
                    g2 = uv_parton * corr_2loop
                    g3 = uv_parton * corr_3loop

                    if (
                        scale_name == "qou_3half_mpi_as_lambda5"
                        and ga_name == "derived_tree_su6_five_thirds"
                    ):
                        if q2_label == "Q2_3_GeV2":
                            raw_gamma_2loop_tree_q2_3 = g2
                        elif q2_label == "Q2_10_GeV2":
                            raw_gamma_2loop_tree_q2_10 = g2

                    branch_gammas[ga_name] = {
                        "g_a_input": fmt(ga_val),
                        "gamma_1_uv_parton_g_a_over_6": fmt(uv_parton),
                        "gamma_1_1loop": fmt(g1),
                        "gamma_1_2loop_exact_43_over_12": fmt(g2),
                        "gamma_1_3loop_lv91": fmt(g3),
                        "offset_3loop_vs_exp": fmt(g3 - exp_val),
                        "z_score_3loop_vs_exp": fmt((g3 - exp_val) / exp_unc),
                    }

                scale_table[scale_name] = {
                    "lambda_nf3_gev": fmt(lam3_gev),
                    "alpha_s_q2": fmt(a_s),
                    "alpha_s_over_pi": fmt(a_over_pi),
                    "radiative_factor_1loop": fmt(corr_1loop),
                    "radiative_factor_2loop": fmt(corr_2loop),
                    "radiative_factor_3loop": fmt(corr_3loop),
                    "g_a_branch_evaluations": branch_gammas,
                }

            evaluations_by_q2[q2_label] = {
                "Q2_GeV2": fmt(q2_val),
                "Q_GeV": fmt(q_gev),
                "experimental_gamma_1_p_minus_n": fmt(exp_val),
                "experimental_uncertainty": fmt(exp_unc),
                "experimental_reference": exp_ref,
                "alpha_s_scale_evaluations": scale_table,
            }

        return {
            "c1_bjorken_exact": fmt(c1_bj),
            "c2_bjorken_nf3_exact_43_over_12": fmt(c2_bj_nf3),
            "c3_bjorken_nf3_nf_sq_term_exact_115_over_72": fmt(c3_bj_nf3_nf_sq_part),
            "c3_bjorken_nf3_larin_vermaseren_1991": fmt(c3_bj_nf3_lv91),
            "uv_parton_limit_tree_five_eighteenths": fmt(mp.mpf(5) / mp.mpf(18)),
            "evaluations_by_q2": evaluations_by_q2,
            "_raw_c2_bj_nf3": c2_bj_nf3,
            "_raw_gamma_2loop_tree_q2_3": raw_gamma_2loop_tree_q2_3,
            "_raw_gamma_2loop_tree_q2_10": raw_gamma_2loop_tree_q2_10,
        }


# ── Section 4: Witness Builder & Main Entrypoint ─────────────────────────────
def main() -> int:
    with mp.workdps(95):
        part1 = compute_spin_flavour_64state_derivation()
        part2 = compute_borromean_axial_coupling_branches()
        part3 = compute_bjorken_polarized_dis_sum_rule(part2["_raw_q0_branches"])

        wb = WitnessBuilder(
            "baryon-axial-charge-and-bjorken-sum-rule",
            engine="mpmath",
        )

        # Assertion 1: Exact S_3 invariance and Casimir eigenvalues on the 64-state space
        max_s3_res = part1["_raw_max_s3_residual"]
        max_cas_res = part1["_raw_max_casimir_residual"]
        wb.add_assertion(
            name="s3_invariance_and_spin_isospin_casimir_exact_on_64_states",
            computed="1"
            if (max_s3_res == mp.mpf(0) and max_cas_res == mp.mpf(0))
            else "0",
            expected="1",
            tolerance="0",
        )

        # Assertion 2: Derived tree-level axial charge g_A^(0) = 5/3 from Lambda^3 W_3 antisymmetry
        g_a_tree = part1["_raw_g_a_tree"]
        five_thirds = mp.mpf(5) / mp.mpf(3)
        wb.add_assertion(
            name="derived_tree_axial_charge_equals_five_thirds_exact",
            computed=fmt(g_a_tree),
            expected=fmt(five_thirds),
            tolerance="1e-75",
        )

        # Assertion 3: Derived tree-level magnetic-moment ratio mu_p^(0)/mu_n^(0) = -3/2
        mu_ratio_tree = part1["_raw_mu_ratio_tree"]
        neg_three_halves = mp.mpf(-3) / mp.mpf(2)
        wb.add_assertion(
            name="derived_proton_neutron_magnetic_moment_ratio_equals_neg_three_halves_exact",
            computed=fmt(mu_ratio_tree),
            expected=fmt(neg_three_halves),
            tolerance="1e-75",
        )

        # Assertion 4: H_3(q) 6-crossing Borromean character identity chi^{(2,1)}(beta_Bor) = 2 - 3 h^4 - h^6
        h3_q0 = part2["_raw_q0_h3_conv_q"]
        chi_res = h3_q0["chi_bor_poly_residual"]
        wb.add_assertion(
            name="h3_borromean_character_polynomial_identity_exact",
            computed="1" if chi_res < mp.mpf("1e-75") else "0",
            expected="1",
            tolerance="0",
        )

        # Assertion 5: Bjorken 2-loop coefficient c_2^{Bj}(3) = 43/12 and asymptotic freedom monotonicity
        c2_bj = part3["_raw_c2_bj_nf3"]
        g2_q3 = part3["_raw_gamma_2loop_tree_q2_3"]
        g2_q10 = part3["_raw_gamma_2loop_tree_q2_10"]
        uv_lim = mp.mpf(5) / mp.mpf(18)
        wb.add_assertion(
            name="bjorken_sum_rule_c2_43_over_12_and_uv_monotonicity",
            computed="1"
            if (
                abs(c2_bj - mp.mpf(43) / mp.mpf(12)) < mp.mpf("1e-75")
                and mp.mpf(0) < g2_q3 < g2_q10 < uv_lim
            )
            else "0",
            expected="1",
            tolerance="0",
        )

        clean_part1 = {k: v for k, v in part1.items() if not k.startswith("_")}
        clean_part2 = {k: v for k, v in part2.items() if not k.startswith("_")}
        clean_part3 = {k: v for k, v in part3.items() if not k.startswith("_")}

        wb.add_data(
            "lean_companion_module",
            "folio/quantum-observable-universe/lean/QOU/StandardModel/"
            "BaryonSpinFlavourAxialAndBjorkenSumRule.lean",
        )
        wb.add_data("part1_spin_flavour_64state_derivation", clean_part1)
        wb.add_data("part2_borromean_axial_coupling_branch_census", clean_part2)
        wb.add_data("part3_bjorken_polarized_dis_sum_rule", clean_part3)

        q0_proton = q_at(95)
        q0_muon = q_muon_at(95)
        out_path = wb.save(
            q0_comparison(
                muon=q0_muon,
                proton=q0_proton,
                reason=(
                    "Evaluates all q-deformed H_3(q) and 64-state Jimbo R-matrix Borromean "
                    "axial-coupling branches side-by-side across {q_0, q_2t, q_muon} together "
                    "with the q-independent 64-state Sym^3(Q^4) derivation of g_A^(0) = 5/3 "
                    "and mu_p^(0)/mu_n^(0) = -3/2."
                ),
                dps=80,
            )
        )

        print(f"Wrote witness: {out_path}")
        print(f"  g_A^(0) derived tree-level : {clean_part1['derived_tree_axial_charge_g_a_0']}")
        print(f"  mu_p^(0)/mu_n^(0) derived  : {clean_part1['derived_tree_mu_p_over_mu_n']}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
