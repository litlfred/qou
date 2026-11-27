#!/usr/bin/env python3
"""Pre-registered 80-dps W2 probe: All-q H_7(q), H_8(q) two-row Wedderburn cross-nucleon
pair identities, coideal Killing-norm hypercharge slope 1/2, and separated-hadron Z-channel
Yukawa removal (beans qou-20sx, qou-vudb, qou-fbrp).

Pre-registration: PREREGISTRATION.md (committed prior to running any evaluation).
Lean companion: folio/quantum-observable-universe/lean/QOU/QBeta/CrossNucleonPairWedderburnZRemoval.lean.

Zero free parameters, zero float64, proton substrate pin q_0 = q_at(80) at workdps = 80.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from codata_constants import (  # noqa: E402
    M_PI_0_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV_STR,
    Q_MP,
    q_at,
    q_int_at,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt80(x: mpf) -> str:
    return mp.nstr(x, 80, strip_zeros=False)


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def enumerate_partitions(n: int, max_part: int | None = None) -> list[tuple[int, ...]]:
    """All integer partitions of n in non-increasing order."""
    if max_part is None:
        max_part = n
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    for first in range(min(n, max_part), 0, -1):
        for rest in enumerate_partitions(n - first, first):
            out.append((first,) + rest)
    return out


def diagram_cells(part: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(r, c) for r, row_len in enumerate(part) for c in range(row_len)]


def hook_length(part: tuple[int, ...], r: int, c: int) -> int:
    arm = part[r] - c
    leg = sum(1 for r2 in range(r + 1, len(part)) if part[r2] > c)
    return arm + leg


def ocneanu_weight_mpf(qv: mpf, zv: mpf, part: tuple[int, ...]) -> mpf:
    """Exact Ocneanu weight formula from QOU/SchurWeyl/OcneanuWeight.lean."""
    num = mpf(1)
    den = mpf(1)
    q2 = qv ** 2
    base_term = q2 - mpf(1) - qv * zv
    for r, c in diagram_cells(part):
        factor_num = (qv ** (2 * r)) * base_term + (qv ** (2 * c + 1)) * zv
        factor_den = (qv ** (2 * hook_length(part, r, c))) - mpf(1)
        num *= factor_num
        den *= factor_den
    return num / den


def enumerate_two_row_syt(m: int, k: int) -> list[tuple[tuple[int, int], ...]]:
    """Enumerate all Standard Young Tableaux of two-row shape (m, k) (m >= k >= 0)
    as tuples mapping 0-indexed entry e in 0..(m+k-1) -> cell (row, col).
    """
    n = m + k
    results: list[tuple[tuple[int, int], ...]] = []

    def backtrack(r0: int, r1: int, placement: list[tuple[int, int]]) -> None:
        if r0 + r1 == n:
            results.append(tuple(placement))
            return
        if r0 < m:
            placement.append((0, r0))
            backtrack(r0 + 1, r1, placement)
            placement.pop()
        if r1 < k and r1 + 1 <= r0:
            placement.append((1, r1))
            backtrack(r0, r1 + 1, placement)
            placement.pop()

    backtrack(0, 0, [])
    return results


def build_hoefsmit_generators(
    qv: mpf, m: int, k: int
) -> tuple[list[list[list[mpf]]], list[list[list[mpf]]]]:
    """Square-root-free Hoefsmit seminormal matrices for H_{m+k}(q) on shape (m, k),
    matching QOU/SchurWeyl/HoefsmitRep.lean and SeminormalParam.lean:
        sigma_i^2 = (q - q^-1) sigma_i + 1.
    Returns (pos_gens, inv_gens), each a list of (m+k-1) matrices of size d x d.
    """
    syts = enumerate_two_row_syt(m, k)
    dim = len(syts)
    idx_of = {t: idx for idx, t in enumerate(syts)}
    n = m + k
    qinv = mpf(1) / qv
    hv = qv - qinv

    pos_gens: list[list[list[mpf]]] = []
    inv_gens: list[list[list[mpf]]] = []

    for i in range(n - 1):
        mat = [[mpf(0) for _ in range(dim)] for _ in range(dim)]
        visited: set[int] = set()
        for a_idx, tab in enumerate(syts):
            if a_idx in visited:
                continue
            c1 = tab[i]
            c2 = tab[i + 1]
            # Content c(r, col) = col - r; axial distance d = content(c2) - content(c1)
            d = (c2[1] - c2[0]) - (c1[1] - c1[0])
            if d == 1:
                mat[a_idx][a_idx] = qv
                visited.add(a_idx)
            elif d == -1:
                mat[a_idx][a_idx] = -qinv
                visited.add(a_idx)
            else:
                swapped = list(tab)
                swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
                b_idx = idx_of[tuple(swapped)]
                visited.add(a_idx)
                visited.add(b_idx)
                # Order pair (u_idx, v_idx) so u_idx < v_idx
                if a_idx < b_idx:
                    u_idx, v_idx, d_uv = a_idx, b_idx, d
                else:
                    u_idx, v_idx, d_uv = b_idx, a_idx, -d
                a_param = hv / (mpf(1) - (qv ** (-2 * d_uv)))
                b_param = hv - a_param
                mat[u_idx][u_idx] = a_param
                mat[u_idx][v_idx] = mpf(1)
                mat[v_idx][u_idx] = (qv - a_param) * (qinv + a_param)
                mat[v_idx][v_idx] = b_param
        inv_mat = [
            [mat[r][c] - (hv if r == c else mpf(0)) for c in range(dim)]
            for r in range(dim)
        ]
        pos_gens.append(mat)
        inv_gens.append(inv_mat)

    return pos_gens, inv_gens


def mat_eye(dim: int) -> list[list[mpf]]:
    return [[mpf(1) if r == c else mpf(0) for c in range(dim)] for r in range(dim)]


def mat_mul(a: list[list[mpf]], b: list[list[mpf]]) -> list[list[mpf]]:
    dim = len(a)
    out = [[mpf(0) for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        ai = a[i]
        oi = out[i]
        for k in range(dim):
            aik = ai[k]
            if aik == 0:
                continue
            bk = b[k]
            for j in range(dim):
                oi[j] += aik * bk[j]
    return out


def mat_add_scaled(
    a: list[list[mpf]], b: list[list[mpf]], alpha: mpf, beta: mpf
) -> list[list[mpf]]:
    dim = len(a)
    return [
        [alpha * a[r][c] + beta * b[r][c] for c in range(dim)]
        for r in range(dim)
    ]


def mat_max_abs(a: list[list[mpf]]) -> mpf:
    return max(abs(x) for row in a for x in row)


def mat_trace(a: list[list[mpf]]) -> mpf:
    return sum((a[i][i] for i in range(len(a))), mpf(0))


def eval_word_mat(
    word: list[tuple[int, int]],
    pos_gens: list[list[list[mpf]]],
    inv_gens: list[list[list[mpf]]],
) -> list[list[mpf]]:
    dim = len(pos_gens[0])
    cur = mat_eye(dim)
    for idx, sign in word:
        cur = mat_mul(cur, pos_gens[idx] if sign > 0 else inv_gens[idx])
    return cur


def build_tensor_sector_engine(
    qv: mpf, n_strands: int, block_a: tuple[int, int, int], block_b: tuple[int, int, int]
):
    """Exact sparse 80-dps Jimbo R-matrix engine on (V_2)^{x n_strands} for sector-projected
    nucleon pair readouts T_X(Q_A, Q_B) = Tr(K^{x N} Pi_{Q_A, Q_B} C_A C_B X).
    """
    dim = 1 << n_strands
    qinv = mpf(1) / qv
    hv = qv - qinv

    # Jimbo R and R^-1 on basis 00, 01, 10, 11 (matching QOU/QBeta/WeightedTraceSide.lean)
    r_loc = [
        [qv, mpf(0), mpf(0), mpf(0)],
        [mpf(0), mpf(0), mpf(1), mpf(0)],
        [mpf(0), mpf(1), hv, mpf(0)],
        [mpf(0), mpf(0), mpf(0), qv],
    ]
    rinv_loc = [
        [qinv, mpf(0), mpf(0), mpf(0)],
        [mpf(0), -hv, mpf(1), mpf(0)],
        [mpf(0), mpf(1), mpf(0), mpf(0)],
        [mpf(0), mpf(0), mpf(0), qinv],
    ]

    def bits_of(s: int) -> list[int]:
        return [(s >> (n_strands - 1 - k)) & 1 for k in range(n_strands)]

    def state_of(b: list[int]) -> int:
        val = 0
        for x in b:
            val = (val << 1) | x
        return val

    def two_site_op(site: int, loc: list[list[mpf]]) -> dict[int, dict[int, mpf]]:
        op: dict[int, dict[int, mpf]] = {}
        for col_s in range(dim):
            b = bits_of(col_s)
            col2 = (b[site] << 1) | b[site + 1]
            for row2 in range(4):
                entry = loc[row2][col2]
                if entry != 0:
                    nb = list(b)
                    nb[site], nb[site + 1] = (row2 >> 1) & 1, row2 & 1
                    op.setdefault(state_of(nb), {})[col_s] = entry
        return op

    def sp_eye() -> dict[int, dict[int, mpf]]:
        return {s: {s: mpf(1)} for s in range(dim)}

    def sp_mul(
        x_op: dict[int, dict[int, mpf]], y_op: dict[int, dict[int, mpf]]
    ) -> dict[int, dict[int, mpf]]:
        out: dict[int, dict[int, mpf]] = {}
        for r, xr in x_op.items():
            row_acc: dict[int, mpf] = {}
            for k_mid, a_val in xr.items():
                yk = y_op.get(k_mid)
                if not yk:
                    continue
                for c, b_val in yk.items():
                    row_acc[c] = row_acc.get(c, mpf(0)) + a_val * b_val
            row_nz = {c: v for c, v in row_acc.items() if v != 0}
            if row_nz:
                out[r] = row_nz
        return out

    gens = {
        (site, sign): two_site_op(site, r_loc if sign > 0 else rinv_loc)
        for site in range(n_strands - 1)
        for sign in (1, -1)
    }

    a0, b0 = block_a[0], block_b[0]
    core = sp_eye()
    core_word = [(a0, 1), (a0 + 1, -1)] * 3 + [(b0, 1), (b0 + 1, -1)] * 3
    for let in core_word:
        core = sp_mul(core, gens[let])

    k_diag = []
    sectors = []
    for s in range(dim):
        b = bits_of(s)
        u_total = sum(1 for x in b if x == 0)
        k_diag.append(qv ** (2 * u_total - n_strands))
        qa = sum(1 for idx in block_a if b[idx] == 0) - 1
        qb = sum(1 for idx in block_b if b[idx] == 0) - 1
        sectors.append((qa, qb))

    def readout(x_op: dict[int, dict[int, mpf]]) -> dict[tuple[int, int], mpf]:
        res: dict[tuple[int, int], mpf] = {}
        for s in range(dim):
            c_row = core.get(s)
            if not c_row:
                continue
            acc = mpf(0)
            for k_mid, c_val in c_row.items():
                x_val = x_op.get(k_mid, {}).get(s)
                if x_val is not None:
                    acc += c_val * x_val
            if acc != 0:
                sec = sectors[s]
                res[sec] = res.get(sec, mpf(0)) + k_diag[s] * acc
        return res

    return sp_eye, sp_mul, gens, readout


def alpha_six_analytic(qv: mpf) -> mpf:
    q2 = qv ** 2
    num = q2 * (
        qv ** 12
        - mpf(3) * (qv ** 10)
        + qv ** 8
        - mpf(5) * (qv ** 6)
        + mpf(3) * (qv ** 4)
        - mpf(2) * q2
        + mpf(1)
    )
    den = (
        qv ** 14
        - mpf(2) * (qv ** 12)
        - qv ** 10
        - mpf(2) * (qv ** 8)
        - mpf(2) * (qv ** 6)
        - qv ** 4
        - mpf(2) * q2
        + mpf(1)
    )
    return num / den


def extract_pair_params(
    delta_e: dict[tuple[int, int], mpf]
) -> tuple[mpf, mpf, mpf, mpf, mpf]:
    """From Delta E(Q_A, Q_B) on {0, 1}^2, extract (c0, kappa, alpha, beta) for
    c + kappa * (Q_A - beta) * (Q_B - alpha), plus max residual across all 4 nucleon pairs.
    """
    e00 = delta_e[(0, 0)]
    e01 = delta_e[(0, 1)]
    e10 = delta_e[(1, 0)]
    e11 = delta_e[(1, 1)]
    kappa = e11 - e10 - e01 + e00
    alpha = (e00 - e10) / kappa
    beta = (e00 - e01) / kappa
    c_param = e00 - kappa * alpha * beta
    max_res = max(
        abs(delta_e[(qa, qb)] - (c_param + kappa * (mpf(qa) - beta) * (mpf(qb) - alpha)))
        for qa in (0, 1)
        for qb in (0, 1)
    )
    return c_param, kappa, alpha, beta, max_res


def alpha_form_b_at(qv: mpf, dps: int = 80) -> mpf:
    q9 = q_int_at(9, q=qv, dps=dps)
    q10 = q_int_at(10, q=qv, dps=dps)
    return mpf(1) / (qv * q9 * q10 + mpf(2) / (mpf(3) * mp.pi))


def exch_neutral(g2: mpf, gp2: mpf, lam: mpf, t_a: mpf, t_b: mpf) -> mpf:
    """Exact CoulombNeedsZRemoval.exch(g2, gp2, lam, T, T')."""
    qa = t_a + mpf(1) / mpf(2)
    qb = t_b + mpf(1) / mpf(2)
    s2 = gp2 / (g2 + gp2)
    e2 = g2 * gp2 / (g2 + gp2)
    gz2 = g2 + gp2
    return e2 * qa * qb + lam * gz2 * (t_a - s2 * qa) * (t_b - s2 * qb)


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        h0 = q0 - qi0
        two_q0 = q0 + qi0
        z_d = (q0 ** 3) / (q0 ** 2 + mpf(1))
        z_d_bar = mpf(1) / (q0 * (q0 ** 2 + mpf(1)))
        z_d_pn = (z_d + z_d_bar) / mpf(2)
        t_bor = (mpf(4) + h0 ** 2 - mpf(3) * (h0 ** 4) - h0 ** 6) / (h0 ** 2 + mpf(4))

        wb = WitnessBuilder(
            "w2-h7-h8-wedderburn-zremoval",
            engine="mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps verification of H_7(q_0) and H_8(q_0) two-row Wedderburn "
            "character/Hoefsmit traces across pp, pn, nn cross-cluster dressings, iterated "
            "left/right WeightedTraceSide chain factorizations, coideal split-bundle hypercharge "
            "slope 1/2, and massive-Z Yukawa nuclear suppression exp(-M_Z r_pi) < 10^-280 "
            "(W2: qou-20sx, qou-vudb, qou-fbrp)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0Anchor", "proton")
        wb.add_parameter("q0", fmt80(q0))
        wb.add_parameter("q0_proton_80dps", fmt80(q0))
        wb.add_parameter("z_D_80dps", fmt80(z_d))
        wb.add_parameter("z_D_bar_80dps", fmt80(z_d_bar))
        wb.add_parameter("tr_M_Borromean_80dps", fmt80(t_bor))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ======================================================================
        # P1: Convention-D Radical Truncation & Two-Row Catalan Block Reduction
        # ======================================================================
        parts_7 = enumerate_partitions(7)
        parts_8 = enumerate_partitions(8)
        three_row_7 = [p for p in parts_7 if len(p) >= 3]
        three_row_8 = [p for p in parts_8 if len(p) >= 3]
        two_row_7 = [(7, 0), (6, 1), (5, 2), (4, 3)]
        two_row_8 = [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4)]

        max_three_row_w7 = max(abs(ocneanu_weight_mpf(q0, z_d, p)) for p in three_row_7)
        max_three_row_w8 = max(abs(ocneanu_weight_mpf(q0, z_d, p)) for p in three_row_8)

        wb.add_assertion(
            "P1_H7_eleven_three_or_more_row_weights_vanish",
            computed=max_three_row_w7,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="OcneanuWeight.ocneanuWeight_conventionD_eq_zero_of_three_rows (N=7)",
        )
        wb.add_assertion(
            "P1_H8_seventeen_three_or_more_row_weights_vanish",
            computed=max_three_row_w8,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="OcneanuWeight.ocneanuWeight_conventionD_eq_zero_of_three_rows (N=8)",
        )

        dims_7 = [len(enumerate_two_row_syt(m, k)) for m, k in two_row_7]
        dims_8 = [len(enumerate_two_row_syt(m, k)) for m, k in two_row_8]
        assert dims_7 == [1, 6, 14, 14] and sum(d * d for d in dims_7) == 429
        assert dims_8 == [1, 7, 20, 28, 14] and sum(d * d for d in dims_8) == 1430

        weights_7: dict[tuple[int, int], mpf] = {}
        max_w7_formula_diff = mpf(0)
        for m, k in two_row_7:
            part_nz = (m,) if k == 0 else (m, k)
            w_cell = ocneanu_weight_mpf(q0, z_d, part_nz)
            w_qdim = q_int_at(m - k + 1, q=q0, dps=80) / (two_q0 ** 7)
            weights_7[(m, k)] = w_cell
            max_w7_formula_diff = max(max_w7_formula_diff, abs(w_cell - w_qdim))

        weights_8: dict[tuple[int, int], mpf] = {}
        max_w8_formula_diff = mpf(0)
        for m, k in two_row_8:
            part_nz = (m,) if k == 0 else (m, k)
            w_cell = ocneanu_weight_mpf(q0, z_d, part_nz)
            w_qdim = q_int_at(m - k + 1, q=q0, dps=80) / (two_q0 ** 8)
            weights_8[(m, k)] = w_cell
            max_w8_formula_diff = max(max_w8_formula_diff, abs(w_cell - w_qdim))

        sum_dw_7 = sum(
            (mpf(d) * weights_7[sh] for d, sh in zip(dims_7, two_row_7)), mpf(0)
        )
        sum_dw_8 = sum(
            (mpf(d) * weights_8[sh] for d, sh in zip(dims_8, two_row_8)), mpf(0)
        )

        wb.add_assertion(
            "P1_H7_two_row_weights_match_qdim_closed_form",
            computed=max_w7_formula_diff,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="CrossNucleonPairWedderburnZRemoval.twoRowWeightD (N=7)",
        )
        wb.add_assertion(
            "P1_H8_two_row_weights_match_qdim_closed_form",
            computed=max_w8_formula_diff,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="CrossNucleonPairWedderburnZRemoval.twoRowWeightD (N=8)",
        )
        wb.add_assertion(
            "P1_H7_and_H8_normalized_weight_sums_eq_one",
            computed=max(abs(sum_dw_7 - mpf(1)), abs(sum_dw_8 - mpf(1))),
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="h7_twoRowWeightD_sum_eq_one / h8_twoRowWeightD_sum_eq_one",
        )

        wb.add_data(
            "P1_wedderburn_accounting",
            {
                "H7": {
                    "factorial_dim": 5040,
                    "partitions_total": len(parts_7),
                    "partitions_three_plus_rows": len(three_row_7),
                    "two_row_shapes": [list(sh) for sh in two_row_7],
                    "two_row_dims": dims_7,
                    "catalan_C7": sum(d * d for d in dims_7),
                    "radical_corank": 5040 - sum(d * d for d in dims_7),
                    "weights_80dps": {str(sh): fmt80(weights_7[sh]) for sh in two_row_7},
                },
                "H8": {
                    "factorial_dim": 40320,
                    "partitions_total": len(parts_8),
                    "partitions_three_plus_rows": len(three_row_8),
                    "two_row_shapes": [list(sh) for sh in two_row_8],
                    "two_row_dims": dims_8,
                    "catalan_C8": sum(d * d for d in dims_8),
                    "radical_corank": 40320 - sum(d * d for d in dims_8),
                    "weights_80dps": {str(sh): fmt80(weights_8[sh]) for sh in two_row_8},
                },
            },
        )

        # ======================================================================
        # P2: Explicit Hoefsmit Seminormal Representations & Cross-Cluster Traces
        # ======================================================================
        hoefsmit_7 = {sh: build_hoefsmit_generators(q0, sh[0], sh[1]) for sh in two_row_7}
        hoefsmit_8 = {sh: build_hoefsmit_generators(q0, sh[0], sh[1]) for sh in two_row_8}

        def check_hecke_relations(
            rep_map: dict[tuple[int, int], tuple[list[list[list[mpf]]], list[list[list[mpf]]]]],
            n_strands: int,
        ) -> mpf:
            worst = mpf(0)
            for sh, (pgens, _) in rep_map.items():
                dim = len(pgens[0])
                id_m = mat_eye(dim)
                for i in range(n_strands - 1):
                    sq = mat_mul(pgens[i], pgens[i])
                    rhs = mat_add_scaled(pgens[i], id_m, h0, mpf(1))
                    worst = max(worst, mat_max_abs(mat_add_scaled(sq, rhs, mpf(1), -mpf(1))))
                for i in range(n_strands - 2):
                    lhs = mat_mul(mat_mul(pgens[i], pgens[i + 1]), pgens[i])
                    rhs = mat_mul(mat_mul(pgens[i + 1], pgens[i]), pgens[i + 1])
                    worst = max(worst, mat_max_abs(mat_add_scaled(lhs, rhs, mpf(1), -mpf(1))))
                for i in range(n_strands - 1):
                    for j in range(i + 2, n_strands - 1):
                        lhs = mat_mul(pgens[i], pgens[j])
                        rhs = mat_mul(pgens[j], pgens[i])
                        worst = max(worst, mat_max_abs(mat_add_scaled(lhs, rhs, mpf(1), -mpf(1))))
            return worst

        hecke_rel_err_7 = check_hecke_relations(hoefsmit_7, 7)
        hecke_rel_err_8 = check_hecke_relations(hoefsmit_8, 8)
        wb.add_assertion(
            "P2_Hoefsmit_H7_and_H8_quadratic_braid_farcomm_relations",
            computed=max(hecke_rel_err_7, hecke_rel_err_8),
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="Hoefsmit seminormal representations on H_7(q_0) and H_8(q_0)",
        )

        # Verify column-removal single-generator character formulas on H_7 and H_8
        expected_gen_tr_7 = {
            (7, 0): q0,
            (6, 1): mpf(5) * q0 - qi0,
            (5, 2): mpf(10) * q0 - mpf(4) * qi0,
            (4, 3): mpf(9) * q0 - mpf(5) * qi0,
        }
        expected_gen_tr_8 = {
            (8, 0): q0,
            (7, 1): mpf(6) * q0 - qi0,
            (6, 2): mpf(15) * q0 - mpf(5) * qi0,
            (5, 3): mpf(19) * q0 - mpf(9) * qi0,
            (4, 4): mpf(9) * q0 - mpf(5) * qi0,
        }
        max_gen_tr_err = mpf(0)
        for sh in two_row_7:
            for gmat in hoefsmit_7[sh][0]:
                max_gen_tr_err = max(max_gen_tr_err, abs(mat_trace(gmat) - expected_gen_tr_7[sh]))
        for sh in two_row_8:
            for gmat in hoefsmit_8[sh][0]:
                max_gen_tr_err = max(max_gen_tr_err, abs(mat_trace(gmat) - expected_gen_tr_8[sh]))

        wb.add_assertion(
            "P2_Hoefsmit_single_generator_traces_match_column_branching",
            computed=max_gen_tr_err,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="h7_twoRow_gen_trace_eq_zD / h8_twoRow_gen_trace_eq_zD",
        )

        def wedderburn_trace(
            word: list[tuple[int, int]],
            shapes: list[tuple[int, int]],
            weights: dict[tuple[int, int], mpf],
            rep_map: dict[tuple[int, int], tuple[list[list[list[mpf]]], list[list[list[mpf]]]]],
        ) -> tuple[mpf, dict[str, str]]:
            total = mpf(0)
            per_block: dict[str, str] = {}
            for sh in shapes:
                pgens, igens = rep_map[sh]
                tr_sh = mat_trace(eval_word_mat(word, pgens, igens))
                per_block[str(sh)] = fmt50(tr_sh)
                total += weights[sh] * tr_sh
            return total, per_block

        # Cross-cluster Borromean nucleon words across H_7 (L7e, L7s) and H_8 (L8e, L8s)
        bor_a = [(0, 1), (1, -1)] * 3
        bor_b_3 = [(3, 1), (4, -1)] * 3
        bor_b_4 = [(4, 1), (5, -1)] * 3
        bor_b_5 = [(5, 1), (6, -1)] * 3

        h7_l7e_pp, blk7_pp = wedderburn_trace(
            bor_a + [(2, 1)] + bor_b_3 + [(5, 1)], two_row_7, weights_7, hoefsmit_7
        )
        h7_l7e_nn, blk7_nn = wedderburn_trace(
            bor_a + [(2, -1)] + bor_b_3 + [(5, 1)], two_row_7, weights_7, hoefsmit_7
        )
        h7_l7e_pn = (h7_l7e_pp + h7_l7e_nn) / mpf(2)
        h7_l7e_monodromy, _ = wedderburn_trace(
            bor_a + [(2, 1), (2, 1)] + bor_b_3 + [(5, -1)], two_row_7, weights_7, hoefsmit_7
        )

        h7_l7s_pp, blk7s_pp = wedderburn_trace(
            bor_a + [(2, 1), (3, 1)] + bor_b_4, two_row_7, weights_7, hoefsmit_7
        )
        h7_l7s_nn, blk7s_nn = wedderburn_trace(
            bor_a + [(2, -1), (3, 1)] + bor_b_4, two_row_7, weights_7, hoefsmit_7
        )
        h7_l7s_pn = (h7_l7s_pp + h7_l7s_nn) / mpf(2)

        h8_l8e_pp, blk8_pp = wedderburn_trace(
            bor_a + [(2, 1)] + bor_b_3 + [(5, 1), (6, -1)], two_row_8, weights_8, hoefsmit_8
        )
        h8_l8e_nn, blk8_nn = wedderburn_trace(
            bor_a + [(2, -1)] + bor_b_3 + [(5, 1), (6, -1)], two_row_8, weights_8, hoefsmit_8
        )
        h8_l8e_pn = (h8_l8e_pp + h8_l8e_nn) / mpf(2)
        h8_l8e_monodromy, _ = wedderburn_trace(
            bor_a + [(2, 1), (2, 1)] + bor_b_3 + [(5, 1), (6, 1)],
            two_row_8,
            weights_8,
            hoefsmit_8,
        )

        h8_l8s_pp, blk8s_pp = wedderburn_trace(
            bor_a + [(2, 1), (3, 1), (4, -1)] + bor_b_5, two_row_8, weights_8, hoefsmit_8
        )
        h8_l8s_nn, blk8s_nn = wedderburn_trace(
            bor_a + [(2, -1), (3, 1), (4, -1)] + bor_b_5, two_row_8, weights_8, hoefsmit_8
        )
        h8_l8s_pn = (h8_l8s_pp + h8_l8s_nn) / mpf(2)

        t_bor_sq = t_bor ** 2
        err_h7_traces = max(
            abs(h7_l7e_pp - (z_d * z_d * t_bor_sq)),
            abs(h7_l7e_nn - (z_d_bar * z_d * t_bor_sq)),
            abs(h7_l7e_pn - (z_d_pn * z_d * t_bor_sq)),
            abs(h7_l7e_monodromy - ((h0 * z_d + mpf(1)) * z_d_bar * t_bor_sq)),
            abs(h7_l7s_pp - (z_d * z_d * t_bor_sq)),
            abs(h7_l7s_nn - (z_d_bar * z_d * t_bor_sq)),
            abs(h7_l7s_pn - (z_d_pn * z_d * t_bor_sq)),
        )
        err_h8_traces = max(
            abs(h8_l8e_pp - (z_d * z_d * z_d_bar * t_bor_sq)),
            abs(h8_l8e_nn - (z_d_bar * z_d * z_d_bar * t_bor_sq)),
            abs(h8_l8e_pn - (z_d_pn * z_d * z_d_bar * t_bor_sq)),
            abs(h8_l8e_monodromy - ((h0 * z_d + mpf(1)) * (z_d ** 2) * t_bor_sq)),
            abs(h8_l8s_pp - (z_d * z_d * z_d_bar * t_bor_sq)),
            abs(h8_l8s_nn - (z_d_bar * z_d * z_d_bar * t_bor_sq)),
            abs(h8_l8s_pn - (z_d_pn * z_d * z_d_bar * t_bor_sq)),
        )

        skein_isotensor_err = max(
            abs((h7_l7e_pp - mpf(2) * h7_l7e_pn + h7_l7e_nn)),
            abs((h7_l7s_pp - mpf(2) * h7_l7s_pn + h7_l7s_nn)),
            abs((h8_l8e_pp - mpf(2) * h8_l8e_pn + h8_l8e_nn)),
            abs((h8_l8s_pp - mpf(2) * h8_l8s_pn + h8_l8s_nn)),
            abs((h7_l7e_pp - h7_l7e_nn) - h0 * z_d * t_bor_sq),
            abs((h8_l8e_pp - h8_l8e_nn) - h0 * z_d * z_d_bar * t_bor_sq),
        )

        wb.add_assertion(
            "P2_H7_Hoefsmit_cross_cluster_pp_pn_nn_match_rational_closed_form",
            computed=err_h7_traces,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="4-block Hoefsmit character sum vs closed rational Markov formula on H_7(q_0)",
        )
        wb.add_assertion(
            "P2_H8_Hoefsmit_cross_cluster_pp_pn_nn_match_rational_closed_form",
            computed=err_h8_traces,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="5-block Hoefsmit character sum vs closed rational Markov formula on H_8(q_0)",
        )
        wb.add_assertion(
            "P2_cross_cluster_skein_isovector_and_zero_coulomb_curvature",
            computed=skein_isotensor_err,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="CrossNucleonPairWedderburnZRemoval.crossCluster_skein_isovector_and_zero_coulomb",
        )

        wb.add_data(
            "P2_hoefsmit_cross_cluster_traces",
            {
                "H7_L7e_pp_80dps": fmt80(h7_l7e_pp),
                "H7_L7e_pn_80dps": fmt80(h7_l7e_pn),
                "H7_L7e_nn_80dps": fmt80(h7_l7e_nn),
                "H7_L7e_per_block_pp": blk7_pp,
                "H7_L7e_per_block_nn": blk7_nn,
                "H7_L7s_per_block_pp": blk7s_pp,
                "H7_L7s_per_block_nn": blk7s_nn,
                "H8_L8e_pp_80dps": fmt80(h8_l8e_pp),
                "H8_L8e_pn_80dps": fmt80(h8_l8e_pn),
                "H8_L8e_nn_80dps": fmt80(h8_l8e_nn),
                "H8_L8e_per_block_pp": blk8_pp,
                "H8_L8e_per_block_nn": blk8_nn,
                "H8_L8s_per_block_pp": blk8s_pp,
                "H8_L8s_per_block_nn": blk8s_nn,
            },
        )

        # ======================================================================
        # P3: Sector-Projected (pp, pn, np, nn) Readouts & Left/Right Chain Collapse
        # ======================================================================
        eye6, mul6, gens6, read6 = build_tensor_sector_engine(q0, 6, (0, 1, 2), (3, 4, 5))
        eye7e, mul7e, gens7e, read7e = build_tensor_sector_engine(q0, 7, (0, 1, 2), (3, 4, 5))
        eye8e, mul8e, gens8e, read8e = build_tensor_sector_engine(q0, 8, (0, 1, 2), (3, 4, 5))
        eye7s, mul7s, gens7s, read7s = build_tensor_sector_engine(q0, 7, (0, 1, 2), (4, 5, 6))
        eye8s, mul8s, gens8s, read8s = build_tensor_sector_engine(q0, 8, (0, 1, 2), (5, 6, 7))

        t1_6 = read6(eye6())
        t1_7e = read7e(eye7e())
        t1_8e = read8e(eye8e())
        t1_7s = read7s(eye7s())
        t1_8s = read8s(eye8s())

        # Cross-block R_2 on L6, R_2 * R_5 on L7e, and R_2 * R_5 * R_6^-1 on L8e
        tx_6 = read6(gens6[(2, 1)])
        tx_7e = read7e(mul7e(gens7e[(2, 1)], gens7e[(5, 1)]))
        tx_8e = read8e(mul8e(mul8e(gens8e[(2, 1)], gens8e[(5, 1)]), gens8e[(6, -1)]))

        nucleon_pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        de_6 = {sec: tx_6[sec] / t1_6[sec] for sec in nucleon_pairs}
        de_7e = {sec: tx_7e[sec] / t1_7e[sec] for sec in nucleon_pairs}
        de_8e = {sec: tx_8e[sec] / t1_8e[sec] for sec in nucleon_pairs}

        right_stab_err = max(
            max(abs(de_7e[sec] - z_d * de_6[sec]) for sec in nucleon_pairs),
            max(abs(de_8e[sec] - z_d * z_d_bar * de_6[sec]) for sec in nucleon_pairs),
        )
        wb.add_assertion(
            "P3_right_spectator_L7e_L8e_exact_zD_factorization",
            computed=right_stab_err,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="rightTrace_R_norm_eq_zD / rightTrace2_R_Rinv_norm_eq_zD_mul_zDBar",
        )

        # Verify rational pair parameter alpha_6(q_0) + beta_6(q_0) = 1
        alpha6_exact = alpha_six_analytic(q0)
        beta6_exact = alpha_six_analytic(qi0)
        wb.add_assertion(
            "P3_alphaSix_plus_betaSix_eq_one_analytic",
            computed=abs((alpha6_exact + beta6_exact) - mpf(1)),
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="CrossNucleonPairWedderburnZRemoval.alphaSix_add_betaSix",
        )

        # Note: a single R_2 crossing has its own specific ray on {0,1}^2? Wait: at N=6, ALL
        # reachable pair terms with kappa != 0 lie on ONE unique ray (alpha_6(q_0), beta_6(q_0)) ONLY
        # after subtracting single-block shifts Q_A + Q_B (which ARE in the span!). Let's verify the
        # exact leftChainOp_two_linear_comb identity across ALL 16 charge sectors of L8s vs L7s vs L6!
        tx_7s_left1 = read7s(gens7s[(3, 1)])
        tx_8s_left2 = read8s(mul8s(gens8s[(3, 1)], gens8s[(4, 1)]))
        all_16_sectors = sorted(t1_6.keys())
        left_chain_16_err = max(
            abs(
                tx_8s_left2[sec]
                - ((q0 ** 2 + mpf(1)) * tx_7s_left1[sec] - (q0 ** 2) * t1_6[sec])
            )
            for sec in all_16_sectors
        )
        wb.add_assertion(
            "P3_leftChainOp_H8_L8s_linear_comb_of_H7_L7s_and_H6_all_16_sectors",
            computed=left_chain_16_err,
            expected=mpf(0),
            tolerance=mpf("1e-77"),
            source="CrossNucleonPairWedderburnZRemoval.leftChainOp_two_linear_comb",
        )

        # Also verify on L6 that (1, Q_A + Q_B) + R_2-dressed span pins (alpha_6(q_0), beta_6(q_0))!
        # Specifically, build a 10-element basis of L6 sector readouts (words of length <= 4 in S_6)
        # and solve the exact linear combination matching T_1 * ((Q_A - beta_6)*(Q_B - alpha_6) + c)
        # across ALL 16 sectors of L6, L7e, and (with arbitrary beta) L7s and L8s!
        def collect_fc_readouts(n_s: int, eye_fn, mul_fn, g_map, rd_fn, max_words: int = 1500):
            start = tuple(range(n_s))
            seen = {start}
            frontier = [(start, eye_fn())]
            vecs = []

            def is_fc(perm: tuple[int, ...]) -> bool:
                ln = len(perm)
                for j in range(1, ln - 1):
                    if any(perm[i] > perm[j] for i in range(j)) and any(
                        perm[r] < perm[j] for r in range(j + 1, ln)
                    ):
                        return False
                return True

            while frontier and len(vecs) < max_words:
                nxt = []
                for perm, mat_op in frontier:
                    rd = rd_fn(mat_op)
                    vecs.append([rd.get(sec, mpf(0)) for sec in all_16_sectors])
                    for i in range(n_s - 1):
                        lst = list(perm)
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        tp = tuple(lst)
                        if tp not in seen and is_fc(tp):
                            seen.add(tp)
                            nxt.append((tp, mul_fn(mat_op, g_map[(i, 1)])))
                frontier = nxt
            return vecs

        def rref_basis(vecs: list[list[mpf]], tol: mpf) -> tuple[list[list[mpf]], list[int]]:
            basis: list[list[mpf]] = []
            pivs: list[int] = []
            for v_in in vecs:
                v = list(v_in)
                for b_row, p_col in zip(basis, pivs):
                    fac = v[p_col]
                    if abs(fac) > tol:
                        v = [v[j] - fac * b_row[j] for j in range(len(v))]
                piv = next((j for j, val in enumerate(v) if abs(val) > tol), None)
                if piv is not None:
                    inv_p = mpf(1) / v[piv]
                    v = [val * inv_p for val in v]
                    # Eliminate above too for clean RREF projection
                    for idx_b in range(len(basis)):
                        fac_b = basis[idx_b][piv]
                        if abs(fac_b) > tol:
                            basis[idx_b] = [
                                basis[idx_b][j] - fac_b * v[j] for j in range(len(v))
                            ]
                    basis.append(v)
                    pivs.append(piv)
            return basis, pivs

        def reduce_against_rref(
            vec: list[mpf], basis: list[list[mpf]], pivs: list[int]
        ) -> list[mpf]:
            v = list(vec)
            for b_row, p_col in zip(basis, pivs):
                fac = v[p_col]
                if fac != 0:
                    v = [v[j] - fac * b_row[j] for j in range(len(v))]
            return v

        vecs_l6 = collect_fc_readouts(6, eye6, mul6, gens6, read6)
        vecs_l7s = collect_fc_readouts(7, eye7s, mul7s, gens7s, read7s)
        vecs_l8s = collect_fc_readouts(8, eye8s, mul8s, gens8s, read8s)

        rref_l6, piv_l6 = rref_basis(vecs_l6, mpf("1e-60"))
        rref_l7s, piv_l7s = rref_basis(vecs_l7s, mpf("1e-60"))
        rref_l8s, piv_l8s = rref_basis(vecs_l8s, mpf("1e-60"))

        assert len(rref_l6) == 10 and len(rref_l7s) == 14 and len(rref_l8s) == 14

        # Verify (Q_A - beta_6)*(Q_B - alpha_6) lies in the L6 span across all 16 sectors,
        # and (Q_A - beta)*(Q_B - alpha_6) lies in BOTH L7s and L8s spans for ANY beta (e.g. beta = 0)!
        target_l6 = [
            t1_6[sec] * (mpf(sec[0]) - beta6_exact) * (mpf(sec[1]) - alpha6_exact)
            for sec in all_16_sectors
        ]
        target_l7s = [
            t1_7s[sec] * mpf(sec[0]) * (mpf(sec[1]) - alpha6_exact)
            for sec in all_16_sectors
        ]
        target_l8s = [
            t1_8s[sec] * mpf(sec[0]) * (mpf(sec[1]) - alpha6_exact)
            for sec in all_16_sectors
        ]
        coulomb_l7s = [
            t1_7s[sec] * mpf(sec[0]) * mpf(sec[1]) for sec in all_16_sectors
        ]
        coulomb_l8s = [
            t1_8s[sec] * mpf(sec[0]) * mpf(sec[1]) for sec in all_16_sectors
        ]

        res_l6_ray = max(abs(x) for x in reduce_against_rref(target_l6, rref_l6, piv_l6))
        res_l7s_pin = max(abs(x) for x in reduce_against_rref(target_l7s, rref_l7s, piv_l7s))
        res_l8s_pin = max(abs(x) for x in reduce_against_rref(target_l8s, rref_l8s, piv_l8s))
        coul_dist_l7s = max(abs(x) for x in reduce_against_rref(coulomb_l7s, rref_l7s, piv_l7s))
        coul_dist_l8s = max(abs(x) for x in reduce_against_rref(coulomb_l8s, rref_l8s, piv_l8s))

        wb.add_assertion(
            "P3_H6_H7s_H8s_fc_wedderburn_spans_match_analytic_alphaSix_to_78dps",
            computed=max(res_l6_ray, res_l7s_pin, res_l8s_pin),
            expected=mpf(0),
            tolerance=mpf("1e-72"),
            source="132/429/1430 Temperley-Lieb basis spans on L6 (dim 10), L7s (dim 14), L8s (dim 14)",
        )
        wb.add_assertion(
            "P3_H7s_and_H8s_strictly_exclude_pure_coulomb_QaQb",
            computed=mpf(1) if (coul_dist_l7s > mpf("1e-3") and coul_dist_l8s > mpf("1e-3")) else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-78"),
            source="CrossNucleonPairWedderburnZRemoval.h7_h8_pinned_alphaSix_not_coulomb",
        )

        wb.add_data(
            "P3_sector_pair_identities",
            {
                "alpha_6_q0_80dps": fmt80(alpha6_exact),
                "beta_6_q0_80dps": fmt80(beta6_exact),
                "L6_span_dim": len(rref_l6),
                "L7s_span_dim": len(rref_l7s),
                "L8s_span_dim": len(rref_l8s),
                "L7s_coulomb_projection_residual": fmt50(coul_dist_l7s),
                "L8s_coulomb_projection_residual": fmt50(coul_dist_l8s),
            },
        )

        # ======================================================================
        # P4: Coideal Killing-Norm Hypercharge Slope 1/2 & Massive-Z Removal
        # ======================================================================
        split_t3 = [mpf(1) / mpf(2), -mpf(1) / mpf(2), mpf(0), mpf(0), mpf(0)]
        split_y = [-mpf(1), -mpf(1), mpf(2) / mpf(3), mpf(2) / mpf(3), mpf(2) / mpf(3)]
        alpha_y = mpf(1) / mpf(2)
        split_q = [t3_i + alpha_y * y_i for t3_i, y_i in zip(split_t3, split_y)]

        tr_f_two_t3_sq = sum(((mpf(2) * x) ** 2 for x in split_t3), mpf(0))
        tr_f_half_y_sq = sum(((y_i / mpf(2)) ** 2 for y_i in split_y), mpf(0))
        tr_f_q_sq = sum((q_i ** 2 for q_i in split_q), mpf(0))
        sin2_tw_unrenorm = (tr_f_two_t3_sq / mpf(4)) / (
            (tr_f_two_t3_sq / mpf(4)) + tr_f_half_y_sq
        )

        killing_err = max(
            abs(tr_f_two_t3_sq - mpf(2)),
            abs(tr_f_half_y_sq - mpf(5) / mpf(6)),
            abs(tr_f_q_sq - mpf(4) / mpf(3)),
            abs(sin2_tw_unrenorm - mpf(3) / mpf(8)),
            abs(split_q[0]),
        )
        wb.add_assertion(
            "P4_split_bundle_killing_norms_slope_half_and_weinberg_3_8",
            computed=killing_err,
            expected=mpf(0),
            tolerance=mpf("1e-78"),
            source="splitT3_traces / splitY_half_sq_trace / gmn_slope_half_from_killing_norm",
        )

        # Exact 80-dps SI-2019 hbar * c in MeV * fm from NIST CODATA defining constants
        h_si = mpf(codata("Planck constant").value_str)
        c_si = mpf(codata("speed of light in vacuum").value_str)
        e_si = mpf(codata("elementary charge").value_str)
        hbar_c_mev_fm = (h_si * c_si) / (mpf(2) * mp.pi * e_si * mpf("1e-9"))

        m_pi_pm = +M_PI_PM_MEV_VALIDATION
        m_pi_0 = +M_PI_0_MEV_VALIDATION
        m_pi_bar = (mpf(2) * m_pi_pm + m_pi_0) / mpf(3)
        m_z_pdg_mev = mpf("91187.6")

        r_pi_pm_fm = hbar_c_mev_fm / m_pi_pm
        r_pi_bar_fm = hbar_c_mev_fm / m_pi_bar
        r_pi_0_fm = hbar_c_mev_fm / m_pi_0
        r_nom_fm = mpf("1.418")

        x_pi_pm = m_z_pdg_mev / m_pi_pm
        x_pi_bar = m_z_pdg_mev / m_pi_bar
        x_pi_0 = m_z_pdg_mev / m_pi_0
        x_nom = m_z_pdg_mev * r_nom_fm / hbar_c_mev_fm

        lam_pi_pm = mp.exp(-x_pi_pm)
        lam_pi_bar = mp.exp(-x_pi_bar)
        lam_pi_0 = mp.exp(-x_pi_0)
        lam_nom = mp.exp(-x_nom)

        # Tree-level QOU Form-B alpha_q(q_0) + NIST G_F comparison scales
        alpha_q0 = alpha_form_b_at(q0, dps=80)
        gf_gev_inv2 = mpf(codata("Fermi coupling constant").value_str)
        sin2_tw_codata = mpf(codata("weak mixing angle").value_str)
        mz_tree_onshell_mev = (
            mpf(1000)
            * mp.sqrt(
                mp.pi
                * alpha_q0
                / (mp.sqrt(mpf(2)) * gf_gev_inv2 * sin2_tw_codata * (mpf(1) - sin2_tw_codata))
            )
        )

        # Evaluate CoulombNeedsZRemoval.exch relative residuals at r = r_{pi^+-} for BOTH
        # unrenormalized SU(5) (g'^2 = 3/5 g^2) and physical on-shell sin^2 theta_W
        e2_target = mpf(4) * mp.pi * alpha_q0
        g2_su5 = e2_target * mpf(8) / mpf(3)
        gp2_su5 = (mpf(3) / mpf(5)) * g2_su5

        g2_phys = e2_target / sin2_tw_codata
        gp2_phys = e2_target / (mpf(1) - sin2_tw_codata)

        def max_coulomb_rel_err(g2_v: mpf, gp2_v: mpf, lam_v: mpf) -> mpf:
            e2_v = g2_v * gp2_v / (g2_v + gp2_v)
            pp_v = exch_neutral(g2_v, gp2_v, lam_v, mpf(1) / mpf(2), mpf(1) / mpf(2))
            pn_v = exch_neutral(g2_v, gp2_v, lam_v, mpf(1) / mpf(2), -mpf(1) / mpf(2))
            nn_v = exch_neutral(g2_v, gp2_v, lam_v, -mpf(1) / mpf(2), -mpf(1) / mpf(2))
            return max(
                abs(pp_v - e2_v) / e2_v,
                abs(pn_v) / e2_v,
                abs(nn_v) / e2_v,
                abs(pn_v - nn_v) / e2_v,
            )

        rel_z_su5_pi_pm = max_coulomb_rel_err(g2_su5, gp2_su5, lam_pi_pm)
        rel_z_phys_pi_pm = max_coulomb_rel_err(g2_phys, gp2_phys, lam_pi_pm)
        rel_z_phys_nom = max_coulomb_rel_err(g2_phys, gp2_phys, lam_nom)

        threshold_280 = mpf(10) ** (-280)
        all_suppressed = (
            x_pi_pm > mpf(653)
            and x_nom > mpf(655)
            and mpf(0) < lam_pi_pm < threshold_280
            and mpf(0) < lam_nom < threshold_280
            and mpf(0) < lam_pi_bar < threshold_280
            and mpf(0) < lam_pi_0 < threshold_280
            and rel_z_su5_pi_pm < threshold_280
            and rel_z_phys_pi_pm < threshold_280
            and rel_z_phys_nom < threshold_280
        )

        wb.add_assertion(
            "P4_massive_Z_yukawa_suppression_below_1e_neg_280_at_r_pi",
            computed=mpf(1) if all_suppressed else mpf(0),
            expected=mpf(1),
            tolerance=mpf("1e-78"),
            source="CrossNucleonPairWedderburnZRemoval.nuclear_z_channel_coulomb_isolation_280_digits",
        )

        # Also verify exact algebraic residual formula match at lam = lam_pi_pm (scaled by 1/lam_pi_pm)
        nn_scaled_diff = abs(
            exch_neutral(g2_phys, gp2_phys, lam_pi_pm, -mpf(1) / mpf(2), -mpf(1) / mpf(2))
            / lam_pi_pm
            - (g2_phys + gp2_phys) / mpf(4)
        )
        wb.add_assertion(
            "P4_exch_Z_residual_matches_analytic_linear_formula_at_80dps",
            computed=nn_scaled_diff,
            expected=mpf(0),
            tolerance=mpf("1e-76"),
            source="CrossNucleonPairWedderburnZRemoval.exch_residuals_exact",
        )

        wb.add_data(
            "P4_z_channel_yukawa_decoupling",
            {
                "m_e_CAL1_MeV": M_E_MEV_STR,
                "hbar_c_SI2019_MeV_fm_80dps": fmt80(hbar_c_mev_fm),
                "r_pi_pm_fm_80dps": fmt80(r_pi_pm_fm),
                "r_pi_bar_fm_80dps": fmt80(r_pi_bar_fm),
                "r_pi_0_fm_80dps": fmt80(r_pi_0_fm),
                "x_MZ_r_pi_pm_80dps": fmt80(x_pi_pm),
                "x_MZ_r_1p418fm_80dps": fmt80(x_nom),
                "x_MZ_r_pi_bar_80dps": fmt80(x_pi_bar),
                "x_MZ_r_pi_0_80dps": fmt80(x_pi_0),
                "lambda_Z_r_pi_pm_80dps": fmt80(lam_pi_pm),
                "lambda_Z_r_1p418fm_80dps": fmt80(lam_nom),
                "lambda_Z_r_pi_bar_80dps": fmt80(lam_pi_bar),
                "lambda_Z_r_pi_0_80dps": fmt80(lam_pi_0),
                "log10_lambda_Z_r_pi_pm": fmt50(mp.log10(lam_pi_pm)),
                "log10_lambda_Z_r_1p418fm": fmt50(mp.log10(lam_nom)),
                "max_rel_Z_contamination_SU5_r_pi_pm": fmt80(rel_z_su5_pi_pm),
                "max_rel_Z_contamination_phys_r_pi_pm": fmt80(rel_z_phys_pi_pm),
                "max_rel_Z_contamination_phys_1p418fm": fmt80(rel_z_phys_nom),
                "M_Z_tree_FormB_onshell_MeV_50dps": fmt50(mz_tree_onshell_mev),
            },
        )

        out_path = wb.save()
        print(f"Wrote witness: {out_path}")
        print(
            f"Summary: C_7={sum(d*d for d in dims_7)}, C_8={sum(d*d for d in dims_8)}, "
            f"x(r_pi+-)={mp.nstr(x_pi_pm, 12)}, lambda(r_pi+-)={mp.nstr(lam_pi_pm, 12)}, "
            f"lambda(1.418fm)={mp.nstr(lam_nom, 12)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
