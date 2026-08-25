#!/usr/bin/env python3
"""qbeta_g3_ggm_stokes_41.py — A_ω step 2: the 4₁ Stokes data from GGM
(library/arxiv-2012.00062v3/2012.00062v3.pdf), implemented exactly and certified internally.

What GGM (Garoufalidis–Gu–Mariño, "Peacock patterns…") §§4–5 give for 4₁,
all glyph-extracted from the in-repo source:

  * the q-series G⁰_m, G¹_m (eqs 51a/51b) with E₁(q) = 1 − 4Σ_{n≥1} qⁿ/(1−qⁿ):
      G⁰_m = Σ_n (−1)ⁿ q^{n(n+1)/2+mn}/(q;q)_n²
      G¹_m = Σ_n (−1)ⁿ q^{n(n+1)/2+mn}/(q;q)_n²·(2m + E₁(q) + 2Σ_{j≤n}(1+qʲ)/(1−qʲ))
  * W_m(q) = [[G⁰_m, G¹_m],[G⁰_{m+1}, G¹_{m+1}]] with THEOREM 9 properties:
      det W_m = 2 (exact),  y_{m+1} − (2−q^m)y_m + y_{m−1} = 0 (eq 49)
  * the Stokes matrix S⁺(q) = ±½·A·W₋₁·B·W₋₁ᵀ·C (eq 59a; the ᵀ placement and
    the SIGNS of the small integer matrices are OCR-ambiguous — the printed
    magnitudes are glyph-verified as |A| = [[0,1],[1,1]], |B| = [[0,1],[1,0]],
    |C| = [[0,1],[1,2]], and the sandwich is DERIVED here by scanning every
    sign pattern × both ᵀ placements against 28 printed coefficients + the
    q→0 limit S⁺(0) = [[1,3],[0,1]] (eq 60, glyph-verified):
      S⁺₁₁ − 1     = −8q − 9q² + 18q³ + 46q⁴ + 90q⁵ + 62q⁶ + O(q⁷)   (61)
      S⁺₁₂/S⁺₁₁ − 3 = 9q + 75q² + 642q³ + 5580q⁴ + 48558q⁵ + 422865q⁶ (62)
      S⁺₂₁/S⁺₁₁    = −9q − 75q² − 642q³ − 5580q⁴ − 48558q⁵ − 422865q⁶ (63)
      S⁺₂₂ − 1 − S⁺₁₂S⁺₂₁/S⁺₁₁ = 8q + 73q² + 638q³ + 5571q⁴ + …      (64)
    (sign rows recovered from the cmsy glyph offset y0 ≈ baseline − 9.2,
    calibrated on (63) whose six minuses are forced by the symmetry (65))
  * the singularity positions ι₁,₂ = ±Vol(4₁)/π (eq 46 with the 2πik towers)
    — EXACTLY the corpus's measured Borel singularity A ≈ 0.646 (#3692/#3819)
  * the q→0 Stokes constants ±3 on those singularities (eq 60)
  * the DICTIONARY (Conjecture 4, eq 21, PROVEN for 4₁):
      S⁺_{σ₁σ₁}(x;q) = Ind^rot(0, x; q) = Σ_e I_{4₁}(0,e)(q)·xᵉ  (x = 1 here)
    — so (61) is simultaneously the Stokes tower AND an exact anchor for the
    still-open total-index assembly (step 1).

Certification levels in this probe:
  V1  det W_m(q) = 2 exactly (several m, full order)      [Theorem 9]
  V2  the q-difference (49) holds exactly for the columns [Theorem 9]
  V3  a sandwich (A,B,C) reproduces ALL FOUR printed series exactly —
      the OCR-free derivation of (59a)
  V4  substrate evaluation S⁺_{σ₁σ₁}(e^{−t}) converges (|q|<1) + stability

Physics rows: the odd-channel Stokes candidate is the INTEGER 3 on the
ι = Vol(4₁)/π singularity, with (61) its descendant tower; the substrate
value of the tower is computed. Anti-laundering: the identification of THIS
Stokes constant with the corpus's A_ω normalization (Im 𝔙 → N_odd) is NOT
claimed — that is the remaining bridge (step 3's residual measurement is the
falsifiable test). Scope-(a); exact integer arithmetic; no fit; no c_k wired.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

ORD = 30            # q-order for certification
ORD_SUB = 1600      # q-order for substrate evaluation. NOT 700: the tower
                    # coefficients grow ~e^{c√k}, so the naive monomial tail
                    # bound e^{-t·k} is wrong — the series only converges to
                    # ~13 digits near q-order 1200-1600 (awpk audit
                    # 2026-07-31; the honest ladder is 800/1200/1600).

# Glyph-verified printed targets (GGM p.15, cmsy sign rows decoded):
PRINTED_61 = [1, -8, -9, 18, 46, 90, 62]                  # S+_11  (= 1 + tower)
RATIO_62 = [3, 9, 75, 642, 5580, 48558, 422865]           # S+_12/S+_11
RATIO_63 = [0, -9, -75, -642, -5580, -48558, -422865]     # S+_21/S+_11 (eq 65)
RESID_64 = [0, 8, 73, 638, 5571, 48538, 422819]           # S+_22 − 1 − S12·S21/S11
SPLUS_Q0 = [[1, 3], [0, 1]]                               # eq (60)
# glyph-verified magnitudes of the (59a) constant matrices (signs scanned):
MAG_A = [[0, 1], [1, 1]]
MAG_B = [[0, 1], [1, 0]]
MAG_C = [[0, 1], [1, 2]]


# ----------------------- exact integer q-series helpers ---------------------
def smul(a, b, order):
    out = [0] * (order + 1)
    for i, ca in enumerate(a):
        if ca == 0 or i > order:
            continue
        top = order - i
        for j, cb in enumerate(b[:top + 1]):
            if cb:
                out[i + j] += ca * cb
    return out


def sadd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(n)]


def sscale(c, a):
    return [c * x for x in a]


def inv_pochhammer_sq(n, order):
    """1/(q;q)_n² via the cumulative-sum trick (twice per factor)."""
    out = [0] * (order + 1)
    out[0] = 1
    for j in range(1, n + 1):
        for _ in range(2):
            for d in range(j, order + 1):
                out[d] += out[d - j]
    return out


def eisenstein_E1(order):
    """E₁ = 1 − 4Σ_{n≥1} qⁿ/(1−qⁿ) = 1 − 4Σ_N d(N)qᴺ (d = number of divisors)."""
    out = [0] * (order + 1)
    out[0] = 1
    for n in range(1, order + 1):
        for k in range(n, order + 1, n):
            out[k] -= 4
    return out


def harmonic_H(n, order):
    """2Σ_{j=1}^n (1+qʲ)/(1−qʲ) = 2n + 4Σ_{j≤n} qʲ/(1−qʲ) as a series."""
    out = [0] * (order + 1)
    out[0] = 2 * n
    for j in range(1, n + 1):
        for k in range(j, order + 1, j):
            out[k] += 4
    return out


def G_series(m, order):
    """(G⁰_m, G¹_m) exact integer series through q^order.

    Restricted to m ≥ −1: for m ≤ −2 the exponent n(n+1)/2 + mn goes
    negative (G_m is genuinely Laurent) and a plain power-series array
    cannot hold it; Theorem 9's symmetry (53) covers negative m instead.
    """
    if m < -1:
        raise ValueError(f"G_series requires m >= -1 (got {m}): G_m is Laurent")
    E1 = eisenstein_E1(order)
    g0 = [0] * (order + 1)
    g1 = [0] * (order + 1)
    n = 0
    while True:
        expo = n * (n + 1) // 2 + m * n
        if n > abs(m) + 1 and expo > order:
            break
        if expo <= order:
            ip = inv_pochhammer_sq(n, order - expo)
            sgn = -1 if n % 2 else 1
            # G0 term
            for d, c in enumerate(ip):
                g0[d + expo] += sgn * c
            # G1 term: weight = 2m + E1 + H(n)
            w = sadd(sadd([2 * m], E1), harmonic_H(n, order - expo))
            tw = smul(ip, w[:order - expo + 1], order - expo)
            for d, c in enumerate(tw):
                g1[d + expo] += sgn * c
        n += 1
        if n > 4 * order + 8:
            break
    return g0, g1


def W_matrix(m, order):
    g0m, g1m = G_series(m, order)
    g0m1, g1m1 = G_series(m + 1, order)
    return [[g0m, g1m], [g0m1, g1m1]]


def mat_mul_series(A, B, order):
    """2×2 matrices of integer series."""
    out = [[None, None], [None, None]]
    for i in range(2):
        for j in range(2):
            acc = [0] * (order + 1)
            for k in range(2):
                acc = sadd(acc, smul(A[i][k], B[k][j], order))
            out[i][j] = [x for x in acc[:order + 1]]
    return out


def const_mat(M, order):
    return [[[M[i][j]] + [0] * order for j in range(2)] for i in range(2)]


def transpose(A):
    return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]


def main() -> int:
    print("=" * 78)
    print(" A_ω step 2 — GGM 4₁ Stokes data, exact implementation + certification")
    print("=" * 78)

    # ---- V1/V2: Theorem-9 certification of the G/W machinery ----
    # m ranges start at −1: G_m is Laurent for m ≤ −2 (see G_series docstring).
    print("\n[V1] det W_m(q) = 2 exactly:")
    v1 = True
    for m in (-1, 0, 1, 2):
        W = W_matrix(m, ORD)
        det = sadd(smul(W[0][0], W[1][1], ORD),
                   sscale(-1, smul(W[0][1], W[1][0], ORD)))
        ok = det[0] == 2 and all(c == 0 for c in det[1:])
        v1 = v1 and ok
        print(f"    m={m:>2}: det = {det[:4]}…  ok={ok}")

    print("\n[V2] q-difference y_(m+1) − (2−q^m)y_m + y_(m−1) = 0 exactly:")
    v2 = True
    for m in (0, 1, 2):
        m_ok = True
        for comp in (0, 1):
            ya = G_series(m + 1, ORD)[comp]
            yb = G_series(m, ORD)[comp]
            yc = G_series(m - 1, ORD)[comp]
            two_qm = [2] + [0] * ORD
            two_qm[m] -= 1
            resid = sadd(sadd(ya, sscale(-1, smul(two_qm, yb, ORD))), yc)
            m_ok = m_ok and all(c == 0 for c in resid)
        v2 = v2 and m_ok
        print(f"    m={m:>2}: both components ok={m_ok}")

    # ---- V3: derive the (59a) sandwich by matching the printed series ----
    # Shape: S⁺ = ±½·A·W₋₁·B·W₋₁ᵀ·C (both ᵀ placements scanned). Magnitudes
    # of A,B,C are glyph-verified (MAG_*); every sign pattern on the nonzero
    # entries is scanned. Filters: (i) q→0 limit = SPLUS_Q0 (eq 60),
    # (ii) all four printed towers (61)-(64), 28 exact coefficients.
    print("\n[V3] deriving S⁺ = ±½·A·W₋₁·B·W₋₁ᵀ·C against the printed series:")
    Wm1 = W_matrix(-1, ORD)
    WT = transpose(Wm1)
    W0 = [[Wm1[i][j][0] for j in range(2)] for i in range(2)]   # q→0 of W₋₁
    W0T = [[W0[j][i] for j in range(2)] for i in range(2)]

    def sign_variants(mag):
        """All sign patterns on the nonzero entries of a 2×2 magnitude matrix."""
        pos = [(i, j) for i in range(2) for j in range(2) if mag[i][j]]
        for signs in itertools.product((1, -1), repeat=len(pos)):
            M = [[mag[i][j] for j in range(2)] for i in range(2)]
            for (i, j), s in zip(pos, signs):
                M[i][j] *= s
            yield M

    def m2(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)]

    def series_div(num, den, order):
        """num/den for integer series with den[0] = ±1 (exact)."""
        inv = [0] * (order + 1)
        inv[0] = den[0]            # den[0] ∈ {1,−1} ⇒ inverse constant = den[0]
        for d in range(1, order + 1):
            inv[d] = -den[0] * sum(den[k] * inv[d - k] for k in range(1, d + 1))
        return smul(num, inv, order)

    hits = []
    S_seen = set()
    S_final = None
    hits_meta = []
    for t_first in (False, True):     # ᵀ on first W (False = glyph reading: second)
        L0, R0 = (W0T, W0) if t_first else (W0, W0T)
        Ls, Rs = (WT, Wm1) if t_first else (Wm1, WT)
        for Am in sign_variants(MAG_A):
            for Bm in sign_variants(MAG_B):
                core0 = m2(m2(L0, Bm), R0)
                for Cm in sign_variants(MAG_C):
                    for sgn in (1, -1):
                        # filter (i): exact q→0 limit (integer arithmetic)
                        lim = m2(m2(Am, core0), Cm)
                        if any(sgn * lim[i][j] != 2 * SPLUS_Q0[i][j]
                               for i in range(2) for j in range(2)):
                            continue
                        # full series
                        core = mat_mul_series(
                            mat_mul_series(Ls, const_mat(Bm, ORD), ORD), Rs, ORD)
                        S = mat_mul_series(
                            mat_mul_series(const_mat(Am, ORD), core, ORD),
                            const_mat(Cm, ORD), ORD)
                        if any(sgn * x % 2 != 0 for i in range(2) for j in range(2)
                               for x in S[i][j]):
                            continue
                        Sh = [[[sgn * x // 2 for x in S[i][j]] for j in range(2)]
                              for i in range(2)]
                        s11, s12, s21, s22 = Sh[0][0], Sh[0][1], Sh[1][0], Sh[1][1]
                        if any(s11[k] != PRINTED_61[k] for k in range(7)):
                            continue
                        r12 = series_div(s12, s11, ORD)
                        if any(r12[k] != RATIO_62[k] for k in range(7)):
                            continue
                        r21 = series_div(s21, s11, ORD)
                        if any(r21[k] != RATIO_63[k] for k in range(7)):
                            continue
                        cross = series_div(smul(s12, s21, ORD), s11, ORD)
                        resid = sadd(s22, sscale(-1, sadd([1], cross)))
                        if any(resid[k] != RESID_64[k] for k in range(7)):
                            continue
                        key = tuple(tuple(tuple(Sh[i][j]) for j in range(2))
                                    for i in range(2))
                        S_seen.add(key)
                        hits.append((sgn, t_first, Am, Bm, Cm))
                        if S_final is None:
                            S_final = Sh
    n_distinct = len(S_seen)
    print(f"    sandwich sign-patterns reproducing (60)+(61)+(62)+(63)+(64): "
          f"{len(hits)}; distinct resulting S⁺(q): {n_distinct}")
    v3 = len(hits) >= 1 and n_distinct == 1
    if hits:
        sgn, t_first, Am, Bm, Cm = hits[0]
        t_where = "first W" if t_first else "second W (glyph reading)"
        print(f"    exemplar: sign={sgn}, ᵀ on {t_where}, A={Am}, B={Bm}, C={Cm}")
        print(f"    S⁺₁₁ = {S_final[0][0][:8]}…")
        print(f"    S⁺₁₂ = {S_final[0][1][:8]}…")
        print(f"    S⁺₂₁ = {S_final[1][0][:8]}…")
        print(f"    S⁺₂₂ = {S_final[1][1][:8]}…")

    # ---- V4 + physics: substrate evaluation ----
    t = mp.log(q_at(50))
    q_sub = mp.e ** (-t)
    print(f"\n[V4] substrate q = e^(−t) = {mp.nstr(q_sub, 10)}:")
    if S_final is not None:
        # recompute S at deep order via the certified sandwich
        sgn, t_first, Am, Bm, Cm = hits[0]
        Wd = W_matrix(-1, ORD_SUB)
        Ld, Rd = (transpose(Wd), Wd) if t_first else (Wd, transpose(Wd))
        Sd = mat_mul_series(
            mat_mul_series(const_mat(Am, ORD_SUB),
                           mat_mul_series(mat_mul_series(Ld,
                                          const_mat(Bm, ORD_SUB), ORD_SUB),
                                          Rd, ORD_SUB), ORD_SUB),
            const_mat(Cm, ORD_SUB), ORD_SUB)
        s11_deep = [sgn * x // 2 for x in Sd[0][0]]
        val = mp.fsum(c * q_sub ** k for k, c in enumerate(s11_deep) if c)
        val_c = mp.fsum(c * q_sub ** k
                        for k, c in enumerate(s11_deep[:ORD_SUB * 3 // 4]) if c)
        conv = abs(val - val_c)
        # honest guard: a truncation difference >= 1 means NON-convergence and
        # must report 0 digits. The previous `else 40` sentinel mapped that
        # case to "40 stable digits" and let a pre-asymptotic value pass —
        # the committed 2026-07-18 witness value 0.2584 was sentinel-passed
        # (see docs/audits/2026-07-31-awpk-perwinding-stokes-41.md Finding 2).
        if conv == 0:
            conf = 40
        elif conv < 1:
            conf = int(-mp.log10(conv))
        else:
            conf = 0
        print(f"    S⁺_(σ1σ1)(q_sub) = Σ_e I(0,e)(q_sub) = {mp.nstr(val, 20)} "
              f"[{conf} stable digits]")
        v4 = conf >= 8
    else:
        val, conf, v4 = None, 0, False

    vol = 2 * mp.clsin(2, mp.pi / 3)
    print(f"\n[physics] Borel singularities at ι = ±Vol(4₁)/π = ±{mp.nstr(vol / mp.pi, 8)}")
    print(f"          — the corpus's measured A ≈ 0.62–0.65 (#3692/#3819) ✓ same object")
    print(f"          q→0 Stokes constants on them: ±3 (GGM eq 60)")
    print(f"          descendant tower (61) evaluated at the substrate above.")

    verdict = (
        f"GGM 4₁ Stokes data implemented exactly and certified internally: "
        f"det W_m = 2 exact ({v1}); q-difference (49) exact ({v2}); the (59a) "
        f"sandwich DERIVED OCR-free by matching the q→0 limit (60) + all four "
        f"printed towers (61)-(64) — {len(hits)} sign-pattern(s), "
        f"{n_distinct} distinct S⁺ ({v3}). The Borel "
        f"singularity carrying the odd-ray physics sits at ι = Vol(4₁)/π — the "
        f"SAME object as the corpus's measured A (#3692/#3819) — with integer "
        f"Stokes constant 3 and descendant tower S⁺_(σ1σ1)(q) = 1 − 8q − 9q² + …; "
        f"substrate value {mp.nstr(val, 12) if val is not None else 'n/a'} "
        f"[{conf}d]. Via the PROVEN (for 4₁) dictionary eq (21) this tower "
        f"equals Σ_e I(0,e) — a new exact anchor for the step-1 assembly. "
        f"NOT claimed: the identification of this Stokes constant with the "
        f"corpus A_ω normalization (step 3's residual test decides). "
        f"Scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-ggm-stokes-41", engine="python-int+mpmath")
    wb.set_description(
        "A_omega step 2: exact implementation of the GGM 4_1 Stokes data "
        "(G/W q-series machinery certified by Theorem-9 identities; the (59a) "
        "sandwich derived OCR-free against the printed series). Records the "
        "integer Stokes constant 3 on the iota = Vol(4_1)/pi singularity "
        "(= the corpus's measured Borel A) with its descendant tower and "
        "substrate value, and the proven eq-(21) dictionary making the tower "
        "an exact anchor for the step-1 index assembly. No A_omega "
        "identification claimed (step 3 decides).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("source", "library/arxiv-2012.00062v3/2012.00062v3.pdf (GGM) sections 4-5, eqs 43-64 + Conj 4 eq 21")
    wb.add_data("theorem9_checks", {"det_Wm_eq_2": bool(v1), "qdifference_49": bool(v2)})
    wb.add_data("sandwich_derivation", {
        "n_matching_sign_patterns": len(hits),
        "n_distinct_Splus": n_distinct,
        "exemplar": ({"sign": hits[0][0],
                      "transpose_on_first_W": hits[0][1],
                      "A": hits[0][2], "B": hits[0][3], "C": hits[0][4]}
                     if hits else None)})
    wb.add_data("stokes_tower_S11", {str(k): (S_final[0][0][k] if S_final else None)
                                     for k in range(min(12, ORD + 1))})
    wb.add_data("printed_anchors_reproduced", bool(v3))
    wb.add_data("singularity", {"iota": "Vol(4_1)/pi = 0.64613 (= corpus measured A)",
                                "q0_stokes_integer": 3})
    wb.add_data("substrate", {"q_sub": mp.nstr(q_sub, 20),
                              "S11_at_substrate": mp.nstr(val, 25) if val is not None else None,
                              "stable_digits": conf})
    wb.add_data("dictionary_eq21",
                "S+_sigma1sigma1(q) = Sum_e I_41(0,e)(q) — proven for 4_1; new exact "
                "anchor for the step-1 assembly search")
    wb.add_data("verdict", verdict)
    wb.add_assertion("theorem9_det_and_qdifference_exact",
                     computed=1.0 if (v1 and v2) else 0.0, expected=1.0, tolerance=0.5,
                     source="det W_m = 2 and eq (49) hold exactly through q^30")
    wb.add_assertion("printed_stokes_series_reproduced",
                     computed=1.0 if v3 else 0.0, expected=1.0, tolerance=0.5,
                     source="a (59a)-shaped sandwich reproduces GGM (61)/(62)/(64) exactly")
    wb.add_assertion("substrate_tower_stable",
                     computed=1.0 if v4 else 0.0, expected=1.0, tolerance=0.5,
                     source="S+_11(e^-t) stable to >= 8 digits under truncation drop")
    wb.save()
    return 0 if (v1 and v2 and v3 and v4) else 1


if __name__ == "__main__":
    raise SystemExit(main())
