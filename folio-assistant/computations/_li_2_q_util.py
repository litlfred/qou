"""
Shared utility: symmetric q-dilogarithm Li_2^q at MPFR precision.

**Context (per prop:li2q-phiq-bar-symmetrization).** Li_2^q is the
**pre-τ / R-side / categorical** form of the q-dilogarithm —
bar-invariant under q ↔ q^{-1}, lives in the Habiro ring
$\\widehat{\\mathbb{Z}[q]}[\\![z]\\!]$, purely algebraic. It is
**canonical for BINDING context** (B(K) = m_atom − Z·m_p − N·m_n,
Δm_pn, isospin differences) because the bar-symmetric form
kills the dimensional mass scale — exactly what is wanted when
masses cancel in a difference.

For MASS context (m_p, m_n, m_e, m_atom absolutes; m_p/m_e ratio)
use `_phi_q_util.py` instead — Φ_q (Faddeev) is the bar-asymmetric
archimedean / post-τ form that carries the dimensional mass scale.

Per `prop:mass-endomorphism-tower` ([mass-endomorphism-tower.md]),
the canonical mass-formula brane-tower contribution uses the
**symmetric q-dilogarithm**

    Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q),

with the symmetric q-integer

    [n]_q = (q^n − q^{-n}) / (q − q^{-1}).

This replaces the earlier Faddeev Φ_q form (asymmetric (q^n − 1)
q-integer), per the 2026-05-03 paper revision note.  The Faddeev
form is empirically incompatible with isospin symmetry at q_0
(`brane-tower-isospin-diagnosis.witness.json`).

The canonical brane-tower terms are

    T2 = − Σ_i Li_2^q(−|V̂_i^full|)
    T3 = − z² · Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)

— note the **minus signs** outside and the **negative argument**
inside.  At the substrate value q_0 with |V̂| ∈ [0, 1) these
evaluate to small positive corrections (the alternating series
converges far from any pole, unlike Faddeev Φ_q which blows up
near |z| = q).

Convergence: Li_2^q(z) converges absolutely for |z| < 1; the
factor z^n / (n · [n]_q) decays super-exponentially because
[n]_q ~ q^{n-1}/(q − q^{-1}) grows exponentially.  We truncate
when the next-term magnitude falls below `eps`.
"""
from __future__ import annotations

import json as _json
from pathlib import Path

from mpmath import mp, mpf


def _q_int(n: int, q: mpf, q_inv: mpf) -> mpf:
    """Symmetric q-integer [n]_q = (q^n − q^{-n})/(q − q^{-1}).

    [0]_q := 0 by convention; [1]_q = 1; [n]_q approaches the
    classical integer as q → 1.
    """
    if n == 0:
        return mpf(0)
    if n == 1:
        return mpf(1)
    return (q**n - q_inv**n) / (q - q_inv)


def li_2_q(
    z_val: mpf,
    q: mpf,
    q_inv: mpf | None = None,
    max_k: int = 2000,
    eps: mpf | None = None,
) -> mpf:
    """Symmetric q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q).

    Convergence: the radius of convergence is |z| < q (not |z| < 1):
    by ratio test, |a_{n+1}/a_n| → |z|/q since [n+1]_q/[n]_q → q
    as n → ∞.  At |z| = q the series fails the necessary condition
    (terms ~ 1/n at the boundary).  We return ``mp.mpf('inf')`` only
    when |z| ≥ q.  In particular Li_2^q(-1) IS FINITE at q_0 ≈ 1.11
    (alternating series with super-exponentially-decaying terms).
    Truncation cuts at the first term whose magnitude < eps.
    """
    if q_inv is None:
        q_inv = mpf(1) / q
    if eps is None:
        eps = mpf(10) ** (5 - mp.dps)
    if mp.fabs(z_val) >= q:
        return mpf("inf")
    total = mpf(0)
    z_pow = mpf(1)
    for n in range(1, max_k + 1):
        z_pow = z_pow * z_val  # z^n
        qn = _q_int(n, q, q_inv)
        if qn == 0:
            return mpf("inf")
        term = z_pow / (mpf(n) * qn)
        total = total + term
        if mp.fabs(term) < eps:
            break
    return total


# ── Shared helpers (centralized per gemini #687 review) ─────────

_Q_WITNESS_DEFAULT = Path(__file__).parent / "q-pinning-50-digit.witness.json"


def load_q_50dps(path: Path | None = None) -> tuple[mpf, mpf, mpf]:
    """Load q_0, q_0^{-1}, and z = 1/(q^{1/2}+q^{-1/2}) at full
    ``mp.dps`` precision from the canonical pinning witness.

    Returns ``(q, q_inv, z)``.  Shared by every script that ingests
    per-generator Wedderburn volumes — centralized per gemini #687.
    """
    if path is None:
        path = _Q_WITNESS_DEFAULT
    with path.open() as fh:
        d = _json.load(fh)
    q = mpf(d["derived_50_digit"]["q"])
    qi = mpf(1) / q
    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
    return q, qi, z


def compute_t2_t3_from_vols(
    vols: list[mpf], q: mpf, q_inv: mpf, z: mpf,
) -> tuple[mpf, mpf]:
    """Compute T2 = Σ_i Li_2^q(|V̂_i|) and T3 = z²·Σ_{i<j} Li_2^q(|V̂_i·V̂_j|).

    Canonical Li_2^q brane-tower contributions per
    ``prop:mass-endomorphism-tower``, applied locally to a list of
    per-generator Wedderburn full-volume scalars.

    Used by ``derive_m_{p,n}_hecke_full_tower_50dps`` when the
    upstream producer no longer emits pre-summed
    ``term2_single_50dps`` / ``term3_pair_50dps`` fields.
    """
    t2 = mpf(0)
    for v in vols:
        t2 = t2 + li_2_q(mp.fabs(v), q, q_inv)
    t3 = mpf(0)
    for i, vi in enumerate(vols):
        for vj in vols[i + 1:]:
            t3 = t3 + li_2_q(mp.fabs(vi * vj), q, q_inv)
    t3 = t3 * z ** 2
    return t2, t3


# ── prop:flavor-split-substrate helpers (from #690) ────────────


def flavor_split_leading(q: mpf, q_inv: mpf | None = None) -> mpf:
    """Δm / M_N leading-order substrate formula (prop:flavor-split-substrate).

    Δm / M_N = (q − 1)² · (1 − q⁻⁴) / 3 = ℏ_q² · h_q · [2]_q / 3
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    return (q - 1) ** 2 * (1 - qi ** 4) / 3


def flavor_split_subleading(q: mpf, q_inv: mpf | None = None) -> mpf:
    """Δm / M_N with (1+ℏ_q³) 3-loop substrate-Planck correction."""
    qi = mpf(1) / q if q_inv is None else q_inv
    leading = flavor_split_leading(q, qi)
    hbar = (q - 1) / q
    return leading * (1 + hbar ** 3)


def linking_weight_family_a(q: mpf, q_inv: mpf | None = None) -> mpf:
    """PROVED Family A categorical linking weight (single source of truth).

    This is the linking-weight component of Geom_full(𝓑₃, q) — older
    docs called it `λ_scale` before PR #1080 absorbed it into the
    per-knot Geom evaluation.  See
    `docs/lambda-scale-absorbed-into-geom-full.md` for the framing.

    Closed-form identity proved in
    `lambda_scale_all_c_i_family_a.py` (Python) and
    `lambda-scale-substrate-form.lean` (Lean):

        linking_weight_A(q) = (1/4) · Σ_{λ ⊢ 4} dim_q V_λ
                            = (3q² + 4 + 3q⁻²) / 4
                            = 5/2 + (3/4) h²

    where h = q − q⁻¹. The h-series TERMINATES exactly at h²:
    all higher h^{2k} coefficients are identically zero.

    Replaces three independent inline copies of the same algebraic
    expression in production scripts (Gemini PR #942 review, 2026-05-23
    — centralize to avoid drift).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    h = q - qi
    return mpf(5) / 2 + mpf(3) * h ** 2 / 4


# NOTE: the legacy alias `lambda_scale_family_a = linking_weight_family_a`
# was REMOVED on 2026-05-24 (PR #1089 review-cycle, Copilot finding).
# Per owner directive: "no lambda-scale ANYWHERE in production".  All
# call sites now import `linking_weight_family_a` (or use the
# `geom_full_borromean` wrapper when the full Geom_full evaluation is
# wanted).  Any future caller attempting `from _li_2_q_util import
# lambda_scale_family_a` will raise ImportError — by design, to force
# migration.


def geom_full_borromean(q: mpf, q_inv: mpf | None = None) -> mpf:
    """Geom_full(𝓑₃, q) — the complete per-knot Geom evaluation for the
    Borromean baryon mass formula (canonical post-PR #1080, 2026-05-23).

    The mass formula is:
        m(B) = m_e × Geom_full(𝓑₃, q₀)            (single Geom call)

    where Geom_full = Geom_leading × linking_weight:
        Geom_leading = Vol(𝓑₃) / ℏ_q²           (bare hyperbolic volume)
        linking_weight = what Geom assigns to multi-component links
                         beyond bare volume (= 1 for knots, > 1 for links)

    Currently: linking_weight = linking_weight_family_a(q) (PROVED Family A
    categorical Wedderburn identity).  The −G·h² Yekutieli correction
    is NOT included — purged 2026-05-24 as non-canonical (PR #985
    bijection NEGATIVE).

    NAMING: older docs called the linking_weight component `λ_scale`
    before it was absorbed into the per-knot Geom evaluation.  There is
    no separate λ_scale constant.  For knots (muon = 4₁): linking_weight
    = 1 (Geom = Vol/ℏ_q²).  For links (proton = 𝓑₃): linking_weight
    ≈ 2.46.

    LEAN COVERAGE:
      - PROVED: linking_weight identity (`lambda-scale-substrate-form.lean`)
      - NOT PROVED: Vol(𝓑₃) = 8·G (Adams 1985 cited from literature);
        Geom_full per-knot decomposition (prop:geom-universality has
        no Lean theorem yet) — flagged as potential source of error.

    Returns Geom_full = Vol(𝓑₃)/ℏ_q² × linking_weight(q).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    hbar_q = 1 - qi  # ℏ_q = (q - 1)/q = 1 - q⁻¹; reuse qi (Gemini PR #1089)
    vol_b3 = 8 * mp.catalan  # Adams 1985 (NOT Lean-formalized — see docstring)
    geom_leading = vol_b3 / hbar_q ** 2
    linking_weight = linking_weight_family_a(q, qi)
    return geom_leading * linking_weight


def yekutieli_correction_h2(q: mpf, q_inv: mpf | None = None) -> mpf:
    """EXPLORATORY: the unproved −G·h² Yekutieli per-cell curvature
    correction to the linking weight.

    Per production-vs-exploratory discipline: this is a FRAMEWORK
    CLAIM, not a proved theorem. The specific value −G comes from
    the Yekutieli non-abelian Stokes argument (per-cell curvature
    on 𝓑₃'s 8 ideal octahedra), but:
      - The S₄↓S₃ bijection step is structurally derived (factor 2/5,
        proved in Lean) but the full Yekutieli categorical chain is
        not Lean-proved end-to-end
      - The standalone polynomial form 5/2 − G·h² fails q-locality
        (substrate-q₀ coincidence per PR #951)
      - PR #985 found κ = +0.5, not −G, in the natural-reading

    The Yekutieli 2015 non-abelian Stokes theorem IS valid math.
    What's unproved is our framework's claim that it yields −G·h²
    for the linking weight correction.

    Use ONLY for exploratory comparison columns, never in production.
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    h = q - qi
    return -mp.catalan * h ** 2


def borromean_markov_trace_h2(q: mpf, q_inv: mpf | None = None) -> mpf:
    """Markov trace of the Borromean braid (σ₁σ₂⁻¹)³ on H₃(q).

    Via the Jones polynomial of the Borromean rings:
        V(t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³
    at t = q², normalized by (q^{1/2} + q^{-1/2})².

    Taylor expansion at q=1 (h = q − q⁻¹ = 0):
        tr_M(β_Bor, q) = 1 + (3/16)·h² + O(h⁴)

    The h² coefficient **3/16** is a clean rational identified by
    `mpmath.identify`.  Under the (n−1)-strand normalization
    (Jones normalization factor 4 = (1+1)² at q=1 for n=3 strands):

        (3/16) × 4 = 3/4 = Family A's proved h² coefficient

    establishing that Family A's λ_A = 5/2 + (3/4)·h² IS the
    Borromean braid trace, renormalized to the H₄ Wedderburn sum.

    Ref: `yekutieli_borromean_h2_extraction.py` (empirical computation).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    sq = mp.sqrt(q)
    sqi = mpf(1) / sq
    t = q ** 2
    ti = qi ** 2
    jones = -ti**3 + 3*ti**2 - 2*ti + 4 - 2*t + 3*t**2 - t**3
    norm = (sq + sqi) ** 2
    return jones / norm
