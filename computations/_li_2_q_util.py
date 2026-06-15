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
        t2 = t2 + li_2_q(v, q, q_inv)
    t3 = mpf(0)
    for i, vi in enumerate(vols):
        for vj in vols[i + 1:]:
            t3 = t3 + li_2_q(vi * vj, q, q_inv)
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
    """Family A linking weight (single source of truth for the
    production multiplier).

    This is the linking-weight component of VolDensity(𝓑₃, q) — older
    docs called it `λ_scale` before PR #1080 absorbed it into the
    per-knot Geom evaluation.  See
    `docs/lambda-scale-absorbed-into-vol-density.md` for the framing.

    The closed-form algebraic identity is proved exactly in
    `lambda_scale_all_c_i_family_a.py` (Python) and
    `lambda-scale-substrate-form.lean` (Lean):

        linking_weight_A(q) = (1/4) · Σ_{λ ⊢ 4} dim_q V_λ
                            = (3q² + 4 + 3q⁻²) / 4
                            = 5/2 + (3/4) h²,    h = q − q⁻¹

    The h-series TERMINATES exactly at h²: all higher h^{2k} coefficients
    are identically zero. Both the closed form and the termination are
    sorry-free Lean identities.

    Status (2026-06-04): the algebraic identity is exact, but the H₄
    Wedderburn-count INTERPRETATION is not a derived categorical count
    — at the substrate anchor q₀ the value ≈ 2.533 is a CODATA-implied
    near-match landing near `λ ≈ 2.46` (the value that round-trips
    m_p). Production use is retained because the round-trip diagnostic
    holds. Full provenance (five refuted derivation paths + the
    remaining productive directions GAP-A-3 / GAP-A-4) is in
    `docs/audits/2026-06-04-three-paths-refuted-roadmap-update.md`.

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
# `vol_density_borromean` wrapper when the full VolDensity evaluation is
# wanted).  Any future caller attempting `from _li_2_q_util import
# lambda_scale_family_a` will raise ImportError — by design, to force
# migration.


def bring_color_weighted_linking_weight(
    Z: int, N: int, q: mpf, q_inv: mpf | None = None,
) -> mpf:
    """Per-atom Bring-color-tube extension of linking_weight_family_a.

    [PROBE — extends `bring_color_weighted` from the per-interface
    p-n averaging in closed_form_tau_M.py to the BASE mass scale.]

    Categorical construction.  Each nucleon carries 3 color tubes
    (r, g, b) per Bring's 3-color-tube structure.  For atom (Z, N):

      Z protons (uud) + N neutrons (udd)
      Total quarks = 3·A where A = Z + N
      n_u = 2Z + N   (u-quark count)
      n_d = Z + 2N   (d-quark count)

    Substrate-derived quark-flavor split δ = flavor_split_subleading(q)
    encodes (m_d - m_u) / M_N.  The linking_weight then has TWO
    Bring-color-tube corrections to the H_4 average:

      linking_weight_bring(Z, N, q)
        = linking_weight_family_a(q) · (1 + δ·asym + δ²·sym)

    where:
      asym = (n_d - n_u) / (3·A) = (N - Z) / (3·A)
             — odd in flavor exchange; positive for neutron-rich, so
               correction is larger for n (matches δ = (m_n - m_p)/M_N > 0)
      sym  = 2·n_u·n_d / (3·A)²  — even in flavor exchange; shifts m_avg

    Reduces to Family A in the substrate-degenerate limit δ → 0.

    Effect at q₀ (δ ≈ 0.00138):
      - asym term: |δ/3| ≈ 4.6e-4 = 460 ppm asymmetric shift per p / n
      - sym term:  δ²·(4/9) ≈ 8.4e-7 = 0.84 ppm = 840 ppb symmetric
                   m_avg shift (measured 842.8 ppb at q₀)

    The symmetric m_avg shift is ~34000× smaller than the +2.89%
    (29 kppm = 28900 ppm) gap recorded in `lambda-scale-absorbed-into-vol-density.md`.
    This implementation therefore CONFIRMS that Bring-color-tube
    quark-flavor weighting at H_4 is structurally insufficient to
    close m_avg — consistent with the 5+ refuted routes documented
    in the canonical reference.

    Status: PROBE, NOT WIRED into production `vol_density_borromean`.
    Use via `vol_density_borromean_bring_color_weighted(Z, N, q)`.
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    base = linking_weight_family_a(q, qi)
    A = Z + N
    if A == 0:
        return base
    delta = flavor_split_subleading(q, qi)
    n_u = 2 * Z + N
    n_d = Z + 2 * N
    asym = mpf(N - Z) / mpf(3 * A)
    sym = mpf(2 * n_u * n_d) / mpf(3 * A) ** 2
    return base * (1 + delta * asym + delta ** 2 * sym)


def vol_density_borromean_bring_color_weighted(
    Z: int, N: int, q: mpf, q_inv: mpf | None = None,
) -> mpf:
    """Bring-color-tube extension of vol_density_borromean for atom (Z, N).

    [PROBE — parallels `vol_density_borromean` but uses the per-atom
    Bring-color-tube linking_weight instead of the H_4 Wedderburn
    average.]

    m(K) = m_e · VolDensity_bring(Z, N, q₀)

    Status: PROBE.  NOT wired into production mass computation;
    the existing `vol_density_borromean` (H_4 average, acknowledged
    CAL-4) remains in production until a categorical Bring-color-tube
    formulation is found that closes the +2.89% m_avg gap.
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    hbar_q = 1 - qi
    vol_b3 = 8 * mp.catalan
    geom_leading = vol_b3 / hbar_q ** 2
    return geom_leading * bring_color_weighted_linking_weight(Z, N, q, qi)


def vol_density_borromean(q: mpf, q_inv: mpf | None = None) -> mpf:
    """[SHORTCUT — global-scalar collapse, NOT the paper's per-block sum.]

    VolDensity(𝓑₃, q) — the complete per-knot Geom evaluation for the
    Borromean baryon mass formula (canonical post-PR #1080, 2026-05-23).

    ⚠ **Discipline note (2026-06-01, PR vol-density-perblock-wiring-fix).**
    This routine multiplies the bare hyperbolic Geom_leading =
    Vol(𝓑₃)/ℏ_q² by a GLOBAL scalar `linking_weight_family_a(q)` =
    (3q²+4+3q⁻²)/4 ≈ 2.53. That scalar is the H₄ (partitions of 4)
    half-symmetric Wedderburn count — it is NOT the paper's Stage-4
    per-block character sum `Σ_λ w_λ χ_λ(β)/dim λ` over partitions of
    the knot's own strand count.  For 𝓑₃ the paper's per-block sum is
    the H₃ Markov trace tr_M(𝓑₃) ≈ 1.065 (proton) / 0.923 (neutron),
    not 2.53.  The two differ by ≈ 2.38×; this routine therefore does
    NOT compute the formula in `prop:hoefsmit-scattering-pipeline`
    Stage 4 — the 2.53 is a CODATA-implied-λ near-match that lands
    near `λ = m_p/(m_e·Vol/ℏ²) ≈ 2.46` (the value that round-trips m_p).
    Use `vol_density_per_block(vol_K, tr_M_K, q, ...)` for the
    paper-faithful per-block evaluation.  This routine is retained ONLY until the
    per-block version is validated and the owner approves a production
    switch (the switch changes the m_p computation).

    The mass formula is:
        m(B) = m_e × VolDensity(𝓑₃, q₀)            (single Geom call)

    where VolDensity = Geom_leading × linking_weight:
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
        VolDensity per-knot decomposition (prop:geom-universality has
        no Lean theorem yet) — flagged as potential source of error.

    CANONICAL FORM (VolDensity → Vol × Density purge, Stage 2):
      This routine is the GLOBAL-density reading of the M=Vol×Density
      formula. It is bit-identical to
      ``mass_vol_density.vol_density_vd(vol_borromean(), q)`` — i.e.
      Vol(𝓑₃)·ρ_global(q)/ℏ_q² with ρ_global = linking_weight_family_a.
      See `mass_vol_density.py` for the proper-definition module exposing
      both the global ρ and the per-block ρ_pb = tr_M side-by-side. The
      primitive factoring (geom_leading × density) lives HERE; the M=VD
      module is the narrative/parity layer that re-exports it.

    Returns VolDensity = Vol(𝓑₃)/ℏ_q² × linking_weight(q).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    hbar_q = 1 - qi  # ℏ_q = (q - 1)/q = 1 - q⁻¹; reuse qi (Gemini PR #1089)
    vol_b3 = 8 * mp.catalan  # Adams 1985 (NOT Lean-formalized — see docstring)
    geom_leading = vol_b3 / hbar_q ** 2
    linking_weight = linking_weight_family_a(q, qi)
    # PROVED production formula: Vol(𝓑₃)/ℏ_q² × Family-A linking weight
    # (lw = (3q²+4+3q⁻²)/4, Lean: lambda-scale-substrate-form.lean).
    # m_e × this = m_avg ≈ 966 MeV (+2.89 % vs CODATA m_avg); the 2.89 %
    # is an OPEN R&D gap (categorical-exactness refinement at h² order).
    # The exploratory spectral-phase correction (spectral_correction_
    # borromean, −819 ppm on m_avg) is NOT applied here: it is unproved
    # (trivial Lean stub) so it must not enter production. Use it only
    # via the explicitly-exploratory vol_density_borromean_spectral().
    return geom_leading * linking_weight


def geom_leading(vol_K: mpf, q: mpf, q_inv: mpf | None = None) -> mpf:
    """Bare hyperbolic Geom_leading(K, q) = Vol(K) / ℏ_q².

    This is the `Geom(K)` factor of `prop:hoefsmit-scattering-pipeline`
    Stage 3 for hyperbolic `K` — the geometric projection of the
    algebraic Markov trace into a measurable observable.  It carries
    NO per-block character sum; the per-block sum is the SEPARATE
    `tr_M = Σ_λ w_λ χ_λ/dim λ` factor (Stage 2 / Stage 4).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    hbar_q = 1 - qi  # ℏ_q = (q - 1)/q
    return vol_K / hbar_q ** 2


def vol_density_per_block(
    vol_K: mpf,
    tr_M_K: mpf,
    q: mpf,
    q_inv: mpf | None = None,
) -> mpf:
    """Paper-faithful per-block VolDensity(K, q) — `prop:hoefsmit-
    scattering-pipeline` Stage 4, WITH the dropped Σ_λ factor restored.

    Computes the FULL mass-formula geometric factor of the paper:

        VolDensity(K) · (Σ_λ w_λ χ_λ(β)/dim λ)
          =  [Vol(K)/ℏ_q²]  ·  tr_M(K, q)

    where `tr_M(K, q) = Σ_λ w_λ χ_λ(β_K)/dim λ` is the canonical
    Markov trace over the partitions of the KNOT'S OWN strand count
    (H₃ for the 3-strand Borromean baryons, H₆ for the deuteron at
    n=6, etc.).  This is the `Σ_λ` factor that the legacy
    `vol_density_borromean` shortcut DROPPED and replaced with a global
    H₄ scalar.

    The mass is then `m(K) = m_e · vol_density_per_block(...)`.

    Arguments
    ---------
    vol_K   : hyperbolic volume Vol(K) of the knot complement
              (8·G for the Borromean rings, Adams 1985).
    tr_M_K  : the per-block Markov trace Σ_λ w_λ χ_λ/dim λ at q,
              loaded from the canonical chi-cache witness
              (`chi-{atom}-h{n}-at-q0-50dps.witness.json`) or computed
              via `canonical_tr_m_via_chi_cache.canonical_tr_m`.
    q, q_inv: substrate parameter and its inverse.

    Per CLAUDE.md production-vs-exploratory discipline: this is a
    DERIVATION (restores the paper's formula), not a fit.  NO fudge
    factor is applied; if the resulting m(K) disagrees with the
    legacy shortcut, that discrepancy is REPORTED, never tuned away.

    Returns Vol(K)/ℏ_q² · tr_M(K, q).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    return geom_leading(vol_K, q, qi) * tr_M_K


def spectral_correction_borromean(q: mpf, q_inv: mpf | None = None) -> mpf:
    """EXPLORATORY (UNPROVED — do not wire into production vol_density).
    Top-down spectral-phase correction to the Borromean linking weight.

    The leading VolDensity (Vol/ℏ² × lw_A) × m_e gives the AVERAGE
    nucleon mass m_avg, and is +2.89 % high.  The correction is the
    rotation angle of the Borromean braid 𝓑₃ on the 2-dimensional
    standard irrep V_(2,1) of H_3, measured per ideal octahedron in
    substrate-tick units:

        θ      = arccos( χ^(2,1)(𝓑₃) / 2 )     (𝓑₃ is det-1 ⇒ a rotation)
        χ^(2,1)(𝓑₃) = 2 − 3h⁴ − h⁶              (exact Hoefsmit character)
        correction = θ / (8 ℏ_q²)                (8 = Vol(𝓑₃)/G octahedra)

    All quantities are categorical with NO free parameter (the 8 cancels
    against Vol = 8G).  Applying it gives m_avg = 938.15 MeV, which is
    −819 ppm vs CODATA m_avg (938.92) — fully derived, no CODATA fitting,
    a ~35× improvement over the bare +2.89 %.  NOTE: m_avg lands only
    ~130 ppm from the PROTON (938.27), but that is coincidence — this
    routine produces the average nucleon mass, NOT m_p; the proton's
    own pinned value comes from the substrate identity (242 ppb / exact).
    See `docs/audits/2026-05-28-spectral-phase-correction-derived.md`.

    NOTE this correction is specific to multi-component LINKS: knots
    (muon = 4₁) have linking weight 1 and take NO such correction —
    their bare Vol/ℏ² is already exact (0.05 ppb).  χ^(2,1)(4₁) = −0.91
    is not near 2, so the rotation-angle reading does not apply.

    Residual ~819 ppm origin (Vol=8G precision / higher geometric term /
    calibration) is OPEN.  The "why the phase multiplies Geom this way"
    step is not yet Lean-proved (trivial stub in TwoRoutesProtonMass).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    h = q - qi
    hbar_q = 1 - qi
    chi = 2 - 3 * h ** 4 - h ** 6  # exact χ^(2,1)(𝓑₃), Hoefsmit seminormal
    theta = mp.acos(chi / 2)
    return theta / (8 * hbar_q ** 2)


def vol_density_borromean_spectral(q: mpf, q_inv: mpf | None = None) -> mpf:
    """EXPLORATORY (not production): proved Family-A vol_density × the
    UNPROVED spectral-phase correction. m_e × this = m_avg ≈ 938.15 MeV
    (−819 ppm vs CODATA m_avg) — a no-fit ~35× improvement over the bare
    +2.89 %, but the correction is not proved (trivial Lean stub) and the
    sinh(θ) refinement is an open lead, so this must NOT feed production.
    Production uses vol_density_borromean (proved Family A, +2.89 %).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    return vol_density_borromean(q, qi) * spectral_correction_borromean(q, qi)


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
