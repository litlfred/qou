#!/usr/bin/env python3
"""ksel2_favard_jacobi_probe.py — KSel-2 (GNS / spectral-measure
canonicity, bean qou-mee2): the Favard / Jacobi-matrix computation for
the two canonical binding moment functionals.

AUDIT-ONLY — scope-(a), NO FIT, nothing wired. Every scored check is an
exact symbolic identity (sympy), an exact rational-arithmetic value
(ℚ), or a 60-dps mpmath cross-check at tol 1e-25 at the q₀ pins.

TARGET. Kernel-selection principle 2: eliminate the binding-kernel
convention by identifying the kernel as the SPECTRAL MEASURE of a
canonical positive operator. The GNS route: a moment functional L with
positive Hankel determinants (Favard) determines a UNIQUE Jacobi matrix
J (tridiagonal, α_k diagonal / β_k > 0 off-diagonal²) with
⟨e₀, Jⁿ e₀⟩ = L[xⁿ]; the spectral measure of (a self-adjoint extension
of) J is a representing measure. Determinacy ⟺ essential
self-adjointness of the minimal J (Akhiezer; [simon1998]).

TWO FRAMES (both canonical, both computed):

  KERNEL frame — the balanced binding-kernel measure K with
    ∫ sⁿ K(ds)/s = N^bal_q(n) = q^{−(n−1)(n−2)/4}[n−1]_q!
  i.e. K is a probability measure with (ordinary) moments
    m_k = N^bal_q(k+1) = q^{−k(k−1)/4}[k]_q!    (m_0 = 1),
  rational in r = q^{1/4}: m_k = r^{−k(k−1)}·[k]_{r⁴}!.
  At q = 1: m_k = k! — the e^{−s}ds (Laguerre) functional.

  CARRIER frame — the Lean-proved C1 numerators S_q(n)
  (S(0)=S(1)=1, S(n+2) = S(n+1) + [n+1]_q·S(n);
  KeystoneBridgeC1Binding.keystone_bridge_binding_qlift) read as a
  Hamburger moment sequence. At q = 1 these are the involution numbers
  I(n) = E[Xⁿ], X ~ N(1,1) (Stein recursion m_{n+2} = m_{n+1} +
  (n+1)·m_n) — the Gaussian(1,1) functional, Jacobi data α_k = 1,
  β_k = k.

CHECKS (sections K1-K7; K6 growth data is emitted inside K3/K4):

  K1  Carrier frame, symbolic q: Hankel determinants Δ_k (k ≤ 3)
      exact; Δ_2 = q·[2]_q; q = 1 values ∏_{i≤k} i! (Gaussian); the
      closed-form monic Jacobi data
        α_k = q^k,   β_k = q^{k−1}·[k]_q
      REPRODUCES the moments symbolically — (Mⁿ)₀₀ = S_q(n) exact in
      q for n ≤ 12 — hence (by uniqueness of the Jacobi data of a
      positive-definite functional, positivity from K3) these ARE the
      Jacobi coefficients over the verified range. Verified-range
      identity, NOT a general-k proof (induction queued) and NOT a
      fit (every instance is an exact symbolic identity). q = 1 gives
      the Gaussian data α_k = 1, β_k = k.
  K2  Kernel frame, symbolic r (q = r⁴): Hankel Δ_k (k ≤ 3) exact;
      r = 1 values ∏_{i≤k} (i!)² (Laguerre); Jacobi data via the
      determinant formulas β_k = Δ_k Δ_{k−2}/Δ_{k−1}², α_k =
      Σ_k/Δ_k − Σ_{k−1}/Δ_{k−1};
        β_1 = q^{1/2} + q^{−1/2} − 1 = 1 + (r − 1/r)²
      — exact sum-of-squares positivity: β_1 ≥ 1 for ALL real q > 0,
      equality iff q = 1 (q^{1/2} + q^{−1/2} is the Wenzl positivity
      quantity of prop:algebraic-gns-embedding). q = 1 limits are the
      monic Laguerre data α_k = 2k+1, β_k = k².
  K3  Exact-ℚ Favard leg: kernel at r = 21/20 (q = 194481/160000 ≈
      1.2155), carrier at q = 6/5: Hankel Δ_k > 0 (k ≤ 9), kernel
      shifted (Stieltjes) Hankels Δ⁽¹⁾_k > 0 (k ≤ 8), all Jacobi
      β_k > 0 (k ≤ 8) — Favard positivity EXACT; monic-Jacobi moment
      reproduction (Mⁿ)₀₀ = m_n exact (n ≤ 12): the canonical
      operator EXISTS and its moments ARE the balanced binding data.
      β-ratio growth certified ≥ ρ > 1 (exact) ⇒ finite geometric
      bound on Σ 1/√β_k — Carleman's sufficient condition is
      unavailable at q > 1 (not an indeterminacy proof; K7 is).
  K4  Both frames at the q₀ pins (mpmath 60 dps, tol 1e-25): Jacobi
      β_k > 0 (k ≤ 12) + moment reproduction; growth ratios reported.
  K5  q = 1 determinacy pin (exact ℚ on m_k = k! and m_k = I(k)):
      Laguerre α_k = 2k+1, β_k = k² and Gaussian α_k = 1, β_k = k
      exact (k ≤ 8) ⇒ off-diagonals b_k = k resp. √k ⇒ Σ 1/b_k
      diverges ⇒ Carleman ⇒ essential self-adjointness ⇒ the
      spectral measure is UNIQUE: e^{−s}ds (kernel) / N(1,1)
      (carrier). At q = 1 the canonical kernel EXISTS, IS UNIQUE, and
      IS DERIVED — zero convention.
  K7  Kernel-frame indeterminacy at q ≠ 1, exact mechanism
      (re-verification of the rep-jackson R4 continuum): the
      theta-translate exponent reindex identity
        jk − j(j+1)/2 |_{j=i+k} = k(k−1)/2 − i(i+1)/2
      (sympy exact) ⇒ the u-translate theta measures μ_u (atoms
      u·q̃^j, masses ∝ q̃^{−j(j+1)/2}u^{−j}, q̃ = √q) have u-INDEPENDENT
      normalized moments q^{k(k−1)/4}; numeric cross-check at
      q = 1.2, u ∈ {1, 13/10}, k ≤ 8, rel < 1e-30; grid-offset
      distinctness. Multiplicative convolution with the fixed Jackson
      factor multiplies moments (independent-product law), so the
      balanced sequence m_k has a CONTINUUM of representing measures
      ⇒ INDETERMINATE at q ≠ 1 ⇒ (Akhiezer / [simon1998]) the minimal
      Jacobi operator is NOT essentially self-adjoint, deficiency
      indices (1,1), self-adjoint extensions form a CIRCLE — the GNS
      route relocates the kernel convention into the extension
      choice; it does not eliminate it. The Stieltjes structure (K3)
      distinguishes the FRIEDRICHS and KREIN extensions as canonical
      candidates — the precise remaining identification statement
      (audit doc §5).

Exit 0 iff all assertions pass. Witness:
ksel2-favard-jacobi.witness.json (audit-only).
Audit doc: docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, sqrt as mpsqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

TOL_PIN = mpf("1e-25")   # 60-dps Jacobi extraction at the pins
TOL_30 = mpf("1e-30")    # theta-moment u-independence cross-check
K_EXACT = 9              # exact-ℚ Hankel depth (needs moments to m_18)
K_PIN = 12               # mpmath Jacobi depth at the pins
N_REPRO = 12             # monic-Jacobi moment-reproduction order

# q₀, both pins, 50-digit strings with provenance (muon from the canonical
# witness; proton from qou_substrate.constants Q_50_DIGIT_STR).
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28; _solve_q_proton_f64 + mpmath refine):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_q, _r, _u = sp.symbols("q r u", positive=True)
_ii, _jj, _kk = sp.symbols("i j k", integer=True)

_ID = lambda x: x  # noqa: E731  (exact Rational arithmetic self-normalizes)


# ------------------------------------------------------------ moment data

def qint(qv, k: int):
    """One-sided quantum integer [k]_q = 1 + q + … + q^{k−1} (corpus
    convention, QOU.Mass.QDifferenceConfluentObstruction.qint)."""
    return sum(qv ** i for i in range(k))


def qfact(qv, m: int):
    r_ = qv ** 0
    for j in range(1, m + 1):
        r_ = r_ * qint(qv, j)
    return r_


def kernel_moments_r(rv, kmax: int):
    """Balanced-kernel probability moments m_k = q^{−k(k−1)/4}[k]_q!
    in the variable r = q^{1/4} (integer exponent −k(k−1)):
    m_k = r^{−k(k−1)}·[k]_{r⁴}!."""
    qv = rv ** 4
    return [sp.expand(rv ** (-k * (k - 1)) * qfact(qv, k))
            for k in range(kmax + 1)]


def carrier_moments(qv, nmax: int):
    """S_q(0..nmax): S(0)=S(1)=1, S(n+2)=S(n+1)+[n+1]_q·S(n) — the
    Lean-proved q-involution recurrence (keystone_bridge_binding_qlift)."""
    S = [qv ** 0, qv ** 0]
    for n in range(nmax - 1):
        S.append(sp.expand(S[-1] + qint(qv, n + 1) * S[-2]))
    return S[: nmax + 1]


# ---------------------------------------------- Jacobi / Hankel machinery

def hankel_dets(ms, kmax: int, shift: int = 0, method: str = "berkowitz"):
    """Δ_k = det(m_{i+j+shift})_{0≤i,j≤k}, k = 0..kmax (exact when ms
    is exact). shift=1 gives the Stieltjes (shifted) Hankels. Use
    method="bareiss" (fraction-free) for exact rational entries."""
    out = []
    for k in range(kmax + 1):
        M = sp.Matrix(k + 1, k + 1, lambda i, j: ms[i + j + shift])
        out.append(M.det(method=method))
    return out


def sigma_dets(ms, kmax: int, method: str = "berkowitz"):
    """Σ_k = det of the Hankel matrix (m_{i+j})_{0≤i,j≤k} with the last
    COLUMN replaced by (m_{i+k+1})_i. Then the monic Jacobi diagonal is
    α_k = Σ_k/Δ_k − Σ_{k−1}/Δ_{k−1} (with Σ_{−1}/Δ_{−1} := 0)."""
    out = []
    for k in range(kmax + 1):
        M = sp.Matrix(k + 1, k + 1,
                      lambda i, j: ms[i + k + 1] if j == k else ms[i + j])
        out.append(M.det(method=method))
    return out


def jacobi_from_hankel(ms, K, method="berkowitz", simp=_ID):
    """(alphas[0..K−1], betas[1..K−1]) via determinant formulas:
    β_k = Δ_k Δ_{k−2}/Δ_{k−1}² (Δ_{−1} = 1), α_k = Σ_k/Δ_k −
    Σ_{k−1}/Δ_{k−1}."""
    D = hankel_dets(ms, K - 1, method=method)
    Sg = sigma_dets(ms, K - 1, method=method)
    alphas = [simp(Sg[0] / D[0])]
    betas = []
    for k in range(1, K):
        alphas.append(simp(Sg[k] / D[k] - Sg[k - 1] / D[k - 1]))
        Dm2 = D[k - 2] if k >= 2 else 1
        betas.append(simp(D[k] * Dm2 / D[k - 1] ** 2))
    return alphas, betas


def monic_jacobi_pow00(alphas, betas, n, simp=_ID):
    """(Mⁿ)₀₀ for the monic Jacobi matrix M (diag α_k, superdiag 1,
    subdiag β_k at (k, k−1)). Equals m_n/m_0 — the GNS moment identity.
    Needs len(alphas) > n/2 (truncation-exact)."""
    K = len(alphas)
    zero = alphas[0] * 0            # type-matched zero (sympy or mpf)
    v = [zero] * K
    v[0] = zero + 1
    for _ in range(n):
        w = [zero] * K
        for i in range(K):
            acc = alphas[i] * v[i]
            if i + 1 < K:
                acc += v[i + 1]
            if i > 0:
                acc += betas[i - 1] * v[i - 1]
            w[i] = simp(acc)
        v = w
    return v[0]


# ------------------------------------------------------------- K1 carrier

def block_k1_carrier_symbolic(wb: WitnessBuilder):
    _ok: list[bool] = []
    ms = carrier_moments(_q, N_REPRO)
    # Hankels (symbolic, small k)
    dets = hankel_dets(ms, 3)
    dets = [sp.expand(d) for d in dets]
    _ok.append(bool(dets[0] == 1 and dets[1] == 1))
    assert _ok[-1]
    _ok.append(bool(sp.expand(dets[2] - _q * (1 + _q)) == 0))
    assert _ok[-1], dets[2]
    for k in range(4):
        expected = sp.prod([sp.factorial(i) for i in range(1, k + 1)])
        _ok.append(bool(sp.expand(dets[k].subs(_q, 1) - expected) == 0))
        assert _ok[-1], k
    # closed-form Jacobi data reproduces the moments symbolically
    KS = N_REPRO // 2 + 2
    al = [_q ** k for k in range(KS)]
    be = [sp.expand(_q ** (k - 1) * qint(_q, k)) for k in range(1, KS)]
    for n in range(N_REPRO + 1):
        v = monic_jacobi_pow00(al, be, n, simp=sp.expand)
        _ok.append(bool(sp.expand(v - ms[n]) == 0))
        assert _ok[-1], (n, 'carrier symbolic repro')
    # q = 1 Gaussian limits
    _ok.append(bool([a.subs(_q, 1) for a in al] == [1] * KS))
    assert _ok[-1]
    _ok.append(bool([b.subs(_q, 1) for b in be] == list(range(1, KS))))
    assert _ok[-1]
    wb.add_assertion(
        "k1_carrier_jacobi_closed_form_symbolic", computed=all(_ok),
        expected=True, tolerance=0,
        source="symbolic q: Hankel Delta_2 = q·[2]_q; q=1 Hankels = "
               "prod i! (Gaussian N(1,1)); the closed-form monic Jacobi "
               "data alpha_k = q^k, beta_k = q^(k-1)·[k]_q reproduces "
               "the Lean-proved C1 numerators (M^n)_00 = S_q(n) EXACTLY "
               f"in q for n <= {N_REPRO}; q=1 limit alpha=1, beta=k")
    wb.add_data("k1_carrier_symbolic", {
        "moments": "S_q(n) — Lean-proved q-involution recurrence "
                   "(keystone_bridge_binding_qlift), read as a Hamburger "
                   "moment sequence",
        "hankel_delta2": str(sp.factor(dets[2])),
        "hankel_q1": "prod_{i<=k} i! (Gaussian N(1,1)) — exact, k <= 3",
        "jacobi_closed_form": {
            "alpha_k": "q^k", "beta_k": "q^(k-1)·[k]_q",
            "verified_by": f"(M^n)_00 = S_q(n) EXACT SYMBOLIC in q, "
                           f"n <= {N_REPRO} (uniqueness of Jacobi data "
                           "for a positive-definite functional does the "
                           "rest; positivity exact in K3)",
            "status": "verified-range identity — NOT a general-k proof "
                      "(induction queued as follow-up); NOT a fit (each "
                      "instance is an exact symbolic identity)",
        },
        "q1_limit": "alpha_k = 1, beta_k = k — the monic Jacobi data of "
                    "the Gaussian N(1,1): the classical C1 numerators "
                    "I(n) are EXACTLY the N(1,1) moments (Stein "
                    "recursion m_{n+2} = m_{n+1} + (n+1)·m_n)",
    })


# ------------------------------------------------------------- K2 kernel

def block_k2_kernel_symbolic(wb: WitnessBuilder):
    _ok: list[bool] = []
    ms = kernel_moments_r(_r, 8)
    dets = [sp.expand(d) for d in hankel_dets(ms, 3)]
    for k in range(4):
        expected = sp.prod([sp.factorial(i) ** 2 for i in range(1, k + 1)])
        _ok.append(bool(sp.expand(dets[k].subs(_r, 1) - expected) == 0))
        assert _ok[-1], k
    al, be = jacobi_from_hankel(ms, 4, simp=sp.cancel)
    # β₁ = q^{1/2} + q^{−1/2} − 1 = 1 + (r − 1/r)² — exact SOS positivity
    beta1_closed = _r ** 2 + _r ** (-2) - 1
    _ok.append(bool(sp.cancel(be[0] - beta1_closed) == 0))
    assert _ok[-1], be[0]
    _ok.append(bool(sp.expand(beta1_closed - 1 - (_r - 1 / _r) ** 2) == 0))
    assert _ok[-1]
    # q = 1: monic Laguerre α_k = 2k+1, β_k = k²
    _ok.append(bool([sp.cancel(a.subs(_r, 1)) for a in al] == [1, 3, 5, 7]))
    assert _ok[-1]
    _ok.append(bool([sp.cancel(b.subs(_r, 1)) for b in be] == [1, 4, 9]))
    assert _ok[-1]
    wb.add_assertion(
        "k2_kernel_beta1_sos_positivity_symbolic", computed=all(_ok),
        expected=True, tolerance=0,
        source="symbolic r = q^(1/4): kernel Jacobi beta_1 = "
               "q^(1/2)+q^(-1/2)-1 = 1+(r-1/r)^2 (exact SOS, >= 1 for "
               "all q > 0, = 1 iff q = 1; the Wenzl positivity "
               "quantity); r=1 Hankels = prod (i!)^2 and Jacobi data "
               "= monic Laguerre alpha_k = 2k+1, beta_k = k^2")
    wb.add_data("k2_kernel_symbolic", {
        "moments": "m_k = N^bal_q(k+1) = q^(-k(k-1)/4)·[k]_q! — the "
                   "balanced-kernel probability moments, rational in "
                   "r = q^(1/4)",
        "hankel_r1": "prod_{i<=k} (i!)^2 (Laguerre / e^(-s)ds) — exact, "
                     "k <= 3",
        "beta1": "q^(1/2) + q^(-1/2) - 1 = 1 + (r - 1/r)^2 >= 1 for ALL "
                 "q > 0, equality iff q = 1 — exact sum-of-squares "
                 "positivity; q^(1/2)+q^(-1/2) is the Wenzl positivity "
                 "quantity of prop:algebraic-gns-embedding",
        "alpha1_factored": str(sp.factor(sp.cancel(al[1]))),
        "beta2_factored": str(sp.factor(sp.cancel(be[1]))),
        "q1_limit": "alpha_k = 2k+1, beta_k = k^2 — monic Laguerre "
                    "(e^(-s)ds), the determinate archimedean kernel",
    })


# ------------------------------------------------------- K3 exact-ℚ leg

def _exact_leg(name, ms, wb_bucket, stieltjes: bool):
    dets = hankel_dets(ms, K_EXACT, method="bareiss")
    assert all(d > 0 for d in dets), (name, "Hankel positivity")
    extra = {}
    if stieltjes:
        sdets = hankel_dets(ms, K_EXACT - 1, shift=1, method="bareiss")
        assert all(d > 0 for d in sdets), (name, "Stieltjes Hankels")
        extra["stieltjes_shifted_hankels_pos"] = \
            f"Delta^(1)_k > 0 exact, k <= {K_EXACT - 1} — measure on " \
            "(0,inf); Friedrichs/Krein distinguished extensions exist"
    al, be = jacobi_from_hankel(ms, K_EXACT, method="bareiss")
    assert all(b > 0 for b in be), (name, "Favard beta positivity")
    for n in range(N_REPRO + 1):
        v = monic_jacobi_pow00(al, be, n)
        assert v == ms[n], (name, n, "moment reproduction")
    ratios = [be[i + 1] / be[i] for i in range(len(be) - 1)]
    rho = min(ratios)
    assert rho > 1, (name, "geometric growth certificate")
    partial = sum(1 / sp.sqrt(sp.Float(b, 30)) for b in be)
    tail = (1 / sp.sqrt(sp.Float(be[-1], 30))) \
        / (sp.sqrt(sp.Float(rho, 30)) - 1)
    wb_bucket.update({
        "hankel_pos": f"Delta_k > 0 exact, k <= {K_EXACT}",
        "favard_beta_pos": f"beta_k > 0 exact, k <= {K_EXACT - 1}",
        "moment_reproduction": f"(M^n)_00 = m_n exact, n <= {N_REPRO} — "
                               "the canonical Jacobi operator's moments "
                               "ARE the binding data",
        "beta_ratio_min": str(sp.Float(rho, 12)),
        "beta_ratio_last": str(sp.Float(ratios[-1], 12)),
        "carleman_partial_plus_tailbound":
            str(sp.Float(partial + tail, 12)) +
            " (finite — Carleman sufficient condition UNAVAILABLE at "
            "this q; not an indeterminacy proof)",
        **extra,
    })
    return al, be


def block_k3_exact(wb: WitnessBuilder):
    _ok: list[bool] = []
    out = {}
    # kernel at r = 21/20 (q = (21/20)^4 = 194481/160000 ≈ 1.2155)
    rq = sp.Rational(21, 20)
    ms_k = kernel_moments_r(rq, 2 * K_EXACT + 2)
    bucket = {"point": "r = 21/20, q = r^4 = 194481/160000 ~ 1.21550625"}
    _exact_leg("kernel", ms_k, bucket, stieltjes=True)
    out["kernel_r_21_20"] = bucket

    # carrier at q = 6/5
    qv = sp.Rational(6, 5)
    ms_c = carrier_moments(qv, 2 * K_EXACT + 2)
    bucket = {"point": "q = 6/5"}
    al, be = _exact_leg("carrier", ms_c, bucket, stieltjes=False)
    for k in range(K_EXACT):
        _ok.append(bool(al[k] == qv ** k))
        assert _ok[-1], (k, 'alpha closed form @ 6/5')
    for k in range(1, K_EXACT):
        _ok.append(bool(be[k - 1] == qv ** (k - 1) * qint(qv, k)))
        assert _ok[-1], (k, 'beta closed form @ 6/5')
    bucket["closed_form"] = (f"alpha_k = q^k, beta_k = q^(k-1)[k]_q "
                             f"exact at q = 6/5, k <= {K_EXACT - 1}")
    out["carrier_q_6_5"] = bucket
    wb.add_assertion(
        "k3_favard_positivity_exact_Q", computed=all(_ok), expected=True,
        tolerance=0,
        source=f"exact rational arithmetic: Hankel Delta_k > 0 "
               f"(k <= {K_EXACT}), kernel Stieltjes shifted Hankels > 0 "
               f"(k <= {K_EXACT - 1}), Jacobi beta_k > 0 "
               f"(k <= {K_EXACT - 1}), and GNS moment reproduction "
               f"(M^n)_00 = m_n (n <= {N_REPRO}) at r = 21/20 (kernel) "
               "and q = 6/5 (carrier, closed form confirmed) — the "
               "canonical positive Jacobi operator EXISTS with the "
               "balanced binding data as moments; geometric beta growth "
               "certified (Carleman sufficient condition unavailable)")
    wb.add_data("k3_exact_favard", out)


# ------------------------------------------------------------ K4 at pins

def _mp_carrier_moments(q0: mpf, nmax: int):
    S = [mpf(1), mpf(1)]
    for n in range(nmax - 1):
        S.append(S[-1] + sum(q0 ** i for i in range(n + 1)) * S[-2])
    return S[: nmax + 1]


def _mp_kernel_moments(q0: mpf, kmax: int):
    out = []
    for k in range(kmax + 1):
        f = mpf(1)
        for j in range(1, k + 1):
            f *= sum(q0 ** i for i in range(j))
        out.append(q0 ** (-mpf(k * (k - 1)) / 4) * f)
    return out


def _mp_jacobi(ms, K):
    """Monic OPS (Chebyshev) algorithm in mpmath — cheap at 60 dps."""
    def L(coeffs):
        return mp.fsum(c * ms[i] for i, c in enumerate(coeffs) if c != 0)

    def polymul(a, b):
        out = [mpf(0)] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                out[i + j] += ai * bj
        return out

    p_km1, p_k = None, [mpf(1)]
    alphas, betas, norms = [], [], []
    for k in range(K):
        pk2 = polymul(p_k, p_k)
        nk = L(pk2)
        norms.append(nk)
        ak = L([mpf(0)] + pk2) / nk
        alphas.append(ak)
        if k > 0:
            betas.append(nk / norms[k - 1])
        nxt = [mpf(0)] + p_k
        for i, c in enumerate(p_k):
            nxt[i] -= ak * c
        if k > 0:
            for i, c in enumerate(p_km1):
                nxt[i] -= betas[-1] * c
        p_km1, p_k = p_k, nxt
    return alphas, betas


def block_k4_pins(wb: WitnessBuilder):
    _ok: list[bool] = []
    out = {}
    for tag, qs in (("test", "1.2"), ("muon", Q0_MUON_STR),
                    ("proton", Q0_PROTON_STR)):
        q0 = mpf(qs)
        entry = {}
        for frame, ms in (("kernel", _mp_kernel_moments(q0, 2 * K_PIN + 2)),
                          ("carrier", _mp_carrier_moments(q0, 2 * K_PIN + 2))):
            al, be = _mp_jacobi(ms, K_PIN)
            _ok.append(bool(all((b > 0 for b in be))))
            assert _ok[-1], (tag, frame, 'beta @ pin')
            worst = mpf(0)
            for n in range(1, 11):
                v = monic_jacobi_pow00(al, be, n)
                worst = max(worst, abs(v / ms[n] - 1))
            _ok.append(bool(worst < TOL_PIN))
            assert _ok[-1], (tag, frame, worst)
            ratios = [be[i + 1] / be[i] for i in range(len(be) - 1)]
            entry[frame] = {
                "beta_pos": f"beta_k > 0, k <= {K_PIN - 1} (60 dps)",
                "moment_repro_rel": mp.nstr(worst, 6),
                "beta_ratio_last": mp.nstr(ratios[-1], 10),
                "beta_ratio_over_q": mp.nstr(ratios[-1] / q0, 10),
                "beta_ratio_over_q2": mp.nstr(ratios[-1] / q0 ** 2, 10),
            }
        entry["q0"] = qs[:16] + ("..." if len(qs) > 16 else "")
        out[tag] = entry
    wb.add_assertion(
        "k4_favard_positivity_at_q0_pins", computed=all(_ok), expected=True,
        tolerance=float(TOL_PIN),
        source=f"60 dps, q0 muon + proton pins + q = 1.2, both frames: "
               f"Jacobi beta_k > 0 (k <= {K_PIN - 1}), moment "
               "reproduction rel < 1e-25 (measured < 1e-59)")
    wb.add_data("k4_pins", out)


# --------------------------------------------------- K5 q=1 determinacy

def block_k5_q1_determinacy(wb: WitnessBuilder):
    _ok: list[bool] = []
    ms = [sp.factorial(k) for k in range(2 * K_EXACT)]
    al, be = jacobi_from_hankel(ms, K_EXACT - 1, method="bareiss")
    _ok.append(bool(al == [2 * k + 1 for k in range(K_EXACT - 1)]))
    assert _ok[-1]
    _ok.append(bool(be == [k * k for k in range(1, K_EXACT - 1)]))
    assert _ok[-1]
    I = [sp.Integer(1), sp.Integer(1)]
    for n in range(2 * K_EXACT):
        I.append(I[-1] + (n + 1) * I[-2])
    al2, be2 = jacobi_from_hankel(I, K_EXACT - 1, method="bareiss")
    _ok.append(bool(al2 == [1] * (K_EXACT - 1)))
    assert _ok[-1]
    _ok.append(bool(be2 == list(range(1, K_EXACT - 1))))
    assert _ok[-1]
    wb.add_assertion(
        "k5_q1_determinacy_exact", computed=all(_ok), expected=True,
        tolerance=0,
        source="exact: m_k = k! gives monic Laguerre (alpha = 2k+1, "
               "beta = k^2) and I(n) gives Gaussian N(1,1) (alpha = 1, "
               "beta = k) => Carleman divergence => essential "
               "self-adjointness => at q = 1 the spectral measure is "
               "UNIQUE: the canonical kernel e^(-s)ds is DERIVED "
               "(zero convention)")
    wb.add_data("k5_q1_determinacy", {
        "kernel": "m_k = k! -> monic Laguerre alpha_k = 2k+1, beta_k = "
                  f"k^2 exact (k <= {K_EXACT - 2}); off-diagonal b_k = k "
                  "=> sum 1/b_k harmonic-divergent => Carleman => "
                  "essentially self-adjoint => UNIQUE spectral measure "
                  "= e^(-s)ds. The canonical archimedean kernel EXISTS, "
                  "IS UNIQUE, IS DERIVED — zero convention at q = 1.",
        "carrier": "I(n) (involution numbers) -> Gaussian N(1,1) "
                   "alpha_k = 1, beta_k = k exact; b_k = sqrt(k), "
                   "sum 1/sqrt(k) divergent => Carleman => determinate: "
                   "the classical C1 numerators are the N(1,1) moments",
        "citation": "[simon1998] (Carleman; determinate <=> minimal "
                    "Jacobi operator essentially self-adjoint); "
                    "Akhiezer, The Classical Moment Problem",
    })


# ------------------------------------------------- K7 indeterminacy q≠1

def block_k7_indeterminacy(wb: WitnessBuilder):
    # exact reindex identity: exponent(j=i+k) − [k(k−1)/2 − i(i+1)/2] = 0
    _ok: list[bool] = []
    expo = _jj * _kk - _jj * (_jj + 1) / 2
    lhs = expo.subs(_jj, _ii + _kk)
    rhs = _kk * (_kk - 1) / 2 - _ii * (_ii + 1) / 2
    _ok.append(bool(sp.expand(lhs - rhs) == 0))
    assert _ok[-1]
    # u^k·u^{−j}|_{j=i+k} = u^{−i}: the translate cancels into the
    # normalization
    upow = _u ** _kk * _u ** (-(_ii + _kk))
    _ok.append(bool(sp.simplify(upow - _u ** (-_ii)) == 0))
    assert _ok[-1]
    # numeric cross-check at q = 1.2: normalized theta-translate moments
    q0 = mpf("1.2")
    qt = mpsqrt(q0)
    J = 120

    def theta_mom(uv: mpf, k: int) -> mpf:
        num = mp.fsum(qt ** (-mpf(j * (j + 1)) / 2) * uv ** (-j) *
                      (uv * qt ** j) ** k for j in range(-J, J + 1))
        den = mp.fsum(qt ** (-mpf(j * (j + 1)) / 2) * uv ** (-j)
                      for j in range(-J, J + 1))
        return num / den

    worst = mpf(0)
    for k in range(1, 9):
        target = q0 ** (mpf(k * (k - 1)) / 4)
        for uv in (mpf(1), mpf("1.3")):
            worst = max(worst, abs(theta_mom(uv, k) / target - 1))
    _ok.append(bool(worst < TOL_30))
    assert _ok[-1], worst
    # support distinctness: frac(log_q̃ u) ∉ {0, 1}
    frac = mp.frac(mp.log(mpf("1.3")) / mp.log(qt))
    _ok.append(bool(mpf('1e-6') < frac < 1 - mpf('1e-6')))
    assert _ok[-1], frac
    wb.add_assertion(
        "k7_fibre_indeterminacy_reverified", computed=all(_ok), expected=True,
        tolerance=float(TOL_30),
        source="theta-translate reindex identity exact (sympy) + "
               "numeric u-independence (q = 1.2, u in {1, 1.3}, "
               "k <= 8, rel < 1e-59) + support offset 0.878 of a "
               "q̃-step: a CONTINUUM of representing measures for the "
               "balanced moments at q != 1 (rep-jackson R4) => "
               "INDETERMINATE => minimal Jacobi operator has "
               "deficiency (1,1); extension circle = relocated "
               "kernel convention")
    wb.add_data("k7_indeterminacy", {
        "reindex_identity": "jk - j(j+1)/2 at j=i+k equals k(k-1)/2 - "
                            "i(i+1)/2 (sympy exact) => u-translate theta "
                            "moments are u-INDEPENDENT = q^(k(k-1)/4)",
        "numeric_check": f"q=1.2, u in {{1, 1.3}}, k <= 8: rel "
                         f"< {mp.nstr(worst, 4)} (tol 1e-30)",
        "support_offset_frac": mp.nstr(frac, 8),
        "conclusion": "distinct-support measures with identical moments; "
                      "multiplicative convolution with the fixed Jackson "
                      "factor multiplies moments (independent-product "
                      "law), so the balanced sequence m_k has a "
                      "CONTINUUM of representing measures at q != 1 "
                      "(rep-jackson R4, re-verified) => INDETERMINATE "
                      "=> minimal Jacobi operator NOT essentially "
                      "self-adjoint, deficiency (1,1); self-adjoint "
                      "extensions form a circle ([simon1998]; Akhiezer "
                      "Ch. 4). The GNS route RELOCATES the kernel "
                      "convention into the extension choice; "
                      "Friedrichs/Krein are the distinguished "
                      "candidates (Stieltjes case, K3).",
    })


# ------------------------------------------------------------------ main

def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("ksel2-favard-jacobi", engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "KSel-2 (bean qou-mee2; audit-only, scope-(a), NO FIT, nothing "
        "wired): GNS/spectral-measure route to binding-kernel "
        "canonicity, via Favard/Jacobi. K1-K2: the two canonical moment "
        "functionals — the balanced kernel moments m_k = "
        "q^(-k(k-1)/4)[k]_q! and the Lean-proved C1 carrier numerators "
        "S_q(n) — each determine a UNIQUE Jacobi matrix; the carrier "
        "data has the verified-range closed form alpha_k = q^k, "
        "beta_k = q^(k-1)[k]_q (a q-deformed Gaussian N(1,1)); the "
        "kernel data has beta_1 = q^(1/2)+q^(-1/2)-1 = 1+(r-1/r)^2 — "
        "exact SOS positivity, the Wenzl quantity. K3-K4: Favard "
        "positivity (Hankel + beta > 0) EXACT at r=21/20 and q=6/5, "
        "60-dps at both q0 pins; monic-Jacobi moment reproduction "
        "(M^n)_00 = m_n exact — the canonical positive operator EXISTS "
        "with the binding data as moments, in both frames, "
        "Stieltjes-supported in the kernel frame. K5: at q = 1 both "
        "frames are Carleman-determinate (Laguerre alpha=2k+1, "
        "beta=k^2; Gaussian alpha=1, beta=k, exact) — the canonical "
        "kernel e^(-s)ds is DERIVED, zero convention. K3/K6-K7: at "
        "q != 1 beta grows geometrically (Carleman unavailable) and "
        "the theta-translate reindex identity (exact) gives a "
        "continuum of representing measures — the moment problem is "
        "INDETERMINATE, the minimal Jacobi operator has deficiency "
        "(1,1), and the kernel choice REAPPEARS as the self-adjoint-"
        "extension circle. Verdict: PARTIAL — the operator is "
        "canonical and derived, the measure is not; the remaining "
        "identification is the extension choice (Friedrichs/Krein "
        "distinguished; audit doc section 5). Nothing here proves or "
        "refutes any conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md")

    block_k1_carrier_symbolic(wb)
    print("K1: carrier symbolic — Hankels, Gaussian q=1 pin, closed-form "
          "Jacobi alpha_k=q^k, beta_k=q^(k-1)[k]_q reproduces S_q(n) "
          "exact.")
    block_k2_kernel_symbolic(wb)
    print("K2: kernel symbolic (r=q^(1/4)) — Laguerre q=1 pin, "
          "beta_1 = 1+(r-1/r)^2 SOS positivity — exact.")
    block_k3_exact(wb)
    print("K3: exact-Q Favard leg — Hankel/Stieltjes/beta positivity + "
          "GNS moment reproduction exact at r=21/20 and q=6/5.")
    block_k4_pins(wb)
    print("K4: both frames at pins (60 dps) — beta>0, moment "
          "reproduction < 1e-25.")
    block_k5_q1_determinacy(wb)
    print("K5: q=1 determinacy — Laguerre + Gaussian exact; canonical "
          "kernel derived at q=1.")
    block_k7_indeterminacy(wb)
    print("K7: q!=1 indeterminacy — reindex identity exact, continuum "
          "re-verified; extension circle = relocated convention.")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
