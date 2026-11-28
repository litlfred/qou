#!/usr/bin/env python3
"""80-dps Proton-Pin Probe: Untapped Algebraic Invariants on O_q(SU(2)), U_q(sl_2), and H_n(q).

Companion Lean 4 modules (`0 sorry`, `0` custom `axiom`s, `[CommRing R]`):
  - `folio/quantum-observable-universe/lean/BraidKnotOctonion/HeckeJucysMurphySymmetricCenter.lean`
    (discharges bean `qou-u9o1`: multiplicative JM commutativity `L_a * L_b = L_b * L_a`,
    general full-twist factorization `prod_{k<n} L_k = Delta_n^2`, and symmetric center
    `e_k(L_0, ..., L_{n-1}) in Z(H_n(q))`)
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/LeptonFramedGNSAndStrainOrder.lean`
    (Wenzl `(2,1)` strain `det G_{(2,1)}(W) = 1` & global electron minimum `tr G_{(2,1)}(e) = 2`,
    `tau_{GenDeg}(mu) = 0`, real-`q` strict inequalities `||e_tilde||_D^2 < ||mu_tilde||_D^2 < ||tau_tilde||_D^2`,
    and `O_q(SU(2))` spinor left/right GNS Haar isospin dichotomy)

Audit report:
  - `docs/audits/2026-11-28-untapped-algebraic-invariants-audit.md`

Strict proton-pin & anti-fit discipline (`2026-11-28`):
  - `mpmath.workdps(85)` (`>= 80` dps, `OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(85)`),
  - zero `float64` imports, casts, or lossy literals (`scripts/probe-float64-guard.py --strict` clean),
  - zero fitted parameters (`NO FITTING EXCEPT CAL-1/2/3`; both structural hits and clean misses recorded).
"""

from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
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

WORK_DPS = 85
OUT_DPS = 50
set_compute_dps(WORK_DPS)


def q_int(n: int, q: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    if abs(q - 1) < mp.mpf("1e-70"):
        return mp.mpf(n)
    return (q**n - q ** (-n)) / (q - q ** (-1))


def q_fact(n: int, q: mp.mpf) -> mp.mpf:
    res = mp.mpf(1)
    for k in range(1, n + 1):
        res *= q_int(k, q)
    return res


def koide_Q(x1: mp.mpf, x2: mp.mpf, x3: mp.mpf) -> mp.mpf:
    if x1 <= 0 or x2 <= 0 or x3 <= 0:
        return mp.mpf(0)
    s = mp.sqrt(x1) + mp.sqrt(x2) + mp.sqrt(x3)
    return (x1 + x2 + x3) / (s * s)


# ---------------------------------------------------------------------------
# 0. Exact Symbolic Verification over Z[h] (H_3, H_4, H_5 JM Center)
# ---------------------------------------------------------------------------
def verify_jm_braid_commutativity_symbolic() -> dict[str, bool]:
    h = sp.Symbol("h", commutative=True)

    def hecke_mul_words(n: int):
        def mul_gen_right(elem: dict[tuple[int, ...], sp.Expr], i: int):
            out: dict[tuple[int, ...], sp.Expr] = {}
            for w, c in elem.items():
                w_list = list(w)
                w2 = list(w_list)
                w2[i], w2[i + 1] = w2[i + 1], w2[i]
                wt = tuple(w2)
                if w_list[i] < w_list[i + 1]:
                    out[wt] = sp.expand(out.get(wt, 0) + c)
                else:
                    out[w] = sp.expand(out.get(w, 0) + h * c)
                    out[wt] = sp.expand(out.get(wt, 0) + c)
            return {k: v for k, v in out.items() if v != 0}

        def reduced_word(w: tuple[int, ...]) -> list[int]:
            arr = list(w)
            seq = []
            for _ in range(len(arr) * len(arr)):
                moved = False
                for idx in range(len(arr) - 1):
                    if arr[idx] > arr[idx + 1]:
                        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                        seq.append(idx)
                        moved = True
                        break
                if not moved:
                    break
            return list(reversed(seq))

        rw_cache: dict[tuple[int, ...], list[int]] = {}

        def mul(a: dict[tuple[int, ...], sp.Expr], b: dict[tuple[int, ...], sp.Expr]):
            res: dict[tuple[int, ...], sp.Expr] = {}
            for wb, cb in b.items():
                if wb not in rw_cache:
                    rw_cache[wb] = reduced_word(wb)
                cur = a
                for g in rw_cache[wb]:
                    cur = mul_gen_right(cur, g)
                for wa, ca in cur.items():
                    val = sp.expand(res.get(wa, 0) + ca * cb)
                    if val == 0:
                        res.pop(wa, None)
                    else:
                        res[wa] = val
            return res

        def add(a, b, sign=1):
            res = dict(a)
            for k, v in b.items():
                val = sp.expand(res.get(k, 0) + sign * v)
                if val == 0:
                    res.pop(k, None)
                else:
                    res[k] = val
            return res

        id_perm = tuple(range(n))
        one = {id_perm: sp.Integer(1)}
        sig = [mul_gen_right(one, i) for i in range(n - 1)]
        L = [one]
        for i in range(n - 1):
            L.append(mul(mul(sig[i], L[-1]), sig[i]))
        return one, sig, L, mul, add

    checks: dict[str, bool] = {}
    for n in (3, 4, 5):
        one, sig, L, mul, add = hecke_mul_words(n)
        below_ok = all(
            len(add(mul(sig[k], L[m]), mul(L[m], sig[k]), -1)) == 0
            for m in range(n)
            for k in range(n - 1)
            if k + 2 <= m
        )
        comm_ok = all(
            len(add(mul(L[a], L[b]), mul(L[b], L[a]), -1)) == 0
            for a in range(n)
            for b in range(a + 1, n)
        )
        prod_L = one
        for m in range(n):
            prod_L = mul(prod_L, L[m])
        cox = one
        for i in range(n - 1):
            cox = mul(cox, sig[i])
        full_twist = one
        for _ in range(n):
            full_twist = mul(full_twist, cox)
        twist_ok = len(add(prod_L, full_twist, -1)) == 0
        central_ok = True
        for k in range(1, n + 1):
            ek: dict[tuple[int, ...], sp.Expr] = {}
            for subset in combinations(range(n), k):
                term = one
                for idx in subset:
                    term = mul(term, L[idx])
                ek = add(ek, term, +1)
            for i in range(n - 1):
                if add(mul(sig[i], ek), mul(ek, sig[i]), -1):
                    central_ok = False
        checks[f"H_{n}_below_comm"] = below_ok
        checks[f"H_{n}_all_JM_comm"] = comm_ok
        checks[f"H_{n}_prod_eq_fullTwist"] = twist_ok
        checks[f"H_{n}_all_ek_central"] = central_ok
    checks["all_passed"] = all(checks.values())
    return checks


# ---------------------------------------------------------------------------
# 1. Family 1: O_q(SU(2)) Non-Tracial Haar State, KMS Twist, & Peter-Weyl
# ---------------------------------------------------------------------------
def run_family_1(
    q0: mp.mpf, m_e: mp.mpf, E0: mp.mpf, c_cat_abs: mp.mpf, dm_np_exp: mp.mpf
) -> tuple[dict[str, object], mp.mpf]:
    two_q = q_int(2, q0)
    four_q = q_int(4, q0)

    h_alpha_delta = mp.mpf(1) / (1 + q0**2)
    h_delta_alpha = q0**2 / (1 + q0**2)
    h_beta_gamma = -q0 / (1 + q0**2)
    kms_ratio = h_delta_alpha / h_alpha_delta
    h_comm_ad = h_alpha_delta - h_delta_alpha
    tanh_ln_q0 = -h_comm_ad

    def h_t_pow(k: int) -> mp.mpf:
        return (1 - q0**2) / (1 - q0 ** (2 * (k + 1)))

    # Ordered 3-quark unit spinor monomials W_p = alpha^2 gamma, W_n = alpha gamma^2
    h_Wp_L = h_t_pow(1) - (1 + q0 ** (-2)) * h_t_pow(2) + q0 ** (-2) * h_t_pow(3)
    h_Wp_L_closed = q0**8 / ((1 + q0**2 + q0**4) * (1 + q0**2 + q0**4 + q0**6))
    h_Wn_L = h_t_pow(2) - h_t_pow(3)
    h_Wn_L_closed = q0**6 / ((1 + q0**2 + q0**4) * (1 + q0**2 + q0**4 + q0**6))
    h_Wp_R = q0**4 * (h_t_pow(1) - (q0**2 + q0**4) * h_t_pow(2) + q0**6 * h_t_pow(3))
    h_Wn_R = q0**4 * (h_t_pow(2) - q0**2 * h_t_pow(3))
    h_W_R_closed = q0**4 / ((1 + q0**2 + q0**4) * (1 + q0**2 + q0**4 + q0**6))

    max_res = max(
        abs(h_Wp_L - h_Wp_L_closed),
        abs(h_Wn_L - h_Wn_L_closed),
        abs(h_Wp_R - h_W_R_closed),
        abs(h_Wn_R - h_W_R_closed),
        abs(h_Wp_L / h_Wn_L - q0**2),
        abs(h_Wp_R - h_Wn_R),
    )

    data = {
        "h_alpha_delta": fmt(h_alpha_delta, dps=OUT_DPS),
        "h_delta_alpha": fmt(h_delta_alpha, dps=OUT_DPS),
        "h_beta_gamma": fmt(h_beta_gamma, dps=OUT_DPS),
        "kms_ratio_q0_sq": fmt(kms_ratio, dps=OUT_DPS),
        "h_commutator_ad_minus_da": fmt(h_comm_ad, dps=OUT_DPS),
        "pw_j1_2_diff_R_n_minus_p": fmt(tanh_ln_q0, dps=OUT_DPS),
        "pw_j3_2_diff_R_3_2": fmt((q0**3 - q0 ** (-3)) / four_q, dps=OUT_DPS),
        "spinor_3quark_L_Wp": fmt(h_Wp_L, dps=OUT_DPS),
        "spinor_3quark_L_Wn": fmt(h_Wn_L, dps=OUT_DPS),
        "spinor_3quark_L_ratio_p_over_n": fmt(h_Wp_L / h_Wn_L, dps=OUT_DPS),
        "spinor_3quark_R_Wp": fmt(h_Wp_R, dps=OUT_DPS),
        "spinor_3quark_R_Wn": fmt(h_Wn_R, dps=OUT_DPS),
        "spinor_3quark_R_ratio_n_over_p": fmt(h_Wn_R / h_Wp_R, dps=OUT_DPS),
        "candidate_splits_MeV": {
            "linear_j1_2_R_in_me": fmt(tanh_ln_q0 * m_e, dps=OUT_DPS),
            "linear_j1_2_R_in_c_cat": fmt(tanh_ln_q0 * c_cat_abs, dps=OUT_DPS),
            "linear_j1_2_R_in_E0": fmt(tanh_ln_q0 * E0, dps=OUT_DPS),
            "linear_j3_2_R_3_2_in_E0": fmt(((q0**3 - q0 ** (-3)) / four_q) * E0, dps=OUT_DPS),
            "plancherel_inv_j1_2_in_E0": fmt(two_q * (q0 - q0 ** (-1)) * E0, dps=OUT_DPS),
            "measured_dm_np_MeV": fmt(dm_np_exp, dps=OUT_DPS),
        },
    }
    return data, max_res


# ---------------------------------------------------------------------------
# 2. H_3(q0) Representations & Family 2 (JM Symmetric Center)
# ---------------------------------------------------------------------------
def build_h3_reps(q0: mp.mpf):
    h0 = q0 - q0 ** (-1)
    two_q = q_int(2, q0)
    three_q = q_int(3, q0)
    I2 = mp.eye(2)

    s0_3 = mp.matrix([[q0]])
    s1_3 = mp.matrix([[q0]])
    s0_111 = mp.matrix([[-q0 ** (-1)]])
    s1_111 = mp.matrix([[-q0 ** (-1)]])

    s0_21 = mp.matrix([[q0, mp.mpf(0)], [mp.mpf(0), -q0 ** (-1)]])
    a = -(q0 ** (-2)) / two_q
    c = (q0**2) / two_q
    b = mp.sqrt(three_q) / two_q
    s1_21 = mp.matrix([[a, b], [b, c]])

    s0i_3 = mp.matrix([[q0 ** (-1)]])
    s1i_3 = mp.matrix([[q0 ** (-1)]])
    s0i_111 = mp.matrix([[-q0]])
    s1i_111 = mp.matrix([[-q0]])
    s0i_21 = s0_21 - h0 * I2
    s1i_21 = s1_21 - h0 * I2

    y_D = {
        (3,): (q0**4 + 1) / (q0**2 + 1) ** 2,
        (2, 1): q0**2 / (q0**2 + 1) ** 2,
        (1, 1, 1): mp.mpf(0),
    }
    qfact3 = q_fact(3, q0)
    y_GenDeg = {
        (3,): q0**3 / qfact3,
        (2, 1): two_q / qfact3,
        (1, 1, 1): q0 ** (-3) / qfact3,
    }
    gens = {
        (3,): {1: s0_3, -1: s0i_3, 2: s1_3, -2: s1i_3},
        (2, 1): {1: s0_21, -1: s0i_21, 2: s1_21, -2: s1i_21},
        (1, 1, 1): {1: s0_111, -1: s0i_111, 2: s1_111, -2: s1i_111},
    }

    def eval_word(word: list[int]):
        mats = {}
        for lam, gmap in gens.items():
            d = 2 if lam == (2, 1) else 1
            M = mp.eye(d)
            for letter in word:
                M = M * gmap[letter]
            mats[lam] = M
        return mats

    return y_D, y_GenDeg, eval_word


def elem_symm_mp(vals: list[mp.mpf], k: int) -> mp.mpf:
    if k == 0:
        return mp.mpf(1)
    if k > len(vals):
        return mp.mpf(0)
    dp = [mp.mpf(0)] * (k + 1)
    dp[0] = mp.mpf(1)
    for v in vals:
        for j in range(min(k, len(vals)), 0, -1):
            dp[j] += dp[j - 1] * v
    return dp[k]


def jm_central_scalars(part: tuple[int, ...], q0: mp.mpf) -> dict[str, mp.mpf]:
    contents = [c - r for r, row in enumerate(part) for c in range(row)]
    n = len(contents)
    evals_J = [q0 ** (2 * c) for c in contents]
    denom = q0**2 - q0 ** (-2)
    evals_C = [(q0 ** (2 * c) - q0 ** (-2 * c)) / denom for c in contents]
    out: dict[str, mp.mpf] = {}
    for k in range(1, min(n, 3) + 1):
        out[f"e_{k}_J"] = elem_symm_mp(evals_J, k)
        out[f"e_{k}_C"] = elem_symm_mp(evals_C, k)
    out["prod_J"] = elem_symm_mp(evals_J, n)
    out["p3_C_skewness"] = sum((x**3 for x in evals_C), mp.mpf(0))
    return out


def run_family_2(q0: mp.mpf, eval_h3, y_D, y_GenDeg) -> tuple[dict[str, object], mp.mpf]:
    h3_parts = [(3,), (2, 1), (1, 1, 1)]
    h3_scalars = {lam: jm_central_scalars(lam, q0) for lam in h3_parts}

    max_mat_res = mp.mpf(0)
    for lam in h3_parts:
        J1 = eval_h3([])[lam]
        J2 = eval_h3([1, 1])[lam]
        J3 = eval_h3([2, 1, 1, 2])[lam]
        d = 2 if lam == (2, 1) else 1
        Id = mp.eye(d)
        max_mat_res = max(
            max_mat_res,
            mp.norm((J1 + J2 + J3) - h3_scalars[lam]["e_1_J"] * Id),
            mp.norm((J1 * J2 + J1 * J3 + J2 * J3) - h3_scalars[lam]["e_2_J"] * Id),
            mp.norm((J1 * J2 * J3) - h3_scalars[lam]["e_3_J"] * Id),
        )

    words_h3 = {
        "beta_Bor": [1, -2, 1, -2, 1, -2],
        "e_hopf": [1, 2, 1],
        "mu_t24": [1, 1, 1, 1, -2],
        "tau_whitehead": [1, 1, -2, 1, -2],
    }
    chi_h3: dict[str, dict[tuple[int, ...], mp.mpf]] = {}
    for name, w in words_h3.items():
        mats = eval_h3(w)
        chi_h3[name] = {
            lam: sum(mats[lam][i, i] for i in range(mats[lam].rows))
            for lam in h3_parts
        }

    for atom, fname in (
        ("proton_uud", "chi-proton-h3-at-q0-50dps.witness.json"),
        ("neutron_udd", "chi-neutron-h3-at-q0-50dps.witness.json"),
    ):
        d = json.loads((_ROOT / "computations" / fname).read_text())
        chi_h3[atom] = {
            tuple(row["partition"]): mp.mpf(row["chi_lambda"])
            for row in d["by_partition"]
        }

    mu_gendeg_abs = abs(
        sum(y_GenDeg[lam] * chi_h3["mu_t24"][lam] for lam in h3_parts)
    )
    max_mat_res = max(max_mat_res, mu_gendeg_abs)

    pairings_out = {}
    for name, ch in chi_h3.items():
        pairings_out[name] = {
            "tauD_1": fmt(sum(y_D[lam] * ch[lam] for lam in h3_parts), dps=OUT_DPS),
            "tauD_e1_J": fmt(
                sum(y_D[lam] * h3_scalars[lam]["e_1_J"] * ch[lam] for lam in h3_parts),
                dps=OUT_DPS,
            ),
            "tauD_e2_J": fmt(
                sum(y_D[lam] * h3_scalars[lam]["e_2_J"] * ch[lam] for lam in h3_parts),
                dps=OUT_DPS,
            ),
            "tauD_e3_J": fmt(
                sum(y_D[lam] * h3_scalars[lam]["e_3_J"] * ch[lam] for lam in h3_parts),
                dps=OUT_DPS,
            ),
            "tauGen_1": fmt(sum(y_GenDeg[lam] * ch[lam] for lam in h3_parts), dps=OUT_DPS),
            "tauGen_p3_C": fmt(
                sum(
                    y_GenDeg[lam] * h3_scalars[lam]["p3_C_skewness"] * ch[lam]
                    for lam in h3_parts
                ),
                dps=OUT_DPS,
            ),
        }

    nuclear_out = {}
    for atom, fname in (
        ("deuteron_H6", "chi-deuteron-h6-at-q0-50dps.witness.json"),
        ("tritium_H9", "chi-tritium-h9-at-q0-50dps.witness.json"),
        ("helium3_H9", "chi-helium-3-h9-at-q0-50dps.witness.json"),
        ("helium4_H12", "chi-helium-4-h12-at-q0-50dps.witness.json"),
    ):
        p = _ROOT / "computations" / fname
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        n_str = d["n_strands"]
        qfact_n = q_fact(n_str, q0)
        le2_e3 = mp.mpf(0)
        eq3_p3C = mp.mpf(0)
        rect_info = {}
        for row in d["by_partition"]:
            part = tuple(row["partition"])
            chi = mp.mpf(row["chi_lambda"])
            y_lam = mp.mpf(row["y_lambda"])
            sc = jm_central_scalars(part, q0)
            hooks = []
            for r_i, r_len in enumerate(part):
                for c_i in range(r_len):
                    arm = r_len - c_i - 1
                    leg = sum(1 for r2 in range(r_i + 1, len(part)) if part[r2] > c_i)
                    hooks.append(arm + leg + 1)
            dim_q = qfact_n
            for h_len in hooks:
                dim_q /= q_int(h_len, q0)
            w_pl = (dim_q**2) / (qfact_n * mp.mpf(row["dim"]))
            if len(part) <= 2:
                le2_e3 += y_lam * sc["e_3_J"] * chi
            elif len(part) == 3:
                eq3_p3C += w_pl * sc["p3_C_skewness"] * chi
            if len(part) == 3 and part[0] == part[1] == part[2]:
                rect_info = {
                    "part": list(part),
                    "chi": fmt(chi, dps=OUT_DPS),
                    "prod_J": fmt(sc["prod_J"], dps=OUT_DPS),
                    "p3_C_skewness": fmt(sc["p3_C_skewness"], dps=OUT_DPS),
                }
        nuclear_out[atom] = {
            "convD_le2_e3J": fmt(le2_e3, dps=OUT_DPS),
            "plancherel_eq3_p3C": fmt(eq3_p3C, dps=OUT_DPS),
            "colour_singlet_AAA": rect_info,
        }

    return {"h3_pairings": pairings_out, "nuclear_sectors": nuclear_out}, max_mat_res


# ---------------------------------------------------------------------------
# 3. Family 3: Higher Power Sums, Framed GNS Norms, & k-Cabled Satellites
# ---------------------------------------------------------------------------
def build_two_row_seminormal_rep(n: int, k_row2: int, q0: mp.mpf):
    shape = (n - k_row2,) if k_row2 == 0 else (n - k_row2, k_row2)
    syts: list[tuple[int, ...]] = []

    def backtrack(r0: int, r1: int, cur: list[int]):
        if len(cur) == n:
            syts.append(tuple(cur))
            return
        if r0 < shape[0]:
            cur.append(0)
            backtrack(r0 + 1, r1, cur)
            cur.pop()
        if k_row2 > 0 and r1 < k_row2 and r1 + 1 <= r0:
            cur.append(1)
            backtrack(r0, r1 + 1, cur)
            cur.pop()

    backtrack(0, 0, [])
    d = len(syts)
    idx_of = {t: idx for idx, t in enumerate(syts)}
    contents = []
    for t in syts:
        c_counts = [0, 0]
        ct = []
        for row_idx in t:
            col_idx = c_counts[row_idx]
            c_counts[row_idx] += 1
            ct.append(col_idx - row_idx)
        contents.append(ct)

    h0 = q0 - q0 ** (-1)
    Id = mp.eye(d)
    sigmas = []
    sigma_invs = []
    for i in range(n - 1):
        M = mp.zeros(d, d)
        for tidx, t in enumerate(syts):
            if t[i] == t[i + 1]:
                M[tidx, tidx] = q0
            else:
                dist = contents[tidx][i + 1] - contents[tidx][i]
                if dist == -1:
                    M[tidx, tidx] = -q0 ** (-1)
                else:
                    t_swapped = list(t)
                    t_swapped[i], t_swapped[i + 1] = t_swapped[i + 1], t_swapped[i]
                    sidx = idx_of[tuple(t_swapped)]
                    if tidx < sidx:
                        r = abs(dist)
                        qr = q_int(r, q0)
                        off = mp.sqrt(q_int(r + 1, q0) * q_int(r - 1, q0)) / qr
                        if dist < 0:
                            M[tidx, tidx] = -(q0 ** (-r)) / qr
                            M[sidx, sidx] = +(q0**r) / qr
                        else:
                            M[tidx, tidx] = +(q0**r) / qr
                            M[sidx, sidx] = -(q0 ** (-r)) / qr
                        M[tidx, sidx] = off
                        M[sidx, tidx] = off
        sigmas.append(M)
        sigma_invs.append(M - h0 * Id)
    return d, sigmas, sigma_invs


def cable_word_3braid(word_3: list[int], k_cable: int) -> list[int]:
    def block_pos(offset: int) -> list[int]:
        return [
            offset + row + col + 1
            for row in range(k_cable - 1, -1, -1)
            for col in range(k_cable)
        ]

    b1_pos = block_pos(0)
    b1_neg = [-g for g in reversed(b1_pos)]
    b2_pos = block_pos(k_cable)
    b2_neg = [-g for g in reversed(b2_pos)]
    mapping = {1: b1_pos, -1: b1_neg, 2: b2_pos, -2: b2_neg}
    res: list[int] = []
    for letter in word_3:
        res.extend(mapping[letter])
    return res


def run_family_3(q0: mp.mpf, eval_h3, y_D) -> tuple[dict[str, object], bool, mp.mpf]:
    ladder = {
        "e": [1, 2, 1],
        "mu": [1, 1, 1, 1, -2],
        "tau": [1, 1, -2, 1, -2],
    }

    def tau_D(mats) -> mp.mpf:
        return y_D[(3,)] * mats[(3,)][0, 0] + y_D[(2, 1)] * (
            mats[(2, 1)][0, 0] + mats[(2, 1)][1, 1]
        )

    def mat_mul(mA, mB):
        return {lam: mA[lam] * mB[lam] for lam in ((3,), (2, 1), (1, 1, 1))}

    def mat_adj(mA):
        return {lam: mA[lam].T for lam in ((3,), (2, 1), (1, 1, 1))}

    h6_reps = [build_two_row_seminormal_rep(6, k, q0) for k in range(4)]
    h6_w = [q_int(6 - 2 * k + 1, q0) / (q_int(2, q0) ** 6) for k in range(4)]
    h9_reps = [build_two_row_seminormal_rep(9, k, q0) for k in range(5)]
    h9_w = [q_int(9 - 2 * k + 1, q0) / (q_int(2, q0) ** 9) for k in range(5)]

    def eval_cable(word_3: list[int], k_cable: int) -> mp.mpf:
        cword = cable_word_3braid(word_3, k_cable)
        reps = h6_reps if k_cable == 2 else h9_reps
        weights = h6_w if k_cable == 2 else h9_w
        tr_val = mp.mpf(0)
        for w_lam, (d, sigs, sig_invs) in zip(weights, reps):
            M = mp.eye(d)
            for s in cword:
                M = M * (sigs[s - 1] if s > 0 else sig_invs[-s - 1])
            tr_val += w_lam * sum(M[idx, idx] for idx in range(d))
        return tr_val

    raw: dict[str, dict[str, mp.mpf]] = {}
    strain_det_err = mp.mpf(0)
    for name, w in ladder.items():
        M0 = eval_h3([])
        M1 = eval_h3(w)
        M2 = mat_mul(M1, M1)
        M3 = mat_mul(M2, M1)
        M4 = mat_mul(M3, M1)
        M1_adj = mat_adj(M1)
        M2_adj = mat_adj(M2)

        p1 = tau_D(M1)
        p2 = tau_D(M2)
        p3 = tau_D(M3)
        p4 = tau_D(M4)
        wr = sum(1 if s > 0 else -1 for s in w)

        gns_norm = tau_D(mat_mul(M1_adj, M1))
        gns_framed = gns_norm / (q0 ** (2 * wr))
        G21 = M1[(2, 1)].T * M1[(2, 1)]
        strain_det_err = max(strain_det_err, abs(mp.det(G21) - 1))
        tr_G21 = G21[0, 0] + G21[1, 1]

        pows = [M0, M1, M2]
        adjs = [M0, M1_adj, M2_adj]
        G3 = mp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                G3[a, b] = tau_D(mat_mul(adjs[a], pows[b]))

        chi21 = M1[(2, 1)][0, 0] + M1[(2, 1)][1, 1]
        tauD_Delta2 = y_D[(3,)] * (q0**6) * M1[(3,)][0, 0] + y_D[(2, 1)] * chi21
        c2 = eval_cable(w, 2)
        c3 = eval_cable(w, 3)

        raw[name] = {
            "p1_tauD": p1,
            "p2_tauD_W2": p2,
            "p3_tauD_W3": p3,
            "p4_tauD_W4": p4,
            "kap2_var": p2 - p1**2,
            "abs_kap3": abs(p3 - 3 * p2 * p1 + 2 * p1**3),
            "gns_norm_unframed": gns_norm,
            "gns_var_detG2": gns_norm - p1**2,
            "det_G3_krylov": mp.det(G3),
            "tr_G21_strain": tr_G21,
            "gns_norm_framed": gns_framed,
            "inv_tauD_e3J_Delta2": 1 / tauD_Delta2,
            "cable2_tauD_H6": c2,
            "cable3_tauD_H9": c3,
            "inv_cable3_tauD_H9": 1 / c3,
        }

    # Check exact electron strain minimum tr G_{(2,1)}(e) == 2
    strain_det_err = max(strain_det_err, abs(raw["e"]["tr_G21_strain"] - 2))

    # Three real-q0 invariants achieving strict I(e) < I(mu) < I(tau):
    strict_three = (
        raw["e"]["gns_norm_framed"]
        < raw["mu"]["gns_norm_framed"]
        < raw["tau"]["gns_norm_framed"]
        and raw["e"]["inv_tauD_e3J_Delta2"]
        < raw["mu"]["inv_tauD_e3J_Delta2"]
        < raw["tau"]["inv_tauD_e3J_Delta2"]
        and raw["e"]["inv_cable3_tauD_H9"]
        < raw["mu"]["inv_cable3_tauD_H9"]
        < raw["tau"]["inv_cable3_tauD_H9"]
    )

    summary_out = {}
    for k in raw["e"]:
        ve, vmu, vtau = raw["e"][k], raw["mu"][k], raw["tau"][k]
        summary_out[k] = {
            "e": fmt(ve, dps=OUT_DPS),
            "mu": fmt(vmu, dps=OUT_DPS),
            "tau": fmt(vtau, dps=OUT_DPS),
            "mu_over_e": fmt(vmu / ve, dps=OUT_DPS),
            "tau_over_e": fmt(vtau / ve, dps=OUT_DPS),
            "koide_Q": fmt(koide_Q(ve, vmu, vtau), dps=OUT_DPS),
            "strict_e_lt_mu_lt_tau": bool(ve < vmu < vtau),
        }

    return summary_out, strict_three, strain_det_err


# ---------------------------------------------------------------------------
# 4. Family 4: Quantum 6j-Symbols & Truncated Turaev-Viro Sums at Real q_0^(p)
# ---------------------------------------------------------------------------
def triangle_ok(two_a: int, two_b: int, two_c: int) -> bool:
    if (two_a + two_b + two_c) % 2 != 0:
        return False
    return (
        abs(two_a - two_b) <= two_c <= two_a + two_b
        and abs(two_b - two_c) <= two_a <= two_b + two_c
        and abs(two_c - two_a) <= two_b <= two_c + two_a
    )


def delta_tri(two_a: int, two_b: int, two_c: int, q0: mp.mpf) -> mp.mpf:
    s1 = (-two_a + two_b + two_c) // 2
    s2 = (two_a - two_b + two_c) // 2
    s3 = (two_a + two_b - two_c) // 2
    s4 = (two_a + two_b + two_c) // 2 + 1
    return mp.sqrt(q_fact(s1, q0) * q_fact(s2, q0) * q_fact(s3, q0) / q_fact(s4, q0))


def q6j_racah_wigner(
    tj1: int, tj2: int, tj3: int, tj4: int, tj5: int, tj6: int, q0: mp.mpf
) -> mp.mpf:
    if not (
        triangle_ok(tj1, tj2, tj3)
        and triangle_ok(tj1, tj5, tj6)
        and triangle_ok(tj4, tj2, tj6)
        and triangle_ok(tj4, tj5, tj3)
    ):
        return mp.mpf(0)
    T1 = (tj1 + tj2 + tj3) // 2
    T2 = (tj1 + tj5 + tj6) // 2
    T3 = (tj4 + tj2 + tj6) // 2
    T4 = (tj4 + tj5 + tj3) // 2
    S1 = (tj1 + tj2 + tj4 + tj5) // 2
    S2 = (tj2 + tj3 + tj5 + tj6) // 2
    S3 = (tj3 + tj1 + tj6 + tj4) // 2
    z_min = max(T1, T2, T3, T4)
    z_max = min(S1, S2, S3)
    if z_min > z_max:
        return mp.mpf(0)
    pref = (
        delta_tri(tj1, tj2, tj3, q0)
        * delta_tri(tj1, tj5, tj6, q0)
        * delta_tri(tj4, tj2, tj6, q0)
        * delta_tri(tj4, tj5, tj3, q0)
    )
    total = mp.mpf(0)
    for z in range(z_min, z_max + 1):
        sign = -1 if (z % 2 == 1) else 1
        num = sign * q_fact(z + 1, q0)
        den = (
            q_fact(z - T1, q0)
            * q_fact(z - T2, q0)
            * q_fact(z - T3, q0)
            * q_fact(z - T4, q0)
            * q_fact(S1 - z, q0)
            * q_fact(S2 - z, q0)
            * q_fact(S3 - z, q0)
        )
        total += num / den
    return pref * total


def run_family_4(q0: mp.mpf) -> tuple[dict[str, object], mp.mpf]:
    orth_sum = sum(
        q_int(3, q0)
        * q_int(tj6 + 1, q0)
        * (q6j_racah_wigner(1, 1, 2, 1, 1, tj6, q0) ** 2)
        for tj6 in (0, 2)
    )
    pent_lhs = mp.mpf(0)
    for tX in (0, 2, 4):
        X = tX // 2
        s = -1 if ((9 + X) % 2 == 1) else 1
        pent_lhs += (
            s * q_int(tX + 1, q0) * (q6j_racah_wigner(2, 2, 2, 2, 2, tX, q0) ** 3)
        )
    pent_rhs = q6j_racah_wigner(2, 2, 2, 2, 2, 2, q0) ** 2
    max_6j_err = max(
        abs(orth_sum - 1),
        abs(abs(pent_lhs) - pent_rhs),
        abs(q6j_racah_wigner(1, 1, 2, 1, 1, 0, q0) - 1 / q_int(2, q0)),
        abs(
            q6j_racah_wigner(2, 2, 2, 1, 1, 1, q0)
            + mp.sqrt(q_int(4, q0)) / (q_int(2, q0) * q_int(3, q0))
        ),
    )

    configs = {
        "tet_1_2_1_2_1__1_2_1_2_0": (1, 1, 2, 1, 1, 0),
        "tet_1_2_1_2_1__1_2_1_2_1": (1, 1, 2, 1, 1, 2),
        "tet_1_1_1__1_2_1_2_1_2_TaitSpinor": (2, 2, 2, 1, 1, 1),
        "tet_1_1_1__1_1_1_j1": (2, 2, 2, 2, 2, 2),
        "tet_1_1_1__3_2_3_2_3_2_Delta": (2, 2, 2, 3, 3, 3),
        "tet_2_2_2__2_2_2_j2": (4, 4, 4, 4, 4, 4),
    }
    q1 = mp.mpf(1)
    tet_out = {}
    for label, six in configs.items():
        vq = q6j_racah_wigner(*six, q0)
        v1 = q6j_racah_wigner(*six, q1)
        tet_out[label] = {
            "at_q0": fmt(vq, dps=OUT_DPS),
            "at_q1": fmt(v1, dps=OUT_DPS),
            "ratio_q0_over_q1": fmt(vq / v1, dps=OUT_DPS),
        }

    return tet_out, max_6j_err


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        vol41 = vol_4_1_at(WORK_DPS)
        m_e = codata("electron mass energy equivalent in mev").value
        dm_np_exp = codata("neutron-proton mass difference energy equivalent in mev").value
        E0 = m_e / (q0 * (q0 - 1))
        tau_e = (q0**3) * (q0**4 + 1) / ((q0**2 + 1) ** 2)
        c_cat_abs = m_e / (-mp.log(tau_e))

        sym_jm = verify_jm_braid_commutativity_symbolic()
        f1_data, f1_err = run_family_1(q0, m_e, E0, c_cat_abs, dm_np_exp)
        y_D, y_GenDeg, eval_h3 = build_h3_reps(q0)
        f2_data, f2_err = run_family_2(q0, eval_h3, y_D, y_GenDeg)
        f3_data, f3_strict_ok, f3_err = run_family_3(q0, eval_h3, y_D)
        f4_data, f4_err = run_family_4(q0)

        wb = WitnessBuilder(
            "untapped_algebraic_invariants_proton_probe", engine="python+mpmath"
        )
        wb.set_description(
            "80-dps proton-pinned systematic audit across 4 untapped algebraic invariant families "
            "on O_q(SU(2)), U_q(sl_2), and H_n(q): (1) Woronowicz Haar KMS & spinor left/right GNS "
            "isospin dichotomy; (2) Jucys-Murphy symmetric center e_k(J) & chiral content skewness; "
            "(3) real-q0 framed GNS norms, Wenzl (2,1) SL(2,R) strain, and H_6/H_9 cabled satellites "
            "on the 2026-11-28 ruled lepton 3-braids; (4) Kirillov-Reshetikhin quantum 6j-symbols."
        )
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("out_dps", OUT_DPS)
        wb.add_parameter("q0_proton", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("vol_4_1", fmt(vol41, dps=OUT_DPS))
        wb.add_data("symbolic_jm_center_checks", sym_jm)
        wb.add_data("family1_oqsu2_haar_and_peter_weyl", f1_data)
        wb.add_data("family2_jucys_murphy_symmetric_center", f2_data)
        wb.add_data("family3_lepton_gns_strain_and_satellites", f3_data)
        wb.add_data("family4_quantum_6j_tetrahedral", f4_data)

        wb.add_assertion(
            "jm_braid_commutativity_full_twist_and_center_symbolic_h3_h4_h5",
            1 if sym_jm["all_passed"] else 0,
            1,
            "0",
            source="HeckeJucysMurphySymmetricCenter.lean (§1-§4 exact [CommRing R] theorems, bean qou-u9o1)",
        )
        wb.add_assertion(
            "oqsu2_spinor_3quark_left_q2_and_right_symmetric_haar_identities",
            fmt(f1_err, dps=15),
            "0",
            "1e-75",
            source="LeptonFramedGNSAndStrainOrder.lean O_q(SU(2)) spinor left/right GNS Haar identities",
        )
        wb.add_assertion(
            "h3_jm_central_scalars_and_muon_generic_degree_vanishing",
            fmt(f2_err, dps=15),
            "0",
            "1e-75",
            source="HeckeJucysMurphySymmetricCenter.lean & LeptonFramedGNSAndStrainOrder.tauGenDeg_mu_eq_zero",
        )
        wb.add_assertion(
            "wenzl_21_strain_det_one_and_electron_global_minimum_two",
            fmt(f3_err, dps=15),
            "0",
            "1e-75",
            source="LeptonFramedGNSAndStrainOrder.lean det G_{(2,1)}(W) = 1 & tr G_{(2,1)}(e) = 2",
        )
        wb.add_assertion(
            "real_q0_framed_gns_top_jm_and_3cable_strict_e_lt_mu_lt_tau",
            1 if f3_strict_ok else 0,
            1,
            "0",
            source="LeptonFramedGNSAndStrainOrder.lean strict real-q0 ordering I(e) < I(mu) < I(tau)",
        )
        wb.add_assertion(
            "quantum_6j_orthogonality_pentagon_and_tait_spinor_closed_forms",
            fmt(f4_err, dps=15),
            "0",
            "1e-75",
            source="Kirillov-Reshetikhin (1989) & Turaev-Viro (1992) Racah-Wigner 6j identities at q_0^(p)",
        )

        wb.add_caveat(
            "1. Strict proton pin (q_at(85)) with zero float64 and zero fitted parameters (NO FITTING EXCEPT CAL-1/2/3). "
            "2. Honest scale exclusion (Family 3): although ||W_tilde||_D^2, 1/tau_D(e_3(J) W), and 1/tau_D(psi^3 W) "
            "achieve strict I(e) < I(mu) < I(tau) at real q_0^(p), finite-strand polynomial invariants yield O(1-8) ratios "
            "and Q in [0.3337, 0.4617], excluding quantitative m_mu/m_e = 206.77 or m_tau/m_e = 3477.23 without the "
            "hbar_q^-2 Compton pole (CAL-2) or asymptotic N -> infinity volume scaling. "
            "3. Honest exclusion (Families 1 & 4): Peter-Weyl right-GNS norms give m_n > m_p linearly (+0.10396) "
            "but require a derived mass-chart scale E; untruncated Turaev-Viro state sums diverge at real q_0 > 1 "
            "and finite spin cutoffs break 2-3 Pachner invariance."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
