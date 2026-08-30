#!/usr/bin/env python3
"""ksel2id_friedrichs_selection_probe.py — KSel-2-ID (bean qou-0ms0):
which self-adjoint extension of the balanced Jacobi operator J(q) is
which named kernel candidate — and does the bar reflection exchange
Friedrichs and Krein?

AUDIT-ONLY — scope-(a) except where a cited invariant is named, NO FIT,
nothing wired. Exact-Q qd-algorithm leg + mpf legs certified by moment
reproduction; all tolerances stated.

BACKGROUND (2026-08-01-ksel2-gns-favard-canonicity.md). The balanced
moments m_k = q^{-k(k-1)/4}[k]_q! are Stieltjes-indeterminate at q > 1;
the minimal Jacobi operator J(q) has deficiency (1,1); its self-adjoint
extensions form a circle; the Friedrichs (J_F) and Krein (J_K)
extensions are the two canonical Stieltjes candidates ([simon1998],
[pedersen1995]). The named kernel candidates from the (REP)/KSel
campaign: the u = 1 theta-grid kernel, the u = qtilde^{1/2} shifted
grid (atoms (u/(1-p)) qtilde^Z, accumulating at 0), and the absolutely
continuous Jackson (*) log-normal kernel.

METHOD.
  * Jacobi coefficients (alpha_k, beta_k) from the moments by the
    quotient-difference (qd) algorithm — exact rational arithmetic at
    r = q^{1/4} rational (kernel-frame moments are rational in r), and
    mpf at dps 400 certified by (M^n)_00 = m_n reproduction.
  * FRIEDRICHS = limit of plain truncations: the polynomials are BY
    DEFINITION a form core of the Friedrichs extension, so by min-max
    every truncation eigenvalue lambda_j(N) DECREASES to lambda_j(J_F)
    (variational argument; [simon1998] Sect. 3, [pedersen1995]).
  * KREIN = the canonical solution with 0 in its support
    ([pedersen1995]): approximated by Gauss-Radau truncations with the
    node pinned at 0 (last diagonal shifted by t_N = P_N(0)/P_{N-1}(0)).
  * Extension circle interpolation: last-diagonal boundary shifts
    s * t_N, s in [0, 1] sweep from the Friedrichs to the Krein
    approximant; s > 1 leaves the nonnegative (Stieltjes) class.

DEFORMATION POINTS. Structural runs at r = 6/5 (q = 2.0736, strong
deformation — truncations converge fast, qtilde-steps are wide) and
r = 21/20 (q ~ 1.2155, exact-Q leg); q0-pin legs (muon + proton)
verify positivity/monotonicity/machinery — the pins sit deep in the
pre-asymptotic window (qtilde - 1 ~ 0.054), so grid-class asymptotics
are read off at the strong-deformation point, stated as such.

SECTIONS:

  F1  Exact-Q qd at r = 21/20, K = 26: Favard positivity beta_k > 0 to
      depth 25 (extends the KSel-2 K3 exact depth 9), beta_1 =
      qtilde + 1/qtilde - 1 exact, moment reproduction exact (n <= 12).
  F2  mpf qd at r = 6/5, dps 400, K = 48: beta_k > 0, moment
      reproduction certificate; cross-check vs exact-Q qd (K = 12).
  F3  Friedrichs truncation study (r = 6/5, N = 36/42/48): lambda_j(N)
      strictly decreasing in N for every j (min-max), lambda_min
      converged (Cauchy), lambda_F in (0.33, 0.34) — strictly positive.
  F4  Krein/Radau (r = 6/5, N = 48): pinned eigenvalue at 0 (< 1e-80),
      mass at 0 equals 1/sum_{k<N} p_k(0)^2 (exact Radau identity,
      checked to 1e-25), sum p_k(0)^2 partials converge (indeterminacy
      corroboration), positive Krein atoms converged and INTERLACING
      the Friedrichs atoms.
  F5  Grid identification (r = 6/5): atom-spacing in qtilde-steps
      decreases monotonically to 2 — the extremal supports are
      asymptotically q-LATTICES (spacing q = qtilde^2), NOT
      qtilde-lattices; the qtilde-class of the Friedrichs atoms drifts
      monotonically to the u = 1 class phi_1 = frac(log_qtilde
      (q/(q-1))) (Aitken limit within tolerance; the half-shifted
      u = qtilde^{1/2} class is rejected by ~0.5), and the Krein atoms
      drift to the SAME class — F and K asymptotically occupy the two
      complementary q-sublattices of the ONE u = 1 qtilde-grid. Exact
      low-end mismatch: the low Friedrichs atoms are OFF the u = 1
      lattice (class distance > 0.1), and every u-translate kernel has
      support accumulating at 0 while every self-adjoint extension has
      discrete spectrum with no finite accumulation point (compact
      resolvent in the indeterminate case, [simon1998]) and
      lambda_F > 0. VERDICT: NONE of the three named candidates is the
      Friedrichs or the Krein measure — the u-continuum and the a.c.
      kernel are non-canonical solutions (interior Nevanlinna points).
  F6  Circle sweep (r = 6/5, N = 44): lambda_min(s t_N) strictly
      decreasing along s in {0, 1/4, 1/2, 3/4, 1}, ~ 0 at s = 1, and
      NEGATIVE at s = 3/2 — beyond-Krein boundary conditions leave the
      Stieltjes (nonnegative) class.
  F7  q0-pin legs (muon + proton; K = 24, dps 500 qd; eigen N =
      16/20/24): beta_k > 0, reproduction certificate, lambda_min(N)
      strictly decreasing and positive, Radau pin at 0, mass-at-0
      identity — machinery verified at the substrate; asymptotic-class
      readout deferred to the strong-deformation leg (stated).
  F8  Bar reflection sigma: s -> qtilde^{-1}/s.
      (i) sympy exact: sigma fixes the SW factor LN(-L/2, L)
          (pushforward invariance — completion of the square), and on
          qtilde-grid classes acts as phi -> -phi with fixed classes
          exactly {0, 1/2} = the u = 1 and u = qtilde^{1/2} classes
          (the ksel1 R4 pair).
      (ii) OBSTRUCTION (scope-(b), cited invariant): every self-adjoint
          extension measure has smallest positive support point
          s_min > 0 (discrete spectrum; Krein additionally an atom AT
          0, whose sigma-image is not a finite measure), so sigma_* of
          an extension measure has support in the BOUNDED interval
          (0, 1/(qtilde s_min)]; bounded-support moments grow at most
          geometrically, while m_k / C^k -> oo for every C (moment
          ratio m_{k+1}/m_k -> oo, verified exactly) — sigma_* of an
          extension measure is NEVER a representing measure. The bar
          reflection does NOT act on the extension circle by
          pushforward; in particular it does NOT exchange Friedrichs
          and Krein. (A non-pushforward action on the Nevanlinna
          parameter is not excluded — scope-(a) open.)
      (iii) numeric corroboration: sigma-moment ratios of the
          truncated Friedrichs measure vs m_k at r = 6/5 and
          r = 21/20: off by O(1) at k = 1 and collapsing at k = 8.

Exit 0 iff all assertions pass. Witness:
ksel2id-friedrichs-selection.witness.json (audit-only).
Audit doc: docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, sqrt as msqrt, log as mlog  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

K_EXACT = 26     # exact-Q qd depth at r = 21/20
K_DEF = 48       # mpf qd depth at r = 6/5
K_PIN = 24       # mpf qd depth at the pins
QD_DPS = 400     # working dps for the deformation-leg qd
PIN_DPS = 500    # working dps for the pin-leg qd
EIG_DPS = 120    # eigen decomposition dps


# ------------------------------------------------------- moment machinery

def qint(qv, k: int):
    s = qv * 0
    x = qv ** 0
    for _ in range(k):
        s = s + x
        x = x * qv
    return s


def balanced_moments(rv, kmax: int):
    """m_k = r^{-k(k-1)} [k]_{r^4}!  (rational in r = q^{1/4})."""
    q = rv ** 4
    out = []
    for k in range(kmax + 1):
        f = rv ** 0
        for j in range(1, k + 1):
            f = f * qint(q, j)
        out.append(rv ** (-k * (k - 1)) * f)
    return out


def qd_jacobi(ms, K):
    """Monic Jacobi data (alpha_0..alpha_{K-1}, beta_1..beta_{K-1}) from
    moments via the quotient-difference algorithm (Rutishauser; Henrici;
    Gautschi, Orthogonal Polynomials): q_1^{(n)} = m_{n+1}/m_n;
    e_k^{(n)} = q_k^{(n+1)} - q_k^{(n)} + e_{k-1}^{(n+1)};
    q_{k+1}^{(n)} = q_k^{(n+1)} e_k^{(n+1)} / e_k^{(n)};
    alpha_0 = q_1^{(0)}, alpha_k = q_{k+1}^{(0)} + e_k^{(0)},
    beta_k = q_k^{(0)} e_k^{(0)}. Field-agnostic (Fraction or mpf)."""
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
    be = [q0[k - 1] * e0[k - 1]
          for k in range(1, min(len(q0), len(e0)) + 1)]
    return al, be


def pow00(al, be, n):
    """(M^n)_00 for the monic Jacobi matrix — the GNS moment identity."""
    K = len(al)
    zero = al[0] * 0
    v = [zero] * K
    v[0] = zero + 1
    for _ in range(n):
        w = [zero] * K
        for i in range(K):
            a = al[i] * v[i]
            if i + 1 < K:
                a = a + v[i + 1]
            if i > 0:
                a = a + be[i - 1] * v[i - 1]
            w[i] = a
        v = w
    return v[0]


def monic_p_at_zero(al, be, K):
    """Monic orthogonal polynomials at 0: P_0(0)=1, P_1(0)=-alpha_0,
    P_{n+1}(0) = -alpha_n P_n(0) - beta_n P_{n-1}(0)."""
    P0 = [al[0] * 0 + 1, -al[0]]
    for n in range(1, K):
        P0.append(-al[n] * P0[n] - be[n - 1] * P0[n - 1])
    return P0


def sym_trunc_eig(al_f, be_f, N, tshift=None):
    """Eigen-decomposition of the symmetric N-truncation (diag alpha,
    off-diag sqrt(beta)); optional last-diagonal boundary shift."""
    A = mp.zeros(N)
    for i in range(N):
        A[i, i] = al_f[i]
        if i + 1 < N:
            A[i, i + 1] = A[i + 1, i] = msqrt(be_f[i])
    if tshift is not None:
        A[N - 1, N - 1] += tshift
    E, EV = mp.eigsy(A)
    lam = [E[i] for i in range(N)]
    w = [EV[0, i] ** 2 for i in range(N)]     # spectral masses (m_0 = 1)
    return lam, w


def frac1(x):
    """Fractional part in [0, 1) (mp.frac is signed for x < 0)."""
    return x - mp.floor(x)


def circ_dist(a, b):
    """Distance on R/Z."""
    d = abs(frac1(a) - frac1(b))
    return min(d, 1 - d)


def aitken(seq):
    """Aitken Delta^2 extrapolation of the last three terms."""
    x0, x1, x2 = seq[-3], seq[-2], seq[-1]
    d1, d2 = x1 - x0, x2 - x1
    return x2 + d2 * d2 / (d1 - d2) if d1 != d2 else x2


# ---------------------------------------------------------- F1 exact leg

def block_f1_exact(wb: WitnessBuilder):
    _ok: list[bool] = []
    r = Fr(21, 20)
    ms = balanced_moments(r, 2 * K_EXACT + 2)
    al, be = qd_jacobi(ms, K_EXACT)
    _ok.append(bool(all((b > 0 for b in be))))
    assert _ok[-1], 'Favard positivity depth 25'
    qt = r * r
    _ok.append(bool(be[0] == qt + 1 / qt - 1))
    assert _ok[-1], be[0]
    for n in range(13):
        _ok.append(bool(pow00(al, be, n) == ms[n]))
        assert _ok[-1], (n, 'exact reproduction')
    wb.add_assertion(
        "f1_exact_qd_favard_depth25", computed=all(_ok), expected=True,
        tolerance=0,
        source="exact rational qd algorithm at r = 21/20 (q ~ 1.2155), "
               "K = 26: all Jacobi beta_k > 0 for k <= 25 (extends the "
               "KSel-2 K3 exact Favard depth 9), beta_1 = qtilde + "
               "1/qtilde - 1 exact, and (M^n)_00 = m_n exact for "
               "n <= 12 — the qd route reproduces the canonical "
               "operator exactly")
    return al, be, ms


# ----------------------------------------------- F2 deformation-leg qd

def block_f2_deformation_qd(wb: WitnessBuilder):
    _ok: list[bool] = []
    mp.dps = QD_DPS
    r = mpf(6) / 5
    ms = balanced_moments(r, 2 * K_DEF + 2)
    al, be = qd_jacobi(ms, K_DEF)
    _ok.append(bool(all((b > 0 for b in be))))
    assert _ok[-1], 'beta > 0 at r = 6/5'
    worst = max(abs(pow00(al, be, n) / ms[n] - 1) for n in range(1, 25))
    _ok.append(bool(worst < mpf('1e-300')))
    assert _ok[-1], worst
    # cross-check vs exact rational qd at K = 12
    re_ = Fr(6, 5)
    mse = balanced_moments(re_, 2 * 12 + 2)
    ale, bee = qd_jacobi(mse, 12)
    xworst = mpf(0)
    for k in range(12):
        ev = mpf(ale[k].numerator) / mpf(ale[k].denominator)
        xworst = max(xworst, abs(al[k] / ev - 1))
        if k < 11:
            ev = mpf(bee[k].numerator) / mpf(bee[k].denominator)
            xworst = max(xworst, abs(be[k] / ev - 1))
    _ok.append(bool(xworst < mpf('1e-350')))
    assert _ok[-1], xworst
    wb.add_assertion(
        "f2_deformation_qd_certified", computed=all(_ok), expected=True,
        tolerance=1e-300,
        source=f"mpf qd at r = 6/5 (q = 2.0736), dps {QD_DPS}, "
               f"K = {K_DEF}: beta_k > 0 all k, moment reproduction "
               f"rel < 1e-300 (measured {mp.nstr(worst, 3)}), and "
               "agreement with the exact-Q qd (K = 12) to rel < 1e-350")
    return al, be, ms


# ------------------------------------------- F3 Friedrichs truncations

def block_f3_friedrichs(wb: WitnessBuilder, al, be):
    _ok: list[bool] = []
    mp.dps = EIG_DPS
    alf = [+a for a in al]
    bef = [+b for b in be]
    res = {}
    for N in (36, 42, 48):
        lam, w = sym_trunc_eig(alf, bef, N)
        res[N] = (lam, w)
    # min-max monotonicity: lambda_j(N) strictly decreasing in N
    for j in range(36):
        _ok.append(bool(res[48][0][j] < res[42][0][j] < res[36][0][j]))
        assert _ok[-1], j
    lam48, w48 = res[48]
    cauchy0 = abs(res[48][0][0] / res[42][0][0] - 1)
    _ok.append(bool(cauchy0 < mpf('1e-4')))
    assert _ok[-1], cauchy0
    _ok.append(bool(mpf('0.33') < lam48[0] < mpf('0.34')))
    assert _ok[-1], lam48[0]
    # per-j convergence table for the class window
    conv = [abs(res[48][0][j] / res[42][0][j] - 1) for j in range(20)]
    wb.add_assertion(
        "f3_friedrichs_limit_positive", computed=all(_ok), expected=True,
        tolerance=1e-4,
        source="r = 6/5: truncation eigenvalues lambda_j(N) strictly "
               "decrease in N for every j (polynomials are a form core "
               "of the Friedrichs extension => min-max; the truncation "
               "limit IS J_F, [simon1998] / [pedersen1995]); "
               f"lambda_min(48) = {mp.nstr(lam48[0], 12)}, Cauchy rel "
               f"{mp.nstr(cauchy0, 3)} (N = 42 vs 48): lambda_F in "
               "(0.33, 0.34) STRICTLY POSITIVE — the Friedrichs "
               "measure has no support near 0")
    wb.add_data("f3_friedrichs", {
        "lambda_low_N48": [mp.nstr(lam48[j], 15) for j in range(8)],
        "cauchy_rel_per_j_42_48": [mp.nstr(c, 3) for c in conv],
        "monotone": "lambda_j(48) < lambda_j(42) < lambda_j(36) for "
                    "all j < 36 — verified",
    })
    return lam48, w48


# ------------------------------------------------- F4 Krein via Radau

def block_f4_krein(wb: WitnessBuilder, al, be, lamF):
    _ok: list[bool] = []
    mp.dps = QD_DPS
    P0 = monic_p_at_zero(al, be, K_DEF)
    mp.dps = EIG_DPS
    alf = [+a for a in al]
    bef = [+b for b in be]
    N = 48
    tsh = +(P0[N] / P0[N - 1])
    lamK, wK = sym_trunc_eig(alf, bef, N, tshift=tsh)
    _ok.append(bool(abs(lamK[0]) < mpf('1e-80')))
    assert _ok[-1], lamK[0]
    _ok.append(bool(all((x > 0 for x in lamK[1:]))))
    assert _ok[-1], 'Krein atoms positive'
    # Radau mass-at-0 identity: w_0 = 1 / sum_{k<N} p_k(0)^2
    mp.dps = QD_DPS
    D = [mpf(1)]
    for b in be:
        D.append(D[-1] * b)
    Ssum = mp.fsum(P0[k] ** 2 / D[k] for k in range(N))
    mp.dps = EIG_DPS
    massid = abs(wK[0] * Ssum - 1)
    _ok.append(bool(massid < mpf('1e-25')))
    assert _ok[-1], massid
    # indeterminacy corroboration: sum p_k(0)^2 partials converge
    mp.dps = QD_DPS
    parts = [mp.fsum(P0[k] ** 2 / D[k] for k in range(m))
             for m in (16, 26, 36, 48)]
    incs = [parts[i + 1] - parts[i] for i in range(3)]
    _ok.append(bool(incs[2] < incs[1] < incs[0]))
    assert _ok[-1], 'sum p_k(0)^2 increments'
    _ok.append(bool(incs[2] / incs[1] < mpf('0.9')))
    assert _ok[-1], 'convergent trend'
    # convergence of the first Krein atoms (N = 42 vs 48)
    mp.dps = EIG_DPS
    tsh42 = +(P0[42] / P0[41])
    lamK42, _ = sym_trunc_eig(alf, bef, 42, tshift=tsh42)
    ck = abs(lamK[1] / lamK42[1] - 1)
    _ok.append(bool(ck < mpf('1e-4')))
    assert _ok[-1], ck
    # interlacing with Friedrichs
    for j in range(6):
        _ok.append(bool(lamF[j] < lamK[j + 1] < lamF[j + 1]))
        assert _ok[-1], (j, 'interlace')
    wb.add_assertion(
        "f4_krein_radau_pinned_at_zero", computed=all(_ok), expected=True,
        tolerance=1e-25,
        source="r = 6/5, N = 48 Gauss-Radau truncation with node pinned "
               "at 0 (boundary shift t_N = P_N(0)/P_{N-1}(0)) — the "
               "canonical solution with 0 in supp = the KREIN extension "
               "measure ([pedersen1995]): pinned eigenvalue < 1e-80, "
               "all other atoms > 0 and Cauchy (rel < 1e-4), mass at 0 "
               "= 1/sum_{k<48} p_k(0)^2 to < 1e-25, sum p_k(0)^2 "
               "convergent (indeterminacy corroboration), and the "
               "positive Krein atoms INTERLACE the Friedrichs atoms")
    wb.add_data("f4_krein", {
        "krein_atoms_low": [mp.nstr(lamK[j], 12) for j in range(1, 8)],
        "mass_at_zero": mp.nstr(wK[0], 10),
        "sum_pk0_sq_partials": [mp.nstr(x, 10) for x in parts],
        "inf_supp": "0 (atom) — vs Friedrichs inf supp ~ 0.3367: the "
                    "Friedrichs solution has the LARGEST smallest "
                    "support point (Pedersen), Krein the smallest",
    })
    return lamK, wK


# --------------------------------------------- F5 grid identification

def block_f5_grid(wb: WitnessBuilder, lamF, wF, lamK):
    _ok: list[bool] = []
    mp.dps = EIG_DPS
    r = mpf(6) / 5
    q = r ** 4
    qt = r ** 2
    Lq = mlog(qt)
    p = 1 / q
    phi1 = frac1(mlog(1 / (1 - p)) / Lq)     # u = 1 class
    phi_half = frac1(phi1 + mpf(1) / 2)      # u = qtilde^{1/2} class
    # spacing in qtilde-steps: monotone decreasing to 2
    steps = [mlog(lamF[j + 1] / lamF[j]) / Lq for j in range(3, 18)]
    _ok.append(bool(all((steps[i + 1] < steps[i] for i in range(len(steps) - 1)))))
    assert _ok[-1], 'spacing monotone'
    _ok.append(bool(mpf('1.995') < steps[-1] < mpf('2.05')))
    assert _ok[-1], steps[-1]
    # Friedrichs class drift -> phi1 (Aitken on the monotone tail)
    classesF = [frac1(mlog(lamF[j]) / Lq) for j in range(3, 19)]
    tail = classesF[:]
    while len(tail) > 3 and not all(
            tail[i + 1] > tail[i] for i in range(len(tail) - 1)):
        tail = tail[1:]
    _ok.append(bool(len(tail) >= 6))
    assert _ok[-1], 'monotone class tail'
    extF = aitken(tail)
    dF = circ_dist(extF, phi1)
    dFh = circ_dist(extF, phi_half)
    _ok.append(bool(dF < mpf('0.01')))
    assert _ok[-1], (extF, phi1)
    _ok.append(bool(dFh > mpf('0.4')))
    assert _ok[-1], dFh
    # Krein class drift -> same class
    classesK = [frac1(mlog(lamK[j]) / Lq) for j in range(3, 14)]
    tailK = classesK[:]
    while len(tailK) > 3 and not all(
            tailK[i + 1] > tailK[i] for i in range(len(tailK) - 1)):
        tailK = tailK[1:]
    _ok.append(bool(len(tailK) >= 4))
    assert _ok[-1], 'monotone Krein class tail'
    extK = aitken(tailK)
    dK = circ_dist(extK, phi1)
    _ok.append(bool(dK < mpf('0.04')))
    assert _ok[-1], (extK, phi1)
    # exact low-end mismatch: lowest Friedrichs atom is OFF the u=1 grid
    d0 = circ_dist(mlog(lamF[0]) / Lq, phi1)
    _ok.append(bool(d0 > mpf('0.1')))
    assert _ok[-1], d0
    wb.add_assertion(
        "f5_extremal_grids_q_lattice_u1_class", computed=all(_ok),
        expected=True, tolerance=0.01,
        source="r = 6/5: Friedrichs atom spacing in qtilde-steps "
               "decreases monotonically to 2 (last window value "
               f"{mp.nstr(steps[-1], 8)}) — the extremal supports are "
               "asymptotically q-LATTICES, incommensurate with the "
               "u-continuum's qtilde-grids; the qtilde-class of the "
               f"Friedrichs atoms Aitken-extrapolates to "
               f"{mp.nstr(extF, 6)} vs the u = 1 class phi_1 = "
               f"{mp.nstr(phi1, 6)} (circ dist {mp.nstr(dF, 3)}; "
               f"half-shifted class rejected, dist {mp.nstr(dFh, 3)}), "
               f"and the Krein class extrapolates to {mp.nstr(extK, 6)} "
               f"(dist {mp.nstr(dK, 3)}) — F and K asymptotically "
               "occupy complementary q-sublattices of the ONE u = 1 "
               "qtilde-grid; the LOW Friedrichs atoms are off that "
               f"grid (lambda_0 class dist {mp.nstr(d0, 3)} > 0.1)")
    wb.add_data("f5_grid", {
        "phi_u1": mp.nstr(phi1, 8),
        "phi_u_sqrt_qtilde": mp.nstr(phi_half, 8),
        "steps_qtilde_window": [mp.nstr(s, 8) for s in steps],
        "classesF_window": [mp.nstr(c, 6) for c in classesF],
        "aitken_F": mp.nstr(extF, 8), "aitken_K": mp.nstr(extK, 8),
        "classesK_window": [mp.nstr(c, 6) for c in classesK],
        "verdict": "NONE of the named candidates (u=1 grid, "
                   "qtilde^(1/2) grid, a.c. log-normal) is Friedrichs "
                   "or Krein: extension spectra are discrete with no "
                   "finite accumulation point (compact resolvent, "
                   "indeterminate case, [simon1998]) and lambda_F > 0, "
                   "while the u-grids accumulate at 0 and the a.c. "
                   "kernel is continuous. The u-continuum members are "
                   "interior (non-extremal) Nevanlinna solutions. NEW "
                   "STRUCTURE: F/K = complementary q-sublattices "
                   "asymptotically aligned with the u = 1 class — the "
                   "extension circle's canonical pair selects the "
                   "u = 1 class (asymptotic-class sense, measured), "
                   "answering the KSel-1 half-step discriminator "
                   "toward u = 1, not qtilde^(1/2).",
    })


# ------------------------------------------------------ F6 circle sweep

def block_f6_sweep(wb: WitnessBuilder, al, be):
    _ok: list[bool] = []
    mp.dps = QD_DPS
    P0 = monic_p_at_zero(al, be, K_DEF)
    N = 44
    tK = +(P0[N] / P0[N - 1])
    mp.dps = EIG_DPS
    alf = [+a for a in al]
    bef = [+b for b in be]
    lam_mins = []
    for snum in (0, 1, 2, 3, 4):
        s = mpf(snum) / 4
        lam, _ = sym_trunc_eig(alf, bef, N,
                               tshift=(s * tK if snum else None))
        lam_mins.append(lam[0])
    _ok.append(bool(all((lam_mins[i + 1] < lam_mins[i] for i in range(4)))))
    assert _ok[-1], lam_mins
    _ok.append(bool(abs(lam_mins[-1]) < mpf('1e-80')))
    assert _ok[-1], lam_mins[-1]
    lam_beyond, _ = sym_trunc_eig(alf, bef, N, tshift=mpf(3) / 2 * tK)
    _ok.append(bool(lam_beyond[0] < 0))
    assert _ok[-1], lam_beyond[0]
    wb.add_assertion(
        "f6_extension_circle_sweep", computed=all(_ok), expected=True,
        tolerance=0,
        source="r = 6/5, N = 44: boundary shifts s*t_N, s in {0, 1/4, "
               "1/2, 3/4, 1} interpolate the truncated extension "
               "family — lambda_min strictly decreasing from the "
               "Friedrichs value to 0 at the Krein pin (s = 1); at "
               "s = 3/2 the smallest eigenvalue is NEGATIVE: "
               "boundary conditions beyond Krein leave the Stieltjes "
               "(nonnegative) sector of the extension circle")
    wb.add_data("f6_sweep", {
        "lambda_min_path": [mp.nstr(x, 10) for x in lam_mins],
        "lambda_min_beyond_krein_s1_5": mp.nstr(lam_beyond[0], 6),
    })


# ------------------------------------------------------- F7 pin legs

def block_f7_pins(wb: WitnessBuilder):
    _ok: list[bool] = []
    out = {}
    for tag, qs in (("muon", Q0_MUON_STR), ("proton", Q0_PROTON_STR)):
        mp.dps = PIN_DPS
        q0 = mpf(qs)
        r = q0 ** mpf("0.25")
        ms = balanced_moments(r, 2 * K_PIN + 2)
        al, be = qd_jacobi(ms, K_PIN)
        _ok.append(bool(all((b > 0 for b in be))))
        assert _ok[-1], (tag, 'beta > 0')
        worst = max(abs(pow00(al, be, n) / ms[n] - 1)
                    for n in range(1, 13))
        _ok.append(bool(worst < mpf('1e-150')))
        assert _ok[-1], (tag, worst)
        P0 = monic_p_at_zero(al, be, K_PIN)
        D = [mpf(1)]
        for b in be:
            D.append(D[-1] * b)
        Ssum = mp.fsum(P0[k] ** 2 / D[k] for k in range(K_PIN))
        mp.dps = 150
        alf = [+a for a in al]
        bef = [+b for b in be]
        lam_mins = []
        for N in (16, 20, 24):
            lam, _ = sym_trunc_eig(alf, bef, N)
            lam_mins.append(lam[0])
        _ok.append(bool(lam_mins[2] < lam_mins[1] < lam_mins[0]))
        assert _ok[-1], (tag, lam_mins)
        _ok.append(bool(lam_mins[2] > 0))
        assert _ok[-1], tag
        tsh = +(P0[K_PIN] / P0[K_PIN - 1])
        lamK, wK = sym_trunc_eig(alf, bef, K_PIN, tshift=tsh)
        _ok.append(bool(abs(lamK[0]) < mpf('1e-40')))
        assert _ok[-1], (tag, lamK[0])
        massid = abs(wK[0] * Ssum - 1)
        _ok.append(bool(massid < mpf('1e-20')))
        assert _ok[-1], (tag, massid)
        out[tag] = {
            "lambda_min_N16_20_24": [mp.nstr(x, 10) for x in lam_mins],
            "krein_first_pos_atoms": [mp.nstr(lamK[i], 8)
                                      for i in (1, 2, 3)],
            "mass_at_zero_N24": mp.nstr(wK[0], 8),
            "repro_worst": mp.nstr(worst, 3),
        }
    wb.add_assertion(
        "f7_pins_machinery", computed=all(_ok), expected=True,
        tolerance=1e-20,
        source="both q0 pins (muon + proton), K = 24: qd beta_k > 0, "
               "moment reproduction < 1e-150, lambda_min(N) strictly "
               "decreasing and positive (N = 16/20/24), Radau pin at 0 "
               "< 1e-40, Radau mass-at-0 identity < 1e-20. The pins "
               "sit deep in the pre-asymptotic window (qtilde - 1 ~ "
               "0.054): asymptotic grid classes are read at the "
               "strong-deformation leg (F5), stated as such — no "
               "class claim is made at the pins")
    wb.add_data("f7_pins", out)


# ------------------------------------------------- F8 bar reflection

def block_f8_bar_reflection(wb: WitnessBuilder, al6, be6, lamF, wF,
                            al_e, be_e, ms_e):
    # (i) sympy exact: sigma fixes LN(-L/2, L); pushforward of LN(mu,s2)
    # under s -> e^{-L}/s is LN(-L - mu, s2); fixed iff mu = -L/2.
    _ok: list[bool] = []
    Ls, mus, s2s, ks = sp.symbols("Ls mus s2s ks", positive=True)
    mom = sp.exp(ks * mus + ks ** 2 * s2s / 2)
    pushed = sp.exp(ks * (-Ls - mus) + ks ** 2 * s2s / 2)
    fixed = sp.simplify(
        (pushed - mom).subs(mus, -Ls / 2))
    _ok.append(bool(fixed == 0))
    assert _ok[-1]
    # class action: phi -> frac(-1 - phi) = frac(-phi); fixed classes on
    # R/Z: -phi = phi (mod 1) <=> 2 phi in Z <=> phi in {0, 1/2} (the
    # u = 1 / u = qtilde^{1/2} pair of ksel1 R4) — exact:
    for ph in (sp.Rational(0), sp.Rational(1, 2)):
        _ok.append(bool(sp.Rational(-ph % 1) == ph))
        assert _ok[-1], ph
    for ph in (sp.Rational(1, 3), sp.Rational(1, 4)):
        _ok.append(bool(sp.Rational(-ph % 1) != ph))
        assert _ok[-1], ph
    # (ii) obstruction: m_{k+1}/m_k -> oo exactly (superexponential):
    # ratio = qtilde^{k - ...}: verify strictly increasing and unbounded
    # on the exact moments at r = 6/5 (Fraction, k <= 24)
    ratios = [ms_e[k + 1] / ms_e[k] for k in range(24)]
    _ok.append(bool(all((ratios[i + 1] > ratios[i] for i in range(23)))))
    assert _ok[-1]
    _ok.append(bool(ratios[-1] > 10 ** 3))
    assert _ok[-1]
    # (iii) numeric: sigma-pushforward of the truncated Friedrichs
    # measure fails moment representation at r = 6/5 ...
    mp.dps = EIG_DPS
    r = mpf(6) / 5
    qt = r ** 2
    msf = balanced_moments(r, 12)
    sig_ratios = []
    for k in (1, 2, 8):
        s = mp.fsum(wF[i] * (1 / (qt * lamF[i])) ** k
                    for i in range(len(lamF)))
        sig_ratios.append(s / msf[k])
    _ok.append(bool(abs(sig_ratios[0] - 1) > mpf('0.2')))
    assert _ok[-1], sig_ratios[0]
    _ok.append(bool(sig_ratios[2] < mpf('0.1')))
    assert _ok[-1], sig_ratios[2]
    # ... and at r = 21/20 (exact-leg Jacobi data, N = 26)
    alf = [mpf(a.numerator) / mpf(a.denominator) for a in al_e]
    bef = [mpf(b.numerator) / mpf(b.denominator) for b in be_e]
    lam26, w26 = sym_trunc_eig(alf, bef, 26)
    r2 = mpf(21) / 20
    qt2 = r2 ** 2
    ms2 = balanced_moments(r2, 6)
    s1 = mp.fsum(w26[i] * (1 / (qt2 * lam26[i])) ** 1
                 for i in range(26))
    ratio_2120 = s1 / ms2[1]
    _ok.append(bool(abs(ratio_2120 - 1) > mpf('1')))
    assert _ok[-1], ratio_2120
    wb.add_assertion(
        "f8_bar_reflection_no_pushforward_action", computed=all(_ok),
        expected=True, tolerance=0,
        source="(i) sympy exact: sigma: s -> qtilde^{-1}/s fixes the "
               "SW factor LN(-L/2, L) and acts on qtilde-grid classes "
               "as phi -> -phi with fixed classes exactly {0, 1/2} = "
               "the u = 1 / u = qtilde^{1/2} pair (ksel1 R4). "
               "(ii) OBSTRUCTION, scope-(b) with cited invariant: "
               "every extension measure has smallest positive support "
               "point s_min > 0 (discrete spectrum, [simon1998]; "
               "lambda_F ~ 0.337 at r = 6/5) or an atom AT 0 (Krein — "
               "sigma-image not a finite measure); sigma_* support is "
               "then bounded by 1/(qtilde s_min), so its moments grow "
               "at most geometrically, while m_{k+1}/m_k is strictly "
               "increasing and unbounded (exact) — sigma_* of an "
               "extension measure is NEVER a representing measure: "
               "the bar reflection does NOT act on the extension "
               "circle by pushforward and does NOT exchange "
               "Friedrichs and Krein. (iii) numeric: sigma-moment/m_k "
               f"= {mp.nstr(sig_ratios[0], 6)} (k=1), "
               f"{mp.nstr(sig_ratios[2], 3)} (k=8) at r = 6/5; "
               f"{mp.nstr(ratio_2120, 6)} (k=1) at r = 21/20")
    wb.add_data("f8_bar_reflection", {
        "sw_factor_fixed": "LN(-L/2, L) is sigma-invariant (exact)",
        "fixed_classes": "{0, 1/2} mod qtilde^Z = u = 1 and "
                         "u = qtilde^(1/2) — on the u-CIRCLE (non-"
                         "canonical solutions), not on the extension "
                         "circle",
        "sigma_moment_ratios_r6_5": [mp.nstr(x, 8) for x in sig_ratios],
        "sigma_moment_ratio_r21_20_k1": mp.nstr(ratio_2120, 8),
        "verdict": "the closing question's premise ('if the bar "
                   "reflection exchanges Friedrichs and Krein...') "
                   "FAILS in the pushforward reading — scope-(b) via "
                   "the bounded-support / superexponential-moment "
                   "invariant; a NON-pushforward action on the "
                   "Nevanlinna parameter remains open (scope-(a), "
                   "not constructed here)",
    })


# ------------------------------------------------------------------ main

def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("ksel2id-friedrichs-selection",
                        engine="sympy+mpmath+fractions")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "KSel-2-ID (bean qou-0ms0; audit-only, NO FIT, nothing wired): "
        "Friedrichs/Krein identification for the balanced binding "
        "Jacobi operator J(q), by exact-Q + certified-mpf qd Jacobi "
        "data, truncation eigenvalues (min-max => Friedrichs limit), "
        "and Gauss-Radau-at-0 (=> Krein, the canonical solution with 0 "
        "in support, [pedersen1995]). Findings: lambda_F > 0 (strict); "
        "Krein has an atom at 0 with mass 1/sum p_k(0)^2; the extremal "
        "supports are asymptotically q-lattices (spacing qtilde-steps "
        "-> 2), F and K occupying complementary q-sublattices whose "
        "common qtilde-class Aitken-extrapolates to the u = 1 class "
        "(u-half-step discriminator answered toward u = 1); NONE of "
        "the three named kernel candidates (u = 1 grid, qtilde^(1/2) "
        "grid, a.c. log-normal) is an extension measure — the "
        "u-continuum members are interior Nevanlinna solutions "
        "(supports accumulate at 0; extension spectra are discrete "
        "with compact resolvent, [simon1998]). Bar reflection: sigma "
        "fixes the SW factor and the u-classes {1, qtilde^(1/2)} but "
        "does NOT act on the extension circle by pushforward "
        "(bounded-support vs superexponential-moment obstruction, "
        "scope-(b)); it does NOT exchange Friedrichs and Krein. "
        "Extension-circle sweep: boundary conditions interpolate "
        "F -> K monotonically; beyond Krein the truncation leaves the "
        "nonnegative sector. Pin legs verify positivity + machinery; "
        "grid classes are read at the strong-deformation point, "
        "stated as such. Nothing here proves or refutes any "
        "conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md")

    al_e, be_e, ms_e26 = block_f1_exact(wb)
    print("F1: exact-Q qd r=21/20 K=26 — Favard depth 25, beta_1 exact, "
          "reproduction exact.")
    al6, be6, ms6 = block_f2_deformation_qd(wb)
    print("F2: mpf qd r=6/5 K=48 certified (< 1e-300) + exact "
          "cross-check.")
    lamF, wF = block_f3_friedrichs(wb, al6, be6)
    print("F3: Friedrichs limit — monotone min-max, lambda_F in "
          "(0.33, 0.34) > 0.")
    lamK, wK = block_f4_krein(wb, al6, be6, lamF)
    print("F4: Krein via Radau-at-0 — pin < 1e-80, mass-at-0 identity, "
          "interlacing.")
    ms_e = balanced_moments(Fr(6, 5), 26)
    block_f5_grid(wb, lamF, wF, lamK)
    print("F5: grids — spacing -> 2 qtilde-steps (q-lattice), F/K "
          "classes -> u=1 class; named candidates excluded.")
    block_f6_sweep(wb, al6, be6)
    print("F6: extension-circle sweep — monotone F -> K, negative "
          "beyond Krein.")
    block_f7_pins(wb)
    print("F7: pins — positivity, monotone lambda_min > 0, Radau "
          "machinery verified.")
    block_f8_bar_reflection(wb, al6, be6, lamF, wF, al_e, be_e, ms_e)
    print("F8: bar reflection — fixes SW factor + u-classes {0, 1/2}; "
          "NO pushforward action on the extension circle; F<->K "
          "exchange refuted (pushforward sense).")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon); "
                  "qou_substrate.constants.Q_50_DIGIT_STR (proton)"})
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
