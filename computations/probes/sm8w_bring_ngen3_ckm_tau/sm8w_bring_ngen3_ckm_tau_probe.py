#!/usr/bin/env python3
"""Standard Model Package 1 (`qou-gen3` / `Q-Gap-7`):
Bring Curve N_gen=3 Zero-Mode Branching, S_3 ⊂ S_5 CKM/PMNS Overlap Textures,
and Satellite T(2,7)–4_1 Tau Mass Candidates at 80 dps.

Pre-registered in `PREREGISTRATION.md` (commit b79c58b664d) BEFORE writing or
executing this numerical probe. Companion sorry-free Lean 4 module:
`folio/quantum-observable-universe/lean/QOU/StandardModel/BringGenerationSplitAndCKMTexture.lean`.

STRICT PRECISION & ANTI-FIT DISCIPLINE:
- `mpmath` at `workdps = 80` throughout; ZERO `float64`, ZERO `math`/`numpy`.
- `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`).
- Experimental constants (PDG-2024 CKM/PMNS, CODATA-2022 `m_tau/m_e`) enter
  strictly as downstream comparison targets, NEVER as calibration inputs.
- All pre-declared candidate formulas are reported with exact residuals, hits
  and misses alike (`selected = "none"`, scope-(a) exploratory probe).
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _rel in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    _p = str(_ROOT / _rel)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from mpmath import mp  # noqa: E402

WORK_DPS = 80
OUT_DIGITS = 50
mp.dps = WORK_DPS

from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

T0 = time.time()
T0_NS = time.monotonic_ns()
ASSERTS: list[dict[str, object]] = []
FAILED: list[str] = []


def log(msg: str) -> None:
    cs = (time.monotonic_ns() - T0_NS) // 10_000_000
    print(f"[{cs // 100:3d}.{cs % 100:02d}s] {msg}", flush=True)


def check(name: str, ok: bool, computed_str: str, expected_str: str, tol_str: str, source: str) -> None:
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {name}: computed={computed_str} (expected={expected_str}, tol={tol_str}) -- {source}", flush=True)
    ASSERTS.append({
        "name": name,
        "ok": bool(ok),
        "computed": computed_str,
        "expected": expected_str,
        "tolerance": tol_str,
        "source": source,
    })
    if not ok:
        FAILED.append(name)


def nstr50(x) -> str:
    return mp.nstr(x, OUT_DIGITS)


def nstr80(x) -> str:
    return mp.nstr(x, WORK_DPS)


# ── Exact finite-group permutation helpers (pure Python ints) ───────────────

def cycle_type_s5(perm: tuple[int, ...]) -> tuple[int, ...]:
    visited = [False] * len(perm)
    lengths = []
    for i in range(len(perm)):
        if not visited[i]:
            cur = i
            ln = 0
            while not visited[cur]:
                visited[cur] = True
                cur = perm[cur]
                ln += 1
            lengths.append(ln)
    return tuple(sorted(lengths, reverse=True))


# ── Complex 3x3 & Hermitian linear algebra at 80 dps in pure mpmath ─────────

def mat_dagger(M):
    r, c = M.rows, M.cols
    out = mp.matrix(c, r)
    for i in range(r):
        for j in range(c):
            out[j, i] = mp.conj(M[i, j])
    return out


def mat_inf_norm(M):
    best = mp.mpf(0)
    for i in range(M.rows):
        for j in range(M.cols):
            val = abs(M[i, j])
            if val > best:
                best = val
    return best


def jarlskog_from_mat(V):
    return mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))


def jarlskog_alt_plaquette(V):
    return mp.im(V[0, 0] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 0]))


def chau_keung_matrix(s12, s23, s13, delta):
    c12 = mp.sqrt(mp.mpf(1) - s12 ** 2)
    c23 = mp.sqrt(mp.mpf(1) - s23 ** 2)
    c13 = mp.sqrt(mp.mpf(1) - s13 ** 2)
    ep = mp.exp(mp.mpc(0, 1) * delta)
    em = mp.exp(mp.mpc(0, -1) * delta)
    R23 = mp.matrix([
        [mp.mpf(1), mp.mpf(0), mp.mpf(0)],
        [mp.mpf(0), c23, s23],
        [mp.mpf(0), -s23, c23],
    ])
    U13 = mp.matrix([
        [c13, mp.mpf(0), s13 * em],
        [mp.mpf(0), mp.mpf(1), mp.mpf(0)],
        [-s13 * ep, mp.mpf(0), c13],
    ])
    R12 = mp.matrix([
        [c12, s12, mp.mpf(0)],
        [-s12, c12, mp.mpf(0)],
        [mp.mpf(0), mp.mpf(0), mp.mpf(1)],
    ])
    return R23 * U13 * R12


def hermitian_eigh_80dps(H):
    """Exact 80-dps Hermitian eigendecomposition via real-block embedding `mp.eigsy`.

    For n x n Hermitian H = A + i B (A^T = A, B^T = -B), the 2n x 2n real
    symmetric matrix [[A, -B], [B, A]] has doubled real eigenvalues; if (u, v)
    is a unit eigenvector for lambda, u + i v is a unit eigenvector of H, and
    (-v, u) is its i-rotated partner spanning the same complex line.
    """
    n = H.rows
    R2 = mp.matrix(2 * n, 2 * n)
    for i in range(n):
        for j in range(n):
            a = mp.re(H[i, j])
            b = mp.im(H[i, j])
            R2[i, j] = a
            R2[i, j + n] = -b
            R2[i + n, j] = b
            R2[i + n, j + n] = a
    evals2, evecs2 = mp.eigsy(R2)
    pairs = sorted(range(2 * n), key=lambda k: evals2[k])
    chosen_vals = []
    chosen_vecs = []
    tol = mp.mpf("1e-50")
    for idx in pairs:
        vec = mp.matrix(n, 1)
        for i in range(n):
            vec[i, 0] = mp.mpc(evecs2[i, idx], evecs2[i + n, idx])
        # Project out already-chosen complex eigenvectors (Gram-Schmidt)
        for prev in chosen_vecs:
            ip = mp.mpc(0, 0)
            for i in range(n):
                ip += mp.conj(prev[i, 0]) * vec[i, 0]
            for i in range(n):
                vec[i, 0] -= ip * prev[i, 0]
        nrm = mp.sqrt(mp.fsum(abs(vec[i, 0]) ** 2 for i in range(n)))
        if nrm > tol:
            for i in range(n):
                vec[i, 0] /= nrm
            chosen_vals.append(evals2[idx])
            chosen_vecs.append(vec)
        if len(chosen_vecs) == n:
            break
    U = mp.matrix(n, n)
    for col, vec in enumerate(chosen_vecs):
        for i in range(n):
            U[i, col] = vec[i, 0]
    return chosen_vals, U


# ── Exact 80-dps Hoefsmit Two-Row Representations of H_n(q) ─────────────────

def standard_young_tableaux(shape: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """All standard Young tableaux of `shape` with entries 1..n."""
    n = sum(shape)
    rows = len(shape)

    def backtrack(partial: list[list[int]], val: int):
        if val > n:
            yield tuple(tuple(r) for r in partial)
            return
        for r in range(rows):
            c = len(partial[r])
            if c < shape[r]:
                if r == 0 or c < len(partial[r - 1]):
                    partial[r].append(val)
                    yield from backtrack(partial, val + 1)
                    partial[r].pop()

    return list(backtrack([[] for _ in range(rows)], 1))


def syt_contents(syt: tuple[tuple[int, ...], ...], n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for r, row in enumerate(syt):
        for c, val in enumerate(row):
            out[val] = c - r
    return out


def syt_swap(syt: tuple[tuple[int, ...], ...], a: int, b: int) -> tuple[tuple[int, ...], ...]:
    res = []
    for row in syt:
        new_row = []
        for v in row:
            if v == a:
                new_row.append(b)
            elif v == b:
                new_row.append(a)
            else:
                new_row.append(v)
        res.append(tuple(new_row))
    return tuple(res)


def q_int_sym(q, m: int):
    if m == 0:
        return mp.mpf(0)
    return (q ** m - q ** (-m)) / (q - mp.mpf(1) / q)


def hoefsmit_generators_80dps(shape: tuple[int, ...], q):
    """Exact 80-dps orthogonal Hoefsmit matrices T_1..T_{n-1} for (T_i - q)(T_i + q^-1) = 0."""
    n = sum(shape)
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    idx_map = {t: idx for idx, t in enumerate(syts)}
    contents = [syt_contents(t, n) for t in syts]
    gens = {}
    for i in range(1, n):
        M = mp.matrix(dim, dim)
        visited = set()
        for u_idx, t in enumerate(syts):
            if u_idx in visited:
                continue
            d = contents[u_idx][i + 1] - contents[u_idx][i]
            if d == 1:
                M[u_idx, u_idx] = q
                visited.add(u_idx)
            elif d == -1:
                M[u_idx, u_idx] = -mp.mpf(1) / q
                visited.add(u_idx)
            else:
                t_sw = syt_swap(t, i, i + 1)
                v_idx = idx_map[t_sw]
                visited.add(u_idx)
                visited.add(v_idx)
                # Ensure pos_idx has positive axial distance d_pos >= 2
                if d > 0:
                    pos_idx, neg_idx, d_pos = u_idx, v_idx, d
                else:
                    pos_idx, neg_idx, d_pos = v_idx, u_idx, -d
                qd = q_int_sym(q, d_pos)
                diag_neg = -(q ** (-d_pos)) / qd
                diag_pos = (q ** d_pos) / qd
                off = mp.sqrt(q_int_sym(q, d_pos - 1) * q_int_sym(q, d_pos + 1)) / qd
                M[pos_idx, pos_idx] = diag_pos
                M[neg_idx, neg_idx] = diag_neg
                M[pos_idx, neg_idx] = off
                M[neg_idx, pos_idx] = off
        gens[i] = M
    # Also precompute inverses T_i^{-1} = T_i - (q - q^{-1}) I
    h = q - mp.mpf(1) / q
    invs = {}
    for i, M in gens.items():
        Minv = mp.matrix(dim, dim)
        for r in range(dim):
            for c in range(dim):
                Minv[r, c] = M[r, c] - (h if r == c else mp.mpf(0))
        invs[i] = Minv
    return dim, gens, invs


def cable2_word(word: list[int]) -> list[int]:
    """2-parallel cable homomorphism B_3 -> B_6 matching `CableShiftFourfold.cableBlock`."""
    out: list[int] = []
    for g in word:
        if g > 0:
            out.extend([2 * g, 2 * g - 1, 2 * g + 1, 2 * g])
        else:
            k = -g
            out.extend([-2 * k, -(2 * k + 1), -(2 * k - 1), -2 * k])
    return out


def eval_word_trace(word: list[int], dim: int, gens: dict, invs: dict):
    acc = mp.eye(dim)
    for letter in word:
        if letter > 0:
            acc = acc * gens[letter]
        else:
            acc = acc * invs[-letter]
    return mp.fsum(acc[i, i] for i in range(dim))


# ── Bloch-Wigner dilogarithm at 80 dps ──────────────────────────────────────

def bloch_wigner_d(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(mp.mpf(1) - z) * mp.log(abs(z))


def main() -> int:
    with mp.workdps(WORK_DPS):
        log("1. Proton-pinned substrate q0 & exact constants at 80 dps")
        q0 = mp.mpf(q_at(WORK_DPS))
        q0_inv = mp.mpf(1) / q0
        h = q0 - q0_inv
        hbar_q = mp.mpf(1) - q0_inv
        hbar_q2 = hbar_q ** 2
        hbar_q3 = hbar_q ** 3
        q2_sym = q_int_sym(q0, 2)
        q3_sym = q_int_sym(q0, 3)
        q5_sym = q_int_sym(q0, 5)
        q7_sym = q_int_sym(q0, 7)
        vol_4_1 = mp.mpf(2) * mp.clsin(2, mp.pi / mp.mpf(3))

        # Cross-check proton substrate fixed-point equation at 80 dps
        mp_me_entry = codata("proton-electron mass ratio")
        mu_me_entry = codata("muon-electron mass ratio")
        tau_me_entry = codata("tau-electron mass ratio")
        mp_me_codata = mp.mpf(mp_me_entry.value_str)
        mu_me_codata = mp.mpf(mu_me_entry.value_str)
        tau_me_codata = mp.mpf(tau_me_entry.value_str)
        tau_me_codata_err = mp.mpf(tau_me_entry.uncertainty_str)
        tau_me_belle2_pdg = mp.mpf("3477.228")
        tau_me_belle2_err = mp.mpf("0.023")

        tr_bor = abs((mp.mpf(4) + h ** 2 - mp.mpf(3) * h ** 4 - h ** 6) / (h ** 2 + mp.mpf(4)))
        mp_me_reconstructed = mp.mpf(2) * (vol_4_1 / hbar_q2) * (tr_bor * q2_sym * q3_sym / (q0 ** 3)) - mp.mpf(12)
        proton_pin_res = abs(mp_me_reconstructed - mp_me_codata)
        check(
            "proton_pin_80dps_roundtrip",
            proton_pin_res < mp.mpf("1e-70"),
            nstr50(proton_pin_res),
            "0",
            "1e-70",
            "q_at(80) solves proton Borromean substrate equation at 80 dps",
        )

        # ── Part (a1): S_5 ⊃ S_4 ⊃ S_3 & S_3 × S_2 Branching & Gram Overlaps ──
        log("2. S_5 ⊃ S_4 ⊃ S_3 and S_5 ⊃ S_3 × S_2 canonical differential branching")
        all_s5 = list(itertools.permutations(range(5)))
        s4_sub = [p for p in all_s5 if p[4] == 4]
        s3_sub = [p for p in all_s5 if p[3] == 3 and p[4] == 4]
        s3xs2_sub = [p for p in all_s5 if set(p[:3]) == {0, 1, 2}]

        def chi_std_perm(p: tuple[int, ...]) -> int:
            return sum(1 for i in range(5) if p[i] == i) - 1

        # Exact S_4 character inner products: <Res chi_std, chi_(3,1)> = 1, <Res chi_std, 1> = 1
        s4_triv_ip = sum(chi_std_perm(p) * 1 for p in s4_sub) // 24
        s4_std_ip = sum(chi_std_perm(p) * (sum(1 for i in range(4) if p[i] == i) - 1) for p in s4_sub) // 24
        s3_std_ip = sum(chi_std_perm(p) * (sum(1 for i in range(3) if p[i] == i) - 1) for p in s3_sub) // 6
        s3_triv_ip = sum(chi_std_perm(p) * 1 for p in s3_sub) // 6
        s3xs2_2_1_ip = sum(chi_std_perm(p) * (sum(1 for i in range(3) if p[i] == i) - 1) for p in s3xs2_sub) // 12
        s3xs2_1_triv_ip = sum(chi_std_perm(p) * 1 for p in s3xs2_sub) // 12
        s3xs2_1_sign_ip = sum(chi_std_perm(p) * (1 if p[3] == 3 else -1) for p in s3xs2_sub) // 12

        branch_ok = (
            len(all_s5) == 120
            and s4_std_ip == 1
            and s4_triv_ip == 1
            and s3_std_ip == 1
            and s3_triv_ip == 2
            and s3xs2_2_1_ip == 1
            and s3xs2_1_triv_ip == 1
            and s3xs2_1_sign_ip == 1
        )
        check(
            "s5_s4_s3_s3xs2_character_branching",
            branch_ok,
            f"S4:({s4_std_ip},{s4_triv_ip});S3:({s3_std_ip},{s3_triv_ip});S3xS2:({s3xs2_2_1_ip},{s3xs2_1_triv_ip},{s3xs2_1_sign_ip})",
            "S4:(1,1);S3:(1,2);S3xS2:(1,1,1)",
            "0",
            "Exact brute-force 120-element S_5 branching matches Lean theorems",
        )

        # Concrete projectors on V_std in 80-dps mpmath
        P_sing = mp.matrix(5, 5)
        vec_sing = [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(-4)]
        for i in range(5):
            P_sing[i, 4] = -vec_sing[i] / mp.mpf(4)
        P_gen3 = mp.eye(5) - P_sing
        P_dem1 = mp.matrix(5, 5)
        vec_dem = [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(-3), mp.mpf(0)]
        for i in range(5):
            P_dem1[i, 3] = -vec_dem[i] / mp.mpf(3)
        P_doublet2 = mp.eye(5) - P_dem1

        proj_err = (
            mat_inf_norm(P_sing * P_sing - P_sing)
            + mat_inf_norm(P_gen3 * P_gen3 - P_gen3)
            + mat_inf_norm(P_sing * P_gen3)
            + mat_inf_norm(P_gen3 * P_sing)
            + mat_inf_norm((P_doublet2 * P_gen3) * (P_doublet2 * P_gen3) - (P_doublet2 * P_gen3))
        )
        check(
            "v_std_idempotent_projectors_80dps",
            proj_err < mp.mpf("1e-75"),
            nstr50(proj_err),
            "0",
            "1e-75",
            "Exact idempotency and mutual annihilation of P_sing1, P_gen3, P_doublet2",
        )

        # Conjugate S_3 ⊂ S_4 fixed lines in V_gen3 and overlap with Z_5 Bloch modes
        tet_vecs = [
            [mp.mpf(-3), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(0)],
            [mp.mpf(1), mp.mpf(-3), mp.mpf(1), mp.mpf(1), mp.mpf(0)],
            [mp.mpf(1), mp.mpf(1), mp.mpf(-3), mp.mpf(1), mp.mpf(0)],
        ]
        tet_gram = mp.matrix(3, 3)
        for a in range(3):
            for b in range(3):
                tet_gram[a, b] = mp.fsum(tet_vecs[a][k] * tet_vecs[b][k] for k in range(5)) / mp.mpf(12)
        tet_cos_err = abs(tet_gram[0, 1] + mp.mpf(1) / mp.mpf(3))
        check(
            "conjugate_s3_in_s4_tetrahedral_gram",
            tet_cos_err < mp.mpf("1e-75"),
            nstr50(tet_gram[0, 1]),
            nstr50(-mp.mpf(1) / mp.mpf(3)),
            "1e-75",
            "Normalized overlap cosine of conjugate S_3 ⊂ S_4 fixed lines in V_gen3 is -1/3",
        )

        # Overlap of the 3 conjugate S_3 lines (3x5) against the first 3 non-trivial Z_5 weak T(3,5) Bloch modes (5x3)
        omega5 = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(5))
        O_s3_z5 = mp.matrix(3, 3)
        for a in range(3):
            for m_idx, k_mode in enumerate((1, 2, 3)):
                O_s3_z5[a, m_idx] = mp.fsum(
                    (tet_vecs[a][j] / mp.sqrt(mp.mpf(12))) * (omega5 ** (-k_mode * j)) / mp.sqrt(mp.mpf(5))
                    for j in range(5)
                )
        svals_sq, _ = hermitian_eigh_80dps(mat_dagger(O_s3_z5) * O_s3_z5)
        svals_s3_z5 = [mp.sqrt(max(mp.mpf(0), v)) for v in svals_sq]

        # Morgan-Voyce b_9 harmonic & Bezout coprimality check at h = q0 - q0^-1
        mv = [mp.mpf(0), mp.mpf(1)]
        for idx in range(2, 10):
            mv.append(h * mv[-1] + mv[-2])
        mv_harm_err = (
            abs(mv[9] - mv[3] * (h ** 6 + mp.mpf(6) * h ** 4 + mp.mpf(9) * h ** 2 + mp.mpf(1)))
            + abs(mv[3] * (h ** 2 + mp.mpf(2)) - mv[5] - mp.mpf(1))
            + abs(mv[3] * (h ** 4 + mp.mpf(4) * h ** 2 + mp.mpf(2)) - mv[7] - mp.mpf(1))
        )
        check(
            "morgan_voyce_b9_harmonic_and_bezout_80dps",
            mv_harm_err < mp.mpf("1e-70"),
            nstr50(mv_harm_err),
            "0",
            "1e-70",
            "b_9 = b_3(h^6+6h^4+9h^2+1) and Bezout coprimality of (b_3, b_5), (b_3, b_7)",
        )

        # Hoefsmit (2,1) crossing angle cos(theta_H) = 1 / [2]_q0
        cos_theta_h = mp.mpf(1) / q2_sym
        sin_theta_h = mp.sqrt(q3_sym) / q2_sym
        hoefsmit_unit_err = abs(cos_theta_h ** 2 + sin_theta_h ** 2 - mp.mpf(1))
        check(
            "hoefsmit_h3_doublet_angle_unitarity",
            hoefsmit_unit_err < mp.mpf("1e-75"),
            nstr50(hoefsmit_unit_err),
            "0",
            "1e-75",
            "cos^2(theta_H) + sin^2(theta_H) = (1 + [3]_q) / [2]_q^2 = 1",
        )

        # ── Part (a2): Parameter-Free CKM & PMNS Candidate Evaluations vs PDG-2024 ──
        log("3. Pre-registered CKM & PMNS candidates vs PDG-2024 (zero fitting)")
        pdg_ckm = {
            "V_us": (mp.mpf("0.2243"), mp.mpf("0.0008")),
            "V_cb": (mp.mpf("0.0422"), mp.mpf("0.0008")),
            "V_ub": (mp.mpf("0.00394"), mp.mpf("0.00036")),
            "J_CP": (mp.mpf("3.08e-5"), mp.mpf("0.15e-5")),
        }
        pdg_pmns = {
            "sin2_theta12": (mp.mpf("0.307"), mp.mpf("0.013")),
            "sin2_theta23": (mp.mpf("0.546"), mp.mpf("0.021")),
            "sin2_theta13": (mp.mpf("0.0220"), mp.mpf("0.0007")),
        }

        def score_ckm(label: str, V, rationale: str) -> dict[str, object]:
            unit_res = mat_inf_norm(mat_dagger(V) * V - mp.eye(3))
            j_val = jarlskog_from_mat(V)
            j_alt = jarlskog_alt_plaquette(V)
            plaq_res = abs(j_val + j_alt)
            vus = abs(V[0, 1])
            vcb = abs(V[1, 2])
            vub = abs(V[0, 2])
            obs = {"V_us": vus, "V_cb": vcb, "V_ub": vub, "J_CP": abs(j_val)}
            comp = {}
            for k, val in obs.items():
                tgt, err = pdg_ckm[k]
                rel_pct = (val - tgt) / tgt * mp.mpf(100)
                pull_sigma = (val - tgt) / err
                comp[k] = {
                    "computed": nstr50(val),
                    "pdg2024": nstr50(tgt),
                    "pdg2024_err": nstr50(err),
                    "signed_rel_err_pct": mp.nstr(rel_pct, 12),
                    "pull_sigma": mp.nstr(pull_sigma, 10),
                }
            return {
                "candidate": label,
                "rationale": rationale,
                "unitarity_residual": nstr50(unit_res),
                "plaquette_antisymmetry_residual": nstr50(plaq_res),
                "signed_J_CP": nstr50(j_val),
                "comparison_vs_pdg2024": comp,
            }

        # CKM-C0: Unperturbed S_3 identity
        V_c0 = mp.eye(3)
        # CKM-C1a: Hecke hierarchy sin(theta_12)=h, sin(theta_23)=h^2, sin(theta_13)=h^3/[3]_q, delta=2*pi/5
        V_c1a = chau_keung_matrix(h, h ** 2, (h ** 3) / q3_sym, mp.mpf(2) * mp.pi / mp.mpf(5))
        # CKM-C1b: Same angles with S_3 Weyl phase delta=pi/3
        V_c1b = chau_keung_matrix(h, h ** 2, (h ** 3) / q3_sym, mp.pi / mp.mpf(3))

        # CKM-C2: Explicit Hermitian democratic + Hecke-perturbed Yukawa overlap V = U_u^H U_d in Jacobi basis
        Yu = mp.matrix([
            [mp.mpf(0), mp.mpf(0), mp.mpf(0)],
            [mp.mpf(0), h ** 2, mp.mpf(0)],
            [mp.mpf(0), mp.mpf(0), q3_sym],
        ])
        ph_z5 = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(5))
        Yd = mp.matrix([
            [mp.mpf(0), (h ** 2) * ph_z5, mp.mpf(0)],
            [(h ** 2) * mp.conj(ph_z5), h, (h ** 2) * q3_sym],
            [mp.mpf(0), (h ** 2) * q3_sym, q3_sym],
        ])
        evals_u, Uu = hermitian_eigh_80dps(Yu)
        evals_d, Ud = hermitian_eigh_80dps(Yd)
        # Reconstruct Yd = Ud * diag(evals_d) * Ud^H to verify 80-dps eigensolver
        D_d = mp.matrix(3, 3)
        for idx in range(3):
            D_d[idx, idx] = evals_d[idx]
        yd_eig_res = mat_inf_norm(Ud * D_d * mat_dagger(Ud) - Yd) + mat_inf_norm(mat_dagger(Ud) * Ud - mp.eye(3))
        check(
            "ckm_c2_hermitian_eigensolver_80dps",
            yd_eig_res < mp.mpf("1e-70"),
            nstr50(yd_eig_res),
            "0",
            "1e-70",
            "80-dps Hermitian eigendecomposition reconstructs Y_d and unitarity to < 1e-70",
        )
        V_c2 = mat_dagger(Uu) * Ud

        ckm_rows = [
            score_ckm("CKM-C0_unperturbed_identity", V_c0, "Unbroken S_3 alignment V = I_3 (baseline miss)"),
            score_ckm(
                "CKM-C1a_hecke_hierarchy_z5_phase",
                V_c1a,
                "sin(theta_12)=h, sin(theta_23)=h^2, sin(theta_13)=h^3/[3]_q0, delta=2*pi/5 (Bring Z_5 phase)",
            ),
            score_ckm(
                "CKM-C1b_hecke_hierarchy_s3_phase",
                V_c1b,
                "sin(theta_12)=h, sin(theta_23)=h^2, sin(theta_13)=h^3/[3]_q0, delta=pi/3 (S_3 Weyl phase)",
            ),
            score_ckm(
                "CKM-C2_democratic_yukawa_svd_overlap",
                V_c2,
                "V = U_u^H U_d from Jacobi-basis Hermitian Yukawas Y_u = diag(0,h^2,[3]_q0) and Hecke-perturbed Y_d",
            ),
        ]

        # Verify unitarity and plaquette identity across all 4 CKM matrices
        ckm_alg_err = max(
            mp.mpf(r["unitarity_residual"]) + mp.mpf(r["plaquette_antisymmetry_residual"])
            for r in ckm_rows
        )
        check(
            "ckm_unitarity_and_jarlskog_plaquette_80dps",
            ckm_alg_err < mp.mpf("1e-70"),
            nstr50(ckm_alg_err),
            "0",
            "1e-70",
            "All CKM candidate matrices satisfy V^H V = I_3 and J_{us,cb} = -J_{ud,cb} to < 1e-70",
        )

        # CKM-C3: Two-generation Cabibbo perturbation formulas comparison
        # (1) tan(2*theta_12) = 2*h / [3]_q0  (Lean `cabibbo_hecke_qThree_relation`)
        theta_c3_q3 = mp.atan(mp.mpf(2) * h / q3_sym) / mp.mpf(2)
        sin_c3_q3 = mp.sin(theta_c3_q3)
        cabibbo_lean_id_err = abs(
            (q3_sym ** 2 + mp.mpf(4) * h ** 2) * (mp.sin(mp.mpf(2) * theta_c3_q3) ** 2)
            - mp.mpf(4) * h ** 2
        )
        check(
            "cabibbo_two_gen_lean_identity_80dps",
            cabibbo_lean_id_err < mp.mpf("1e-75"),
            nstr50(cabibbo_lean_id_err),
            "0",
            "1e-75",
            "([3]_q0^2 + 4 h^2) sin^2(2 theta_12) = 4 h^2 matches Lean `cabibbo_hecke_qThree_relation`",
        )
        sin_c3_tanh = h / mp.sqrt(mp.mpf(1) + h ** 2)
        sin_c3_div_sqrt3q = h / mp.sqrt(q3_sym)
        ckm_c3_table = {
            "tan2theta_eq_2h_over_q3": {
                "sin_theta12": nstr50(sin_c3_q3),
                "rel_err_vs_Vus_pct": mp.nstr((sin_c3_q3 - pdg_ckm["V_us"][0]) / pdg_ckm["V_us"][0] * mp.mpf(100), 10),
            },
            "tantheta_eq_h": {
                "sin_theta12": nstr50(sin_c3_tanh),
                "rel_err_vs_Vus_pct": mp.nstr((sin_c3_tanh - pdg_ckm["V_us"][0]) / pdg_ckm["V_us"][0] * mp.mpf(100), 10),
            },
            "sintheta_eq_h": {
                "sin_theta12": nstr50(h),
                "rel_err_vs_Vus_pct": mp.nstr((h - pdg_ckm["V_us"][0]) / pdg_ckm["V_us"][0] * mp.mpf(100), 10),
            },
            "sintheta_eq_h_over_sqrt_q3": {
                "sin_theta12": nstr50(sin_c3_div_sqrt3q),
                "rel_err_vs_Vus_pct": mp.nstr((sin_c3_div_sqrt3q - pdg_ckm["V_us"][0]) / pdg_ckm["V_us"][0] * mp.mpf(100), 10),
            },
        }

        # PMNS candidates: U_TBM and U_e(arcsin h, delta)^H * U_TBM
        s2 = mp.sqrt(mp.mpf(2))
        s3 = mp.sqrt(mp.mpf(3))
        s6 = s2 * s3
        U_tbm = mp.matrix([
            [mp.mpf(2) / s6, mp.mpf(1) / s3, mp.mpf(0)],
            [-mp.mpf(1) / s6, mp.mpf(1) / s3, -mp.mpf(1) / s2],
            [-mp.mpf(1) / s6, mp.mpf(1) / s3, mp.mpf(1) / s2],
        ])

        def charged_lepton_rot12(sin_th, delta):
            cos_th = mp.sqrt(mp.mpf(1) - sin_th ** 2)
            ep = mp.exp(mp.mpc(0, 1) * delta)
            em = mp.exp(mp.mpc(0, -1) * delta)
            return mp.matrix([
                [cos_th, sin_th * em, mp.mpf(0)],
                [-sin_th * ep, cos_th, mp.mpf(0)],
                [mp.mpf(0), mp.mpf(0), mp.mpf(1)],
            ])

        def score_pmns(label: str, U, rationale: str) -> dict[str, object]:
            unit_res = mat_inf_norm(mat_dagger(U) * U - mp.eye(3))
            s2_13 = abs(U[0, 2]) ** 2
            c2_13 = mp.mpf(1) - s2_13
            s2_12 = (abs(U[0, 1]) ** 2) / c2_13
            s2_23 = (abs(U[1, 2]) ** 2) / c2_13
            j_pmns = jarlskog_from_mat(U)
            obs = {
                "sin2_theta12": s2_12,
                "sin2_theta23": s2_23,
                "sin2_theta13": s2_13,
            }
            comp = {}
            for k, val in obs.items():
                tgt, err = pdg_pmns[k]
                comp[k] = {
                    "computed": nstr50(val),
                    "pdg2024": nstr50(tgt),
                    "pdg2024_err": nstr50(err),
                    "signed_rel_err_pct": mp.nstr((val - tgt) / tgt * mp.mpf(100), 12),
                    "pull_sigma": mp.nstr((val - tgt) / err, 10),
                }
            return {
                "candidate": label,
                "rationale": rationale,
                "unitarity_residual": nstr50(unit_res),
                "J_PMNS": nstr50(j_pmns),
                "comparison_vs_pdg2024": comp,
            }

        U_p1a = mat_dagger(charged_lepton_rot12(h, mp.pi / mp.mpf(2))) * U_tbm
        pmns_rows = [
            score_pmns("PMNS-P0_exact_tribimaximal", U_tbm, "Exact S_3 tribimaximal U_TBM (refuted on theta_13 > 0)"),
            score_pmns(
                "PMNS-P1a_hecke_charged_lepton_tbm_maximal_cp",
                U_p1a,
                "U_PMNS = R_12(arcsin h, delta=pi/2)^H U_TBM => sin^2(theta_13) = h^2 / 2",
            ),
            score_pmns(
                "PMNS-P1b_hecke_charged_lepton_tbm_z5_cp",
                mat_dagger(charged_lepton_rot12(h, mp.mpf(2) * mp.pi / mp.mpf(5))) * U_tbm,
                "U_PMNS = R_12(arcsin h, delta=2*pi/5)^H U_TBM",
            ),
            score_pmns(
                "PMNS-P1c_hecke_charged_lepton_tbm_real",
                mat_dagger(charged_lepton_rot12(h, mp.mpf(0))) * U_tbm,
                "U_PMNS = R_12(arcsin h, delta=0)^T U_TBM (CP-conserving real rotation)",
            ),
        ]
        reactor_id_err = abs(abs(U_p1a[0, 2]) ** 2 - (h ** 2) / mp.mpf(2))
        check(
            "pmns_reactor_h_sq_half_identity",
            reactor_id_err < mp.mpf("1e-75"),
            nstr50(reactor_id_err),
            "0",
            "1e-75",
            "U_PMNS = R_12(arcsin h, delta)^H U_TBM gives exact sin^2(theta_13) = (q0 - q0^-1)^2 / 2",
        )

        # ── Part (b): Satellite T(2,7)–4_1 vs Bare 5_2 / T(2,7) Tau Mass Candidates ──
        log("4. Satellite C_{2,7}(4_1) Alexander/Burau, H_6(q0) Markov trace, & tau/e candidates")

        # 80-dps Vol(5_2) = 3 * D(y_1) where y_1^3 - 2 y_1^2 + 3 y_1 - 1 = 0, Im(y_1) > 0
        roots_5_2 = mp.polyroots([mp.mpf(1), mp.mpf(-2), mp.mpf(3), mp.mpf(-1)], maxsteps=200, extraprec=40)
        y1_5_2 = [r for r in roots_5_2 if mp.im(r) > mp.mpf("0.1")][0]
        cubic_5_2_res = abs(y1_5_2 ** 3 - mp.mpf(2) * y1_5_2 ** 2 + mp.mpf(3) * y1_5_2 - mp.mpf(1))
        vol_5_2 = mp.mpf(3) * bloch_wigner_d(y1_5_2)
        check(
            "five_two_hyperbolic_volume_80dps",
            cubic_5_2_res < mp.mpf("1e-75") and abs(vol_5_2 - mp.mpf("2.828122088330783")) < mp.mpf("1e-14"),
            nstr50(vol_5_2),
            "2.828122088330783",
            "1e-14",
            "Vol(5_2) = 3 D(y_1) on X^3 - 2 X^2 + 3 X - 1 = 0 at 80 dps",
        )

        # Verify Lean cabled Burau-Alexander factorisation at t = q0 and golden-ratio node
        def alex_4_1_pos(t):
            return -mp.mpf(1) + mp.mpf(3) * t - t ** 2

        def alex_torus2_odd(t, m: int):
            return mp.fsum((-t) ** j for j in range(m))

        def alex_cable2_4_1(t, m: int):
            return alex_4_1_pos(t ** 2) * alex_torus2_odd(t, m)

        def burau_clasp_scaled(t):
            return mp.matrix([[t - t ** 2, -mp.mpf(1)], [t, -mp.mpf(1)]])

        C_q0sq = burau_clasp_scaled(q0 ** 2)
        M_bur = (q0 ** 4) * mp.eye(2) - C_q0sq * C_q0sq
        det_bur = M_bur[0, 0] * M_bur[1, 1] - M_bur[0, 1] * M_bur[1, 0]
        lhs_bur = det_bur * (mp.mpf(1) - (-q0) ** 7)
        rhs_bur = (q0 ** 4) * (mp.mpf(1) + q0 ** 2 + q0 ** 4) * (mp.mpf(1) + q0) * alex_cable2_4_1(q0, 7)
        bur_id_err = abs(lhs_bur - rhs_bur)
        check(
            "cabled_burau_alexander_factorisation_80dps",
            bur_id_err < mp.mpf("1e-70"),
            nstr50(bur_id_err),
            "0",
            "1e-70",
            "Matches Lean `cabled_burau_alexander_factorisation` at t = q0, 2n+1 = 7",
        )

        # Golden-ratio sign node of Delta_{C_{2,w}(4_1)}(q0^w) across w in {3, 5, 7}
        golden_phi = (mp.mpf(1) + mp.sqrt(mp.mpf(5))) / mp.mpf(2)
        alex_winding_eval = {
            f"w={w}": nstr50(alex_cable2_4_1(q0 ** w, w))
            for w in (3, 5, 7)
        }
        s_w3 = "+1" if alex_cable2_4_1(q0 ** 3, 3) > 0 else "-1"
        s_w5 = "+1" if alex_cable2_4_1(q0 ** 5, 5) > 0 else "-1"
        node_label = f"sign(w=3)={s_w3}, sign(w=5)={s_w5}"
        check(
            "cabled_alexander_golden_node_sign_flip",
            node_label == "sign(w=3)=+1, sign(w=5)=-1",
            node_label,
            "sign(w=3)=+1, sign(w=5)=-1",
            "0",
            "Delta_{4_1}(q0^{2w}) crosses its golden-ratio root phi^2 between w=3 and w=5",
        )

        # Exact 80-dps Hoefsmit two-row Markov trace of 2-cabled 4_1 + sigma_1^{2k+1} in H_6(q0)
        two_row_6 = [(6,), (5, 1), (4, 2), (3, 3)]
        h6_reps = {}
        h6_weights = {}
        axiom_err = mp.mpf(0)
        for lam in two_row_6:
            k_row2 = lam[1] if len(lam) > 1 else 0
            h6_weights[lam] = q_int_sym(q0, 6 - 2 * k_row2 + 1) / (q2_sym ** 6)
            dim_l, gens_l, invs_l = hoefsmit_generators_80dps(lam, q0)
            h6_reps[lam] = (dim_l, gens_l, invs_l)
            for i_g in range(1, 6):
                quad = (gens_l[i_g] - q0 * mp.eye(dim_l)) * (gens_l[i_g] + q0_inv * mp.eye(dim_l))
                axiom_err += mat_inf_norm(quad)
            for i_g in range(1, 5):
                br = gens_l[i_g] * gens_l[i_g + 1] * gens_l[i_g] - gens_l[i_g + 1] * gens_l[i_g] * gens_l[i_g + 1]
                axiom_err += mat_inf_norm(br)

        def tr_m_h6(word: list[int]):
            return mp.fsum(
                h6_weights[lam] * eval_word_trace(word, *h6_reps[lam])
                for lam in two_row_6
            )

        z_d = (q0 ** 3) / (q0 ** 2 + mp.mpf(1))
        m1_err = abs(tr_m_h6([]) - mp.mpf(1))
        m2_err = abs(tr_m_h6([1, -2, 1, -2, 5]) - z_d * tr_m_h6([1, -2, 1, -2]))
        check(
            "h6_hoefsmit_and_markov_axioms_80dps",
            axiom_err + m1_err + m2_err < mp.mpf("1e-70"),
            nstr50(axiom_err + m1_err + m2_err),
            "0",
            "1e-70",
            "Exact 80-dps H_6(q0) two-row Hoefsmit quadratic, braid, M1, and M2 stabilization axioms",
        )

        # Companion 4_1 braid word in B_3: (sigma_1 sigma_2^{-1})^2 = [1, -2, 1, -2]
        # 2-parallel cable in B_6 + pattern twist sigma_1^w on the cabled pair {1, 2}
        cable_base_4_1 = cable2_word([1, -2, 1, -2])
        sat_traces = {}
        for w in (3, 5, 7):
            sat_word = cable_base_4_1 + [1] * w
            sat_traces[w] = tr_m_h6(sat_word)
        sat_bend = (sat_traces[5] ** 2) / (sat_traces[3] * sat_traces[7])
        obs_lepton_bend = (mu_me_codata ** 2) / tau_me_codata

        # Evaluate all pre-registered tau/e mass-ratio candidates
        four_catalan = mp.mpf(4) * mp.catalan
        mu_anchor_pred = vol_4_1 / hbar_q2

        def score_tau(label: str, val, rationale: str) -> dict[str, object]:
            rel_codata = (val - tau_me_codata) / tau_me_codata * mp.mpf(100)
            rel_belle2 = (val - tau_me_belle2_pdg) / tau_me_belle2_pdg * mp.mpf(100)
            pull_codata = (val - tau_me_codata) / tau_me_codata_err
            return {
                "candidate": label,
                "computed_m_tau_over_m_e": nstr50(val),
                "codata2022_target": nstr50(tau_me_codata),
                "signed_rel_err_vs_codata2022_pct": mp.nstr(rel_codata, 12),
                "abs_rel_err_vs_codata2022_pct": mp.nstr(abs(rel_codata), 12),
                "pull_vs_codata2022_sigma": mp.nstr(pull_codata, 10),
                "signed_rel_err_vs_belle2_3477_228_pct": mp.nstr(rel_belle2, 12),
                "rationale": rationale,
            }

        tau_candidates = [
            score_tau("TAU-B0_bare_T27_volume", mp.mpf(0), "Vol(T(2,7)) = 0 (torus knot has zero hyperbolic volume)"),
            score_tau("TAU-B1_bare_5_2_vol_k2", vol_5_2 / hbar_q2, "Vol(5_2) / hbar_q0^2 (CAL-2 exponent k=2)"),
            score_tau("TAU-B2_bare_5_2_vol_k3", vol_5_2 / hbar_q3, "Vol(5_2) / hbar_q0^3 (exponent k=3, -16.4% miss)"),
            score_tau(
                "TAU-S1_pure_cable_C27_4_1_jsj_vol_k2",
                vol_4_1 / hbar_q2,
                "Vol_JSJ(C_{2,7}(4_1)) / hbar_q0^2 = Vol(4_1)/hbar_q0^2 (Seifert cable piece has Vol=0; recovers muon)",
            ),
            score_tau(
                "TAU-S2a_whitehead_satellite_jsj_vol_k2",
                (vol_4_1 + four_catalan) / hbar_q2,
                "(Vol(4_1) + 4*Catalan) / hbar_q0^2 (Whitehead hyperbolic pattern JSJ sum at k=2)",
            ),
            score_tau(
                "TAU-S2b_whitehead_satellite_jsj_vol_k3",
                (vol_4_1 + four_catalan) / hbar_q3,
                "(Vol(4_1) + 4*Catalan) / hbar_q0^3 (Whitehead hyperbolic pattern JSJ sum at k=3)",
            ),
            score_tau(
                "TAU-S3a_cabled_alexander_q0sq_dressed_k2",
                mu_anchor_pred * alex_cable2_4_1(q0 ** 2, 7),
                "(Vol(4_1)/hbar_q0^2) * Delta_{C_{2,7}(4_1)}(q0^2)",
            ),
            score_tau(
                "TAU-S3b_cabled_alexander_ratio_k3",
                (vol_4_1 / hbar_q3) * (alex_cable2_4_1(q0, 7) / alex_cable2_4_1(q0, 5)),
                "(Vol(4_1)/hbar_q0^3) * (Delta_{C_{2,7}(4_1)}(q0) / Delta_{C_{2,5}(4_1)}(q0))",
            ),
            score_tau(
                "TAU-S4a_h6_cabled_markov_mul_k3",
                (vol_4_1 / hbar_q3) * abs(sat_traces[7]),
                "(Vol(4_1)/hbar_q0^3) * |tr_M(cable_2(4_1) * sigma_1^7)| in H_6(q0)",
            ),
            score_tau(
                "TAU-S4b_h6_cabled_markov_div_k2",
                (vol_4_1 / hbar_q2) / abs(sat_traces[7]),
                "(Vol(4_1)/hbar_q0^2) / |tr_M(cable_2(4_1) * sigma_1^7)| in H_6(q0)",
            ),
        ]

        log("5. Summary of honest hits & misses across pre-registered candidates:")
        for row in ckm_rows[1:]:
            c = row["comparison_vs_pdg2024"]
            log(
                f"  {row['candidate']}: |V_us|={c['V_us']['signed_rel_err_pct']}%, "
                f"|V_cb|={c['V_cb']['signed_rel_err_pct']}%, |V_ub|={c['V_ub']['signed_rel_err_pct']}%, "
                f"J={c['J_CP']['signed_rel_err_pct']}%"
            )
        for row in pmns_rows:
            c = row["comparison_vs_pdg2024"]
            log(
                f"  {row['candidate']}: s12^2={c['sin2_theta12']['signed_rel_err_pct']}%, "
                f"s23^2={c['sin2_theta23']['signed_rel_err_pct']}%, s13^2={c['sin2_theta13']['signed_rel_err_pct']}%"
            )
        for row in tau_candidates:
            log(
                f"  {row['candidate']}: m_tau/m_e={mp.nstr(mp.mpf(row['computed_m_tau_over_m_e']), 10)} "
                f"({row['signed_rel_err_vs_codata2022_pct']}% vs CODATA 3477.23)"
            )

        wb = WitnessBuilder(
            "sm8w-bring-ngen3-ckm-tau",
            engine="mpmath",
            start_time=T0,
            output_dir=_HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps evaluation for Standard Model Package 1 (`qou-gen3` / `Q-Gap-7`): "
            "(a) S_5 ⊃ S_4 ⊃ S_3 and S_5 ⊃ S_3 × S_2 canonical differential branching, conjugate S_3 "
            "vs Z_5 T(3,5) Bloch overlaps, and parameter-free CKM/PMNS candidate matrices vs PDG-2024; "
            "(b) Seifert-Torres cabled figure-eight Alexander/Burau factorisation, H_6(q0) two-row "
            "Markov traces of cable_2(4_1)*sigma_1^w, and satellite vs bare 5_2/T(2,7) tau/e mass-ratio "
            "candidates vs CODATA-2022 m_tau/m_e = 3477.23(23). Zero fitting; honest misses reported."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("q0_proton_80dps", nstr80(q0))
        wb.add_parameter("hecke_defect_h", nstr50(h))
        wb.add_parameter("hbar_q0", nstr50(hbar_q))
        wb.add_parameter("q2_sym", nstr50(q2_sym))
        wb.add_parameter("q3_sym", nstr50(q3_sym))

        wb.add_data("companion_lean_module", "folio/quantum-observable-universe/lean/QOU/StandardModel/BringGenerationSplitAndCKMTexture.lean")
        wb.add_data("preregistration_file", "computations/probes/sm8w_bring_ngen3_ckm_tau/PREREGISTRATION.md")
        wb.add_data("selected", "none (scope-(a) pre-registered exploratory comparison; zero fitting)")
        wb.add_data(
            "honest_generation_scope",
            {
                "owner_guardrail": "Bring's generation count is not established unconditionally (2026-10-10 owner ruling)",
                "canonical_h0_dim": 4,
                "s4_branching": "4 -> 3 + 1",
                "s3_branching": "4 -> 2 + 1 + 1 (3 -> 2 + 1 on V_gen3)",
                "s3xs2_branching": "4 -> (2 x 1) + (1 x 1) + (1 x sgn)",
                "filter_counts": {
                    "seifert_genus_le_4": [3, 5, 7, 9],
                    "primitive_morgan_voyce_continuant": [3, 5, 7],
                    "s5_equivariant_odd_order": [3, 5],
                },
                "conditional_lean_class": "BringChiralGenerationSelectionHypothesis (0 instances, Rule 13a)",
                "conjugate_s3_z5_overlap_singular_values": [nstr50(v) for v in svals_s3_z5],
                "hoefsmit_h3_cos_theta": nstr50(cos_theta_h),
                "hoefsmit_h3_sin_theta": nstr50(sin_theta_h),
            },
        )
        wb.add_data("ckm_candidates", ckm_rows)
        wb.add_data("ckm_c3_cabibbo_two_gen_comparison", ckm_c3_table)
        wb.add_data("pmns_candidates", pmns_rows)
        wb.add_data(
            "satellite_tau_analysis",
            {
                "vol_4_1_80dps": nstr50(vol_4_1),
                "vol_5_2_80dps": nstr50(vol_5_2),
                "golden_ratio_phi": nstr50(golden_phi),
                "cabled_alexander_winding_scaled_q0w": alex_winding_eval,
                "h6_cabled_4_1_markov_traces": {f"w={w}": nstr50(sat_traces[w]) for w in (3, 5, 7)},
                "h6_cabled_4_1_bend": nstr50(sat_bend),
                "observed_charged_lepton_bend": nstr50(obs_lepton_bend),
                "tau_over_e_candidates": tau_candidates,
            },
        )

        for a_ in ASSERTS:
            wb.add_assertion(
                str(a_["name"]),
                computed=str(a_["computed"]),
                expected=str(a_["expected"]),
                tolerance=str(a_["tolerance"]),
                source=str(a_["source"]),
            )
        wpath = wb.save({"q0Anchor": "proton"})
        log(f"Witness saved -> {wpath.relative_to(_ROOT)} ({len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} assertions passed)")
        return 0 if not FAILED else 1


if __name__ == "__main__":
    raise SystemExit(main())
