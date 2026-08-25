#!/usr/bin/env python3
"""Balanced D-function theta limit — closing (or honestly bounding) the fibre leg.

Bean: qou-r4ya.  Audit: docs/audits/2026-08-01-balanced-theta-limit.md.
Parents: docs/audits/2026-08-01-awzero-asymptotics.md (the SW-core theorem this
         transports), docs/audits/2026-08-01-ksel2id-tropical-transport.md §3
         (the residual), docs/audits/2026-08-01-ksel2id-u1-promotion.md §4.

TARGET.  The SW core's Nevanlinna denominator is D_SW(z) = c0 z A_w(z),
w = q̃⁻¹, and its zeros are PROVED to satisfy ζ_n = w^{1−2n}(1+O(w^n)) by a
theta-limit Rouché argument.  The BALANCED family's own Nevanlinna denominator

    D_bal(z) = z Σ_{n≥0} p_n(0) p_n(z)      (p_n orthonormal for m_k)

with balanced moments  m_k = q̃^{k(k−1)/2} (p;p)_k E^k,  E = 1/(1−p) = q/(q−1),
has NOT been linked to the balanced tropical lattice.  This probe runs the same
machinery on it.

WHAT IS DERIVED (not fitted).

  R1  E-SHIFTED RECENTRING, EXACT.  Normalise the Taylor coefficients of
      Φ_bal(z) := D_bal(z)/z as   d_j = d_0 (−1)^j E^{−j} w^{j²} g_j.
      Substituting  z = E w^{1−2n} u  makes the E cancel IDENTICALLY (E^{−j}
      against E^{j}), leaving exactly the SW recentring:
          Φ_bal(E w^{1−2n} u) = d_0 (−1)^n w^{n−n²} u^n Φ_n(u),
          Φ_n(u) = Σ_{k≥−n} (−1)^k w^{k(k+1)} g_{n+k} u^k.
      The balanced recentred series IS the SW recentred series with
      1/(w;w)_{n+k} replaced by g_{n+k}.  This is the E-shifted recentring the
      problem statement anticipated; it is exact, not asymptotic.

  R2  THE THETA LIMIT IS THE SAME THETA.  g_m → g_∞ gives Φ_n → G = g_∞ ϑ,
          ϑ(u) = Σ_{k∈ℤ} (−1)^k w^{k(k+1)} u^k
               = (w²;w²)_∞ (w²u;w²)_∞ (u⁻¹;w²)_∞      (Jacobi triple product),
      whose zero set is EXACTLY u ∈ w^{2ℤ} — the balanced tropical lattice.
      Only the prefactor differs (g_∞ instead of 1/(w;w)_∞).

  R3  THE DEFECT EXPANSION TRANSFERS VERBATIM under hypothesis
      (H)   g_m = g_∞ Ψ(w^m),  Ψ(x) = 1 + Σ_{j≥1} c_j x^j analytic, Ψ(0)=1,
      because then D_n := Φ_n − G = g_∞ Σ_{j≥1} c_j w^{jn} S_j(u) with the SAME
      theta products S_j(u) = (w^{j+2}u;w²)_∞ (w^{−j}u⁻¹;w²)_∞ (w²;w²)_∞ as in
      the SW argument.  Hence the SAME telescoping, the SAME master bound, the
      SAME Ω-majorants, the SAME Rouché — with the SW coefficients
      c_j^SW = (−1)^j w^{j(j+1)/2}/(w;w)_j replaced by the balanced c_j.
      SW is the special case Ψ_SW(x) = (wx;w)_∞.

  R4  THE CONVERGENCE CONDITION, DERIVED.  The master bound's even-j term is
      |c_{2s}| w^{2sn} w^{−s(s+1)}|u|^{−s}: it converges iff |c_j| decays
      Gaussianly faster than w^{−j²/4}, i.e. iff (writing |c_j| ≍ C e^{−a j²})
          4a > ln(1/w)          [equivalently a > a_SW/2, since a_SW = ½ln(1/w)].
      This threshold is DERIVED from the displayed bound, never tuned.  It is
      the precise criterion for the SW machinery to transfer.

  R5  THE LEADING CONSTANT.  θ_n = −κ_bal w^n + …, with
          κ_bal = |c_1| · w^{-1} · (w;w²)_∞²/(w²;w²)_∞²   =  (|c_1|/|c_1^SW|)·κ_SW,
      κ_SW(w) = (w;w²)_∞²/[(1−w)(w²;w²)_∞²] the awzero constant; the ratio is
      |c_1|(1−w)/w.  Also |c_1| = C/(q̃−1) where C := lim (1−ρ_j)/w^j and
      ρ_j := (−d_{j−1}/d_j)/(E w^{1−2j}) is the normalised tropical corner.

BLOCKS.
  B1  R1–R2 exact identities, symbolically (sympy) and to working precision.
  B2  machinery validation: the same qd → orthonormal → D pipeline reproduces
      the KNOWN closed form d_j^SW = c0(−1)^j w^{j²}/(w;w)_j for the SW core.
  B3  balanced d_j, the normalised corners ρ_j, and C = lim (1−ρ_j)/w^j.
  B4  hypothesis (H): overdetermined reconstruction of Ψ from g_m, with the
      reliable-order window fixed a priori by the Vandermonde conditioning.
  B5  the derived threshold R4: measured Gaussian rate a of |c_j| against
      ln(1/w)/4, per rung; and the negative-index contrast Ψ_SW(w^{-m}) = 0.
  B6  the payoff: zeros of Φ_bal vs the E-shifted lattice E w^{1−2n}; the
      log_q̃ class → φ₁ = frac(log_q̃ E).

NO FIT.  Every scored quantity is an exact identity, a check of a DISPLAYED
bound, or a measurement reported as such.  The one threshold (R4) is derived
from the master bound.  Nothing here is wired to production.
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import time
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, matrix, lu_solve, log as mlog, sqrt as msqrt, nstr

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "baldfn-theta-limit.witness.json"
T0 = time.time()

# rung name -> (q̃ numerator, q̃ denominator, KM, KJ, N, J, dps)
RUNGS = [
    ("qt=2",      2, 1,  340, 170, 165, 40, 1500),
    ("qt=36/25", 36, 25, 1000, 500, 490, 48, 6000),
    ("qt=6/5",    6, 5,  1300, 650, 640, 48, 4000),
]
_FRAC = {"B1": 0.03, "B2": 0.08, "B3": 0.42, "B4": 0.60, "B5": 0.72,
         "B4b": 0.66, "B6": 0.90, "B7": 0.98}


def prog(tag: str, msg: str) -> None:
    el = time.time() - T0
    fr = _FRAC.get(tag)
    eta = (el * (1 - fr) / fr) if fr else float("nan")
    print(f"[{el:7.1f}s | ETA ~{eta:6.0f}s] {tag}: {msg}", flush=True)


def git_sha(path: Path) -> str:
    r = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(path)],
                       capture_output=True, text=True, cwd=HERE, check=False)
    return r.stdout.strip() or "unknown"


# ------------------------------------------------------------------ machinery

def balanced_moments(qt, p, E, K):
    """m_k = q̃^{k(k−1)/2} (p;p)_k E^k  — the exact factorisation
    SWJacksonMomentFactorization (SW Gaussian × Jackson × E-scale)."""
    out = [qt ** 0]
    poch = qt ** 0
    pk = qt ** 0
    for k in range(1, K + 1):
        pk = pk * p
        poch = poch * (1 - pk)
        out.append(qt ** (mpf(k * (k - 1)) / 2) * poch * E ** k)
    return out


def sw_moments(qt, K):
    """G_k = q̃^{k(k−1)/2} — the pure SW core."""
    return [qt ** (mpf(k * (k - 1)) / 2) for k in range(K + 1)]


def qd_jacobi(ms, K):
    """Monic Jacobi data by the quotient-difference algorithm (Rutishauser)."""
    n_max = len(ms) - 1
    qc = [ms[n + 1] / ms[n] for n in range(n_max)]
    ec = [ms[0] * 0] * n_max
    q0 = [qc[0]]
    e0 = []
    for _ in range(1, K):
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


def pow00(al, be, n):
    """(M^n)_00 for the monic Jacobi matrix — moment reproduction check."""
    K = len(al)
    z = al[0] * 0
    v = [z] * K
    v[0] = z + 1
    for _ in range(n):
        w = [z] * K
        for i in range(K):
            a = al[i] * v[i]
            if i + 1 < K:
                a = a + v[i + 1]
            if i > 0:
                a = a + be[i - 1] * v[i - 1]
            w[i] = a
        v = w
    return v[0]


def d_taylor(al, be, N, J):
    """Taylor coefficients of D(z)/z = Σ_n p_n(0) p_n(z) (orthonormal p_n),
    together with the partial sum 25 steps earlier (truncation gauge)."""
    Dn = [al[0] * 0 + 1]
    for b in be[:N - 1]:
        Dn.append(Dn[-1] * b)
    zero = al[0] * 0
    Pm = [zero] * (J + 2)
    Pn = [zero] * (J + 2)
    Pn[0] = zero + 1
    acc = [zero] * (J + 1)
    prev = None
    for n in range(N):
        inv = 1 / Dn[n]
        for j in range(J + 1):
            acc[j] = acc[j] + Pn[0] * Pn[j] * inv
        if n + 1 == N - 25:
            prev = list(acc)
        nxt = [zero] * (J + 2)
        for j in range(J + 1):
            nxt[j + 1] = nxt[j + 1] + Pn[j]
            nxt[j] = nxt[j] - al[n] * Pn[j]
            if n > 0:
                nxt[j] = nxt[j] - be[n - 1] * Pm[j]
        Pm, Pn = Pn, nxt
    conv = max(abs(acc[j] / prev[j] - 1) for j in range(J + 1))
    return acc, conv


def qpoch(a, base, n):
    r = base * 0 + 1
    t = base * 0 + 1
    for _ in range(n):
        r = r * (1 - a * t)
        t = t * base
    return r


def theta_series(w, u, kmax):
    """Σ_{k∈ℤ} (−1)^k w^{k(k+1)} u^k."""
    s = w * 0
    for k in range(-kmax, kmax + 1):
        s = s + (-1) ** (k % 2) * w ** (mpf(k * (k + 1))) * u ** k
    return s


def theta_product(w, u, nmax):
    """Jacobi triple product at base w²: (w²;w²)_∞ (w²u;w²)_∞ (u⁻¹;w²)_∞."""
    b = w * w
    return qpoch(b, b, nmax) * qpoch(b * u, b, nmax) * qpoch(1 / u, b, nmax)


# ------------------------------------------------------------------------ B1

def block_b1():
    """R1/R2 exact identities: E-absorption + recentring + JTP indices."""
    j, n, k, Es, ws, us = sp.symbols("j n k E w u", positive=True)
    checks = {}
    # recentring exponent (integers)
    ji, ni = sp.symbols("ji ni", integer=True)
    checks["recentring_exponent"] = sp.simplify(
        ji ** 2 + (1 - 2 * ni) * ji - ((ni - ni ** 2) + (ji - ni) * (ji - ni + 1)))
    # E-absorption: E^{-j} w^{j^2} (E w^{1-2n})^j = w^{n-n^2} w^{k(k+1)}, j=n+k
    ki = sp.symbols("ki", integer=True)
    lhs = Es ** (-(ni + ki)) * ws ** ((ni + ki) ** 2) * (Es * ws ** (1 - 2 * ni)) ** (ni + ki)
    rhs = ws ** (ni - ni ** 2) * ws ** (ki * (ki + 1))
    checks["E_absorption"] = sp.simplify(sp.powsimp(sp.expand(lhs / rhs), force=True) - 1)
    # JTP index base changes
    checks["theta_index_base_change"] = sp.simplify(ki * (ki + 1) - (ki * (ki - 1) + 2 * ki))
    checks["defect_index_base_change"] = sp.simplify(
        ki * (ki + 1) + ji * ki - (ki * (ki - 1) + (ji + 2) * ki))
    # balanced coefficient ratio, division-free
    gj, gj1, d0 = sp.symbols("gj gj1 d0")
    dj = d0 * (-1) ** ji * Es ** (-ji) * ws ** (ji ** 2) * gj
    dj1 = d0 * (-1) ** (ji + 1) * Es ** (-(ji + 1)) * ws ** ((ji + 1) ** 2) * gj1
    checks["dcoef_ratio"] = sp.simplify(
        sp.expand(dj * ws ** (2 * ji + 1) * gj1 / Es + dj1 * gj))
    for name, val in checks.items():
        assert sp.simplify(val) == 0, (name, val)
    # numeric identity: theta series == triple product
    mp.dps = 60
    w = mpf(1) / mpf(2)
    rels = []
    for uu in (mpf("1.37"), mpf("0.61"), mpf("2.9"), mpf("-1.4")):
        ts = theta_series(w, uu, 40)
        tp = theta_product(w, uu, 200)
        rels.append(abs(ts / tp - 1))
    assert max(rels) < mpf("1e-50"), max(rels)
    prog("B1", f"5 exact identities symbolically zero; JTP series=product "
               f"rel {nstr(max(rels), 3)}")
    return {"symbolic_identities": sorted(checks),
            "jtp_series_vs_product_rel": nstr(max(rels), 3)}


# ------------------------------------------------------------------------ B2

def block_b2():
    """Validate the D-pipeline against the KNOWN SW closed form."""
    mp.dps = 1500
    qt = mpf(2)
    pt = 1 / qt
    KM, KJ, N, J = 340, 170, 165, 30
    ms = sw_moments(qt, KM)
    al, be = qd_jacobi(ms, KJ)
    rep = max(abs(pow00(al, be, n) / ms[n] - 1) for n in (1, 10, 40, 80))
    d, conv = d_taylor(al, be, N, J)
    poch = mpf(1)
    rels = []
    for jj in range(1, J + 1):
        poch = poch * (1 - pt ** jj)
        closed = d[0] * (-1) ** jj * pt ** (jj * jj) / poch
        rels.append(abs(d[jj] / closed - 1))
    worst = max(rels)
    # the pipeline can only be as good as its own truncation gauge
    tol = 100 * conv
    assert worst < tol, (worst, tol)
    prog("B2", f"SW closed form d_j = c0(−1)^j w^{{j²}}/(w;w)_j reproduced to "
               f"{nstr(worst, 3)} (gauge {nstr(tol, 3)}), qd reproduction "
               f"{nstr(rep, 3)}")
    return {"qt": "2", "moment_reproduction": nstr(rep, 3),
            "N_truncation_gauge": nstr(conv, 3),
            "worst_rel_vs_closed_form": nstr(worst, 3),
            "tolerance": nstr(tol, 3)}


# ------------------------------------------------------- per-rung balanced run

def rung(label, a, b, KM, KJ, N, J, dps):
    mp.dps = dps
    qt = mpf(a) / b
    q = qt * qt
    p = 1 / q
    pt = 1 / qt
    E = 1 / (1 - p)
    ms = balanced_moments(qt, p, E, KM)
    al, be = qd_jacobi(ms, KJ)
    rep = max(abs(pow00(al, be, n) / ms[n] - 1) for n in (1, 10, 40, 80))
    d, conv = d_taylor(al, be, N, J)
    g = [d[j] * (-1) ** j * E ** j * qt ** (mpf(j * j)) / d[0] for j in range(J + 1)]
    rho = [None] + [(-d[j - 1] / d[j]) / (E * qt ** (2 * j - 1)) for j in range(1, J + 1)]
    return dict(label=label, qt=qt, q=q, p=p, pt=pt, E=E, al=al, be=be, d=d,
                g=g, rho=rho, conv=conv, rep=rep, J=J, N=N, dps=dps)


# ------------------------------------------------------------------------ B3

def block_b3(R):
    """Normalised tropical corners ρ_j and the constant C = lim (1−ρ_j)/w^j."""
    out = {}
    for r in R:
        mp.dps = r["dps"]
        pt, J = r["pt"], r["J"]
        Cs = [(1 - r["rho"][j]) / pt ** j for j in range(1, J + 1)]
        # ρ_j → 1: the corners approach the E-shifted lattice
        assert abs(1 - r["rho"][J]) < abs(1 - r["rho"][1]), "corners not converging"
        # C_j converges; rate must be pt (derived: ρ_j = 1 − C w^j + O(w^{2j}))
        tail = [Cs[j] for j in range(J - 12, J)]
        diffs = [tail[i + 1] - tail[i] for i in range(len(tail) - 1)]
        rates = [diffs[i + 1] / diffs[i] for i in range(len(diffs) - 1)]
        rate_err = max(abs(x - pt) for x in rates[-5:])
        assert rate_err < 10 * pt ** (J - 12), (r["label"], rate_err)
        # c_1 = C/(q̃−1)  (derived from ρ_j = Ψ(w^{j−1})/Ψ(w^j))
        C = tail[-1] + diffs[-1] * pt / (1 - pt)
        c1_pred = C / (r["qt"] - 1)
        sw_c1 = pt / (1 - pt)
        out[r["label"]] = {
            "moment_reproduction": nstr(r["rep"], 3),
            "N_truncation_gauge": nstr(r["conv"], 3),
            "rho_1": nstr(r["rho"][1], 12),
            "rho_J": nstr(r["rho"][J], 16),
            "C_limit": nstr(C, 14),
            "C_rate_err_vs_pt": nstr(rate_err, 3),
            "c1_from_C": nstr(c1_pred, 14),
            "c1_SW_closed_form": nstr(sw_c1, 14),
            "ratio_c1_over_c1SW": nstr(c1_pred / sw_c1, 12),
        }
        r["C"] = C
        prog("B3", f"{r['label']}: C = {nstr(C, 10)}, c1 = {nstr(c1_pred, 10)} "
                   f"(SW {nstr(sw_c1, 8)}), gauge {nstr(r['conv'], 3)}")
    return out


# ------------------------------------------------------------------------ B4

def _reconstruct(pt, g, M):
    """Least-squares-free exact solve g_m = A(1 + Σ_{j≤M} c_j w^{jm}), m = 0..M."""
    A = matrix(M + 1, M + 1)
    rhs = matrix(M + 1, 1)
    for row in range(M + 1):
        A[row, 0] = mpf(1)
        for jj in range(1, M + 1):
            A[row, jj] = pt ** (jj * row)
        rhs[row] = g[row]
    sol = lu_solve(A, rhs)
    Ac = sol[0]
    return Ac, [sol[jj] / Ac for jj in range(1, M + 1)]


def block_b4(R):
    """Hypothesis (H): g_m = g_infty * Psi(w^m) with Psi analytic.

    Two independent things are checked, neither of them a fit:
      (i)  OVERDETERMINATION - reconstruct Psi from g_0..g_M and predict the
           held-out g_{M+1}..g_J.  Under (H) the error must fall to the data's
           own truncation gauge.
      (ii) ORDER STABILITY - a Taylor coefficient c_j is retained only if two
           reconstructions of different order agree on it to 1e-6.  This fixes
           the reliable window by a stability criterion, not by inspection.
    """
    out = {}
    for r in R:
        mp.dps = r["dps"]
        pt, J, g = r["pt"], r["J"], r["g"]
        held = {}
        recs = {}
        Mmax = min(J - 8, 26)
        for M in range(4, Mmax + 1):
            Ac, c = _reconstruct(pt, g, M)
            recs[M] = (Ac, c)
            held[M] = max(abs(Ac * (1 + sum(c[jj - 1] * pt ** (jj * m)
                                            for jj in range(1, M + 1))) / g[m] - 1)
                          for m in range(M + 1, J + 1))
        # per-coefficient stability: c_j is retained only if the reconstructions
        # of orders M = j+2 .. j+7 agree on it to 1e-6.  This is a stability
        # criterion, not inspection of where the values look wrong.
        j_rel = 0
        for jj in range(1, Mmax - 7):
            vals = [recs[M][1][jj - 1] for M in range(jj + 2, min(jj + 8, Mmax) + 1)
                    if M in recs]
            if len(vals) < 3:
                break
            spread = max(abs(v / vals[0] - 1) for v in vals)
            if spread < mpf("1e-6"):
                j_rel = jj
            else:
                break
        Mtop = min(j_rel + 4, Mmax)
        assert j_rel >= 4, (r["label"], "reliable window too short", j_rel)
        # (H) must reconstruct held-out g_m down to the data's own gauge
        best = min(held.values())
        assert best < 1e4 * r["conv"], (r["label"], best, r["conv"])
        cs, ginf = recs[Mtop]
        # c_1 from the reconstruction vs the independent B3 route (C/(qt-1))
        c1_cross = abs(-cs[0] / (r["C"] / (r["qt"] - 1)) - 1)
        assert c1_cross < mpf("1e-8"), (r["label"], c1_cross)
        r["cs"], r["ginf"], r["j_rel"] = cs, ginf, j_rel
        out[r["label"]] = {
            "reliable_order_by_stability": j_rel,
            "fit_orders": [min(recs), Mtop, Mmax],
            "held_out_rel_err_by_M": {str(k): nstr(v, 3)
                                      for k, v in sorted(held.items())
                                      if k in (4, 6, 8, Mtop, Mmax)},
            "best_held_out": nstr(best, 3),
            "N_truncation_gauge": nstr(r["conv"], 3),
            "g_infinity": nstr(ginf, 16),
            "c1": nstr(cs[0], 14),
            "c1_cross_check_vs_B3": nstr(c1_cross, 3),
            "c_j_reliable": [nstr(cs[jj - 1], 10) for jj in range(1, j_rel + 1)],
        }
        prog("B4", f"{r['label']}: (H) held-out {nstr(best, 3)} (gauge "
                   f"{nstr(r['conv'], 3)}); stable to j={j_rel}; "
                   f"g_inf={nstr(ginf, 12)}")
    return out


# ----------------------------------------------------------------------- B4b

def block_b4b(R):
    """The exact structural difference: the SW corner function is rho(x) = 1 - x,
    a DEGREE-1 POLYNOMIAL; the balanced one is not rational.  Pade in x = w^j,
    overdetermined against held-out j."""
    out = {}
    for r in R:
        mp.dps = min(r["dps"], 400)
        pt, J, rho = r["pt"], r["J"], r["rho"]
        rows = []
        for dp in range(1, 6):
            for dq in range(0, 6):
                nun = dp + 1 + dq
                if nun + 6 > J:
                    continue
                A = matrix(nun, nun)
                bb = matrix(nun, 1)
                ok = True
                for i, jj in enumerate(range(1, nun + 1)):
                    x = pt ** jj
                    rr = rho[jj]
                    for e in range(dp + 1):
                        A[i, e] = x ** e
                    for e in range(dq):
                        A[i, dp + 1 + e] = -rr * x ** (e + 1)
                    bb[i] = rr
                try:
                    sol = lu_solve(A, bb)
                except Exception:
                    ok = False
                if not ok:
                    continue
                P = [sol[e] for e in range(dp + 1)]
                Q = [mpf(1)] + [sol[dp + 1 + e] for e in range(dq)]
                err = mpf(0)
                for jj in range(nun + 1, min(J, nun + 10) + 1):
                    x = pt ** jj
                    num = sum(P[e] * x ** e for e in range(dp + 1))
                    den = sum(Q[e] * x ** e for e in range(dq + 1))
                    err = max(err, abs(num / den / rho[jj] - 1))
                rows.append((dp, dq, err))
        best = min(rows, key=lambda t: t[2])
        # SW control: rho_SW(x) = 1 - x is EXACT at (dp, dq) = (1, 0)
        A = matrix(2, 2)
        bb = matrix(2, 1)
        for i, jj in enumerate((1, 2)):
            x = pt ** jj
            A[i, 0] = mpf(1)
            A[i, 1] = x
            bb[i] = 1 - x
        sol = lu_solve(A, bb)
        sw_err = max(abs((sol[0] + sol[1] * pt ** jj) / (1 - pt ** jj) - 1)
                     for jj in range(3, 14))
        assert sw_err < mpf("1e-30"), (r["label"], sw_err)
        # the balanced corner function is NOT degree-(1,0) rational
        d10 = [x for x in rows if x[0] == 1 and x[1] == 0][0][2]
        assert d10 > mpf("1e-3"), (r["label"], "unexpected rationality", d10)
        out[r["label"]] = {
            "sw_rho_is_1_minus_x_residual": nstr(sw_err, 3),
            "bal_rho_deg_1_0_residual": nstr(d10, 3),
            "bal_rho_best_pade": {"degP": best[0], "degQ": best[1],
                                  "held_out_residual": nstr(best[2], 3)},
            "bal_rho_pade_ladder": {f"({dp},{dq})": nstr(e, 3)
                                    for dp, dq, e in rows if dp <= 4 and dq <= 4},
        }
        prog("B4b", f"{r['label']}: rho_SW = 1-x exact ({nstr(sw_err, 3)}); "
                    f"rho_bal deg(1,0) residual {nstr(d10, 3)}, best Pade "
                    f"({best[0]},{best[1]}) -> {nstr(best[2], 3)}")
    return out


# ------------------------------------------------------------------------ B5

def _lsq_quadratic(js, ys):
    S = [mpf(0)] * 5
    T = [mpf(0)] * 3
    for jj, y in zip(js, ys):
        x = mpf(jj)
        for e in range(5):
            S[e] += x ** e
        T[0] += y
        T[1] += y * x
        T[2] += y * x * x
    A = matrix(3, 3)
    bb = matrix(3, 1)
    for i in range(3):
        for k in range(3):
            A[i, k] = S[i + k]
        bb[i] = T[i]
    sol = lu_solve(A, bb)
    return sol[2], sol[1], sol[0]


def block_b5(R):
    """R4 - the DERIVED transfer threshold.

    The master bound's even-j term is |c_{2s}| w^{2sn} w^{-s(s+1)} |u|^{-s}.
    Writing |c_j| ~ C exp(-a j^2) it converges (for every n) iff 4a > ln(1/w),
    i.e. a > a_SW/2 where a_SW = (1/2)ln(1/w) is the SW-core rate.  Reported,
    not asserted: the accessible window does not settle it.

    The DIRECT quantity is t_s := |c_{2s}| w^{-s(s+1)} - the actual bound terms
    with n = 0.  Its trend over the reliable window is the honest evidence.
    """
    out = {}
    for r in R:
        mp.dps = 60
        pt, cs, j_rel = r["pt"], r["cs"], r["j_rel"]
        L = mlog(1 / pt)
        a_sw_exact = L / 2
        thresh = L / 4
        lo = 2 if j_rel < 9 else 3
        js = list(range(lo, j_rel + 1))
        if len(js) < 4:
            js = list(range(1, j_rel + 1))
        a_bal, b_bal, _ = _lsq_quadratic(js, [-mlog(abs(cs[jj - 1])) for jj in js])
        poch = mpf(1)
        sw_c = []
        for jj in range(1, j_rel + 1):
            poch = poch * (1 - pt ** jj)
            sw_c.append((-1) ** jj * pt ** (mpf(jj * (jj + 1)) / 2) / poch)
        a_sw_fit, _, _ = _lsq_quadratic(js, [-mlog(abs(sw_c[jj - 1])) for jj in js])
        # estimator sanity only (the window is short; the bias is reported)
        assert a_sw_fit > 0, (r["label"], a_sw_fit)
        assert mpf("1") / 3 < a_sw_fit / a_sw_exact < 3, (r["label"], a_sw_fit)
        assert a_bal > 0, (r["label"], "balanced c_j do not decay Gaussianly")
        ts = [(s, abs(cs[2 * s - 1]) * pt ** (-s * (s + 1)))
              for s in range(1, j_rel // 2 + 1)]
        ts_sw = [(s, abs(sw_c[2 * s - 1]) * pt ** (-s * (s + 1)))
                 for s in range(1, j_rel // 2 + 1)]
        # the SW terms MUST decay (a_SW is exactly twice the threshold)
        assert ts_sw[-1][1] < ts_sw[0][1], (r["label"], "SW control failed")
        out[r["label"]] = {
            "window_j": [js[0], js[-1]],
            "a_balanced_lsq": nstr(a_bal, 10),
            "a_SW_exact": nstr(a_sw_exact, 10),
            "a_SW_same_estimator": nstr(a_sw_fit, 10),
            "estimator_bias_SW": nstr(a_sw_fit / a_sw_exact, 6),
            "threshold_a_gt": nstr(thresh, 10),
            "ratio_a_over_aSW_exact": nstr(a_bal / a_sw_exact, 8),
            "ratio_a_over_aSW_same_estimator": nstr(a_bal / a_sw_fit, 8),
            "transfer_condition_raw": bool(a_bal > thresh),
            "transfer_condition_bias_corrected": bool(a_bal / a_sw_fit > mpf(1) / 2),
            "master_bound_terms_t_s_balanced": [nstr(v, 6) for _, v in ts],
            "master_bound_terms_t_s_SW": [nstr(v, 6) for _, v in ts_sw],
            "t_s_balanced_decreasing_over_window": bool(ts[-1][1] < ts[0][1]),
        }
        r["a_bal"] = a_bal
        prog("B5", f"{r['label']}: a={nstr(a_bal, 8)} thr={nstr(thresh, 8)} "
                   f"ratio(a/a_SW)={nstr(a_bal / a_sw_exact, 6)} "
                   f"[bias-corrected {nstr(a_bal / a_sw_fit, 6)}]; "
                   f"t_s decreasing: {ts[-1][1] < ts[0][1]}")
    return out


# ------------------------------------------------------------------------ B6

def block_b6(R):
    """Zeros of Phi_bal vs the E-shifted lattice E w^{1-2n}; log_qt class -> phi1.
    kappa_bal is the DERIVED constant |c_1| w^{-1} (w;w^2)_inf^2/(w^2;w^2)_inf^2,
    which reduces to the awzero kappa(w) when |c_1| = w/(1-w)."""
    out = {}
    for r in R:
        J, d, qt, E, pt = r["J"], r["d"], r["qt"], r["E"], r["pt"]
        digits = float(-mlog(r["conv"]) / mlog(10))
        per_n2 = float(mlog(1 / pt) / mlog(10))
        nmax = int(msqrt(max(mpf(4), mpf(digits - 15) / per_n2)))
        nmax = max(4, min(nmax, J // 2 - 3, 20))
        mp.dps = int(per_n2 * (nmax + 4) ** 2) + 140
        dd = [+x for x in d]
        kap = abs(r["cs"][0]) / pt * qpoch(pt, pt * pt, 600) ** 2             / qpoch(pt * pt, pt * pt, 600) ** 2

        def phi(z):
            s = mp.mpf(0)
            for j in range(J, -1, -1):
                s = s * z + dd[j]
            return s

        found = []
        for n in range(1, nmax + 1):
            centre = E * qt ** (2 * n - 1)
            eps = min(mpf(1) / 2, 3 * kap * pt ** n)
            z = None
            for _try in range(4):
                lo, hi = centre * (1 - eps), centre * (1 + eps)
                flo, fhi = phi(lo), phi(hi)
                if flo * fhi < 0:
                    for _ in range(int(mp.dps * 3.4) + 40):
                        mid = (lo + hi) / 2
                        fm = phi(mid)
                        if fm == 0:
                            break
                        if flo * fm < 0:
                            hi, fhi = mid, fm
                        else:
                            lo, flo = mid, fm
                    z = (lo + hi) / 2
                    break
                eps = min(mpf(1) / 2, eps * 3)
            if z is not None:
                found.append((n, z))
        assert len(found) >= nmax - 2, (r["label"], len(found), nmax)
        Lq = mlog(qt)
        phi1_class = mlog(E) / Lq
        phi1_frac = phi1_class - mp.floor(phi1_class)
        devs = []
        for n, z in found:
            lg = mlog(z) / Lq - phi1_class
            devs.append(lg - mp.nint(lg))
        tail = devs[-8:] if len(devs) >= 8 else devs
        rates = [tail[i + 1] / tail[i] for i in range(len(tail) - 1)]
        rate_err = max(abs(x - pt) for x in rates[-3:])
        assert rate_err < 30 * pt ** (found[-1][0] - 5), (r["label"], rate_err)
        assert abs(devs[-1]) < abs(devs[0]), (r["label"], "class not converging")
        thetas = [(n, z / (E * qt ** (2 * n - 1)) - 1) for n, z in found]
        worst = max(abs(t) / (2 * kap * pt ** n) for n, t in thetas)
        assert worst < 1, (r["label"], "|theta_n| exceeds 2 kappa_bal w^n", worst)
        out[r["label"]] = {
            "n_zeros": len(found),
            "phi1_frac_log_qt_E": nstr(phi1_frac, 14),
            "class_dev_first": nstr(devs[0], 3),
            "class_dev_last": nstr(devs[-1], 3),
            "class_dev_rate_err_vs_pt": nstr(rate_err, 3),
            "kappa_bal_derived": nstr(kap, 12),
            "kappa_SW_awzero": nstr(qpoch(pt, pt * pt, 600) ** 2
                                    / ((1 - pt) * qpoch(pt * pt, pt * pt, 600) ** 2), 12),
            "worst_theta_over_2kappa_w_n": nstr(worst, 8),
            "zeros_low": [nstr(z, 14) for _, z in found[:5]],
        }
        prog("B6", f"{r['label']}: {len(found)} zeros, class dev "
                   f"{nstr(devs[0], 3)} -> {nstr(devs[-1], 3)} at rate w; "
                   f"|theta_n| <= 2 kappa_bal w^n worst {nstr(worst, 6)}")
    return out


# ------------------------------------------------------------------------ B7

Q_MUON = "1.10997859555733471"      # computations/ layer canonical q0 (muon pin)
Q_PROTON = "1.10997858275138081"    # proton pin (package layer), 17 dp like Q_MUON
# Was "1.10997861", commented "proton-pinned spot value" — but that literal is
# +24.5 ppb from the proton pin, i.e. 2.1x the ~11.5 ppb mu-p substrate tension
# this very probe measures. A muon-vs-proton comparison run against it was
# comparing the muon pin to a point 2 tensions past proton, so the quantity it
# reported as the mu-p difference was wrong by more than the difference itself.
# The comparison is deliberate and correct; only the proton value was not.


def _theta_abs(w, r, kmax=400):
    """Theta(r) = (1/(w r)) * sum_{l in Z} w^{l^2} r^l  - the ALL-POSITIVE theta
    that replaces |vartheta| when the cancellation is discarded."""
    s = w * 0
    for l in range(-kmax, kmax + 1):
        s = s + w ** (l * l) * r ** l
    return s / (w * r)


def _l1_constants(w, Gam, nmax=800):
    """Closed-form ingredients of the l1 (no-cancellation) route."""
    w2 = w * w
    A = qpoch(w2, w2, nmax)             # (w^2;w^2)_inf
    B = qpoch(w, w2, nmax)              # (w;w^2)_inf
    kap = Gam * _theta_abs(w, mpf(1)) / A ** 3
    # counting condition on |u| = w^{-1}:  Gam w^n Theta(w^{-1}) < A B^2
    n_count = 0
    lhs = Gam * _theta_abs(w, 1 / w)
    rhs = A * B ** 2
    while lhs > rhs:
        lhs = lhs * w
        n_count += 1
    # localization at eps* = (1-w^2)/2:  Gam w^n Theta(1+eps) < A eps/(1+eps) P^2
    eps = (1 - w2) / 2
    P = qpoch(w2 / (1 - eps), w2, nmax)
    n_loc = 0
    lhs = Gam * _theta_abs(w, 1 + eps)
    rhs = A * eps / (1 + eps) * P ** 2
    while lhs > rhs:
        lhs = lhs * w
        n_loc += 1
    return kap, max(n_count, n_loc), n_count, n_loc


def block_b7(R):
    """The l1 (no-cancellation) transfer that DOES go through.

    Hypothesis (H1)   |g_m - g_inf| <= Gam * g_inf * w^m   for all m >= 0
    (and trivially for m < 0, where g_m = 0 and w^m >= 1, provided Gam >= 1).
    Then |D_n(u)| <= Gam g_inf w^n Theta(|u|) with Theta the ALL-POSITIVE theta;
    Rouche closes with the CLOSED-FORM constant and index

        kappa_l1 = Gam Theta(1) / (w^2;w^2)_inf^3 ,
        n_0 = least n with  Gam w^n Theta(w^{-1}) < (w^2;w^2)_inf (w;w^2)_inf^2
              and           Gam w^n Theta(1+eps) < (w^2;w^2)_inf eps/(1+eps) P^2,
                            eps = (1-w^2)/2, P = (w^2/(1-eps); w^2)_inf.

    This throws away the theta cancellation, so n_0 is far larger than the SW
    theorem's - but it needs only ONE measured constant, not the Gaussian decay
    of the whole Taylor sequence.  Gam is measured directly from g_m with no
    ill-conditioning.
    """
    out = {}
    for r in R:
        mp.dps = 60
        pt, g, ginf, J = r["pt"], r["g"], r["ginf"], r["J"]
        gam = max(abs(1 - g[m] / ginf) / pt ** m for m in range(J + 1))
        assert gam < mp.inf and gam > 0, (r["label"], gam)
        # Gam -> |c_1| asymptotically (derived); check the sup is close to it
        gam_use = max(gam, mpf(1))
        kap, n0, nc, nl = _l1_constants(pt, gam_use)
        kap_sharp = abs(r["cs"][0]) / pt * qpoch(pt, pt * pt, 600) ** 2 \
            / qpoch(pt * pt, pt * pt, 600) ** 2
        out[r["label"]] = {
            "Gamma_measured": nstr(gam, 12),
            "abs_c1": nstr(abs(r["cs"][0]), 12),
            "Gamma_over_abs_c1": nstr(gam / abs(r["cs"][0]), 8),
            "kappa_l1": nstr(kap, 10),
            "kappa_sharp_theta_route": nstr(kap_sharp, 10),
            "price_of_discarding_cancellation": nstr(kap / kap_sharp, 6),
            "n0_l1": n0, "n0_counting": nc, "n0_localization": nl,
        }
        prog("B7", f"{r['label']}: Gamma={nstr(gam, 8)} (|c1|="
                   f"{nstr(abs(r['cs'][0]), 8)}), kappa_l1={nstr(kap, 6)}, "
                   f"n0_l1={n0} (sharp kappa {nstr(kap_sharp, 6)})")
    # substrate pins: n_0 depends on Gamma only LOGARITHMICALLY, so a range of
    # Gamma is reported instead of an unmeasured pin value.
    mp.dps = 60
    pins = {}
    for name, qs in (("muon", Q_MUON), ("proton", Q_PROTON)):
        w = 1 / msqrt(mpf(qs))
        row = {"w": nstr(w, 20)}
        for Gam in (mpf(1), mpf(3), mpf(10), mpf(1000)):
            kap, n0, nc, nl = _l1_constants(w, Gam)
            row[f"Gamma={int(Gam)}"] = {"kappa_l1": nstr(kap, 6), "n0_l1": n0,
                                        "n0_counting": nc, "n0_localization": nl}
        pins[name] = row
    out["substrate_pins"] = pins
    ex = pins["muon"]["Gamma=3"]
    prog("B7", f"muon pin (Gamma=3): n0_l1={ex['n0_l1']}, "
               f"kappa_l1={ex['kappa_l1']} — compare the SW theorem's n0=135")
    return out


# ------------------------------------------------------------------------ main

def main() -> int:
    results = {}
    prog("B1", "exact identities (E-absorption, recentring, JTP indices) ...")
    results["B1_exact_identities"] = block_b1()
    prog("B2", "pipeline validation against the SW closed form ...")
    results["B2_pipeline_validation_sw"] = block_b2()
    prog("B3", "balanced d_j, normalised corners, C ...")
    R = []
    for cfg in RUNGS:
        R.append(rung(*cfg))
        prog("B3", f"rung {cfg[0]} built")
    results["B3_balanced_corners"] = block_b3(R)
    prog("B4", "hypothesis (H) reconstruction ...")
    results["B4_hypothesis_H"] = block_b4(R)
    prog("B4b", "rho_SW = 1 - x exact vs rho_bal non-rational ...")
    results["B4b_corner_function"] = block_b4b(R)
    prog("B5", "derived transfer threshold 4a > ln(1/w) ...")
    results["B5_transfer_threshold"] = block_b5(R)
    prog("B6", "zeros of Phi_bal vs the E-shifted lattice ...")
    results["B6_zeros_and_class"] = block_b6(R)
    prog("B7", "l1 (no-cancellation) transfer: Gamma, kappa_l1, n0 ...")
    results["B7_l1_transfer"] = block_b7(R)
    results["summary"] = {
        "target": "does the SW-core theta-limit Rouché machinery transfer to the "
                  "BALANCED family's Nevanlinna D-function?",
        "verdict": "YES for the structure, CONDITIONALLY for the theorem. The "
                   "E-shifted recentring z = E w^{1−2n}u makes E cancel "
                   "IDENTICALLY; the recentred balanced series is the SW one "
                   "with 1/(w;w)_{n+k} → g_{n+k}; the theta limit is the SAME "
                   "Jacobi triple product at base w², so the candidate zero "
                   "lattice is exactly the balanced tropical lattice. The whole "
                   "defect/telescoping/Rouché apparatus transfers VERBATIM under "
                   "hypothesis (H) (g_m = g_∞ Ψ(w^m), Ψ analytic), whose "
                   "coefficients replace the SW ones; (H) is measured to the "
                   "data's own gauge but NOT proved.",
        "derived_threshold": "the master bound converges iff 4a > ln(1/w) where "
                             "|c_j| ≍ C e^{−a j²}; SW has a = ½ln(1/w), exactly "
                             "twice the threshold. Measured balanced a is "
                             "reported per rung.",
        "residual": "(i) (H) is not proved; (ii) the Gaussian rate a is measured "
                    "on a finite, conditioning-limited window; (iii) no rung at "
                    "the substrate pins (out of budget); (iv) nothing wired.",
        "scope": "no scope-(b) claims anywhere",
    }
    src = Path(__file__)
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                          text=True, cwd=HERE, check=False).stdout.strip() or "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "mpmath+sympy",
        "engineVersion": f"python {platform.python_version()}",
        "commitSha": head,
        "scriptFile": src.name,
        "scriptHash": hashlib.sha256(src.read_bytes()).hexdigest()[:12],
        "scriptCommitSha": git_sha(src),
        "computation": "baldfn-theta-limit",
        "description": ("Balanced Nevanlinna D-function: the E-shifted recentring "
                        "absorbs E exactly, the theta limit is the same Jacobi "
                        "triple product, and the SW Rouché apparatus transfers "
                        "under an explicit measured hypothesis (H) with the "
                        "derived threshold 4a > ln(1/w)"),
        "auditOnly": "docs/audits/2026-08-01-balanced-theta-limit.md",
        "bean": "qou-r4ya",
        "allPassed": True,
        "precisionMetadata": {"per_rung_dps": {c[0]: c[7] for c in RUNGS},
                              "zero_finding_dps": "log10(1/w)·(n_max+4)² + 120"},
        "data": results,
    }
    WITNESS.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n✓ Witness: {WITNESS.name}  (8 assertion blocks, all passed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
