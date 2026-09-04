#!/usr/bin/env python3
"""Friedrichs-vs-Krein selection: what each candidate principle actually implies.

Bean: qou-f6sm.  Audit: docs/audits/2026-08-01-fvk-selection-framing.md.
Parents:
  docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md  (F/K computed)
  docs/audits/2026-08-01-ksel2id-u1-promotion.md                  (F/K = complementary
                                                                   sublattices of ONE
                                                                   u ≡ 1 class)
  docs/audits/2026-08-01-awzero-asymptotics.md                    (supp K = zeros(A_w),
                                                                   supp F = zeros/q̃)
  docs/audits/2026-08-01-ksel3-modular-double-covariance.md       (precedent: two natural
                                                                   covariance notions pin
                                                                   DIFFERENT kernels)

THE QUESTION.  Which self-adjoint extension of the canonical Jacobi operator J(q)
of the balanced moment functional m_k = q^{-k(k-1)/4}[k]_q!  is distinguished?
F and K sit in the SAME u ≡ 1 lattice class on complementary sublattices, exactly
one q̃-step apart, so no lattice/class result can decide between them.  This probe
tests the operator-level and substrate-level content of four candidate principles.

WHAT IS TESTED (nothing is fitted; every scored item is an exact identity or a
check of a DISPLAYED relation at a stated tolerance).

  V1  S-map algebra, EXACT (sympy).  The "multiply by s, rescale by q̃" map is
      J ↦ q̃^{-1}·LR(J), where LR is the sqrt-free Christoffel/LR step
        e_k = β_{k+1}/l_k,  l_{k+1} = α_{k+1} − e_k,
        α'_k = l_k + e_k,   β'_k = l_k·e_{k−1}.
      For the Stieltjes–Wigert core (α_k = v^{k−1}(v^k(1+v) − 1),
      β_{k+1} = v^{3k}(v^{k+1} − 1), v = q̃) this map is an EXACT fixed point:
      α'_k = v·α_k, β'_k = v²·β_k.  Symbolic, general k in the checked range.
      For the balanced family it is NOT a fixed point: the obstruction is exactly
      the Jackson factor (1 − p^{k+1}) (exact symbolic), decaying geometrically.

  V2  Therefore F = S(K) EXACTLY at every truncation order for the SW core:
      Gauss–Radau-at-0 on N points and plain Gauss on N−1 points satisfy
        λ^K_j = q̃·λ^F_{j−1},     λ^K_j·w^K_j = w^F_{j−1}.
      Consequence for the framing: the F/K choice IS the choice of s-power in the
      measure (ds versus s·ds) — i.e. the conjecture's own ς·ds/s normalization,
      one level down.  Measured deviation for the balanced family.

  V3  The computational-time (ds/s) diagnostic.  For a representing measure μ of
      the balanced moments, the conjecture's object is ν with μ = s·ν (its
      s^n-moments are the normalizers N(n) = m_{n−1}).  The harmonic moment
        I(μ) := ∫ s^{-1} dμ = (J^{-1})_{00}
      is the total ν-mass.  Along the nonnegative-extension arc [K, F]:
      I is finite for every member except Krein, where it is EXACTLY +∞ (the
      truncated matrix is exactly singular at the Radau boundary shift), and it
      is MINIMIZED at Friedrichs.  Verified: strict monotonicity along the arc,
      d_0(t_N) → 0, the identity I = Σ_j w_j/λ_j, and monotone-in-N lower bounds.

  V4  P3 orthogonality, exact reason.  KSel-3's dual-mode criteria are defined on
      lattice samplings of the Gaussian LN(−L/2, L) at step L, where σ² = L =
      step is exactly what makes the dual modes moment-blind.  The F/K supports
      are lattices of step 2L, so the k-th moment shift kσ² = kL is a lattice
      vector only for EVEN k: the mechanism fails at odd k, the criteria have no
      domain of definition on the extension circle.  Corroborated numerically:
      the F masses are not proportional to the Gaussian evaluated at the F atoms.

  V5  P4 non-selection.  Every arc member reproduces every moment (checked to
      k ≤ 30); the harmonic moment is the first functional that separates them,
      and it separates them by ∞.  Quantifies "the ambiguity is invisible to
      moments" — the corpus's only current consumer class.

  V6  The decisive-test dry run (EXPLORATORY, no assertion on the physics).
      If μ_F ≈ e^{-s}ds truncated below its spectral gap, then
        I_F(q) + ln λ_F(q)  →  −γ  as q → 1⁺
      (since ∫_λ^∞ e^{-s}ds/s = E₁(λ) = −γ − ln λ + O(λ)) — a parameter-free,
      falsifiable comparison against the ζ-regularized finite part of N(0).  The
      same quantity is computed for a MID-ARC member: if it also tends to −γ, the
      test does not discriminate F from the rest of the arc and only excludes K.
      Reported at measured tier with the pre-asymptotic caveat; no fit.

Audit-only.  Nothing wired; no content block or production script touched.
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import time
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, nstr, log as mlog, sqrt as msqrt, euler as meuler

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "fvk-selection.witness.json"

_MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"
Q0_MUON_STR = json.loads(_MUON_WITNESS.read_text())["q0Value"]
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

t0 = time.time()
results: dict = {}


def log(msg: str) -> None:
    print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)


def fmt(x, d: int = 12) -> str:
    return nstr(mpf(x), d)


# --------------------------------------------------------------- machinery

def qint(qv, k: int):
    """[k]_q = 1 + q + ... + q^{k-1}, field-agnostic."""
    s = qv * 0
    x = qv ** 0
    for _ in range(k):
        s = s + x
        x = x * qv
    return s


def balanced_moments(rv, kmax: int):
    """m_k = r^{-k(k-1)} [k]_{r^4}!  with r = q^{1/4}  (=  q^{-k(k-1)/4}[k]_q!)."""
    q = rv ** 4
    out = []
    for k in range(kmax + 1):
        f = rv ** 0
        for j in range(1, k + 1):
            f = f * qint(q, j)
        out.append(rv ** (-k * (k - 1)) * f)
    return out


def sw_moments(v, kmax: int):
    """Stieltjes-Wigert core moments G_k = v^{k(k-1)/2},  v = q̃ = sqrt(q)."""
    return [v ** ((k * (k - 1)) // 2) if (k * (k - 1)) % 2 == 0
            else v ** sp.Rational(k * (k - 1), 2) for k in range(kmax + 1)]


def sw_jacobi(v, K: int):
    """Closed-form SW monic Jacobi data (u1-promotion A-1, content-block index):
       α_k = v^{k-1}(v^k(1+v) − 1),  β_{k+1} = v^{3k}(v^{k+1} − 1)."""
    al = [v ** (k - 1) * (v ** k * (1 + v) - 1) for k in range(K)]
    be = [v ** (3 * k) * (v ** (k + 1) - 1) for k in range(K - 1)]
    return al, be


def qd_jacobi(ms, K):
    """Monic Jacobi data from moments by the quotient-difference algorithm
    (Rutishauser; Henrici; Gautschi).  Field-agnostic."""
    N = len(ms) - 1
    qc = [ms[n + 1] / ms[n] for n in range(N)]
    ec = [ms[0] * 0] * N
    q0 = [qc[0]]
    e0 = []
    for _k in range(1, K):
        en = [qc[n + 1] - qc[n] + ec[n + 1] for n in range(len(qc) - 1)]
        qn = [qc[n + 1] * en[n + 1] / en[n] for n in range(len(en) - 1)]
        e0.append(en[0])
        if qn:
            q0.append(qn[0])
        qc, ec = qn, en
        if not qc:
            break
    al = [q0[0]] + [q0[k] + e0[k - 1] for k in range(1, len(q0))]
    be = [q0[k - 1] * e0[k - 1] for k in range(1, min(len(q0), len(e0)) + 1)]
    return al, be


def lr_step(al, be):
    """Sqrt-free Christoffel/LR step at shift 0: the Jacobi data of s·dμ.
       J = L·U (L unit lower bidiagonal, U upper bidiagonal); J' = U·L.
         l_0 = α_0;  e_k = β_{k+1}/l_k;  l_{k+1} = α_{k+1} − e_k
         α'_k = l_k + e_k;  β'_k = l_k·e_{k−1}."""
    n = min(len(al), len(be) + 1)
    lvals = [al[0]]
    evals = []
    for k in range(n - 1):
        evals.append(be[k] / lvals[k])
        lvals.append(al[k + 1] - evals[k])
    alp = [lvals[k] + (evals[k] if k < len(evals) else lvals[0] * 0)
           for k in range(n)]
    bep = [lvals[k] * evals[k - 1] for k in range(1, n)]
    return alp[:n - 1], bep[:n - 1]


def monic_p_at_zero(al, be, K):
    """Monic OPs at 0: P_0 = 1, P_1(0) = −α_0, P_{n+1}(0) = −α_n P_n − β_n P_{n−1}."""
    P0 = [al[0] * 0 + 1, -al[0]]
    for n in range(1, K):
        P0.append(-al[n] * P0[n] - be[n - 1] * P0[n - 1])
    return P0


def sym_trunc_eig(al, be, N, tshift=None):
    """Eigen-decomposition of the symmetric N-truncation (diag α, off-diag √β),
       with an optional boundary shift on the last diagonal entry."""
    A = mp.zeros(N)
    for i in range(N):
        A[i, i] = al[i]
        if i + 1 < N:
            A[i, i + 1] = A[i + 1, i] = msqrt(be[i])
    if tshift is not None:
        A[N - 1, N - 1] += tshift
    E, EV = mp.eigsy(A)
    return [E[i] for i in range(N)], [EV[0, i] ** 2 for i in range(N)]


def inv00(al, be, N, tshift=None):
    """(A_N^{-1})_{00} = 1/d_0 with d_{N-1} = a_{N-1}, d_i = a_i − β_{i+1}/d_{i+1}.
       Returns (value, d_0).  d_0 = 0 ⟺ A_N singular ⟺ harmonic moment +∞."""
    d = al[N - 1] + (tshift if tshift is not None else al[0] * 0)
    for i in range(N - 2, -1, -1):
        d = al[i] - be[i] / d
    return (None if d == 0 else 1 / d), d


def sturm_count(al, be, N, z):
    """Number of eigenvalues of the N-truncation strictly below z."""
    tiny = mpf(10) ** (-mp.dps + 10)
    d = al[0] - z
    neg = 1 if d < 0 else 0
    for i in range(1, N):
        if d == 0:
            d = tiny
        d = (al[i] - z) - be[i - 1] / d
        if d < 0:
            neg += 1
    return neg


def lambda_min(al, be, N, hi):
    """Smallest eigenvalue of the N-truncation, by Sturm bisection on (0, hi)."""
    lo = mpf(0)
    for _ in range(int(3.4 * mp.dps) + 40):
        mid = (lo + hi) / 2
        if sturm_count(al, be, N, mid) >= 1:
            hi = mid
        else:
            lo = mid
        if hi - lo < mpf(10) ** (-mp.dps + 12) * max(hi, mpf(1)):
            break
    return (lo + hi) / 2


# ---------------------------------------------------- V1  exact S-map algebra

def block_v1_smap_algebra():
    log("V1  S-map / LR-step algebra (sympy exact)")
    v = sp.symbols("v", positive=True)
    K = 7
    al = [sp.simplify(v ** (k - 1) * (v ** k * (1 + v) - 1)) for k in range(K)]
    be = [sp.simplify(v ** (3 * k) * (v ** (k + 1) - 1)) for k in range(K - 1)]

    # self-test: closed form reproduces qd on the SW moments G_k
    G = sw_moments(v, 2 * K)
    alq, beq = qd_jacobi(G, K)
    for k in range(4):
        assert sp.simplify(sp.together(alq[k] - al[k])) == 0, ("sw alpha", k)
    for k in range(3):
        assert sp.simplify(sp.together(beq[k] - be[k])) == 0, ("sw beta", k)

    # exact S-fixedness of the moments:  v^{-k} G_{k+1}/G_1 = G_k
    for k in range(9):
        assert sp.simplify(v ** (-k) * G[k + 1] / G[1] - G[k]) == 0, ("S-moment", k)

    # the LR step scales the SW Jacobi matrix by exactly (v, v²)
    alp, bep = lr_step(al, be)
    n_al = len(alp)
    for k in range(n_al):
        assert sp.simplify(sp.together(alp[k] - v * al[k])) == 0, ("LR alpha", k)
    for k in range(len(bep)):
        assert sp.simplify(sp.together(bep[k] - v ** 2 * be[k])) == 0, ("LR beta", k)

    # balanced family: the obstruction is exactly the Jackson factor
    r = sp.symbols("r", positive=True)
    q = r ** 4
    p = 1 / q
    E = 1 / (1 - p)
    m = balanced_moments(r, 12)
    for k in range(10):
        want = r ** (2 * k) * E * (1 - p ** (k + 1))
        assert sp.simplify(sp.together(m[k + 1] / m[k] - want)) == 0, ("bal ratio", k)
    # S-fixedness with ANY constant c would need m_{k+1}/m_k = c^k·m_1 = c^k;
    # the ratio of consecutive ratios must then be constant in k.  It is not:
    rr = sp.simplify(sp.together(
        (m[2] / m[1]) / (m[1] / m[0]) / ((m[3] / m[2]) / (m[2] / m[1]))))
    assert sp.simplify(rr - 1) != 0, "balanced would be S-fixed"
    rr_s = sp.simplify(rr)

    out = {
        "sw_jacobi_closed_form_matches_qd": "exact, k ≤ 3 (α), k ≤ 2 (β), symbolic in v",
        "sw_moment_S_fixed": "v^{-k} G_{k+1}/G_1 = G_k exact for k ≤ 8",
        "LR_step_scales_SW_by_(v, v^2)": f"exact, α: k < {n_al}, β: k < {len(bep)}",
        "balanced_ratio_identity": "m_{k+1}/m_k = q̃^k E (1 − p^{k+1}) exact, k ≤ 9",
        "balanced_not_S_fixed_witness": sp.srepr(rr_s)[:0] or str(rr_s),
        "reading": ("the S-map (multiply by s, rescale by q̃) is J ↦ q̃^{-1}·LR(J); "
                    "the SW core is an EXACT fixed point, the balanced family is "
                    "not, and the whole obstruction is the Jackson factor "
                    "(1 − p^{k+1}) → 1 geometrically"),
    }
    log("V1  done — LR fixed-point identity exact")
    return out


# ------------------------------------- V2  F = S(K) exactly at every order (SW)

def block_v2_f_equals_s_of_k(v_num, N):
    log(f"V2  F = S(K) at finite order — SW core, N = {N}")
    mp.dps = 200
    v = mpf(v_num)
    al, be = sw_jacobi(v, N + 4)
    P0 = monic_p_at_zero(al, be, N + 1)
    tN = P0[N] / P0[N - 1]
    assert tN < 0, "Radau shift must be negative for a Stieltjes measure"
    mp.dps = 120
    alf = [+a for a in al]
    bef = [+b for b in be]
    lamK, wK = sym_trunc_eig(alf, bef, N, tshift=+tN)
    lamF, wF = sym_trunc_eig(alf, bef, N - 1)
    assert abs(lamK[0]) < mpf("1e-60"), lamK[0]

    node_dev, mass_dev = [], []
    for j in range(1, min(N - 1, 12)):
        node_dev.append(abs(lamK[j] / (v * lamF[j - 1]) - 1))
        mass_dev.append(abs(lamK[j] * wK[j] / wF[j - 1] - 1))
    worst_node, worst_mass = max(node_dev), max(mass_dev)
    assert worst_node < mpf("1e-40"), worst_node
    assert worst_mass < mpf("1e-40"), worst_mass

    out = {
        "N": N, "q_tilde": fmt(v),
        "radau_zero_node": fmt(abs(lamK[0]), 4),
        "worst_node_rel_dev": fmt(worst_node, 4),
        "worst_mass_rel_dev": fmt(worst_mass, 4),
        "statement": ("SW core: λ^K_j = q̃·λ^F_{j−1} and λ^K_j·w^K_j = w^F_{j−1} "
                      "at every truncation order — the Friedrichs measure IS the "
                      "s-multiplied, q̃-rescaled Krein measure (Christoffel/LR)"),
        "consequence": ("the F/K choice is exactly the choice of s-power in the "
                        "measure: ds versus s·ds.  It is the conjecture's own "
                        "ς·ds/s normalization one level down, not an independent "
                        "degree of freedom"),
    }
    log(f"V2  done — node dev {fmt(worst_node, 3)}, mass dev {fmt(worst_mass, 3)}")
    return out


def block_v2b_balanced_smap_deviation(r_num, K):
    log("V2b balanced: measured failure of exact S-covariance")
    mp.dps = 400
    r = mpf(r_num)
    v = r ** 2
    ms = balanced_moments(r, 2 * K + 2)
    al, be = qd_jacobi(ms, K)
    assert all(b > 0 for b in be), "Favard positivity"
    # moment reproduction certificate
    alp, bep = lr_step(al, be)
    dev_al = [abs(alp[k] / (v * al[k]) - 1) for k in range(min(len(alp), 30))]
    dev_be = [abs(bep[k] / (v ** 2 * be[k]) - 1) for k in range(min(len(bep), 30))]
    # Geometric decay.  HONEST RUN-HISTORY NOTE: the first draft predicted the
    # MOMENT-RATIO rate p = 1/q here (tropical-transport T3).  The run measured
    # 0.69432 at r = 6/5, i.e. p̃ = 1/q̃ = 0.69444 — which is the corpus's own
    # documented rate for the JACOBI-DATA layer (u1-promotion A-6: "at per-step
    # rate = p̃").  The two layers have different rates; the fix was to state the
    # correct prediction, NOT to loosen the tolerance (which was tightened from
    # 5e-2 to 1e-2 in the same edit).
    ptil = 1 / r ** 2
    p = 1 / r ** 4
    rate = dev_al[20] / dev_al[19]
    assert dev_al[-1] < dev_al[0], "S-deviation must decay"
    assert abs(rate / ptil - 1) < mpf("0.01"), (rate, ptil)
    out = {
        "q": fmt(r ** 4), "K": K,
        "alpha_S_dev_k0_k10_k25": [fmt(dev_al[0], 6), fmt(dev_al[10], 6),
                                   fmt(dev_al[25], 6)],
        "beta_S_dev_k0_k10_k25": [fmt(dev_be[0], 6), fmt(dev_be[10], 6),
                                  fmt(dev_be[25], 6)],
        "measured_decay_rate": fmt(rate, 8),
        "predicted_rate_p_tilde": fmt(ptil, 8),
        "moment_ratio_rate_p_for_contrast": fmt(p, 8),
        "statement": ("balanced: LR(J)/q̃ ≠ J.  The Jacobi-data S-deviation decays "
                      "at exactly p̃ = 1/q̃ (u1-promotion A-6), one square root off "
                      "the moment-ratio rate p — S is an asymptotic, not exact, "
                      "automorphism, and the obstruction is the Jackson factor"),
    }
    log("V2b done")
    return out


# ------------------------------------------- V3  the ds/s (harmonic) diagnostic

def block_v3_harmonic(r_num, K):
    log("V3  harmonic moment I(μ) = ∫ s^{-1}dμ along the nonnegative arc")
    mp.dps = 400
    r = mpf(r_num)
    ms = balanced_moments(r, 2 * K + 2)
    al, be = qd_jacobi(ms, K)
    mp.dps = 160
    alf = [+a for a in al]
    bef = [+b for b in be]

    N = 44
    P0 = monic_p_at_zero(al, be, N + 1)
    tN = +(P0[N] / P0[N - 1])
    assert tN < 0, tN

    # sweep the arc t = s·t_N, s ∈ [0, 1]:  s = 0 is Friedrichs, s = 1 is Krein
    sweep = []
    prev = None
    for num, den in ((0, 1), (1, 4), (1, 2), (3, 4), (9, 10), (99, 100),
                     (9999, 10000)):
        sfac = mpf(num) / den
        val, d0 = inv00(alf, bef, N, tshift=sfac * tN)
        lmin = lambda_min([alf[i] + (sfac * tN if i == N - 1 else 0)
                           for i in range(N)], bef, N, mpf(4))
        sweep.append({"s": f"{num}/{den}", "I": fmt(val, 12), "d0": fmt(d0, 6),
                      "lambda_min": fmt(lmin, 10)})
        if prev is not None:
            assert val > prev, ("harmonic moment must increase toward Krein",
                                num, den)
        prev = val
    valK, d0K = inv00(alf, bef, N, tshift=tN)
    assert abs(d0K) < mpf("1e-70"), d0K            # exactly singular at Krein
    I_F, _ = inv00(alf, bef, N, tshift=None)

    # identity cross-check  I = Σ_j w_j/λ_j  from the eigen decomposition
    mp.dps = 120
    lamF, wF = sym_trunc_eig(alf, bef, N)
    I_eig = mp.fsum(wF[j] / lamF[j] for j in range(N))
    assert abs(I_eig / I_F - 1) < mpf("1e-40"), abs(I_eig / I_F - 1)

    # monotone-in-N lower bounds (compression ⇒ (A_N^{-1})_{00} increases with N)
    mp.dps = 160
    ladder = []
    prev = None
    for n in (20, 28, 36, 44):
        val, _ = inv00(alf, bef, n, tshift=None)
        ladder.append({"N": n, "I_F_lower_bound": fmt(val, 14)})
        if prev is not None:
            assert val > prev, ("I_N(0) must increase in N", n)
        prev = val
    cauchy = abs(ladder[-1]["I_F_lower_bound"] and
                 (mpf(ladder[-1]["I_F_lower_bound"]) /
                  mpf(ladder[-2]["I_F_lower_bound"]) - 1))

    out = {
        "q": fmt(r ** 4), "N": N,
        "arc_sweep_Friedrichs_to_Krein": sweep,
        "sweep_parametrization_caveat": ("the sweep is LINEAR in the boundary shift "
                                         "t = s·t_N, in which I looks nearly flat "
                                         "until s → 1.  That flatness is a "
                                         "parametrization artifact: read the sweep "
                                         "against the invariant axis λ_min, which "
                                         "runs from λ_F down to 0.  The "
                                         "parametrization-free content is only "
                                         "(i) monotone, (ii) minimal at F, "
                                         "(iii) +∞ at K"),
        "resolution_caveat": ("λ_min is ALSO nearly constant across the sweep and "
                              "collapses only between s = 0.9999 and s = 1: at "
                              "N = 44 the boundary-shift family does not resolve "
                              "the INTERIOR of the extension circle at all, only "
                              "its two endpoints.  The minimality of I at "
                              "Friedrichs over the whole arc therefore rests on "
                              "the operator ordering J_K ≤ J_t ≤ J_F (Krein–Ando), "
                              "NOT on this sweep, which only corroborates it"),
        "I_at_Krein": "+∞ (truncated matrix exactly singular; d_0 < 1e-70)",
        "d0_at_Krein": fmt(abs(d0K), 4),
        "I_Friedrichs": fmt(I_F, 14),
        "identity_I_eq_sum_w_over_lambda_rel": fmt(abs(I_eig / I_F - 1), 4),
        "N_ladder_lower_bounds": ladder,
        "N_ladder_last_step_rel": fmt(cauchy, 4),
        "statement": ("I(μ) = (J^{-1})_{00} is the TOTAL MASS of the "
                      "computational-time measure ν with μ = s·ν.  It is strictly "
                      "monotone along the nonnegative-extension arc, minimal at "
                      "Friedrichs, and exactly +∞ at Krein — the atom at s = 0 "
                      "means no ν on (0,∞) satisfies s·ν = μ_K at all"),
        "honest_caveat": ("Friedrichs-minimality of I is NOT independent evidence: "
                          "J_K ≤ J_t ≤ J_F in the form order gives J_F^{-1} ≤ "
                          "J_t^{-1}, so 'largest form', 'largest spectral gap' and "
                          "'smallest ds/s mass' are ONE fact in three costumes"),
    }
    log(f"V3  done — I_F = {fmt(I_F, 10)}, singular at Krein")
    return out, al, be, I_F


# --------------------------------- V4  why the KSel-3 criteria are orthogonal

def block_v4_p3_orthogonality(v_num, N):
    log("V4  P3 orthogonality — variance-vs-step and the mass test")
    # exact side: the KSel-3 mechanism needs σ² = lattice step.
    Ls, ks = sp.symbols("L k", positive=True)
    sigma2 = Ls                       # SW core: LN(−L/2, L), σ² = L
    step_u = Ls                       # KSel-3 atomic family: step L  → blind
    step_fk = 2 * Ls                  # F / K supports: step 2L (one q-step)
    assert sp.simplify(sigma2 / step_u - 1) == 0
    assert sp.simplify(sigma2 / step_fk - sp.Rational(1, 2)) == 0
    # the k-th moment shifts the sampling by k·σ²; a lattice vector iff kσ² ∈ step·ℤ
    blind_u = sp.simplify(ks * sigma2 / step_u)          # = k  ∈ ℤ  ∀k
    blind_fk = sp.simplify(ks * sigma2 / step_fk)        # = k/2 ∈ ℤ  iff k even
    assert blind_u == ks and blind_fk == ks / 2

    # numeric side: F masses are not proportional to the Gaussian at the F atoms
    mp.dps = 120
    v = mpf(v_num)
    L = mlog(v)
    al, be = sw_jacobi(v, N + 2)
    lamF, wF = sym_trunc_eig([+a for a in al], [+b for b in be], N)
    # HONEST RUN-HISTORY NOTE: the first draft asserted spread > 10 ("decisively
    # not proportional").  The run REFUTED that expectation — the spread is only
    # ~1.5 over the first 8 atoms, i.e. the Friedrichs masses are NEAR-, though
    # not exactly, proportional to the Gaussian samplings.  The assertion was
    # rewritten to test what is actually true (spread bounded away from 1, so the
    # masses are not Gaussian samplings), and the near-proportionality is recorded
    # as a finding rather than deleted.  It is also the mechanism behind the
    # parent audits' asymptotic u ≡ 1 alignment.
    ratios = []
    for j in range(10):
        t = mlog(lamF[j])
        g = mp.e ** (-(t + L / 2) ** 2 / (2 * L))
        ratios.append(wF[j] / g)
    spread = max(ratios) / min(ratios)
    assert spread > mpf("1.05"), spread    # not proportional: not a Gaussian sampling
    assert spread < mpf(10), spread        # but near-proportional: recorded, not hidden

    out = {
        "sigma_squared_over_step_u_circle": "1  (moment shift is a lattice vector: blind)",
        "sigma_squared_over_step_FK": "1/2 (moment shift is a HALF-lattice vector at odd k)",
        "mass_over_gaussian_spread": fmt(spread, 6),
        "mass_over_gaussian_first10": [fmt(x, 6) for x in ratios],
        "unexpected_finding": ("the Friedrichs masses are NEAR-proportional to the "
                               "Gaussian samplings (spread ≈ 1.5, not orders of "
                               "magnitude): exact proportionality is excluded, but "
                               "the near-miss is the quantitative mechanism behind "
                               "the parent audits' asymptotic u ≡ 1 alignment"),
        "statement": ("the KSel-3 dual-mode criteria (dual-positivity / modular "
                      "inertness) are defined via the Poisson dual of a Gaussian "
                      "sampled at step = variance.  The F/K supports have step 2L "
                      "against variance L, and their masses (Nevanlinna masses "
                      "1/Σ p_n(x)²) are not Gaussian samplings at all — the "
                      "criteria have NO domain of definition on the extension "
                      "circle.  P3 is orthogonal, not merely inconclusive"),
    }
    log(f"V4  done — mass/Gaussian spread {fmt(spread, 4)}")
    return out


# ------------------------------------------ V5  moment-blindness of the arc

def block_v5_moment_blindness(al, be, r_num):
    log("V5  moment blindness of the whole arc")
    mp.dps = 400
    r = mpf(r_num)
    ms = balanced_moments(r, 40)
    mp.dps = 120
    alf = [+a for a in al]
    bef = [+b for b in be]
    N = 40
    P0 = monic_p_at_zero(al, be, N + 1)
    mp.dps = 120
    tN = +(P0[N] / P0[N - 1])
    worst = mpf(0)
    per_member = []
    for num, den in ((0, 1), (1, 2), (9, 10), (1, 1)):
        sfac = mpf(num) / den
        lam, w = sym_trunc_eig(alf, bef, N, tshift=(None if num == 0 else sfac * tN))
        devs = []
        for k in range(1, 31):
            got = mp.fsum(w[j] * lam[j] ** k for j in range(N))
            devs.append(abs(got / mpf(nstr(ms[k], 60)) - 1))
        d = max(devs)
        worst = max(worst, d)
        per_member.append({"s": f"{num}/{den}", "worst_moment_rel_dev": fmt(d, 4)})
    assert worst < mpf("1e-25"), worst
    out = {
        "members_tested": per_member,
        "worst_relative_moment_deviation_k_le_30": fmt(worst, 4),
        "contrast": ("every arc member reproduces every moment; the harmonic "
                     "moment (V3) separates them, and separates Krein from the "
                     "rest by ∞.  So the F/K ambiguity is invisible to the corpus's "
                     "only current consumer class (integer moments)"),
    }
    log(f"V5  done — worst moment dev {fmt(worst, 3)}")
    return out


# --------------------------------- V6  decisive-test dry run (EXPLORATORY)

def block_v6_gamma_dry_run():
    log("V6  decisive-test dry run: I_F + ln λ_F vs −γ  (EXPLORATORY)")
    rows = []
    gamma = +meuler
    for label, rstr, K, N in (("q = 2.0736", "1.2", 48, 44),
                              ("q = 1.4641", "1.1", 48, 44),
                              ("q ≈ 1.2155", "1.05", 48, 44)):
        mp.dps = 500
        r = mpf(rstr)
        ms = balanced_moments(r, 2 * K + 2)
        al, be = qd_jacobi(ms, K)
        mp.dps = 160
        alf = [+a for a in al]
        bef = [+b for b in be]
        row = {"case": label, "q": fmt(r ** 4, 10)}
        for tag, sfac in (("F", None), ("mid", mpf(1) / 2)):
            P0 = monic_p_at_zero(al, be, N + 1)
            tN = +(P0[N] / P0[N - 1])
            ts = None if sfac is None else sfac * tN
            I, _ = inv00(alf, bef, N, tshift=ts)
            lm = lambda_min(alf, bef, N, mpf(4))
            row[f"I_{tag}"] = fmt(I, 10)
            row[f"lambda_min_{tag}"] = fmt(lm, 10)
            row[f"I_plus_log_lambda_{tag}"] = fmt(I + mlog(lm), 10)
            if tag == "F":
                # the truncated-exponential model the −γ prediction assumed
                row["E1_at_lambda_F"] = fmt(mp.e1(lm), 10)
                row["I_F_over_E1"] = fmt(I / mp.e1(lm), 10)
                row["I_F_minus_E1"] = fmt(I - mp.e1(lm), 10)
        rows.append(row)
    # N-sensitivity of the reported quantity at the SMALLEST q of the ladder —
    # without this the "trend" would be unreadable, since I_N(0) rises with N
    # while λ_min(N) falls with N.
    mp.dps = 500
    r = mpf("1.05")
    ms = balanced_moments(r, 2 * 48 + 2)
    al, be = qd_jacobi(ms, 48)
    mp.dps = 160
    alf = [+a for a in al]
    bef = [+b for b in be]
    nsens = []
    for n in (20, 28, 36, 44):
        I, _ = inv00(alf, bef, n, tshift=None)
        lm = lambda_min(alf, bef, n, mpf(4))
        nsens.append({"N": n, "I_F": fmt(I, 10), "lambda_min": fmt(lm, 10),
                      "I_plus_log_lambda": fmt(I + mlog(lm), 10)})

    # pins, honest pre-asymptotic
    pin_rows = []
    for name, qs in (("muon", Q0_MUON_STR), ("proton", Q0_PROTON_STR)):
        mp.dps = 500
        q0 = mpf(qs)
        r = q0 ** mpf("0.25")
        K = 24
        ms = balanced_moments(r, 2 * K + 2)
        al, be = qd_jacobi(ms, K)
        assert all(b > 0 for b in be), ("Favard positivity at pin", name)
        mp.dps = 160
        alf = [+a for a in al]
        bef = [+b for b in be]
        N = 22
        I, _ = inv00(alf, bef, N, tshift=None)
        lm = lambda_min(alf, bef, N, mpf(4))
        pin_rows.append({"pin": name, "N": N, "I_F_lower_bound": fmt(I, 12),
                         "lambda_min_N": fmt(lm, 12),
                         "I_plus_log_lambda": fmt(I + mlog(lm), 12)})
    out = {
        "minus_euler_gamma": fmt(-gamma, 12),
        "ladder": rows,
        "N_sensitivity_at_q_1p2155": nsens,
        "pins_preasymptotic": pin_rows,
        "prediction_tested": ("if μ_F ≈ e^{-s}ds truncated below its gap then "
                              "I_F + ln λ_F → −γ as q → 1⁺, because "
                              "∫_λ^∞ e^{-s}ds/s = E₁(λ) = −γ − ln λ + O(λ)"),
        "outcome": ("REFUTED, scope-(a).  I_F + ln λ_F is N-STABLE to ~6 digits "
                    "(the two badly pre-asymptotic legs cancel), so the ladder "
                    "values 0.9802 / 0.9596 / 0.9506 and 0.9476 at the pins are "
                    "converged in N — and they sit ~1.53 above −γ = −0.5772 and "
                    "drift by only ~0.003 per major q step.  The truncated-"
                    "exponential model is simply wrong for μ_F: I_F is ~2.6× "
                    "E₁(λ_F), because μ_F is a q-LATTICE measure whose harmonic "
                    "moment is dominated by the single lowest atom, not a "
                    "truncated density.  Both readings are reported because they "
                    "point opposite ways and the honest verdict needs both: the "
                    "RATIO I_F/E₁ does fall toward 1 (2.52 → 2.06 → 1.78), so the "
                    "leading behaviour is right, but the ADDITIVE residual "
                    "I_F − E₁ GROWS (1.25 → 1.36 → 1.43).  The −γ test is an "
                    "additive finite-part test, so it is the growing residual that "
                    "governs, and the test as posed fails"),
        "non_discrimination": ("the mid-arc column agrees with the Friedrichs "
                               "column to 7 digits at every rung — this quantity "
                               "does NOT discriminate F from the arc interior; it "
                               "separates Krein (where it is +∞) from everything "
                               "else"),
        "unexplained_regularity_do_not_fit": ("I_F + ln λ_F sits near 0.95 across "
                                              "the whole studied q range and "
                                              "drifts slowly downward.  Recorded "
                                              "as an observation only.  It is NOT "
                                              "interpreted, NOT fitted, and NOT "
                                              "claimed to converge to anything"),
        "tier": ("EXPLORATORY — the q-ladder stops at q ≈ 1.2155 plus the pins; "
                 "no claim is made about the q → 1 limit beyond the observed "
                 "trend, which does not head toward −γ"),
    }
    log("V6  done")
    return out


# ------------------------------------------------------------------- main

def git_sha(path: Path) -> str:
    r = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(path)],
                       capture_output=True, text=True, cwd=HERE, check=False)
    return r.stdout.strip() or "unknown"


def main() -> None:
    mp.dps = 60
    results["V1_smap_algebra"] = block_v1_smap_algebra()
    results["V2_F_equals_S_of_K_sw"] = block_v2_f_equals_s_of_k("1.44", 34)
    results["V2b_balanced_smap_deviation"] = block_v2b_balanced_smap_deviation("1.2", 48)
    v3, al, be, _I_F = block_v3_harmonic("1.2", 48)
    results["V3_harmonic_moment"] = v3
    results["V4_p3_orthogonality"] = block_v4_p3_orthogonality("1.44", 30)
    results["V5_moment_blindness"] = block_v5_moment_blindness(al, be, "1.2")
    results["V6_gamma_dry_run"] = block_v6_gamma_dry_run()
    results["summary"] = {
        "question": ("which self-adjoint extension of J(q) is distinguished — "
                     "Friedrichs or Krein?"),
        "P1_friedrichs_as_form": ("CONVENTIONAL-DEFAULT.  The polynomials are a "
                                  "form core of J_F by construction, but the SAME "
                                  "datum (operator + domain) determines J_K just "
                                  "as canonically.  The three 'independent' "
                                  "arguments for F (largest form, largest spectral "
                                  "gap, smallest ds/s mass) are one fact"),
        "P2_krein_atom": ("EXCLUDES KREIN, DOES NOT SELECT FRIEDRICHS.  Exact core: "
                          "μ = s·ν has a solution ν on (0,∞) iff μ({0}) = 0, which "
                          "fails exactly at Krein.  Every other arc member passes"),
        "P3_modular": ("ORTHOGONAL with a reason: the criteria are defined on a "
                       "step-L sampled Gaussian; the F/K supports have step 2L and "
                       "Nevanlinna masses.  No domain of definition"),
        "P4_non_selection": ("LIVE.  No corpus consumer touches a non-moment "
                            "functional of the kernel, and every arc member has "
                            "every moment"),
        "structural_finding": ("F = S(K) exactly (SW core, every truncation order): "
                               "the F/K choice IS the ds-versus-s·ds level choice, "
                               "i.e. the conjecture's own ς·ds/s normalization one "
                               "level down"),
        "no_fit": "every scored item is an exact identity or a displayed-relation check",
        "wired": "nothing",
    }
    src = Path(__file__)
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                          text=True, cwd=HERE, check=False).stdout.strip() or "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "sympy+mpmath",
        "engineVersion": f"python {platform.python_version()}",
        "commitSha": head,
        "scriptFile": src.name,
        "scriptHash": hashlib.sha256(src.read_bytes()).hexdigest()[:12],
        "scriptCommitSha": git_sha(src),
        "computation": "fvk-selection",
        "description": ("Friedrichs-vs-Krein selection survey: the S-map/LR "
                        "fixed-point identity (F = S(K) exactly on the SW core), "
                        "the ds/s harmonic-moment diagnostic along the nonnegative "
                        "extension arc, the exact reason the modular criteria are "
                        "orthogonal, and the moment-blindness of the whole arc"),
        "auditOnly": "docs/audits/2026-08-01-fvk-selection-framing.md",
        "bean": "qou-f6sm",
        "allPassed": True,
        "precisionMetadata": {"qd_dps": 400, "pin_qd_dps": 500,
                              "eigen_dps": 120, "continued_fraction_dps": 160,
                              "sw_monic_dps": 200},
        "data": results,
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added.
    #
    # 🛑 CORRECTED 2026-09-04 (bean qou-zk51). This said "no q0 in this
    # producer's cone; stamp provenance only" and passed q0_anchor=False,
    # which stamps `q0Anchor: "independent"`. Both were FALSE, and the
    # contradiction was inside this same file: line 92 reads the muon anchor's
    # q0Value out of q-pinning-50-digit.witness.json, line 93 carries the
    # proton pin, and the `pins_preasymptotic` loop below consumes BOTH --
    # `q0 = mpf(qs); r = q0 ** 0.25` feeds the moments, the Jacobi recurrence
    # and every I_F_lower_bound / lambda_min_N this witness reports.
    #
    # Measured: the 2026-08-22 muon re-pin (fca08de7d2, A -> CODATA-2022 C)
    # moves I_F_lower_bound 3.43617345782 -> 3.43617345755, i.e. -0.0786 ppb
    # against the anchor's own -0.0769 ppb -- a ~1:1 sensitivity, in a witness
    # declaring it had none.
    #
    # A FALSE `independent` is worse than an absent stamp: `q0_anchor_is_declared`
    # treats it as settled, so no q0 gate ever revisits it, while the
    # anchor-flip gate (which reads q0Anchor/q0Value) and the value-drift gate
    # (which reads q0 literals) are both blind to a witness recording only
    # DERIVED numbers. This producer evaluates at both pins deliberately, so
    # the honest declaration is "comparison" -- the E1 exception in AGENTS.md
    # §"q0 anchor convention", not independence.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    # q0Values is what makes the "comparison" claim CHECKABLE rather than
    # taken on trust: q0_anchor_consistency_audit verifies each named leg
    # against its canonical pin, and a comparison stamped without it counts
    # as Q0_COMPARISON_NO_VALUES ("the claim is unchecked"). Measured: adding
    # the stamp alone moved Q0_ANCHOR_MISSING 1603 -> 1602 and raised
    # Q0_COMPARISON_NO_VALUES 0 -> 1, i.e. traded one gate red for another.
    witness["q0Values"] = {"muon": Q0_MUON_STR, "proton": Q0_PROTON_STR}
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor="comparison",
        q0_anchor_reason=(
            "deliberate two-pin comparison: pins_preasymptotic evaluates the "
            "Favard/Jacobi chain at BOTH the muon anchor (read from "
            "q-pinning-50-digit.witness.json) and the proton pin. Corrected "
            "2026-09-04 from a false 'independent' -- bean qou-zk51"))
    WITNESS.write_text(json.dumps(witness, indent=2) + "\n")
    log(f"✓ Witness: {WITNESS.name}  (6 assertion blocks, all passed)")


if __name__ == "__main__":
    main()
