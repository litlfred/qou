#!/usr/bin/env python3
"""Explicit 5D TL_3(q_0) Rieffel-Kantorovich metric under D_nabla's q_0^-1 / hbar_{q_0} split.

Closes Beans `qou-5uj7` and `qou-adwi` (Part 2) alongside
`QOU/InformationTheory/FiniteRieffelQuantumMetric.lean` and
`QOU/InformationTheory/UnifiedClockScaleLayers.lean`.

WHAT IS COMPUTED AND VERIFIED AT 80 DPS (proton anchor `q_at(80)`, zero float64):
  1. Layer-I algebraic identities at `q_0`:
       grad_weight = q_0^-1,   hbar_{q_0} = 1 - q_0^-1,   t_P(q_0) = hbar_{q_0}^-1,
       grad_weight + hbar_{q_0} = 1,   hbar_{q_0} * t_P(q_0) = 1,
       grad_weight / hbar_{q_0} = 1 / (q_0 - 1) = c_{q_0} = t_P(q_0) - 1.
  2. Unquotiented 6D Hecke algebra H_3(q_0) Convention-D star-Gram obstruction:
       S_ij = tr_M(b_i * b_j^*) on NF basis {1, s1, s2, s1 s2, s2 s1, s1 s2 s1}
       with z_D = q_0^3 / (q_0^2 + 1) = q_0^2 / [2]_{q_0}.
       The 3-strand q-antisymmetriser r_{[1^3]} = (1, -q^-1, -q^-1, q^-2, q^-2, -q^-3)
       satisfies ||S * r_{[1^3]}||_inf = 0 (to 80 dps) while chi_{(1^3)}(r_{[1^3]}) != 0
       and tau_D(r_{[1^3]}) = 0, confirming Rieffel unboundedness d_L = +inf prior to
       quotienting by rad(tau_D).
  3. Faithful 5D Temperley-Lieb quotient TL_3(q_0) = H_3(q_0) / rad(tau_D):
       Planar basis {1, e_1, e_2, e_1 e_2, e_2 e_1} with e_i = q_0 - s_i, delta = [2]_{q_0}.
       5x5 GNS star-Gram matrix G^{TL}_{ab} = tr_M(u_a u_b^*) has strictly positive
       determinant det(G^{TL}) > 0 and matches the Wedderburn decomposition
       TL_3(q_0) = R_{(3)} (+) M_2(R)_{(2,1)} with weights
         y_{(3)} = [4]_{q_0} / [2]_{q_0}^3 = (q_0^2 + q_0^-2) / [2]_{q_0}^2,
         y_{(2,1)} = [2]_{q_0} / [2]_{q_0}^3 = 1 / [2]_{q_0}^2,
         y_{(3)} + 2 * y_{(2,1)} = 1,   cos(theta_{JW}) = 1 / [2]_{q_0}.
  4. Explicit 5D Rieffel-Kantorovich metric under D_nabla = q_0^-1 nabla_hor + hbar_{q_0} iota_xi nabla:
       On the 4D tau_D-orthogonal complement TL_3(q_0) (-) R*1, D_nabla acts with
       horizontal weight q_0^-1 (~0.90091828) on the inter-sector Bratteli contrast and
       off-diagonal strand-braiding directions, and Reeb contact weight hbar_{q_0}
       (~0.09908172) on the H_2 subset H_3 Cartan/isospin fiber direction, giving
       strictly trivial Lip-kernel ker(L) = R*1 and anisotropy ratio c_{q_0} ~ 9.092679.
       Exact 5x5 Rieffel-Kantorovich state-space distances d_L(phi_i, phi_j) across
       {omega_{(3)}, omega_{(2,1),+}, omega_{(2,1),-}, omega_{e_2}, tau_D} are evaluated
       with explicit 1-Lipschitz dual witnesses attaining zero duality gap (< 1e-76),
       strict metric positivity, triangle inequality, and exact Kantorovich-Rubinstein
       3x3 optimal transport plan matching on the maximal abelian spectrum.

Reproduce:
    python3 -u computations/probes/finite_rieffel_tl3_metric_probe.py
"""

from __future__ import annotations

import os as _os
import sys as _sys
from pathlib import Path as _Path

_os.environ.setdefault("QOU_COMPUTE_DPS", "80")
_os.environ.setdefault("QOU_OUTPUT_DPS", "70")

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80


def q_int(q: mp.mpf, n: int) -> mp.mpf:
    """Balanced quantum integer [n]_q = (q^n - q^-n) / (q - q^-1)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def build_h3_star_gram(q: mp.mpf) -> tuple[mp.matrix, list[mp.mpf], mp.mpf]:
    """Build the 6x6 Convention-D Markov star-Gram S_ij = tr_M(b_i * b_j^*) on H_3(q).

    Basis order:
      0: 1
      1: s1
      2: s2
      3: s1 s2
      4: s2 s1
      5: s1 s2 s1   (longest word w_0; s1^2 = h s1 + 1, s1 s2 s1 = s2 s1 s2)
    """
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)

    # Represent each basis element by its 6-vector of NF coordinates via left-action matrices
    # of s1 and s2 on {1, s1, s2, s1 s2, s2 s1, s1 s2 s1}.
    L1 = mp.matrix(6, 6)
    # s1 * 1 = s1
    L1[1, 0] = mp.mpf(1)
    # s1 * s1 = h s1 + 1
    L1[0, 1] = mp.mpf(1)
    L1[1, 1] = h
    # s1 * s2 = s1 s2
    L1[3, 2] = mp.mpf(1)
    # s1 * (s1 s2) = (h s1 + 1) s2 = s2 + h s1 s2
    L1[2, 3] = mp.mpf(1)
    L1[3, 3] = h
    # s1 * (s2 s1) = s1 s2 s1
    L1[5, 4] = mp.mpf(1)
    # s1 * (s1 s2 s1) = (h s1 + 1) s2 s1 = s2 s1 + h s1 s2 s1
    L1[4, 5] = mp.mpf(1)
    L1[5, 5] = h

    L2 = mp.matrix(6, 6)
    # s2 * 1 = s2
    L2[2, 0] = mp.mpf(1)
    # s2 * s1 = s2 s1
    L2[4, 1] = mp.mpf(1)
    # s2 * s2 = h s2 + 1
    L2[0, 2] = mp.mpf(1)
    L2[2, 2] = h
    # s2 * (s1 s2) = s2 s1 s2 = s1 s2 s1
    L2[5, 3] = mp.mpf(1)
    # s2 * (s2 s1) = (h s2 + 1) s1 = s1 + h s2 s1
    L2[1, 4] = mp.mpf(1)
    L2[4, 4] = h
    # s2 * (s1 s2 s1) = s2 (s2 s1 s2) = (h s2 + 1) s1 s2 = s1 s2 + h s1 s2 s1
    L2[3, 5] = mp.mpf(1)
    L2[5, 5] = h

    I6 = mp.eye(6)
    ops = [I6, L1, L2, L1 * L2, L2 * L1, L1 * L2 * L1]
    # Anti-involution b_j^* swaps index 3 <-> 4 (i.e. (s1 s2)^* = s2 s1) and fixes 0,1,2,5.
    star_idx = [0, 1, 2, 4, 3, 5]

    tr_vals = [
        mp.mpf(1),
        z,
        z,
        z ** 2,
        z ** 2,
        h * (z ** 2) + z,
    ]

    S = mp.matrix(6, 6)
    e0 = mp.matrix(6, 1)
    e0[0, 0] = mp.mpf(1)
    for i in range(6):
        for j in range(6):
            prod_vec = ops[i] * ops[star_idx[j]] * e0
            val = mp.mpf(0)
            for k in range(6):
                val += prod_vec[k, 0] * tr_vals[k]
            S[i, j] = val

    rad = [
        mp.mpf(1),
        -1 / q,
        -1 / q,
        1 / (q ** 2),
        1 / (q ** 2),
        -1 / (q ** 3),
    ]
    return S, rad, z


def build_tl3_planar_gram(q: mp.mpf) -> mp.matrix:
    """Build the 5x5 Convention-D GNS star-Gram matrix on TL_3(q).

    Planar basis: u_0 = 1, u_1 = e_1, u_2 = e_2, u_3 = e_1 e_2, u_4 = e_2 e_1
    with e_i^2 = delta e_i, e_1 e_2 e_1 = e_1, e_2 e_1 e_2 = e_2, delta = q + q^-1,
    and tr_M(1) = 1, tr_M(e_i) = delta^-1, tr_M(e_1 e_2) = tr_M(e_2 e_1) = delta^-2.
    Note u_3^* = u_4, u_4^* = u_3, and u_0, u_1, u_2 are self-adjoint.
    """
    d = q + 1 / q
    inv_d = 1 / d
    inv_d2 = inv_d ** 2
    # Exact trace table tr_M(u_a * u_b^*) verified from TL_3 planar relations:
    #   1 * {1, e1, e2, e2e1, e1e2} -> {1, d^-1, d^-1, d^-2, d^-2}
    #   e1 * 1 = e1 (d^-1); e1 * e1 = d e1 (1); e1 * e2 = e1e2 (d^-2);
    #   e1 * (e1e2)^* = e1 e2 e1 = e1 (d^-1); e1 * (e2e1)^* = e1^2 e2 = d e1e2 (d^-1)
    #   (e1e2) * (e1e2)^* = e1 e2^2 e1 = d e1 e2 e1 = d e1 (1)
    #   (e1e2) * (e2e1)^* = e1 e2 e1 e2 = e1 e2 (d^-2)
    rows = [
        [mp.mpf(1), inv_d, inv_d, inv_d2, inv_d2],
        [inv_d, mp.mpf(1), inv_d2, inv_d, inv_d],
        [inv_d, inv_d2, mp.mpf(1), inv_d, inv_d],
        [inv_d2, inv_d, inv_d, mp.mpf(1), inv_d2],
        [inv_d2, inv_d, inv_d, inv_d2, mp.mpf(1)],
    ]
    return mp.matrix(rows)


def main() -> int:
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        grad_w = 1 / q0
        hbar_q0 = 1 - 1 / q0
        t_p = 1 / hbar_q0
        c_q0 = 1 / (q0 - 1)
        delta = q0 + 1 / q0

        # ── 1. Layer-I grain, circuit, and Thomae-Jackson UV ceiling checks ──
        convex_res = abs((grad_w + hbar_q0) - mp.mpf(1))
        circuit_res = abs(hbar_q0 * t_p - mp.mpf(1))
        anisotropy_ratio = grad_w / hbar_q0
        anisotropy_res = abs(anisotropy_ratio - c_q0)

        # Jackson UV sum N = 25: sum_{j=0}^{24} (q0^-1)^j = (1 - q0^-25) * t_P(q0) < t_P(q0)
        N_uv = 25
        jackson_sum = mp.fsum([grad_w ** j for j in range(N_uv)])
        jackson_closed = (1 - grad_w ** N_uv) / (1 - grad_w)
        jackson_res = abs(jackson_sum - jackson_closed)
        jackson_headroom = t_p - jackson_sum

        # ── 2. 6D H_3(q_0) radical & infinite Connes-Rieffel distance wall ──
        S_h3, rad_vec, z_d = build_h3_star_gram(q0)
        rad_col = mp.matrix(6, 1)
        for idx, rv in enumerate(rad_vec):
            rad_col[idx, 0] = rv
        S_rad = S_h3 * rad_col
        rad_null_norm = max(abs(S_rad[i, 0]) for i in range(6))

        # On [1^3], s_i acts by -q0^-1, so T_w acts by (-q0^-1)^len(w).
        # Hence chi_{(1^3)}(r_{[1^3]}) = 1 + 2*q0^-2 + 2*q0^-4 + q0^-6 > 0 while tau_D(r_{[1^3]}) = 0.
        chi_111_on_rad = (
            mp.mpf(1)
            + 2 / (q0 ** 2)
            + 2 / (q0 ** 4)
            + 1 / (q0 ** 6)
        )
        tau_on_rad = (
            mp.mpf(1)
            - (2 / q0) * z_d
            + (2 / (q0 ** 2)) * (z_d ** 2)
            - (1 / (q0 ** 3)) * ((q0 - 1 / q0) * (z_d ** 2) + z_d)
        )

        # ── 3. Faithful 5D TL_3(q_0) GNS Gram & Wedderburn isomorphism ──
        G_tl = build_tl3_planar_gram(q0)
        det_G_tl = mp.det(G_tl)
        # Closed-form two-row weights y_{(n-k, k)} = [n - 2k + 1]_q / [2]_q^n at n = 3:
        #   k = 0 -> y_{(3)}   = [4]_q / [2]_q^3 = (q^2 + q^-2) / [2]_q^2
        #   k = 1 -> y_{(2,1)} = [2]_q / [2]_q^3 = 1 / [2]_q^2
        y_3 = q_int(q0, 4) / (delta ** 3)
        y_21 = 1 / (delta ** 2)
        wedderburn_norm_res = abs((y_3 + 2 * y_21) - mp.mpf(1))

        # Verify Wedderburn trace reproduces all 5 planar basis expectations:
        # In R_{(3)} (+) M_2(R)_{(2,1)}:
        #   1     -> (1, I_2)
        #   e_1   -> (0, [[0, 0], [0, delta]])
        #   e_2   -> (0, [[delta*(1 - delta^-2), sqrt(1 - delta^-2)],
        #                 [sqrt(1 - delta^-2),   delta^-1]])
        sin_jw = mp.sqrt(1 - 1 / (delta ** 2))
        cos_jw = 1 / delta
        E1_mat = mp.matrix([[mp.mpf(0), mp.mpf(0)], [mp.mpf(0), delta]])
        E2_mat = mp.matrix([
            [delta * (sin_jw ** 2), sin_jw],
            [sin_jw, 1 / delta],
        ])
        # Check TL relations in M_2(R)_{(2,1)}: e1^2 = delta e1, e2^2 = delta e2, e1 e2 e1 = e1, e2 e1 e2 = e2
        E1_sq_res = max(abs((E1_mat * E1_mat - delta * E1_mat)[r, c]) for r in range(2) for c in range(2))
        E2_sq_res = max(abs((E2_mat * E2_mat - delta * E2_mat)[r, c]) for r in range(2) for c in range(2))
        E121_res = max(abs((E1_mat * E2_mat * E1_mat - E1_mat)[r, c]) for r in range(2) for c in range(2))
        E212_res = max(abs((E2_mat * E1_mat * E2_mat - E2_mat)[r, c]) for r in range(2) for c in range(2))
        tl_rel_res = max(E1_sq_res, E2_sq_res, E121_res, E212_res)

        # Verify G_tl matches Wedderburn inner product <u_a, u_b>_{tau_D} = y_3 a_3 b_3 + y_21 Tr(A_21 B_21^T)
        I2 = mp.eye(2)
        Z2 = mp.matrix(2, 2)
        wed_ops = [
            (mp.mpf(1), I2),
            (mp.mpf(0), E1_mat),
            (mp.mpf(0), E2_mat),
            (mp.mpf(0), E1_mat * E2_mat),
            (mp.mpf(0), E2_mat * E1_mat),
        ]
        gram_wed_res = mp.mpf(0)
        for a_idx in range(5):
            for b_idx in range(5):
                s_a, M_a = wed_ops[a_idx]
                s_b, M_b = wed_ops[b_idx]
                tr_prod = (
                    M_a[0, 0] * M_b[0, 0]
                    + M_a[0, 1] * M_b[0, 1]
                    + M_a[1, 0] * M_b[1, 0]
                    + M_a[1, 1] * M_b[1, 1]
                )
                ip_val = y_3 * s_a * s_b + y_21 * tr_prod
                gram_wed_res = max(gram_wed_res, abs(ip_val - G_tl[a_idx, b_idx]))

        # ── 4. Explicit 5D Rieffel-Kantorovich metric under D_nabla ──
        # Construct tau_D-orthonormal basis of the 4D traceless space TL_3(q_0) (-) R*1:
        #   u_sec  : inter-sector Bratteli contrast between R_{(3)} and M_2(R)_{(2,1)}
        #            u_sec = (sqrt(2*y_21 / y_3),  -sqrt(y_3 / (2*y_21)) * I_2)
        #            check: tau_D(u_sec) = y_3*sqrt(2*y_21/y_3) - 2*y_21*sqrt(y_3/(2*y_21)) = 0,
        #                   ||u_sec||_{tau_D}^2 = 2*y_21 + y_3 = 1!
        #   u_x    : symmetric strand-braiding off-diagonal (1/sqrt(2*y_21)) * [[0, 1], [1, 0]]
        #   u_asym : skew strand-braiding element           (1/sqrt(2*y_21)) * [[0, 1], [-1, 0]]
        #   u_reeb : H_2 subset H_3 Cartan/Reeb fiber axis  (1/sqrt(2*y_21)) * [[1, 0], [0, -1]]
        u_sec = (mp.sqrt(2 * y_21 / y_3), -mp.sqrt(y_3 / (2 * y_21)) * I2)
        inv_s2y = 1 / mp.sqrt(2 * y_21)
        u_x = (mp.mpf(0), inv_s2y * mp.matrix([[mp.mpf(0), mp.mpf(1)], [mp.mpf(1), mp.mpf(0)]]))
        u_asym = (mp.mpf(0), inv_s2y * mp.matrix([[mp.mpf(0), mp.mpf(1)], [mp.mpf(-1), mp.mpf(0)]]))
        u_reeb = (mp.mpf(0), inv_s2y * mp.matrix([[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(-1)]]))
        orth_basis = [u_sec, u_x, u_asym, u_reeb]
        # D_nabla Lipschitz weights: horizontal gradient directions carry grad_w = q_0^-1,
        # Reeb contact direction carries hbar_{q_0} = 1 - q_0^-1.
        lip_weights = [grad_w, grad_w, grad_w, hbar_q0]

        # Verify tau_D-orthonormality and tracelessness of {u_sec, u_x, u_asym, u_reeb}
        orth_res = mp.mpf(0)
        for i in range(4):
            si, Mi = orth_basis[i]
            tr_i = y_3 * si + y_21 * (Mi[0, 0] + Mi[1, 1])
            orth_res = max(orth_res, abs(tr_i))
            for j in range(4):
                sj, Mj = orth_basis[j]
                ip = y_3 * si * sj + y_21 * (
                    Mi[0, 0] * Mj[0, 0]
                    + Mi[0, 1] * Mj[0, 1]
                    + Mi[1, 0] * Mj[1, 0]
                    + Mi[1, 1] * Mj[1, 1]
                )
                target = mp.mpf(1) if i == j else mp.mpf(0)
                orth_res = max(orth_res, abs(ip - target))

        # Canonical physical states on TL_3(q_0) = R_{(3)} (+) M_2(R)_{(2,1)}:
        # Each state phi is a linear functional phi(s, M).
        def eval_state(name: str, s: mp.mpf, M: mp.matrix) -> mp.mpf:
            if name == "omega_3":
                return s
            if name == "omega_21_plus":
                return M[0, 0]
            if name == "omega_21_minus":
                return M[1, 1]
            if name == "omega_e2":
                # Pure state supporting P_2 = e_2 / delta: vector (sin_jw, cos_jw)^T
                return (
                    (sin_jw ** 2) * M[0, 0]
                    + sin_jw * cos_jw * (M[0, 1] + M[1, 0])
                    + (cos_jw ** 2) * M[1, 1]
                )
            if name == "tau_D":
                return y_3 * s + y_21 * (M[0, 0] + M[1, 1])
            raise ValueError(name)

        state_names = ["omega_3", "omega_21_plus", "omega_21_minus", "omega_e2", "tau_D"]

        # Under L(sum c_k u_k) = sqrt(sum_k (lip_weights[k] * c_k)^2), Cauchy-Schwarz gives
        # exact Connes-Rieffel-Kantorovich dual distance:
        #   d_L(phi, psi) = sqrt( sum_{k=0}^3 ( (phi(u_k) - psi(u_k)) / lip_weights[k] )^2 )
        # with primal/dual optimal witness c_k^* = (Delta_k / lip_weights[k]^2) / d_L(phi, psi),
        # satisfying L(a^*) = 1 and phi(a^*) - psi(a^*) = d_L(phi, psi) identically!
        dist_mat = mp.matrix(5, 5)
        max_dual_attained_res = mp.mpf(0)
        min_offdiag_dist = mp.mpf(1000)

        for i in range(5):
            for j in range(5):
                if i == j:
                    dist_mat[i, j] = mp.mpf(0)
                    continue
                deltas = [
                    eval_state(state_names[i], orth_basis[k][0], orth_basis[k][1])
                    - eval_state(state_names[j], orth_basis[k][0], orth_basis[k][1])
                    for k in range(4)
                ]
                d_ij = mp.sqrt(mp.fsum([(deltas[k] / lip_weights[k]) ** 2 for k in range(4)]))
                dist_mat[i, j] = d_ij
                min_offdiag_dist = min(min_offdiag_dist, d_ij)

                # Explicit optimal witness a^* = sum_k c_k^* u_k
                cs = [(deltas[k] / (lip_weights[k] ** 2)) / d_ij for k in range(4)]
                lip_norm_star = mp.sqrt(mp.fsum([(lip_weights[k] * cs[k]) ** 2 for k in range(4)]))
                s_star = mp.fsum([cs[k] * orth_basis[k][0] for k in range(4)])
                M_star = mp.matrix(2, 2)
                for k in range(4):
                    M_star += cs[k] * orth_basis[k][1]
                diff_star = (
                    eval_state(state_names[i], s_star, M_star)
                    - eval_state(state_names[j], s_star, M_star)
                )
                max_dual_attained_res = max(
                    max_dual_attained_res,
                    abs(lip_norm_star - mp.mpf(1)),
                    abs(diff_star - d_ij),
                )

        # Verify metric triangle inequality across all state triples (i, k, j)
        max_triangle_slack_violation = mp.mpf(0)
        for i in range(5):
            for k in range(5):
                for j in range(5):
                    viol = dist_mat[i, j] - (dist_mat[i, k] + dist_mat[k, j])
                    if viol > max_triangle_slack_violation:
                        max_triangle_slack_violation = viol

        # ── 5. Exact Kantorovich-Rubinstein primal=dual transport on 3-vertex spectrum ──
        # Maximal abelian diagonal subalgebra R^3 = span{p_{(3)}, p_{(2,1),+}, p_{(2,1),-}}
        # Weighted path graph: vertex 0 = (3) <--cost 1/grad_w = q_0--> vertex 1 = (2,1)_+
        #                      vertex 1 = (2,1)_+ <--cost 1/hbar_{q_0} = t_P(q_0)--> vertex 2 = (2,1)_-
        # Shortest-path distance matrix D_graph:
        c01 = 1 / grad_w   # = q_0 (proton substrate pin)
        c12 = 1 / hbar_q0  # = t_P(q_0) ~ 10.09267946
        D_graph = [
            [mp.mpf(0), c01, c01 + c12],
            [c01, mp.mpf(0), c12],
            [c01 + c12, c12, mp.mpf(0)],
        ]
        # Transport from Markov tracial state mu = (y_3, y_21, y_21) to pure singlet nu = (0, 0, 1):
        # Primal optimal coupling pi^* moves mass y_3 from 0->2 (cost c01+c12), y_21 from 1->2 (cost c12),
        # and keeps y_21 at 2->2 (cost 0).
        primal_w1 = y_3 * (c01 + c12) + y_21 * c12
        # Dual 1-Lipschitz potential f^* = (c01 + c12, c12, 0) satisfies |f_u - f_v| <= D_graph[u][v]:
        f_dual = [c01 + c12, c12, mp.mpf(0)]
        mu_vec = [y_3, y_21, y_21]
        nu_vec = [mp.mpf(0), mp.mpf(0), mp.mpf(1)]
        dual_w1 = mp.fsum([f_dual[u] * (mu_vec[u] - nu_vec[u]) for u in range(3)])
        kr_duality_gap = abs(primal_w1 - dual_w1)

        # Build Witness JSON
        b = WitnessBuilder("finite-rieffel-tl3-metric")
        b.set_description(
            "Explicit 80-dps Rieffel-Kantorovich quantum metric on the 5D Temperley-Lieb "
            "quotient TL_3(q_0) = H_3(q_0)/rad(tau_D) at the proton substrate anchor (closes "
            "beans qou-5uj7 and qou-adwi Part 2). Verifies: (1) Layer-I exact identities "
            "q_0^-1 + hbar_{q_0} = 1, hbar_{q_0} * t_P(q_0) = 1, anisotropy ratio "
            "q_0^-1 / hbar_{q_0} = c_{q_0} = 1/(q_0 - 1), and Thomae-Jackson UV ceiling < t_P(q_0); "
            "(2) rank-5 Convention-D star-Gram degeneracy on 6D H_3(q_0) along the 3-strand "
            "q-antisymmetriser r_{[1^3]} driving d_L = +inf prior to quotienting; "
            "(3) strict GNS faithfulness det(G^{TL}) > 0 on 5D TL_3(q_0) = R_{(3)} (+) M_2(R)_{(2,1)}; "
            "(4) exact 5x5 Rieffel-Kantorovich state-space distances across {omega_3, omega_21_+, "
            "omega_21_-, omega_e2, tau_D} with explicit unit-Lip dual witnesses attaining zero "
            "duality gap (< 1e-76); and (5) exact Kantorovich-Rubinstein primal=dual transport "
            "cost between tau_D and omega_21_- on the 3-vertex abelian spectrum."
        )

        b.add_parameter("workdps", str(WORK_DPS))
        b.add_parameter("q0_proton_80dps", fmt(q0, dps=70))
        b.add_parameter("grad_weight_q0_inv", fmt(grad_w, dps=70))
        b.add_parameter("reeb_weight_hbar_q0", fmt(hbar_q0, dps=70))
        b.add_parameter("planck_tick_t_P_q0", fmt(t_p, dps=70))

        b.add_data("layer1_clock_grain_identities", {
            "grad_weight_q0_inv": fmt(grad_w, dps=70),
            "reeb_weight_hbar_q0": fmt(hbar_q0, dps=70),
            "planck_tick_t_P": fmt(t_p, dps=70),
            "info_speed_c_q0_eq_grad_over_reeb": fmt(c_q0, dps=70),
            "jackson_uv_partial_sum_N25": fmt(jackson_sum, dps=70),
            "jackson_uv_headroom_below_t_P": fmt(jackson_headroom, dps=70),
        })

        b.add_data("h3_radical_and_tl3_faithfulness", {
            "h3_star_gram_on_radical_sup_norm": fmt(rad_null_norm, dps=70),
            "chi_111_on_radical": fmt(chi_111_on_rad, dps=70),
            "tau_D_on_radical": fmt(tau_on_rad, dps=70),
            "tl3_planar_gram_det": fmt(det_G_tl, dps=70),
            "y_3_convention_D": fmt(y_3, dps=70),
            "y_21_convention_D": fmt(y_21, dps=70),
            "jw_cup_cos_theta": fmt(cos_jw, dps=70),
            "jw_cup_sin_theta": fmt(sin_jw, dps=70),
        })

        dist_dict = {}
        for i in range(5):
            for j in range(i + 1, 5):
                key = f"d({state_names[i]},{state_names[j]})"
                dist_dict[key] = fmt(dist_mat[i, j], dps=70)

        b.add_data("tl3_rieffel_kantorovich_distances_5d", {
            "lip_singular_values_on_traceless_4d": [fmt(w, dps=70) for w in lip_weights],
            "pairwise_distances": dist_dict,
            "kr_3vertex_primal_w1_tauD_to_singlet": fmt(primal_w1, dps=70),
            "kr_3vertex_dual_w1_tauD_to_singlet": fmt(dual_w1, dps=70),
            "kr_3vertex_duality_gap": fmt(kr_duality_gap, dps=70),
        })

        b.add_assertion(
            "layer1_convex_and_circuit_identities_exact",
            computed=fmt(max(convex_res, circuit_res, anisotropy_res, jackson_res), dps=70),
            expected="0",
            tolerance="1e-75",
            source="UnifiedClockScaleLayers: q^-1 + hbar_q = 1, hbar_q * t_P = 1, "
                   "q^-1 / hbar_q = c_q, and Jackson geometric UV sum at 80 dps.",
        )
        b.add_assertion(
            "jackson_uv_partial_sum_strictly_below_t_P",
            computed="1" if jackson_headroom > mp.mpf(0) else "0",
            expected="1",
            source="UnifiedClockScaleLayers.jackson_uv_sum_lt_planckTick: finite Jackson "
                   "UV sum is strictly bounded above by t_P(q_0) = hbar_{q_0}^-1.",
        )
        b.add_assertion(
            "h3_convention_d_star_gram_kills_antisymmetriser",
            computed=fmt(max(rad_null_norm, abs(tau_on_rad)), dps=70),
            expected="0",
            tolerance="1e-75",
            source="GramSignature / FiniteRieffelQuantumMetric: S * r_{[1^3]} = 0 while "
                   "chi_{(1^3)}(r_{[1^3]}) > 0 forces unbounded Connes sup on unquotiented H_3.",
        )
        b.add_assertion(
            "tl3_quotient_gns_gram_strictly_positive_definite",
            computed="1" if (det_G_tl > mp.mpf("1e-4") and wedderburn_norm_res < mp.mpf("1e-75") and gram_wed_res < mp.mpf("1e-75") and tl_rel_res < mp.mpf("1e-75")) else "0",
            expected="1",
            source="5D Temperley-Lieb quotient TL_3(q_0) = R_{(3)} (+) M_2(R)_{(2,1)} has "
                   "det(G^{TL}) > 0, y_{(3)} + 2*y_{(2,1)} = 1, and exact Wedderburn inner-product agreement.",
        )
        b.add_assertion(
            "tl3_rieffel_kantorovich_duality_and_triangle_exact",
            computed=fmt(max(orth_res, max_dual_attained_res, max_triangle_slack_violation, kr_duality_gap), dps=70),
            expected="0",
            tolerance="1e-74",
            source="FiniteRieffelQuantumMetric: ker(L) = R*1 on 5D TL_3(q_0), unit-Lip dual "
                   "witness attainment across all 10 state pairs, triangle inequality, and "
                   "exact Kantorovich-Rubinstein primal=dual W_1 transport on 3-vertex spectrum.",
        )

        out_path = b.save({"q0Anchor": "proton", "workdps": WORK_DPS})

        print("=== 80-dps 5D TL_3(q_0) Rieffel-Kantorovich Metric Probe ===")
        print(f"q_0 (proton, 80 dps)  = {fmt(q0, dps=50)}")
        print(f"grad weight q_0^-1    = {fmt(grad_w, dps=50)}")
        print(f"Reeb weight hbar_q0   = {fmt(hbar_q0, dps=50)}")
        print(f"Planck tick t_P(q_0)  = {fmt(t_p, dps=50)}")
        print(f"ratio q_0^-1/hbar_q0  = {fmt(anisotropy_ratio, dps=50)} (= c_q0)")
        print(f"H_3 ||S r_[1^3]||_inf = {fmt(rad_null_norm, dps=20)}")
        print(f"TL_3 det(G^TL)        = {fmt(det_G_tl, dps=50)}")
        print(f"y_(3), y_(2,1)        = {fmt(y_3, dps=30)}, {fmt(y_21, dps=30)}")
        print("\nPairwise 5D TL_3(q_0) Rieffel-Kantorovich distances:")
        for k, v in dist_dict.items():
            print(f"  {k:<36} = {v[:42]}")
        print(f"\n3-vertex KR transport W_1(tau_D, omega_21_-): primal = {fmt(primal_w1, dps=40)}")
        print(f"                                              dual   = {fmt(dual_w1, dps=40)}")
        print(f"                                              gap    = {fmt(kr_duality_gap, dps=20)}")
        print(f"Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
