#!/usr/bin/env python3
"""A_w zero asymptotics — the "extremal support class = tropical class" residual.

Bean: qou-k16h.  Audit: docs/audits/2026-08-01-awzero-asymptotics.md.
Parents: docs/audits/2026-08-01-ksel2id-tropical-transport.md §3 (the residual),
         docs/audits/2026-08-01-ksel2id-u1-promotion.md §4 gap 2.

TARGET.  For the Ramanujan entire function (q-Airy function)

    A_w(z) = Σ_{m≥0} w^{m²}(−z)^m/(w;w)_m,      0 < w < 1,

show its zeros ζ_1 < ζ_2 < … obey ζ_n = w^{1−2n}(1 + O(w^n)) — the zeros are
asymptotic to the successive coefficient ratios (the tropical / Newton-polygon
corners).  With w = q̃⁻¹ this is exactly the Stieltjes–Wigert-core input the
KSel-2-ID chain still owed.

THE ARGUMENT (derived in the audit; NOT a fit).

  L1 recentring, EXACT   A_w(w^{1−2n}u) = (−1)^n w^{n−n²} u^n Φ_n(u),
                         Φ_n(u) = Σ_{k≥−n}(−1)^k w^{k(k+1)}u^k/(w;w)_{n+k}.
  L2 theta limit, EXACT  Φ_n → G, G(u) = (w²;w²)_∞(w²u;w²)_∞(u⁻¹;w²)_∞/(w;w)_∞
                         (Jacobi triple product).  G's zeros are u ∈ w^{2ℤ};
                         u = 1 is simple, nearest neighbours at w^{±2}.
  L3 defect, EXACT       D_n := Φ_n − G obeys, with
                         S_j(u) := (w^{j+2}u;w²)_∞(w^{−j}u⁻¹;w²)_∞(w²;w²)_∞,
                           D_n = −(w;w)_∞⁻¹ Σ_{j≥1}(−1)^{j+1}w^{j(j+1)/2+nj}S_j/(w;w)_j.
  L4 telescoping, EXACT  |S_j| / |(w²u;w²)_∞(u⁻¹;w²)_∞(w²;w²)_∞| equals
                           even j = 2s   :  w^{−s(s+1)}|u|^{−s}
                           odd  j = 2s+1 :  w^{−(s+1)²}|u|^{−(s+1)}·Ω(u),
                         Ω(u) := |(wu;w²)_∞(wu⁻¹;w²)_∞|/|(w²u;w²)_∞(u⁻¹;w²)_∞|.
                         The q-shifts cancel EXACTLY.  This is the whole point:
                         the comparison stays against |G(u)| pointwise, keeping
                         the theta cancellation, which a single-term Rouché
                         throws away — and that is why the argument survives
                         w → 1, where the single-term route provably cannot.
  L5 master bound        |D_n(u)| ≤ B_n(u)|G(u)|,
                           B_n(u) = Ω(u)·Σ_{s≥0} w^{s(s+1)+(2s+1)n}|u|^{−(s+1)}
                                                 /(w;w)_{2s+1}
                                  + Σ_{s≥1} w^{s²+2sn}|u|^{−s}/(w;w)_{2s}.
  M1 counting majorant   on |u| = w⁻¹ (u = w⁻¹e^{iθ}, S = sin²(θ/2)) each factor
                         of Ω is DECREASING in S, so Ω ≤ 2(w²;w²)_∞²/(w;w²)_∞².
  M2 localization maj.   on |u−1| = ε (ε < ½, Λ_even·ε/(1−ε) ≤ ½),
                         Ω ≤ ((1+ε)/ε)·κ(w)(1−w)·exp((Λ_odd+2Λ_even)(ε+ε/(1−ε))),
                         Λ_odd = Σ_i w^{2i+1}/(1−w^{2i+1}), Λ_even likewise even.
  T  Rouché              sup_{|u|=w⁻¹} B_n < 1 ⇒ A_w has exactly n zeros in
                         |z| < w^{−2n};  sup_{|u−1|=ε} B_n < 1 with ε < 1−w²
                         ⇒ exactly one zero in |z − w^{1−2n}| < ε w^{1−2n}.
                         With ε_n = 2κ(w)w^n and the ETA-QUOTIENT constant
                           κ(w) = (w;w²)_∞²/[(1−w)(w²;w²)_∞²]
                         this gives, for every n ≥ n₀(w),
                           ζ_n = w^{1−2n}(1 + θ_n),   |θ_n| ≤ 2κ(w)w^n,
                         with n₀(w) EXPLICIT (M1/M2 are closed-form, grid-free).
                         κ(0⁺) = 1, κ(1⁻) = 2/π.
  Refinement (measured)  θ_n = −κ(w)w^n + O(w^{3n}).

BLOCKS.
  A1  L1–L4, the four exact identities, at working precision.
  A2  L5 dominates |D_n/G| at every sampled (w, n, u).
  A3  M1/M2 dominate the evaluated suprema; n₀(w) from the CERTIFIED majorants
      over a w-ladder incl. both substrate pins, with the sharper (evaluated,
      non-certified) n₀ reported alongside.
  A4  certified zeros ζ_n by bracketed bisection with an EXPLICIT truncation
      bound; the theorem's conclusion |θ_n| ≤ 2κ w^n ASSERTED for n ≥ n₀; the
      refinement constant κ verified and the next-order rate measured.
  A5  where the argument fails, reported honestly: the naive single-term Rouché
      threshold w₀, and sup B_n just below n₀.

NO FIT.  Every scored quantity is an exact identity or a check of a DISPLAYED
bound.  Tolerances are the displayed bounds themselves or working precision —
none is tuned to make a check pass.  Nothing here is wired to production.
"""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import time
from pathlib import Path

from mpmath import mp, mpf, mpc, nstr, exp as mexp, pi as mpi, log as mlog, sqrt as msqrt

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "awzero-asymptotics.witness.json"

Q_MUON = "1.10997859555733471"      # computations/ layer canonical q₀ (muon pin)
Q_PROTON = "1.10997858275138081"    # proton pin (package layer), 17 dp like Q_MUON
# Was "1.10997861", commented "proton-pinned spot value" — but that literal is
# +24.5 ppb from the proton pin, i.e. 2.1x the ~11.5 ppb mu-p substrate tension
# this very probe measures. A muon-vs-proton comparison run against it was
# comparing the muon pin to a point 2 tensions past proton, so the quantity it
# reported as the mu-p difference was wrong by more than the difference itself.
# The comparison is deliberate and correct; only the proton value was not.

t0 = time.time()
results: dict = {}


def log(msg: str) -> None:
    print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)


def fmt(x, d: int = 6) -> str:
    if isinstance(x, mpc):
        return nstr(x, d)
    return nstr(mpf(x), d)


# --------------------------------------------------------------- q-machinery
def qpoch_inf(a, q):
    """(a;q)_∞ for |q| < 1, to working precision."""
    tiny = mpf(10) ** (-mp.dps - 8)
    r = a * 0 + 1
    t = a
    while abs(t) > tiny:
        r *= (1 - t)
        t *= q
    return r


def qpoch(a, q, n: int):
    r = a * 0 + 1
    t = a
    for _ in range(n):
        r *= (1 - t)
        t *= q
    return r


def kappa(w):
    """κ(w) = (w;w²)_∞²/[(1−w)(w²;w²)_∞²] — the first-order zero-shift constant."""
    return qpoch_inf(w, w ** 2) ** 2 / ((1 - w) * qpoch_inf(w ** 2, w ** 2) ** 2)


def lambda_sums(w):
    """Λ_odd = Σ_i w^{2i+1}/(1−w^{2i+1}), Λ_even = Σ_i w^{2i+2}/(1−w^{2i+2})."""
    tiny = mpf(10) ** (-mp.dps - 8)
    lo = le = mpf(0)
    x = w
    i = 0
    while x > tiny:
        if i % 2 == 0:
            lo += x / (1 - x)
        else:
            le += x / (1 - x)
        x *= w
        i += 1
    return lo, le


# ------------------------------------------------------------ A_w evaluation
def aw_coeffs(w, M: int):
    """[a_0..a_M], a_m = (−1)^m w^{m²}/(w;w)_m, built with O(M) multiplications."""
    cs = [mpf(1)]
    poch = mpf(1)
    wsq = mpf(1)        # w^{m²}
    for m in range(1, M + 1):
        wsq *= w ** (2 * m - 1)
        poch *= (1 - w ** m)
        cs.append((-1) ** m * wsq / poch)
    return cs


def aw_trunc_order(w, zmax, tol_exp: int) -> int:
    """Least M whose CERTIFIED tail bound is < 10^{−tol_exp}.

    |Σ_{m>M} a_m z^m| ≤ w^{(M+1)²}|z|^{M+1}/[(w;w)_∞(1−r)],  r = w^{2M+3}|z| < 1
    (the term-ratio w^{2m+1}|z| is decreasing in m).
    """
    L = mlog(1 / w)
    lz = mlog(abs(zmax))
    target = -tol_exp * mlog(10) + mlog(qpoch_inf(w, w))
    M = max(4, int(lz / (2 * L)) + 2)
    while True:
        r = w ** (2 * M + 3) * abs(zmax)
        if r < mpf("0.5"):
            val = -((M + 1) ** 2) * L + (M + 1) * lz - mlog(1 - r)
            if val < target:
                return M
        M += max(2, M // 10)


def aw_eval(cs, z):
    """Horner evaluation of Σ_{m≤M} a_m z^m."""
    s = cs[-1]
    for c in reversed(cs[:-1]):
        s = s * z + c
    return s


def aw_tail(w, z, M: int):
    r = w ** (2 * M + 3) * abs(z)
    return w ** ((M + 1) ** 2) * abs(z) ** (M + 1) / (qpoch_inf(w, w) * (1 - r))


# ------------------------------------------------------ Φ_n, G, defect, bound
def Phi(w, u, n: int, K: int = 0):
    if K == 0:
        K = int(mlog(mpf(10) ** (-mp.dps - 8)) / mlog(w)) // 2 + 8
    s = u * 0
    for k in range(-n, K + 1):
        s += (-1) ** k * w ** (k * (k + 1)) * u ** k / qpoch(w, w, n + k)
    return s


def G_lim(w, u):
    return (qpoch_inf(w ** 2, w ** 2) * qpoch_inf(w ** 2 * u, w ** 2)
            * qpoch_inf(1 / u, w ** 2) / qpoch_inf(w, w))


def S_j(w, u, j: int):
    return (qpoch_inf(w ** (j + 2) * u, w ** 2) * qpoch_inf(w ** (-j) / u, w ** 2)
            * qpoch_inf(w ** 2, w ** 2))


def D_expansion(w, u, n: int, J: int = 0):
    """The EXACT defect expansion L3, summed until the j-term underflows.

    The j-term scales like w^{j²/4 + j/2 + nj} (the S_j pole factors contribute
    w^{−j²/4}), so the tail is Gaussian in j; J is chosen adaptively.
    """
    cinf = 1 / qpoch_inf(w, w)
    s = u * 0
    tiny = mpf(10) ** (-mp.dps - 5)
    scale = mpf(0)
    j = 1
    while True:
        term = (-cinf * (-1) ** (j + 1) * w ** (mpf(j * (j + 1)) / 2 + n * j)
                / qpoch(w, w, j) * S_j(w, u, j))
        s += term
        scale = max(scale, abs(term))
        if j > 4 and abs(term) < tiny * scale:
            return s
        j += 1
        if J and j > J:
            return s
        if j > 4000:
            raise RuntimeError("defect expansion did not terminate")


def Omega(w, u):
    return (abs(qpoch_inf(w * u, w ** 2) * qpoch_inf(w / u, w ** 2))
            / abs(qpoch_inf(w ** 2 * u, w ** 2) * qpoch_inf(1 / u, w ** 2)))


def B_series(w, n: int, r, S: int = 30):
    """(C1, C2) of L5 with |u|^{−k} ≤ r^{−k}."""
    c1 = sum(w ** (s * (s + 1) + (2 * s + 1) * n) * r ** (-(s + 1))
             / qpoch(w, w, 2 * s + 1) for s in range(S))
    c2 = sum(w ** (s * s + 2 * s * n) * r ** (-s) / qpoch(w, w, 2 * s)
             for s in range(1, S))
    return c1, c2


def B_bound(w, u, n: int, S: int = 30):
    c1, c2 = B_series(w, n, abs(u), S)
    return Omega(w, u) * c1 + c2


# ------------------------------------------------- certified Ω majorants M1/M2
def omega_majorant_counting(w):
    """M1: Ω ≤ 2(w²;w²)_∞²/(w;w²)_∞² on |u| = w⁻¹ (grid-free, proved)."""
    return 2 * qpoch_inf(w ** 2, w ** 2) ** 2 / qpoch_inf(w, w ** 2) ** 2


def omega_majorant_localization(w, eps, lo, le):
    """M2: closed-form majorant of Ω on |u−1| = ε; None when out of range."""
    if eps >= mpf("0.5"):
        return None
    epsp = eps / (1 - eps)
    if le * epsp > mpf("0.5"):
        return None
    return ((1 + eps) / eps) * kappa(w) * (1 - w) * mexp((lo + 2 * le) * (eps + epsp))


def n0_counting(w, cap: int = 40000):
    """Least n with the CERTIFIED counting condition Ω†·C1 + C2 < 1."""
    om = omega_majorant_counting(w)
    for n in range(0, cap):
        c1, c2 = B_series(w, n, 1 / w)
        v = om * c1 + c2
        if v < 1:
            return n, om, v
    return None, om, None


def n0_localization(w, cap: int = 40000):
    """Least n with the CERTIFIED localization condition at ε_n = 2κ(w)w^n."""
    k = kappa(w)
    lo, le = lambda_sums(w)
    for n in range(1, cap):
        e = 2 * k * w ** n
        if e >= 1 - w ** 2:
            continue
        om = omega_majorant_localization(w, e, lo, le)
        if om is None:
            continue
        c1, c2 = B_series(w, n, 1 - e)
        v = om * c1 + c2
        if v < 1:
            return n, e, v
    return None, None, None


def sup_omega_grid(w, contour: str, eps=None, M: int = 0):
    """Evaluated (NOT certified) supremum of Ω, reported only to exhibit the
    slack in the closed-form majorants M1/M2.  The certified n₀ uses no grid.
    The sample count is reduced for w > 0.95, where each q-product needs
    ~10³–10⁴ factors; a coarser grid can only UNDER-estimate the supremum, so
    the assertion `grid sup ≤ majorant` stays sound (it merely gets weaker)."""
    if M == 0:
        M = 720 if w <= mpf("0.95") else 120
    best = mpf(0)
    for i in range(M + 1):
        th = mpi * i / M
        u = ((1 / w) * mexp(mpc(0, 1) * th) if contour == "count"
             else 1 + eps * mexp(mpc(0, 1) * th))
        v = Omega(w, u)
        if v > best:
            best = v
    return best


# ------------------------------------------------------------------- blocks
def block_a1_exact_identities() -> dict:
    log("A1: exact identities L1–L4 (recentring / theta limit / defect / telescoping)")
    rows = []
    tol = mpf(10) ** (-mp.dps + 20)
    for wv, n in (("0.5", 3), ("0.7", 5), ("0.85", 4)):
        w = mpf(wv)
        for u in (mpf("1.13"), mpf("0.9") + mpc(0, 1) * mpf("0.4"),
                  (1 / w) * mexp(mpc(0, 1) * mpf("0.8"))):
            z = w ** (1 - 2 * n) * u
            M = aw_trunc_order(w, abs(z), mp.dps - 10)
            cs = aw_coeffs(w, M)
            aval = aw_eval(cs, z)
            rhs = (-1) ** n * w ** (n - n * n) * u ** n * Phi(w, u, n)
            e1 = abs(aval - rhs) / abs(aval)
            psi = sum((-1) ** k * w ** (k * (k + 1)) * u ** k
                      for k in range(-90, 91)) / qpoch_inf(w, w)
            e2 = abs(psi - G_lim(w, u)) / abs(psi)
            d_direct = Phi(w, u, n) - G_lim(w, u)
            e3 = abs(d_direct - D_expansion(w, u, n)) / abs(d_direct)
            den = abs(qpoch_inf(w ** 2 * u, w ** 2) * qpoch_inf(1 / u, w ** 2)
                      * qpoch_inf(w ** 2, w ** 2))
            e4 = mpf(0)
            for s in range(0, 5):
                if s:
                    lhs_e = abs(S_j(w, u, 2 * s)) / den
                    e4 = max(e4, abs(lhs_e - w ** (-s * (s + 1))
                                     * abs(u) ** (-s)) / lhs_e)
                lhs_o = abs(S_j(w, u, 2 * s + 1)) / den
                pred_o = w ** (-(s + 1) ** 2) * abs(u) ** (-(s + 1)) * Omega(w, u)
                e4 = max(e4, abs(lhs_o - pred_o) / lhs_o)
            for name, e in (("L1_recentring", e1), ("L2_theta", e2),
                            ("L3_defect", e3), ("L4_telescoping", e4)):
                assert e < tol, f"{name} failed at w={wv}, n={n}, u={fmt(u)}: {fmt(e)}"
            rows.append({"w": wv, "n": n, "u": fmt(u, 8), "trunc_order": M,
                         "trunc_tail_bound": fmt(aw_tail(w, z, M)),
                         "L1_rel_err": fmt(e1), "L2_rel_err": fmt(e2),
                         "L3_rel_err": fmt(e3), "L4_rel_err": fmt(e4)})
    log(f"A1:   -> {len(rows)} (w,n,u) samples; all four identities exact to "
        f"working precision (dps {mp.dps})")
    return {"samples": rows, "tolerance": f"1e-{mp.dps - 20}",
            "identities": {
                "L1": "A_w(w^{1−2n}u) = (−1)^n w^{n−n²} u^n Φ_n(u)",
                "L2": "G = (w²;w²)_∞(w²u;w²)_∞(u⁻¹;w²)_∞/(w;w)_∞",
                "L3": "D_n = −(w;w)_∞⁻¹ Σ_j (−1)^{j+1} w^{j(j+1)/2+nj} S_j/(w;w)_j",
                "L4": "even j=2s: w^{−s(s+1)}|u|^{−s}; odd j=2s+1: "
                      "w^{−(s+1)²}|u|^{−(s+1)}Ω(u)"}}


def block_a2_master_bound() -> dict:
    log("A2: master bound B_n(u) ≥ |D_n(u)/G(u)|")
    rows = []
    worst = mpf(0)
    for wv in ("0.5", "0.7", "0.85", "0.93"):
        w = mpf(wv)
        for n in (2, 4, 8):
            for thv in ("0.35", "1.4", "2.6"):
                th = mpf(thv)
                for contour, u in (("count", (1 / w) * mexp(mpc(0, 1) * th)),
                                   ("near1", 1 + mpf("0.13") * mexp(mpc(0, 1) * th))):
                    act = abs((Phi(w, u, n) - G_lim(w, u)) / G_lim(w, u))
                    bnd = B_bound(w, u, n)
                    assert act <= bnd, (f"L5 VIOLATED at w={wv}, n={n}, θ={thv}, "
                                        f"{contour}: {fmt(act)} > {fmt(bnd)}")
                    ratio = act / bnd
                    worst = max(worst, ratio)
                    rows.append({"w": wv, "n": n, "theta": thv, "contour": contour,
                                 "actual": fmt(act), "bound": fmt(bnd),
                                 "actual_over_bound": fmt(ratio)})
    log(f"A2:   -> {len(rows)} samples; bound dominates everywhere, tightest "
        f"actual/bound = {fmt(worst)}")
    return {"samples": rows, "n_samples": len(rows),
            "max_actual_over_bound": fmt(worst),
            "verdict": "L5 dominates |D_n/G| at every sample and is tight to "
                       "within the reported factor — never loose by an "
                       "exponential in 1/log(1/w)"}


def block_a3_thresholds() -> dict:
    log("A3: certified Ω majorants and the resulting n₀(w) ladder")
    qm, qp = mpf(Q_MUON), mpf(Q_PROTON)
    ladder = [("0.3", ""), ("0.5", ""), ("0.7", ""), ("0.8", ""), ("0.9", ""),
              ("0.94", ""),
              (nstr(1 / msqrt(qm), 25), "muon pin w = q̃⁻¹"),
              (nstr(1 / msqrt(qp), 25), "proton pin w = q̃⁻¹"),
              ("0.97", "")]
    rows = []
    for wv, note in ladder:
        w = mpf(wv)
        k = kappa(w)
        lo, le = lambda_sums(w)
        nc, om_c, vc = n0_counting(w)
        nl, e_nl, vl = n0_localization(w)
        n0 = max(nc, nl)
        # certified majorants must dominate the evaluated suprema
        sup_c = sup_omega_grid(w, "count")
        assert sup_c <= om_c, f"M1 violated at w={wv}: {fmt(sup_c)} > {fmt(om_c)}"
        om_l = omega_majorant_localization(w, e_nl, lo, le)
        sup_l = sup_omega_grid(w, "loc", eps=e_nl)
        assert sup_l <= om_l, f"M2 violated at w={wv}: {fmt(sup_l)} > {fmt(om_l)}"
        # sharper, NON-certified n₀ from the evaluated sup on the counting circle
        nc_eval = None
        for n in range(0, 40000):
            c1, c2 = B_series(w, n, 1 / w)
            if sup_c * c1 + c2 < 1:
                nc_eval = n
                break
        rows.append({
            "w": wv, "note": note, "kappa": fmt(k, 12),
            "Lambda_odd": fmt(lo, 8), "Lambda_even": fmt(le, 8),
            "M1_majorant": fmt(om_c, 8), "sup_Omega_counting_evaluated": fmt(sup_c, 8),
            "M1_slack": fmt(om_c / sup_c, 6),
            "M2_majorant_at_n0": fmt(om_l, 8),
            "sup_Omega_localization_evaluated": fmt(sup_l, 8),
            "M2_slack": fmt(om_l / sup_l, 6),
            "n0_counting_certified": nc, "supB_counting_at_n0": fmt(vc, 8),
            "n0_counting_evaluated_sup": nc_eval,
            "n0_localization_certified": nl, "eps_at_n0": fmt(e_nl, 8),
            "supB_localization_at_n0": fmt(vl, 8),
            "n0_certified": n0,
            "theorem_relative_bound_at_n0": fmt(2 * k * w ** n0, 6),
            "one_minus_w2": fmt(1 - w ** 2, 6)})
        log(f"A3:   -> w = {wv[:10]}: κ = {fmt(k)}, n₀ = {n0} "
            f"(count {nc}, loc {nl}); |θ_{n0}| ≤ {fmt(2 * k * w ** n0)}")
    return {"ladder": rows,
            "kappa_limits": {"w->0+": "1", "w->1-": fmt(2 / mpi, 12)},
            "certification": "M1 and M2 are CLOSED-FORM majorants (no grid): M1 "
                             "from the monotonicity of each Ω-factor in "
                             "S = sin²(θ/2); M2 from factorwise perturbation "
                             "around u = 1.  The evaluated grid suprema are "
                             "reported only to exhibit the slack.",
            "reading": "n₀(w) is the explicit index from which the theorem "
                       "applies.  It grows as w → 1 but is finite for every "
                       "w < 1, and is modest at both substrate pins."}


def block_a4_zeros() -> dict:
    log("A4: certified zeros and the θ_n = −κ(w)w^n refinement")
    qm = mpf(Q_MUON)
    cases = [("0.5", None), ("0.7", None), ("0.85", None), ("0.9", None),
             (nstr(1 / msqrt(qm), 25), "muon pin")]
    out = []
    for wv, note in cases:
        w = mpf(wv)
        nl, _, _ = n0_localization(w)
        nc, _, _ = n0_counting(w)
        n0 = max(nl, nc)
        nmax = n0 + 8
        # enumerate every index when n₀ is small (this also verifies the
        # INDEXING); otherwise probe the certified window around n₀ only.
        idx = list(range(1, nmax + 1)) if n0 <= 12 else \
            list(range(1, 5)) + list(range(n0 - 2, nmax + 1))
        dps_needed = int(nmax * nmax * mlog(1 / w) / mlog(10)) + 120
        old = mp.dps
        mp.dps = max(80, dps_needed)
        w = mpf(wv)
        k = kappa(w)
        log(f"A4:   w = {wv[:10]} {note or ''}: n₀ = {n0}, ζ_n for n ∈ "
            f"[{idx[0]}..{idx[-1]}] ({len(idx)} zeros) at dps {mp.dps}")
        zmax = w ** (1 - 2 * nmax) * 2
        M = aw_trunc_order(w, zmax, mp.dps - 20)
        cs = aw_coeffs(w, M)
        rows = []
        max_ratio = mpf(0)
        n_done = 0
        for n in idx:
            c = w ** (1 - 2 * n)
            eps = 2 * k * w ** n
            half = eps if n >= n0 else min(mpf("0.45"), (1 - w ** 2) / 2)
            a, b = c * (1 - half), c * (1 + half)
            fa, fb = aw_eval(cs, a), aw_eval(cs, b)
            # CERTIFY the endpoint signs against the tail bound (Copilot review,
            # PR #4507): the bisection sees only the truncation Σ_{m≤M} a_m z^m,
            # so a sign change there certifies a sign change of the TRUE series
            # only if |truncation| exceeds the tail bound at each endpoint.
            ta, tb = aw_tail(w, a, M), aw_tail(w, b, M)
            endpoints_certified = bool(abs(fa) > ta and abs(fb) > tb)
            if n >= n0:
                assert endpoints_certified, (
                    f"TAIL CERTIFICATION FAILED at w={wv}, n={n}: "
                    f"|f(a)|={fmt(abs(fa))} vs tail {fmt(ta)}, "
                    f"|f(b)|={fmt(abs(fb))} vs tail {fmt(tb)}")
            if fa * fb > 0:
                assert n < n0, (f"THEOREM VIOLATED: no sign change in the "
                                f"certified interval at w={wv}, n={n}")
                rows.append({"n": n, "status": "no sign change in the (wider) "
                                              "sub-n₀ bracket — theorem silent here",
                             "half_width": fmt(half)})
                continue
            for _ in range(140):
                m = (a + b) / 2
                fm = aw_eval(cs, m)
                if fm == 0:
                    a = b = m
                    break
                if (fm < 0) == (fa < 0):
                    a, fa = m, fm
                else:
                    b, fb = m, fm
            z = (a + b) / 2
            theta = z * w ** (2 * n - 1) - 1
            pred = -k * w ** n
            rows.append({"n": n, "zeta": nstr(z, 22), "theta": nstr(theta, 22),
                         "endpoints_certified_vs_tail": endpoints_certified,
                         "tail_bound_at_a": fmt(ta), "tail_bound_at_b": fmt(tb),
                         "kappa_prediction": fmt(pred, 12),
                         "theta_over_prediction": fmt(theta / pred, 12),
                         "theorem_bound_2kw^n": fmt(2 * k * w ** n, 8),
                         "obeys_theorem_bound": bool(abs(theta) <= 2 * k * w ** n)})
            if n >= n0:
                n_done += 1
                max_ratio = max(max_ratio, abs(theta) / (2 * k * w ** n))
                assert abs(theta) <= 2 * k * w ** n, (
                    f"THEOREM BOUND VIOLATED at w={wv}, n={n}: "
                    f"|θ| = {fmt(abs(theta))} > {fmt(2 * k * w ** n)}")
        assert n_done >= 5, f"too few certified indices tested at w={wv}"
        good = [r for r in rows if "zeta" in r]
        rate = None
        if len(good) >= 4:
            def resid(r):
                nn = r["n"]
                return (mpf(r["theta"]) + k * w ** nn) / w ** (2 * nn)
            r1, r2 = good[-4], good[-1]
            if resid(r1) != 0 and resid(r2) != 0:
                rate = (abs(resid(r2) / resid(r1))) ** (mpf(1) / (r2["n"] - r1["n"]))
        out.append({"w": wv, "note": note, "n0": n0, "n_max": nmax, "dps": mp.dps,
                    "trunc_order": M, "kappa": fmt(k, 12), "zeros": rows,
                    "n_certified_indices_tested": n_done,
                    "max_|theta|_over_theorem_bound": fmt(max_ratio, 8),
                    "measured_next_order_rate": fmt(rate, 8) if rate else "n/a",
                    "predicted_next_order_rate_w": fmt(w, 8)})
        log(f"A4:   -> max |θ_n|/(2κw^n) = {fmt(max_ratio)} over {n_done} "
            f"certified indices; next-order rate "
            f"{fmt(rate) if rate else 'n/a'} vs predicted w = {fmt(w)}")
        mp.dps = old
    return {"cases": out,
            "conclusion": "ζ_n = w^{1−2n}(1 + θ_n), |θ_n| ≤ 2κ(w)w^n for every "
                          "n ≥ n₀(w) — the theorem's own conclusion, ASSERTED "
                          "here, not merely observed; θ_n = −κ(w)w^n + O(w^{3n}) "
                          "is the measured refinement (rate → w per step of the "
                          "residual/w^{2n} ratio)"}


def block_a5_where_it_fails() -> dict:
    log("A5: honest failure map")
    lo_, hi_ = mpf("0.01"), mpf("0.999")
    for _ in range(200):
        mid = (lo_ + hi_) / 2
        if 2 * sum(mid ** (kk * kk) for kk in range(1, 400)) < 1:
            lo_ = mid
        else:
            hi_ = mid
    w_naive = (lo_ + hi_) / 2
    w_pin = 1 / msqrt(mpf(Q_MUON))
    rows = []
    for wv in ("0.7", "0.9", nstr(w_pin, 25)):
        w = mpf(wv)
        k = kappa(w)
        lo, le = lambda_sums(w)
        nl, _, _ = n0_localization(w)
        sub = []
        for n in range(max(1, nl - 3), nl + 2):
            e = 2 * k * w ** n
            om = omega_majorant_localization(w, e, lo, le) if e < 1 - w ** 2 else None
            if om is None:
                sub.append({"n": n, "supB": "ε out of the majorant's range "
                                            "(ε ≥ ½ or Λ_even·ε′ > ½)"})
                continue
            c1, c2 = B_series(w, n, 1 - e)
            v = om * c1 + c2
            sub.append({"n": n, "eps": fmt(e, 8), "supB_certified": fmt(v, 8),
                        "holds": bool(v < 1)})
        rows.append({"w": wv, "n0_localization": nl, "transition": sub})
    log(f"A5:   -> naive single-term Rouché closes only for w < {fmt(w_naive, 8)}; "
        f"pin w = {fmt(w_pin, 8)} sits far above it")
    return {
        "naive_single_term_rouche_threshold_w0": fmt(w_naive, 10),
        "naive_criterion": "2 Σ_{k≥1} w^{k²} < 1 at the geometric-mean radius "
                           "ρ_n = √(r_{n−1}r_n).  Log-concavity of the terms with "
                           "curvature ≥ 2ln(1/w) gives T_{n±k} ≤ T_n w^{k²}, so "
                           "the single dominant term beats the rest only below "
                           "this w₀ — and the dominance ratio → w as n → ∞, so it "
                           "NEVER improves with n.  This is a scope-(a) statement "
                           "about that argument, not about the result.",
        "pin_w": fmt(w_pin, 12),
        "why_the_theta_route_works": "L4's exact q-shift cancellation keeps the "
                                     "theta cancellation in numerator AND "
                                     "denominator, so the comparison is against "
                                     "|G(u)| pointwise rather than against "
                                     "Σ|terms|; the loss factor (w²;w²)_∞³ that "
                                     "kills the naive route never appears.",
        "transitions": rows,
        "honest_residual": "for n < n₀(w) the theorem is SILENT.  Nothing here "
                           "excludes the asymptotic holding earlier — numerically "
                           "it does — the condition is sufficient, not necessary.",
    }


def git_sha(path: Path) -> str:
    try:
        return subprocess.run(["git", "log", "-1", "--format=%H", "--", str(path)],
                              capture_output=True, text=True, cwd=HERE,
                              check=False).stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def main() -> None:
    mp.dps = 60
    results["A1_exact_identities"] = block_a1_exact_identities()
    results["A2_master_bound"] = block_a2_master_bound()
    results["A3_rouche_thresholds"] = block_a3_thresholds()
    results["A4_certified_zeros"] = block_a4_zeros()
    results["A5_failure_map"] = block_a5_where_it_fails()
    results["summary"] = {
        "target": "ζ_n = w^{1−2n}(1 + O(w^n)) for the zeros of A_w",
        "verdict": "PROVED for every 0 < w < 1 and every n ≥ n₀(w), with the "
                   "explicit constant 2κ(w), κ(w) = (w;w²)_∞²/[(1−w)(w²;w²)_∞²], "
                   "and n₀(w) explicit from the closed-form majorants M1/M2 — "
                   "computed here at both substrate pins",
        "residual": "the theorem is silent for n < n₀(w); the refinement "
                    "θ_n = −κ w^n + O(w^{3n}) is derived-and-measured, not "
                    "separately proved; nothing is wired",
        "scope": "no scope-(b) claims anywhere",
    }
    src = Path(__file__)
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                          text=True, cwd=HERE, check=False).stdout.strip() or "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "mpmath",
        "engineVersion": f"python {platform.python_version()}",
        "commitSha": head,
        "scriptFile": src.name,
        "scriptHash": hashlib.sha256(src.read_bytes()).hexdigest()[:12],
        "scriptCommitSha": git_sha(src),
        "computation": "awzero-asymptotics",
        "description": ("Zeros of the Ramanujan entire function A_w: theta-limit "
                        "Rouché localization ζ_n = w^{1−2n}(1+θ_n), "
                        "|θ_n| ≤ 2κ(w)w^n for n ≥ n₀(w), n₀ explicit"),
        "auditOnly": "docs/audits/2026-08-01-awzero-asymptotics.md",
        "bean": "qou-k16h",
        "allPassed": True,
        "precisionMetadata": {"compute_dps": 60,
                              "zero_finding_dps": "n²·log₁₀(1/w) + 120, per case"},
        "data": results,
    }
    WITNESS.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n✓ Witness: {WITNESS.name}  (5 assertion blocks, all passed)")


if __name__ == "__main__":
    main()
