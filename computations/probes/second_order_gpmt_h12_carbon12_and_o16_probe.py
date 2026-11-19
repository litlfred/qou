#!/usr/bin/env python3
"""second_order_gpmt_h12_carbon12_and_o16_probe.py — 80-dps Second-Order (m=2) GPMT
Multi-Alpha Rectangular (k^4) Census, Telescoping Hook-Content Residue, Cabled Braid
Twist 8*C(k,2), and Pauli-Allowed Inter-Alpha Binding Audit (Bean qou-ozdk).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/SecondOrderGPMTCabledAlphaAndCarbon12.lean`
  (`namespace QOU.Nuclear.SecondOrderGPMTCabledAlphaAndCarbon12`).

STRICT ANTI-FITTING & PRECISION DISCIPLINE
------------------------------------------
1. ZERO fitting to AME2020 binding energies or separation thresholds; ZERO integer
   hunting; ZERO assertions gated on proximity to experimental `B_AME`.
2. ZERO binary64 (`float64`) arithmetic, ZERO `math` or `numpy` imports, ZERO
   `float(...)` or `complex(...)` calls, ZERO float literals, and ZERO raw JSON
   floats in the emitted witness (`witness_raw_float64_audit` = 0).
3. Evaluates at 80 decimal places across `q_0`, `q_2t`, and `q_muon`:
   - Part 1: Complete `H_{4k}(q)` (`k = 1..5`, `A = 4, 8, 12, 16, 20`) Pauli-allowed
     (`ell(lambda) <= 4`) Convention-D `(z - z_D)^m` root-multiplicity census (`m <= 2`
     universally), `SU(4)` Wigner-singlet uniqueness of `(k^4)`, exact telescoping
     quantum-factorial closed form `d_mod^{(2)}(k^4; q)`, and exact bridge to the
     Ocneanu/Wenzl `(z - z_D)^2`-stripped Markov residue across all 226 Pauli-allowed
     partitions plus independent 125-dps central-difference verification.
   - Part 2: Exact cabled inter-alpha twist identity `2*c(k^4) - k*2*c(1^4) = 8*C(k,2)`,
     multiplicative eigenvalue factorization `q^{2c(k^4)} = (q^{2c(1^4)})^k * (q^8)^{C(k,2)}`,
     column-by-column Pauli promotion content decomposition (`c(3^4) = c(1^4) = -6`,
     `c(4^4) = 0`), and Dehn-Sommerville net-triad invariance on 3D ball triangulations.
   - Part 3: Side-by-side 80-dps evaluation of all parameter-free inter-alpha strong
     and Coulomb binding mechanisms across `4He -> 8Be -> 12C -> 16O -> 20Ne` with
     complete candor on `8Be` unboundness vs `12C` and `16O` Borromean triad binding.
"""
from __future__ import annotations

from fractions import Fraction
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (str(ROOT), str(ROOT / "substrate"), str(ROOT / "audits"), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

from canonical_mass import e0_hadronic_tower_mev  # noqa: E402
from codata_constants import M_E_MEV, _ame_entry, ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from nuclear_3d_ball_manifold_triangulation_probe import (  # noqa: E402
    apollonian_3tree_triangulation,
    build_close_packed_shell_ball_triangulation,
    build_explicit_3d_fcc_delone_ball_complex,
)
from qou_substrate.constants import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    q0_comparison,
)


# ── Pure-Integer Combinatorics & Partition Helpers (Zero `math` Import) ──────
def _int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = k if k <= n - k else n - k
    acc = 1
    for i in range(1, k_use + 1):
        acc = (acc * (n - k_use + i)) // i
    return acc


def _int_factorial(n: int) -> int:
    acc = 1
    for k in range(2, n + 1):
        acc *= k
    return acc


def _partitions_descending(n: int) -> list[tuple[int, ...]]:
    def _gen(rem: int, max_part: int):
        if rem == 0:
            yield ()
            return
        for part in range(min(rem, max_part), 0, -1):
            for tail in _gen(rem - part, part):
                yield (part,) + tail

    return list(_gen(n, n))


def _pad4(shape: tuple[int, ...]) -> tuple[int, int, int, int]:
    padded = list(shape) + [0] * (4 - len(shape))
    return (padded[0], padded[1], padded[2], padded[3])


def _hook_length(shape: tuple[int, ...], r: int, c: int) -> int:
    arm = shape[r] - c - 1
    leg = sum(1 for r2 in range(r + 1, len(shape)) if shape[r2] > c)
    return arm + leg + 1


def _syt_dim(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    prod = 1
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            prod *= _hook_length(shape, r, c)
    return _int_factorial(n) // prod


def _rect_alpha_catalan_dim(k: int) -> int:
    """Lean `rectAlphaCatalanDim k = 12 * (4k)! / ((k+3)! (k+2)! (k+1)! k!)`."""
    return (12 * _int_factorial(4 * k)) // (
        _int_factorial(k + 3)
        * _int_factorial(k + 2)
        * _int_factorial(k + 1)
        * _int_factorial(k)
    )


def _su4_weyl_dim(l1: int, l2: int, l3: int, l4: int) -> int:
    """Classical SU(4) Weyl dimension of 4-row Young diagram (l1, l2, l3, l4)."""
    rows = (l1, l2, l3, l4)
    num = 1
    den = 1
    for i in range(4):
        for j in range(i + 1, 4):
            num *= rows[i] - rows[j] + (j - i)
            den *= j - i
    return num // den


def _content_sum(shape: tuple[int, ...]) -> int:
    total = 0
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            total += c - r
    return total


# ── Quantum Integers, Hook-Content Stripped Products & Ocneanu Weights ───────
def _q_int_signed(n: int, q: mp.mpf) -> mp.mpf:
    """Symmetric signed quantum integer `[n]_q = (q^n - q^{-n}) / (q - q^{-1})`."""
    if n == 0:
        return mp.mpf(0)
    if n < 0:
        return -_q_int_signed(-n, q)
    return (q ** n - q ** (-n)) / (q - mp.mpf(1) / q)


def _q_fact(n: int, q: mp.mpf) -> mp.mpf:
    """Symmetric quantum factorial `[n]_q! = prod_{m=1}^n [m]_q`, `[0]_q! = 1`."""
    acc = mp.mpf(1)
    for m in range(1, n + 1):
        acc *= _q_int_signed(m, q)
    return acc


def _hook_content_stripped_mod_dim(shape: tuple[int, ...], q: mp.mpf) -> tuple[int, mp.mpf]:
    """Direct box-by-box N=2 hook-content stripped quantum dimension:
        d_mod_hk^{(m)}(shape; q) = (prod_{2 + c - r != 0} [2 + c - r]_q) / (prod_{(r,c)} [h(r,c)]_q)
    matching Lean `rectAlphaStrippedContentProd / rectAlphaQHookProd` on `(k^4)`."""
    zero_mult = 0
    num = mp.mpf(1)
    den = mp.mpf(1)
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            h_rc = _hook_length(shape, r, c)
            den *= _q_int_signed(h_rc, q)
            shifted = 2 + c - r
            if shifted == 0:
                zero_mult += 1
            else:
                num *= _q_int_signed(shifted, q)
    return zero_mult, num / den


def _rect_alpha_dmod2_closed(k: int, q: mp.mpf) -> mp.mpf:
    """Lean `rectAlphaDMod2 q k = -([3]_q! [2]_q! [k-1]_q! [k-2]_q!) / ([k+3]_q! [k+2]_q!)`."""
    num = _q_fact(3, q) * _q_fact(2, q) * _q_fact(k - 1, q) * _q_fact(k - 2, q)
    den = _q_fact(k + 3, q) * _q_fact(k + 2, q)
    return -num / den


def _ocneanu_weight_at_z(shape: tuple[int, ...], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """Exact Ocneanu/Wenzl Markov weight `w_{shape}(q, z)`."""
    one = mp.mpf(1)
    num = one
    den = one
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            num *= (q ** (2 * r)) * (q ** 2 - one - q * z) + (q ** (2 * c + 1)) * z
            h_rc = _hook_length(shape, r, c)
            den *= (q ** (2 * h_rc)) - one
    return num / den


def _ocneanu_gpmt_residue_at_zd(shape: tuple[int, ...], q: mp.mpf) -> tuple[int, mp.mpf]:
    """Exact `(z - z_D)^m`-stripped Ocneanu/Wenzl residue `w_{shape}(q, z) / (z - z_D)^m |_{z=z_D}`."""
    one = mp.mpf(1)
    z_d = (q ** 3) / (q ** 2 + one)
    zero_mult = 0
    num_reg = one
    den = one
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            h_rc = _hook_length(shape, r, c)
            den *= (q ** (2 * h_rc)) - one
            if r - c == 2:
                zero_mult += 1
                num_reg *= (q ** (2 * c + 1)) - (q ** (2 * r + 1))
            else:
                num_reg *= (
                    (q ** (2 * r)) * (q ** 2 - one - q * z_d)
                    + (q ** (2 * c + 1)) * z_d
                )
    return zero_mult, num_reg / den


# ── Part 1: Complete H_{4k}(q) Pauli-Allowed Census & Telescoping Residue ────
def _evaluate_part1_at_pin(q: mp.mpf, pin_label: str) -> dict[str, object]:
    with mp.workdps(95):
        q2 = _q_int_signed(2, q)
        z_d = (q ** 3) / (q ** 2 + mp.mpf(1))

        by_k: dict[str, object] = {}
        pauli_cap_ok = True
        stratum_iff_ok = True
        su4_singlet_unique_ok = True
        max_telescoping_gap = mp.mpf(0)
        max_ocneanu_bridge_gap = mp.mpf(0)
        rect_negativity_ok = True

        for k in (1, 2, 3, 4, 5):
            A = 4 * k
            all_parts = _partitions_descending(A)
            pauli_parts = [sh for sh in all_parts if len(sh) <= 4]

            hist_pauli = {0: 0, 1: 0, 2: 0}
            sum_m0_prob = mp.mpf(0)
            sum_m1_ocn_abs = mp.mpf(0)
            sum_m2_ocn_abs = mp.mpf(0)
            sum_m2_hk_abs = mp.mpf(0)
            m2_table: list[dict[str, object]] = []

            for sh in pauli_parts:
                l1, l2, l3, l4 = _pad4(sh)
                d_syt = _syt_dim(sh)
                su4_d = _su4_weyl_dim(l1, l2, l3, l4)
                kap = _content_sum(sh)

                # Verify SU(4) Wigner singlet uniqueness among Pauli-allowed shapes of size 4k
                if (su4_d == 1) != (sh == (k, k, k, k)):
                    su4_singlet_unique_ok = False

                m_hk, d_hk = _hook_content_stripped_mod_dim(sh, q)
                m_ocn, w_res = _ocneanu_gpmt_residue_at_zd(sh, q)

                if m_hk != m_ocn or m_ocn not in (0, 1, 2):
                    pauli_cap_ok = False
                else:
                    hist_pauli[m_ocn] += 1

                # Verify Lean Section 2 stratum iff characterizations
                expected_m = (1 if l3 >= 1 else 0) + (1 if l4 >= 2 else 0)
                if m_ocn != expected_m:
                    stratum_iff_ok = False

                # Universal bridge: w_res == (-1)^m * [2]_q^{2m - A} * d_hk
                sign_m = mp.mpf(-1) if (m_ocn % 2 == 1) else mp.mpf(1)
                expected_w_res = sign_m * (q2 ** (2 * m_ocn - A)) * d_hk
                bridge_gap = abs(w_res - expected_w_res)
                if bridge_gap > max_ocneanu_bridge_gap:
                    max_ocneanu_bridge_gap = bridge_gap

                if m_ocn == 0:
                    sum_m0_prob += mp.mpf(d_syt) * w_res
                elif m_ocn == 1:
                    sum_m1_ocn_abs += mp.mpf(d_syt) * abs(w_res)
                elif m_ocn == 2:
                    sum_m2_ocn_abs += mp.mpf(d_syt) * abs(w_res)
                    sum_m2_hk_abs += mp.mpf(d_syt) * abs(d_hk)
                    m2_table.append(
                        {
                            "partition": list(sh),
                            "syt_dim": d_syt,
                            "su4_spin_isospin_dim": su4_d,
                            "content_sum": kap,
                            "full_twist_exponent": 2 * kap,
                            "d_mod2_hook_content": fmt(d_hk),
                            "w_mod2_ocneanu_residue": fmt(w_res),
                        }
                    )

            # Rectangular (k^4) specific checks
            rect_sh = (k, k, k, k)
            m_rect, d_hk_rect = _hook_content_stripped_mod_dim(rect_sh, q)
            _, w_res_rect = _ocneanu_gpmt_residue_at_zd(rect_sh, q)
            d_syt_rect = _syt_dim(rect_sh)
            d_cat_rect = _rect_alpha_catalan_dim(k)
            if d_syt_rect != d_cat_rect:
                su4_singlet_unique_ok = False

            rect_entry: dict[str, object] = {
                "partition": [k, k, k, k],
                "syt_dim_catalan4": d_syt_rect,
                "su4_weyl_dim": _su4_weyl_dim(k, k, k, k),
                "content_sum": _content_sum(rect_sh),
                "full_twist_exponent": 2 * _content_sum(rect_sh),
                "zD_zero_multiplicity": m_rect,
                "d_mod_hook_content": fmt(d_hk_rect),
                "w_mod_ocneanu_residue": fmt(w_res_rect),
                "plancherel_syt_mul_abs_d_mod_hk": fmt(mp.mpf(d_syt_rect) * abs(d_hk_rect)),
                "plancherel_syt_mul_abs_w_ocneanu": fmt(mp.mpf(d_syt_rect) * abs(w_res_rect)),
            }

            if k >= 2:
                d_closed = _rect_alpha_dmod2_closed(k, q)
                if not (d_closed < mp.mpf(0) and m_rect == 2):
                    rect_negativity_ok = False
                tel_gap = abs(d_hk_rect - d_closed)
                ocn_closed_gap = abs(w_res_rect - (q2 ** (4 - 4 * k)) * d_closed)
                max_telescoping_gap = max(max_telescoping_gap, tel_gap, ocn_closed_gap)
                rect_entry["d_mod2_telescoping_closed"] = fmt(d_closed)
                rect_entry["telescoping_vs_box_product_gap"] = fmt(tel_gap)
                rect_entry["ocneanu_vs_qInt2_scaled_closed_gap"] = fmt(ocn_closed_gap)

            by_k[f"k{k}_A{A}"] = {
                "k_alpha": k,
                "A": A,
                "total_partitions": len(all_parts),
                "pauli_allowed_ell_le_4_count": len(pauli_parts),
                "pauli_zD_multiplicity_histogram": {
                    str(m_key): m_cnt for m_key, m_cnt in sorted(hist_pauli.items())
                },
                "two_row_m0_probability_sum": fmt(sum_m0_prob),
                "m1_stratum_syt_weighted_ocneanu_abs_sum": fmt(sum_m1_ocn_abs),
                "m2_stratum_syt_weighted_ocneanu_abs_sum": fmt(sum_m2_ocn_abs),
                "m2_stratum_syt_weighted_hk_abs_sum": fmt(sum_m2_hk_abs),
                "unique_su4_singlet_rectangle": rect_entry,
                "m2_pauli_allowed_shapes": m2_table,
            }

        # Independent 125-dps central-difference verification of `(z - z_D)^2` residue on (2^4), (3^4), (4^4)
        max_central_diff_gap = mp.mpf(0)
        with mp.workdps(130):
            q_hi = +q
            zd_hi = (q_hi ** 3) / (q_hi ** 2 + mp.mpf(1))
            eps = mp.mpf(10) ** (-30)
            for k_cd in (2, 3, 4):
                sh_cd = (k_cd, k_cd, k_cd, k_cd)
                # At z_D, w(z_D) = 0 and w'(z_D) = 0 because m = 2, so:
                #   (w(z_D + eps) + w(z_D - eps)) / (2 * eps^2) = w^{(2)}_res + O(eps^2)
                w_plus = _ocneanu_weight_at_z(sh_cd, q_hi, zd_hi + eps)
                w_minus = _ocneanu_weight_at_z(sh_cd, q_hi, zd_hi - eps)
                w_at_zd = _ocneanu_weight_at_z(sh_cd, q_hi, zd_hi)
                cd_approx = (w_plus + w_minus - mp.mpf(2) * w_at_zd) / (mp.mpf(2) * (eps ** 2))
                _, exact_res_hi = _ocneanu_gpmt_residue_at_zd(sh_cd, q_hi)
                rel_cd_err = abs(cd_approx - exact_res_hi) / abs(exact_res_hi)
                if rel_cd_err > max_central_diff_gap:
                    max_central_diff_gap = rel_cd_err
        max_central_diff_gap = +max_central_diff_gap

        # Classical q -> 1 rational benchmark checks from Lean Section 3
        dmod2_q1_k2 = Fraction(-(_int_factorial(3) * _int_factorial(2)), _int_factorial(5) * _int_factorial(4))
        dmod2_q1_k3 = Fraction(-(_int_factorial(3) * (_int_factorial(2) ** 2)), _int_factorial(6) * _int_factorial(5))
        dmod2_q1_k4 = Fraction(-((_int_factorial(3) ** 2) * (_int_factorial(2) ** 2)), _int_factorial(7) * _int_factorial(6))
        planch_q1_k2 = _rect_alpha_catalan_dim(2) * (-dmod2_q1_k2)
        planch_q1_k3 = _rect_alpha_catalan_dim(3) * (-dmod2_q1_k3)
        planch_q1_k4 = _rect_alpha_catalan_dim(4) * (-dmod2_q1_k4)
        q1_limits_ok = (
            dmod2_q1_k2 == Fraction(-1, 240)
            and dmod2_q1_k3 == Fraction(-1, 3600)
            and dmod2_q1_k4 == Fraction(-1, 25200)
            and planch_q1_k2 == Fraction(7, 120)
            and planch_q1_k3 == Fraction(77, 600)
            and planch_q1_k4 == Fraction(143, 150)
        )

        return {
            "pin_label": pin_label,
            "q": fmt(q),
            "z_D": fmt(z_d),
            "max_telescoping_closed_form_gap": fmt(max_telescoping_gap),
            "max_ocneanu_hook_bridge_gap_all_226_pauli_shapes": fmt(max_ocneanu_bridge_gap),
            "max_central_diff_130dps_rel_err_k2_k3_k4": fmt(max_central_diff_gap),
            "classical_q_eq_1_benchmarks": {
                "dMod2_24": f"{dmod2_q1_k2.numerator}/{dmod2_q1_k2.denominator}",
                "dMod2_34": f"{dmod2_q1_k3.numerator}/{dmod2_q1_k3.denominator}",
                "dMod2_44": f"{dmod2_q1_k4.numerator}/{dmod2_q1_k4.denominator}",
                "plancherel_24": f"{planch_q1_k2.numerator}/{planch_q1_k2.denominator}",
                "plancherel_34": f"{planch_q1_k3.numerator}/{planch_q1_k3.denominator}",
                "plancherel_44": f"{planch_q1_k4.numerator}/{planch_q1_k4.denominator}",
            },
            "census_by_k": by_k,
            "_raw_checks": {
                "pauli_cap_and_strata_ok": (
                    pauli_cap_ok
                    and stratum_iff_ok
                    and su4_singlet_unique_ok
                    and rect_negativity_ok
                    and q1_limits_ok
                ),
                "max_telescoping_and_bridge_gap": max(
                    max_telescoping_gap, max_ocneanu_bridge_gap
                ),
                "max_central_diff_gap": max_central_diff_gap,
            },
        }


# ── Part 2: Cabled Twist 8*C(k,2), Pauli Column Shifts & Simplicial Geometry ─
def _evaluate_part2_cabling_and_geometry(q: mp.mpf) -> dict[str, object]:
    with mp.workdps(95):
        c1 = _content_sum((1, 1, 1, 1))  # -6
        cabling_rows: list[dict[str, object]] = []
        cabling_exact_ok = True
        max_zpow_gap = mp.mpf(0)
        ds_invariance_ok = True

        for k in (1, 2, 3, 4, 5):
            A = 4 * k
            sh = (k, k, k, k)
            ck = _content_sum(sh)
            two_ck = 2 * ck
            internal_exp = k * (2 * c1)
            inter_exp = two_ck - internal_exp
            eight_choose_2 = 8 * _int_comb(k, 2)
            col_contents = [4 * c_idx - 6 for c_idx in range(k)]

            if (
                ck != 2 * k * (k - 4)
                or inter_exp != eight_choose_2
                or sum(col_contents) != ck
            ):
                cabling_exact_ok = False

            # Multiplicative central full-twist factorization:
            #   q^{2 c(k^4)} == (q^{2 c(1^4)})^k * (q^8)^{C(k, 2)}
            lhs_zpow = q ** two_ck
            rhs_zpow = ((q ** (2 * c1)) ** k) * ((q ** 8) ** _int_comb(k, 2))
            zpow_gap = abs(lhs_zpow - rhs_zpow)
            if zpow_gap > max_zpow_gap:
                max_zpow_gap = zpow_gap

            # Simplicial complexes at A = 4k
            t_tree = apollonian_3tree_triangulation(A)
            t_kuhn = build_explicit_3d_fcc_delone_ball_complex(A)
            t_shell = build_close_packed_shell_ball_triangulation(A)

            df_tree = (
                int(t_tree["f1"]) - 6 * k,
                int(t_tree["f2"]) - 4 * k,
                int(t_tree["f3"]) - k,
            )
            df_kuhn = (
                int(t_kuhn["f1"]) - 6 * k,
                int(t_kuhn["f2"]) - 4 * k,
                int(t_kuhn["f3"]) - k,
            )
            df_shell = (
                int(t_shell["f1"]) - 6 * k,
                int(t_shell["f2"]) - 4 * k,
                int(t_shell["f3"]) - k,
            )

            # Dehn-Sommerville net-triad invariant Delta(f_2 - 2 f_3) = 2(k - 1) whenever f0_int == 0
            if int(t_tree["f0_int"]) == 0 and (df_tree[1] - 2 * df_tree[2]) != 2 * (k - 1):
                ds_invariance_ok = False
            if int(t_kuhn["f0_int"]) == 0 and (df_kuhn[1] - 2 * df_kuhn[2]) != 2 * (k - 1):
                ds_invariance_ok = False

            # Coarse-grained k-alpha Apollonian cluster simplex counts
            f1_cl = 0 if k <= 1 else (1 if k == 2 else 3 * k - 6)
            f2_cl = 0 if k <= 2 else 3 * k - 8
            f3_cl = 0 if k <= 3 else k - 3
            net_cl_triads = f2_cl - 2 * f3_cl
            if net_cl_triads != max(0, k - 2):
                ds_invariance_ok = False

            cabling_rows.append(
                {
                    "k_alpha": k,
                    "A": A,
                    "content_sum_c_k4": ck,
                    "column_pauli_content_progression": col_contents,
                    "total_full_twist_exp_2c_k4": two_ck,
                    "internal_k_alpha_twist_exp": internal_exp,
                    "cabled_inter_alpha_twist_exp_8_choose_k_2": inter_exp,
                    "multiplicative_zpow_factorization_gap": fmt(zpow_gap),
                    "cluster_simplex_f_vector": [k, f1_cl, f2_cl, f3_cl],
                    "cluster_net_h3_gpmt_triads_f2_minus_2f3": net_cl_triads,
                    "nucleon_excess_vs_k_K4_apollonian_3tree": list(df_tree),
                    "nucleon_excess_vs_k_K4_3D_kuhn_ball": list(df_kuhn),
                    "nucleon_excess_vs_k_K4_3D_shell_ball": list(df_shell),
                    "kuhn_f0_int_buried_vertices": int(t_kuhn["f0_int"]),
                }
            )

        # Spin-isospin tensor cube (C^4)^{x 3} S_3 decomposition across 3 saturated [1^4] alpha cells:
        #   dim Sym^3(C^4) = C(6, 3) = 20,  2 * dim S^{(2,1)}(C^4) = 2 * 20 = 40,  dim Lambda^3(C^4) = C(4, 3) = 4.
        dim_sym3_c4 = _int_comb(6, 3)
        dim_21_total_c4 = 2 * 20
        dim_alt3_c4 = _int_comb(4, 3)
        distinct_ordered_triples = 4 * 3 * 2  # 24 = 2 * 12
        distinct_unoriented_cycles = distinct_ordered_triples // 2  # 12
        antisym_pair_fraction = Fraction(_int_comb(4, 2), 4 * 4)  # 6/16 = 3/8

        spin_iso_ok = (
            dim_sym3_c4 + dim_21_total_c4 + dim_alt3_c4 == 64
            and distinct_ordered_triples == 24
            and distinct_unoriented_cycles == 12
            and antisym_pair_fraction == Fraction(3, 8)
        )

        # Lean Section 4 specific identities for 12C (k=3) and 16O (k=4)
        c3 = _content_sum((3, 3, 3, 3))
        c4 = _content_sum((4, 4, 4, 4))
        c12_o16_ok = (c3 == c1 == -6) and (c4 == 0)

        return {
            "cabled_twist_rows": cabling_rows,
            "three_alpha_spin_isospin_cube_decomposition": {
                "total_cross_cluster_flavor_triples_4_cubed": 64,
                "dim_Sym3_C4_spatial_antisym": dim_sym3_c4,
                "dim_two_copies_S21_C4_mixed": dim_21_total_c4,
                "dim_Lambda3_C4_spatial_swave_allowed": dim_alt3_c4,
                "distinct_flavor_ordered_triples": distinct_ordered_triples,
                "distinct_flavor_unoriented_triad_channels": distinct_unoriented_cycles,
                "two_alpha_Lambda2_C4_pair_fraction": f"{antisym_pair_fraction.numerator}/{antisym_pair_fraction.denominator}",
            },
            "_raw_checks": {
                "cabling_and_spin_iso_ok": cabling_exact_ok and spin_iso_ok and c12_o16_ok,
                "max_zpow_gap": max_zpow_gap,
                "ds_invariance_ok": ds_invariance_ok,
            },
        }


# ── Part 3: Side-by-Side 80-dps Multi-Alpha Binding Audit (4He..20Ne) ────────
def _ame_sigma_total_mev(Z: int, A: int) -> mp.mpf:
    entry = _ame_entry(Z, A)
    unc_kev = entry.get("binding_energy_per_A_unc_keV")
    if unc_kev is None:
        return mp.mpf(0)
    return mp.mpf(str(unc_kev)) * mp.mpf(A) / mp.mpf(1000)


def _evaluate_part3_binding_models(q: mp.mpf, pin_label: str) -> dict[str, object]:
    with mp.workdps(95):
        one = mp.mpf(1)
        qi = one / q
        h = q - qi
        me = mp.mpf(str(M_E_MEV))
        e0_bare = me / (q * (q - one))
        e0_tower = mp.mpf(str(e0_hadronic_tower_mev(q=q)))

        z_d = (q ** 3) / (q ** 2 + one)
        z_gg = z_d - h / mp.mpf(2)
        q2 = _q_int_signed(2, q)
        q3 = _q_int_signed(3, q)

        q2_1 = q ** 2 + one
        q4_1 = q ** 4 + one
        q4_2_1 = q ** 4 + q ** 2 + one
        h4_mod_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        mu3_gpmt = one / (q2 * q3)  # |d_mod(1,1,1)|
        casimir_gpmt_h4 = (
            mp.mpf(12)
            * (q ** 3)
            * (q ** 8 + mp.mpf(2) * (q ** 6) + mp.mpf(4) * (q ** 4) + mp.mpf(2) * (q ** 2) + one)
            / h4_mod_denom
        )

        # Fundamental scales (evaluated at tower E_0, with bare E_0 also recorded on 8Be threshold)
        b2_d_bare = e0_bare * mp.log(one / z_d)
        b2_d_tower = e0_tower * mp.log(one / z_d)
        b2_gg_tower = e0_tower * mp.log(one / z_gg)
        w3_tower = e0_tower * mu3_gpmt
        w4_h3_tower = -mp.mpf(2) * w3_tower

        # Intra-alpha cell baselines:
        #   - Lane N1 H_4 full-twist cell B1: 6 * b2_logGG + E_0 * casimirGPMTRow3(q)
        #   - Lane N2 1-crossing K_4 cell A:  6 * b2_logD + 4 * w3 + w4_H3 = 6 * b2_logD + 2 * w3
        cell_n1_b1_tower = mp.mpf(6) * b2_gg_tower + e0_tower * casimir_gpmt_h4
        cell_n2_1x_tower = mp.mpf(6) * b2_d_tower + mp.mpf(2) * w3_tower

        alpha_nuclei = [
            ("4He", 1, 2, 2),
            ("8Be", 2, 4, 4),
            ("12C", 3, 6, 6),
            ("16O", 4, 8, 8),
            ("20Ne", 5, 10, 10),
        ]

        b_ame_he4 = mp.mpf(str(ame_binding_mev(2, 4)))
        ec_he4 = mp.mpf(str(coulomb_energy_mev(2, 4, q=q)))
        b_str_exp_he4 = b_ame_he4 + ec_he4

        # Check Borromean Hoyle threshold window on 8Be (k=2) vs 12C (k=3)
        ec_be8 = mp.mpf(str(coulomb_energy_mev(4, 8, q=q)))
        d_ec_be8 = ec_be8 - mp.mpf(2) * ec_he4
        db_be8_bare = b2_d_bare - d_ec_be8
        db_be8_tower = b2_d_tower - d_ec_be8

        per_nucleus: dict[str, object] = {}
        for name, k, Z, N in alpha_nuclei:
            A = Z + N
            b_ame = mp.mpf(str(ame_binding_mev(Z, A)))
            sig_ame = _ame_sigma_total_mev(Z, A)
            ec = mp.mpf(str(coulomb_energy_mev(Z, A, q=q)))
            b_str_exp = b_ame + ec

            d_b_exp = b_ame - mp.mpf(k) * b_ame_he4
            d_ec = ec - mp.mpf(k) * ec_he4
            d_b_str_exp = b_str_exp - mp.mpf(k) * b_str_exp_he4

            f1_cl = 0 if k <= 1 else (1 if k == 2 else 3 * k - 6)
            f2_cl = 0 if k <= 2 else 3 * k - 8
            f3_cl = 0 if k <= 3 else k - 3
            net_cl_triads = f2_cl - 2 * f3_cl

            t_kuhn = build_explicit_3d_fcc_delone_ball_complex(A)
            df1_k = int(t_kuhn["f1"]) - 6 * k
            df2_k = int(t_kuhn["f2"]) - 4 * k
            df3_k = int(t_kuhn["f3"]) - k
            e_ex_kuhn_full = (
                mp.mpf(df1_k) * b2_d_tower
                + mp.mpf(df2_k) * w3_tower
                + mp.mpf(df3_k) * w4_h3_tower
            )

            # Second-order GPMT (k^4) global trace contribution (0 at k=1; Plancherel-weighted at k>=2)
            if k >= 2:
                d_syt_k4 = _rect_alpha_catalan_dim(k)
                d_mod2_k4 = abs(_rect_alpha_dmod2_closed(k, q))
                e_gpmt_m2_planch = mp.mpf(d_syt_k4) * d_mod2_k4 * e0_tower
            else:
                e_gpmt_m2_planch = mp.mpf(0)

            def _pack_model(d_b_str_pred: mp.mpf, intra_cell: mp.mpf = cell_n1_b1_tower) -> dict[str, str]:
                d_b_net = d_b_str_pred - d_ec
                b_tot = mp.mpf(k) * intra_cell + d_b_str_pred - ec
                return {
                    "Delta_B_strong_inter_MeV": fmt(d_b_str_pred),
                    "Delta_B_net_vs_k_alpha_MeV": fmt(d_b_net),
                    "B_total_MeV": fmt(b_tot),
                    "B_total_minus_AME_MeV": fmt(b_tot - b_ame),
                    "B_total_err_pct": fmt((b_tot - b_ame) / b_ame * mp.mpf(100)),
                }

            models = {
                "C1_naive_cabled_8_choose_k_2_crossings": _pack_model(
                    mp.mpf(8 * _int_comb(k, 2)) * b2_d_tower
                ),
                "C2_global_rect_m2_GPMT_plancherel_plus_pair_bond": _pack_model(
                    mp.mpf(f1_cl) * b2_d_tower + e_gpmt_m2_planch
                ),
                "M0_cluster_simplex_unscaled_1x_w3": _pack_model(
                    mp.mpf(f1_cl) * b2_d_tower + mp.mpf(net_cl_triads) * w3_tower
                ),
                "M1_cluster_simplex_Lambda3C4_4x_w3": _pack_model(
                    mp.mpf(f1_cl) * b2_d_tower + mp.mpf(net_cl_triads) * (mp.mpf(4) * w3_tower)
                ),
                "M2_cluster_simplex_qInt3_sq_cabled_w3": _pack_model(
                    mp.mpf(f1_cl) * b2_d_tower + mp.mpf(net_cl_triads) * ((q3 ** 2) * w3_tower)
                ),
                "M3_cluster_simplex_distinct_flavor_12x_w3": _pack_model(
                    mp.mpf(f1_cl) * b2_d_tower + mp.mpf(net_cl_triads) * (mp.mpf(12) * w3_tower)
                ),
                "M4a_kuhn_3ball_excess_pauli_3_div_8_on_N1_cell": _pack_model(
                    (mp.mpf(3) / mp.mpf(8)) * e_ex_kuhn_full
                ),
                "M4b_kuhn_3ball_excess_unfiltered_on_N1_cell": _pack_model(
                    e_ex_kuhn_full
                ),
                "N2_baseline_1crossing_kuhn_3ball_total": _pack_model(
                    e_ex_kuhn_full, intra_cell=cell_n2_1x_tower
                ),
            }

            per_nucleus[name] = {
                "k_alpha": k,
                "Z": Z,
                "N": N,
                "A": A,
                "B_AME2020_validation_only_MeV": fmt(b_ame),
                "sigma_AME2020_MeV": fmt(sig_ame),
                "E_Coulomb_FormB_MeV": fmt(ec),
                "B_strong_inferred_AME_plus_EC_MeV": fmt(b_str_exp),
                "Delta_EC_vs_k_He4_MeV": fmt(d_ec),
                "Delta_B_AME_vs_k_He4_MeV": fmt(d_b_exp),
                "Delta_B_strong_vs_k_He4_MeV": fmt(d_b_str_exp),
                "models": models,
            }

        # Exact Borromean Hoyle window verification on M2 ([3]_q^2 * w3) and M3 (12 * w3):
        #   0 < d_ec_be8 - b2_d_tower < w3_eff / 3  <=>  Delta_B(8Be) < 0 and Delta_B(12C) > 0
        gap_be8_pos = d_ec_be8 - b2_d_tower
        w3_m2 = (q3 ** 2) * w3_tower
        db_c12_m2 = mp.mpf(3) * b2_d_tower + w3_m2 - (
            mp.mpf(str(coulomb_energy_mev(6, 12, q=q))) - mp.mpf(3) * ec_he4
        )
        hoyle_window_ok = (
            db_be8_bare < mp.mpf(0)
            and db_be8_tower < mp.mpf(0)
            and mp.mpf(0) < gap_be8_pos < (w3_m2 / mp.mpf(3))
            and db_c12_m2 > mp.mpf(0)
        )

        return {
            "pin_label": pin_label,
            "scales": {
                "E0_bare_MeV": fmt(e0_bare),
                "E0_tower_MeV": fmt(e0_tower),
                "b2_logD_bare_MeV": fmt(b2_d_bare),
                "b2_logD_tower_MeV": fmt(b2_d_tower),
                "b2_logGG_tower_MeV": fmt(b2_gg_tower),
                "w3_GPMT_tower_MeV": fmt(w3_tower),
                "w3_qInt3_sq_cabled_MeV": fmt(w3_m2),
                "w3_12x_distinct_flavor_MeV": fmt(mp.mpf(12) * w3_tower),
                "cell_N1_B1_H4_fulltwist_strong_MeV": fmt(cell_n1_b1_tower),
                "cell_N2_1crossing_K4_strong_MeV": fmt(cell_n2_1x_tower),
                "be8_two_alpha_net_bare_MeV": fmt(db_be8_bare),
                "be8_two_alpha_net_tower_MeV": fmt(db_be8_tower),
            },
            "nuclei": per_nucleus,
            "_raw_checks": {
                "hoyle_window_ok": hoyle_window_ok,
            },
        }


def main() -> int:
    set_compute_dps(80)
    with mp.workdps(95):
        q0 = q_at(95)
        q2t = q_two_term_borromean_at(95, k_weighted=False)
        q_mu = q_muon_at(95)

        pins = {
            "q0_proton_1term": q0,
            "q2t_two_term_borromean": q2t,
            "q_muon_codata2022": q_mu,
        }

        part1_by_pin = {
            p_name: _evaluate_part1_at_pin(q_val, p_name)
            for p_name, q_val in pins.items()
        }
        part2_by_pin = {
            p_name: _evaluate_part2_cabling_and_geometry(q_val)
            for p_name, q_val in pins.items()
        }
        part3_by_pin = {
            p_name: _evaluate_part3_binding_models(q_val, p_name)
            for p_name, q_val in pins.items()
        }

        p1_raws = [v.pop("_raw_checks") for v in part1_by_pin.values()]
        p2_raws = [v.pop("_raw_checks") for v in part2_by_pin.values()]
        p3_raws = [v.pop("_raw_checks") for v in part3_by_pin.values()]

        wb = WitnessBuilder(
            "second-order-gpmt-h12-carbon12-and-o16",
            engine="mpmath-80dps",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps parameter-free verification of SecondOrderGPMTCabledAlphaAndCarbon12.lean "
            "(Bean qou-ozdk): complete H_{4k}(q) (k = 1..5, A = 4..20) Pauli-allowed (ell <= 4) "
            "Convention-D zero-multiplicity census (m <= 2 cap), SU(4) Wigner-singlet uniqueness "
            "of (k^4), exact telescoping second-order GPMT formula d_mod^{(2)}(k^4; q), "
            "cabled inter-alpha twist factorization 2*c(k^4) - k*2*c(1^4) = 8*C(k,2), and "
            "side-by-side multi-alpha binding audit across 4He, 8Be, 12C, 16O, and 20Ne."
        )

        wb.add_parameter("precision_dps", 80)
        wb.add_parameter("q0_proton_1term", fmt(q0))
        wb.add_parameter("q2t_two_term_borromean", fmt(q2t))
        wb.add_parameter("q0_muon_codata2022", fmt(q_mu))
        wb.add_parameter("zero_fitting", True)
        wb.add_parameter("zero_ame_proximity_assertions", True)
        wb.add_parameter(
            "lean_companion",
            "folio/quantum-observable-universe/lean/QOU/Nuclear/SecondOrderGPMTCabledAlphaAndCarbon12.lean",
        )

        wb.add_data("part1_pauli_gpmt_census_and_telescoping_residues", part1_by_pin)
        wb.add_data("part2_cabled_alpha_twist_and_simplicial_geometry", part2_by_pin)
        wb.add_data("part3_multi_alpha_binding_candidates", part3_by_pin)

        # Strictly mathematical, combinatorial, hook-content, and cabling assertions ONLY
        # (ZERO assertions gated on proximity to AME2020 binding energies!)
        wb.add_assertion(
            name="part1_pauli_allowed_zD_zero_multiplicity_cap_le_two_exact",
            computed="1" if all(r["pauli_cap_and_strata_ok"] for r in p1_raws) else "0",
            expected="1",
            tolerance="0",
            source="zeroContentBoxCount_le_two, stratum iff theorems, SU(4) singlet uniqueness, and q=1 limits across k=1..5",
        )
        wb.add_assertion(
            name="part1_second_order_gpmt_telescoping_and_ocneanu_bridge_80dps",
            computed=fmt(max(r["max_telescoping_and_bridge_gap"] for r in p1_raws)),
            expected="0",
            tolerance="1e-80",
            source="rectAlpha_dMod2_closed_form & w_lambda^{(m)} = (-1)^m [2]_q^{2m-A} d_mod_hk^{(m)} across all 226 Pauli shapes",
        )
        wb.add_assertion(
            name="part1_independent_130dps_central_difference_zD_residue_crosscheck",
            computed=fmt(max(r["max_central_diff_gap"] for r in p1_raws)),
            expected="0",
            tolerance="1e-50",
            source="Symmetric central difference (w(z_D+eps)+w(z_D-eps)-2w(z_D))/(2 eps^2) vs algebraic m=2 residue on (2^4),(3^4),(4^4)",
        )
        wb.add_assertion(
            name="part2_cabled_alpha_twist_8_choose_k_2_and_spin_isospin_cube_exact",
            computed="1" if all(r["cabling_and_spin_iso_ok"] for r in p2_raws) else "0",
            expected="1",
            tolerance="0",
            source="cabledInterAlphaTwistExp_eq_eight_choose_two, carbon12_internal_vs_cabled_cancellation, oxygen16_internal_vs_cabled_neutrality",
        )
        wb.add_assertion(
            name="part2_multiplicative_full_twist_zpow_and_dehn_sommerville_80dps",
            computed=(
                fmt(max(r["max_zpow_gap"] for r in p2_raws))
                if all(r["ds_invariance_ok"] for r in p2_raws)
                else "1"
            ),
            expected="0",
            tolerance="1e-80",
            source="cabledInterAlpha_zpow_factorization & Dehn-Sommerville net triad invariance Delta(f_2 - 2 f_3)",
        )
        wb.add_assertion(
            name="part3_borromean_hoyle_window_8be_unbound_12c_bound_inequalities",
            computed="1" if all(r["hoyle_window_ok"] for r in p3_raws) else "0",
            expected="1",
            tolerance="0",
            source="SeniorityPairingAndHoyleTriadThreshold.borromean_hoyle_window_theorem across q_0, q_2t, q_muon",
        )

        wb.add_caveat(
            "Exact H_{4k}(q) GPMT stratification vs global trace scaling: Part 1 verifies across "
            "all 226 Pauli-allowed (ell <= 4) partitions of A = 4, 8, 12, 16, 20 that Convention-D "
            "zero multiplicity satisfies m(lambda) <= 2 universally (0 shapes have m >= 3), that "
            "(k^4) is the unique SU(4) spin-isospin singlet at A = 4k with m(k^4) = 2 for all k >= 2, "
            "and that its second-order GPMT dimension telescopes to -[3]_q![2]_q![k-1]_q![k-2]_q! / "
            "([k+3]_q![k+2]_q!). Evaluated directly as an un-localized global A-strand trace, "
            "f^{(k^4)} |d_mod^{(2)}(k^4; q)| * E_0^(tower) gives 0.2205 MeV (8Be), 0.4388 MeV (12C), and "
            "2.8673 MeV (16O) while f^{(k^4)} |w^{(2)}_{(k^4)}| * E_0^(tower) decays as [2]_q^{4-4k}, "
            "confirming that physical nuclear binding is extensive/simplicial rather than a single "
            "global A-strand Markov functional."
        )
        wb.add_caveat(
            "Sign of cabled twist 8*C(k,2) and candid inter-alpha comparison (zero fitting): "
            "(1) In S^{(k^4)}, internal alpha attraction comes from negative column content "
            "2*c(1^4) = -12 < 0, whereas 2*c(k^4) - k*2*c(1^4) = +8*C(k,2) > 0 has the opposite "
            "sign — representing Pauli antisymmetrization / harmonic-oscillator shell promotion "
            "across columns (-6, -2, +2, +6, +10), so treating +8*C(k,2) naively as attractive "
            "crossings (Model C1) severely overbinds 8Be (+14.44 MeV vs -0.092 MeV AME). "
            "(2) A single inter-alpha Convention-D bond b2_logD per cluster edge leaves 8Be "
            "properly unbound (-0.0760 MeV at bare E_0, -0.0557 MeV at tower E_0 vs -0.0918 MeV AME). "
            "(3) Across cluster-simplex Borromean 3-alpha triad candidates at q_2t (all keeping 8Be "
            "at -0.0557 MeV unbound), unscaled 1*w3 underbinds Delta_B(12C) (+1.21 vs +7.27 MeV), "
            "[3]_q^2 * w3 = (E_0 * [3]_q / [2]_q) gives Delta_B(12C) = +6.914 MeV (-4.96%) and "
            "Delta_B(16O) = +14.723 MeV (+1.98% vs +14.437 MeV AME; total B: -5.60% on 12C, -4.79% "
            "on 16O), and 12*w3 (unoriented distinct spin-isospin flavor triples) gives total B "
            "88.89 MeV (-3.55%) on 12C, 125.28 MeV (-1.83%) on 16O, and 160.57 MeV (-0.05%) on 20Ne; "
            "deriving the exact coarse-grained 3-alpha triad coefficient from H_{12}(q) projector "
            "contraction remains open."
        )

        stamp = q0_comparison(
            muon=q_mu,
            proton=q0,
            reason=(
                "Bean qou-ozdk second-order GPMT H_12/H_16 multi-alpha probe evaluates (k^4) "
                "telescoping residues, cabled braid twists, and inter-alpha binding candidates "
                "side-by-side across q_0, q_2t, and q_muon."
            ),
        )
        saved_path = wb.save(stamp)
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))

        import witness_raw_float64_audit as _f64_audit

        n_raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if n_raw_floats != 0:
            raise RuntimeError(f"Emitted witness contains {n_raw_floats} raw float64 values!")

        p1_2t = part1_by_pin["q2t_two_term_borromean"]
        p3_2t = part3_by_pin["q2t_two_term_borromean"]
        print("=" * 126)
        print(
            "  Bean qou-ozdk: 80-dps Second-Order (m=2) GPMT (k^4) Census, Cabled Twist & Multi-Alpha Binding Audit (@ q_2t)"
        )
        print("=" * 126)
        print(
            f"  Part 1: max telescoping/bridge gap = {mp.nstr(mp.mpf(p1_2t['max_ocneanu_hook_bridge_gap_all_226_pauli_shapes']), 4)} | "
            f"130-dps central-diff check = {mp.nstr(mp.mpf(p1_2t['max_central_diff_130dps_rel_err_k2_k3_k4']), 4)}"
        )
        for k_idx in (1, 2, 3, 4, 5):
            ck_entry = p1_2t["census_by_k"][f"k{k_idx}_A{4 * k_idx}"]
            rc = ck_entry["unique_su4_singlet_rectangle"]
            print(
                f"    k={k_idx} (A={4*k_idx:2d}): Pauli={ck_entry['pauli_allowed_ell_le_4_count']:3d}/{ck_entry['total_partitions']:3d} "
                f"hist={ck_entry['pauli_zD_multiplicity_histogram']} | (k^4) m={rc['zD_zero_multiplicity']} "
                f"2c={rc['full_twist_exponent']:3d} f={rc['syt_dim_catalan4']:7d} "
                f"d_mod_hk={mp.nstr(mp.mpf(rc['d_mod_hook_content']), 7):>12s} "
                f"f*|d_mod|={mp.nstr(mp.mpf(rc['plancherel_syt_mul_abs_d_mod_hk']), 7):>10s}"
            )
        print("-" * 126)
        hdr = (
            f"{'Model':<45} | {'dB(8Be)':>9} {'dB(12C)':>9} {'dB(16O)':>9} | "
            f"{'B(12C) err%':>11} {'B(16O) err%':>11} {'B(20Ne) err%':>12}"
        )
        print(hdr)
        print("-" * len(hdr))
        model_keys = list(p3_2t["nuclei"]["12C"]["models"].keys())
        for mk in model_keys:
            db8 = mp.nstr(mp.mpf(p3_2t["nuclei"]["8Be"]["models"][mk]["Delta_B_net_vs_k_alpha_MeV"]), 5)
            db12 = mp.nstr(mp.mpf(p3_2t["nuclei"]["12C"]["models"][mk]["Delta_B_net_vs_k_alpha_MeV"]), 5)
            db16 = mp.nstr(mp.mpf(p3_2t["nuclei"]["16O"]["models"][mk]["Delta_B_net_vs_k_alpha_MeV"]), 5)
            e12 = mp.nstr(mp.mpf(p3_2t["nuclei"]["12C"]["models"][mk]["B_total_err_pct"]), 5)
            e16 = mp.nstr(mp.mpf(p3_2t["nuclei"]["16O"]["models"][mk]["B_total_err_pct"]), 5)
            e20 = mp.nstr(mp.mpf(p3_2t["nuclei"]["20Ne"]["models"][mk]["B_total_err_pct"]), 5)
            print(
                f"{mk:<45} | {db8:>9} {db12:>9} {db16:>9} | {e12:>10}% {e16:>10}% {e20:>11}%"
            )
        print(
            f"{'AME2020_reference_dB_vs_k_He4':<45} | "
            f"{mp.nstr(mp.mpf(p3_2t['nuclei']['8Be']['Delta_B_AME_vs_k_He4_MeV']), 5):>9} "
            f"{mp.nstr(mp.mpf(p3_2t['nuclei']['12C']['Delta_B_AME_vs_k_He4_MeV']), 5):>9} "
            f"{mp.nstr(mp.mpf(p3_2t['nuclei']['16O']['Delta_B_AME_vs_k_He4_MeV']), 5):>9} | "
            f"{'92.162 MeV':>11} {'127.619 MeV':>11} {'160.645 MeV':>12}"
        )
        print("=" * 126)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
