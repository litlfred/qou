#!/usr/bin/env python3
"""80-dps and exact-Fraction verification probe for `qou-o43i` and `qou-1a69`:

1. `qou-o43i` (`QOU.Nuclear.PauliLockSpinIsospinDiagnostic`):
   - Evaluates the corpus `H_2` / `H_3` isospin projector scalars `isoMuPlus(q_0, z_2)` and
     `isoMuMinus(q_0, z_2)` at the canonical proton pin `q_0 = q_at(80)` with two-row `SU(2)`
     Markov parameter `z_2 = q_0^3 / (q_0^2 + 1)`.
   - Verifies exact agreement (`< 1e-75`) against:
     * two-strand Wedderburn weights `(y_(2), y_(1,1))`,
     * three-strand radical-quotient branching `(1 - y_(2,1), y_(2,1))` (`y_(1,1,1) = 0`),
     * rational closed forms `(q_0^4 + q_0^2 + 1)/(q_0^2 + 1)^2` and `q_0^2/(q_0^2 + 1)^2`,
     * Pauli-locked equal-scalar product `q_0^2(q_0^4 + q_0^2 + 1)/(q_0^2 + 1)^4` and deficit
       `1 - 4 mu_+ mu_- = (q_0^4 + 1)^2 / (q_0^2 + 1)^4 > 0`,
     * reciprocal rescaling invariance `(mu_+ * t)(mu_- / t) == mu_+ * mu_-`,
     * single-bond band separation `mu_-(q_0) < z_2 - h_0 < z_2 < mu_+(q_0)`,
     * `A_5` (`[1, 3, 3, 4, 5]`, zero 2D irreps) vs binary icosahedral `2I` (`[1, 2, 3, 4, 5, 6, 4, 2, 3]`,
       two 2D spinors with `1 + 3 = 2^2`), and exact classical-spin `(3/4, 1/4)` vs `q_0`-isospin
       discrepancy `(q_0^2 - 1)^2 / (4 (q_0^2 + 1)^2) > 0` driving the linear S-wave channel defect
       `s_+ mu_- - s_- mu_+ = s_+ - mu_+`.

2. `qou-1a69` (`QOU.BraidsAndKnots.YoungDiagramTailSecondInstance`):
   - Verifies in exact `Fraction` and 80-dps `mpmath`:
     * full partition enumeration `nu_{n-1}(n)` for `n = 4..18`,
     * depth-1 3-carrier reduction (`[n]`, `1^n`, and `(a, 2, 1^c)`) for `n = 4..40`,
     * uniform `j = 0..n` symmetric `u(n, j) = j(n - j)` binomial-square sum and `u^0..u^3`
       moment formulas for `n = 4..40`,
     * closed form `(n - 1)(n - 4)(n^3 - 11n^2 + 32n - 30) * C(2n - 6, n - 3) / (3 * n!)` for `n = 4..40`,
     * exact row-by-row agreement across all 22 rows (`n = 4..25`) and sign-onset metadata
       (`zero_at = 4`, `negative_at = [5, 6, 7]`, `positive_from = 8`) of
       `computations/deltalambda/wlambda-covariance-epic-A2-tail-second-instance.witness.json`,
     * 80-dps isolation of the unique real root `rho = 7.077574223045071... in (7, 8)` of
       `x^3 - 11x^2 + 32x - 30 = (x - 8)((x - 2)^2 + (x - 1) + 5) + 34`.

Zero fitting, zero float64, zero empirical literals; canonical proton pin `q_0 = q_at(80)`.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402
from qou_substrate.constants import Q_MP, q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 80


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def fact_int(n: int) -> int:
    acc = 1
    for k in range(2, n + 1):
        acc *= k
    return acc


def comb_int(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for j in range(1, k + 1):
        num *= n - k + j
        den *= j
    return num // den


def partitions_of(n: int, max_part: int | None = None) -> list[list[int]]:
    if n == 0:
        return [[]]
    cap = n if max_part is None else min(n, max_part)
    out: list[list[int]] = []
    for first in range(cap, 0, -1):
        for tail in partitions_of(n - first, first):
            out.append([first] + tail)
    return out


def conj_part(lam: list[int]) -> list[int]:
    if not lam:
        return []
    return [sum(1 for x in lam if x > j) for j in range(lam[0])]


def hook_lengths_and_dim(lam: list[int]) -> tuple[list[int], int]:
    c = conj_part(lam)
    hooks: list[int] = []
    prod_h = 1
    for i, row in enumerate(lam):
        for j in range(row):
            h = row + c[j] - j - i - 1
            hooks.append(h)
            prod_h *= h
    return hooks, fact_int(sum(lam)) // prod_h


def omega3_int(n: int, lam: list[int]) -> int:
    csq = sum((j - i) ** 2 for i, row in enumerate(lam) for j in range(row))
    return csq - (n * (n - 1) // 2)


def sum_sq_upto(m: int) -> int:
    return m * (m + 1) * (2 * m + 1) // 6


def nu_depth_one_closed_form(n: int) -> Fraction:
    poly = (n - 1) * (n - 4) * (n ** 3 - 11 * (n ** 2) + 32 * n - 30)
    return Fraction(poly * comb_int(2 * n - 6, n - 3), 3 * fact_int(n))


def nu_depth_one_carrier_reduction(n: int) -> Fraction:
    fact = fact_int(n)
    c2 = n * (n - 1) // 2
    tot = Fraction(2 * (sum_sq_upto(n - 1) - c2), fact)
    for i in range(n - 3):
        a = i + 2
        c = n - 4 - i
        f_dim = fact // ((n - 1) * a * (c + 2) * fact_int(i) * fact_int(c))
        om = sum_sq_upto(a - 1) + sum_sq_upto(c + 1) - c2
        tot += Fraction(f_dim * f_dim * om, fact)
    return tot


def nu_depth_one_full_enum(n: int) -> Fraction:
    fact = fact_int(n)
    tot = Fraction(0)
    for lam in partitions_of(n):
        hooks, f_dim = hook_lengths_and_dim(lam)
        nv = sum(1 for h in hooks if h == n - 1)
        if nv:
            tot += Fraction(f_dim * f_dim * nv * omega3_int(n, lam), fact)
    return tot


def main() -> int:
    with mp.workdps(80):
        mp.dps = 80
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        h0 = q0 - qi0
        s2 = q0 + qi0
        z2 = (q0 ** 3) / (q0 ** 2 + mpf(1))

        wb = WitnessBuilder(
            "pauli-lock-and-d6-nu-onset",
            engine="mpmath (80 dps) + exact Fraction/int",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps and exact-Fraction verification for Pauli-lock spin/isospin diagnostic "
            "(qou-o43i, QOU.Nuclear.PauliLockSpinIsospinDiagnostic) and depth-1 nu_{n-1} "
            "closed form + n_1 = 8 sign onset against the A2 second-instance witness "
            "(qou-1a69, QOU.BraidsAndKnots.YoungDiagramTailSecondInstance)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("z_twoRow_proton_50dps", fmt50(z2))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ==================================================================
        # 1. qou-o43i: Pauli-Lock Spin/Isospin Diagnostic at 80 dps
        # ==================================================================
        mu_plus = (z2 + qi0) / s2
        mu_minus = (q0 - z2) / s2

        # Closed forms at z_2 = q^3 / (q^2 + 1)
        mu_plus_cf = (q0 ** 4 + q0 ** 2 + mpf(1)) / ((q0 ** 2 + mpf(1)) ** 2)
        mu_minus_cf = (q0 ** 2) / ((q0 ** 2 + mpf(1)) ** 2)

        # Solve H_2 Wedderburn system: y2 + y11 = 1, q*y2 - q^-1*y11 = z_2
        y2_h2 = (z2 + qi0) / (q0 + qi0)
        y11_h2 = mpf(1) - y2_h2

        # Solve H_3 Wedderburn system with alternating (1,1,1) radical y111 = 0:
        # y3 + 2*y21 = 1, q*y3 + (q - q^-1)*y21 = z_2  =>  y21 = (q - z_2)/(q + q^-1)
        y21_h3 = (q0 - z2) / (q0 + qi0)
        y3_h3 = mpf(1) - mpf(2) * y21_h3
        tr_e_h3 = (q0 ** 3) * y3_h3  # matches h_0 * z_2^2 + z_2 when y111 = 0
        tr_e_rhs = h0 * (z2 ** 2) + z2

        iso_closed_form_err = (
            abs((mu_plus + mu_minus) - mpf(1))
            + abs(mu_plus - mu_plus_cf)
            + abs(mu_minus - mu_minus_cf)
            + abs((y2_h2 * q0 - y11_h2 * qi0) - z2)
            + abs((q0 * y3_h3 + h0 * y21_h3) - z2)
            + abs(tr_e_h3 - tr_e_rhs)
        )
        wb.add_assertion(
            "isoMu_H2_H3_branching_and_twoRow_rational_closed_forms_at_q0",
            computed=iso_closed_form_err,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="PauliLockSpinIsospinDiagnostic.{isoMu_eq_h2_weights,isoMu_eq_h3_branching_of_radical,isoMuPlus_twoRow_closed_form,isoMuMinus_twoRow_closed_form}",
        )

        # Pauli-locked product, product deficit, and reciprocal rescaling invariance
        prod_pauli = mu_plus * mu_minus
        prod_cf = (q0 ** 2) * (q0 ** 4 + q0 ** 2 + mpf(1)) / ((q0 ** 2 + mpf(1)) ** 4)
        deficit_lhs = mpf(1) - mpf(4) * prod_pauli
        deficit_sq = (mu_plus - mu_minus) ** 2
        deficit_cf = ((q0 ** 4 + mpf(1)) ** 2) / ((q0 ** 2 + mpf(1)) ** 4)

        rescale_err = mpf(0)
        for exp_f in (-3, -1, 0, 2, 5):
            t_scale = q0 ** exp_f
            rescale_err = max(
                rescale_err,
                abs((mu_plus * t_scale) * (mu_minus / t_scale) - prod_pauli),
            )

        wb.add_assertion(
            "pauliLockedProduct_deficit_and_reciprocal_rescaling_invariance_at_q0",
            computed=abs(prod_pauli - prod_cf)
            + abs(deficit_lhs - deficit_sq)
            + abs(deficit_lhs - deficit_cf)
            + rescale_err,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="PauliLockSpinIsospinDiagnostic.{pauliLockedProduct_twoRow_closed_form,isoMu_twoRow_product_deficit,reciprocal_rescale_preserves_product}",
        )

        # Spin-side A_5 vs 2I representation dims & classical-spin (3/4, 1/4) vs q_0-isospin defect
        a5_dims = [1, 3, 3, 4, 5]
        two_i_dims = [1, 2, 3, 4, 5, 6, 4, 2, 3]
        rep_check = (
            abs(a5_dims.count(2) - 0)
            + abs(two_i_dims.count(2) - 2)
            + abs(sum(d * d for d in two_i_dims) - sum(d * d for d in a5_dims) - 60)
            + abs((a5_dims[0] + a5_dims[1]) - 4)
        )

        s_plus_classical = mpf(3) / mpf(4)
        s_minus_classical = mpf(1) / mpf(4)
        spin_iso_gap_cf = ((q0 ** 2 - mpf(1)) ** 2) / (
            mpf(4) * ((q0 ** 2 + mpf(1)) ** 2)
        )
        # Unit-sum linear channel difference: s_+ * mu_- - s_- * mu_+ == s_+ - mu_+
        swave_cross_diff = s_plus_classical * mu_minus - s_minus_classical * mu_plus
        swave_linear_diff = s_plus_classical - mu_plus

        # Band separation margins at q_0: mu_- < z_2 - h_0 < z_2 < mu_+
        band_floor = z2 - h0
        band_order_violation = (
            (mpf(0) if mu_minus < band_floor else mpf(1))
            + (mpf(0) if band_floor < z2 else mpf(1))
            + (mpf(0) if z2 < mu_plus else mpf(1))
            + (mpf(0) if spin_iso_gap_cf > mpf(0) else mpf(1))
        )

        wb.add_assertion(
            "A5_2I_spinor_obstruction_classical_spin_discrepancy_and_band_disjointness",
            computed=mpf(rep_check)
            + band_order_violation
            + abs((mu_plus - s_plus_classical) - spin_iso_gap_cf)
            + abs((s_minus_classical - mu_minus) - spin_iso_gap_cf)
            + abs(swave_cross_diff - swave_linear_diff),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="PauliLockSpinIsospinDiagnostic.{a5Irrep_no_two_dim_spinor,binaryIcosahedral_two_dim_spinors,unit_sum_channel_diff_eq,classicalSpin_eq_twoRowIso_iff_q_sq_eq_one,isoMu_disjoint_from_admissible_bond}",
        )

        # ==================================================================
        # 2. qou-1a69: Depth-1 nu_{n-1} Closed Form & n_1 = 8 Onset vs Witness
        # ==================================================================
        # Check exact Fraction agreement:
        # - full partition enumeration n = 4..18
        # - 3-carrier reduction n = 4..40
        # - uniform j = 0..n u-sum and u^0..u^3 moment formulas n = 4..40
        # - closed form n = 4..40
        enum_err = Fraction(0)
        for n in range(4, 19):
            enum_err += abs(nu_depth_one_full_enum(n) - nu_depth_one_closed_form(n))

        carrier_and_u_err = Fraction(0)
        for n in range(4, 41):
            cf = nu_depth_one_closed_form(n)
            red = nu_depth_one_carrier_reduction(n)
            carrier_and_u_err += abs(red - cf)

            # Check u^0..u^3 moments and uniform range(n + 1) identity at n = r + 3
            r_idx = n - 3
            u_moms = [
                sum(((j * (n - j)) ** p) * (comb_int(n, j) ** 2) for j in range(n + 1))
                for p in range(4)
            ]
            m0_f = comb_int(2 * n, n)
            m1_f = n * (n - 1) * comb_int(2 * n - 2, n - 1)
            m2_f = (n ** 2) * ((n - 1) ** 2) * comb_int(2 * n - 4, n - 2)
            m3_f = (n ** 2) * ((n - 1) ** 2) * (
                (r_idx + 1) * r_idx * comb_int(2 * r_idx, r_idx)
                + (r_idx + 2) * comb_int(2 * (r_idx + 1), r_idx + 1)
            )
            carrier_and_u_err += Fraction(
                abs(u_moms[0] - m0_f)
                + abs(u_moms[1] - m1_f)
                + abs(u_moms[2] - m2_f)
                + abs(u_moms[3] - m3_f),
                1,
            )

            unif_sum = 2 * (n - 1) * sum(
                ((j * (n - j) - (n - 1)) ** 2)
                * (n * (n - 2) - 3 * j * (n - j))
                * (comb_int(n, j) ** 2)
                for j in range(n + 1)
            )
            collapsed_int = (
                ((n - 1) ** 2)
                * 2
                * (n - 1)
                * (n - 4)
                * (n ** 3 - 11 * (n ** 2) + 32 * n - 30)
                * comb_int(2 * n - 6, n - 3)
            )
            carrier_and_u_err += Fraction(abs(unif_sum - collapsed_int), 1)

        wb.add_assertion(
            "nu_depthOne_full_enum_n4_18_and_uMoment_closed_form_collapse_n4_40",
            computed=mpf(enum_err.numerator) / mpf(enum_err.denominator)
            + mpf(carrier_and_u_err.numerator) / mpf(carrier_and_u_err.denominator),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="YoungDiagramTailSecondInstance.{uMoment1,uMoment2,uMoment3,sq_depthOne_int_sum_eq_u_sum,depthOne_int_sum_collapse,nuV_depthOne_closed_form}",
        )

        # Cross-check against computations/deltalambda/wlambda-covariance-epic-A2-tail-second-instance.witness.json
        ref_witness_path = (
            ROOT
            / "computations"
            / "deltalambda"
            / "wlambda-covariance-epic-A2-tail-second-instance.witness.json"
        )
        with open(ref_witness_path, "r", encoding="utf-8") as fh:
            ref_witness = json.load(fh)

        per_n_rows = ref_witness["per_n"]
        sign_meta = ref_witness["verdict"]["sign_onset"]
        witness_mismatch = Fraction(0)
        if len(per_n_rows) != 22:
            witness_mismatch += Fraction(1)
        if (
            sign_meta.get("zero_at") != 4
            or sign_meta.get("negative_at") != [5, 6, 7]
            or sign_meta.get("positive_from") != 8
            or sign_meta.get("onset_pattern_confirmed") is not True
        ):
            witness_mismatch += Fraction(1)

        for row in per_n_rows:
            n_val = int(row["n"])
            rec_frac = Fraction(row["nu_nm1"])
            cf_frac = nu_depth_one_closed_form(n_val)
            witness_mismatch += abs(rec_frac - cf_frac)
            exp_sign = (
                "0"
                if n_val == 4
                else ("-" if n_val in (5, 6, 7) else "+")
            )
            if row["sign"] != exp_sign:
                witness_mismatch += Fraction(1)

        # Isolate the unique real root rho in (7, 8) of x^3 - 11x^2 + 32x - 30 at 80 dps via Newton
        rho = mpf("7.08")
        for _ in range(30):
            f_rho = rho ** 3 - mpf(11) * (rho ** 2) + mpf(32) * rho - mpf(30)
            df_rho = mpf(3) * (rho ** 2) - mpf(22) * rho + mpf(32)
            rho = rho - f_rho / df_rho
        cubic_res = abs(rho ** 3 - mpf(11) * (rho ** 2) + mpf(32) * rho - mpf(30))
        decomp_res = abs(
            (rho ** 3 - mpf(11) * (rho ** 2) + mpf(32) * rho - mpf(30))
            - ((rho - mpf(8)) * ((rho - mpf(2)) ** 2 + (rho - mpf(1)) + mpf(5)) + mpf(34))
        )
        root_window_violation = (
            mpf(0) if (mpf(7) < rho and rho < mpf(8)) else mpf(1)
        )

        wb.add_assertion(
            "nu_depthOne_onset_n1_eq_8_matches_A2_second_instance_witness_and_cubic_root",
            computed=mpf(witness_mismatch.numerator) / mpf(witness_mismatch.denominator)
            + cubic_res
            + decomp_res
            + root_window_violation,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="YoungDiagramTailSecondInstance.{nuV_depthOne_witness_values,nuV_depthOne_pos_iff,nuV_depthOne_neg_iff,nuV_depthOne_eq_zero_iff,depthOneCubicFactor_decomp}",
        )

        wb.add_data(
            "pauli_lock_spin_isospin_q0",
            {
                "isoMuPlus_q0": fmt50(mu_plus),
                "isoMuMinus_q0": fmt50(mu_minus),
                "pauli_locked_product_q0": fmt50(prod_pauli),
                "product_deficit_1_minus_4prod_q0": fmt50(deficit_lhs),
                "classical_spin_vs_twoRow_iso_gap_q0": fmt50(spin_iso_gap_cf),
                "single_bond_band_floor_z_minus_h_q0": fmt50(band_floor),
                "single_bond_band_ceiling_z_q0": fmt50(z2),
                "a5_irrep_dims": a5_dims,
                "binary_icosahedral_irrep_dims": two_i_dims,
            },
        )
        wb.add_data(
            "nu_depthOne_onset_summary",
            {
                "closed_form": "(n - 1)*(n - 4)*(n^3 - 11*n^2 + 32*n - 30)*C(2*n - 6, n - 3)/(3*n!)",
                "values_n4_to_10": {
                    str(n): str(nu_depth_one_closed_form(n)) for n in range(4, 11)
                },
                "zero_at": 4,
                "negative_at": [5, 6, 7],
                "positive_onset_n1": 8,
                "cubic_real_root_50dps": fmt50(rho),
                "reference_witness_rows_verified": len(per_n_rows),
            },
        )

        wb.save({"q0Anchor": "proton"})
        print(
            f"[PASS] pauli_lock_and_d6_nu_onset_probe: "
            f"mu+(q0)={mp.nstr(mu_plus, 16)}, mu-(q0)={mp.nstr(mu_minus, 16)}, "
            f"spin_iso_gap={mp.nstr(spin_iso_gap_cf, 12)}, "
            f"nu_nm1(4..9)={[str(nu_depth_one_closed_form(n)) for n in range(4, 10)]}, "
            f"rho={mp.nstr(rho, 16)}"
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
