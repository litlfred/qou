#!/usr/bin/env python3
"""bring_fano_octonion_blichfeldt_su3_probe.py — 80-dps Bring Genus-3 Fano Plane,
S_4 Maximal-Subgroup Bridge, Octonion Multiplication, and 168-Element Blichfeldt
Subgroup of SU(3)_c Probe (Wave 6B, Bean qou-ys29).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Eightfold/BringGenusThreeFanoOctonionAndBlichfeldtSU3.lean`

STRICT ANTI-FITTING & PRECISION DISCIPLINE
------------------------------------------
1. ZERO empirical parameters, ZERO fitting, and ZERO calibration inputs (`q0Anchor = "independent"`).
2. ZERO binary64 (`float64`) arithmetic, ZERO `math` or `numpy` imports, ZERO
   `float(...)` or `complex(...)` calls, ZERO float or `1j` literals, and ZERO raw JSON
   floats in the emitted witness (`witness_raw_float64_audit` = 0).
3. Evaluates at 80-dps output precision (`mp.workdps(95)` guard digits):
   - Part 1: Exact `GL(3, F_2) ~= PSL(2, 7)` (`168` matrices), Fano plane `PG(2, 2)`
     (`7` points, `7` lines), conjugacy class partition `1 + 21 + 56 + 42 + 24 + 24 = 168`
     (orders `1, 2, 3, 4, 7, 7`), `168 !| 120` obstruction, and the common maximal
     subgroup `S_4` (`24` elements) bridging `Aut(Bring) = S_5` (index `5`) and
     `Aut(Fano) = GL(3, F_2)` (point stabilizer of index `7` and line stabilizer of index `7`).
   - Part 2: Explicit generation of all `168` unitary `3x3` Blichfeldt matrices
     `G_168 < SU(3)_c` over `Q(zeta_7)` from `T = diag(zeta_7, zeta_7^2, zeta_7^4)`,
     cyclic shift `R`, and Klein's involution `-S`, certifying unitarity, unit determinant,
     character spectrum `{3, -1, 0, 1, (-1 + i*sqrt(7))/2, (-1 - i*sqrt(7))/2}`, and
     Schur irreducibility `(1/168) sum_{U in G_168} |tr(U)|^2 = 1` to `< 10^{-88}`.
   - Part 3: Cayley-Dickson / Fano octonion algebra `O` (Degen's 8-square norm identity,
     left/right alternativity, all three Moufang identities, `28` anti-Fano non-associating
     3-subsets / `168` ordered non-associating basis triples), and exact rational linear
     derivation rank/nullity confirming `dim Der(O) = 21 - 7 = 14 = dim g_2` and
     stabilizer cutdown `D(e_7) = 0` from `14 -> 8 = dim su(3)_c` with negative-definite
     Killing forms and complex-structure compatibility on `C^3`.
"""
from __future__ import annotations

from collections import Counter
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

from qou_substrate.witness import WitnessBuilder  # noqa: E402


# ── Pure-Integer & Exact-Rational Linear Algebra Helpers (Zero `math` Import) ─
def _gcd_int(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def _binom_int(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= n - (k - i)
        den *= i
    return num // den


def _f2_vec(n: int) -> tuple[int, int, int]:
    return ((n >> 2) & 1, (n >> 1) & 1, n & 1)


def _f2_int(v: tuple[int, int, int]) -> int:
    return (v[0] << 2) | (v[1] << 1) | v[2]


def _f2_det3(m: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> int:
    a, b, c = m[0], m[1], m[2]
    val = (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )
    return val & 1


def _f2_matmul(
    a: tuple[tuple[int, int, int], ...],
    b: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple((a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]) & 1 for j in range(3))
        for i in range(3)
    )


def _f2_matvec(
    m: tuple[tuple[int, int, int], ...],
    v: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple((m[i][0] * v[0] + m[i][1] * v[1] + m[i][2] * v[2]) & 1 for i in range(3))


def _f2_charpoly(m: tuple[tuple[int, int, int], ...]) -> tuple[int, int, int, int]:
    """Return coefficients (1, c2, c1, c0) over F_2 of det(x I + M) = x^3 + c2 x^2 + c1 x + c0."""
    tr = (m[0][0] + m[1][1] + m[2][2]) & 1
    m01 = (m[0][0] * m[1][1] - m[0][1] * m[1][0]) & 1
    m02 = (m[0][0] * m[2][2] - m[0][2] * m[2][0]) & 1
    m12 = (m[1][1] * m[2][2] - m[1][2] * m[2][1]) & 1
    c1 = (m01 + m02 + m12) & 1
    c0 = _f2_det3(m)
    return (1, tr, c1, c0)


def _rref_fraction(rows: list[list[Fraction]], ncols: int) -> tuple[int, list[list[Fraction]]]:
    """Exact rational RREF returning (rank, basis_of_nullspace)."""
    mat = [ [Fraction(x) for x in r] for r in rows ]
    nrows = len(mat)
    pivot_cols: list[int] = []
    r = 0
    for c in range(ncols):
        if r >= nrows:
            break
        piv = None
        for i in range(r, nrows):
            if mat[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        scale = mat[r][c]
        mat[r] = [val / scale for val in mat[r]]
        for i in range(nrows):
            if i != r and mat[i][c] != 0:
                factor = mat[i][c]
                mat[i] = [mat[i][j] - factor * mat[r][j] for j in range(ncols)]
        pivot_cols.append(c)
        r += 1

    rank = len(pivot_cols)
    piv_set = set(pivot_cols)
    free_cols = [c for c in range(ncols) if c not in piv_set]
    null_basis: list[list[Fraction]] = []
    for fc in free_cols:
        vec = [Fraction(0)] * ncols
        vec[fc] = Fraction(1)
        for row_idx, pc in enumerate(pivot_cols):
            vec[pc] = -mat[row_idx][fc]
        null_basis.append(vec)
    return rank, null_basis


def _frobenius_norm(m: mp.matrix) -> mp.mpf:
    return mp.sqrt(
        mp.fsum(
            mp.re(m[r, c]) ** 2 + mp.im(m[r, c]) ** 2
            for r in range(m.rows)
            for c in range(m.cols)
        )
    )


def _conj_transpose(m: mp.matrix) -> mp.matrix:
    out = mp.zeros(m.cols, m.rows)
    for r in range(m.rows):
        for c in range(m.cols):
            out[c, r] = mp.conj(m[r, c])
    return out


def _mat_trace3(m: mp.matrix) -> mp.mpc:
    return m[0, 0] + m[1, 1] + m[2, 2]


def _mat_det3(m: mp.matrix) -> mp.mpc:
    return (
        m[0, 0] * (m[1, 1] * m[2, 2] - m[1, 2] * m[2, 1])
        - m[0, 1] * (m[1, 0] * m[2, 2] - m[1, 2] * m[2, 0])
        + m[0, 2] * (m[1, 0] * m[2, 1] - m[1, 1] * m[2, 0])
    )


# ── Part 1: GL(3, F_2), Fano Plane PG(2, 2), and S_4 Bridge ──────────────────
def _evaluate_part1_gl3f2_and_s4_bridge() -> tuple[dict[str, object], bool]:
    ident = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    gl3_f2: list[tuple[tuple[int, int, int], ...]] = []
    for bits in range(512):
        m = (
            ((bits >> 8) & 1, (bits >> 7) & 1, (bits >> 6) & 1),
            ((bits >> 5) & 1, (bits >> 4) & 1, (bits >> 3) & 1),
            ((bits >> 2) & 1, (bits >> 1) & 1, bits & 1),
        )
        if _f2_det3(m) == 1:
            gl3_f2.append(m)

    gl3_set = set(gl3_f2)
    order_gl3 = len(gl3_f2)

    # Inverse lookup table in GL(3, F_2)
    inv_map: dict[tuple[tuple[int, int, int], ...], tuple[tuple[int, int, int], ...]] = {}
    order_map: dict[tuple[tuple[int, int, int], ...], int] = {}
    for g in gl3_f2:
        cur = g
        k = 1
        prev = ident
        while cur != ident:
            prev = cur
            cur = _f2_matmul(cur, g)
            k += 1
        order_map[g] = k
        inv_map[g] = ident if k == 1 else prev

    # Fano plane PG(2, 2): 7 points {1..7}, 7 lines {a, b, a ^ b}
    fano_points = list(range(1, 8))
    fano_lines_set: set[frozenset[int]] = set()
    for a in fano_points:
        for b in fano_points:
            if a < b:
                c = a ^ b
                fano_lines_set.add(frozenset((a, b, c)))
    fano_lines = sorted(( tuple(sorted(ln)) for ln in fano_lines_set ))

    lines_per_point = {
        pt: sum(1 for ln in fano_lines if pt in ln) for pt in fano_points
    }
    unique_line_per_pair = all(
        sum(1 for ln in fano_lines if a in ln and b in ln) == 1
        for a in fano_points
        for b in fano_points
        if a < b
    )
    unique_pt_per_line_pair = all(
        len(set(fano_lines[i]) & set(fano_lines[j])) == 1
        for i in range(len(fano_lines))
        for j in range(i + 1, len(fano_lines))
    )

    # Verify GL(3, F_2) acts faithfully as collineation group Aut(PG(2, 2))
    collineation_perms: set[tuple[int, ...]] = set()
    preserves_all_lines = True
    for g in gl3_f2:
        perm = tuple(_f2_int(_f2_matvec(g, _f2_vec(pt))) for pt in fano_points)
        collineation_perms.add(perm)
        for ln in fano_lines_set:
            img = frozenset(_f2_int(_f2_matvec(g, _f2_vec(pt))) for pt in ln)
            if img not in fano_lines_set:
                preserves_all_lines = False

    # Conjugacy classes of GL(3, F_2)
    unvisited = set(gl3_f2)
    conj_classes: list[dict[str, object]] = []
    while unvisited:
        rep = min(unvisited)
        cls = {_f2_matmul(_f2_matmul(h, rep), inv_map[h]) for h in gl3_f2}
        unvisited -= cls
        ord_rep = order_map[rep]
        cpoly = _f2_charpoly(rep)
        conj_classes.append(
            {
                "order": ord_rep,
                "size": len(cls),
                "charpoly_f2_coeffs_x3_x2_x1_x0": list(cpoly),
            }
        )
    conj_classes.sort(key=lambda d: (int(d["order"]), int(d["size"]), d["charpoly_f2_coeffs_x3_x2_x1_x0"]))
    class_sizes = [int(c["size"]) for c in conj_classes]
    class_orders = [int(c["order"]) for c in conj_classes]

    # Point stabilizer Stab(e_7) (fixing point 7 = (1, 1, 1)) and line stabilizer Stab({1, 2, 3})
    fixed_pt = 7
    stab_pt = [g for g in gl3_f2 if _f2_int(_f2_matvec(g, _f2_vec(fixed_pt))) == fixed_pt]
    local_lines = [ln for ln in fano_lines if fixed_pt in ln]
    nonlocal_lines = [ln for ln in fano_lines if fixed_pt not in ln]

    # Explicit isomorphism Stab(e_7) -> S_4 via action on the 4 non-local Fano lines
    nonlocal_fsets = [frozenset(ln) for ln in nonlocal_lines]
    stab_pt_induced_s4: set[tuple[int, ...]] = set()
    for g in stab_pt:
        induced = tuple(
            nonlocal_fsets.index(frozenset(_f2_int(_f2_matvec(g, _f2_vec(pt))) for pt in ln))
            for ln in nonlocal_fsets
        )
        stab_pt_induced_s4.add(induced)

    stab_pt_order_hist = dict(sorted(Counter(order_map[g] for g in stab_pt).items()))

    # Verify maximality of Stab(e_7) ~= S_4 inside GL(3, F_2)
    stab_pt_set = set(stab_pt)
    stab_pt_is_maximal = True
    for g in gl3_f2:
        if g in stab_pt_set:
            continue
        gen_sub = set(stab_pt_set)
        queue = list(stab_pt_set) + [g]
        gen_sub.add(g)
        gens_here = list(stab_pt) + [g]
        while queue:
            cur = queue.pop()
            for h in gens_here:
                prod = _f2_matmul(cur, h)
                if prod not in gen_sub:
                    gen_sub.add(prod)
                    queue.append(prod)
        if len(gen_sub) != 168:
            stab_pt_is_maximal = False
            break

    # Dual check: Line stabilizer Stab({1, 2, 3}) ~= S_4 via action on the 4 complement points {4, 5, 6, 7}
    fixed_line = frozenset((1, 2, 3))
    comp_pts = [4, 5, 6, 7]
    stab_line = [
        g
        for g in gl3_f2
        if frozenset(_f2_int(_f2_matvec(g, _f2_vec(pt))) for pt in fixed_line) == fixed_line
    ]
    stab_line_induced_s4: set[tuple[int, ...]] = set()
    for g in stab_line:
        induced_l = tuple(comp_pts.index(_f2_int(_f2_matvec(g, _f2_vec(pt)))) for pt in comp_pts)
        stab_line_induced_s4.add(induced_l)
    stab_line_order_hist = dict(sorted(Counter(order_map[g] for g in stab_line).items()))

    # Bring surface S_5 comparison: |S_5| = 120, point stabilizer S_4 of order 24 (index 5, prime => maximal)
    s5_perms = list(itertools.permutations(range(5)))
    s5_stab4 = [p for p in s5_perms if p[4] == 4]
    order_s5 = len(s5_perms)
    order_s4 = len(s5_stab4)
    gcd_s5_psl27 = _gcd_int(order_s5, order_gl3)
    divides_168_120 = (order_s5 % order_gl3) == 0
    divides_7_120 = (order_s5 % 7) == 0

    irrep_dims = [1, 3, 3, 6, 7, 8]
    sum_irrep_sq = sum(d * d for d in irrep_dims)

    expected_s4_hist = {1: 1, 2: 9, 3: 8, 4: 6}
    passed = (
        order_gl3 == 168
        and len(fano_points) == 7
        and len(fano_lines) == 7
        and all(v == 3 for v in lines_per_point.values())
        and unique_line_per_pair
        and unique_pt_per_line_pair
        and preserves_all_lines
        and len(collineation_perms) == 168
        and class_sizes == [1, 21, 56, 42, 24, 24]
        and class_orders == [1, 2, 3, 4, 7, 7]
        and sum(class_sizes) == 168
        and sum_irrep_sq == 168
        and len(stab_pt) == 24
        and len(stab_pt_induced_s4) == 24
        and stab_pt_order_hist == expected_s4_hist
        and stab_pt_is_maximal
        and len(local_lines) == 3
        and len(nonlocal_lines) == 4
        and len(stab_line) == 24
        and len(stab_line_induced_s4) == 24
        and stab_line_order_hist == expected_s4_hist
        and order_s5 == 120
        and order_s4 == 24
        and gcd_s5_psl27 == 24
        and (not divides_168_120)
        and (not divides_7_120)
    )

    payload: dict[str, object] = {
        "gl3_f2_order": order_gl3,
        "fano_plane_pg22": {
            "num_points": len(fano_points),
            "num_lines": len(fano_lines),
            "lines_1_indexed_xor_triples": [list(ln) for ln in fano_lines],
            "lines_per_point_all_three": all(v == 3 for v in lines_per_point.values()),
            "unique_line_per_point_pair": unique_line_per_pair,
            "unique_point_per_line_pair": unique_pt_per_line_pair,
            "collineation_group_order": len(collineation_perms),
        },
        "conjugacy_classes": conj_classes,
        "conjugacy_class_sizes": class_sizes,
        "conjugacy_class_orders": class_orders,
        "psl27_irrep_dimensions": irrep_dims,
        "sum_irrep_dimensions_squared": sum_irrep_sq,
        "s4_common_maximal_subgroup_bridge": {
            "bring_aut_s5_order": order_s5,
            "fano_aut_psl27_order": order_gl3,
            "168_divides_120": divides_168_120,
            "7_divides_120": divides_7_120,
            "gcd_120_168": gcd_s5_psl27,
            "index_s4_in_s5_bring_sheets": order_s5 // order_s4,
            "index_s4_in_psl27_fano_points": order_gl3 // len(stab_pt),
            "fixed_point_e7_f2_coords": [1, 1, 1],
            "point_stabilizer_order": len(stab_pt),
            "point_stabilizer_element_order_histogram": {str(k): v for k, v in stab_pt_order_hist.items()},
            "point_stabilizer_faithful_s4_on_4_nonlocal_lines": len(stab_pt_induced_s4) == 24,
            "point_stabilizer_is_maximal_in_gl3f2": stab_pt_is_maximal,
            "local_lines_through_e7": [list(ln) for ln in local_lines],
            "nonlocal_lines_disjoint_from_e7": [list(ln) for ln in nonlocal_lines],
            "line_stabilizer_order": len(stab_line),
            "line_stabilizer_element_order_histogram": {str(k): v for k, v in stab_line_order_hist.items()},
            "line_stabilizer_faithful_s4_on_4_complement_points": len(stab_line_induced_s4) == 24,
        },
    }
    return payload, passed


# ── Part 2: 168 Unitary 3x3 Blichfeldt Matrices Inside SU(3)_c at 80 dps ─────
def _evaluate_part2_blichfeldt_su3_group() -> tuple[dict[str, object], dict[str, mp.mpf]]:
    with mp.workdps(95):
        i_unit = mp.mpc(0, 1)
        two_pi_over_7 = mp.mpf(2) * mp.pi / mp.mpf(7)
        zeta_7 = mp.exp(i_unit * two_pi_over_7)

        alpha = zeta_7 + zeta_7 ** 2 + zeta_7 ** 4
        alpha_bar = zeta_7 ** 6 + zeta_7 ** 5 + zeta_7 ** 3
        i_sqrt7 = i_unit * mp.sqrt(mp.mpf(7))
        gauss_sum_err = abs((alpha - alpha_bar) - i_sqrt7)
        alpha_exact = (mp.mpf(-1) + i_sqrt7) / mp.mpf(2)
        alpha_bar_exact = (mp.mpf(-1) - i_sqrt7) / mp.mpf(2)

        # Generators in SU(3)_c (Weil odd-function basis x = (1, 4, 2) mod 7 so x^2 mod 7 = (1, 2, 4))
        xs = (1, 4, 2)
        t_gen = mp.zeros(3, 3)
        t_gen[0, 0] = zeta_7
        t_gen[1, 1] = zeta_7 ** 2
        t_gen[2, 2] = zeta_7 ** 4

        r_gen = mp.zeros(3, 3)
        r_gen[0, 1] = mp.mpf(1)
        r_gen[1, 2] = mp.mpf(1)
        r_gen[2, 0] = mp.mpf(1)

        s_klein = mp.zeros(3, 3)
        for r in range(3):
            for c in range(3):
                exp_rc = (2 * xs[r] * xs[c]) % 7
                s_klein[r, c] = (zeta_7 ** exp_rc - zeta_7 ** (7 - exp_rc)) / i_sqrt7
        neg_s_gen = -s_klein

        ident3 = mp.eye(3)
        tr_neg_s_err = abs(_mat_trace3(neg_s_gen) - mp.mpc(-1, 0))
        det_neg_s_err = abs(_mat_det3(neg_s_gen) - mp.mpc(1, 0))
        inv_neg_s_err = _frobenius_norm(neg_s_gen * neg_s_gen - ident3)
        rel_t_negs_cubed_err = _frobenius_norm((t_gen * neg_s_gen) ** 3 - ident3)

        # Generate full finite matrix group G_168 < SU(3)_c up to 1e-85 Frobenius tolerance
        tol_dedup = mp.mpf("1e-85")
        group: list[mp.matrix] = [ident3]
        gens = (t_gen, r_gen, neg_s_gen)
        q_idx = 0
        while q_idx < len(group):
            g_cur = group[q_idx]
            q_idx += 1
            for h_gen in gens:
                prod = g_cur * h_gen
                already = False
                for ex in group:
                    if _frobenius_norm(prod - ex) < tol_dedup:
                        already = True
                        break
                if not already:
                    group.append(prod)
                    if len(group) > 200:
                        raise RuntimeError("Blichfeldt matrix generation failed to close at 168!")

        # Verify closure under all left/right multiplications by generators and inverses
        max_closure_err = mp.mpf(0)
        for u_mat in group:
            u_inv = _conj_transpose(u_mat)
            min_inv_d = min(_frobenius_norm(u_inv - v_mat) for v_mat in group)
            if min_inv_d > max_closure_err:
                max_closure_err = min_inv_d
            for h_gen in gens:
                prod = h_gen * u_mat
                min_d = min(_frobenius_norm(prod - v_mat) for v_mat in group)
                if min_d > max_closure_err:
                    max_closure_err = min_d

        max_unitarity_err = mp.mpf(0)
        max_det_err = mp.mpf(0)
        traces: list[mp.mpc] = []
        for u_mat in group:
            u_err = _frobenius_norm(u_mat * _conj_transpose(u_mat) - ident3)
            if u_err > max_unitarity_err:
                max_unitarity_err = u_err
            d_err = abs(_mat_det3(u_mat) - mp.mpc(1, 0))
            if d_err > max_det_err:
                max_det_err = d_err
            traces.append(_mat_trace3(u_mat))

        char_targets = [
            ("3_class_1A", mp.mpc(3, 0)),
            ("-1_class_2A", mp.mpc(-1, 0)),
            ("0_class_3A", mp.mpc(0, 0)),
            ("1_class_4A", mp.mpc(1, 0)),
            ("alpha_(-1+i*sqrt7)/2_class_7A", alpha_exact),
            ("alpha_bar_(-1-i*sqrt7)/2_class_7B", alpha_bar_exact),
        ]
        char_counts = {label: 0 for label, _ in char_targets}
        max_char_snap_err = mp.mpf(0)
        for tr_val in traces:
            best_label = char_targets[0][0]
            best_dist = abs(tr_val - char_targets[0][1])
            for label, target_val in char_targets[1:]:
                dist = abs(tr_val - target_val)
                if dist < best_dist:
                    best_dist = dist
                    best_label = label
            if best_dist > max_char_snap_err:
                max_char_snap_err = best_dist
            char_counts[best_label] += 1

        n_grp = mp.mpf(len(group))
        schur_norm = mp.fsum(mp.re(t) ** 2 + mp.im(t) ** 2 for t in traces) / n_grp
        schur_err = abs(schur_norm - mp.mpf(1))
        trivial_mult = abs(mp.fsum(traces) / n_grp)

        # Sym^2(W_3) (6D) and Alt^2(W_3) ~= W_3^* (3D) character orthogonality checks
        # tr_{Alt^2}(U) = (tr(U)^2 - tr(U^2))/2 = conj(tr(U)) for U in SU(3);
        # tr_{Sym^2}(U) = (tr(U)^2 + tr(U^2))/2 -> Schur norm = 1 (irreducible 6D rep of PSL(2,7)!)
        sym2_traces: list[mp.mpc] = []
        for u_mat, tr_u in zip(group, traces):
            tr_u2 = _mat_trace3(u_mat * u_mat)
            sym2_traces.append((tr_u * tr_u + tr_u2) / mp.mpf(2))
        sym2_schur_norm = mp.fsum(mp.re(t) ** 2 + mp.im(t) ** 2 for t in sym2_traces) / n_grp
        sym2_schur_err = abs(sym2_schur_norm - mp.mpf(1))

        payload = {
            "group_order": len(group),
            "gauss_period_alpha_re_80dps": fmt(mp.re(alpha)),
            "gauss_period_alpha_im_80dps": fmt(mp.im(alpha)),
            "gauss_quadratic_sum_alpha_minus_alphabar_im_80dps": fmt(mp.im(alpha - alpha_bar)),
            "sqrt7_80dps": fmt(mp.sqrt(mp.mpf(7))),
            "gauss_quadratic_sum_abs_err": fmt(gauss_sum_err),
            "generator_relations": {
                "tr_neg_S_minus_neg1_abs_err": fmt(tr_neg_s_err),
                "det_neg_S_minus_1_abs_err": fmt(det_neg_s_err),
                "neg_S_squared_minus_I3_frobenius": fmt(inv_neg_s_err),
                "T_mul_neg_S_cubed_minus_I3_frobenius": fmt(rel_t_negs_cubed_err),
            },
            "su3_embedding_certification": {
                "max_closure_frobenius_err": fmt(max_closure_err),
                "max_unitarity_U_Udag_minus_I3_frobenius": fmt(max_unitarity_err),
                "max_special_unitary_det_U_minus_1_abs": fmt(max_det_err),
                "max_character_value_snap_abs_err": fmt(max_char_snap_err),
                "character_value_multiplicities": char_counts,
                "schur_orthogonality_norm_W3_80dps": fmt(schur_norm),
                "schur_orthogonality_W3_minus_1_abs_err": fmt(schur_err),
                "trivial_invariant_multiplicity_abs": fmt(trivial_mult),
                "schur_orthogonality_Sym2_W3_6D_irrep_minus_1_abs_err": fmt(sym2_schur_err),
            },
        }
        metrics = {
            "gauss_sum_err": gauss_sum_err,
            "max_closure_err": max_closure_err,
            "max_unitarity_err": max_unitarity_err,
            "max_det_err": max_det_err,
            "max_char_snap_err": max_char_snap_err,
            "schur_err": schur_err,
            "trivial_mult": trivial_mult,
            "sym2_schur_err": sym2_schur_err,
            "group_order": mp.mpf(len(group)),
        }
        return payload, metrics


# ── Part 3: Fano Octonion Algebra O and g_2 -> su(3)_c Derivation Stabilizer ─
def _build_cayley_dickson_octonion_table() -> list[list[tuple[int, int]]]:
    """Construct exact multiplication table e_i * e_j = (sign, k) for i, j in 0..7 via R->C->H->O."""
    # Represent basis unit e_i as unit tuple in 2^d-dimensional algebra; double 3 times.
    # Start d=0: R has 1 basis unit.
    table: list[list[tuple[int, int]]] = [[(1, 0)]]
    conj_sign: list[int] = [1]

    for _step in range(3):
        n = len(table)
        new_table: list[list[tuple[int, int]]] = [[(1, 0) for _ in range(2 * n)] for _ in range(2 * n)]
        new_conj = [conj_sign[i] if i < n else -1 for i in range(2 * n)]
        # Cayley-Dickson product: (p, 0)*(r, 0) = (p*r, 0)
        #                         (p, 0)*(0, s) = (0, s*p)
        #                         (0, q)*(r, 0) = (0, q*conj(r))
        #                         (0, q)*(0, s) = (-conj(s)*q, 0)
        for i in range(n):
            for j in range(n):
                sgn_ij, k_ij = table[i][j]
                new_table[i][j] = (sgn_ij, k_ij)

                sgn_ji, k_ji = table[j][i]
                new_table[i][n + j] = (sgn_ji, n + k_ji)

                sgn_ij_c, k_ij_c = table[i][j]
                new_table[n + i][j] = (conj_sign[j] * sgn_ij_c, n + k_ij_c)

                sgn_ji_c, k_ji_c = table[j][i]
                new_table[n + i][n + j] = (-conj_sign[j] * sgn_ji_c, k_ji_c)
        table = new_table
        conj_sign = new_conj
    return table


def _evaluate_part3_octonions_and_g2_su3() -> tuple[dict[str, object], bool, mp.mpf]:
    mult_table = _build_cayley_dickson_octonion_table()

    # Structure constants c[i][j][k] in {-1, 0, +1} such that e_i * e_j = sum_k c[i][j][k] e_k
    c_tensor = [[[0 for _ in range(8)] for _ in range(8)] for _ in range(8)]
    xor_index_holds = True
    for i in range(8):
        for j in range(8):
            sgn, k = mult_table[i][j]
            c_tensor[i][j][k] = sgn
            if k != (i ^ j):
                xor_index_holds = False

    def oct_mul_frac(x: list[Fraction], y: list[Fraction]) -> list[Fraction]:
        out = [Fraction(0)] * 8
        for i in range(8):
            xi = x[i]
            if xi == 0:
                continue
            for j in range(8):
                yj = y[j]
                if yj != 0:
                    sgn, k = mult_table[i][j]
                    out[k] += sgn * xi * yj
        return out

    # 1. Exact bilinear Degen 8-square identity check over all 8^4 = 4096 index quadruples:
    #    <e_i e_j, e_i e_l> = delta_{jl}, and <e_i e_j, e_k e_l> + <e_i e_l, e_k e_j> = 2 delta_{ik} delta_{jl}
    degen_exact_bilinear = True
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l_idx in range(8):
                    lhs = sum(
                        c_tensor[i][j][m] * c_tensor[k][l_idx][m]
                        + c_tensor[i][l_idx][m] * c_tensor[k][j][m]
                        for m in range(8)
                    )
                    rhs = 2 if (i == k and j == l_idx) else 0
                    if lhs != rhs:
                        degen_exact_bilinear = False

    # 2. Associator census on the binom(7, 3) = 35 unordered imaginary triples & all 512 ordered basis triples
    fano_assoc_triples: list[list[int]] = []
    anti_fano_nonassoc_triples: list[list[int]] = []
    for a in range(1, 8):
        for b in range(a + 1, 8):
            for c_idx in range(b + 1, 8):
                ea = [Fraction(1 if t == a else 0) for t in range(8)]
                eb = [Fraction(1 if t == b else 0) for t in range(8)]
                ec = [Fraction(1 if t == c_idx else 0) for t in range(8)]
                lhs = oct_mul_frac(oct_mul_frac(ea, eb), ec)
                rhs = oct_mul_frac(ea, oct_mul_frac(eb, ec))
                diff = [lhs[t] - rhs[t] for t in range(8)]
                norm_sq = sum(d * d for d in diff)
                if norm_sq == 0:
                    fano_assoc_triples.append([a, b, c_idx])
                elif norm_sq == 4:
                    anti_fano_nonassoc_triples.append([a, b, c_idx])

    ordered_nonassoc_512 = 0
    for i in range(8):
        ei = [Fraction(1 if t == i else 0) for t in range(8)]
        for j in range(8):
            ej = [Fraction(1 if t == j else 0) for t in range(8)]
            eij = oct_mul_frac(ei, ej)
            for k in range(8):
                ek = [Fraction(1 if t == k else 0) for t in range(8)]
                lhs = oct_mul_frac(eij, ek)
                rhs = oct_mul_frac(ei, oct_mul_frac(ej, ek))
                if lhs != rhs:
                    ordered_nonassoc_512 += 1

    # 3. 80-dps transcendental test of Degen's 8-square norm, alternativity, and all 3 Moufang identities
    with mp.workdps(95):
        def oct_mul_mp(u: list[mp.mpf], v: list[mp.mpf]) -> list[mp.mpf]:
            res = [mp.mpf(0) for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    sgn, k = mult_table[i][j]
                    res[k] += mp.mpf(sgn) * u[i] * v[j]
            return res

        def oct_norm_sq_mp(u: list[mp.mpf]) -> mp.mpf:
            return mp.fsum(val * val for val in u)

        def oct_max_diff_mp(u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
            return max(abs(u[t] - v[t]) for t in range(8))

        x_vec = [
            mp.pi / mp.mpf(3),
            mp.e / mp.mpf(5),
            -mp.sqrt(mp.mpf(2)),
            mp.sqrt(mp.mpf(3)) / mp.mpf(2),
            -mp.ln(mp.mpf(2)),
            mp.sqrt(mp.mpf(5)) / mp.mpf(4),
            mp.cos(mp.mpf(2) * mp.pi / mp.mpf(7)),
            -mp.sin(mp.mpf(2) * mp.pi / mp.mpf(7)),
        ]
        y_vec = [
            mp.sqrt(mp.mpf(7)) / mp.mpf(3),
            -mp.pi / mp.mpf(7),
            mp.ln(mp.mpf(3)),
            mp.e / mp.mpf(4),
            mp.cos(mp.mpf(4) * mp.pi / mp.mpf(7)),
            -mp.sqrt(mp.mpf(11)) / mp.mpf(5),
            mp.sin(mp.mpf(4) * mp.pi / mp.mpf(7)),
            mp.catalan,
        ]
        z_vec = [
            -mp.ln(mp.mpf(5)),
            mp.sqrt(mp.mpf(13)) / mp.mpf(6),
            mp.cos(mp.mpf(8) * mp.pi / mp.mpf(7)),
            -mp.sin(mp.mpf(8) * mp.pi / mp.mpf(7)),
            mp.pi / mp.mpf(11),
            mp.e / mp.mpf(9),
            -mp.sqrt(mp.mpf(17)) / mp.mpf(7),
            mp.euler,
        ]

        xy_vec = oct_mul_mp(x_vec, y_vec)
        degen_mp_err = abs(oct_norm_sq_mp(xy_vec) - oct_norm_sq_mp(x_vec) * oct_norm_sq_mp(y_vec))
        left_alt_err = oct_max_diff_mp(oct_mul_mp(oct_mul_mp(x_vec, x_vec), y_vec), oct_mul_mp(x_vec, xy_vec))
        right_alt_err = oct_max_diff_mp(
            oct_mul_mp(oct_mul_mp(y_vec, x_vec), x_vec),
            oct_mul_mp(y_vec, oct_mul_mp(x_vec, x_vec)),
        )
        flex_err = oct_max_diff_mp(oct_mul_mp(xy_vec, x_vec), oct_mul_mp(x_vec, oct_mul_mp(y_vec, x_vec)))
        moufang1_err = oct_max_diff_mp(
            oct_mul_mp(x_vec, oct_mul_mp(y_vec, oct_mul_mp(x_vec, z_vec))),
            oct_mul_mp(oct_mul_mp(xy_vec, x_vec), z_vec),
        )
        moufang2_err = oct_max_diff_mp(
            oct_mul_mp(oct_mul_mp(oct_mul_mp(z_vec, x_vec), y_vec), x_vec),
            oct_mul_mp(z_vec, oct_mul_mp(x_vec, oct_mul_mp(y_vec, x_vec))),
        )
        moufang3_err = oct_max_diff_mp(
            oct_mul_mp(xy_vec, oct_mul_mp(z_vec, x_vec)),
            oct_mul_mp(x_vec, oct_mul_mp(oct_mul_mp(y_vec, z_vec), x_vec)),
        )
        max_oct_identity_err = max(
            degen_mp_err,
            left_alt_err,
            right_alt_err,
            flex_err,
            moufang1_err,
            moufang2_err,
            moufang3_err,
        )

    # 4. Exact rational derivation equations D(e_a e_b) = (D e_a) e_b + e_a (D e_b)
    #    Parameterize 7x7 skew-symmetric matrices on Im(O) = span{e_1..e_7}: 21 parameters (p, q) with 1 <= p < q <= 7
    #    Convention: (D e_b)_a = D_{a, b}, with D_{p, q} = +v_{(p, q)} and D_{q, p} = -v_{(p, q)}.
    skew_pairs = [(p, q) for p in range(1, 8) for q in range(p + 1, 8)]
    pair_idx = {pq: idx for idx, pq in enumerate(skew_pairs)}
    n_so7 = len(skew_pairs)  # 21

    der_rows_so7: list[list[Fraction]] = []
    for a in range(1, 8):
        for b in range(1, 8):
            # Equation for each output basis component m in 0..7:
            # sum_k c[a][b][k] (D e_k)_m - sum_p (D e_a)_p c[p][b][m] - sum_q (D e_b)_q c[a][q][m] = 0
            for m in range(8):
                row = [Fraction(0)] * n_so7
                # Term 1: D(e_a * e_b)_m — nonzero only when k >= 1 and m >= 1
                if m >= 1:
                    for k in range(1, 8):
                        cabk = c_tensor[a][b][k]
                        if cabk != 0 and m != k:
                            if m < k:
                                row[pair_idx[(m, k)]] += Fraction(cabk)
                            else:
                                row[pair_idx[(k, m)]] -= Fraction(cabk)
                # Term 2: - ((D e_a) * e_b)_m = - sum_{p=1..7} D_{p, a} c[p][b][m]
                for p in range(1, 8):
                    cpbm = c_tensor[p][b][m]
                    if cpbm != 0 and p != a:
                        if p < a:
                            row[pair_idx[(p, a)]] -= Fraction(cpbm)
                        else:
                            row[pair_idx[(a, p)]] += Fraction(cpbm)
                # Term 3: - (e_a * (D e_b))_m = - sum_{q=1..7} D_{q, b} c[a][q][m]
                for q in range(1, 8):
                    caqm = c_tensor[a][q][m]
                    if caqm != 0 and q != b:
                        if q < b:
                            row[pair_idx[(q, b)]] -= Fraction(caqm)
                        else:
                            row[pair_idx[(b, q)]] += Fraction(caqm)
                if any(val != 0 for val in row):
                    der_rows_so7.append(row)

    rank_so7, g2_basis_vecs = _rref_fraction(der_rows_so7, n_so7)
    dim_g2 = len(g2_basis_vecs)  # 21 - 7 = 14

    # Also verify full gl(8) (64 parameters, no skew-symmetry or D(e_0)=0 assumed a priori)
    gl8_rows: list[list[Fraction]] = []
    for a in range(8):
        for b in range(8):
            for m in range(8):
                row64 = [Fraction(0)] * 64
                for k in range(8):
                    cabk = c_tensor[a][b][k]
                    if cabk != 0:
                        row64[m * 8 + k] += Fraction(cabk)
                for p in range(8):
                    cpbm = c_tensor[p][b][m]
                    if cpbm != 0:
                        row64[p * 8 + a] -= Fraction(cpbm)
                for q in range(8):
                    caqm = c_tensor[a][q][m]
                    if caqm != 0:
                        row64[q * 8 + b] -= Fraction(caqm)
                if any(val != 0 for val in row64):
                    gl8_rows.append(row64)
    rank_gl8, gl8_null = _rref_fraction(gl8_rows, 64)

    # 5. Impose colour-axis stabilizer D(e_7) = 0: D_{p, 7} = 0 for all p in 1..6
    stab_rows_so7 = list(der_rows_so7)
    for p in range(1, 7):
        r_stab = [Fraction(0)] * n_so7
        r_stab[pair_idx[(p, 7)]] = Fraction(1)
        stab_rows_so7.append(r_stab)

    rank_stab_so7, su3_basis_vecs = _rref_fraction(stab_rows_so7, n_so7)
    dim_su3 = len(su3_basis_vecs)  # 21 - 13 = 8

    # Convert skew parameter vector into 7x7 Fraction matrix (0-indexed on e_1..e_7)
    def vec_to_mat7(v: list[Fraction]) -> list[list[Fraction]]:
        mat = [[Fraction(0) for _ in range(7)] for _ in range(7)]
        for (p, q), idx in pair_idx.items():
            mat[p - 1][q - 1] = v[idx]
            mat[q - 1][p - 1] = -v[idx]
        return mat

    def mat7_comm(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
        return [
            [
                sum(a[i][k] * b[k][j] - b[i][k] * a[k][j] for k in range(7))
                for j in range(7)
            ]
            for i in range(7)
        ]

    # Verify complex structure J = L_{e_7}|_{span(e_1..e_6)}: J^2 = -I_6, [B, J] = 0, and 3x3 tracelessness on C^3
    j_mat6 = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for col_b in range(1, 7):
        sgn, k = mult_table[7][col_b]
        j_mat6[k - 1][col_b - 1] = Fraction(sgn)

    j_sq_is_neg_id6 = all(
        sum(j_mat6[r][k] * j_mat6[k][c] for k in range(6)) == (Fraction(-1) if r == c else Fraction(0))
        for r in range(6)
        for c in range(6)
    )

    # Complex basis of C^3 from the 3 local Fano lines through e_7:
    # Choose u_1 = e_1, u_2 = e_2, u_3 = e_4; then J(u_a) = e_7 * u_a gives the imaginary partners!
    u_indices = [1, 2, 4]
    ju_pairs = [mult_table[7][u] for u in u_indices]  # (sgn, idx) so J(e_u) = sgn * e_{idx}

    su3_mats7 = [vec_to_mat7(v) for v in su3_basis_vecs]
    commutes_with_j = True
    all_traceless_skew_hermitian_on_c3 = True
    for m7 in su3_mats7:
        m6 = [row[:6] for row in m7[:6]]
        for r in range(6):
            for c in range(6):
                comm_rc = sum(m6[r][k] * j_mat6[k][c] - j_mat6[r][k] * m6[k][c] for k in range(6))
                if comm_rc != 0:
                    commutes_with_j = False
        # Extract 3x3 complex matrix A = Re(A) + i Im(A) on basis {u_1, u_2, u_3} where i acts as J:
        # M(u_c) = sum_r (Re_A[r, c] * u_r + Im_A[r, c] * J(u_r))
        re_a = [[Fraction(0) for _ in range(3)] for _ in range(3)]
        im_a = [[Fraction(0) for _ in range(3)] for _ in range(3)]
        for c_col, u_c in enumerate(u_indices):
            for r_row, u_r in enumerate(u_indices):
                re_a[r_row][c_col] = m6[u_r - 1][u_c - 1]
                sgn_jr, idx_jr = ju_pairs[r_row]
                im_a[r_row][c_col] = Fraction(sgn_jr) * m6[idx_jr - 1][u_c - 1]
        # Skew-Hermitian: Re(A)^T = -Re(A) and Im(A)^T = +Im(A); Traceless: tr(Re A) = 0 and tr(Im A) = 0
        for r_row in range(3):
            for c_col in range(3):
                if re_a[r_row][c_col] != -re_a[c_col][r_row]:
                    all_traceless_skew_hermitian_on_c3 = False
                if im_a[r_row][c_col] != im_a[c_col][r_row]:
                    all_traceless_skew_hermitian_on_c3 = False
        if sum(re_a[t][t] for t in range(3)) != 0 or sum(im_a[t][t] for t in range(3)) != 0:
            all_traceless_skew_hermitian_on_c3 = False

    # Verify Killing form of su(3)_c (8x8) is negative definite of full rank 8 over Q
    # Express [B_a, B_b] = sum_c f^c_{ab} B_c using the free-column coordinates of RREF!
    def lie_killing_rank_and_negdef(mats: list[list[list[Fraction]]]) -> tuple[int, bool]:
        d_alg = len(mats)
        # Flatten 7x7 -> 49 coordinates to solve for structure constants f[a][b][c]
        flat_basis = [[mats[idx][r][c] for r in range(7) for c in range(7)] for idx in range(d_alg)]
        # Build 49 x d_alg matrix and solve per commutator
        f_struct = [[[Fraction(0) for _ in range(d_alg)] for _ in range(d_alg)] for _ in range(d_alg)]
        for a in range(d_alg):
            for b in range(a + 1, d_alg):
                comm = mat7_comm(mats[a], mats[b])
                flat_comm = [comm[r][c] for r in range(7) for c in range(7)]
                # Solve sum_c coeff_c * flat_basis[c] = flat_comm via RREF on augmented columns
                aug = [[flat_basis[c_i][pos] for c_i in range(d_alg)] + [flat_comm[pos]] for pos in range(49)]
                rk_aug, null_aug = _rref_fraction(aug, d_alg + 1)
                if rk_aug != d_alg or len(null_aug) != 1 or null_aug[0][d_alg] == 0:
                    return 0, False
                scale = null_aug[0][d_alg]
                for c_i in range(d_alg):
                    val = -null_aug[0][c_i] / scale
                    f_struct[a][b][c_i] = val
                    f_struct[b][a][c_i] = -val

        killing = [[Fraction(0) for _ in range(d_alg)] for _ in range(d_alg)]
        for a in range(d_alg):
            for b in range(d_alg):
                killing[a][b] = sum(
                    f_struct[a][m][n] * f_struct[b][n][m]
                    for m in range(d_alg)
                    for n in range(d_alg)
                )
        rk_k, _ = _rref_fraction(killing, d_alg)
        # Sylvester criterion on -Killing (symmetric positive definite <=> all leading principal minors > 0,
        # checked via exact rational Cholesky / Gaussian pivot signs without row swaps)
        neg_k = [[-killing[i][j] for j in range(d_alg)] for i in range(d_alg)]
        pos_def = True
        for p in range(d_alg):
            piv_val = neg_k[p][p]
            if piv_val <= 0:
                pos_def = False
                break
            for i in range(p + 1, d_alg):
                fac = neg_k[i][p] / piv_val
                for j in range(p, d_alg):
                    neg_k[i][j] -= fac * neg_k[p][j]
        return rk_k, pos_def

    su3_killing_rank, su3_killing_negdef = lie_killing_rank_and_negdef(su3_mats7)
    g2_mats7 = [vec_to_mat7(v) for v in g2_basis_vecs]
    g2_killing_rank, g2_killing_negdef = lie_killing_rank_and_negdef(g2_mats7)

    passed = (
        xor_index_holds
        and degen_exact_bilinear
        and len(fano_assoc_triples) == 7
        and len(anti_fano_nonassoc_triples) == 28
        and len(fano_assoc_triples) + len(anti_fano_nonassoc_triples) == _binom_int(7, 3)
        and ordered_nonassoc_512 == 168
        and dim_so7_check(n_so7)
        and rank_so7 == 7
        and dim_g2 == 14
        and rank_gl8 == 50
        and len(gl8_null) == 14
        and rank_stab_so7 == 13
        and dim_su3 == 8
        and (dim_g2 - dim_su3) == 6
        and j_sq_is_neg_id6
        and commutes_with_j
        and all_traceless_skew_hermitian_on_c3
        and su3_killing_rank == 8
        and su3_killing_negdef
        and g2_killing_rank == 14
        and g2_killing_negdef
    )

    payload: dict[str, object] = {
        "cayley_dickson_xor_grading_verified": xor_index_holds,
        "degen_8_square_bilinear_identity_all_4096_quadruples": degen_exact_bilinear,
        "associator_census": {
            "total_imaginary_3_subsets": _binom_int(7, 3),
            "associating_fano_lines_count": len(fano_assoc_triples),
            "non_associating_anti_fano_3_subsets_count": len(anti_fano_nonassoc_triples),
            "associating_fano_lines": fano_assoc_triples,
            "ordered_non_associating_triples_out_of_512": ordered_nonassoc_512,
        },
        "transcendental_80dps_identities": {
            "degen_8_square_norm_abs_err": fmt(degen_mp_err),
            "left_alternativity_max_abs_err": fmt(left_alt_err),
            "right_alternativity_max_abs_err": fmt(right_alt_err),
            "flexibility_max_abs_err": fmt(flex_err),
            "left_moufang_max_abs_err": fmt(moufang1_err),
            "right_moufang_max_abs_err": fmt(moufang2_err),
            "middle_moufang_max_abs_err": fmt(moufang3_err),
            "max_identity_abs_err": fmt(max_oct_identity_err),
        },
        "g2_and_su3_derivation_linear_algebra": {
            "ambient_gl8_dim": 64,
            "gl8_derivation_system_rank": rank_gl8,
            "gl8_derivation_nullity_dim_g2": len(gl8_null),
            "ambient_so7_skew_dim": n_so7,
            "so7_derivation_constraint_rank": rank_so7,
            "so7_derivation_nullity_dim_g2": dim_g2,
            "g2_killing_form_rank": g2_killing_rank,
            "g2_killing_form_strictly_negative_definite": g2_killing_negdef,
            "stabilizer_De7_eq_0_so7_rank": rank_stab_so7,
            "stabilizer_De7_eq_0_nullity_dim_su3": dim_su3,
            "coset_dimension_dim_g2_minus_dim_su3_eq_dim_S6": dim_g2 - dim_su3,
            "complex_structure_J_eq_Le7_squares_to_neg_I6": j_sq_is_neg_id6,
            "stabilizer_commutes_with_J": commutes_with_j,
            "stabilizer_maps_to_traceless_skew_hermitian_3x3_on_C3": all_traceless_skew_hermitian_on_c3,
            "su3_killing_form_rank": su3_killing_rank,
            "su3_killing_form_strictly_negative_definite": su3_killing_negdef,
        },
    }
    return payload, passed, max_oct_identity_err


def dim_so7_check(n: int) -> bool:
    return n == 21


def main() -> int:
    with mp.workdps(95):
        wb = WitnessBuilder(
            name="bring-fano-octonion-blichfeldt-su3",
            engine="mpmath",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps Bring Genus-3 Fano Plane, S_4 Maximal-Subgroup Bridge, Octonion Algebra O, "
            "and 168-Element Blichfeldt Subgroup of SU(3)_c Probe (Wave 6B, bean qou-ys29)"
        )

        part1, p1_ok = _evaluate_part1_gl3f2_and_s4_bridge()
        part2, p2_metrics = _evaluate_part2_blichfeldt_su3_group()
        part3, p3_ok, p3_max_err = _evaluate_part3_octonions_and_g2_su3()

        wb.add_data("part1_gl3_f2_fano_and_s4_bridge", part1)
        wb.add_data("part2_blichfeldt_168_subgroup_in_su3", part2)
        wb.add_data("part3_fano_octonion_and_g2_to_su3_derivations", part3)

        wb.add_assertion(
            name="part1_gl3_f2_order_168_fano_and_conjugacy_partition_exact",
            computed="1" if p1_ok else "0",
            expected="1",
            tolerance="0",
            source=(
                "|GL(3, F_2)| = 168, Fano PG(2,2) axioms (7 pts, 7 lines), conjugacy classes "
                "1 + 21 + 56 + 42 + 24 + 24 = 168 (orders 1, 2, 3, 4, 7, 7), and 168 !| 120"
            ),
        )
        s4_bridge = part1["s4_common_maximal_subgroup_bridge"]
        s4_ok = (
            bool(s4_bridge["point_stabilizer_is_maximal_in_gl3f2"])
            and bool(s4_bridge["point_stabilizer_faithful_s4_on_4_nonlocal_lines"])
            and bool(s4_bridge["line_stabilizer_faithful_s4_on_4_complement_points"])
        )
        wb.add_assertion(
            name="part1_s4_common_maximal_subgroup_bridge_exact",
            computed="1" if s4_ok else "0",
            expected="1",
            tolerance="0",
            source="Stab(e_7) ~= Stab(line) ~= S_4 (order 24, index 7 in GL(3, F_2), maximal) and S_4 < S_5 (index 5)",
        )
        wb.add_assertion(
            name="part2_blichfeldt_group_order_exactly_168",
            computed=str(int(part2["group_order"])),
            expected="168",
            tolerance="0",
            source="Generated finite matrix group <T, R, -S> inside SU(3)_c has exact order 168",
        )
        wb.add_assertion(
            name="part2_blichfeldt_su3_unitarity_and_special_determinant_88dps",
            computed=fmt(
                max(
                    p2_metrics["gauss_sum_err"],
                    p2_metrics["max_closure_err"],
                    p2_metrics["max_unitarity_err"],
                    p2_metrics["max_det_err"],
                    p2_metrics["max_char_snap_err"],
                )
            ),
            expected="0",
            tolerance="1e-88",
            source="max_{U in G_168} (||U U^dag - I_3||_F, |det U - 1|, character snap, closure) < 1e-88",
        )
        wb.add_assertion(
            name="part2_blichfeldt_w3_schur_irreducibility_and_zero_invariants_88dps",
            computed=fmt(max(p2_metrics["schur_err"], p2_metrics["trivial_mult"], p2_metrics["sym2_schur_err"])),
            expected="0",
            tolerance="1e-88",
            source="|(1/168) sum |tr(U)|^2 - 1| < 1e-88, |(1/168) sum tr(U)| < 1e-88, and Sym^2(W_3) 6D Schur norm = 1",
        )
        wb.add_assertion(
            name="part3_octonion_fano_associator_and_g2_14_to_su3_8_verified",
            computed=fmt(p3_max_err) if p3_ok else "1",
            expected="0",
            tolerance="1e-88",
            source=(
                "Degen 8-square, alternativity, and Moufang identities (< 1e-88); 28 anti-Fano 3-subsets "
                "(168/512 ordered triples); exact rational dim Der(O) = 21 - 7 = 14 (g_2) and Stab(e_7) = 8 (su(3)_c)"
            ),
        )

        wb.add_caveat(
            "Candid scope of bean qou-ys29 (zero fitting): (1) Because |PSL(2, 7)| = 168 does not divide "
            "|Aut(Sigma_Bring)| = |S_5| = 120 (7 !| 120, gcd(120, 168) = 24), PSL(2, 7) is NOT a subgroup of "
            "Bring's automorphism group S_5. What is proved algebraically and representation-theoretically here "
            "is the exact S_4 maximal-subgroup bridge (Stab_{S_5}(pt) ~= S_4 of index 5 and Stab_{GL(3,F_2)}(pt) "
            "~= Stab_{GL(3,F_2)}(line) ~= S_4 of index 7), the faithful irreducible embedding of all 168 elements "
            "of PSL(2, 7) as Blichfeldt's finite subgroup G_168 inside SU(3)_c, and the exact Lie-derivation "
            "cutdown dim Der(O) = 14 (g_2) -> dim Stab_{Der(O)}(e_7) = 8 (su(3)_c). (2) What remains open in "
            "moduli / surface geometry is proving that pinching an S_4-invariant cycle on Bring's genus-4 curve "
            "and normalizing produces a genus-3 curve whose automorphism group enhances from S_4 to the Hurwitz "
            "maximum PSL(2, 7) (the Klein quartic), and constructing the smooth manifold coset G_2 / SU(3)_c ~= S^6 "
            "beyond Lie-algebra tangent spaces."
        )

        saved_path = wb.save(
            {
                "q0Anchor": "independent",
                "q0AnchorReason": (
                    "Pure group-theoretic, cyclotomic Q(zeta_7) unitary representation, and exact rational "
                    "octonion Lie-derivation verification (GL(3, F_2), Blichfeldt G_168 < SU(3)_c, Der(O) = g_2 "
                    "-> su(3)_c); no calibration parameter q_0 or CODATA input enters."
                ),
            }
        )
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))

        import witness_raw_float64_audit as _f64_audit

        n_raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if n_raw_floats != 0:
            raise RuntimeError(f"Emitted witness contains {n_raw_floats} raw float64 values!")

        print("=" * 116)
        print(
            "  Wave 6B (qou-ys29): 80-dps Bring Genus-3 Fano Plane, S_4 Bridge, Octonions & Blichfeldt G_168 < SU(3)_c"
        )
        print("=" * 116)
        print(
            f"  Part 1: |GL(3, F_2)| = {part1['gl3_f2_order']} | classes = {part1['conjugacy_class_sizes']} "
            f"(orders {part1['conjugacy_class_orders']}) | gcd(120,168) = 24 = |S_4| | 168|120 = False"
        )
        s_cert = part2["su3_embedding_certification"]
        print(
            f"  Part 2: |G_168| = {part2['group_order']} | "
            f"max ||U U^dag - I||_F = {mp.nstr(mp.mpf(s_cert['max_unitarity_U_Udag_minus_I3_frobenius']), 4)} | "
            f"max |det U - 1| = {mp.nstr(mp.mpf(s_cert['max_special_unitary_det_U_minus_1_abs']), 4)} | "
            f"Schur err = {mp.nstr(mp.mpf(s_cert['schur_orthogonality_W3_minus_1_abs_err']), 4)}"
        )
        g2_d = part3["g2_and_su3_derivation_linear_algebra"]
        a_cen = part3["associator_census"]
        print(
            f"  Part 3: Fano/anti-Fano = {a_cen['associating_fano_lines_count']}/"
            f"{a_cen['non_associating_anti_fano_3_subsets_count']} ({a_cen['ordered_non_associating_triples_out_of_512']}/512 ordered) | "
            f"dim Der(O) = 21 - {g2_d['so7_derivation_constraint_rank']} = {g2_d['so7_derivation_nullity_dim_g2']} (g_2) -> "
            f"Stab(e_7) = {g2_d['stabilizer_De7_eq_0_nullity_dim_su3']} (su(3)_c)"
        )
        print("=" * 116)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
