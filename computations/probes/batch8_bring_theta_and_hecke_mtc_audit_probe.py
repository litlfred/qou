#!/usr/bin/env python3
"""80-dps algebraic & substrate diagnostic for Batch 8 beans qou-2a2o, qou-9l0d, and hkmt.

1. Part A (`qou-2a2o`, `qou-9l0d` — `QOU/BringsSurface/BringThetaCharacteristicsSymplectic.lean`):
   - Exact `Sp(8, F_2)` action of `S_5` on the mod-2 homology model `H = V_0 (+) V_0^* ~= F_2^8`
     of Bring's genus-4 curve (`V_0 = {x in F_2^5 : sum x_i = 0}`).
   - Verifies that all 120 elements of `S_5` preserve the canonical symplectic pairing `omega`
     and the hyperbolic quadratic refinement `q_0(u, v) = u . v`.
   - Enumerates all `2^8 = 256` quadratic refinements `q_c(x) = q_0(x) + omega(c, x)`,
     certifying:
       * `136` even (`Arf = 0`) + `120` odd (`Arf = 1`);
       * Braden & Disney-Hogg (2024) Theorem 5.9 even `S_5`-orbits:
         `[1, 5, 5, 5, 10, 10, 10, 30, 30, 30]` (`10` orbits, unique `S_5`-invariant spin
         structure `q_0`, correcting unmerged PR `#8150`'s `1 + 15 + 60 + 60`);
       * Braden & Disney-Hogg (2024) Corollary 5.7 odd `S_5`-orbits:
         `[20, 20, 20, 60]` (`4` orbits, correcting unmerged PR `#8150`'s `60 + 60`);
       * Braden & Disney-Hogg (2024) Footnote 29 order-5 `S`-orbits:
         `136 = 1 + 27 * 5` (1 fixed even) and `120 = 24 * 5` (0 fixed odd);
       * Kummer root divisibility on `chi = -6` (`#8862`, `qou-n2aa`): admissible levels in
         `{1..12}` are `{1, 2, 3, 6}`.

2. Part B (`hkmt`, `rtep` — `QOU/BraidKnot/HeckeRealVsRootOfUnityModularity.lean`):
   - At 80-dps proton `q_0` (`q0Anchor = "proton"`), evaluates symmetric quantum integers
     `[k]_{q_0}` (`k = 1..30`) by both closed form and the division-free Chebyshev recurrence
     `symQInt`, verifying `[k]_{q_0} > k` for all `k >= 2`, agreement `< 1e-75`, and prefix
     global-dimension growth `sum_{k=1}^{30} [k]_{q_0}^2 > 9455 > 30` (non-truncation on `q > 1`).
   - At roots of unity `q = exp(i * pi / ell)` (`ell in {3, 4, 5, 7, 10}`, corresponding to
     `SU(2)_1`, `SU(2)_2`, `SU(2)_3`, `SU(2)_5`, `SU(2)_8`), verifies at 80-dps complex precision:
       * exact truncation `[ell]_q = 0` (`|symQInt(q, ell)| < 1e-76`) with `[k]_q > 0` for
         `1 <= k <= ell - 1`;
       * closed-form global dimension `D^2 = sum_{a=0}^{ell-2} [a+1]_q^2 = ell / (2 sin^2(pi/ell))`;
       * vacuum-row ratio `S_{0,a} / S_{0,0} = [a+1]_q`;
       * symmetric unitary `S^2 = I_{ell-1}` and modular relation
         `(S * T)^3 = exp(2 * pi * i * c / 8) * I_{ell-1}` with central charge
         `c = 3 * (ell - 2) / ell` and `T_{a,a} = exp(2 * pi * i * a * (a + 2) / (4 * ell))`.
"""

from __future__ import annotations

import itertools
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[2]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "tools" / "pyhecke" / "python",
    _ROOT / "computations" / "substrate",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)


def _perm_mat_v4(p: tuple[int, ...]) -> list[list[int]]:
    """4x4 F_2 matrix of permutation `p in S_5` on `V_0 = {x in F_2^5 : sum x_i = 0}`."""
    mat = [[0] * 4 for _ in range(4)]
    for j in range(4):
        # Image of basis vector e_j + e_4 under x -> x o p^{-1} is e_{p[j]} + e_{p[4]}
        vec = [0] * 5
        vec[p[j]] ^= 1
        vec[p[4]] ^= 1
        for i in range(4):
            mat[i][j] = vec[i]
    return mat


def _mat_inv_f2(a: list[list[int]]) -> list[list[int]]:
    """Exact inverse of an invertible matrix over F_2."""
    n = len(a)
    aug = [a[i][:] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if aug[r][col])
        aug[col], aug[piv] = aug[piv], aug[col]
        for r in range(n):
            if r != col and aug[r][col]:
                aug[r] = [aug[r][k] ^ aug[col][k] for k in range(2 * n)]
    return [row[n:] for row in aug]


def _mat_transpose(a: list[list[int]]) -> list[list[int]]:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def _mat_mul_f2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n, m, p = len(a), len(b), len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(m)) & 1 for j in range(p)]
        for i in range(n)
    ]


def _apply8_f2(g: list[list[int]], x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(g[i][j] * x[j] for j in range(8)) & 1 for i in range(8))


def _q0_f2(x: tuple[int, ...]) -> int:
    return sum(x[i] * x[i + 4] for i in range(4)) & 1


def _sym_qint_chebyshev(q: mp.mpf | mp.mpc, n: int) -> mp.mpf | mp.mpc:
    """Division-free Chebyshev recurrence matching Lean `symQInt`."""
    if n == 0:
        return mp.mpf(0)
    if n == 1:
        return mp.mpf(1)
    two_c = q + mp.mpf(1) / q
    prev2: mp.mpf | mp.mpc = mp.mpf(0)
    prev1: mp.mpf | mp.mpc = mp.mpf(1)
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, two_c * prev1 - prev2
    return prev1


def main() -> int:
    with mp.workdps(WORK_DPS):
        # ── Part A: Exact F_2[S_5] symplectic & theta-characteristic audit ──
        s5_perms = list(itertools.permutations(range(5)))
        j_symp = [
            [1 if abs(i - j) == 4 else 0 for j in range(8)]
            for i in range(8)
        ]

        s5_mats8: list[list[list[int]]] = []
        all_symplectic = True
        all_preserve_q0 = True

        for p in s5_perms:
            a4 = _perm_mat_v4(p)
            b4 = _mat_transpose(_mat_inv_f2(a4))
            g8 = [a4[i] + [0] * 4 for i in range(4)] + [
                [0] * 4 + b4[i] for i in range(4)
            ]
            s5_mats8.append(g8)
            gt_j_g = _mat_mul_f2(_mat_transpose(g8), _mat_mul_f2(j_symp, g8))
            if gt_j_g != j_symp:
                all_symplectic = False

        all_vecs = [
            tuple((mask >> i) & 1 for i in range(8)) for mask in range(256)
        ]
        for g8 in s5_mats8:
            for x in all_vecs:
                if _q0_f2(_apply8_f2(g8, x)) != _q0_f2(x):
                    all_preserve_q0 = False

        even_vecs = [x for x in all_vecs if _q0_f2(x) == 0]
        odd_vecs = [x for x in all_vecs if _q0_f2(x) == 1]

        seen: set[tuple[int, ...]] = set()
        even_orbits: list[int] = []
        odd_orbits: list[int] = []
        for x in all_vecs:
            if x in seen:
                continue
            orb = {_apply8_f2(g8, x) for g8 in s5_mats8}
            seen |= orb
            if _q0_f2(x) == 0:
                even_orbits.append(len(orb))
            else:
                odd_orbits.append(len(orb))
        even_orbits.sort()
        odd_orbits.sort()

        # Order-5 cyclic generator S = (0 1 2 3 4)
        five_cycle_perm = (1, 2, 3, 4, 0)
        a_five = _perm_mat_v4(five_cycle_perm)
        b_five = _mat_transpose(_mat_inv_f2(a_five))
        g_five = [a_five[i] + [0] * 4 for i in range(4)] + [
            [0] * 4 + b_five[i] for i in range(4)
        ]
        seen5: set[tuple[int, ...]] = set()
        even_five_orbits: list[int] = []
        odd_five_orbits: list[int] = []
        for x in all_vecs:
            if x in seen5:
                continue
            cur = x
            orb5: set[tuple[int, ...]] = set()
            for _ in range(5):
                orb5.add(cur)
                cur = _apply8_f2(g_five, cur)
            seen5 |= orb5
            if _q0_f2(x) == 0:
                even_five_orbits.append(len(orb5))
            else:
                odd_five_orbits.append(len(orb5))
        even_five_orbits.sort()
        odd_five_orbits.sort()

        kummer_admissible_1_to_12 = [n for n in range(1, 13) if (-6) % n == 0]

        # ── Part B: 80-dps Hecke modularity split (real q_0 > 1 vs roots of unity) ──
        q0 = q_at(dps=WORK_DPS)
        denom_q0 = q0 - mp.mpf(1) / q0

        max_cheb_vs_closed_diff = mp.mpf(0)
        strict_growth_ok = True
        prefix_sq_sum_30 = mp.mpf(0)

        for k in range(1, 31):
            q_cheb = _sym_qint_chebyshev(q0, k)
            q_closed = (mp.power(q0, k) - mp.power(q0, -k)) / denom_q0
            diff = abs(q_cheb - q_closed)
            if diff > max_cheb_vs_closed_diff:
                max_cheb_vs_closed_diff = diff
            if k >= 2 and not (q_cheb > mp.mpf(k)):
                strict_growth_ok = False
            prefix_sq_sum_30 += q_cheb * q_cheb

        sum_k_sq_30 = sum(k * k for k in range(1, 31))  # 9455

        # Root-of-unity SU(2)_{ell-2} MTC verification at q = exp(i * pi / ell)
        levels = [3, 4, 5, 7, 10]
        max_trunc_zero_err = mp.mpf(0)
        max_global_dim_err = mp.mpf(0)
        max_vac_ratio_err = mp.mpf(0)
        max_s_sq_err = mp.mpf(0)
        max_modular_st3_err = mp.mpf(0)
        all_interior_qdims_pos = True

        for ell in levels:
            q_root = mp.expj(mp.pi / mp.mpf(ell))
            trunc_val = abs(_sym_qint_chebyshev(q_root, ell))
            if trunc_val > max_trunc_zero_err:
                max_trunc_zero_err = trunc_val

            rank = ell - 1
            qdims: list[mp.mpf] = []
            for a in range(rank):
                val = _sym_qint_chebyshev(q_root, a + 1)
                if mp.re(val) <= mp.mpf(0) or abs(mp.im(val)) > mp.mpf("1e-75"):
                    all_interior_qdims_pos = False
                qdims.append(mp.re(val))

            d_sq_sum = sum(d * d for d in qdims)
            d_sq_closed = mp.mpf(ell) / (
                mp.mpf(2) * mp.sin(mp.pi / mp.mpf(ell)) ** 2
            )
            g_err = abs(d_sq_sum - d_sq_closed)
            if g_err > max_global_dim_err:
                max_global_dim_err = g_err

            big_d = mp.sqrt(d_sq_sum)
            s_mat = [
                [
                    mp.re(_sym_qint_chebyshev(q_root, (a + 1) * (b + 1))) / big_d
                    for b in range(rank)
                ]
                for a in range(rank)
            ]
            t_diag = [
                mp.expj(
                    mp.mpf(2)
                    * mp.pi
                    * mp.mpf(a * (a + 2))
                    / mp.mpf(4 * ell)
                )
                for a in range(rank)
            ]

            for a in range(rank):
                r_err = abs(s_mat[0][a] / s_mat[0][0] - qdims[a])
                if r_err > max_vac_ratio_err:
                    max_vac_ratio_err = r_err

            # Check S^2 = I_{ell-1}
            for a in range(rank):
                for b in range(rank):
                    entry = sum(s_mat[a][m] * s_mat[m][b] for m in range(rank))
                    target = mp.mpf(1) if a == b else mp.mpf(0)
                    err = abs(entry - target)
                    if err > max_s_sq_err:
                        max_s_sq_err = err

            # Check (S * T)^3 = exp(2 * pi * i * c / 8) * I_{ell-1}, c = 3*(ell-2)/ell
            st_mat = [
                [mp.mpc(s_mat[a][b]) * t_diag[b] for b in range(rank)]
                for a in range(rank)
            ]

            def _cmat_mul(
                x: list[list[mp.mpc]], y: list[list[mp.mpc]]
            ) -> list[list[mp.mpc]]:
                n = len(x)
                return [
                    [sum(x[i][k] * y[k][j] for k in range(n)) for j in range(n)]
                    for i in range(n)
                ]

            st3 = _cmat_mul(_cmat_mul(st_mat, st_mat), st_mat)
            c_central = mp.mpf(3 * (ell - 2)) / mp.mpf(ell)
            anomaly_phase = mp.expj(mp.mpf(2) * mp.pi * c_central / mp.mpf(8))
            for a in range(rank):
                for b in range(rank):
                    target_c = anomaly_phase if a == b else mp.mpc(0)
                    err_c = abs(st3[a][b] - target_c)
                    if err_c > max_modular_st3_err:
                        max_modular_st3_err = err_c

        wb = WitnessBuilder(
            "batch8-bring-theta-and-hecke-mtc-audit",
            engine="mpmath-80dps+exact-F2-Sp8",
            output_dir=_ROOT / "computations" / "probes",
        )
        wb.set_description(
            "Batch 8 (qou-tw5j) 80-dps & exact F_2[S_5] diagnostic verifying "
            "BringThetaCharacteristicsSymplectic (unique S_5-invariant even spin structure and "
            "Braden-Disney-Hogg 2024 orbit decompositions) and HeckeRealVsRootOfUnityModularity "
            "(real q_0 > 1 non-truncation vs root-of-unity SU(2)_{ell-2} MTC modular relations)."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("q0_proton", fmt(q0, dps=OUT_DPS))
        wb.add_data(
            "bring_theta_symplectic",
            {
                "even_count": len(even_vecs),
                "odd_count": len(odd_vecs),
                "even_S5_orbits": even_orbits,
                "odd_S5_orbits": odd_orbits,
                "even_fiveCycle_fixed_count": even_five_orbits.count(1),
                "odd_fiveCycle_fixed_count": odd_five_orbits.count(1),
                "kummer_admissible_levels_1_to_12": kummer_admissible_1_to_12,
            },
        )
        wb.add_data(
            "hecke_modularity_split",
            {
                "prefix_qdim_sq_sum_N30_at_q0": fmt(prefix_sq_sum_30, dps=OUT_DPS),
                "classical_sum_k_sq_N30": sum_k_sq_30,
                "levels_tested": levels,
                "max_chebyshev_vs_closed_diff": fmt(max_cheb_vs_closed_diff, dps=15),
                "max_root_truncation_err": fmt(max_trunc_zero_err, dps=15),
                "max_modular_st3_err": fmt(max_modular_st3_err, dps=15),
            },
        )

        wb.add_assertion(
            "s5_acts_symplectically_and_preserves_q0",
            int(all_symplectic and all_preserve_q0 and len(s5_mats8) == 120),
            1,
            "0",
            source="BringThetaCharacteristicsSymplectic.{Phi_preserves_omega, Phi_preserves_q0}",
        )
        wb.add_assertion(
            "bring_theta_arf_counts_136_even_120_odd",
            int(len(even_vecs) == 136 and len(odd_vecs) == 120),
            1,
            "0",
            source="BringThetaCharacteristicsSymplectic.even_and_odd_counts_bdh",
        )
        wb.add_assertion(
            "bdh2024_even_theta_S5_orbits_1_5x3_10x3_30x3",
            int(even_orbits == [1, 5, 5, 5, 10, 10, 10, 30, 30, 30]),
            1,
            "0",
            source="Braden-Disney-Hogg 2024 Thm 5.9; BringThetaCharacteristicsSymplectic.even_orbit_partition_bdh",
        )
        wb.add_assertion(
            "bdh2024_odd_theta_S5_orbits_20x3_60",
            int(odd_orbits == [20, 20, 20, 60]),
            1,
            "0",
            source="Braden-Disney-Hogg 2024 Cor 5.7; BringThetaCharacteristicsSymplectic.odd_orbit_partition_bdh",
        )
        wb.add_assertion(
            "bdh2024_five_cycle_unique_fixed_spin_structure",
            int(
                even_five_orbits == [1] + [5] * 27
                and odd_five_orbits == [5] * 24
            ),
            1,
            "0",
            source="Braden-Disney-Hogg 2024 Footnote 29; unique_fiveCycle_invariant_quadRefinement + fiveCycle_fixed_points_bdh",
        )
        wb.add_assertion(
            "bring_kummer_admissible_levels_1_2_3_6",
            int(kummer_admissible_1_to_12 == [1, 2, 3, 6]),
            1,
            "0",
            source="CechGenus4Good.genus4_kummer_trivial_iff (#8862 / qou-n2aa)",
        )
        wb.add_assertion(
            "real_q0_symqint_chebyshev_matches_closed_form_and_grows_unboundedly",
            int(
                max_cheb_vs_closed_diff < mp.mpf("1e-75")
                and strict_growth_ok
                and prefix_sq_sum_30 > mp.mpf(sum_k_sq_30)
            ),
            1,
            "0",
            source="HeckeRealVsRootOfUnityModularity.{natCast_lt_symQInt_of_one_lt, globalDimSq_prefix_ge}",
        )
        wb.add_assertion(
            "root_of_unity_truncation_and_global_dim_formula_80dps",
            fmt(max(max_trunc_zero_err, max_global_dim_err, max_vac_ratio_err), dps=15),
            "0",
            "1e-75",
            source="HeckeRealVsRootOfUnityModularity.symQInt_eq_zero_iff_pow_two_mul_eq_one + Verlinde D^2",
        )
        wb.add_assertion(
            "root_of_unity_interior_qdims_positive_and_S_sq_identity_80dps",
            int(all_interior_qdims_pos and max_s_sq_err < mp.mpf("1e-75")),
            1,
            "0",
            source="SU(2)_{ell-2} MTC unitarity & self-duality S^2 = I (ell = 3,4,5,7,10)",
        )
        wb.add_assertion(
            "root_of_unity_modular_ST_cubed_anomaly_relation_80dps",
            fmt(max_modular_st3_err, dps=15),
            "0",
            "1e-74",
            source="Bakalov-Kirillov 2001 (S*T)^3 = exp(2*pi*i*c/8)*S^2 across ell = 3,4,5,7,10",
        )

        wb.add_caveat(
            "1. On qou-2a2o / qou-9l0d: uniqueness of the S_5-invariant even theta characteristic "
            "(Szego/Burns spin structure) and the orbit decompositions 136 = 1+5+5+5+10+10+10+30+30+30 "
            "and 120 = 20+20+20+60 are classical algebraic-geometry theorems (Braden & Disney-Hogg "
            "2024), not QOU predictions; which principal bundle the brane tower lifts remains open. "
            "2. On hkmt / rtep: at generic real q_0 > 1 all [k]_{q_0} > 0 so the full Hecke/TL "
            "category has infinitely many non-negligible objects and is not modular without either "
            "a root-of-unity semisimplified quotient (q^{2*ell} = 1) or an explicit finite block "
            "set (KeystoneHeckeMTC.heckeMTC); whether hkmt scopes to the root-of-unity quotient is "
            "an open owner question, and bwse / bwhk stays open."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"Even S_5 orbits (sum={sum(even_orbits)}): {even_orbits}")
        print(f"Odd  S_5 orbits (sum={sum(odd_orbits)}): {odd_orbits}")
        print(f"N=30 sum [k]_{{q_0}}^2 = {fmt(prefix_sq_sum_30, dps=20)} (> {sum_k_sq_30})")
        print(f"Max |(ST)^3 - zeta^3 I| across ell={levels}: {fmt(max_modular_st3_err, dps=15)}")
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
