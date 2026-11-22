#!/usr/bin/env python3
"""borromean_three_cusp_nz_hessian_probe.py — Full 3-cusp Neumann–Zagier Jacobian,
quadratic complex-volume Hessian, and 3rd-order inter-cusp coupling of the Borromean
rings complement B_3 (SnapPy census manifold L6a4).

Task: qou-ay84 (absorbing qou-mcus under epic qou-avtq, Q-AVTQ-2 = 1).
Lean companion: `QOU/QBeta/BorromeanThreeCuspNZHessian.lean`.

Mathematical summary:
  1. Complete structure (u = (0, 0, 0)):
     SnapPy's 8-tetrahedron ideal triangulation of L6a4 decomposes into two regular
     ideal octahedra with complete shape parameters
       z^(0) = ((1+i)/2, 1+i, 1+i, 1+i, 1+i, (1+i)/2, (1+i)/2, (1+i)/2) in Q(i),
       w_k^(0) = z_k^(0) / (1 - z_k^(0)) in {i, -1 + i}.
     Selecting the 5 independent edge rows (0, 1, 2, 3, 4) and the 3 meridian rows
     gives an 8x8 linear system M_sys over Q(i) with exact determinant
       det(M_sys) = -64 i   (|det(M_sys)| = 64 != 0).

  2. Dense 1st-order shape Jacobian dZ_k / du_j |_{u=0} (8x3 over Q(i)):
     Every entry of 4 * (dZ_k / du_j)|_{u=0} lies in {+1+i, +1-i, -1+i, -1-i}.
     In particular, every ideal tetrahedron responds non-trivially to all 3 cusps.

  3. Strictly diagonal 1st-order longitude Jacobian J^(1)_{ij} = dv_i / du_j |_{u=0}
     and quadratic complex-volume Hessian H_{ij}:
       J^(1) = C_lon * (dZ / du)|_{u=0} = -2 i * I_3
     (or tau_{ij} = -dv_i / du_j |_{u=0} = +2 i * delta_{ij} in the standard Cusp
     modulus convention tau_i = +2 i).
     All 6 off-diagonal entries vanish identically (J^(1)_{ij} = 0 for i != j)
     because the Borromean rings have pairwise linking numbers lk(K_i, K_j) = 0
     and (Z/2Z)^3 component-reversal symmetries u_k -> -u_k, forcing v_i(u_1, u_2, u_3)
     to be odd in u_i and even in u_j (j != i).
     Consequently, at quadratic order in u, the 3-cusp Hessian is strictly diagonal:
       kappa_Bor^sym = sum_{i,j=1}^3 kappa_{ij} = 3 * kappa_per_cusp + 0 = 3 * kappa_per_cusp.
     Inter-cusp quadratic cross-terms vanish identically and CANNOT flip the sign of
     kappa_Bor^sym (`sign_flip_resolved = False`, anti-fit guard per qou-mcus).

  4. Exact vanishing of 2nd-order longitude derivatives:
     While the internal 2nd-order shape derivatives d^2 Z_k / (du_p du_q)|_{u=0} are
     non-zero in {+-1/8, +-i/8}, all 27 second-order longitude derivatives vanish:
       d^2 v_i / (du_p du_q) |_{u=0} = 0  for all i, p, q in {1, 2, 3}.

  5. Non-zero inter-cusp coupling at 3rd order in v_i (quartic order O(u^4) in CVol):
     Solving the 3rd-order variational gluing system over Q(i) yields:
       d^3 v_i / du_i^3 |_{u=0} = +i / 2,
       d^3 v_i / (du_i du_j^2) |_{u=0} = -i / 2   (for j != i),
       d^3 v_1 / (du_1 du_2 du_3) |_{u=0} = 0.
     Hence the 3-cusp longitude Taylor expansion through O(u^4) is:
       v_i(u_1, u_2, u_3) = -2 i u_i + (i / 12) u_i^3 - (i / 4) u_i sum_{j != i} u_j^2 + O(u^5).
     On a single-cusp deformation (u, 0, 0), the cubic coefficient of v_1 is +i/12.
     On the symmetric 3-cusp deformation (u, u, u), the two off-diagonal inter-cusp
     channels (2 * (-i/4) = -i/2) flip the sign and quintuple the magnitude of the
     cubic longitude coefficient:
       a_{3,sym} = i/12 + 2 * (-i/4) = -5 i / 12,
     verified to < 10^{-31} against 60-dps mpmath Newton solves of the nonlinear gluing
     equations.
"""
from __future__ import annotations

import datetime as _dt
from fractions import Fraction
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from _witness_q0_stamp import stamp_q0  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 discipline: set compute dps at module import time before any mpf.
set_compute_dps()
mp.mp.dps = 60

from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0_STR = _Q0_RESOLVED
Q0 = mp.mpf(Q0_STR)


class GFrac:
    """Exact Gaussian rational a + b*i with a, b in Q (fractions.Fraction)."""

    __slots__ = ("re", "im")

    def __init__(self, re: int | Fraction = 0, im: int | Fraction = 0) -> None:
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, other: GFrac | int | Fraction) -> GFrac:
        other = other if isinstance(other, GFrac) else GFrac(other, 0)
        return GFrac(self.re + other.re, self.im + other.im)

    def __radd__(self, other: GFrac | int | Fraction) -> GFrac:
        return self.__add__(other)

    def __sub__(self, other: GFrac | int | Fraction) -> GFrac:
        other = other if isinstance(other, GFrac) else GFrac(other, 0)
        return GFrac(self.re - other.re, self.im - other.im)

    def __rsub__(self, other: GFrac | int | Fraction) -> GFrac:
        other = other if isinstance(other, GFrac) else GFrac(other, 0)
        return other.__sub__(self)

    def __neg__(self) -> GFrac:
        return GFrac(-self.re, -self.im)

    def __mul__(self, other: GFrac | int | Fraction) -> GFrac:
        other = other if isinstance(other, GFrac) else GFrac(other, 0)
        return GFrac(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __rmul__(self, other: GFrac | int | Fraction) -> GFrac:
        return self.__mul__(other)

    def __truediv__(self, other: GFrac | int | Fraction) -> GFrac:
        other = other if isinstance(other, GFrac) else GFrac(other, 0)
        denom = other.re * other.re + other.im * other.im
        if denom == 0:
            raise ZeroDivisionError("Division by zero GFrac")
        return GFrac(
            (self.re * other.re + self.im * other.im) / denom,
            (self.im * other.re - self.re * other.im) / denom,
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (int, Fraction)):
            return self.re == Fraction(other) and self.im == 0
        if isinstance(other, GFrac):
            return self.re == other.re and self.im == other.im
        return False

    def __hash__(self) -> int:
        return hash((self.re, self.im))

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def to_mpc(self) -> mp.mpc:
        return mp.mpc(
            mp.mpf(self.re.numerator) / mp.mpf(self.re.denominator),
            mp.mpf(self.im.numerator) / mp.mpf(self.im.denominator),
        )

    def to_dict(self) -> dict[str, str]:
        return {"re": str(self.re), "im": str(self.im), "expr": str(self)}

    def __repr__(self) -> str:
        if self.im == 0:
            return f"{self.re}"
        if self.re == 0:
            return f"{self.im}*i"
        sign = "+" if self.im > 0 else "-"
        return f"{self.re}{sign}{abs(self.im)}*i"


# ---------------------------------------------------------------------------
# SnapPy L6a4 (Borromean rings B_3) 8-tetrahedron rectangular gluing rows
# Equation: prod_k z_k^{a_k} (1 - z_k)^{b_k} = (-1)^sign, so in logarithmic
# coordinates sum_k a_k log(z_k) + sum_k (-b_k) log(1/(1 - z_k)) = i*pi*sign.
# Each 16-column row below is [a_0..a_7, -b_0..-b_7] from SnapPy 3.3.2
# (matching computations/probes/borromean_nz_adjoint_torsion.py BOR["rows"]).
# ---------------------------------------------------------------------------
EDGE_GLUE_16: list[list[int]] = [
    [1, 0, 1, -1, 0, 1, 0, 0, 1, -1, 0, -1, 0, 0, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, -1, -1, 1, 0, 0, 1, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 1, 1, 0, 0, 0],
    [0, -1, 0, 0, -1, 1, 0, 0, 1, -1, -1, 0, -1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, -1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, -1, -1, -1, 0, 1, 0, 0, 0, -1, -1, -1],
    [0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 1, 1, 0, -1, -1, 0],
    [0, 0, -1, 1, 0, 0, 1, 1, 0, 0, -1, 0, -1, 1, 0, 1],
]

MERIDIAN_GLUE_16: list[list[int]] = [
    [0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, 0, -1, -1, 1, 1, -1, 0, 1, -1, 0, -1, 1],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0],
]

LONGITUDE_GLUE_16: list[list[int]] = [
    [1, 0, -1, 1, 0, 0, 1, 0, 1, -1, -1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, -1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, -1, 0, 0, 1, 1, 1, 0, 0],
]

INDEP_EDGE_INDICES = (0, 1, 2, 3, 4)

# Complete regular-octahedral shape parameters z_k^(0) in Q(i)
Z0_GFRAC: list[GFrac] = [
    GFrac(Fraction(1, 2), Fraction(1, 2)),  # tet 0: (1+i)/2
    GFrac(1, 1),                            # tet 1: 1+i
    GFrac(1, 1),                            # tet 2: 1+i
    GFrac(1, 1),                            # tet 3: 1+i
    GFrac(1, 1),                            # tet 4: 1+i
    GFrac(Fraction(1, 2), Fraction(1, 2)),  # tet 5: (1+i)/2
    GFrac(Fraction(1, 2), Fraction(1, 2)),  # tet 6: (1+i)/2
    GFrac(Fraction(1, 2), Fraction(1, 2)),  # tet 7: (1+i)/2
]

# w_k^(0) = z_k^(0) / (1 - z_k^(0)) in {i, -1 + i}
W0_GFRAC: list[GFrac] = [z / (GFrac(1, 0) - z) for z in Z0_GFRAC]


def build_combined_operator(rows_16: list[list[int]], w_vec: list[GFrac]) -> list[list[GFrac]]:
    """Convert a 16-column log(z), log(1/(1-z)) operator into an 8-column operator
    acting on dZ_k where d(log(1/(1-z_k))) = w_k * dZ_k."""
    out: list[list[GFrac]] = []
    for row in rows_16:
        out.append([
            GFrac(row[k], 0) + GFrac(row[k + 8], 0) * w_vec[k]
            for k in range(8)
        ])
    return out


def gauss_jordan_det_and_solve(
    mat: list[list[GFrac]], rhs: list[list[GFrac]]
) -> tuple[GFrac, list[list[GFrac]]]:
    """Exact Gauss–Jordan elimination over Q(i) returning (det(mat), mat^{-1} * rhs)."""
    n = len(mat)
    m = len(rhs[0])
    A = [row[:] for row in mat]
    B = [row[:] for row in rhs]
    det = GFrac(1, 0)

    for col in range(n):
        piv = col
        while piv < n and A[piv][col].is_zero():
            piv += 1
        if piv == n:
            return GFrac(0, 0), B
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            B[col], B[piv] = B[piv], B[col]
            det = -det
        pivot_val = A[col][col]
        det = det * pivot_val
        for j in range(col, n):
            A[col][j] = A[col][j] / pivot_val
        for j in range(m):
            B[col][j] = B[col][j] / pivot_val
        for row in range(n):
            if row != col and not A[row][col].is_zero():
                factor = A[row][col]
                for j in range(col, n):
                    A[row][j] = A[row][j] - factor * A[col][j]
                for j in range(m):
                    B[row][j] = B[row][j] - factor * B[col][j]
    return det, B


def mat_mul_gfrac(A: list[list[GFrac]], B: list[list[GFrac]]) -> list[list[GFrac]]:
    """Exact matrix multiplication over Q(i)."""
    r = len(A)
    k_len = len(A[0])
    c = len(B[0])
    return [
        [sum((A[i][k] * B[k][j] for k in range(k_len)), GFrac(0, 0)) for j in range(c)]
        for i in range(r)
    ]


def solve_nonlinear_gluing_mpmath(u1: mp.mpc, u2: mp.mpc, u3: mp.mpc) -> tuple[list[mp.mpc], list[mp.mpc]]:
    """60-dps damped Newton solver for the exact nonlinear gluing equations of L6a4
    in logarithmic shape offsets dZ_k = log(z_k / z_k^(0)).
    Returns (dZ_list, v_longitude_list)."""
    z0_mp = [z.to_mpc() for z in Z0_GFRAC]
    dZ = [mp.mpc(0, 0) for _ in range(8)]
    u_Re = [r[8:] for r in EDGE_GLUE_16]
    u_Rm = [r[8:] for r in MERIDIAN_GLUE_16]
    u_Rl = [r[8:] for r in LONGITUDE_GLUE_16]

    for _ in range(40):
        z = [z0_mp[k] * mp.exp(dZ[k]) for k in range(8)]
        dW = [
            -mp.log(1 - z[k]) - (-mp.log(1 - z0_mp[k]))
            for k in range(8)
        ]
        w = [z[k] / (1 - z[k]) for k in range(8)]

        F: list[mp.mpc] = []
        J: list[list[mp.mpc]] = []
        for idx in INDEP_EDGE_INDICES:
            F.append(sum(EDGE_GLUE_16[idx][k] * dZ[k] + u_Re[idx][k] * dW[k] for k in range(8)))
            J.append([EDGE_GLUE_16[idx][k] + u_Re[idx][k] * w[k] for k in range(8)])
        targets = (u1, u2, u3)
        for idx in range(3):
            F.append(
                sum(MERIDIAN_GLUE_16[idx][k] * dZ[k] + u_Rm[idx][k] * dW[k] for k in range(8))
                - targets[idx]
            )
            J.append([MERIDIAN_GLUE_16[idx][k] + u_Rm[idx][k] * w[k] for k in range(8)])

        if max(abs(f_val) for f_val in F) < mp.mpf("1e-52"):
            break

        J_mp = mp.matrix(J)
        F_mp = mp.matrix(8, 1)
        for k in range(8):
            F_mp[k, 0] = -F[k]
        delta = mp.lu_solve(J_mp, F_mp)
        for k in range(8):
            dZ[k] += delta[k, 0]

    z = [z0_mp[k] * mp.exp(dZ[k]) for k in range(8)]
    dW = [-mp.log(1 - z[k]) - (-mp.log(1 - z0_mp[k])) for k in range(8)]
    v_lon = [
        sum(LONGITUDE_GLUE_16[idx][k] * dZ[k] + u_Rl[idx][k] * dW[k] for k in range(8))
        for idx in range(3)
    ]
    return dZ, v_lon


def main() -> None:
    # 1. Verify w_k^(0) and linear operator M_sys over Q(i)
    assert W0_GFRAC == [
        GFrac(0, 1), GFrac(-1, 1), GFrac(-1, 1), GFrac(-1, 1),
        GFrac(-1, 1), GFrac(0, 1), GFrac(0, 1), GFrac(0, 1),
    ], f"Unexpected W0_GFRAC: {W0_GFRAC}"

    indep_edge_rows_16 = [EDGE_GLUE_16[idx] for idx in INDEP_EDGE_INDICES]
    M_sys_rows_16 = indep_edge_rows_16 + MERIDIAN_GLUE_16
    M_sys = build_combined_operator(M_sys_rows_16, W0_GFRAC)
    C_lon = build_combined_operator(LONGITUDE_GLUE_16, W0_GFRAC)

    # RHS for 1st-order meridian deformations du_1, du_2, du_3
    rhs_1 = [[GFrac(0, 0) for _ in range(3)] for _ in range(8)]
    for j in range(3):
        rhs_1[5 + j][j] = GFrac(1, 0)

    det_M_sys, Z1 = gauss_jordan_det_and_solve(M_sys, rhs_1)
    assert det_M_sys == GFrac(0, -64), f"Expected det(M_sys) = -64i, got {det_M_sys}"

    # Verify that 4 * Z1 has all entries in {+1+i, +1-i, -1+i, -1-i}
    allowed_scaled_z1 = {
        GFrac(1, 1), GFrac(1, -1), GFrac(-1, 1), GFrac(-1, -1)
    }
    scaled_Z1 = [[ GFrac(4, 0) * Z1[k][j] for j in range(3)] for k in range(8)]
    for k in range(8):
        for j in range(3):
            assert scaled_Z1[k][j] in allowed_scaled_z1, (
                f"4*Z1[{k}][{j}] = {scaled_Z1[k][j]} not in +-1+-i"
            )

    # 2. Compute 1st-order longitude Jacobian J^(1)_{ij} = dv_i / du_j |_{u=0}
    J1 = mat_mul_gfrac(C_lon, Z1)
    for i in range(3):
        for j in range(3):
            expected = GFrac(0, -2) if i == j else GFrac(0, 0)
            assert J1[i][j] == expected, f"J1[{i}][{j}] = {J1[i][j]} != {expected}"

    # Cusp modulus matrix tau_{ij} = -dv_i / du_j |_{u=0} = +2i * delta_{ij}
    tau_matrix = [[-J1[i][j] for j in range(3)] for i in range(3)]

    # 3. Compute 2nd-order shape derivatives Z2_{(p,q)} and longitude derivatives v2_{(p,q)}
    # Using d^2(log(1/(1-z_k))) / dZ_k^2 = w_k * (1 + w_k) = w_k + w_k^2
    w_1pw = [w * (GFrac(1, 0) + w) for w in W0_GFRAC]
    u_sys = [row[8:] for row in M_sys_rows_16]
    u_lon = [row[8:] for row in LONGITUDE_GLUE_16]

    pairs = [(p, q) for p in range(3) for q in range(3)]
    rhs_2 = [[GFrac(0, 0) for _ in range(9)] for _ in range(8)]
    for col_idx, (p, q) in enumerate(pairs):
        for r in range(8):
            rhs_2[r][col_idx] = -sum(
                (GFrac(u_sys[r][k], 0) * w_1pw[k] * Z1[k][p] * Z1[k][q] for k in range(8)),
                GFrac(0, 0),
            )
    _, Z2 = gauss_jordan_det_and_solve(M_sys, rhs_2)

    v2 = [[GFrac(0, 0) for _ in range(9)] for _ in range(3)]
    for col_idx, (p, q) in enumerate(pairs):
        for i in range(3):
            lin_part = sum((C_lon[i][k] * Z2[k][col_idx] for k in range(8)), GFrac(0, 0))
            nl_part = sum(
                (GFrac(u_lon[i][k], 0) * w_1pw[k] * Z1[k][p] * Z1[k][q] for k in range(8)),
                GFrac(0, 0),
            )
            v2[i][col_idx] = lin_part + nl_part
            assert v2[i][col_idx] == GFrac(0, 0), (
                f"Expected d^2 v_{i} / (du_{p} du_{q}) = 0, got {v2[i][col_idx]}"
            )

    # 4. Compute 3rd-order shape and longitude derivatives d^3 v_i / (du_p du_q du_r) |_{u=0}
    # Using d^3(log(1/(1-z_k))) / dZ_k^3 = w_k * (1 + w_k) * (1 + 2*w_k)
    w_1pw_1p2w = [w * (GFrac(1, 0) + w) * (GFrac(1, 0) + GFrac(2, 0) * w) for w in W0_GFRAC]
    triples = [(p, q, s) for p in range(3) for q in range(3) for s in range(3)]
    pair_to_idx = {pair: idx for idx, pair in enumerate(pairs)}

    rhs_3 = [[GFrac(0, 0) for _ in range(len(triples))] for _ in range(8)]
    for col_idx, (p, q, s) in enumerate(triples):
        idx_pq = pair_to_idx[(p, q)]
        idx_ps = pair_to_idx[(p, s)]
        idx_qs = pair_to_idx[(q, s)]
        for r in range(8):
            acc = GFrac(0, 0)
            for k in range(8):
                sym_z2_z1 = (
                    Z2[k][idx_pq] * Z1[k][s]
                    + Z2[k][idx_ps] * Z1[k][q]
                    + Z2[k][idx_qs] * Z1[k][p]
                )
                term = (
                    w_1pw[k] * sym_z2_z1
                    + w_1pw_1p2w[k] * Z1[k][p] * Z1[k][q] * Z1[k][s]
                )
                acc = acc + GFrac(u_sys[r][k], 0) * term
            rhs_3[r][col_idx] = -acc

    _, Z3 = gauss_jordan_det_and_solve(M_sys, rhs_3)

    v3_tensor: dict[tuple[int, int, int, int], GFrac] = {}
    for col_idx, (p, q, s) in enumerate(triples):
        idx_pq = pair_to_idx[(p, q)]
        idx_ps = pair_to_idx[(p, s)]
        idx_qs = pair_to_idx[(q, s)]
        for i in range(3):
            lin_part = sum((C_lon[i][k] * Z3[k][col_idx] for k in range(8)), GFrac(0, 0))
            nl_part = GFrac(0, 0)
            for k in range(8):
                sym_z2_z1 = (
                    Z2[k][idx_pq] * Z1[k][s]
                    + Z2[k][idx_ps] * Z1[k][q]
                    + Z2[k][idx_qs] * Z1[k][p]
                )
                term = (
                    w_1pw[k] * sym_z2_z1
                    + w_1pw_1p2w[k] * Z1[k][p] * Z1[k][q] * Z1[k][s]
                )
                nl_part = nl_part + GFrac(u_lon[i][k], 0) * term
            val = lin_part + nl_part
            v3_tensor[(i, p, q, s)] = val

    # Verify exact 3rd-order tensor law:
    # d^3 v_i / (du_p du_q du_s) is non-zero iff (p, q, s) is a permutation of (i, j, j):
    #   +i/2 when p = q = s = i,
    #   -i/2 when one index is i and the other two equal j != i,
    #   0 otherwise.
    for (i, p, q, s), val in v3_tensor.items():
        indices = sorted((p, q, s))
        if p == i and q == i and s == i:
            expected_v3 = GFrac(0, Fraction(1, 2))
        elif indices.count(i) == 1 and len(set(indices)) == 2:
            expected_v3 = GFrac(0, Fraction(-1, 2))
        else:
            expected_v3 = GFrac(0, 0)
        assert val == expected_v3, (
            f"v3_tensor[({i},{p},{q},{s})] = {val} != {expected_v3}"
        )

    # Taylor coefficients in v_1(u_1, u_2, u_3) = a1*u_1 + a3_self*u_1^3 + a3_cross*u_1*(u_2^2 + u_3^2) + O(u^5)
    a1_lon = J1[0][0]                                       # -2i
    a3_self_lon = v3_tensor[(0, 0, 0, 0)] / Fraction(6, 1)  # +i/12
    a3_cross_lon = v3_tensor[(0, 0, 1, 1)] / Fraction(2, 1) # -i/4
    a3_sym_lon = a3_self_lon + GFrac(2, 0) * a3_cross_lon   # -5i/12

    assert a3_self_lon == GFrac(0, Fraction(1, 12))
    assert a3_cross_lon == GFrac(0, Fraction(-1, 4))
    assert a3_sym_lon == GFrac(0, Fraction(-5, 12))

    # 5. Cross-check against 60-dps nonlinear mpmath Newton solves at eps = 10^{-8}
    eps = mp.mpf("1e-8")
    _, v_single_nl = solve_nonlinear_gluing_mpmath(eps, mp.mpc(0), mp.mpc(0))
    _, v_sym_nl = solve_nonlinear_gluing_mpmath(eps, eps, eps)
    _, v_asym_nl = solve_nonlinear_gluing_mpmath(eps, mp.mpc(2) * eps, mp.mpc(3) * eps)

    v1_single_taylor = a1_lon.to_mpc() * eps + a3_self_lon.to_mpc() * (eps ** 3)
    v1_sym_taylor = a1_lon.to_mpc() * eps + a3_sym_lon.to_mpc() * (eps ** 3)
    v1_asym_taylor = (
        a1_lon.to_mpc() * eps
        + a3_self_lon.to_mpc() * (eps ** 3)
        + a3_cross_lon.to_mpc() * eps * ((mp.mpf(2) * eps) ** 2 + (mp.mpf(3) * eps) ** 2)
    )

    err_single = abs(v_single_nl[0] - v1_single_taylor)
    err_sym = abs(v_sym_nl[0] - v1_sym_taylor)
    err_asym = abs(v_asym_nl[0] - v1_asym_taylor)

    # At eps = 10^{-8}, O(eps^5) is ~ 10^{-40}, so residual is < 10^{-38}
    assert err_single < mp.mpf("1e-36"), f"Single-cusp Taylor residual too large: {err_single}"
    assert err_sym < mp.mpf("1e-36"), f"Symmetric 3-cusp Taylor residual too large: {err_sym}"
    assert err_asym < mp.mpf("1e-35"), f"Asymmetric 3-cusp Taylor residual too large: {err_asym}"

    # Extracted numerical cubic coefficients (v_1(eps) + 2i*eps) / eps^3
    num_a3_single = (v_single_nl[0] - a1_lon.to_mpc() * eps) / (eps ** 3)
    num_a3_sym = (v_sym_nl[0] - a1_lon.to_mpc() * eps) / (eps ** 3)
    assert abs(num_a3_single - a3_self_lon.to_mpc()) < mp.mpf("1e-14")
    assert abs(num_a3_sym - a3_sym_lon.to_mpc()) < mp.mpf("1e-14")

    # 6. Quadratic complex-volume Hessian and symmetric kappa comparison
    # In the NZ convention (borromean_nz_adjoint_torsion.py), per-cusp modulus tau_i = +2i gives
    # per-cusp quadratic curvature kappa_per_cusp = -1 (or c_2_per_cusp = -1/2).
    # Because H_{ij} is strictly diagonal (H_{ij} = 0 for i != j), the symmetric deformation
    # u_1 = u_2 = u_3 = u has quadratic coefficient:
    #   kappa_Bor^sym = sum_{i=1}^3 kappa_{ii} + sum_{i != j} kappa_{ij} = 3 * (-1) + 0 = -3.
    kappa_per_cusp_nz = -1
    kappa_off_diag_sum = 0
    kappa_bor_sym_nz = 3 * kappa_per_cusp_nz + kappa_off_diag_sum

    witness = {
        "computation": "borromean-three-cusp-nz-hessian",
        "scriptFile": "borromean_three_cusp_nz_hessian_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "bean": "qou-ay84",
        "absorbed_beans": ["qou-mcus"],
        "epic": "qou-avtq",
        "engine": "exact Q(i) Gaussian-rational Gauss-Jordan + 60-dps mpmath Newton cross-check",
        "free_parameters": 0,
        "sign_flip_resolved": False,
        "inputs": {
            "manifold": "L6a4 (Borromean rings complement B_3, 3 cusps, 8 ideal tetrahedra = 2 regular ideal octahedra)",
            "q0": Q0_STR,
            "q0_pin": "proton (experimental pin, resolved)",
            "indep_edge_rows": list(INDEP_EDGE_INDICES),
            "complete_shapes_z0": [z.to_dict() for z in Z0_GFRAC],
            "complete_shapes_w0": [w.to_dict() for w in W0_GFRAC],
            "arithmetic": f"Exact Q(i) + mpmath at {mp.mp.dps} dps (no float64)",
        },
        "results": {
            "det_M_sys": det_M_sys.to_dict(),
            "abs_det_M_sys": 64,
            "first_order_shape_jacobian_4_dZ_du": [
                [scaled_Z1[k][j].to_dict() for j in range(3)] for k in range(8)
            ],
            "all_24_shape_sensitivities_nonzero": all(
                not Z1[k][j].is_zero() for k in range(8) for j in range(3)
            ),
            "longitude_jacobian_dv_du": [
                [J1[i][j].to_dict() for j in range(3)] for i in range(3)
            ],
            "cusp_modulus_matrix_tau": [
                [tau_matrix[i][j].to_dict() for j in range(3)] for i in range(3)
            ],
            "hessian_strictly_diagonal": all(
                J1[i][j].is_zero() for i in range(3) for j in range(3) if i != j
            ),
            "off_diagonal_quadratic_entries_count_nonzero": sum(
                0 if J1[i][j].is_zero() else 1
                for i in range(3)
                for j in range(3)
                if i != j
            ),
            "second_order_longitude_derivatives_all_zero": all(
                v2[i][col].is_zero() for i in range(3) for col in range(9)
            ),
            "third_order_longitude_derivatives": {
                "d3v_i_du_i3": v3_tensor[(0, 0, 0, 0)].to_dict(),
                "d3v_i_du_i_du_j2_for_j_ne_i": v3_tensor[(0, 0, 1, 1)].to_dict(),
                "d3v_1_du_1_du_2_du_3": v3_tensor[(0, 0, 1, 2)].to_dict(),
            },
            "longitude_taylor_coefficients": {
                "a1_linear": a1_lon.to_dict(),
                "a3_single_cusp_u_i3": a3_self_lon.to_dict(),
                "a3_inter_cusp_u_i_u_j2": a3_cross_lon.to_dict(),
                "a3_symmetric_3cusp": a3_sym_lon.to_dict(),
                "symmetric_to_single_cubic_ratio": "-5",
            },
            "mpmath_60dps_newton_verification": {
                "eps": fmt(eps),
                "single_cusp_residual_abs": fmt(err_single),
                "symmetric_3cusp_residual_abs": fmt(err_sym),
                "asymmetric_1_2_3_residual_abs": fmt(err_asym),
                "extracted_a3_single_imag": fmt(num_a3_single.imag),
                "exact_a3_single_imag": fmt(a3_self_lon.to_mpc().imag),
                "extracted_a3_sym_imag": fmt(num_a3_sym.imag),
                "exact_a3_sym_imag": fmt(a3_sym_lon.to_mpc().imag),
            },
            "quadratic_kappa_comparison": {
                "kappa_per_cusp_nz_frame": kappa_per_cusp_nz,
                "kappa_off_diagonal_sum": kappa_off_diag_sum,
                "kappa_bor_sym_nz_frame": kappa_bor_sym_nz,
                "three_times_kappa_per_cusp": 3 * kappa_per_cusp_nz,
                "quadratic_sym_equals_three_times_per_cusp": (
                    kappa_bor_sym_nz == 3 * kappa_per_cusp_nz
                ),
                "sign_flip_resolved": False,
            },
        },
        "verdict": (
            "EXACT ALGEBRAIC & 60-DPS VERIFICATION (scope-(b) at quadratic order, "
            "non-trivial inter-cusp coupling at quartic CVol / cubic longitude order): "
            "(1) For L6a4 (B_3), the 8x8 linearized gluing system at the regular-octahedral "
            "complete structure has det(M_sys) = -64i and a completely dense 8x3 shape "
            "sensitivity matrix 4*(dZ_k/du_j) in {+-1+-i}. "
            "(2) Despite shared octahedral tetrahedra, the 3x3 longitude Jacobian "
            "dv_i/du_j|_{u=0} = -2i*delta_{ij} (cusp modulus matrix tau_{ij} = +2i*delta_{ij}) "
            "is STRICTLY DIAGONAL with all 6 off-diagonal entries identically zero, forced by "
            "pairwise linking number lk(K_i, K_j) = 0 and (Z/2Z)^3 component-reversal parity. "
            "Hence at quadratic order in u, kappa_Bor^sym = 3 * kappa_per_cusp with zero "
            "off-diagonal cross-term (`sign_flip_resolved = False`). "
            "(3) Inter-cusp coupling from the shared octahedral edges first enters at 3rd order "
            "in v_i (4th order O(u^4) in CVol): d^3 v_i / du_i^3 = +i/2 while "
            "d^3 v_i / (du_i du_j^2) = -i/2 (j != i), so v_i(u) = -2i*u_i + (i/12)*u_i^3 "
            "- (i/4)*u_i*sum_{j!=i} u_j^2 + O(u^5). On the symmetric locus u_1=u_2=u_3=u, "
            "the two inter-cusp cross-terms flip the sign of the cubic longitude coefficient "
            "from +i/12 to -5i/12 (verified to < 10^{-36} against 60-dps Newton solves)."
        ),
        "lean": "QOU.QBeta.BorromeanThreeCuspNZHessian",
        "wired": False,
    }

    stamp_q0(witness, __file__)

    out_path = os.path.join(
        os.path.dirname(__file__), "borromean-three-cusp-nz-hessian.witness.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False
        )
        json.dump(witness, fh, indent=2)
        fh.write("\n")

    print(f"det(M_sys) = {det_M_sys}")
    print(f"J^(1) = dv_i/du_j |_{{u=0}} = {J1}")
    print(f"a3_single = {a3_self_lon}, a3_cross = {a3_cross_lon}, a3_sym = {a3_sym_lon}")
    print(f"60-dps Newton residuals: single={mp.nstr(err_single, 3)}, sym={mp.nstr(err_sym, 3)}, asym={mp.nstr(err_asym, 3)}")
    print(f"wrote {out_path}")
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
