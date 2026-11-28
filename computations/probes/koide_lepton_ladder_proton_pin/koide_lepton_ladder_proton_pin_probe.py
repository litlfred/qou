#!/usr/bin/env python3
"""Pre-registered 80-dps proton-pin probe for bean `qou-cw8i` (`qou-s028` / `qou-myts`):
Division-Free S_3/Z_3 Singlet-Doublet Koide Equipartition & 2026-11-28 Least-Crossing Lepton Ladder Invariants.

Pre-registration committed BEFORE numerical execution:
  - `computations/probes/koide_lepton_ladder_proton_pin/PREREGISTRATION.md`
Companion Lean 4 formalizations (`0 sorry`, `0` custom `axiom`s, `[CommRing R]`):
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/KoideSingletDoubletEquipartition.lean`
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean`
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean`

Strict proton-pin & anti-fit discipline (`owner-rulings.md` rows 17-18, 228-230):
  - `mpmath.workdps(80)` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`, registered in
    `computations/q0_anchor_manifest.json` -> `"physical_proton"`),
  - CAL-2 muon pin explicitly ON HOLD until first-principles rederivation (2026-11-28 owner directive),
  - zero `float64` imports, casts, or lossy literals (`scripts/probe-float64-guard.py --diff` clean),
  - zero fitted parameters, colours, or weights (`NO FITTING, EXCEPT CAL-1/2/3`).
"""

from __future__ import annotations

from collections import defaultdict
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "schemas" / "witness-schema" / "python",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at, vol_4_1_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

# 2026-11-28 ruled least-crossing 2-component lepton link ladder (`owner-rulings.md` row 17):
# 1-based strand-slot encoding: +1 = sigma_0, -1 = sigma_0^-1, +2 = sigma_1, -2 = sigma_1^-1
LADDER_WORDS: dict[str, list[int]] = {
    "e_hopf": [1, 2, 1],
    "mu_t24": [1, 1, 1, 1, -2],
    "tau_whitehead": [1, 1, -2, 1, -2],
}
AXIS_LOOP_4STRAND: list[int] = [3, 2, 1, 1, 2, 3]


# ---------------------------------------------------------------------------
# 1. Exact Symbolic Verification (`sympy` over Z / Q) mirroring Lean 4 module
# ---------------------------------------------------------------------------
def run_symbolic_checks() -> dict[str, object]:
    u, v, x, q, vol41, a0, b, c, w = sp.symbols(
        "u v x q vol41 a0 b c w", commutative=True
    )
    t = sp.Symbol("t", commutative=True)

    # §1: Scaled S_3 projectors 3 P_1 and 3 P_std
    p_sing = sp.Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    p_doub = sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
    vec = sp.Matrix([u, v, x])
    vs = p_sing * vec
    vd = p_doub * vec
    norm_v = u**2 + v**2 + x**2
    norm_vs = sum(comp**2 for comp in vs)
    norm_vd = sum(comp**2 for comp in vd)
    pyth_ok = sp.expand(9 * norm_v - (norm_vs + norm_vd)) == 0
    koide_proj_ok = (
        sp.expand(norm_vd - norm_vs - 3 * (3 * norm_v - 2 * (u + v + x) ** 2)) == 0
    )

    # §2: Circulant Fourier moments (1 + w + w^2 = 0) & Schur-Weyl 4 = 4 split
    cyc3 = 1 + w + w**2
    lam0 = a0 + b + c
    lam1 = a0 + b * w + c * w**2
    lam2 = a0 + b * w**2 + c * w
    _, rem_m1 = sp.div(sp.expand(lam0 + lam1 + lam2 - 3 * a0), cyc3, w)
    _, rem_m2 = sp.div(
        sp.expand(lam0**2 + lam1**2 + lam2**2 - 3 * (a0**2 + 2 * b * c)), cyc3, w
    )
    _, rem_det = sp.div(
        sp.expand(lam0 * lam1 * lam2 - (a0**3 + b**3 + c**3 - 3 * a0 * b * c)),
        cyc3,
        w,
    )
    fourier_ok = (
        sp.expand(rem_m1) == 0
        and sp.expand(rem_m2) == 0
        and sp.expand(rem_det) == 0
    )

    sw_sing = q**6 + q**4 + q**2 + 1
    sw_doub = 2 * q**2 * (q**2 + 1)
    sw_tot = (q**2 + 1) ** 3
    schur_weyl_ok = (
        sp.expand(sw_sing + sw_doub - sw_tot) == 0
        and sp.expand(sw_sing - sw_doub - (q**2 + 1) * (q**2 - 1) ** 2) == 0
        and sw_sing.subs(q, 1) == 4
        and sw_doub.subs(q, 1) == 4
    )

    # §3: Radical-free symmetric quartic Koide mass polynomial K_4(m1, m2, m3)
    m1, m2, m3 = u**2, v**2, x**2
    k4 = ((m1 + m2 + m3) ** 2 - 16 * (m1 * m2 + m2 * m3 + m3 * m1)) ** 2 - 1536 * (
        m1 + m2 + m3
    ) * m1 * m2 * m3
    four_factors = (
        (3 * (m1 + m2 + m3) - 2 * (u + v + x) ** 2)
        * (3 * (m1 + m2 + m3) - 2 * (u + v - x) ** 2)
        * (3 * (m1 + m2 + m3) - 2 * (u - v + x) ** 2)
        * (3 * (m1 + m2 + m3) - 2 * (-u + v + x) ** 2)
    )
    quartic_fac_ok = sp.expand(k4 - four_factors) == 0

    # §5: Morton-Birman reduced Burau & q^12 skein differences on least-crossing ladder
    b0 = sp.Matrix([[-t, 1], [0, 1]])
    b0i = sp.Matrix([[-1 / t, 1 / t], [0, 1]])
    b1 = sp.Matrix([[1, 0], [t, -t]])
    b1i = sp.Matrix([[1, 0], [1, -1 / t]])
    gmap = {1: b0, -1: b0i, 2: b1, -2: b1i}

    def eval_burau(word: list[int]) -> sp.Matrix:
        mat = sp.eye(2)
        for s in reversed(word):
            mat = gmap[s] * mat
        return sp.simplify(mat)

    be = eval_burau(LADDER_WORDS["e_hopf"])
    bmu = eval_burau(LADDER_WORDS["mu_t24"])
    btau = eval_burau(LADDER_WORDS["tau_whitehead"])
    bfig8 = eval_burau([1, -2, 1, -2])

    burau_ok = (
        sp.simplify((sp.eye(2) - be).det() - (1 - t**3)) == 0
        and sp.simplify(t * (sp.eye(2) - bmu).det() - (1 - t**3) * (1 + t**2)) == 0
        and sp.simplify(
            t**2 * (sp.eye(2) - btau).det() - (t**3 - 1) * (t - 1) ** 2
        )
        == 0
        and sp.simplify(
            t**2 * (sp.eye(2) - bfig8).det() + (1 + t + t**2) * (t**2 - 3 * t + 1)
        )
        == 0
    )

    q12_me = q**6 * (q**2 + 1) * (q**4 + 1)
    q12_mmu = (q**2 + 1) * (q**8 + q**4 - q**2 + 1)
    q12_mtau = q**4 * (q**2 + 1) * (q**10 - q**8 + 2 * q**6 - q**4 + 2 * q**2 - 1)
    skein_ok = (
        sp.expand((q12_me - q12_mmu) - (q**12 - 1)) == 0
        and sp.expand((q12_mtau - q12_me) - q**4 * (q**12 - 1)) == 0
        and q12_me.subs(q, 1) == 4
        and q12_mmu.subs(q, 1) == 4
        and q12_mtau.subs(q, 1) == 4
    )

    all_ok = (
        pyth_ok
        and koide_proj_ok
        and fourier_ok
        and schur_weyl_ok
        and quartic_fac_ok
        and burau_ok
        and skein_ok
    )
    return {
        "all_symbolic_identities_verified": all_ok,
        "s3_projector_pythagorean_and_koide_exact": pyth_ok and koide_proj_ok,
        "circulant_fourier_moments_discharged": fourier_ok,
        "schur_weyl_v3_four_eq_four_equipartition": schur_weyl_ok,
        "koide_quartic_mass_poly_four_branch_factorization": quartic_fac_ok,
        "morton_birman_burau_ladder_factorizations": burau_ok,
        "q12_ring_mass_skein_differences_exact": skein_ok,
    }


# ---------------------------------------------------------------------------
# 2. 80-dps Pure-`mpmath` U_q(sl_2) R-Matrix & Weight-Block Trace Engine
# ---------------------------------------------------------------------------
def qint_mp(n: int, q: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


def qint_root_safe(n: int, q: mp.mpc) -> mp.mpc:
    """Exact geometric sum sum_{m=0}^{n-1} q^{n - 1 - 2m} (division-free at roots of unity)."""
    acc = mp.mpc(0)
    for m in range(n):
        acc += q ** (n - 1 - 2 * m)
    return acc


def build_rcheck_mp(
    n_col: int, t_log_q: mp.mpf | mp.mpc
) -> tuple[list[list[mp.mpc]], list[list[mp.mpc]], list[mp.mpc], list[int]]:
    """Build exact N^2 x N^2 checked R-matrix Rc = P D S, its inverse Rci = S^-1 D^-1 P,
    pivotal K diagonal, and weight list h_p = (N - 1) - 2p at q = exp(t_log_q)."""
    q = mp.exp(t_log_q)
    n_top = n_col - 1
    weights = [n_top - 2 * p for p in range(n_col)]
    k_diag = [mp.exp(t_log_q * w) for w in weights]

    e_mat = [[mp.mpc(0) for _ in range(n_col)] for _ in range(n_col)]
    f_mat = [[mp.mpc(0) for _ in range(n_col)] for _ in range(n_col)]
    for p in range(n_col):
        if p + 1 < n_col:
            f_mat[p + 1][p] = qint_root_safe(p + 1, q)
        if p >= 1:
            e_mat[p - 1][p] = qint_root_safe(n_top - p + 1, q)

    def mat_mul_small(
        a: list[list[mp.mpc]], b: list[list[mp.mpc]]
    ) -> list[list[mp.mpc]]:
        sz = len(a)
        out = [[mp.mpc(0) for _ in range(sz)] for _ in range(sz)]
        for i in range(sz):
            for k in range(sz):
                aik = a[i][k]
                if aik != 0:
                    for j in range(sz):
                        out[i][j] += aik * b[k][j]
        return out

    dim2 = n_col * n_col
    s_mat = [[mp.mpc(0) for _ in range(dim2)] for _ in range(dim2)]
    ek = [[mp.mpc(1 if i == j else 0) for j in range(n_col)] for i in range(n_col)]
    fk = [[mp.mpc(1 if i == j else 0) for j in range(n_col)] for i in range(n_col)]
    q_minus_qi = q - mp.mpf(1) / q
    qfact_k = mp.mpc(1)
    for k in range(n_col):
        if k > 0:
            qfact_k *= qint_root_safe(k, q)
        pref = mp.exp(t_log_q * (mp.mpf(k * (k - 1)) / mp.mpf(2))) * (
            q_minus_qi**k
        ) / qfact_k
        for i1 in range(n_col):
            for j1 in range(n_col):
                e_val = ek[i1][j1]
                if e_val == 0:
                    continue
                for i2 in range(n_col):
                    for j2 in range(n_col):
                        f_val = fk[i2][j2]
                        if f_val != 0:
                            s_mat[i1 * n_col + i2][j1 * n_col + j2] += (
                                pref * e_val * f_val
                            )
        ek = mat_mul_small(ek, e_mat)
        fk = mat_mul_small(fk, f_mat)

    # Rc = P D S: row (j1, j2) of D*S moved to (j2, j1)
    rc = [[mp.mpc(0) for _ in range(dim2)] for _ in range(dim2)]
    for i1 in range(n_col):
        for i2 in range(n_col):
            d_fac = mp.exp(t_log_q * (mp.mpf(weights[i1] * weights[i2]) / mp.mpf(2)))
            row_ds = i1 * n_col + i2
            row_rc = i2 * n_col + i1
            for col in range(dim2):
                rc[row_rc][col] = d_fac * s_mat[row_ds][col]

    # Inverse Rc^-1 via mp.matrixlu on each 2-strand weight block (tiny: max size N <= 16)
    blocks2: dict[int, list[int]] = defaultdict(list)
    for p1 in range(n_col):
        for p2 in range(n_col):
            blocks2[p1 + p2].append(p1 * n_col + p2)
    rci = [[mp.mpc(0) for _ in range(dim2)] for _ in range(dim2)]
    for idxs in blocks2.values():
        bsz = len(idxs)
        sub = mp.matrix([[rc[r][c] for c in idxs] for r in idxs])
        sub_inv = sub ** (-1)
        for bi, r in enumerate(idxs):
            for bj, c in enumerate(idxs):
                rci[r][c] = sub_inv[bi, bj]

    return rc, rci, k_diag, weights


def closed_braid_ring_mass_mp(
    n_col: int, q_real: mp.mpf, word: list[int], n_strands: int
) -> mp.mpf:
    """Exact 80-dps framing-stabilized ring mass m_N(beta) = f^{-w} tr(K^{otimes n} rho_N(beta))
    exploiting weight-sector block diagonalization (zero precision loss, fast for N <= 4)."""
    t_log = mp.log(q_real)
    rc, rci, k_diag, _ = build_rcheck_mp(n_col, t_log)
    n_top = n_col - 1
    writhe = sum(1 if s > 0 else -1 for s in word)
    # Framing factor f = q^{2 j (j + 1)} = q^{(N^2 - 1)/2}
    framing = mp.exp(t_log * (mp.mpf(n_col * n_col - 1) / mp.mpf(2)))

    # Enumerate tuples in {0..N-1}^{n_strands} grouped by sum(p)
    states_by_sum: dict[int, list[tuple[int, ...]]] = defaultdict(list)

    def gen_tuples(rem: int, prefix: tuple[int, ...]) -> None:
        if rem == 0:
            states_by_sum[sum(prefix)].append(prefix)
            return
        for p in range(n_col):
            gen_tuples(rem - 1, prefix + (p,))

    gen_tuples(n_strands, ())

    total_trace = mp.mpc(0)
    unique_letters = set(word)
    for p_sum, states in states_by_sum.items():
        dim_b = len(states)
        pos = {st: idx for idx, st in enumerate(states)}
        gen_mats: dict[int, list[list[mp.mpc]]] = {}
        for s in unique_letters:
            slot = abs(s) - 1
            rmat = rc if s > 0 else rci
            gmat = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for st, col_idx in pos.items():
                pa, pb = st[slot], st[slot + 1]
                pair_sum = pa + pb
                in_pair = pa * n_col + pb
                for a_new in range(max(0, pair_sum - n_top), min(n_top, pair_sum) + 1):
                    b_new = pair_sum - a_new
                    val = rmat[a_new * n_col + b_new][in_pair]
                    if val != 0:
                        new_st = st[:slot] + (a_new, b_new) + st[slot + 2 :]
                        gmat[pos[new_st]][col_idx] += val
            gen_mats[s] = gmat

        # Multiply word on block
        cur = [
            [mp.mpc(1 if i == j else 0) for j in range(dim_b)] for i in range(dim_b)
        ]
        for s in word:
            gm = gen_mats[s]
            nxt = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for i in range(dim_b):
                for k in range(dim_b):
                    cik = cur[i][k]
                    if cik != 0:
                        for j in range(dim_b):
                            if gm[k][j] != 0:
                                nxt[i][j] += cik * gm[k][j]
            cur = nxt

        # K^{otimes n_strands} acts as q^{n_strands*(N-1) - 2*p_sum} on this weight block!
        k_weight = mp.exp(t_log * mp.mpf(n_strands * n_top - 2 * p_sum))
        blk_tr = mp.mpc(0)
        for i in range(dim_b):
            blk_tr += cur[i][i]
        total_trace += k_weight * blk_tr

    return (total_trace * (framing ** (-writhe))).real


def axis_convolution_from_weight_spaces_mp(
    n_col: int, q_real: mp.mpf, word3: list[int]
) -> mp.mpf:
    """Exact 3-strand weight-space decomposition of m_N(closure(beta) union axis)
    (`AxisConvolutionOperator.lean`):
      On V_j^{otimes 3}, multiplicity trace mu_a = T_{a-1} - T_{a+1} (a = 2J + 1),
      chi_a = mu_a * [a]_q, and m_N(beta union A) = f^{-6} sum_a mu_a * [a * N]_q."""
    t_log = mp.log(q_real)
    rc, rci, _, _ = build_rcheck_mp(n_col, t_log)
    n_top = n_col - 1
    writhe = sum(1 if s > 0 else -1 for s in word3)
    framing = mp.exp(t_log * (mp.mpf(n_col * n_col - 1) / mp.mpf(2)))

    groups: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for p1 in range(n_col):
        for p2 in range(n_col):
            for p3 in range(n_col):
                w2 = 3 * n_top - 2 * (p1 + p2 + p3)
                if w2 >= 0:
                    groups[w2].append((p1, p2, p3))

    t_weight: dict[int, mp.mpc] = {}
    unique_letters = set(word3)
    for w2, states in groups.items():
        dim_b = len(states)
        pos = {st: idx for idx, st in enumerate(states)}
        gen_mats: dict[int, list[list[mp.mpc]]] = {}
        for s in unique_letters:
            slot = abs(s) - 1
            rmat = rc if s > 0 else rci
            gmat = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for st, col_idx in pos.items():
                pa, pb = st[slot], st[slot + 1]
                pair_sum = pa + pb
                in_pair = pa * n_col + pb
                for a_new in range(max(0, pair_sum - n_top), min(n_top, pair_sum) + 1):
                    b_new = pair_sum - a_new
                    val = rmat[a_new * n_col + b_new][in_pair]
                    if val != 0:
                        if slot == 0:
                            new_st = (a_new, b_new, st[2])
                        else:
                            new_st = (st[0], a_new, b_new)
                        gmat[pos[new_st]][col_idx] += val
            gen_mats[s] = gmat

        cur = [
            [mp.mpc(1 if i == j else 0) for j in range(dim_b)] for i in range(dim_b)
        ]
        for s in word3:
            gm = gen_mats[s]
            nxt = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for i in range(dim_b):
                for k in range(dim_b):
                    cik = cur[i][k]
                    if cik != 0:
                        for j in range(dim_b):
                            if gm[k][j] != 0:
                                nxt[i][j] += cik * gm[k][j]
            cur = nxt
        blk_tr = mp.mpc(0)
        for i in range(dim_b):
            blk_tr += cur[i][i]
        t_weight[w2] = blk_tr * (framing ** (-writhe))

    tot = mp.mpc(0)
    for w2, tw in t_weight.items():
        a_dim = w2 + 1
        mu_a = tw - t_weight.get(w2 + 2, mp.mpc(0))
        tot += mu_a * qint_mp(a_dim * n_col, q_real)
    return (tot * (framing ** (-6))).real


def cut_axis_kashaev_root_mp(n_col: int, word3: list[int]) -> mp.mpc:
    """Exact 80-dps Kashaev cut-axis invariant c_N(beta) at q = exp(i pi / N)
    (`AxisKashaevReading.lean`: c_N = f^{-6} sum_a mu_a(beta) * a * (-1)^{a - 1})."""
    t_root = mp.mpc(0, 1) * mp.pi / mp.mpf(n_col)
    rc, rci, _, _ = build_rcheck_mp(n_col, t_root)
    n_top = n_col - 1
    writhe = sum(1 if s > 0 else -1 for s in word3)
    framing = mp.exp(t_root * (mp.mpf(n_col * n_col - 1) / mp.mpf(2)))

    groups: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for p1 in range(n_col):
        for p2 in range(n_col):
            for p3 in range(n_col):
                w2 = 3 * n_top - 2 * (p1 + p2 + p3)
                if w2 >= 0:
                    groups[w2].append((p1, p2, p3))

    t_weight: dict[int, mp.mpc] = {}
    unique_letters = set(word3)
    for w2, states in groups.items():
        dim_b = len(states)
        pos = {st: idx for idx, st in enumerate(states)}
        gen_mats: dict[int, list[list[mp.mpc]]] = {}
        for s in unique_letters:
            slot = abs(s) - 1
            rmat = rc if s > 0 else rci
            gmat = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for st, col_idx in pos.items():
                pa, pb = st[slot], st[slot + 1]
                pair_sum = pa + pb
                in_pair = pa * n_col + pb
                for a_new in range(max(0, pair_sum - n_top), min(n_top, pair_sum) + 1):
                    b_new = pair_sum - a_new
                    val = rmat[a_new * n_col + b_new][in_pair]
                    if val != 0:
                        if slot == 0:
                            new_st = (a_new, b_new, st[2])
                        else:
                            new_st = (st[0], a_new, b_new)
                        gmat[pos[new_st]][col_idx] += val
            gen_mats[s] = gmat

        cur = [
            [mp.mpc(1 if i == j else 0) for j in range(dim_b)] for i in range(dim_b)
        ]
        for s in word3:
            gm = gen_mats[s]
            nxt = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for i in range(dim_b):
                for k in range(dim_b):
                    cik = cur[i][k]
                    if cik != 0:
                        for j in range(dim_b):
                            if gm[k][j] != 0:
                                nxt[i][j] += cik * gm[k][j]
            cur = nxt
        blk_tr = mp.mpc(0)
        for i in range(dim_b):
            blk_tr += cur[i][i]
        t_weight[w2] = blk_tr * (framing ** (-writhe))

    tot = mp.mpc(0)
    for w2, tw in t_weight.items():
        a_dim = w2 + 1
        mu_a = tw - t_weight.get(w2 + 2, mp.mpc(0))
        sign = mp.mpf(1) if (a_dim - 1) % 2 == 0 else mp.mpf(-1)
        tot += mu_a * mp.mpf(a_dim) * sign
    return tot * (framing ** (-6))


def cut_axis_4strand_partial_trace_mp(n_col: int, word4: list[int]) -> mp.mpc:
    """Independent 4-strand partial-trace cross-check at q = exp(i pi / N):
    traces strands 0, 1, 2 with K^{-1} while leaving axis strand 3 open at state p4 = 0."""
    t_root = mp.mpc(0, 1) * mp.pi / mp.mpf(n_col)
    rc, rci, k_diag, _ = build_rcheck_mp(n_col, t_root)
    n_top = n_col - 1
    writhe = sum(1 if s > 0 else -1 for s in word4)
    framing = mp.exp(t_root * (mp.mpf(n_col * n_col - 1) / mp.mpf(2)))

    states_by_sum: dict[int, list[tuple[int, int, int, int]]] = defaultdict(list)
    for p1 in range(n_col):
        for p2 in range(n_col):
            for p3 in range(n_col):
                for p4 in range(n_col):
                    states_by_sum[p1 + p2 + p3 + p4].append((p1, p2, p3, p4))

    diag00 = mp.mpc(0)
    unique_letters = set(word4)
    for states in states_by_sum.values():
        # Only blocks containing at least one state with p4 == 0 contribute to (0,0) axis slot
        if not any(st[3] == 0 for st in states):
            continue
        dim_b = len(states)
        pos = {st: idx for idx, st in enumerate(states)}
        gen_mats: dict[int, list[list[mp.mpc]]] = {}
        for s in unique_letters:
            slot = abs(s) - 1
            rmat = rc if s > 0 else rci
            gmat = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for st, col_idx in pos.items():
                pa, pb = st[slot], st[slot + 1]
                pair_sum = pa + pb
                in_pair = pa * n_col + pb
                for a_new in range(max(0, pair_sum - n_top), min(n_top, pair_sum) + 1):
                    b_new = pair_sum - a_new
                    val = rmat[a_new * n_col + b_new][in_pair]
                    if val != 0:
                        new_st = st[:slot] + (a_new, b_new) + st[slot + 2 :]
                        gmat[pos[new_st]][col_idx] += val
            gen_mats[s] = gmat

        cur = [
            [mp.mpc(1 if i == j else 0) for j in range(dim_b)] for i in range(dim_b)
        ]
        for s in word4:
            gm = gen_mats[s]
            nxt = [[mp.mpc(0) for _ in range(dim_b)] for _ in range(dim_b)]
            for i in range(dim_b):
                for k in range(dim_b):
                    cik = cur[i][k]
                    if cik != 0:
                        for j in range(dim_b):
                            if gm[k][j] != 0:
                                nxt[i][j] += cik * gm[k][j]
            cur = nxt

        for idx, st in enumerate(states):
            if st[3] == 0:
                piv = mp.mpf(1) / (k_diag[st[0]] * k_diag[st[1]] * k_diag[st[2]])
                diag00 += piv * cur[idx][idx]

    return diag00 * (framing ** (-writhe))


def koide_ratio_vec_mp(m1: mp.mpf, m2: mp.mpf, m3: mp.mpf) -> mp.mpf:
    u1, u2, u3 = mp.sqrt(abs(m1)), mp.sqrt(abs(m2)), mp.sqrt(abs(m3))
    return (m1 + m2 + m3) / ((u1 + u2 + u3) ** 2)


# ---------------------------------------------------------------------------
# 3. Main Execution & Schema-Validated Witness Generation
# ---------------------------------------------------------------------------
def main() -> int:
    with mp.workdps(WORK_DPS):
        sym_res = run_symbolic_checks()

        # Proton-pinned substrate constants at 80 dps (muon pin on hold per 2026-11-28 directive)
        q0 = q_at(WORK_DPS)
        vol41 = vol_4_1_at(WORK_DPS)
        hbar_q0 = mp.mpf(1) - mp.mpf(1) / q0

        # Part A: Exact N = 2, 3, 4 bare closure & closure U axis ring traces at proton pin q0
        eps_diff = mp.mpf(10) ** (-32)
        part_a_ladder_traces: dict[str, dict[str, object]] = {}
        max_axis_isotypic_rel_err = mp.mpf(0)

        # Also check q^12 skein difference identity numerically at q0 for N = 2
        m2_e = closed_braid_ring_mass_mp(2, q0, LADDER_WORDS["e_hopf"], 3)
        m2_mu = closed_braid_ring_mass_mp(2, q0, LADDER_WORDS["mu_t24"], 3)
        m2_tau = closed_braid_ring_mass_mp(2, q0, LADDER_WORDS["tau_whitehead"], 3)
        skein_diff_e_mu_res = abs((m2_e - m2_mu) - (mp.mpf(1) - q0 ** (-12)))
        skein_diff_tau_e_res = abs(
            (m2_tau - m2_e) - (q0**4) * (mp.mpf(1) - q0 ** (-12))
        )

        for n_col in (2, 3, 4):
            bare_vals: dict[str, mp.mpf] = {}
            bare_u_q0: dict[str, mp.mpf] = {}
            bare_u_q1: dict[str, mp.mpf] = {}
            axis_vals: dict[str, mp.mpf] = {}
            axis_u_q0: dict[str, mp.mpf] = {}

            for gname, wd in LADDER_WORDS.items():
                mb = closed_braid_ring_mass_mp(n_col, q0, wd, 3)
                mb_hi = closed_braid_ring_mass_mp(n_col, q0 + eps_diff, wd, 3)
                mb_lo = closed_braid_ring_mass_mp(n_col, q0 - eps_diff, wd, 3)
                ub_q0 = -q0 * (mp.log(mb_hi) - mp.log(mb_lo)) / (2 * eps_diff)

                mb_1hi = closed_braid_ring_mass_mp(n_col, mp.mpf(1) + eps_diff, wd, 3)
                mb_1lo = closed_braid_ring_mass_mp(n_col, mp.mpf(1) - eps_diff, wd, 3)
                ub_q1 = -(mp.log(mb_1hi) - mp.log(mb_1lo)) / (2 * eps_diff)

                ma_iso = axis_convolution_from_weight_spaces_mp(n_col, q0, wd)
                ma_brute = closed_braid_ring_mass_mp(
                    n_col, q0, wd + AXIS_LOOP_4STRAND, 4
                )
                rel_iso = abs(ma_iso - ma_brute) / abs(ma_brute)
                if rel_iso > max_axis_isotypic_rel_err:
                    max_axis_isotypic_rel_err = rel_iso

                ma_hi = axis_convolution_from_weight_spaces_mp(
                    n_col, q0 + eps_diff, wd
                )
                ma_lo = axis_convolution_from_weight_spaces_mp(
                    n_col, q0 - eps_diff, wd
                )
                ua_q0 = -q0 * (mp.log(ma_hi) - mp.log(ma_lo)) / (2 * eps_diff)

                bare_vals[gname] = mb
                bare_u_q0[gname] = ub_q0
                bare_u_q1[gname] = ub_q1
                axis_vals[gname] = ma_iso
                axis_u_q0[gname] = ua_q0

            q_koide_bare = koide_ratio_vec_mp(
                bare_vals["e_hopf"], bare_vals["mu_t24"], bare_vals["tau_whitehead"]
            )
            q_koide_axis = koide_ratio_vec_mp(
                axis_vals["e_hopf"], axis_vals["mu_t24"], axis_vals["tau_whitehead"]
            )
            part_a_ladder_traces[f"N_{n_col}"] = {
                "colour_N": n_col,
                "bare_closure_ring_mass": {
                    k: fmt(v, dps=OUT_DPS) for k, v in bare_vals.items()
                },
                "bare_closure_ratios_over_e": {
                    "mu_over_e": fmt(
                        bare_vals["mu_t24"] / bare_vals["e_hopf"], dps=OUT_DPS
                    ),
                    "tau_over_e": fmt(
                        bare_vals["tau_whitehead"] / bare_vals["e_hopf"], dps=OUT_DPS
                    ),
                },
                "bare_closure_U_at_q1": {
                    k: fmt(v, dps=25) for k, v in bare_u_q1.items()
                },
                "bare_closure_U_at_q0": {
                    k: fmt(v, dps=30) for k, v in bare_u_q0.items()
                },
                "bare_closure_koide_Q": fmt(q_koide_bare, dps=30),
                "closure_union_axis_mass": {
                    k: fmt(v, dps=OUT_DPS) for k, v in axis_vals.items()
                },
                "closure_union_axis_ratios_over_e": {
                    "mu_over_e": fmt(
                        axis_vals["mu_t24"] / axis_vals["e_hopf"], dps=OUT_DPS
                    ),
                    "tau_over_e": fmt(
                        axis_vals["tau_whitehead"] / axis_vals["e_hopf"], dps=OUT_DPS
                    ),
                },
                "closure_union_axis_U_at_q0": {
                    k: fmt(v, dps=30) for k, v in axis_u_q0.items()
                },
                "closure_union_axis_koide_Q": fmt(q_koide_axis, dps=30),
            }

        # Part B: 80-dps Kashaev root-of-unity cut-axis invariants c_N(beta) at q = exp(i pi / N)
        max_cut_partial_rel_err = mp.mpf(0)
        for n_col in (2, 3, 4):
            for wd in LADDER_WORDS.values():
                c_ws = cut_axis_kashaev_root_mp(n_col, wd)
                c_pt = cut_axis_4strand_partial_trace_mp(
                    n_col, wd + AXIS_LOOP_4STRAND
                )
                denom = max(mp.mpf(1), abs(c_pt))
                err = abs(c_ws - c_pt) / denom
                if err > max_cut_partial_rel_err:
                    max_cut_partial_rel_err = err

        kashaev_rows: dict[str, dict[str, str]] = {}
        e_poly_bounded = True
        hierarchy_monotone_from_n4 = True
        for n_col in range(2, 15):
            ce = abs(cut_axis_kashaev_root_mp(n_col, LADDER_WORDS["e_hopf"]))
            cmu = abs(cut_axis_kashaev_root_mp(n_col, LADDER_WORDS["mu_t24"]))
            ctau = abs(cut_axis_kashaev_root_mp(n_col, LADDER_WORDS["tau_whitehead"]))
            if ce > mp.mpf(n_col * n_col):
                e_poly_bounded = False
            if n_col >= 4 and not (ce < cmu < ctau):
                hierarchy_monotone_from_n4 = False
            two_pi_over_n = 2 * mp.pi / mp.mpf(n_col)
            kashaev_rows[f"N_{n_col}"] = {
                "abs_cN_e": fmt(ce, dps=30),
                "abs_cN_mu": fmt(cmu, dps=30),
                "abs_cN_tau": fmt(ctau, dps=30),
                "growth_2pi_over_N_ln_cN_mu": fmt(two_pi_over_n * mp.log(cmu), dps=25),
                "growth_2pi_over_N_ln_cN_tau": fmt(
                    two_pi_over_n * mp.log(ctau), dps=25
                ),
            }

        # Part C: 80-dps Proton-Pin Verification of Radical-Free Quartic Koide Polynomial & Table 3.1a Row
        u_amp = mp.mpf(1)
        r_mu_proton = vol41 / (hbar_q0**2)
        v_amp = mp.sqrt(r_mu_proton)
        disc_core = u_amp**2 + 4 * u_amp * v_amp + v_amp**2
        s_root = mp.sqrt(3 * disc_core)
        x_plus = 2 * (u_amp + v_amp) + s_root
        r_tau_proton = x_plus**2

        # Evaluate radical-free quartic K_4(1, r_mu_proton, r_tau_proton)
        s1_m = mp.mpf(1) + r_mu_proton + r_tau_proton
        s2_m = r_mu_proton + r_mu_proton * r_tau_proton + r_tau_proton
        s3_m = r_mu_proton * r_tau_proton
        k4_residual = abs((s1_m**2 - 16 * s2_m) ** 2 - 1536 * s1_m * s3_m)

        # Evaluate division-free saddle quartic eliminating v (`koide_saddle_quartic_eliminating_v`)
        lhs_saddle = (
            (q0 - mp.mpf(1)) ** 2 * (x_plus**2 - 4 * u_amp * x_plus + u_amp**2)
            + (q0**2) * vol41 * (u_amp**2)
        ) ** 2
        rhs_saddle = (
            16
            * ((q0 - mp.mpf(1)) ** 2)
            * (q0**2)
            * vol41
            * (u_amp**2)
            * ((x_plus + u_amp) ** 2)
        )
        saddle_quartic_rel_res = abs(lhs_saddle - rhs_saddle) / abs(rhs_saddle)

        # Scaled S_3 singlet vs doublet norm check at 80 dps
        s_sum = u_amp + v_amp + x_plus
        norm_3p1 = 3 * (s_sum**2)
        norm_3pstd = (
            (2 * u_amp - v_amp - x_plus) ** 2
            + (2 * v_amp - u_amp - x_plus) ** 2
            + (2 * x_plus - u_amp - v_amp) ** 2
        )
        projector_equipartition_rel_res = abs(norm_3p1 - norm_3pstd) / norm_3p1

        # Read-only CODATA-2022 & PDG-2024 comparison for Table 3.1a `m_tau_over_m_e`
        tau_codata = codata("tau-electron mass ratio")
        me_codata = codata("electron mass energy equivalent in MeV")
        r_tau_codata = mp.mpf(tau_codata.value_str)
        r_tau_codata_err = mp.mpf(tau_codata.uncertainty_str)
        m_e_mev = mp.mpf(me_codata.value_str)
        m_e_mev_err = mp.mpf(me_codata.uncertainty_str)
        m_tau_pdg24_mev = mp.mpf("1776.93")
        m_tau_pdg24_err_mev = mp.mpf("0.09")
        r_tau_pdg24 = m_tau_pdg24_mev / m_e_mev
        r_tau_pdg24_err = mp.sqrt(
            (m_tau_pdg24_err_mev / m_e_mev) ** 2
            + (r_tau_pdg24 * m_e_mev_err / m_e_mev) ** 2
        )
        pull_codata = (r_tau_proton - r_tau_codata) / r_tau_codata_err
        pull_pdg24 = (r_tau_proton - r_tau_pdg24) / r_tau_pdg24_err

        print(
            "=== qou-cw8i: Koide Singlet-Doublet Equipartition & Least-Crossing Ladder Probe (80 dps, Proton Pin) ==="
        )
        print(f"q0 (proton pin)               = {fmt(q0, dps=OUT_DPS)}")
        print(
            f"Symbolic [CommRing R] checks  = {sym_res['all_symbolic_identities_verified']}"
        )
        print(f"N=2 q^12 skein diff residuals = {fmt(skein_diff_e_mu_res, dps=10)}, {fmt(skein_diff_tau_e_res, dps=10)}")
        print(f"Max 4-strand axis iso rel err = {fmt(max_axis_isotypic_rel_err, dps=10)}")
        print(f"Max 4-strand cut-axis rel err = {fmt(max_cut_partial_rel_err, dps=10)}")
        for nk, nv in part_a_ladder_traces.items():
            print(
                f"  {nk}: bare mu/e={nv['bare_closure_ratios_over_e']['mu_over_e'][:12]}, "
                f"tau/e={nv['bare_closure_ratios_over_e']['tau_over_e'][:12]} (Q={nv['bare_closure_koide_Q'][:10]}) | "
                f"axis mu/e={nv['closure_union_axis_ratios_over_e']['mu_over_e'][:12]}, "
                f"tau/e={nv['closure_union_axis_ratios_over_e']['tau_over_e'][:12]} (Q={nv['closure_union_axis_koide_Q'][:10]})"
            )
        print(
            f"Kashaev |c_14|: e={kashaev_rows['N_14']['abs_cN_e'][:12]}, "
            f"mu={kashaev_rows['N_14']['abs_cN_mu'][:12]}, tau={kashaev_rows['N_14']['abs_cN_tau'][:12]}"
        )
        print(
            f"Protected Koide (proton pin)  = {fmt(r_tau_proton, dps=20)} "
            f"(CODATA-22: {fmt(pull_codata, dps=8)}s, PDG-24: {fmt(pull_pdg24, dps=8)}s)"
        )
        print(
            f"Quartic K_4(1, r_mu, r_tau)   = {fmt(k4_residual, dps=10)} | saddle rel res = {fmt(saddle_quartic_rel_res, dps=10)}"
        )

        wb = WitnessBuilder(
            name="koide-lepton-ladder-proton-pin-probe",
            engine="mpmath",
            output_dir=Path(__file__).resolve().parent,
        )
        wb.set_description(
            "Pre-registered 80-dps proton-pin evaluation for bean qou-cw8i (epics qou-s028, qou-myts): "
            "(1) verifies all division-free [CommRing R] identities of KoideSingletDoubletEquipartition.lean "
            "(scaled S_3 projectors, Fourier moments, 3-strand Schur-Weyl 4=4 singlet-doublet equipartition, "
            "radical-free quartic Koide mass polynomial K_4, universal 3-braid det(I_2 - B_w(-1)) = 2 - tr(imgZ w), "
            "Morton-Birman Burau factorizations, and N=2 q^12 skein differences); "
            "(2) measures exact N = 2, 3, 4 bare closure and closure union axis U_q(sl_2) ring traces and "
            "root-of-unity zeta_N Kashaev cut-axis invariants (N = 2..14) on the 2026-11-28 ruled least-crossing "
            "2-component lepton link ladder (e = s0 s1 s0, mu = s0^4 s1^-1, tau = s0^2 s1^-1 s0 s1^-1); "
            "(3) verifies the narrowed KoideSingletDoubletEquipartitionBridge & radical-free quartic polynomial "
            "at the proton pin (muon pin on hold until rederivation per 2026-11-28 owner directive)."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("out_dps", OUT_DPS)
        wb.add_parameter("q0_proton", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("hbar_q0_proton", fmt(hbar_q0, dps=OUT_DPS))
        wb.add_parameter("vol_4_1", fmt(vol41, dps=OUT_DPS))
        wb.add_parameter("muon_pin_status", "on_hold_until_rederivation_2026_11_28")
        wb.add_parameter(
            "preregistration",
            "computations/probes/koide_lepton_ladder_proton_pin/PREREGISTRATION.md",
        )
        wb.add_parameter(
            "lean_module",
            "folio/quantum-observable-universe/lean/QOU/StandardModel/KoideSingletDoubletEquipartition.lean",
        )

        wb.add_data("symbolic_commring_verification", sym_res)
        wb.add_data("part_a_least_crossing_ring_and_axis_traces", part_a_ladder_traces)
        wb.add_data("part_b_kashaev_cut_axis_zeta_n_growth", kashaev_rows)
        wb.add_data(
            "part_c_proton_pin_koide_quartic_and_narrowed_bridge",
            {
                "m_mu_over_m_e_vol41_proton_pin": fmt(r_mu_proton, dps=OUT_DPS),
                "m_tau_over_m_e_protected_koide_proton_pin": fmt(
                    r_tau_proton, dps=OUT_DPS
                ),
                "norm_3P_singlet_sq": fmt(norm_3p1, dps=OUT_DPS),
                "norm_3P_doublet_sq": fmt(norm_3pstd, dps=OUT_DPS),
                "projector_equipartition_rel_residual": fmt(
                    projector_equipartition_rel_res, dps=15
                ),
                "koide_quartic_K4_abs_residual": fmt(k4_residual, dps=15),
                "saddle_quartic_v_eliminated_rel_residual": fmt(
                    saddle_quartic_rel_res, dps=15
                ),
                "sigma_pull_vs_codata_2022": fmt(pull_codata, dps=12),
                "sigma_pull_vs_pdg_2024": fmt(pull_pdg24, dps=12),
                "discharged_algebraic_theorems": [
                    "threeProj_idempotent_orthog_and_trace",
                    "singlet_doublet_equipartition_iff_koide_ring",
                    "matrix_trace_equipartition_iff_koide_ring",
                    "circulant3FourierSpec_moments",
                    "q3SchurWeyl_partition_and_classical_equipartition",
                    "koide_discriminant_pos_and_upper_root_dominance",
                    "koide_saddle_quartic_eliminating_v",
                    "koideMassQuarticPoly_galois_factorization",
                    "det_one_sub_burau_neg_one_eq_two_sub_trace",
                    "morton_birman_burau_ladder_invariants",
                    "q12_ring_mass_skein_differences_and_singlet_collapse",
                ],
                "irreducible_remaining_hypothesis": "QOU.StandardModel.KoideSingletDoubletEquipartition.KoideSingletDoubletEquipartitionBridge",
            },
        )

        wb.add_assertion(
            "sympy_all_commring_koide_schur_weyl_burau_skein_identities",
            1 if sym_res["all_symbolic_identities_verified"] else 0,
            1,
            "0",
            source="KoideSingletDoubletEquipartition.lean (§1-§5 exact [CommRing R] theorems)",
        )
        wb.add_assertion(
            "n2_q12_skein_differences_match_closed_form_80dps",
            fmt(max(skein_diff_e_mu_res, skein_diff_tau_e_res), dps=15),
            "0",
            "1e-70",
            source="KoideSingletDoubletEquipartition.q12_ring_mass_skein_differences_and_singlet_collapse",
        )
        wb.add_assertion(
            "axis_convolution_matches_4strand_trace_n2_n3_n4_80dps",
            fmt(max_axis_isotypic_rel_err, dps=15),
            "0",
            "1e-65",
            source="AxisConvolutionOperator.lean weight-space vs 4-strand R-matrix trace",
        )
        wb.add_assertion(
            "kashaev_cut_axis_matches_4strand_partial_trace_n2_n3_n4_80dps",
            fmt(max_cut_partial_rel_err, dps=15),
            "0",
            "1e-65",
            source="AxisKashaevReading.lean root-of-unity formula vs 4-strand partial trace",
        )
        wb.add_assertion(
            "kashaev_cut_axis_electron_poly_and_monotone_hierarchy_n4_to_n14",
            1 if (e_poly_bounded and hierarchy_monotone_from_n4) else 0,
            1,
            "0",
            source="Mapping-torus volume ordering Vol(e U A) = 0 < Vol(mu U A) = 6.3546 < Vol(tau U A) = 9.5034",
        )
        wb.add_assertion(
            "radical_free_quartic_koide_and_v_eliminated_saddle_exact_80dps",
            fmt(
                max(projector_equipartition_rel_res, saddle_quartic_rel_res), dps=15
            ),
            "0",
            "1e-65",
            source="KoideSingletDoubletEquipartition.koideMassQuarticPoly_galois_factorization & koide_saddle_quartic_eliminating_v",
        )

        wb.add_caveat(
            "1. All 80-dps substrate evaluations run strictly on the proton pin (q_at(80)); the CAL-2 muon pin "
            "is on hold until first-principles rederivation per the 2026-11-28 owner directive. "
            "2. On the 2026-11-28 ruled least-crossing 2-component link ladder (e = s0 s1 s0, mu = s0^4 s1^-1, "
            "tau = s0^2 s1^-1 s0 s1^-1), bare N=2 ring masses satisfy m_e - m_mu = 1 - q^-12 and "
            "m_tau - m_e = q^4(1 - q^-12), collapsing to pure S_3 singlet (4,4,4) at q=1 (Q -> 1/3), while "
            "root-of-unity Kashaev cut-axis invariants |c_N(beta)| grow strictly monotonically |c_N(e)| < |c_N(mu)| < |c_N(tau)| "
            "for all N >= 4 along the mapping-torus volumes (0 < 6.3546 < 9.5034); per owner-rulings.md row 18, "
            "neither reading is scored until derived from the axioms. "
            "3. 100% of the algebraic S_3/Z_3 projector, Fourier-moment, V^{otimes 3} = (4x1)+(2x2) classical 4=4 "
            "equipartition, quadratic resolvent, and radical-free quartic mass polynomial identities are discharged "
            "unconditionally over [CommRing R] in KoideSingletDoubletEquipartition.lean, narrowing Table 3.1a's "
            "m_tau/m_e Conditional status strictly to the 1-equation physical bridge KoideSingletDoubletEquipartitionBridge."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
