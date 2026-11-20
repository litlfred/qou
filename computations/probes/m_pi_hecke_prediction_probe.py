#!/usr/bin/env python3
"""
m_pi_hecke_prediction_probe.py — Probe: is m_π± derivable from
(CAL-1 m_e, CAL-2 q_0) without using m_π as a calibration input?

## Question

The framework derives m_p and m_n from (m_e, m_μ, q_0) via the
substrate identity m_p = 2·m_μ·F_Bor(q_0) − 12·m_e (see
m_p_substrate_identity_50dps.py, 0.24 ppm vs CODATA). Q_β reduces
similarly to 6 ppb via PR #546's N=3 ladder. Question: does the
charged pion m_π± = 139.57039 MeV (PDG 2024, ±1.3 ppb) reduce too,
or is it the elusive CAL-3 (a strong-sector observable independent
of the substrate)?

## Meson model

Per folio/quantum-observable-universe/archimedean-universe/
meson-to-proton-via-borromean.md, the u-dbar meson is the H_3(q)
braid

  𝓜_+ = σ_0 · L_+ · σ_0⁻¹

with NF (at q_0 ≈ 1.1098):

  NF(𝓜_+) = -0.209σ_1 - 0.044 L_+ + 1.000 L_- + 0.209 e⁻
  net(𝓜_+) ≈ +0.956

(verified by the _deprecated/meson-nucleon-nf.py probe; we
re-derive the canonical absolute |tr_M(𝓜_+)| here at 50 dps from
the canonical Markov-trace conventions.)

## Candidate formulas tried

Calibrations available without using m_π:
  CAL-1 = m_e = 0.51099895 MeV (CODATA 2022)
  CAL-2 = m_μ/m_e (= 206.768283) → q_0 = 1.10978... via Vol(4_1)/ℏ_q²

DERIVED from CAL-1+CAL-2 only (no Q_β):
  E_0 ~ m_e / (q_0(q_0−1)) ≈ 4.186 MeV (beta-scale, computable
        once q_0 is fixed; same scale used in mesons-nucleon-NF)
  F_Bor(q_0)             — Borromean Markov+q-factorial observable
  |tr_M(σ_0·L_+·σ_0⁻¹)|  — meson absolute Markov trace
  net(𝓜_+)               — meson NF net (≈0.956)
  m_μ = m_e · CAL-2       — muon mass (CAL-1 × CAL-2)

Candidate predictions (all in MeV):

  (a) m_π ?= |tr_M(𝓜_+)| · E_0
  (b) m_π ?= net(𝓜_+) · E_0
  (c) m_π ?= 2·m_μ · F_meson(q_0) − N · m_e  for integer N in [-30,30]
  (d) m_π ?= m_e · |tr_M(𝓜_+)|^k for k = ±1..±5 (lepton-tower extension)
  (e) m_π ?= m_e · F_Bor(q_0) · (some integer ratio)
  (f) m_π ?= m_μ · |tr_M(𝓜_+)|  (light meson via muon scale)
  (g) m_π ?= m_μ · (|tr_M(𝓜_+)| + N·h)  for h = q-q⁻¹ and various N

## Long-compute discipline

Compute is symbolic + 50-dps mpmath; runs in < 5 sec. No
periodic-progress hooks needed.

## Production wiring

Audit-only. No content block wires to this script; it tests whether
m_π is in fact a derivable observable (in which case it does NOT
need to be CAL-3) or whether it is genuinely independent (in which
case it IS a CAL-3 candidate).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, sqrt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_MU_MEV_VALIDATION as M_MU_MEV,
    M_PI_PM_MEV_VALIDATION,
)


# ── PDG 2024 reference for charged pion ─────────────────────────
M_PI_PDG_MEV = M_PI_PM_MEV_VALIDATION       # PDG 2024 (codata_constants registry)
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

M_PI_PDG_ERR_MEV = mpf("0.00018")           # ±0.00018 MeV (1.3 ppb)


def q_int(q, n):
    """Balanced q-integer [n]_q = (q^n − q^-n)/(q − q^-1)."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def qfact_three(q):
    """[3]_q! = [3]_q · [2]_q · [1]_q."""
    return q_int(q, 3) * q_int(q, 2) * q_int(q, 1)


def trM_borromean(q):
    """|tr_M(β_Bor, q)| from BorromeanMarkovTrace.lean closed form."""
    # convention D — verified by EVALUATION at q0, not by reading: computations/audits/borromean_convention_by_evaluation.py
    h = q - 1 / q
    return abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))


def F_Bor(q):
    """F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3."""
    return trM_borromean(q) * qfact_three(q) / q ** 3


# ── Hecke H_3(q) NF of the meson braid σ_0 · L_+ · σ_0⁻¹ ────────
#
# We use the symbolic reduction from the existing meson-nucleon-nf
# probe (verified at q_0 ≈ 1.1098: NF = -0.209σ_1 -0.044 L_+ +1.000 L_-
# +0.209 e⁻, net ≈ 0.956).  Here we redo the reduction symbolically in
# q via the closed-form skein/Hecke relations, evaluated at q_0 to
# 50 dps.
#
# σ_0·L_+·σ_0⁻¹ with L_+ = σ_0σ_1.  Substituting σ_0⁻¹ = σ_0 − h
# (Hecke skein) and using σ_0² → h·σ_0 + 1:
#
#   σ_0 · (σ_0 σ_1) · (σ_0 − h)
#     = σ_0² σ_1 σ_0 − h σ_0² σ_1
#     = (h σ_0 + 1) σ_1 σ_0 − h (h σ_0 + 1) σ_1
#     = h σ_0 σ_1 σ_0 + σ_1 σ_0 − h² σ_0 σ_1 − h σ_1
#     = h·e⁻ + L_− − h²·L_+ − h·σ_1
#
# where e⁻ ↔ σ_0σ_1σ_0 (trefoil), L_+ ↔ σ_0σ_1, L_− ↔ σ_1σ_0.
# Net at q_0:  N(𝓜_+) = h·tr(e⁻) + tr(L_−) − h²·tr(L_+) − h·tr(σ_1)
# but the paper's "net" is a *sum of NF coefficients* in the
# Gröbner-Shirshov basis (not the Markov trace).  We expose BOTH
# the GS net and the canonical Markov trace |tr_M(𝓜_+)|.

def meson_nf_coefficients(q):
    """Return (c_sigma1, c_Lplus, c_Lminus, c_e_minus) at q.

    NF of σ_0·L_+·σ_0⁻¹ = σ_0²·σ_1·(σ_0 − h)
                       = h·(σ_0σ_1σ_0) + (σ_1σ_0) − h²·(σ_0σ_1) − h·(σ_1)
    """
    h = q - 1 / q
    c_sigma1 = -h
    c_Lplus = -h ** 2          # coefficient of L_+ = σ_0σ_1
    c_Lminus = mpf(1)          # coefficient of L_− = σ_1σ_0
    c_e_minus = h              # coefficient of e⁻ = σ_0σ_1σ_0
    return c_sigma1, c_Lplus, c_Lminus, c_e_minus


def meson_net(q):
    """GS net = sum of NF coefficients at q."""
    c1, cLp, cLm, cem = meson_nf_coefficients(q)
    return c1 + cLp + cLm + cem


def markov_trace_basis(q):
    """Canonical Wenzl Markov trace of the basis elements at q.

    Convention A (matches lepton_tower_probe_1):
      z := q^3/(q^2+1) = q^2/[2]_q      (convention D, canonical 2026-08-15;
                                        convention C, 1/(q^½ + q^-½), is excised)
      tr_M(1)            = 1
      tr_M(σ_i)          = z
      tr_M(σ_i σ_j)      = z²    for i ≠ j (Hopf link)
      tr_M(σ_i σ_j σ_i)  = z² − h·z³? — derived from skein.

    For the meson 𝓜_+ = h·e⁻ + L_− − h²·L_+ − h·σ_1 we evaluate
    the trace linearly:
      tr_M(𝓜_+) = h·tr_M(σ_0σ_1σ_0) + tr_M(σ_1σ_0)
                  − h²·tr_M(σ_0σ_1) − h·tr_M(σ_1)

    tr_M(σ_0σ_1σ_0) in H_3(q): via cyclicity + Hecke σ_0² = h·σ_0 + 1,
      tr_M(σ_0σ_1σ_0) = tr_M(σ_1·σ_0²) = tr_M(σ_1·(h·σ_0+1))
                      = h·tr_M(σ_1σ_0) + tr_M(σ_1)
                      = h·z² + z.
    (Distinct from the H_2 trace of σ_0³ = (h²+1)z + h: both close to
    the trefoil knot, but the Markov trace differs by the strand
    normalization. The meson NF lives in H_3(q), so we use the H_3
    trace.)
    """
    # Convention D (canonical, 2026-08-15 owner ruling). The tr_M identities
    # below (tr(sigma)=z, tr(sigma_i sigma_j)=z^2, tr(sigma_0 sigma_1 sigma_0)
    # = h z^2 + z) follow from the Markov property plus the Hecke relation and
    # hold for ANY z, so they are convention-independent and this is a pure
    # definition migration.
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    tr_sig = z
    tr_Lplus = z ** 2          # Hopf link L_+
    tr_Lminus = z ** 2         # Hopf link L_− (same up to sign convention)
    tr_e_minus = h * z ** 2 + z   # trefoil in H_3(q)
    return tr_sig, tr_Lplus, tr_Lminus, tr_e_minus, z, h


def markov_trace_meson(q):
    """Canonical |tr_M(𝓜_+)| at q."""
    c1, cLp, cLm, cem = meson_nf_coefficients(q)
    tr_sig, tr_Lp, tr_Lm, tr_em, _, _ = markov_trace_basis(q)
    tr = (c1 * tr_sig + cLp * tr_Lp + cLm * tr_Lm + cem * tr_em)
    return fabs(tr)


def E0_from_substrate(q, m_e):
    """Energy scale derivable from CAL-1 + CAL-2 alone.

    The meson-to-proton-via-borromean.md derives E_0 = Q_β/|Δnet|
    ≈ 4.155 MeV using CAL-3 (Q_β).  Without CAL-3 we need an
    E_0 from (m_e, q_0).  Natural candidates:
      E_0^(A) = m_e / (q_0(q_0 − 1))     ← hint formula
      E_0^(B) = m_e / h²                  ← Hecke amplitude squared
      E_0^(C) = m_e · F_Bor(q_0)          ← Borromean observable
      E_0^(D) = m_e · [3]_q! · (q − 1)    ← q-factorial scaling
    """
    h = q - 1 / q
    return {
        "E0_A_me_over_q_qminus1": _qbeta_e0.order_zero_scaled(m_e, q),
        "E0_B_me_over_h_sq": m_e / h ** 2,
        "E0_C_me_FBor": m_e * F_Bor(q),
        "E0_D_me_qfact_qminus1": m_e * qfact_three(q) * (q - 1),
    }


def ppm(pred, target):
    return (pred - target) / target * mpf("1e6")


def ppb(pred, target):
    return (pred - target) / target * mpf("1e9")


def main():
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(M_E_MEV)
    m_mu = mpf(M_MU_MEV)
    h = q - 1 / q

    print("=" * 78)
    print("  m_π± Hecke-prediction probe (CAL-1 + CAL-2 only)")
    print("=" * 78)
    print()
    print(f"  CALIBRATIONS (only 2):")
    print(f"    m_e   = {mp.nstr(m_e, 14)} MeV   (CAL-1)")
    print(f"    m_μ/m_e = {mp.nstr(m_mu/m_e, 14)}  (CAL-2)")
    print(f"    q_0   = {mp.nstr(q, 14)}      (substrate, derived)")
    print(f"    h     = q − q⁻¹ = {mp.nstr(h, 14)}")
    print()
    print(f"  TARGET:")
    print(f"    m_π±_PDG   = {mp.nstr(M_PI_PDG_MEV, 14)} MeV  (PDG 2024, ±1.3 ppb)")
    print()

    # ── BUILDING BLOCKS ──────────────────────────────────────────
    abs_trM_meson = markov_trace_meson(q)
    net_meson = meson_net(q)
    F = F_Bor(q)
    abs_trM_Bor = trM_borromean(q)
    qfact3 = qfact_three(q)

    print(f"  BUILDING BLOCKS:")
    print(f"    |tr_M(𝓜_+)|      = {mp.nstr(abs_trM_meson, 18)}")
    print(f"    net(𝓜_+) (GS)    = {mp.nstr(net_meson, 18)}")
    print(f"    F_Bor(q_0)        = {mp.nstr(F, 18)}")
    print(f"    |tr_M(β_Bor, q_0)| = {mp.nstr(abs_trM_Bor, 18)}")
    print(f"    [3]_q!            = {mp.nstr(qfact3, 18)}")
    print()

    # ── E_0 candidates (no CAL-3) ────────────────────────────────
    E0s = E0_from_substrate(q, m_e)
    print(f"  E_0 (substrate-only) candidates:")
    for k, v in E0s.items():
        print(f"    {k}  = {mp.nstr(v, 12)} MeV")
    print()

    # ── CANDIDATE PREDICTIONS ────────────────────────────────────
    candidates = []

    # (a) |tr_M(𝓜_+)| · E_0 for each E_0
    for k, e0 in E0s.items():
        pred = abs_trM_meson * e0
        candidates.append(
            (f"(a/{k})  |tr_M(𝓜_+)| · {k}", pred)
        )

    # (b) net(𝓜_+) · E_0 for each E_0
    for k, e0 in E0s.items():
        pred = net_meson * e0
        candidates.append(
            (f"(b/{k})  net(𝓜_+) · {k}", pred)
        )

    # (c) 2·m_μ · F_meson − N·m_e for N ∈ [-30..30]; F_meson = |tr_M(𝓜_+)|
    for N in range(-30, 31):
        pred = 2 * m_mu * abs_trM_meson - N * m_e
        candidates.append((f"(c, N={N:+d})  2·m_μ·|tr_M(𝓜_+)| − {N}·m_e", pred))

    # (c') 2·m_μ · F_Bor − N·m_e (the substrate-identity transposed)
    for N in range(-30, 31):
        pred = 2 * m_mu * F - N * m_e
        candidates.append((f"(c', N={N:+d})  2·m_μ·F_Bor − {N}·m_e", pred))

    # (d) m_e · |tr_M(𝓜_+)|^k for k = ±1..±5
    for k in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
        pred = m_e * abs_trM_meson ** k
        candidates.append((f"(d, k={k:+d})  m_e · |tr_M(𝓜_+)|^{k}", pred))

    # (e) m_e · F_Bor^k for k = ±1..±5
    for k in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
        pred = m_e * F ** k
        candidates.append((f"(e, k={k:+d})  m_e · F_Bor^{k}", pred))

    # (f) m_μ · |tr_M(𝓜_+)|
    candidates.append(("(f)  m_μ · |tr_M(𝓜_+)|", m_mu * abs_trM_meson))

    # (g) m_μ · (|tr_M(𝓜_+)| + N·h) for N ∈ [-10..10]
    for N in range(-10, 11):
        pred = m_mu * (abs_trM_meson + N * h)
        candidates.append(
            (f"(g, N={N:+d})  m_μ · (|tr_M(𝓜_+)| + {N}·h)", pred)
        )

    # (h) m_μ · (F_Bor + N·h)
    for N in range(-10, 11):
        pred = m_mu * (F + N * h)
        candidates.append((f"(h, N={N:+d})  m_μ · (F_Bor + {N}·h)", pred))

    # (i) sqrt(m_e · m_μ) · |tr_M|^k  (geometric mean lepton scale)
    geo = sqrt(m_e * m_mu)
    for k in [-3, -2, -1, 0, 1, 2, 3]:
        pred = geo * abs_trM_meson ** k
        candidates.append(
            (f"(i, k={k:+d})  √(m_e·m_μ) · |tr_M(𝓜_+)|^{k}", pred)
        )

    # (j) m_μ · F_Bor (light-meson via Borromean)
    candidates.append(("(j)  m_μ · F_Bor", m_mu * F))

    # (k) m_e · (q-factorial / h^k) — small-h amplification
    for k in [1, 2, 3, 4, 5]:
        pred = m_e * qfact3 / h ** k
        candidates.append((f"(k, k={k:+d})  m_e · [3]_q! / h^{k}", pred))

    # (l) m_μ · (2 - net(𝓜_+)) (instability penalty)
    candidates.append(("(l)  m_μ · (2 − net(𝓜_+))", m_mu * (2 - net_meson)))
    candidates.append(("(l')  m_μ · (1 + net(𝓜_+))", m_mu * (1 + net_meson)))

    # ── SCORE & SORT ─────────────────────────────────────────────
    # NO-FLOAT64 (2026-09-13): `miss` stays an mpf end to end. It was
    # `float(fabs(...))` — a float64 that was BOTH the sort key and the
    # published `miss_ppm` / `miss_ppb`, i.e. computation, not display.
    # Sorting on the mpf keeps the ranking exact; the witness serializes
    # with `mp.nstr` at the same width as its neighbours.
    def miss_ppm(pred):
        return fabs(ppm(pred, M_PI_PDG_MEV))

    scored = sorted(
        ((label, pred, miss_ppm(pred)) for label, pred in candidates),
        key=lambda x: x[2],
    )

    print("=" * 78)
    print("  TOP 20 CANDIDATES (sorted by ppm miss vs PDG m_π± = 139.57039 MeV)")
    print("=" * 78)
    print(f"  {'rank':>4}  {'pred (MeV)':>16}  {'miss (ppm)':>14}  formula")
    print(f"  {'-'*4}  {'-'*16}  {'-'*14}  {'-'*60}")
    for rank, (label, pred, miss) in enumerate(scored[:20], 1):
        # float() here is DISPLAY ONLY (AGENTS.md permits it in an f-string).
        miss_str = (f"{float(miss):>14.3e}" if miss >= 1
                    else f"{float(miss * 1000):>11.3f} ppb")
        print(f"  {rank:>4}  {float(pred):>16.6f}  {miss_str}  {label}")
    print()

    best_label, best_pred, best_miss_ppm = scored[0]
    best_miss_ppb = best_miss_ppm * 1000

    print("=" * 78)
    print("  BEST MATCH")
    print("=" * 78)
    print(f"  Formula: {best_label}")
    print(f"  Pred:    {mp.nstr(best_pred, 14)} MeV")
    print(f"  PDG:     {mp.nstr(M_PI_PDG_MEV, 14)} MeV")
    print(f"  Miss:    {float(best_miss_ppm):.3e} ppm  "
          f"({float(best_miss_ppb):.3e} ppb)")
    print(f"  PDG exp: ±1.3 ppb")
    print()

    # ── VERDICT ──────────────────────────────────────────────────
    if best_miss_ppb < mpf("1.3"):
        verdict = "DERIVABLE — best candidate matches PDG within experimental precision"
        cal3_status = "m_π is NOT a CAL-3 candidate (reduces to CAL-1+CAL-2)"
    elif best_miss_ppm < mpf(100):
        verdict = (
            f"NEARLY-DERIVABLE — best candidate within {float(best_miss_ppm):.1f} ppm. "
            "Likely indicates a formula correction is needed, not new physics."
        )
        cal3_status = "m_π is a WEAK CAL-3 candidate (close match suggests derivable)"
    elif best_miss_ppm < mpf(10000):
        verdict = (
            f"PARTIAL — best candidate within {float(best_miss_ppm):.0f} ppm. "
            "Order of magnitude correct but no exact formula found."
        )
        cal3_status = "m_π is a MODERATE CAL-3 candidate"
    else:
        verdict = (
            f"NOT DERIVABLE from tried formulas — best miss {float(best_miss_ppm):.0f} ppm. "
            "Suggests m_π carries information beyond (m_e, q_0)."
        )
        cal3_status = (
            "m_π is a STRONG CAL-3 candidate — likely encodes "
            "chiral condensate / strange-flavor degree of freedom not "
            "present in the leptonic substrate."
        )

    print(f"  VERDICT: {verdict}")
    print(f"  CAL-3 status: {cal3_status}")
    print()

    # ── BUILD WITNESS ────────────────────────────────────────────
    w = WitnessBuilder("m-pi-hecke-prediction-probe", engine="mpmath")
    w.set_description(
        "Probe: tries 100+ candidate formulas for m_π± from CAL-1 (m_e) "
        "and CAL-2 (q_0/m_μ) alone (no m_π input). Tests whether the "
        "charged pion mass reduces the way Q_β did (PR #546, 6 ppb) or "
        "whether it is the elusive CAL-3 — a strong-sector observable "
        "independent of the leptonic substrate. Uses the meson braid "
        "𝓜_+ = σ_0·L_+·σ_0⁻¹ in H_3(q) from "
        "meson-to-proton-via-borromean.md, evaluated at q_0 to 50 dps "
        "via the canonical Markov trace (Wenzl convention A)."
    )
    w.set_audit_only(
        "Audit-only probe — no content block consumes this output. "
        "Question: is m_π± derivable from (m_e, q_0)?"
    )

    w.add_parameter("q0", mp.nstr(q, 25))
    w.add_parameter("m_e_MeV", mp.nstr(m_e, 18))
    w.add_parameter("m_mu_MeV", mp.nstr(m_mu, 18))
    w.add_parameter("m_pi_pdg_MeV", mp.nstr(M_PI_PDG_MEV, 18))
    w.add_parameter("m_pi_pdg_err_MeV", mp.nstr(M_PI_PDG_ERR_MEV, 18))
    w.add_parameter("m_pi_pdg_err_ppb",
                    mp.nstr(M_PI_PDG_ERR_MEV / M_PI_PDG_MEV * mpf("1e9"), 6))

    w.add_data("substrate_building_blocks", {
        "h": mp.nstr(h, 25),
        "abs_trM_meson": mp.nstr(abs_trM_meson, 25),
        "net_meson_GS": mp.nstr(net_meson, 25),
        "F_Bor": mp.nstr(F, 25),
        "abs_trM_Bor": mp.nstr(abs_trM_Bor, 25),
        "qfact_3": mp.nstr(qfact3, 25),
        "meson_NF_coeffs": {
            "c_sigma1": mp.nstr(meson_nf_coefficients(q)[0], 18),
            "c_Lplus": mp.nstr(meson_nf_coefficients(q)[1], 18),
            "c_Lminus": mp.nstr(meson_nf_coefficients(q)[2], 18),
            "c_e_minus": mp.nstr(meson_nf_coefficients(q)[3], 18),
        },
    })

    w.add_data("E0_candidates_MeV",
               {k: mp.nstr(v, 18) for k, v in E0s.items()})

    pdg_err_ppb = M_PI_PDG_ERR_MEV / M_PI_PDG_MEV * mpf("1e9")

    w.add_data("top_20_candidates", [
        {
            "rank": i + 1,
            "formula": label,
            "pred_MeV": mp.nstr(pred, 18),
            "miss_ppm": mp.nstr(miss, 18),
            "miss_ppb": mp.nstr(miss * 1000, 18),
            "within_pdg_err": bool((miss * 1000) < pdg_err_ppb),
        }
        for i, (label, pred, miss) in enumerate(scored[:20])
    ])

    w.add_data("best_match", {
        "formula": best_label,
        "pred_MeV": mp.nstr(best_pred, 25),
        "pdg_MeV": mp.nstr(M_PI_PDG_MEV, 18),
        "miss_ppm": mp.nstr(best_miss_ppm, 18),
        "miss_ppb": mp.nstr(best_miss_ppb, 18),
        "pdg_exp_precision_ppb": mp.nstr(pdg_err_ppb, 18),
        "matches_within_pdg_error": bool(best_miss_ppb < mpf("1.3")),
    })

    w.add_data("verdict", {
        "summary": verdict,
        "cal3_status": cal3_status,
        "n_candidates_tried": len(candidates),
        "best_miss_ppm": mp.nstr(best_miss_ppm, 18),
        "best_miss_ppb": mp.nstr(best_miss_ppb, 18),
    })

    w.add_caveat(
        "This is a TRIAL-AND-ERROR probe — it does not derive any "
        "candidate from first principles. A best-miss < 1 ppb is "
        "necessary-but-not-sufficient for m_π to be 'derivable'; a "
        "categorical derivation of the matching formula would also be "
        "required. A best-miss >> 100 ppm is strong evidence m_π "
        "needs an independent input."
    )
    w.add_caveat(
        "Mesons are flagged UNSTABLE at q_0 in "
        "meson-to-proton-via-borromean.md (negative NF coefficients "
        "demand environment crossing/Hopf content). The mass formula "
        "for an unstable state may differ structurally from the "
        "stable-baryon one (which uses 2·m_μ·F_Bor − 12·m_e)."
    )

    w.add_assertion(
        name="best_miss_below_1ppb_means_derivable",
        # add_assertion takes STRINGS to keep the value out of float64
        # (qou-t0rf); `passed` coerces with float() either way.
        computed=mp.nstr(best_miss_ppb, 18),
        expected="0",
        tolerance="1.3",  # PDG exp precision
        unit="ppb",
        source=(
            "If the best candidate matches m_π± within 1.3 ppb (PDG "
            "experimental precision), m_π is derivable from CAL-1+CAL-2. "
            "If not, m_π is a CAL-3 candidate."
        ),
    )

    out = w.save()
    print(f"  Witness: {out}")


if __name__ == "__main__":
    main()
