#!/usr/bin/env python3
"""Pre-registered 80-dps probe for Closing Open Gap 1 Backup (Option 1B, bean `qou-3kkz`):
4-Body Tetrahedral K_4 Colour-Flux Ring Exchange, Nucleon-Cluster Wigner Majorana Space-Exchange,
and Zero-Parameter 3D Jacobi Variational Compression across A = 2, 3, 4.

Pre-registration committed & pushed BEFORE any numerical binding evaluation:
  - `computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/PREREGISTRATION.md`
Formal Lean 4 backing (`0 sorry`, `0 axiom`, zero empirical literals, generic §7c):
  - `folio/quantum-observable-universe/lean/QOU/Nuclear/TetrahedralFluxRingAndMajoranaCluster.lean`

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - exact symbolic `sympy` verification over `Q(q)` for 9q & 12q Jimbo overlaps, rank-1 cluster
    transfer matrix M(q), and closed triangular/tetrahedral plaquette cumulants,
  - zero `float64` imports, casts, or binary float literals (`probe-float64-guard.py --strict` clean),
  - zero post-hoc parameter fitting (`free_parameters = 0`; only CAL-1/2/3 enter MeV readouts).
"""

from __future__ import annotations

import itertools
import operator
import sys
from pathlib import Path
from typing import Callable

_ROOT = Path(__file__).resolve().parents[3]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
FX_BITS = 340  # 2^340 ~ 2.24e102 (> 102 decimal digits: 22+ guard digits above WORK_DPS = 80)
FX_ONE = 1 << FX_BITS
FX_HALF = 1 << (FX_BITS - 1)
set_compute_dps(WORK_DPS)

SyTableau = tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
BraidWord = list[tuple[int, bool]]

# Canonical K_4 Tait 3-edge-colouring strand assignment phi(a, b) (0-indexed strands 0..11),
# pairing all 12 valence quarks 1-to-1 with the 12 half-edges of K_4 without reuse:
TAIT_EDGE_STRANDS: dict[tuple[int, int], tuple[int, int]] = {
    (0, 1): (2, 3),   # colour 0
    (2, 3): (8, 9),   # colour 0
    (0, 2): (1, 7),   # colour 1
    (1, 3): (4, 10),  # colour 1
    (0, 3): (0, 11),  # colour 2
    (1, 2): (5, 6),   # colour 2
}

# Canonical unoriented Hamiltonian 4-cycles on K_4 (fixing base vertex 0 and canonicalizing reversal):
K4_UNORIENTED_4CYCLES: tuple[tuple[int, int, int, int], ...] = (
    (0, 1, 2, 3),
    (0, 1, 3, 2),
    (0, 2, 1, 3),
)


# ---------------------------------------------------------------------------
# Part 1: Exact Combinatorial, Wigner SU(4) Majorana & Symbolic Q(q) Checks
# ---------------------------------------------------------------------------
def verify_part1_combinatorics_and_wigner() -> dict:
    """Verify exact K_A simplex/cycle counts, Tait 12-quark bijection, and Wigner [1^A]_{sigma tau}
    Majorana space-exchange eigenvalues +1 (A = 2, 3, 4) and Pauli shell closure (A = 5)."""
    simplex_counts: dict[str, dict[str, int]] = {}
    counts_ok = True
    expected = {
        1: (0, 0, 0, 0, 0, 0),
        2: (1, 2, 0, 0, 0, 0),
        3: (3, 6, 1, 2, 0, 0),
        4: (6, 12, 4, 8, 3, 6),
    }

    for a_nuc in (1, 2, 3, 4):
        verts = list(range(a_nuc))
        unoriented_edges = [(i, j) for i in verts for j in verts if i < j]
        oriented_edges = [(i, j) for i in verts for j in verts if i != j]
        unoriented_tris = [
            (i, j, k) for i in verts for j in verts for k in verts if i < j < k
        ]
        oriented_tris = [
            (i, j, k)
            for i in verts
            for j in verts
            for k in verts
            if i < j and i < k and j != k
        ]
        oriented_4cycles = [
            (0, b, c, d)
            for b in verts
            for c in verts
            for d in verts
            if 0 < b and 0 < c and 0 < d and len({0, b, c, d}) == 4
        ]
        unoriented_4cycles = [
            (a0, b, c, d) for (a0, b, c, d) in oriented_4cycles if b < d
        ]
        tup = (
            len(unoriented_edges),
            len(oriented_edges),
            len(unoriented_tris),
            len(oriented_tris),
            len(unoriented_4cycles),
            len(oriented_4cycles),
        )
        if tup != expected[a_nuc]:
            counts_ok = False
        simplex_counts[f"A={a_nuc}"] = {
            "unoriented_edges": tup[0],
            "oriented_edges": tup[1],
            "unoriented_triangles": tup[2],
            "oriented_triangles": tup[3],
            "unoriented_4cycles": tup[4],
            "oriented_4cycles": tup[5],
        }

    # Tetrahedral boundary S^2 Euler characteristic V - E + F = 4 - 6 + 4 = 2
    euler_k4 = 4 - simplex_counts["A=4"]["unoriented_edges"] + simplex_counts["A=4"]["unoriented_triangles"]
    euler_ok = euler_k4 == 2

    # Verify Tait 3-matching bijection on K_4 and valid strand bounds on A = 2, 3, 4
    used_strands_k4: list[int] = []
    tait_clusters_ok = True
    for (a_idx, b_idx), (s_left, s_right) in TAIT_EDGE_STRANDS.items():
        used_strands_k4.extend([s_left, s_right])
        if not (3 * a_idx <= s_left < 3 * a_idx + 3 and 3 * b_idx <= s_right < 3 * b_idx + 3):
            tait_clusters_ok = False
    tait_bijection_ok = sorted(used_strands_k4) == list(range(12)) and tait_clusters_ok

    # Integer Pauli swap identity 4 P_{12}^{sigma tau} = (I + sigma_1 . sigma_2)(I + tau_1 . tau_2)
    # on single-nucleon spin-isospin states {0,1}_sigma x {0,1}_tau (indexed 0..3):
    pauli_x = [[0, 1], [1, 0]]
    pauli_z = [[1, 0], [0, -1]]
    pauli_minus_y2 = [[0, -1], [1, 0]]  # i * sigma_y; (-i sigma_y) x (-i sigma_y) = + sigma_y x sigma_y

    def sigma_dot_2(s1: int, s2: int, s1p: int, s2p: int) -> int:
        # Matrix element of I + sigma_1 . sigma_2 = 2 P_{12}^sigma
        val = (1 if (s1 == s1p and s2 == s2p) else 0)
        val += pauli_x[s1][s1p] * pauli_x[s2][s2p]
        val -= pauli_minus_y2[s1][s1p] * pauli_minus_y2[s2][s2p]
        val += pauli_z[s1][s1p] * pauli_z[s2][s2p]
        return val

    pauli_fierz_ok = True
    for s1, t1, s2, t2, s1p, t1p, s2p, t2p in itertools.product((0, 1), repeat=8):
        lhs = 4 * (1 if (s1p == s2 and t1p == t2 and s2p == s1 and t2p == t1) else 0)
        rhs = sigma_dot_2(s1, s2, s1p, s2p) * sigma_dot_2(t1, t2, t1p, t2p)
        if lhs != rhs:
            pauli_fierz_ok = False
            break

    # Construct antisymmetric spin-isospin tensors Lambda^A(Z^4) = [1^A]_{sigma tau} for A = 2, 3, 4, 5
    wigner_checks: dict[str, dict] = {}
    wigner_all_ok = True
    for a_nuc in (2, 3, 4, 5):
        subsets = list(itertools.combinations(range(4), a_nuc))
        dim_st = len(subsets)
        pair_ok = True
        pair_sum_val = (a_nuc * (a_nuc - 1)) // 2
        for sub in subsets:
            # Antisymmetric basis tensor psi_sub on {0..3}^A
            psi: dict[tuple[int, ...], int] = {}
            for perm in itertools.permutations(sub):
                inv = sum(
                    1 for i in range(a_nuc) for j in range(i + 1, a_nuc) if perm[i] > perm[j]
                )
                psi[perm] = -1 if (inv % 2 == 1) else 1
            # Check Majorana space-exchange P_{ab}^x = -P_{ab}^{sigma tau} = +1 on every pair a < b
            for a_idx in range(a_nuc):
                for b_idx in range(a_idx + 1, a_nuc):
                    for cfg, amp in psi.items():
                        swapped = list(cfg)
                        swapped[a_idx], swapped[b_idx] = swapped[b_idx], swapped[a_idx]
                        maj_amp = -psi.get(tuple(swapped), 0)
                        if maj_amp != amp:
                            pair_ok = False
        expected_dim = {2: 6, 3: 4, 4: 1, 5: 0}[a_nuc]
        if dim_st != expected_dim or not pair_ok:
            wigner_all_ok = False
        wigner_checks[f"A={a_nuc}"] = {
            "spin_isospin_antisym_dim": dim_st,
            "majorana_all_pairs_plus_one": pair_ok,
            "majorana_pair_sum": pair_sum_val if dim_st > 0 else 0,
        }

    return {
        "all_combinatorics_and_wigner_pass": bool(
            counts_ok and euler_ok and tait_bijection_ok and pauli_fierz_ok and wigner_all_ok
        ),
        "kA_simplex_and_cycle_counts": simplex_counts,
        "k4_euler_characteristic": euler_k4,
        "k4_tait_12quark_bijection_exact": tait_bijection_ok,
        "pauli_spin_isospin_swap_identity_exact": pauli_fierz_ok,
        "wigner_majorana_su4_checks": wigner_checks,
    }


def verify_part1_sympy_9q_12q_plaquettes() -> dict:
    """Exact symbolic Q(q) check of Lean §3 theorems:
    - 9q open 2-interface R_{3,4} R_{6,7} overlap = (q^3 / [3]_q)^2
    - 9q single-quark cyclic 3-cycle R_{3,6} R_{6,9} overlap = (q^3 / [3]_q)^2
    - 12q open 3-interface R_{3,4} R_{6,7} R_{9,10} overlap = (q^3 / [3]_q)^3
    - clusterStepMat M(q) rank-1 identity & eigenvalues {[2]_q, -q^-3, -q^-3}
    - 9q closed triangular plaquette R_{3,4} R_{6,7} R_{9,1} = (q^9 [2]_q^3 - 8)/([2]_q^3 [3]_q^3)
      and connected colour-octet cumulant kappa_3(q) = -8 / ([2]_q^3 [3]_q^3)
    - 12q closed tetrahedral 4-cycle R_{3,4} R_{6,7} R_{9,10} R_{12,1} = (q^12 [2]_q^4 + 8)/([2]_q^4 [3]_q^4)
      and connected colour-octet cumulant kappa_4(q) = +8 / ([2]_q^4 [3]_q^4)
    """
    q = sp.Symbol("q", nonzero=True)
    inv_q = sp.Integer(1) / q
    q2 = q + inv_q
    q3 = q**2 + 1 + inv_q**2

    # Exact integer Laurent-polynomial arithmetic in Z[q, q^-1] (represented as {power: coeff})
    # for the 216-state (9q) and 1296-state (12q) multi-cluster contractions, then converted
    # directly into SymPy expressions over Q(q) for symbolic rational-function verification:
    def lmul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
        out: dict[int, int] = {}
        for ka, va in a.items():
            if va == 0:
                continue
            for kb, vb in b.items():
                if vb:
                    deg = ka + kb
                    nv = out.get(deg, 0) + va * vb
                    if nv:
                        out[deg] = nv
                    elif deg in out:
                        del out[deg]
        return out

    def ladd_inplace(acc: dict[int, int], term: dict[int, int]) -> None:
        for deg, val in term.items():
            if val:
                nv = acc.get(deg, 0) + val
                if nv:
                    acc[deg] = nv
                elif deg in acc:
                    del acc[deg]

    def l_to_sympy(poly: dict[int, int]) -> sp.Expr:
        return sum((sp.Integer(val) * (q**deg) for deg, val in sorted(poly.items())), sp.Integer(0))

    perms3 = list(itertools.permutations((0, 1, 2)))

    def inv_count(p: tuple[int, int, int]) -> int:
        return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])

    eps3_l: dict[tuple[int, int, int], dict[int, int]] = {
        p: {-inv_count(p): (-1 if (inv_count(p) % 2 == 1) else 1)} for p in perms3
    }
    norm_sq = sp.expand((1 + inv_q**2) * (1 + inv_q**2 + inv_q**4))

    l_q = {1: 1}
    l_one = {0: 1}
    l_h = {1: 1, -1: -1}

    def jr_transitions_l(c: int, d: int) -> list[tuple[int, int, dict[int, int]]]:
        if c == d:
            return [(c, c, l_q)]
        out: list[tuple[int, int, dict[int, int]]] = [(d, c, l_one)]
        if d < c:
            out.append((c, d, l_h))
        return out

    # 1. 9q open 2-interface R_{3,4} R_{6,7} (216 bra states)
    num_9q_open_l: dict[int, int] = {}
    for u1, v1 in eps3_l.items():
        for u2, v2 in eps3_l.items():
            v12 = lmul(v1, v2)
            for u3, v3 in eps3_l.items():
                bra_amp = lmul(v12, v3)
                for c1p, a2p, w12 in jr_transitions_l(u1[2], u2[0]):
                    k1 = (u1[0], u1[1], c1p)
                    if k1 not in eps3_l:
                        continue
                    bw1 = lmul(lmul(bra_amp, w12), eps3_l[k1])
                    for c2p, a3p, w23 in jr_transitions_l(u2[2], u3[0]):
                        k2 = (a2p, u2[1], c2p)
                        k3 = (a3p, u3[1], u3[2])
                        if k2 in eps3_l and k3 in eps3_l:
                            ladd_inplace(
                                num_9q_open_l,
                                lmul(lmul(bw1, w23), lmul(eps3_l[k2], eps3_l[k3])),
                            )
    ratio_9q_open = sp.simplify(l_to_sympy(num_9q_open_l) / (norm_sq**3))
    ok_9q_open = sp.simplify(ratio_9q_open - (q**3 / q3) ** 2) == 0

    # 2. 9q cyclic 3-quark R_{3,6} R_{6,9}
    num_9q_cyc3_l: dict[int, int] = {}
    for u1, v1 in eps3_l.items():
        for u2, v2 in eps3_l.items():
            v12 = lmul(v1, v2)
            for u3, v3 in eps3_l.items():
                bra_amp = lmul(v12, v3)
                for c1p, x_mid, w12 in jr_transitions_l(u1[2], u2[2]):
                    k1 = (u1[0], u1[1], c1p)
                    if k1 not in eps3_l:
                        continue
                    bw1 = lmul(lmul(bra_amp, w12), eps3_l[k1])
                    for c2p, c3p, w23 in jr_transitions_l(x_mid, u3[2]):
                        k2 = (u2[0], u2[1], c2p)
                        k3 = (u3[0], u3[1], c3p)
                        if k2 in eps3_l and k3 in eps3_l:
                            ladd_inplace(
                                num_9q_cyc3_l,
                                lmul(lmul(bw1, w23), lmul(eps3_l[k2], eps3_l[k3])),
                            )
    ratio_9q_cyc3 = sp.simplify(l_to_sympy(num_9q_cyc3_l) / (norm_sq**3))
    ok_9q_cyc3 = sp.simplify(ratio_9q_cyc3 - (q**3 / q3) ** 2) == 0

    # 3. 9q closed triangular plaquette R_{3,4} R_{6,7} R_{9,1}
    num_9q_tri_l: dict[int, int] = {}
    for u1, v1 in eps3_l.items():
        for u2, v2 in eps3_l.items():
            v12 = lmul(v1, v2)
            for u3, v3 in eps3_l.items():
                bra_amp = lmul(v12, v3)
                for c1p, a2p, w12 in jr_transitions_l(u1[2], u2[0]):
                    bw1 = lmul(bra_amp, w12)
                    for c2p, a3p, w23 in jr_transitions_l(u2[2], u3[0]):
                        k2 = (a2p, u2[1], c2p)
                        if k2 not in eps3_l:
                            continue
                        bw2 = lmul(lmul(bw1, w23), eps3_l[k2])
                        for c3p, a1p, w31 in jr_transitions_l(u3[2], u1[0]):
                            k1 = (a1p, u1[1], c1p)
                            k3 = (a3p, u3[1], c3p)
                            if k1 in eps3_l and k3 in eps3_l:
                                ladd_inplace(
                                    num_9q_tri_l,
                                    lmul(lmul(bw2, w31), lmul(eps3_l[k1], eps3_l[k3])),
                                )
    ratio_9q_tri = sp.simplify(l_to_sympy(num_9q_tri_l) / (norm_sq**3))
    expected_t3 = (q**9 * q2**3 - 8) / (q2**3 * q3**3)
    expected_k3 = -sp.Integer(8) / (q2**3 * q3**3)
    ok_9q_tri = sp.simplify(ratio_9q_tri - expected_t3) == 0
    ok_9q_k3 = sp.simplify((ratio_9q_tri - (q**3 / q3) ** 3) - expected_k3) == 0
    ok_9q_tri_q1 = sp.simplify(expected_t3.subs(q, 1)) == 0

    # 4. 12q open 3-interface R_{3,4} R_{6,7} R_{9,10} & closed 4-cycle R_{3,4} R_{6,7} R_{9,10} R_{12,1}
    num_12q_open_l: dict[int, int] = {}
    num_12q_ring_l: dict[int, int] = {}
    for u1, v1 in eps3_l.items():
        for u2, v2 in eps3_l.items():
            v12 = lmul(v1, v2)
            for c1p, a2p, w12 in jr_transitions_l(u1[2], u2[0]):
                v12w = lmul(v12, w12)
                for u3, v3 in eps3_l.items():
                    v123 = lmul(v12w, v3)
                    for c2p, a3p, w23 in jr_transitions_l(u2[2], u3[0]):
                        k2 = (a2p, u2[1], c2p)
                        if k2 not in eps3_l:
                            continue
                        w123 = lmul(lmul(v123, w23), eps3_l[k2])
                        for u4, v4 in eps3_l.items():
                            bra_amp = lmul(w123, v4)
                            for c3p, a4p, w34 in jr_transitions_l(u3[2], u4[0]):
                                k3 = (a3p, u3[1], c3p)
                                if k3 not in eps3_l:
                                    continue
                                w1234 = lmul(lmul(bra_amp, w34), eps3_l[k3])
                                k1_open = (u1[0], u1[1], c1p)
                                k4_open = (a4p, u4[1], u4[2])
                                if k1_open in eps3_l and k4_open in eps3_l:
                                    ladd_inplace(
                                        num_12q_open_l,
                                        lmul(w1234, lmul(eps3_l[k1_open], eps3_l[k4_open])),
                                    )
                                for c4p, a1p, w41 in jr_transitions_l(u4[2], u1[0]):
                                    k1_cl = (a1p, u1[1], c1p)
                                    k4_cl = (a4p, u4[1], c4p)
                                    if k1_cl in eps3_l and k4_cl in eps3_l:
                                        ladd_inplace(
                                            num_12q_ring_l,
                                            lmul(
                                                lmul(w1234, w41),
                                                lmul(eps3_l[k1_cl], eps3_l[k4_cl]),
                                            ),
                                        )

    ratio_12q_open = sp.simplify(l_to_sympy(num_12q_open_l) / (norm_sq**4))
    ok_12q_open = sp.simplify(ratio_12q_open - (q**3 / q3) ** 3) == 0

    ratio_12q_ring = sp.simplify(l_to_sympy(num_12q_ring_l) / (norm_sq**4))
    expected_t4 = (q**12 * q2**4 + 8) / (q2**4 * q3**4)
    expected_k4 = sp.Integer(8) / (q2**4 * q3**4)
    ok_12q_ring = sp.simplify(ratio_12q_ring - expected_t4) == 0
    ok_12q_k4 = sp.simplify((ratio_12q_ring - (q**3 / q3) ** 4) - expected_k4) == 0

    # 5. Exact 3x3 clusterStepMat M(q) rank-1 identity & eigenvalues
    m_step = sp.Matrix(
        [
            [q - inv_q**3, q, q],
            [inv_q, inv_q - inv_q**3, inv_q],
            [inv_q**3, inv_q**3, 0],
        ]
    )
    rk1_diff = m_step + inv_q**3 * sp.eye(3) - sp.Matrix([q, inv_q, inv_q**3]) * sp.Matrix([[1, 1, 1]])
    ok_rk1 = all(sp.simplify(x) == 0 for x in rk1_diff)
    lam = sp.Symbol("lam")
    char_m = sp.Poly(m_step.charpoly(lam).as_expr(), lam)
    expected_char_m = sp.Poly((lam - q2) * (lam + inv_q**3) ** 2, lam)
    ok_spec_m = all(
        sp.simplify(c) == 0 for c in (char_m - expected_char_m).all_coeffs()
    )

    return {
        "all_sympy_plaquette_identities_pass": bool(
            ok_9q_open
            and ok_9q_cyc3
            and ok_9q_tri
            and ok_9q_k3
            and ok_9q_tri_q1
            and ok_12q_open
            and ok_12q_ring
            and ok_12q_k4
            and ok_rk1
            and ok_spec_m
        ),
        "nine_quark_open_R34_R67_ratio": str(ratio_9q_open),
        "nine_quark_cyclic3_R36_R69_ratio": str(ratio_9q_cyc3),
        "nine_quark_closed_triangle_t3": str(sp.factor(ratio_9q_tri)),
        "nine_quark_connected_cumulant_kappa3": str(sp.factor(expected_k3)),
        "twelve_quark_open_R34_R67_R910_ratio": str(ratio_12q_open),
        "twelve_quark_closed_ring_t4": str(sp.factor(ratio_12q_ring)),
        "twelve_quark_connected_cumulant_kappa4": str(sp.factor(expected_k4)),
        "cluster_step_eigenvalues": [str(q2), str(-inv_q**3), str(-inv_q**3)],
    }


# ---------------------------------------------------------------------------
# Part 2: 80-dps Hoefsmit S^{[A,A,A]}_{H_{3A}(q_0)} & 3D Jacobi Variational Battery
# ---------------------------------------------------------------------------
def enumerate_rect_three_syts(a_nuc: int) -> list[SyTableau]:
    n_tot = 3 * a_nuc
    partial: list[tuple[list[int], list[int], list[int]]] = [([], [], [])]
    for val in range(1, n_tot + 1):
        nxt: list[tuple[list[int], list[int], list[int]]] = []
        for r0, r1, r2 in partial:
            if len(r0) < a_nuc:
                nxt.append((r0 + [val], r1, r2))
            if len(r1) < len(r0):
                nxt.append((r0, r1 + [val], r2))
            if len(r2) < len(r1):
                nxt.append((r0, r1, r2 + [val]))
        partial = nxt
    syts = [(tuple(r0), tuple(r1), tuple(r2)) for r0, r1, r2 in partial]
    syts.sort()
    return syts


def factorized_nucleon_syt(a_nuc: int) -> SyTableau:
    return (
        tuple(3 * k + 1 for k in range(a_nuc)),
        tuple(3 * k + 2 for k in range(a_nuc)),
        tuple(3 * k + 3 for k in range(a_nuc)),
    )


def q_bracket_mp(q: mp.mpf, n: int) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


class SparseHoefsmitGenerators:
    """Exact 80-dps real-symmetric Hoefsmit generators R_k(q) (0 <= k < 3A - 1) on S^{[A,A,A]}."""

    def __init__(self, a_nuc: int, q: mp.mpf) -> None:
        self.a_nuc = a_nuc
        self.n_strands = 3 * a_nuc
        self.q = q
        self.q_inv = mp.mpf(1) / q
        self.h = q - self.q_inv
        self.syts = enumerate_rect_three_syts(a_nuc)
        self.dim = len(self.syts)
        self.syt_to_idx = {t: idx for idx, t in enumerate(self.syts)}
        self.fac_idx = self.syt_to_idx[factorized_nucleon_syt(a_nuc)]

        pos_list: list[list[tuple[int, int]]] = []
        for t in self.syts:
            pos = [(0, 0)] * (self.n_strands + 1)
            for r in range(3):
                for c, val in enumerate(t[r]):
                    pos[val] = (r, c)
            pos_list.append(pos)

        self.gen_rows: list[list[list[tuple[int, mp.mpf]]]] = []
        self.inv_gen_rows: list[list[list[tuple[int, mp.mpf]]]] = []
        one = mp.mpf(1)

        for k in range(self.n_strands - 1):
            v1, v2 = k + 1, k + 2
            rows_k: list[list[tuple[int, mp.mpf]]] = [[] for _ in range(self.dim)]
            inv_rows_k: list[list[tuple[int, mp.mpf]]] = [[] for _ in range(self.dim)]
            for i, t in enumerate(self.syts):
                r1, c1 = pos_list[i][v1]
                r2, c2 = pos_list[i][v2]
                if r1 == r2:
                    rows_k[i] = [(i, q)]
                    inv_rows_k[i] = [(i, self.q_inv)]
                elif c1 == c2:
                    rows_k[i] = [(i, -self.q_inv)]
                    inv_rows_k[i] = [(i, -q)]
                else:
                    d_ax = (c2 - r2) - (c1 - r1)
                    abs_d = abs(d_ax)
                    qd = q_bracket_mp(q, abs_d)
                    diag = self.h / (one - q ** (-2 * d_ax))
                    off = mp.sqrt(q_bracket_mp(q, abs_d - 1) * q_bracket_mp(q, abs_d + 1)) / qd
                    grid = [list(row) for row in t]
                    grid[r1][c1] = v2
                    grid[r2][c2] = v1
                    j = self.syt_to_idx[(tuple(grid[0]), tuple(grid[1]), tuple(grid[2]))]
                    rows_k[i] = [(i, diag), (j, off)]
                    inv_rows_k[i] = [(i, diag - self.h), (j, off)]
            self.gen_rows.append(rows_k)
            self.inv_gen_rows.append(inv_rows_k)

        self.gen_rows_fx: list[list[list[tuple[int, int]]]] = [
            [[(j, int(mp.nint(mp.ldexp(val, FX_BITS)))) for j, val in row] for row in rows_k]
            for rows_k in self.gen_rows
        ]
        self.inv_gen_rows_fx: list[list[list[tuple[int, int]]]] = [
            [[(j, int(mp.nint(mp.ldexp(val, FX_BITS)))) for j, val in row] for row in rows_k]
            for rows_k in self.inv_gen_rows
        ]

    def apply_gen(self, k: int, vec: list[mp.mpf], inverse: bool = False) -> list[mp.mpf]:
        rows = self.inv_gen_rows[k] if inverse else self.gen_rows[k]
        zero = mp.mpf(0)
        out = [zero] * self.dim
        for j, vj in enumerate(vec):
            if vj != zero:
                for i, val in rows[j]:
                    out[i] += val * vj
        return out

    def apply_gen_fx(self, k: int, vec_fx: list[int], inverse: bool = False) -> list[int]:
        rows = self.inv_gen_rows_fx[k] if inverse else self.gen_rows_fx[k]
        out = [0] * self.dim
        for j, vj in enumerate(vec_fx):
            if vj:
                for i, val in rows[j]:
                    out[i] += (val * vj + FX_HALF) >> FX_BITS
        return out

    def apply_word(self, word: BraidWord, vec: list[mp.mpf]) -> list[mp.mpf]:
        """Apply `(generator_index, is_inverse)` list right-to-left to `vec`."""
        cur = list(vec)
        for k, inv in reversed(word):
            cur = self.apply_gen(k, cur, inverse=inv)
        return cur

    def apply_word_fx(self, word: BraidWord, vec_fx: list[int]) -> list[int]:
        cur = list(vec_fx)
        for k, inv in reversed(word):
            cur = self.apply_gen_fx(k, cur, inverse=inv)
        return cur

    def apply_sym_word(self, word: BraidWord, vec: list[mp.mpf]) -> list[mp.mpf]:
        """Apply 1/2 * (U(word) + U(word)^T) using exact symmetry R_k^T = R_k."""
        half = mp.mpf(1) / mp.mpf(2)
        u_vec = self.apply_word(word, vec)
        ut_vec = self.apply_word(list(reversed(word)), vec)
        return [half * (u_vec[i] + ut_vec[i]) for i in range(self.dim)]

    def apply_sym_word_fx(self, word: BraidWord, vec_fx: list[int]) -> list[int]:
        u_vec = self.apply_word_fx(word, vec_fx)
        ut_vec = self.apply_word_fx(list(reversed(word)), vec_fx)
        return [(u_vec[i] + ut_vec[i] + 1) >> 1 for i in range(self.dim)]

    def build_dense_from_op(self, op_fn: Callable[[list[mp.mpf]], list[mp.mpf]]) -> list[list[mp.mpf]]:
        zero = mp.mpf(0)
        one = mp.mpf(1)
        cols: list[list[mp.mpf]] = []
        for j in range(self.dim):
            ej = [zero] * self.dim
            ej[j] = one
            cols.append(op_fn(ej))
        return [[cols[j][i] for j in range(self.dim)] for i in range(self.dim)]

    def build_dense_from_fx_op(self, op_fx: Callable[[list[int]], list[int]]) -> list[list[mp.mpf]]:
        cols_fx: list[list[int]] = []
        for j in range(self.dim):
            ej = [0] * self.dim
            ej[j] = FX_ONE
            cols_fx.append(op_fx(ej))
        zero = mp.mpf(0)
        return [
            [
                mp.ldexp(mp.mpf(cols_fx[j][i]), -FX_BITS) if cols_fx[j][i] else zero
                for j in range(self.dim)
            ]
            for i in range(self.dim)
        ]

    def build_dense_from_word(self, word: BraidWord) -> list[list[mp.mpf]]:
        return self.build_dense_from_fx_op(lambda v: self.apply_word_fx(word, v))

    def verify_relations_and_symmetry_residual(self) -> mp.mpf:
        max_res = mp.mpf(0)
        probe = [mp.mpf(1) / mp.mpf(i + 2) for i in range(self.dim)]
        for k in range(self.n_strands - 1):
            rk = self.apply_gen(k, probe)
            rk2 = self.apply_gen(k, rk)
            for i in range(self.dim):
                max_res = max(max_res, abs(rk2[i] - self.h * rk[i] - probe[i]))
            row_map = {
                (i, j): val for i, entries in enumerate(self.gen_rows[k]) for j, val in entries
            }
            for (i, j), val in row_map.items():
                max_res = max(max_res, abs(val - row_map.get((j, i), mp.mpf(0))))
        for k in range(self.n_strands - 2):
            lhs = self.apply_word([(k, False), (k + 1, False), (k, False)], probe)
            rhs = self.apply_word([(k + 1, False), (k, False), (k + 1, False)], probe)
            for i in range(self.dim):
                max_res = max(max_res, abs(lhs[i] - rhs[i]))
        return max_res


def transport_crossing_word(s_strand: int, t_strand: int) -> BraidWord:
    """Corrected positive-braid transport word U_{p,q}(q_0) for 0 <= s != t < 3A:
    With p = min(s, t), q = max(s, t):
      U_{p,q} = (R_p^{-1} ... R_{q-2}^{-1}) R_{q-1} (R_{q-2} ... R_p)."""
    if s_strand == t_strand:
        raise ValueError("transport_crossing_word requires distinct strands")
    p_idx = min(s_strand, t_strand)
    q_idx = max(s_strand, t_strand)
    left_undo = [(g_idx, True) for g_idx in range(p_idx, q_idx - 1)]
    right_fwd = [(g_idx, False) for g_idx in range(q_idx - 2, p_idx - 1, -1)]
    return left_undo + [(q_idx - 1, False)] + right_fwd


def legacy_w4_reversed_pair_word(a_idx: int, b_idx: int) -> BraidWord:
    """Verbatim #9221 (`w4_colour_reconn_stokes_aomega_probe.py` lines 772-776) pair word for M0."""
    s_strand = 3 * a_idx + 2
    target_gen = 3 * b_idx - 1
    prefix = [(g_idx, False) for g_idx in range(target_gen - 1, s_strand - 1, -1)]
    suffix = [(g_idx, True) for g_idx in range(s_strand, target_gen)]
    return prefix + [(target_gen, False)] + suffix


def to_srows(mat: list[list[mp.mpf]]) -> list[list[tuple[int, mp.mpf]]]:
    zero = mp.mpf(0)
    return [[(j, val) for j, val in enumerate(row) if val != zero] for row in mat]


def matvec_srows(srows: list[list[tuple[int, mp.mpf]]], vec: list[mp.mpf]) -> list[mp.mpf]:
    zero = mp.mpf(0)
    out = [zero] * len(srows)
    for i, entries in enumerate(srows):
        if entries:
            acc = zero
            for j, val in entries:
                acc += val * vec[j]
            out[i] = acc
    return out


def matvec_srows_colskip(srows: list[list[tuple[int, mp.mpf]]], vec: list[mp.mpf]) -> list[mp.mpf]:
    """Symmetric sparse matvec skipping zero entries of `vec` (when `srows` is symmetric)."""
    zero = mp.mpf(0)
    out = [zero] * len(srows)
    for j, vj in enumerate(vec):
        if vj != zero:
            for i, val in srows[j]:
                out[i] += val * vj
    return out


def matvec_dense(mat: list[list[mp.mpf]], vec: list[mp.mpf]) -> list[mp.mpf]:
    zero = mp.mpf(0)
    out = [zero] * len(mat)
    for i, row in enumerate(mat):
        acc = zero
        for j, val in enumerate(row):
            if val != zero:
                acc += val * vec[j]
        out[i] = acc
    return out


def dot_mp(u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
    acc = mp.mpf(0)
    for x, y in zip(u, v):
        acc += x * y
    return acc


def sym_centered_from_word(hoef: SparseHoefsmitGenerators, word: BraidWord) -> list[list[mp.mpf]]:
    """Build 1/2 * (1/2 * (U + U^T) - <T_fac | 1/2 * (U + U^T) | T_fac> I) via sparse word action."""
    quarter = mp.mpf(1) / mp.mpf(4)
    half = mp.mpf(1) / mp.mpf(2)
    u_mat = hoef.build_dense_from_word(word)
    fac_diag = u_mat[hoef.fac_idx][hoef.fac_idx]
    dim = hoef.dim
    out = [[quarter * (u_mat[i][j] + u_mat[j][i]) for j in range(dim)] for i in range(dim)]
    for i in range(dim):
        out[i][i] -= half * fac_diag
    return out


def add_scaled_inplace(
    acc: list[list[mp.mpf]], mat: list[list[mp.mpf]], scale: mp.mpf
) -> None:
    dim = len(acc)
    for i in range(dim):
        row_a = acc[i]
        row_m = mat[i]
        for j in range(dim):
            row_a[j] += scale * row_m[j]


def cg_solve_spd(
    mat: list[list[mp.mpf]], rhs: list[mp.mpf], tol: mp.mpf, max_iter: int = 300
) -> tuple[list[mp.mpf], mp.mpf]:
    n = len(rhs)
    zero = mp.mpf(0)
    srows = to_srows(mat)
    x = [zero] * n
    r = list(rhs)
    p = list(r)
    rs_old = dot_mp(r, r)
    if rs_old == zero:
        return x, zero
    for _ in range(max_iter):
        ap = matvec_srows(srows, p)
        pap = dot_mp(p, ap)
        alpha = rs_old / pap
        for i in range(n):
            x[i] += alpha * p[i]
            r[i] -= alpha * ap[i]
        rs_new = dot_mp(r, r)
        if mp.sqrt(rs_new) < tol:
            break
        beta = rs_new / rs_old
        for i in range(n):
            p[i] = r[i] + beta * p[i]
        rs_old = rs_new
    ax = matvec_srows(srows, x)
    inf_res = max(abs(ax[i] - rhs[i]) for i in range(n))
    return x, inf_res


def tridiag_solve_gepp(
    dl_in: list[mp.mpf], d_in: list[mp.mpf], du_in: list[mp.mpf], rhs_in: list[mp.mpf]
) -> list[mp.mpf]:
    """Exact O(k) tridiagonal linear solver with partial pivoting (LAPACK `dgtsv` algorithm)."""
    k = len(d_in)
    zero = mp.mpf(0)
    tiny = mp.mpf("1e-150")
    dl = list(dl_in)
    d = list(d_in)
    du = list(du_in)
    du2 = [zero] * max(0, k - 2)
    rhs = list(rhs_in)

    for i in range(k - 1):
        if abs(d[i]) >= abs(dl[i]):
            piv = d[i] if d[i] != zero else tiny
            d[i] = piv
            fact = dl[i] / piv
            d[i + 1] -= fact * du[i]
            rhs[i + 1] -= fact * rhs[i]
        else:
            # Swap row i and row i + 1
            piv = dl[i]
            fact = d[i] / piv
            d[i] = piv
            temp = d[i + 1]
            d[i + 1] = du[i] - fact * temp
            du[i] = temp
            if i + 1 < k - 1:
                du2[i] = du[i + 1]
                du[i + 1] = -fact * du[i + 1]
            r_tmp = rhs[i]
            rhs[i] = rhs[i + 1]
            rhs[i + 1] = r_tmp - fact * rhs[i + 1]

    if d[k - 1] == zero:
        d[k - 1] = tiny
    x = [zero] * k
    x[k - 1] = rhs[k - 1] / d[k - 1]
    if k >= 2:
        x[k - 2] = (rhs[k - 2] - du[k - 2] * x[k - 1]) / d[k - 2]
    for i in range(k - 3, -1, -1):
        x[i] = (rhs[i] - du[i] * x[i + 1] - du2[i] * x[i + 2]) / d[i]
    return x


def tridiag_lowest_eigenpair_sturm(
    alphas: list[mp.mpf], betas: list[mp.mpf]
) -> tuple[mp.mpf, list[mp.mpf]]:
    """Exact 80-dps O(k) lowest eigenpair of an unreduced symmetric tridiagonal matrix via
    Sturm-sequence bisection (280 steps) + 3-step partial-pivoted shifted inverse iteration."""
    k_dim = len(alphas)
    zero = mp.mpf(0)
    one = mp.mpf(1)
    if k_dim == 1:
        return alphas[0], [one]

    zero = mp.mpf(0)
    half = one / mp.mpf(2)
    tiny_piv = mp.mpf("1e-150")
    b_sq = [b * b for b in betas]

    lo = min(
        alphas[i]
        - (abs(betas[i - 1]) if i > 0 else zero)
        - (abs(betas[i]) if i < k_dim - 1 else zero)
        for i in range(k_dim)
    ) - one
    hi = min(alphas) + mp.mpf("1e-65")

    def count_lt(mu: mp.mpf) -> int:
        cnt = 0
        d_val = alphas[0] - mu
        if d_val <= zero:
            cnt += 1
            if d_val == zero:
                d_val = -tiny_piv
        for i in range(1, k_dim):
            d_val = (alphas[i] - mu) - b_sq[i - 1] / d_val
            if d_val <= zero:
                cnt += 1
                if d_val == zero:
                    d_val = -tiny_piv
        return cnt

    for _ in range(280):
        mid = half * (lo + hi)
        if count_lt(mid) >= 1:
            hi = mid
        else:
            lo = mid
    lam_min = half * (lo + hi)

    shift = lam_min - mp.mpf("1e-77")
    d_shifted = [a - shift for a in alphas]
    u_vec = [one / mp.mpf(i + 1) for i in range(k_dim)]
    nrm = mp.sqrt(dot_mp(u_vec, u_vec))
    u_vec = [x / nrm for x in u_vec]
    for _ in range(3):
        u_vec = tridiag_solve_gepp(betas, d_shifted, betas, u_vec)
        nrm = mp.sqrt(dot_mp(u_vec, u_vec))
        u_vec = [x / nrm for x in u_vec]

    # Rayleigh polish on T
    tu0 = alphas[0] * u_vec[0] + betas[0] * u_vec[1]
    rq = u_vec[0] * tu0
    for i in range(1, k_dim - 1):
        rq += u_vec[i] * (betas[i - 1] * u_vec[i - 1] + alphas[i] * u_vec[i] + betas[i] * u_vec[i + 1])
    rq += u_vec[k_dim - 1] * (betas[k_dim - 2] * u_vec[k_dim - 2] + alphas[k_dim - 1] * u_vec[k_dim - 1])
    return rq, u_vec


def lowest_eigenpair_sym(
    mat: list[list[mp.mpf]],
    start_idx: int,
    perturbed_start: bool = True,
    force_perturbed: bool = False,
) -> tuple[mp.mpf, list[mp.mpf], mp.mpf]:
    """Exact 80-dps lowest eigenpair of real-symmetric `mat`, certified by full L_inf residual."""
    n = len(mat)
    if n <= 10:
        m_mp = mp.matrix(mat)
        evals, evecs = mp.eigsy(m_mp)
        min_idx = min(range(n), key=lambda idx: evals[idx])
        lam = evals[min_idx]
        vec = [evecs[i, min_idx] for i in range(n)]
        mv = matvec_dense(mat, vec)
        res = max(abs(mv[i] - lam * vec[i]) for i in range(n))
        return lam, vec, res

    zero = mp.mpf(0)
    srows = to_srows(mat)
    mat_fx = [[int(mp.nint(mp.ldexp(val, FX_BITS))) for val in row] for row in mat]
    use_pert = force_perturbed or (perturbed_start and n <= 60)
    if use_pert:
        v0 = [mp.mpf(1) / mp.mpf(1000 * (i + 3)) for i in range(n)]
        v0[start_idx] = mp.mpf(1)
        nrm0 = mp.sqrt(dot_mp(v0, v0))
        v0 = [x / nrm0 for x in v0]
    else:
        v0 = [zero] * n
        v0[start_idx] = mp.mpf(1)

    v0_fx = [int(mp.nint(mp.ldexp(x, FX_BITS))) for x in v0]
    basis_fx: list[list[int]] = [v0_fx]
    m_steps = min(220, n)
    alphas: list[mp.mpf] = []
    betas: list[mp.mpf] = []
    betas_fx: list[int] = []
    check_steps = {25, 45, 75, 110, 155, 190, m_steps}
    starmap_fn = itertools.starmap
    mul_fn = operator.mul

    def fx_dot(u_fx: list[int], w_fx: list[int]) -> int:
        return (sum(starmap_fn(mul_fn, zip(u_fx, w_fx))) + FX_HALF) >> FX_BITS

    def extract_ritz() -> tuple[mp.mpf, list[mp.mpf], mp.mpf]:
        k_dim = len(alphas)
        _, t_vec = tridiag_lowest_eigenpair_sturm(alphas, betas[: k_dim - 1])
        t_fx = [int(mp.nint(mp.ldexp(c, FX_BITS))) for c in t_vec]
        vec_fx = [0] * n
        for s_idx in range(k_dim):
            cf = t_fx[s_idx]
            if cf:
                bs = basis_fx[s_idx]
                for i in range(n):
                    vec_fx[i] += (cf * bs[i] + FX_HALF) >> FX_BITS
        vec_cur = [mp.ldexp(mp.mpf(x), -FX_BITS) for x in vec_fx]
        vn = mp.sqrt(dot_mp(vec_cur, vec_cur))
        vec_cur = [x / vn for x in vec_cur]
        # Exact Rayleigh quotient and residual certified in pure 80-dps mp.mpf:
        mv = matvec_srows(srows, vec_cur)
        lam_cur = dot_mp(vec_cur, mv)
        res_cur = max(abs(mv[i] - lam_cur * vec_cur[i]) for i in range(n))
        return lam_cur, vec_cur, res_cur

    for step in range(m_steps):
        cur_fx = basis_fx[step]
        w_fx = [(sum(starmap_fn(mul_fn, zip(row_fx, cur_fx))) + FX_HALF) >> FX_BITS for row_fx in mat_fx]
        if step > 0:
            b_prev_fx = betas_fx[step - 1]
            prev_fx = basis_fx[step - 1]
            for i in range(n):
                w_fx[i] -= (b_prev_fx * prev_fx[i] + FX_HALF) >> FX_BITS
        a_fx = fx_dot(cur_fx, w_fx)
        alphas.append(mp.ldexp(mp.mpf(a_fx), -FX_BITS))
        for i in range(n):
            w_fx[i] -= (a_fx * cur_fx[i] + FX_HALF) >> FX_BITS
        for _ in range(2):
            for qv_fx in basis_fx:
                ov_fx = fx_dot(qv_fx, w_fx)
                if ov_fx:
                    for i in range(n):
                        w_fx[i] -= (ov_fx * qv_fx[i] + FX_HALF) >> FX_BITS
        b_sq_fx = sum(starmap_fn(mul_fn, zip(w_fx, w_fx)))
        b_next = mp.ldexp(mp.sqrt(mp.mpf(b_sq_fx)), -FX_BITS)
        if b_next < mp.mpf("1e-78"):
            return extract_ritz()
        if step + 1 in check_steps:
            lam_c, vec_c, res_c = extract_ritz()
            if res_c < mp.mpf("1e-78") or step + 1 == m_steps:
                return lam_c, vec_c, res_c
        if step + 1 < m_steps:
            b_fx = int(mp.nint(mp.ldexp(b_next, FX_BITS)))
            inv_b = mp.mpf(1) / b_next
            inv_b_fx = int(mp.nint(mp.ldexp(inv_b, FX_BITS)))
            betas.append(b_next)
            betas_fx.append(b_fx)
            basis_fx.append([(x * inv_b_fx + FX_HALF) >> FX_BITS for x in w_fx])

    return extract_ritz()


def safeguarded_root_1d(
    fn: Callable[[mp.mpf], mp.mpf],
    lo_init: mp.mpf,
    hi_init: mp.mpf,
    tol_x: mp.mpf,
    tol_f: mp.mpf,
    max_iter: int = 80,
) -> tuple[mp.mpf, mp.mpf]:
    """80-dps Dekker-Brent secant-bisection root finder on [lo_init, hi_init] with fn(lo) <= 0 <= fn(hi).
    Superlinear order-1.618 convergence (~12-15 evaluations to 70+ digits) with guaranteed bracket contraction."""
    a = lo_init
    b = hi_init
    fa = fn(a)
    fb = fn(b)
    zero = mp.mpf(0)
    half = mp.mpf(1) / mp.mpf(2)
    if abs(fa) <= tol_f:
        return a, fa
    if abs(fb) <= tol_f:
        return b, fb
    if not (fa < zero < fb):
        raise ValueError("safeguarded_root_1d requires fn(lo) < 0 < fn(hi)")

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c, fc = a, fa
    prev_step = abs(b - a)

    for _ in range(max_iter):
        width = abs(a - b)
        if abs(fb) <= tol_f or width <= tol_x:
            return b, fb

        mid = half * (a + b)
        denom = fb - fc
        x_next = mid
        if denom != zero:
            cand = b - fb * (b - c) / denom
            lo_ab = a if a < b else b
            hi_ab = b if a < b else a
            if lo_ab < cand < hi_ab and abs(cand - b) <= half * prev_step:
                x_next = cand

        step_taken = abs(x_next - b)
        # Force a bisection step whenever steps shrink too slowly relative to bracket width
        if step_taken < tol_x:
            x_next = b + (tol_x * half if a > b else -tol_x * half)
            if not ((a < x_next < b) or (b < x_next < a)):
                x_next = mid

        f_next = fn(x_next)
        prev_step = abs(b - c) if x_next != mid else width
        c, fc = b, fb

        if (f_next > zero and fb < zero) or (f_next < zero and fb > zero):
            a, fa = b, fb
        b, fb = x_next, f_next

        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa

    return b, fb


def build_gap1b_operators(
    hoef: SparseHoefsmitGenerators,
) -> tuple[list[list[mp.mpf]], dict[str, list[list[mp.mpf]]], dict[str, mp.mpf]]:
    """Construct H_G2^{(A)}(q_0) and all pre-registered microscopic operators M0..M4b on S^{[A,A,A]}."""
    a_nuc = hoef.a_nuc
    dim = hoef.dim
    q = hoef.q
    h = hoef.h
    zero = mp.mpf(0)
    zero = mp.mpf(0)
    one = mp.mpf(1)
    half = one / mp.mpf(2)
    q_m6 = q ** (-6)
    delta8 = (one - q_m6) / h
    delta10 = (q**6 - q_m6) / h

    # Intra-cluster Casimir gap operators G_k and total H_G2 = sum_k G_k
    ft_words: list[BraidWord] = []
    for k in range(a_nuc):
        g0, g1 = 3 * k, 3 * k + 1
        ft_words.append(
            [(g0, False), (g1, False), (g0, False), (g0, False), (g1, False), (g0, False)]
        )

    def apply_gk(k: int, vec: list[mp.mpf]) -> list[mp.mpf]:
        ft_v = hoef.apply_sym_word(ft_words[k], vec)
        return [(ft_v[i] - q_m6 * vec[i]) / h for i in range(dim)]

    def apply_proj_singlet(k: int, vec: list[mp.mpf]) -> list[mp.mpf]:
        # Pi_k^1 = (I - G_k / delta8)(I - G_k / delta10)
        gk_v = apply_gk(k, vec)
        u = [vec[i] - gk_v[i] / delta10 for i in range(dim)]
        gk_u = apply_gk(k, u)
        return [u[i] - gk_u[i] / delta8 for i in range(dim)]

    def apply_proj_exc(k: int, vec: list[mp.mpf]) -> list[mp.mpf]:
        p1 = apply_proj_singlet(k, vec)
        return [vec[i] - p1[i] for i in range(dim)]

    # Precompute sparse row representations of Pi_k^1 and Pi_k^{exc} (each <= 6 nonzeros per row)
    proj_sing_rows: list[list[list[tuple[int, mp.mpf]]]] = []
    proj_exc_rows: list[list[list[tuple[int, mp.mpf]]]] = []
    sparse_cutoff = mp.mpf("1e-76")
    for k in range(a_nuc):
        s_mat = hoef.build_dense_from_op(lambda v, kk=k: apply_proj_singlet(kk, v))
        s_rows: list[list[tuple[int, mp.mpf]]] = []
        e_rows: list[list[tuple[int, mp.mpf]]] = []
        for i in range(dim):
            sr = [(j, s_mat[i][j]) for j in range(dim) if abs(s_mat[i][j]) > sparse_cutoff]
            er: list[tuple[int, mp.mpf]] = []
            for j in range(dim):
                ev = (one if i == j else zero) - s_mat[i][j]
                if abs(ev) > sparse_cutoff:
                    er.append((j, ev))
            s_rows.append(sr)
            e_rows.append(er)
        proj_sing_rows.append(s_rows)
        proj_exc_rows.append(e_rows)

    def apply_cluster_projector_vec(
        exc_clusters: set[int], vec: list[mp.mpf]
    ) -> list[mp.mpf]:
        cur = list(vec)
        for cl in range(a_nuc):
            srows = proj_exc_rows[cl] if (cl in exc_clusters) else proj_sing_rows[cl]
            cur = matvec_srows_colskip(srows, cur)
        return cur

    def apply_left_srows_mat(
        srows: list[list[tuple[int, mp.mpf]]], mat: list[list[mp.mpf]]
    ) -> list[list[mp.mpf]]:
        """Compute S * mat where each row of S has <= 3 nonzeros."""
        out: list[list[mp.mpf]] = []
        for entries in srows:
            if not entries:
                out.append([zero] * dim)
            elif len(entries) == 1:
                idx0, w0 = entries[0]
                row0 = mat[idx0]
                out.append([w0 * x for x in row0])
            else:
                acc_row = [zero] * dim
                for idx_k, wk in entries:
                    if wk != zero:
                        rk = mat[idx_k]
                        for j in range(dim):
                            vj = rk[j]
                            if vj != zero:
                                acc_row[j] += wk * vj
                out.append(acc_row)
        return out

    def build_cumulant_projected_mat(
        c_mat: list[list[mp.mpf]], exc_clusters: set[int]
    ) -> list[list[mp.mpf]]:
        """Compute P C Pi_0 + Pi_0 C P + P C P by factored ultra-sparse cluster multiplication:
        P C P = P * (P * (P * C)^T)^T since C and each cluster projector factor are symmetric."""
        fac = hoef.fac_idx
        p_cfac = apply_cluster_projector_vec(exc_clusters, [c_mat[k][fac] for k in range(dim)])

        # Step 1: M1 = P * C
        cur_m = c_mat
        for cl in range(a_nuc):
            srows = proj_exc_rows[cl] if (cl in exc_clusters) else proj_sing_rows[cl]
            cur_m = apply_left_srows_mat(srows, cur_m)

        # Step 2: M2 = P * (M1^T) = (M1 * P)^T = P * C * P (symmetric!)
        cur_mt = [[cur_m[j][i] for j in range(dim)] for i in range(dim)]
        for cl in range(a_nuc):
            srows = proj_exc_rows[cl] if (cl in exc_clusters) else proj_sing_rows[cl]
            cur_mt = apply_left_srows_mat(srows, cur_mt)

        out = [[half * (cur_mt[i][j] + cur_mt[j][i]) for j in range(dim)] for i in range(dim)]
        for i in range(dim):
            out[i][fac] += p_cfac[i]
            out[fac][i] += p_cfac[i]
        return out

    h_g2 = [[zero] * dim for _ in range(dim)]
    for k in range(a_nuc):
        gk_mat = hoef.build_dense_from_op(lambda v, kk=k: apply_gk(kk, v))
        add_scaled_inplace(h_g2, gk_mat, one)

    # M0: Verbatim #9221 V2_allpairs_fierz (reversed transport on non-adjacent edges)
    v_m0 = [[zero] * dim for _ in range(dim)]
    for a_idx in range(a_nuc):
        for b_idx in range(a_idx + 1, a_nuc):
            w_leg = legacy_w4_reversed_pair_word(a_idx, b_idx)
            add_scaled_inplace(v_m0, sym_centered_from_word(hoef, w_leg), one)

    # M1: Corrected positive-braid transport 2-body K_A Majorana-Fierz sum on boundary strands (3a+2, 3b)
    v_m1 = [[zero] * dim for _ in range(dim)]
    for a_idx in range(a_nuc):
        for b_idx in range(a_idx + 1, a_nuc):
            w_bnd = transport_crossing_word(3 * a_idx + 2, 3 * b_idx)
            add_scaled_inplace(v_m1, sym_centered_from_word(hoef, w_bnd), one)

    # M2: Canonical Tait 3-matching strand assignment phi(a, b) (12 quarks <-> 12 half-edges on K_4)
    v_m2 = [[zero] * dim for _ in range(dim)]
    tait_fierz_fx_ops: dict[tuple[int, int], Callable[[list[int]], list[int]]] = {}
    for a_idx in range(a_nuc):
        for b_idx in range(a_idx + 1, a_nuc):
            s_left, s_right = TAIT_EDGE_STRANDS[(a_idx, b_idx)]
            w_tait = transport_crossing_word(s_left, s_right)
            f_mat = sym_centered_from_word(hoef, w_tait)
            add_scaled_inplace(v_m2, f_mat, one)
            u_fac_col_fx = hoef.apply_word_fx(
                w_tait, [FX_ONE if i == hoef.fac_idx else 0 for i in range(dim)]
            )
            fac_d_fx = u_fac_col_fx[hoef.fac_idx]

            def make_fierz_fx_op(
                w_loc: BraidWord = w_tait, fd_fx: int = fac_d_fx
            ) -> Callable[[list[int]], list[int]]:
                def _op_fx(v_fx: list[int]) -> list[int]:
                    sv_fx = hoef.apply_sym_word_fx(w_loc, v_fx)
                    return [
                        (sv_fx[i] - ((fd_fx * v_fx[i] + FX_HALF) >> FX_BITS) + 1) >> 1
                        for i in range(dim)
                    ]

                return _op_fx

            tait_fierz_fx_ops[(a_idx, b_idx)] = make_fierz_fx_op()
            tait_fierz_fx_ops[(b_idx, a_idx)] = tait_fierz_fx_ops[(a_idx, b_idx)]

    # Triangular 3-interface plaquette holonomies P_triangle across all C(A, 3) faces
    plaq_3_sum = [[zero] * dim for _ in range(dim)]
    fierz_ring_3_sum = [[zero] * dim for _ in range(dim)]
    cyc_quark_3_raw = [[zero] * dim for _ in range(dim)]
    cyc_quark_3_cum = [[zero] * dim for _ in range(dim)]

    diagnostics: dict[str, mp.mpf] = {
        "delta8_single_cluster": delta8,
        "delta10_single_cluster": delta10,
    }

    for a_idx, b_idx, c_idx in itertools.combinations(range(a_nuc), 3):
        w_tri = (
            transport_crossing_word(3 * a_idx + 2, 3 * b_idx)
            + transport_crossing_word(3 * b_idx + 2, 3 * c_idx)
            + transport_crossing_word(3 * a_idx, 3 * c_idx + 2)
        )
        p_tri = sym_centered_from_word(hoef, w_tri)
        add_scaled_inplace(plaq_3_sum, p_tri, one)

        fab = tait_fierz_fx_ops[(a_idx, b_idx)]
        fbc = tait_fierz_fx_ops[(b_idx, c_idx)]
        fca = tait_fierz_fx_ops[(c_idx, a_idx)]
        f3_prod = hoef.build_dense_from_fx_op(lambda v, f1=fab, f2=fbc, f3=fca: f1(f2(f3(v))))
        f3_diag = f3_prod[hoef.fac_idx][hoef.fac_idx]
        f3_raw = [[half * (f3_prod[i][j] + f3_prod[j][i]) for j in range(dim)] for i in range(dim)]
        for i in range(dim):
            f3_raw[i][i] -= f3_diag
        add_scaled_inplace(fierz_ring_3_sum, f3_raw, one)

        w_cyc3 = transport_crossing_word(
            3 * a_idx + 2, 3 * b_idx + 2
        ) + transport_crossing_word(3 * b_idx + 2, 3 * c_idx + 2)
        c3_mat = sym_centered_from_word(hoef, w_cyc3)
        add_scaled_inplace(cyc_quark_3_raw, c3_mat, one)

        c3_cum = build_cumulant_projected_mat(c3_mat, {a_idx, b_idx, c_idx})
        add_scaled_inplace(cyc_quark_3_cum, c3_cum, one)

        if a_nuc == 3 and (a_idx, b_idx, c_idx) == (0, 1, 2):
            p_tri_3exc = apply_cluster_projector_vec(
                {0, 1, 2}, [p_tri[k][hoef.fac_idx] for k in range(dim)]
            )
            c3_3exc = apply_cluster_projector_vec(
                {0, 1, 2}, [c3_mat[k][hoef.fac_idx] for k in range(dim)]
            )
            diagnostics["v3_plaq_3cluster_norm_sq"] = dot_mp(p_tri_3exc, p_tri_3exc)
            diagnostics["v3_cyc_3cluster_norm_sq"] = dot_mp(c3_3exc, c3_3exc)

    # Tetrahedral 4-interface Hamiltonian 4-cycles across c_4(A) in {0, 0, 3}
    plaq_4_sum = [[zero] * dim for _ in range(dim)]
    fierz_ring_4_sum = [[zero] * dim for _ in range(dim)]
    cyc_quark_4_raw = [[zero] * dim for _ in range(dim)]
    cyc_quark_4_cum = [[zero] * dim for _ in range(dim)]

    if a_nuc == 4:
        for cyc_idx, (v0, v1, v2, v3) in enumerate(K4_UNORIENTED_4CYCLES):
            w_ring4 = (
                transport_crossing_word(3 * v0 + 2, 3 * v1)
                + transport_crossing_word(3 * v1 + 2, 3 * v2)
                + transport_crossing_word(3 * v2 + 2, 3 * v3)
                + transport_crossing_word(3 * v3 + 2, 3 * v0)
            )
            p_ring4 = sym_centered_from_word(hoef, w_ring4)
            add_scaled_inplace(plaq_4_sum, p_ring4, one)

            f01 = tait_fierz_fx_ops[(v0, v1)]
            f12 = tait_fierz_fx_ops[(v1, v2)]
            f23 = tait_fierz_fx_ops[(v2, v3)]
            f30 = tait_fierz_fx_ops[(v3, v0)]
            f4_prod = hoef.build_dense_from_fx_op(
                lambda v, g1=f01, g2=f12, g3=f23, g4=f30: g1(g2(g3(g4(v))))
            )
            f4_diag = f4_prod[hoef.fac_idx][hoef.fac_idx]
            f4_raw = [[half * (f4_prod[i][j] + f4_prod[j][i]) for j in range(dim)] for i in range(dim)]
            for i in range(dim):
                f4_raw[i][i] -= f4_diag
            add_scaled_inplace(fierz_ring_4_sum, f4_raw, one)

            w_cyc4 = (
                transport_crossing_word(3 * v0 + 2, 3 * v1 + 2)
                + transport_crossing_word(3 * v1 + 2, 3 * v2 + 2)
                + transport_crossing_word(3 * v2 + 2, 3 * v3 + 2)
            )
            c4_mat = sym_centered_from_word(hoef, w_cyc4)
            add_scaled_inplace(cyc_quark_4_raw, c4_mat, one)

            if cyc_idx == 0:
                p_ring4_4exc = apply_cluster_projector_vec(
                    {0, 1, 2, 3}, [p_ring4[k][hoef.fac_idx] for k in range(dim)]
                )
                c4_4exc = apply_cluster_projector_vec(
                    {0, 1, 2, 3}, [c4_mat[k][hoef.fac_idx] for k in range(dim)]
                )
                diagnostics["v4_plaq_4cluster_norm_sq"] = dot_mp(p_ring4_4exc, p_ring4_4exc)
                diagnostics["v4_cyc_4cluster_norm_sq"] = dot_mp(c4_4exc, c4_4exc)

        # Single factored projection of the summed 4-cycles onto {0, 1, 2, 3} all-excited subspace:
        cyc_quark_4_cum = build_cumulant_projected_mat(cyc_quark_4_raw, {0, 1, 2, 3})

    def combine_mats(
        base: list[list[mp.mpf]],
        m3: list[list[mp.mpf]],
        m4: list[list[mp.mpf]],
        sgn: mp.mpf,
    ) -> list[list[mp.mpf]]:
        return [
            [base[i][j] + sgn * (m3[i][j] + m4[i][j]) for j in range(dim)]
            for i in range(dim)
        ]

    v_models = {
        "M0_w4_v2_baseline": v_m0,
        "M1_kA_2body_boundary": v_m1,
        "M2_kA_2body_tait_matched": v_m2,
        "M3a_kA_plaquette_pos": combine_mats(v_m2, plaq_3_sum, plaq_4_sum, one),
        "M3a_kA_plaquette_neg": combine_mats(v_m2, plaq_3_sum, plaq_4_sum, -one),
        "M3a_bnd_plaquette_pos": combine_mats(v_m1, plaq_3_sum, plaq_4_sum, one),
        "M3a_bnd_plaquette_neg": combine_mats(v_m1, plaq_3_sum, plaq_4_sum, -one),
        "M3b_kA_connected_fierz_pos": combine_mats(v_m2, fierz_ring_3_sum, fierz_ring_4_sum, one),
        "M3b_kA_connected_fierz_neg": combine_mats(v_m2, fierz_ring_3_sum, fierz_ring_4_sum, -one),
        "M4a_kA_cyclic_quark_raw_pos": combine_mats(v_m2, cyc_quark_3_raw, cyc_quark_4_raw, one),
        "M4a_kA_cyclic_quark_raw_neg": combine_mats(v_m2, cyc_quark_3_raw, cyc_quark_4_raw, -one),
        "M4b_kA_cyclic_quark_cumulant_pos": combine_mats(v_m2, cyc_quark_3_cum, cyc_quark_4_cum, one),
        "M4b_kA_cyclic_quark_cumulant_neg": combine_mats(v_m2, cyc_quark_3_cum, cyc_quark_4_cum, -one),
    }

    return h_g2, v_models, diagnostics


def evaluate_static_and_analytic_models(
    q0: mp.mpf,
    e0_mev: mp.mpf,
    eosc_mev: mp.mpf,
    b_ame: dict[str, mp.mpf],
) -> tuple[dict, dict[int, SparseHoefsmitGenerators], dict[int, list[list[mp.mpf]]], dict[int, dict[str, list[list[mp.mpf]]]]]:
    """Evaluate M0..M5 at 80 dps across A = 2, 3, 4 and return operators for §3b J_var battery."""
    hoef_by_a: dict[int, SparseHoefsmitGenerators] = {}
    h_g2_by_a: dict[int, list[list[mp.mpf]]] = {}
    v_by_a: dict[int, dict[str, list[list[mp.mpf]]]] = {}
    diag_by_a: dict[int, dict[str, mp.mpf]] = {}
    max_hecke_res = mp.mpf(0)

    for a_nuc in (2, 3, 4):
        hoef = SparseHoefsmitGenerators(a_nuc, q0)
        max_hecke_res = max(max_hecke_res, hoef.verify_relations_and_symmetry_residual())
        h_g2, v_models, diags = build_gap1b_operators(hoef)
        hoef_by_a[a_nuc] = hoef
        h_g2_by_a[a_nuc] = h_g2
        v_by_a[a_nuc] = v_models
        diag_by_a[a_nuc] = diags

    model_names = list(v_by_a[2].keys())
    models_out: dict[str, dict] = {}
    a2_b_mev_by_model: dict[str, mp.mpf] = {}
    max_cg_res = mp.mpf(0)
    max_eig_res = mp.mpf(0)

    for m_name in model_names:
        per_a: dict[str, dict] = {}
        shifts_bh2: dict[int, mp.mpf] = {}
        shifts_exact: dict[int, mp.mpf] = {}

        for a_nuc in (2, 3, 4):
            hoef = hoef_by_a[a_nuc]
            dim = hoef.dim
            fac = hoef.fac_idx
            hid_indices = [i for i in range(dim) if i != fac]
            g_mat = h_g2_by_a[a_nuc]
            v_mat = v_by_a[a_nuc][m_name]

            h0_fac_norm = max(abs(g_mat[i][fac]) for i in range(dim))
            max_cg_res = max(max_cg_res, h0_fac_norm)

            h_hid = [[g_mat[i][j] for j in hid_indices] for i in hid_indices]
            b_vec = [v_mat[i][fac] for i in hid_indices]
            v_leak_sq = dot_mp(b_vec, b_vec)

            sol_hid, cg_res = cg_solve_spd(h_hid, b_vec, mp.mpf("1e-76"))
            max_cg_res = max(max_cg_res, cg_res)
            delta_bh2 = -dot_mp(b_vec, sol_hid)

            h_tot = [[g_mat[i][j] + v_mat[i][j] for j in range(dim)] for i in range(dim)]
            e_ground, psi_ground, eig_res = lowest_eigenpair_sym(h_tot, fac, perturbed_start=True)
            max_eig_res = max(max_eig_res, eig_res)
            if a_nuc == 4 and m_name == "M1_kA_2body_boundary":
                e_glob, _, eig_glob = lowest_eigenpair_sym(
                    h_tot, fac, perturbed_start=True, force_perturbed=True
                )
                max_eig_res = max(max_eig_res, eig_glob, abs(e_glob - e_ground))

            p_hid_prob = mp.mpf(1) - (psi_ground[fac] ** 2)
            shifts_bh2[a_nuc] = abs(delta_bh2)
            shifts_exact[a_nuc] = abs(e_ground)

            per_a[f"A={a_nuc}"] = {
                "dim_singlet": dim,
                "v_offdiag_norm_sq": fmt(v_leak_sq, dps=OUT_DPS),
                "delta_E_BH2_dimless": fmt(delta_bh2, dps=OUT_DPS),
                "E_ground_exact_dimless": fmt(e_ground, dps=OUT_DPS),
                "hidden_colour_admixture_prob": fmt(p_hid_prob, dps=OUT_DPS),
                "bind_BH2_in_Eosc_MeV": fmt(abs(delta_bh2) * eosc_mev, dps=OUT_DPS),
                "bind_exact_in_Eosc_MeV": fmt(abs(e_ground) * eosc_mev, dps=OUT_DPS),
                "bind_exact_in_E0_MeV": fmt(abs(e_ground) * e0_mev, dps=OUT_DPS),
                "cg_solve_inf_residual": fmt(cg_res, dps=15),
                "lanczos_eig_inf_residual": fmt(eig_res, dps=15),
            }

        b2_bh = shifts_bh2[2]
        b2_ex = shifts_exact[2]
        b2_mev = b2_ex * eosc_mev
        b3_mev = shifts_exact[3] * eosc_mev
        b4_mev = shifts_exact[4] * eosc_mev
        a2_b_mev_by_model[m_name] = b2_mev

        models_out[m_name] = {
            "per_A": per_a,
            "scaling_ratios_BH2_vs_A2": {
                "A3_over_A2": fmt(shifts_bh2[3] / b2_bh, dps=25),
                "A4_over_A2": fmt(shifts_bh2[4] / b2_bh, dps=25),
            },
            "scaling_ratios_exact_vs_A2": {
                "A3_over_A2": fmt(shifts_exact[3] / b2_ex, dps=25),
                "A4_over_A2": fmt(shifts_exact[4] / b2_ex, dps=25),
            },
            "ame_residuals_in_Eosc_chart_pct": {
                "2H_rel_err_pct": fmt(mp.mpf(100) * (b2_mev - b_ame["2H"]) / b_ame["2H"], dps=12),
                "3H_rel_err_pct": fmt(mp.mpf(100) * (b3_mev - b_ame["3H"]) / b_ame["3H"], dps=12),
                "3He_rel_err_pct": fmt(mp.mpf(100) * (b3_mev - b_ame["3He"]) / b_ame["3He"], dps=12),
                "4He_rel_err_pct": fmt(mp.mpf(100) * (b4_mev - b_ame["4He"]) / b_ame["4He"], dps=12),
            },
        }

    # Verify that fixing #9221's reversed transport (`M1_kA_2body_boundary`) restores exact 1 : 3 : 6 BH2 scaling!
    m1_bh_r3 = mp.mpf(models_out["M1_kA_2body_boundary"]["scaling_ratios_BH2_vs_A2"]["A3_over_A2"])
    m1_bh_r4 = mp.mpf(models_out["M1_kA_2body_boundary"]["scaling_ratios_BH2_vs_A2"]["A4_over_A2"])
    m1_bh_scaling_err = max(abs(m1_bh_r3 - mp.mpf(3)), abs(m1_bh_r4 - mp.mpf(6)))

    # M5: Closed-form analytic cluster-simplex cumulant sum
    zero = mp.mpf(0)
    one = mp.mpf(1)
    q2_q0 = q0 + one / q0
    q3_q0 = q0**2 + one + q0 ** (-2)
    delta8_q0 = (q0 ** (-3)) * q3_q0
    kappa3_q0 = -mp.mpf(8) / ((q2_q0**3) * (q3_q0**3))
    kappa4_q0 = mp.mpf(8) / ((q2_q0**4) * (q3_q0**4))

    b2_th_mev = a2_b_mev_by_model["M1_kA_2body_boundary"]
    b2_th_dimless = b2_th_mev / eosc_mev

    v3_plaq_sq = diag_by_a[3]["v3_plaq_3cluster_norm_sq"]
    v4_plaq_sq = diag_by_a[4]["v4_plaq_4cluster_norm_sq"]

    for m5_tag, v3_sq, v4_sq in (
        ("M5a_analytic_hoefsmit_plaq_cumulant", v3_plaq_sq, v4_plaq_sq),
        ("M5b_analytic_closed_octet_cumulant", (kappa3_q0**2) / mp.mpf(4), (kappa4_q0**2) / mp.mpf(4)),
    ):
        m5_b: dict[int, mp.mpf] = {}
        for a_nuc, e2_c, f3_c, c4_c in ((2, 1, 0, 0), (3, 3, 1, 0), (4, 6, 4, 3)):
            shift_dimless = (
                mp.mpf(e2_c) * b2_th_dimless
                + mp.mpf(f3_c) * (v3_sq / (mp.mpf(3) * delta8_q0))
                + mp.mpf(c4_c) * (v4_sq / (mp.mpf(4) * delta8_q0))
            )
            m5_b[a_nuc] = shift_dimless * eosc_mev
        a2_b_mev_by_model[m5_tag] = m5_b[2]

        models_out[m5_tag] = {
            "per_A": {
                f"A={a_nuc}": {
                    "bind_exact_in_Eosc_MeV": fmt(m5_b[a_nuc], dps=OUT_DPS),
                }
                for a_nuc in (2, 3, 4)
            },
            "v3_sq_dimless": fmt(v3_sq, dps=OUT_DPS),
            "v4_sq_dimless": fmt(v4_sq, dps=OUT_DPS),
            "scaling_ratios_exact_vs_A2": {
                "A3_over_A2": fmt(m5_b[3] / m5_b[2], dps=25),
                "A4_over_A2": fmt(m5_b[4] / m5_b[2], dps=25),
            },
            "ame_residuals_in_Eosc_chart_pct": {
                "2H_rel_err_pct": fmt(mp.mpf(100) * (m5_b[2] - b_ame["2H"]) / b_ame["2H"], dps=12),
                "3H_rel_err_pct": fmt(mp.mpf(100) * (m5_b[3] - b_ame["3H"]) / b_ame["3H"], dps=12),
                "3He_rel_err_pct": fmt(mp.mpf(100) * (m5_b[3] - b_ame["3He"]) / b_ame["3He"], dps=12),
                "4He_rel_err_pct": fmt(mp.mpf(100) * (m5_b[4] - b_ame["4He"]) / b_ame["4He"], dps=12),
            },
        }

    max_a2_dev_mev = max(abs(val - b2_th_mev) for val in a2_b_mev_by_model.values())

    summary = {
        "models": models_out,
        "b2_th_Eosc_MeV": b2_th_mev,
        "b2_th_dimless": b2_th_dimless,
        "max_a2_deviation_mev": max_a2_dev_mev,
        "kappa3_at_q0": fmt(kappa3_q0, dps=OUT_DPS),
        "kappa4_at_q0": fmt(kappa4_q0, dps=OUT_DPS),
        "v3_plaq_3cluster_norm_sq": fmt(v3_plaq_sq, dps=OUT_DPS),
        "v4_plaq_4cluster_norm_sq": fmt(v4_plaq_sq, dps=OUT_DPS),
        "m1_bh2_scaling_1_3_6_max_err": m1_bh_scaling_err,
        "max_hecke_res": max_hecke_res,
        "max_cg_res": max_cg_res,
        "max_eig_res": max_eig_res,
    }
    return summary, hoef_by_a, h_g2_by_a, v_by_a


def build_reduced_pencil(
    h0_mat: list[list[mp.mpf]], v_mat: list[list[mp.mpf]], fac_idx: int, max_dim: int = 45
) -> tuple[list[list[mp.mpf]], list[list[mp.mpf]], int]:
    """Build an orthonormal basis Q (dim x r, r <= max_dim) generated from |T_fac> under BOTH H_0 and V
    via BFS with double Gram-Schmidt, returning reduced symmetric r x r matrices (Q^T H_0 Q, Q^T V Q, 0)."""
    dim = len(h0_mat)
    if dim <= max_dim:
        return h0_mat, v_mat, fac_idx

    starmap_fn = itertools.starmap
    mul_fn = operator.mul
    h0_fx = [[int(mp.nint(mp.ldexp(val, FX_BITS))) for val in row] for row in h0_mat]
    v_fx = [[int(mp.nint(mp.ldexp(val, FX_BITS))) for val in row] for row in v_mat]

    def mv_fx(m_fx: list[list[int]], x_fx: list[int]) -> list[int]:
        return [(sum(starmap_fn(mul_fn, zip(row_fx, x_fx))) + FX_HALF) >> FX_BITS for row_fx in m_fx]

    def dot_fx(u_fx: list[int], w_fx: list[int]) -> int:
        return (sum(starmap_fn(mul_fn, zip(u_fx, w_fx))) + FX_HALF) >> FX_BITS

    v0_fx = [0] * dim
    v0_fx[fac_idx] = FX_ONE
    q_fx_basis: list[list[int]] = [v0_fx]
    q_idx = 0
    cutoff = mp.mpf("1e-74")

    while q_idx < len(q_fx_basis) and len(q_fx_basis) < max_dim:
        cur_fx = q_fx_basis[q_idx]
        q_idx += 1
        for cand_fx in (mv_fx(v_fx, cur_fx), mv_fx(h0_fx, cur_fx)):
            if len(q_fx_basis) >= max_dim:
                break
            w_fx = list(cand_fx)
            for _ in range(2):
                for qv_fx in q_fx_basis:
                    ov_fx = dot_fx(qv_fx, w_fx)
                    if ov_fx:
                        for i in range(dim):
                            w_fx[i] -= (ov_fx * qv_fx[i] + FX_HALF) >> FX_BITS
            nrm = mp.ldexp(mp.sqrt(mp.mpf(sum(starmap_fn(mul_fn, zip(w_fx, w_fx))))), -FX_BITS)
            if nrm > cutoff:
                inv_nrm_fx = int(mp.nint(mp.ldexp(mp.mpf(1) / nrm, FX_BITS)))
                q_fx_basis.append([(x * inv_nrm_fx + FX_HALF) >> FX_BITS for x in w_fx])

    r_dim = len(q_fx_basis)
    hq_fx_cols = [mv_fx(h0_fx, q_fx_basis[j]) for j in range(r_dim)]
    vq_fx_cols = [mv_fx(v_fx, q_fx_basis[j]) for j in range(r_dim)]
    zero = mp.mpf(0)
    h0_red = [[zero] * r_dim for _ in range(r_dim)]
    v_red = [[zero] * r_dim for _ in range(r_dim)]
    for i in range(r_dim):
        qi_fx = q_fx_basis[i]
        for j in range(i, r_dim):
            hij_fx = (dot_fx(qi_fx, hq_fx_cols[j]) + dot_fx(q_fx_basis[j], hq_fx_cols[i]) + 1) >> 1
            vij_fx = (dot_fx(qi_fx, vq_fx_cols[j]) + dot_fx(q_fx_basis[j], vq_fx_cols[i]) + 1) >> 1
            hij = mp.ldexp(mp.mpf(hij_fx), -FX_BITS)
            vij = mp.ldexp(mp.mpf(vij_fx), -FX_BITS)
            h0_red[i][j] = hij
            h0_red[j][i] = hij
            v_red[i][j] = vij
            v_red[j][i] = vij
    return h0_red, v_red, 0


def evaluate_jacobi_variational_battery(
    e0_mev: mp.mpf,
    eosc_mev: mp.mpf,
    b2_th_mev: mp.mpf,
    b_ame: dict[str, mp.mpf],
    hoef_by_a: dict[int, SparseHoefsmitGenerators],
    h_g2_by_a: dict[int, list[list[mp.mpf]]],
    v_by_a: dict[int, dict[str, list[list[mp.mpf]]]],
) -> dict:
    """Evaluate §3b zero-parameter 3D Jacobi variational compression models (`free_parameters = 0`)."""
    zero = mp.mpf(0)
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    four = mp.mpf(4)
    sqrt2 = mp.sqrt(two)
    three_quarters = three / four
    half = one / two
    tol_x = mp.mpf("1e-62")
    tol_f = mp.mpf("1e-60")

    jacobi_models: dict[str, dict] = {}
    max_var_grad_res = mp.mpf(0)
    max_var_eig_res = mp.mpf(0)

    # 1. J_var_breath: min_{eta > 0} [ 3/4*(A-1)*E_osc*(eta - 1/eta)^2 + E_osc * E_-(H_G2 + (2 eta^2 / (1 + eta^2))^(3/2) V) ]
    for v_key, label in (
        ("M1_kA_2body_boundary", "J_var_breath__M1_boundary"),
        ("M2_kA_2body_tait_matched", "J_var_breath__M2_tait"),
        ("M3a_kA_plaquette_pos", "J_var_breath__M3a_plaq_pos"),
        ("M3a_kA_plaquette_neg", "J_var_breath__M3a_plaq_neg"),
    ):
        per_a: dict[str, dict] = {}
        binds_mev: dict[int, mp.mpf] = {}
        for a_nuc in (2, 3, 4):
            hoef = hoef_by_a[a_nuc]
            dim = hoef.dim
            fac = hoef.fac_idx
            h0_mat = h_g2_by_a[a_nuc]
            v_mat = v_by_a[a_nuc][v_key]
            v_srows = to_srows(v_mat)

            def eval_breath_grad(eta: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
                eta2 = eta * eta
                op_u = one + eta2
                w_val = ((two * eta2) / op_u) ** (three * half)
                dw_deta = (mp.mpf(6) * sqrt2 * eta2) / (op_u ** (mp.mpf(5) * half))
                h_eta = [
                    [h0_mat[i][j] + w_val * v_mat[i][j] for j in range(dim)]
                    for i in range(dim)
                ]
                lam_e, psi_e, eig_r = lowest_eigenpair_sym(h_eta, fac, perturbed_start=True)
                v_exp = dot_mp(psi_e, matvec_srows(v_srows, psi_e))
                t_kin = three_quarters * mp.mpf(a_nuc - 1) * eosc_mev * ((eta - one / eta) ** 2)
                dt_kin = (
                    (three * half)
                    * mp.mpf(a_nuc - 1)
                    * eosc_mev
                    * (eta - one / eta)
                    * (one + one / eta2)
                )
                return t_kin + eosc_mev * lam_e, dt_kin + eosc_mev * dw_deta * v_exp, eig_r

            hi_b = mp.mpf(3)
            while eval_breath_grad(hi_b)[1] <= zero:
                hi_b *= two
            eta_opt, _ = safeguarded_root_1d(
                lambda x: eval_breath_grad(x)[1],
                one,
                hi_b,
                tol_x=tol_x,
                tol_f=tol_f,
            )
            e_min_mev, grad_opt, eig_res_f = eval_breath_grad(eta_opt)

            eta2_f = eta_opt * eta_opt
            w_f = ((two * eta2_f) / (one + eta2_f)) ** (three * half)
            t_kin_f = three_quarters * mp.mpf(a_nuc - 1) * eosc_mev * ((eta_opt - one / eta_opt) ** 2)
            b_mev = -e_min_mev

            max_var_grad_res = max(max_var_grad_res, abs(grad_opt))
            max_var_eig_res = max(max_var_eig_res, eig_res_f)
            binds_mev[a_nuc] = b_mev

            per_a[f"A={a_nuc}"] = {
                "eta_star": fmt(eta_opt, dps=OUT_DPS),
                "overlap_weight_w_star": fmt(w_f, dps=OUT_DPS),
                "breathing_T_MeV": fmt(t_kin_f, dps=25),
                "bind_MeV": fmt(b_mev, dps=25),
                "stationarity_grad_abs": fmt(abs(grad_opt), dps=15),
                "lanczos_eig_inf_residual": fmt(eig_res_f, dps=15),
            }

        jacobi_models[label] = {
            "per_A": per_a,
            "scaling_ratios_vs_A2": {
                "A3_over_A2": fmt(binds_mev[3] / binds_mev[2], dps=25),
                "A4_over_A2": fmt(binds_mev[4] / binds_mev[2], dps=25),
            },
            "ame_residuals_pct": {
                "2H_rel_err_pct": fmt(mp.mpf(100) * (binds_mev[2] - b_ame["2H"]) / b_ame["2H"], dps=12),
                "3H_rel_err_pct": fmt(mp.mpf(100) * (binds_mev[3] - b_ame["3H"]) / b_ame["3H"], dps=12),
                "3He_rel_err_pct": fmt(mp.mpf(100) * (binds_mev[3] - b_ame["3He"]) / b_ame["3He"], dps=12),
                "4He_rel_err_pct": fmt(mp.mpf(100) * (binds_mev[4] - b_ame["4He"]) / b_ame["4He"], dps=12),
            },
        }

    # 2. J_var_selfbound_Eosc & J_var_selfbound_E0:
    # Exact 3D relative Jacobi kinetic (A - 1) * t_kin * eta^2 vs C(A, 2) * V_0 * (eta^2 / (1 + eta^2))^(3/2),
    # with V_0 uniquely locked by -min_{eta > 0} E^{(2)}(eta) = b2_th_mev (zero empirical nuclear input).
    for scale_tag, t_kin_unit in (
        ("Eosc", three_quarters * eosc_mev),
        ("E0", three_quarters * e0_mev),
    ):
        # Exact stationary quadratic 1/3 * t_kin * u2 * (2*u2 - 1) = b2_th_mev (u2 = eta_2^* ^ 2 > 1/2):
        u2_star = (one + mp.sqrt(one + mp.mpf(24) * b2_th_mev / t_kin_unit)) / four
        eta2_star = mp.sqrt(u2_star)
        g_u2 = ((one + u2_star) ** (mp.mpf(5) * half)) / mp.sqrt(u2_star)
        v0_locked = (two / three) * t_kin_unit * g_u2
        t2_kin_mev = t_kin_unit * u2_star

        hp_binds: dict[int, mp.mpf] = {}
        var_binds: dict[int, mp.mpf] = {}
        hp_per_a: dict[str, dict] = {}
        var_per_a: dict[str, dict] = {}

        for a_nuc in (2, 3, 4):
            n_pairs = (a_nuc * (a_nuc - 1)) // 2
            hp_tri = ((a_nuc - 1) * (a_nuc - 2)) // 2
            # Fixed-eta_2^* Hall-Post energy: C(A,2) * b2_th + C(A-1, 2) * T2_th
            b_hp = mp.mpf(n_pairs) * b2_th_mev + mp.mpf(hp_tri) * t2_kin_mev
            # Verify Lean's algebraic identity -( (A-1)*t_kin*u2 - C(A,2)*V_0*(u2/(1+u2))^(3/2) ) == b_hp
            e_at_u2 = mp.mpf(a_nuc - 1) * t_kin_unit * u2_star - mp.mpf(n_pairs) * v0_locked * (
                (u2_star / (one + u2_star)) ** (three * half)
            )
            max_var_grad_res = max(max_var_grad_res, abs((-e_at_u2) - b_hp))
            hp_binds[a_nuc] = b_hp
            hp_per_a[f"A={a_nuc}"] = {
                "eta_fixed_at_A2": fmt(eta2_star, dps=OUT_DPS),
                "V0_locked_MeV": fmt(v0_locked, dps=25),
                "T2_kin_MeV": fmt(t2_kin_mev, dps=25),
                "bind_MeV": fmt(b_hp, dps=25),
            }

            # Unrestricted eta_A^* minimization: solve (1 + u)^(5/2) / sqrt(u) = (A/2) * g_u2 on u > 1/4
            if a_nuc == 2:
                u_a_star = u2_star
                f_res = mp.mpf(0)
            else:
                rhs_target = (mp.mpf(a_nuc) / two) * g_u2
                hi_u = u2_star * mp.mpf(2)
                while ((one + hi_u) ** (mp.mpf(5) * half)) / mp.sqrt(hi_u) <= rhs_target:
                    hi_u *= two
                u_a_star, f_res = safeguarded_root_1d(
                    lambda u, rt=rhs_target: (((one + u) ** (mp.mpf(5) * half)) / mp.sqrt(u)) - rt,
                    u2_star,
                    hi_u,
                    tol_x=tol_x,
                    tol_f=tol_f,
                )
            max_var_grad_res = max(max_var_grad_res, abs(f_res))
            eta_a_star = mp.sqrt(u_a_star)
            e_var = mp.mpf(a_nuc - 1) * t_kin_unit * u_a_star - mp.mpf(n_pairs) * v0_locked * (
                (u_a_star / (one + u_a_star)) ** (three * half)
            )
            b_var = -e_var
            var_binds[a_nuc] = b_var
            var_per_a[f"A={a_nuc}"] = {
                "eta_star": fmt(eta_a_star, dps=OUT_DPS),
                "compression_ratio_etaA_over_eta2": fmt(eta_a_star / eta2_star, dps=25),
                "V0_locked_MeV": fmt(v0_locked, dps=25),
                "bind_MeV": fmt(b_var, dps=25),
                "hall_post_excess_MeV": fmt(b_var - b_hp, dps=25),
            }

        for sub_name, b_map, p_map in (
            (f"J_var_selfbound_{scale_tag}__hall_post_fixed_eta2", hp_binds, hp_per_a),
            (f"J_var_selfbound_{scale_tag}__unrestricted_etaA", var_binds, var_per_a),
        ):
            jacobi_models[sub_name] = {
                "per_A": p_map,
                "scaling_ratios_vs_A2": {
                    "A3_over_A2": fmt(b_map[3] / b_map[2], dps=25),
                    "A4_over_A2": fmt(b_map[4] / b_map[2], dps=25),
                },
                "ame_residuals_pct": {
                    "2H_rel_err_pct": fmt(mp.mpf(100) * (b_map[2] - b_ame["2H"]) / b_ame["2H"], dps=12),
                    "3H_rel_err_pct": fmt(mp.mpf(100) * (b_map[3] - b_ame["3H"]) / b_ame["3H"], dps=12),
                    "3He_rel_err_pct": fmt(mp.mpf(100) * (b_map[3] - b_ame["3He"]) / b_ame["3He"], dps=12),
                    "4He_rel_err_pct": fmt(mp.mpf(100) * (b_map[4] - b_ame["4He"]) / b_ame["4He"], dps=12),
                },
            }

    # 3. J_var_micro_E0: Coupled microscopic Hoefsmit saturation
    # E_micro^{(A)}(eta) = 3/4 * (A - 1) * E_0(q_0) * eta^2 + E_osc(q_0) * E_-(H_G2^{(A)} + g_E0 * (eta^2 / (1 + eta^2))^(3/2) * V_M1^{(A)}),
    # where g_E0(q_0) is uniquely locked at A = 2 by -min_{eta > 0} E_micro^{(2)}(eta) = b2_th_mev.
    t_kin_e0 = three_quarters * e0_mev
    hoef2 = hoef_by_a[2]
    h0_2 = h_g2_by_a[2]
    v1_2 = v_by_a[2]["M1_kA_2body_boundary"]

    def min_a2_micro_for_g(g_val: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        def grad_eta(eta: mp.mpf) -> mp.mpf:
            eta2 = eta * eta
            op_u = one + eta2
            w_loc = g_val * ((eta2 / op_u) ** (three * half))
            dw_loc = g_val * (three * eta2) / (op_u ** (mp.mpf(5) * half))
            h_loc = [[h0_2[i][j] + w_loc * v1_2[i][j] for j in range(hoef2.dim)] for i in range(hoef2.dim)]
            _, psi_loc, _ = lowest_eigenpair_sym(h_loc, hoef2.fac_idx, perturbed_start=True)
            v_exp = dot_mp(psi_loc, matvec_dense(v1_2, psi_loc))
            return two * t_kin_e0 * eta + eosc_mev * dw_loc * v_exp

        # Stationary minimum branch lies past the barrier near eta >= 0.75 when g_val > threshold
        lo_e = mp.mpf(3) / four
        while grad_eta(lo_e) >= mp.mpf(0) and lo_e > mp.mpf(1) / mp.mpf(4):
            lo_e *= mp.mpf(7) / mp.mpf(8)
        hi_e = mp.mpf(2)
        while grad_eta(hi_e) <= mp.mpf(0):
            hi_e *= two
        eta_s, _ = safeguarded_root_1d(grad_eta, lo_e, hi_e, tol_x=tol_x, tol_f=tol_f)
        eta2_s = eta_s * eta_s
        w_s = g_val * ((eta2_s / (one + eta2_s)) ** (three * half))
        h_s = [[h0_2[i][j] + w_s * v1_2[i][j] for j in range(hoef2.dim)] for i in range(hoef2.dim)]
        lam_s, _, _ = lowest_eigenpair_sym(h_s, hoef2.fac_idx, perturbed_start=True)
        b2_s = -(t_kin_e0 * eta2_s + eosc_mev * lam_s)
        return b2_s, eta_s

    g_lo = mp.mpf(3)
    while min_a2_micro_for_g(g_lo)[0] >= b2_th_mev:
        g_lo *= half
    g_hi = mp.mpf(6)
    while min_a2_micro_for_g(g_hi)[0] <= b2_th_mev:
        g_hi *= two

    g_e0_locked, g_lock_res = safeguarded_root_1d(
        lambda g: min_a2_micro_for_g(g)[0] - b2_th_mev,
        g_lo,
        g_hi,
        tol_x=tol_x,
        tol_f=tol_f,
    )
    _, eta2_micro_star = min_a2_micro_for_g(g_e0_locked)
    max_var_grad_res = max(max_var_grad_res, abs(g_lock_res))

    micro_hp_binds: dict[int, mp.mpf] = {}
    micro_var_binds: dict[int, mp.mpf] = {}
    micro_hp_per_a: dict[str, dict] = {}
    micro_var_per_a: dict[str, dict] = {}

    for a_nuc in (2, 3, 4):
        hoef = hoef_by_a[a_nuc]
        dim = hoef.dim
        fac = hoef.fac_idx
        h0_mat = h_g2_by_a[a_nuc]
        v_mat = v_by_a[a_nuc]["M1_kA_2body_boundary"]

        # Fixed-eta2_micro_star evaluation
        u2_m = eta2_micro_star * eta2_micro_star
        w_fixed = g_e0_locked * ((u2_m / (one + u2_m)) ** (three * half))
        h_fixed = [[h0_mat[i][j] + w_fixed * v_mat[i][j] for j in range(dim)] for i in range(dim)]
        lam_fix, _, eig_fix = lowest_eigenpair_sym(h_fixed, fac, perturbed_start=True)
        max_var_eig_res = max(max_var_eig_res, eig_fix)
        b_micro_hp = -(mp.mpf(a_nuc - 1) * t_kin_e0 * u2_m + eosc_mev * lam_fix)
        micro_hp_binds[a_nuc] = b_micro_hp
        micro_hp_per_a[f"A={a_nuc}"] = {
            "g_E0_locked": fmt(g_e0_locked, dps=OUT_DPS),
            "eta_fixed_at_A2": fmt(eta2_micro_star, dps=OUT_DPS),
            "bind_MeV": fmt(b_micro_hp, dps=25),
            "lanczos_eig_inf_residual": fmt(eig_fix, dps=15),
        }

        # Unrestricted eta_A^* minimization directly on exact unreduced (h0_mat, v_mat)
        if a_nuc == 2:
            eta_m_opt = eta2_micro_star
            grad_m_res = mp.mpf(0)
        else:
            v_m_srows = to_srows(v_mat)

            def grad_micro_exact(eta: mp.mpf) -> mp.mpf:
                eta2 = eta * eta
                op_u = one + eta2
                w_loc = g_e0_locked * ((eta2 / op_u) ** (three * half))
                dw_loc = g_e0_locked * (three * eta2) / (op_u ** (mp.mpf(5) * half))
                h_loc = [[h0_mat[i][j] + w_loc * v_mat[i][j] for j in range(dim)] for i in range(dim)]
                _, psi_loc, _ = lowest_eigenpair_sym(h_loc, fac, perturbed_start=True)
                v_exp = dot_mp(psi_loc, matvec_srows(v_m_srows, psi_loc))
                return two * mp.mpf(a_nuc - 1) * t_kin_e0 * eta + eosc_mev * dw_loc * v_exp

            lo_m = eta2_micro_star
            while grad_micro_exact(lo_m) >= zero and lo_m > (one / four):
                lo_m *= mp.mpf(7) / mp.mpf(8)
            hi_m = eta2_micro_star * two
            while grad_micro_exact(hi_m) <= zero:
                hi_m *= two
            eta_m_opt, grad_m_res = safeguarded_root_1d(
                grad_micro_exact,
                lo_m,
                hi_m,
                tol_x=tol_x,
                tol_f=tol_f,
            )

        max_var_grad_res = max(max_var_grad_res, abs(grad_m_res))
        u_m_opt = eta_m_opt * eta_m_opt
        w_opt = g_e0_locked * ((u_m_opt / (one + u_m_opt)) ** (three * half))
        h_opt = [[h0_mat[i][j] + w_opt * v_mat[i][j] for j in range(dim)] for i in range(dim)]
        lam_opt, psi_opt, eig_opt = lowest_eigenpair_sym(h_opt, fac, perturbed_start=True)
        max_var_eig_res = max(max_var_eig_res, eig_opt)
        b_micro_var = -(mp.mpf(a_nuc - 1) * t_kin_e0 * u_m_opt + eosc_mev * lam_opt)
        micro_var_binds[a_nuc] = b_micro_var
        micro_var_per_a[f"A={a_nuc}"] = {
            "g_E0_locked": fmt(g_e0_locked, dps=OUT_DPS),
            "eta_star": fmt(eta_m_opt, dps=OUT_DPS),
            "hidden_colour_admixture_prob": fmt(one - psi_opt[fac] ** 2, dps=OUT_DPS),
            "bind_MeV": fmt(b_micro_var, dps=25),
            "lanczos_eig_inf_residual": fmt(eig_opt, dps=15),
        }

    for sub_name, b_map, p_map in (
        ("J_var_micro_E0__fixed_eta2", micro_hp_binds, micro_hp_per_a),
        ("J_var_micro_E0__unrestricted_etaA", micro_var_binds, micro_var_per_a),
    ):
        jacobi_models[sub_name] = {
            "per_A": p_map,
            "scaling_ratios_vs_A2": {
                "A3_over_A2": fmt(b_map[3] / b_map[2], dps=25),
                "A4_over_A2": fmt(b_map[4] / b_map[2], dps=25),
            },
            "ame_residuals_pct": {
                "2H_rel_err_pct": fmt(mp.mpf(100) * (b_map[2] - b_ame["2H"]) / b_ame["2H"], dps=12),
                "3H_rel_err_pct": fmt(mp.mpf(100) * (b_map[3] - b_ame["3H"]) / b_ame["3H"], dps=12),
                "3He_rel_err_pct": fmt(mp.mpf(100) * (b_map[3] - b_ame["3He"]) / b_ame["3He"], dps=12),
                "4He_rel_err_pct": fmt(mp.mpf(100) * (b_map[4] - b_ame["4He"]) / b_ame["4He"], dps=12),
            },
        }

    return {
        "jacobi_models": jacobi_models,
        "max_var_grad_res": max_var_grad_res,
        "max_var_eig_res": max_var_eig_res,
    }


def main() -> int:
    wb = WitnessBuilder(
        "gap1b-4he-tetrahedral-k4-flux-ring",
        engine="mpmath+sympy",
        output_dir=Path(__file__).resolve().parent,
    )
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        one = mp.mpf(1)
        me_mev = mp.mpf(codata("electron mass energy equivalent in MeV").value_str)
        mp_mev = mp.mpf(codata("proton mass energy equivalent in MeV").value_str)
        mn_mev = mp.mpf(codata("neutron mass energy equivalent in MeV").value_str)
        md_mev = mp.mpf(codata("deuteron mass energy equivalent in MeV").value_str)
        mt_mev = mp.mpf(codata("triton mass energy equivalent in MeV").value_str)
        mh_mev = mp.mpf(codata("helion mass energy equivalent in MeV").value_str)
        ma_mev = mp.mpf(codata("alpha particle mass energy equivalent in MeV").value_str)

        b_ame = {
            "2H": mp_mev + mn_mev - md_mev,
            "3H": mp_mev + mp.mpf(2) * mn_mev - mt_mev,
            "3He": mp.mpf(2) * mp_mev + mn_mev - mh_mev,
            "4He": mp.mpf(2) * mp_mev + mp.mpf(2) * mn_mev - ma_mev,
        }

        e0_mev = me_mev / (q0 * (q0 - one))
        eosc_mev = me_mev / ((q0 - one) ** 2)

        print("=" * 90)
        print(" Gap 1B (qou-3kkz) 80-dps Probe: K_4 Tetrahedral Flux Ring, Majorana & 3D Jacobi Battery")
        print("=" * 90)
        print(f"  q0 (proton pin)  = {fmt(q0, dps=30)}")
        print(f"  E0(q0) [MeV]     = {fmt(e0_mev, dps=16)}   |   E_osc(q0) [MeV] = {fmt(eosc_mev, dps=16)}")
        print(
            "  CODATA-2022 [MeV]: "
            + ", ".join(f"{k}={fmt(v, dps=10)}" for k, v in b_ame.items())
        )

        part1_comb = verify_part1_combinatorics_and_wigner()
        part1_sympy = verify_part1_sympy_9q_12q_plaquettes()
        print("  [stage 1/3] Part 1 combinatorics, Wigner & SymPy 9q/12q checks complete.", flush=True)
        static_res, hoef_by_a, h_g2_by_a, v_by_a = evaluate_static_and_analytic_models(
            q0, e0_mev, eosc_mev, b_ame
        )
        print("  [stage 2/3] Part 2A Hoefsmit 5D/42D/462D static & analytic models complete.", flush=True)
        jacobi_res = evaluate_jacobi_variational_battery(
            e0_mev,
            eosc_mev,
            static_res["b2_th_Eosc_MeV"],
            b_ame,
            hoef_by_a,
            h_g2_by_a,
            v_by_a,
        )
        print("  [stage 3/3] Part 2B 3D Jacobi variational battery complete.", flush=True)

        print("\n[Part 1] Exact Combinatorial, Wigner SU(4) & SymPy Q(q) Plaquette Verifications:")
        print(f"  K_A simplices, Tait 12q & Wigner [1^A] pass : {part1_comb['all_combinatorics_and_wigner_pass']}")
        print(f"  SymPy Q(q) 9q/12q plaquette & M(q) pass     : {part1_sympy['all_sympy_plaquette_identities_pass']}")
        print(f"  M1 corrected BH2 1:3:6 scaling max error    : {fmt(static_res['m1_bh2_scaling_1_3_6_max_err'], dps=10)}")

        print("\n[Part 2A] Fixed-Radius Microscopic & Analytic Plaquette Models (in E_osc(q0) [MeV]):")
        for m_name, m_val in static_res["models"].items():
            b2_s = m_val["per_A"]["A=2"]["bind_exact_in_Eosc_MeV"]
            b3_s = m_val["per_A"]["A=3"]["bind_exact_in_Eosc_MeV"]
            b4_s = m_val["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"]
            r3_s = m_val["scaling_ratios_exact_vs_A2"]["A3_over_A2"]
            r4_s = m_val["scaling_ratios_exact_vs_A2"]["A4_over_A2"]
            e4_pct = m_val["ame_residuals_in_Eosc_chart_pct"]["4He_rel_err_pct"]
            print(
                f"  {m_name:<36} 2H={b2_s[:8]}  A3={b3_s[:8]}  4He={b4_s[:9]} "
                f"(1:{r3_s[:6]}:{r4_s[:7]} | 4He {e4_pct[:7]}%)"
            )

        print("\n[Part 2B] Zero-Parameter 3D Jacobi Variational Compression Models (free_parameters = 0):")
        for j_name, j_val in jacobi_res["jacobi_models"].items():
            b2_s = j_val["per_A"]["A=2"]["bind_MeV"]
            b3_s = j_val["per_A"]["A=3"]["bind_MeV"]
            b4_s = j_val["per_A"]["A=4"]["bind_MeV"]
            r3_s = j_val["scaling_ratios_vs_A2"]["A3_over_A2"]
            r4_s = j_val["scaling_ratios_vs_A2"]["A4_over_A2"]
            e4_pct = j_val["ame_residuals_pct"]["4He_rel_err_pct"]
            print(
                f"  {j_name:<44} 2H={b2_s[:8]}  A3={b3_s[:8]}  4He={b4_s[:9]} "
                f"(1:{r3_s[:6]}:{r4_s[:7]} | 4He {e4_pct[:7]}%)"
            )

        wb.set_description(
            "Pre-registered 80-dps (50-dps serialized) Option 1B (`qou-3kkz`) evaluation of "
            "(1) exact K_A simplex/Hamiltonian-cycle combinatorics, K_4 Tait 12-quark bijection, "
            "Wigner SU(4) Majorana space-exchange on [1^A]_{sigma tau} (A <= 4) with A = 5 Pauli "
            "shell closure, and symbolic Q(q) 9q/12q colour-reconnection traces & closed plaquette "
            "cumulants backing `TetrahedralFluxRingAndMajoranaCluster.lean`; (2A) fixed-radius "
            "Hoefsmit S^{[A,A,A]}_{H_{3A}(q_0)} 2-body + 3-body triangular face + 4-body tetrahedral "
            "ring models M0..M5; and (2B) zero-parameter 3D Jacobi variational compression models "
            "(A - 1 relative kinetic modes vs C(A,2) Wigner pairs) across A = 2, 3, 4."
        )
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("E_osc_MeV", fmt(eosc_mev, dps=OUT_DPS))
        wb.add_parameter("E0_MeV", fmt(e0_mev, dps=OUT_DPS))
        wb.add_parameter("m_e_MeV", fmt(me_mev, dps=OUT_DPS))
        wb.add_parameter("free_parameters", 0)

        wb.add_data(
            "lean_module",
            "folio/quantum-observable-universe/lean/QOU/Nuclear/TetrahedralFluxRingAndMajoranaCluster.lean",
        )
        wb.add_data(
            "preregistration",
            "computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/PREREGISTRATION.md",
        )
        wb.add_data(
            "codata_2022_nuclear_binding_MeV",
            {k: fmt(v, dps=OUT_DPS) for k, v in b_ame.items()},
        )
        wb.add_data(
            "codata_2022_binding_ratios_vs_2H",
            {
                "3H_over_2H": fmt(b_ame["3H"] / b_ame["2H"], dps=25),
                "3He_over_2H": fmt(b_ame["3He"] / b_ame["2H"], dps=25),
                "4He_over_2H": fmt(b_ame["4He"] / b_ame["2H"], dps=25),
            },
        )
        wb.add_data("part1_combinatorics_tait_and_wigner_majorana", part1_comb)
        wb.add_data("part1_sympy_9q_12q_plaquette_identities", part1_sympy)
        wb.add_data(
            "part2a_fixed_radius_plaquette_summary",
            {
                "kappa3_at_q0": static_res["kappa3_at_q0"],
                "kappa4_at_q0": static_res["kappa4_at_q0"],
                "v3_plaq_3cluster_norm_sq": static_res["v3_plaq_3cluster_norm_sq"],
                "v4_plaq_4cluster_norm_sq": static_res["v4_plaq_4cluster_norm_sq"],
                "m1_bh2_scaling_1_3_6_max_err": fmt(
                    static_res["m1_bh2_scaling_1_3_6_max_err"], dps=20
                ),
                "models": static_res["models"],
            },
        )
        wb.add_data("part2b_jacobi_variational_battery", jacobi_res["jacobi_models"])

        wb.add_assertion(
            "kA_simplex_counts_tait_12q_bijection_and_wigner_majorana_su4_exact",
            1 if part1_comb["all_combinatorics_and_wigner_pass"] else 0,
            1,
            "0",
            source="TetrahedralFluxRingAndMajoranaCluster.kA_simplex_and_cycle_counts & wignerMajorana_eigenvalue_and_pair_sum",
        )
        wb.add_assertion(
            "sympy_9q_12q_plaquette_overlaps_and_rank1_cluster_transfer_exact",
            1 if part1_sympy["all_sympy_plaquette_identities_pass"] else 0,
            1,
            "0",
            source="TetrahedralFluxRingAndMajoranaCluster.closedTriangle_nine_eq_trace & closedRing_twelve_eq_trace",
        )
        wb.add_assertion(
            "corrected_positive_braid_transport_restores_exact_1_3_6_BH2_scaling",
            fmt(static_res["m1_bh2_scaling_1_3_6_max_err"], dps=15),
            "0",
            "1e-70",
            source="Fixing #9221 reversed non-adjacent braid transport in M1_kA_2body_boundary",
        )
        wb.add_assertion(
            "hoefsmit_hecke_cg_and_lanczos_residuals_below_1e_minus_70",
            fmt(
                max(
                    static_res["max_hecke_res"],
                    static_res["max_cg_res"],
                    static_res["max_eig_res"],
                    jacobi_res["max_var_eig_res"],
                ),
                dps=15,
            ),
            "0",
            "1e-68",
            source="80-dps Hoefsmit S^{[A,A,A]} Hecke/symmetry, CG, and Lanczos residual certification",
        )
        wb.add_assertion(
            "jacobi_variational_stationarity_and_hall_post_identities_below_1e_minus_58",
            fmt(jacobi_res["max_var_grad_res"], dps=15),
            "0",
            "1e-58",
            source="TetrahedralFluxRingAndMajoranaCluster.jacobi_mode_factorization_and_hall_post_ring & 80-dps stationarity",
        )
        wb.add_assertion(
            "deuteron_2H_benchmark_preserved_identically_across_all_3body_4body_plaquette_models",
            fmt(static_res["max_a2_deviation_mev"], dps=15),
            "0",
            "1e-70",
            source="f_3(2) = 0 and c_4(2) = 0 on K_2 (zero 3-/4-body terms in deuteron)",
        )

        wb.add_caveat(
            "1. Fixing #9221's reversed non-adjacent braid transport in M1_kA_2body_boundary restores "
            "exact 1 : 3 : 6 BH2 pair scaling and lifts A=3 at fixed spatial overlap from 5.1059 MeV "
            "to 6.9623 MeV (-9.79% vs 3He) while preserving 2H = 2.2648 MeV (+1.81%) and placing pure "
            "pairwise 4He at 14.3267 MeV (6.326x, vs single-bag [12]_S12 Pauli-quenched 6.65 MeV). "
            "2. Adding pre-registered positive-braid 3-interface triangular plaquettes across C(A,3) "
            "faces and 4-interface Hamiltonian rings across c_4(A) = 3*C(A,4) tetrahedral 4-cycles "
            "with direct holonomy sign (+, M3a_kA_plaquette_pos, free_parameters = 0) yields "
            "2H = 2.2648 MeV (+1.81%), A=3 = 9.0140 MeV (+6.27% vs 3H), and 4He = 29.3291 MeV "
            "(+3.65% vs 28.2956 MeV, ratio 1 : 3.980 : 12.950 vs empirical 1 : 3.813 : 12.720), while "
            "the 2nd-order non-double-counted 3-/4-cluster cumulant sum (M5a) gives 8.5574 MeV (+0.89% "
            "vs 3H) and 24.7943 MeV (-12.37% vs 4He); by contrast, the opposite Kogut-Susskind sign "
            "(-, M3a_kA_plaquette_neg = 17.5360 MeV) and strictly planar cyclic cumulants without "
            "interior braid over-crossings (M5b = 13.5965 MeV) underbind 4He, showing sign/ordering "
            "sensitivity of non-local braid holonomies. "
            "3. Independently, pure 2-body Wigner pairing with 3D relative Jacobi variational "
            "compression in the order-zero nuclear kinetic scale E_0(q_0) = m_e / (q_0(q_0 - 1)) "
            "(J_var_selfbound_E0, free_parameters = 0) brackets empirical 4He between 26.0197 MeV "
            "(-8.04%, fixed-eta_2^* Hall-Post bound) and 30.5457 MeV (+7.95%, unrestricted eta_4^*), "
            "confirming that 3D Jacobi kinematics and tetrahedral colour-flux ring reconnection must "
            "be derived jointly from a single microscopic 3D spatial-braid action so their contributions "
            "are not double-counted (as seen in J_var_breath__M3a_plaq_pos = 35.2700 MeV, +24.65%)."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
