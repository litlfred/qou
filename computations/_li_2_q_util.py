"""
Shared utility: symmetric q-dilogarithm Li_2^q at MPFR precision.

**Context (per `li2q-phiq-bar-symmetrization`).** Li_2^q is the
**pre-τ / R-side / categorical** form of the q-dilogarithm —
bar-invariant under q ↔ q^{-1}, lives in the Habiro ring
$\\widehat{\\mathbb{Z}[q]}[\\![z]\\!]$, purely algebraic. It is
**canonical for BINDING context** (B(K) = m_atom − Z·m_p − N·m_n,
Δm_pn, isospin differences) because the bar-symmetric form
kills the dimensional mass scale — exactly what is wanted when
masses cancel in a difference.

For MASS context (m_p, m_n, m_e, m_atom absolutes; m_p/m_e ratio)
use `_phi_q_util.py` instead — its `phi_q` is the COMPACT quantum
dilogarithm (reciprocal q-Pochhammer `∏(1−q^{-k}z)^{-1}`), the
bar-asymmetric archimedean / post-τ form that carries the dimensional
mass scale. (NOT the Faddeev *non-compact* Φ_b modular double; the legacy
"Faddeev" naming there is corrected — see the terminology ruling in
`docs/audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`.)

Per `prop:mass-endomorphism-tower` ([mass-endomorphism-tower.md]),
the canonical mass-formula brane-tower contribution uses the
**symmetric q-dilogarithm**

    Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q),

with the symmetric q-integer

    [n]_q = (q^n − q^{-n}) / (q − q^{-1}).

This replaces the earlier compact-q-dilog form (asymmetric (q^n − 1)
q-integer), per the 2026-05-03 paper revision note.  That compact form
is empirically incompatible with isospin symmetry at q_0
(`brane-tower-isospin-diagnosis.witness.json`).

The canonical brane-tower terms are

    T2 = − Σ_i Li_2^q(−|V̂_i^full|)
    T3 = − z² · Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)

— note the **minus signs** outside and the **negative argument**
inside.  At the substrate value q_0 with |V̂| ∈ [0, 1) these
evaluate to small positive corrections (the alternating series
converges far from any pole, unlike the compact q-dilog phi_q which
blows up near |z| = q).

Convergence: Li_2^q(z) converges absolutely for |z| < 1; the
factor z^n / (n · [n]_q) decays super-exponentially because
[n]_q ~ q^{n-1}/(q − q^{-1}) grows exponentially.  We truncate
when the next-term magnitude falls below `eps`.

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import json as _json
from pathlib import Path

from mpmath import mp, mpf


#: [n]_q cache, keyed by (working precision, q). [n]_q depends ONLY on q and n
#: — never on z — and q is a pinned substrate constant, so every caller of
#: `li_2_q` at a given precision wants the same ladder. Keyed on `mp.prec` as
#: well as q because an mpf keeps the precision it was CREATED at: a ladder
#: built at dps 15 must not be served to a caller running at 70.
_QINT_CACHE: dict = {}


def _q_int_ladder(q: mpf, q_inv: mpf, upto: int) -> list:
    """Return [[0]_q, [1]_q, ..., [upto]_q], extending the cache in place.

    Powers are built INCREMENTALLY (q^n from q^{n-1}) rather than by `q**n`.
    The naive form costs two full mpf exponentiations per term; at the
    ~7,000 terms the series needs near the disc edge that dominates the whole
    evaluation. Measured 3.4x on its own.
    """
    key = (mp.prec, q)
    st = _QINT_CACHE.get(key)
    if st is None:
        st = {"vals": [mpf(0)], "qp": mpf(1), "qip": mpf(1), "h": q - q_inv}
        _QINT_CACHE[key] = st
    vals = st["vals"]
    while len(vals) <= upto:
        n = len(vals)
        st["qp"] = st["qp"] * q
        st["qip"] = st["qip"] * q_inv
        vals.append(mpf(1) if n == 1 else (st["qp"] - st["qip"]) / st["h"])
    return vals


def _q_int(n: int, q: mpf, q_inv: mpf) -> mpf:
    """Symmetric q-integer [n]_q = (q^n − q^{-n})/(q − q^{-1}).

    [0]_q := 0 by convention; [1]_q = 1; [n]_q approaches the
    classical integer as q → 1.
    """
    if n == 0:
        return mpf(0)
    if n == 1:
        return mpf(1)
    return _q_int_ladder(q, q_inv, n)[n]


def li_2_q(
    z_val: mpf,
    q: mpf,
    q_inv: mpf | None = None,
    max_k: int = 50_000,
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
    # DISPATCH TO THE CLOSED FORM for negative z near the disc edge.
    #
    # The series and the q-product are the SAME function (see
    # `li_2_q_negative_continuation` for the derivation), but their costs run in
    # opposite directions:
    #
    #   series      terms ~ dps·ln10 / ln(q/|z|)   -> explodes as |z| -> q
    #   closed form terms ~ dps·ln10 / (2·ln q)    -> independent of z
    #
    # Equating them puts the crossover at ln(q/|z|) = 2·ln q, i.e. |z| = 1/q.
    # That is DERIVED, not tuned, and it matches measurement: at dps 70 the
    # series needs 180 terms at z = -0.5 but 7,083 at z = -1.08837, while the
    # product sits at ~717 throughout. At the brane tower's largest argument
    # (max|V_hat| = 1.08837) this is a 29.6x speedup, and the two agree to the
    # full 65 digits.
    if z_val < 0 and mp.fabs(z_val) >= q_inv:
        return li_2_q_negative_continuation(z_val, q, q_inv, eps=eps)
    if mp.fabs(z_val) >= q:
        # OUTSIDE THE SERIES DISC. The series has radius |z| < q, but the
        # FUNCTION does not stop there — see `li_2_q_negative_continuation`.
        # For z < 0 every product factor is 1 + |z|q^{-1-2m} > 1, so the
        # continuation is real, positive-argument and convergent, and we
        # return it. That is the branch the brane tower actually takes:
        # it only ever evaluates g(x) = -Li_2^q(-x) at x > 0.
        #
        # For z >= q > 0 the first factors 1 - z·q^{-1-2m} go negative, so the
        # continuation is genuinely complex (the branch cut) and `inf` is
        # retained rather than silently returning a principal value.
        if z_val < 0:
            return li_2_q_negative_continuation(z_val, q, q_inv, eps=eps)
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
            return total
    raise RuntimeError(
        f"li_2_q: series did not reach eps={mp.nstr(eps, 3)} within "
        f"max_k={max_k} at z={mp.nstr(z_val, 10)} (|z|/q="
        f"{mp.nstr(mp.fabs(z_val) / q, 6)}). The old max_k=2000 default "
        f"returned SILENTLY here, correct to ~21 digits rather than mp.dps; "
        f"raise max_k or use li_2_q_negative_continuation for z < 0.")


# ── Shared helpers (centralized per gemini #687 review) ─────────

def _find_q_witness() -> Path:
    """Locate q-pinning-50-digit.witness.json in whichever layout we are in.

    `Path(__file__).parent / ...` is right for computations/ but WRONG for the
    vendored copy: the sync flattens this module into qou-mass/.../_internal/
    while the witness lands one level up in qou-mass/.../qou_mass/. Same class
    of bug as the fixed-`.parent`-count in `_precision.py` — a path tuned for
    one layout, silently wrong in the other. Searched, not counted.
    """
    here = Path(__file__).resolve().parent
    for base in (here, *here.parents):
        cand = base / "q-pinning-50-digit.witness.json"
        if cand.is_file():
            return cand
        cand = base / "computations" / "q-pinning-50-digit.witness.json"
        if cand.is_file():
            return cand
    # preserve the historical value so the error names the expected location
    return here / "q-pinning-50-digit.witness.json"


_Q_WITNESS_DEFAULT = _find_q_witness()


def li_2_q_negative_continuation(
    z_val: mpf,
    q: mpf,
    q_inv: mpf | None = None,
    max_m: int = 100_000,
    eps: mpf | None = None,
) -> mpf:
    """Analytic continuation of ``li_2_q`` to ``z < 0``, past the series disc.

    DERIVED, not fitted. With ``[n]_q = (q^n - q^-n)/h`` and ``h = q - q^-1``,

        z^n / (n [n]_q) = (h/n) · SUM_{m>=0} (z q^{-1-2m})^n

    and summing over ``n`` first (``SUM_n w^n/n = -ln(1-w)``) gives the q-product

        Li_2^q(z) = -h · SUM_{m>=0} ln(1 - z q^{-1-2m}),

    convergent off the poles ``{q^{1+2m}}`` and equal to the series wherever the
    series converges. Verified against `li_2_q` to ~1e-45 at
    z in {-1, -0.5, 0.5, 0.9, 1.05} (`--self-test`).

    Restricted to ``z < 0`` deliberately: there every factor is
    ``1 + |z| q^{-1-2m} > 1``, so the sum is real, and it is the only branch the
    brane tower needs — it evaluates ``g(x) = -Li_2^q(-x)`` at ``x > 0`` only.
    For ``z >= q > 0`` the continuation is complex and `li_2_q` keeps returning
    ``inf`` rather than a silent principal value.

    WHY THIS EXISTS. `li_2_q` hard-returned ``inf`` for ``|z| >= q``, and that
    GUARD — not the function — is what made the atom-word brane tower "diverge
    for Z >= 2". Only one argument even crosses the radius (tau_p^2 = 1.13488
    against q0 = 1.10998, over by 2.2%). The divergence is also GEOMETRIC
    (ratio -> |z|/q), not factorial, so Borel resummation is the wrong tool;
    analytic continuation is the right one and this is it in closed form.
    Bean `qou-cw27`.
    """
    if q_inv is None:
        q_inv = mpf(1) / q
    if z_val >= 0:
        raise ValueError(
            f"li_2_q_negative_continuation is for z < 0 (got {z_val}); for "
            f"z >= q the continuation is complex, not real")
    if eps is None:
        eps = mpf(10) ** (5 - mp.dps)
    h = q - q_inv
    total = mpf(0)
    q_pow = q_inv           # q^{-1-2m} at m = 0
    q_step = q_inv * q_inv  # multiply by q^{-2} each step
    for _ in range(max_m):
        term = mp.log(1 - z_val * q_pow)   # 1 - z·q^{..} > 1 since z < 0
        total = total + term
        if mp.fabs(term) < eps:
            break
        q_pow = q_pow * q_step
    return -h * total


def _markov_z(q):
    """Canonical convention-D Markov parameter, via the single definition.

    Deliberately NOT respelled inline as `q**3/(q**2+1)`. An inline copy is a
    second definition that a future convention audit has to find by its SHAPE,
    and shape-keyed detectors are exactly what missed the value-literal and
    return-form C sites on this branch — including site A below, which was a
    `return` expression and therefore invisible to an assignment-keyed scan.

    Imported inside the function, mirroring closed_form_tau_M's own idiom, so
    no module-level import cycle is introduced.
    """
    from closed_form_tau_M import markov_z
    return markov_z(q)


def load_q_50dps(
    path: Path | None = None,
    anchor: str = "proton",
) -> tuple[mpf, mpf, mpf]:
    """Load q_0, q_0^{-1}, and the Markov parameter z at full ``mp.dps``.

    `z` is CONVENTION D, `q**3/(q**2+1)`, via `_markov_z` -> the single
    definition in `closed_form_tau_M`. This line previously advertised
    `z = 1/(q^{1/2}+q^{-1/2})`, which is convention C and has not been
    what the function returns since the excision. A stale convention
    claim in a docstring is worse than none on a loader with ~33
    importers: a reader checking the contract here would conclude they
    were handed C. Corrected 2026-08-29 (qou-cds3).

    Returns ``(q, q_inv, z)``.  Shared by every script that ingests
    per-generator Wedderburn volumes — centralized per gemini #687.

    Resolution order:

    ``path``    an explicit witness file — wins over ``anchor``, for a
                caller that must read one particular pinning witness.
    ``anchor``  ``"proton"`` (default) takes the experimental pin from
                ``q_parameter.Q_MP``; ``"muon"`` reads the ideal/CAL-2
                pin from ``q-pinning-50-digit.witness.json``.

    The default was ``None`` -> the muon witness until 2026-08-22.  That
    made the ideal pin reachable without naming it: a caller writing
    ``load_q_50dps()`` got muon while the 2026-08-07 owner directive says
    compute defaults to proton, and with no signal that a layer boundary
    had been crossed.  Measured at the time: 28 live no-arg call sites in
    26 files, of which **nine were declared ``physical_proton``** in
    ``q0_anchor_manifest.json`` and emitting witnesses stamped ``proton``
    while carrying muon data — and **zero** were declared ``ideal_muon``.
    So no caller wanted the old default.  Beans ``qou-dkm2`` / ``qou-v90i``.

    A muon-layer caller must now say ``anchor="muon"``, which is the
    point: the ideal layer stays reachable but has to be asked for.
    """
    if path is None:
        if anchor == "proton":
            # `q_parameter` lives in computations/substrate/.  This module
            # sets up no path bridge of its own, and a caller need not have
            # one either, so resolve it relative to this file rather than
            # relying on the caller's sys.path.
            try:
                from q_parameter import Q_MP
            except ModuleNotFoundError:  # pragma: no cover - path setup
                import sys as _sys
                _sub = str(Path(__file__).resolve().parent / "substrate")
                if _sub not in _sys.path:
                    _sys.path.insert(0, _sub)
                from q_parameter import Q_MP
            q = Q_MP
            qi = mpf(1) / q
            return q, qi, _markov_z(q)
        if anchor != "muon":
            raise ValueError(
                f"load_q_50dps: anchor must be 'proton' or 'muon', got {anchor!r}"
            )
        path = _Q_WITNESS_DEFAULT
    with path.open() as fh:
        d = _json.load(fh)
    q = mpf(d["derived_50_digit"]["q"])
    qi = mpf(1) / q
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1) = 0.6126880.  Was z_C = 1/(sqrt q + sqrt(1/q))
    #   = sqrt(q)/(q+1) = 0.4993203, excised.
    z = _markov_z(q)
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

    Exact for a SYMBOLIC `q` as well as an `mpf` one. The reciprocal is
    ``1 / q``, not ``mpf(1) / q``: for an mpf argument the two are identical
    (mpmath promotes the int exactly), but for a sympy `q` the latter drags
    `mpf(1)` in as a `Float(1.0)` and the whole expression inherits float
    contagion — `(q**2 - 1)*(-6*q**4 + (q - 1)**2*(q**4 - 1.0))/(12*q**5)`
    instead of a rational function. That matters because this is the closed
    form q-symbolic callers pass as `d_for_ctype(..., delta=...)` precisely to
    avoid a pinned constant; returning one with a `Float` in it defeats half
    the point.
    """
    qi = 1 / q if q_inv is None else q_inv
    return (q - 1) ** 2 * (1 - qi ** 4) / 3


def flavor_split_subleading(q: mpf, q_inv: mpf | None = None) -> mpf:
    """Δm / M_N with the (1+ℏ_q³) "3-loop substrate-Planck" correction.

    ⚠ POSITED — NOT DERIVED (audit 2026-06-29). The `(1+ℏ_q³)` multiplier
    has no derivation (no content block, Lean, or witness derives it — only
    this docstring label). It is also INSUFFICIENT: the correction CODATA
    demands is C_true = (Δm/M_N)_CODATA / leading = 1.0012784, whereas
    (1+ℏ_q³) = 1.0009727 — it supplies only 76% of the gap
    ((C_true−1)/ℏ_q³ = 1.314). So it is a partial shape-fix, not the closure,
    and must NOT be cited as backed by `prop:flavor-split-substrate` (which
    proves ONLY the leading `flavor_split_leading`).

    The genuine subleading correction should be DERIVED from the 3-strand /
    3-quark (spectator) categorical structure (open Archimedean-mass-functor
    R&D), not as an ℏ_q-power fit. See
    docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md.

    Until that derivation lands, treat this as `posited`, not `canonical`.
    """
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
# `per_knot_density_borromean` wrapper when the full VolDensity evaluation is
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

    Status: PROBE, NOT WIRED into production `per_knot_density_borromean`.
    Use via `per_knot_density_borromean_bring_color_weighted(Z, N, q)`.
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


def per_knot_density_borromean_bring_color_weighted(
    Z: int, N: int, q: mpf, q_inv: mpf | None = None,
) -> mpf:
    """Bring-color-tube extension of per_knot_density_borromean for atom (Z, N).

    [PROBE — parallels `per_knot_density_borromean` but uses the per-atom
    Bring-color-tube linking_weight instead of the H_4 Wedderburn
    average.]

    m(K) = m_e · VolDensity_bring(Z, N, q₀)

    Status: PROBE.  NOT wired into production mass computation;
    the existing `per_knot_density_borromean` (H_4 average, acknowledged
    CAL-4) remains in production until a categorical Bring-color-tube
    formulation is found that closes the +2.89% m_avg gap.
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    hbar_q = 1 - qi
    vol_b3 = 8 * mp.catalan
    geom_leading = vol_b3 / hbar_q ** 2
    return geom_leading * bring_color_weighted_linking_weight(Z, N, q, qi)


def per_knot_density_borromean(q: mpf, q_inv: mpf | None = None) -> mpf:
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
    Use `per_knot_density_per_block(vol_K, tr_M_K, q, ...)` for the
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

    ⚠ DEPRECATED FOR ABSOLUTE NUCLEON/ATOM MASS (owner ruling 2026-06-24):
    this is the λ_A fit (→ m_p ≈ 966, +2.96%). Route absolute mass through the
    `canonical_mass` facade (muon-anchored Hecke energy → 938.27). See
    docs/canonical-mass-formula-guardrail.md.
    """
    import warnings as _warnings
    _warnings.warn(
        "per_knot_density_borromean is the λ_A fit (Vol(𝓑₃)·ρ_global/ℏ_q² → 966 MeV) "
        "— NOT the canonical absolute nucleon mass. Use the canonical_mass "
        "facade (muon-anchored Hecke energy). See "
        "docs/canonical-mass-formula-guardrail.md.",
        DeprecationWarning,
        stacklevel=2,
    )
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
    # via the explicitly-exploratory per_knot_density_borromean_spectral().
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


def per_knot_density_per_block(
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
    `per_knot_density_borromean` shortcut DROPPED and replaced with a global
    H₄ scalar.

    The mass is then `m(K) = m_e · per_knot_density_per_block(...)`.

    Arguments
    ---------
    vol_K   : hyperbolic volume Vol(K) of the knot complement
              (8·G for the Borromean rings, Adams 1985).
    tr_M_K  : the per-block Markov trace Σ_λ w_λ χ_λ/dim λ at q,
              loaded from the canonical chi-cache witness
              (`chi-{atom}-h{n}-at-q0-50dps.witness.json`) or computed
              via `canonical_tr_m_via_chi_cache.canonical_tr_m`.
    q, q_inv: substrate parameter and its inverse.

    Per AGENTS.md production-vs-exploratory discipline: this is a
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


def per_knot_density_borromean_spectral(q: mpf, q_inv: mpf | None = None) -> mpf:
    """EXPLORATORY (not production): proved Family-A vol_density × the
    UNPROVED spectral-phase correction. m_e × this = m_avg ≈ 938.15 MeV
    (−819 ppm vs CODATA m_avg) — a no-fit ~35× improvement over the bare
    +2.89 %, but the correction is not proved (trivial Lean stub) and the
    sinh(θ) refinement is an open lead, so this must NOT feed production.
    Production uses per_knot_density_borromean (proved Family A, +2.89 %).
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    return per_knot_density_borromean(q, qi) * spectral_correction_borromean(q, qi)


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
    """Borromean braid (σ₁σ₂⁻¹)³ trace in the **jones** normalisation —
    the ALTERNATIVE-normalisation comparison column, kept deliberately.

    Via the Jones polynomial of the Borromean rings:
        V(t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³
    at t = q², divided by the loop value `q + 2 + q⁻¹`.

    ── which normalisation this is, and why it is NOT migrated ──────

    `q + 2 + q⁻¹ = (q^{1/2} + q^{-1/2})² = 1/z_C²` — the square of the
    **convention-C** loop value, since `z_C = 1/(√q + 1/√q)`.  It is a
    loop value raised to `n−1 = 2` (Markov closure of a 3-strand braid),
    NOT a dimension count: the `4` it tends to at `q = 1` is `δ(1)²`, and
    EVERY candidate normaliser below equals 4 there, so that limit
    distinguishes nothing.

    It is nevertheless **left exactly as it is**, because this function's
    job IS to be the non-canonical column.  The canonical (**wenzl**)
    normaliser for this object is `[2]_q² = q² + 2 + q⁻²`, carried by
    `markov_trace_for_knot` and by Lean `QOU.BraidsAndKnots.trM_borromean`
    (`= (4 + h² − 3h⁴ − h⁶)/(h² + 4)`, sorry-free).  Two audits display
    the two side by side; overwriting this one would delete the
    comparison it exists to make.  Measured at q₀ (70 dps):

        normaliser                          value      trace
        q + 2 + q⁻¹   (jones, here)    4.0108969   1.0067304534877074
        [2]_q² = q²+2+q⁻² (wenzl)      4.0437062   0.99856216383678727
        1/z_D² = (q²+1)²/q⁶             2.6639201   1.5157706817416908

    The `√q` spelling was removed (2026-08-25): `q + 2 + q⁻¹` is the same
    number to the last bit (difference exactly 0.0 at 70 dps), so no
    committed value moves, and no half-integer power of `q` is left in
    this module for the next convention detector to re-flag.

    ── the (3/16) × 4 = 3/4 claim: REFUTED, retained as the datum ───

    Taylor at q = 1 (h = q − q⁻¹), exact:
        this (jones)  : 1 + (3/16)h² − (97/128)h⁴ − (829/4096)h⁶
        wenzl / Lean  : 1 + 0·h²      − (3/4)h⁴    − (1/16)h⁶

    An earlier version of this docstring read the h² match
    `(3/16) × 4 = 3/4` as "establishing that Family A's
    λ_A = 5/2 + (3/4)·h² IS the Borromean braid trace".  **That claim is
    false and is withdrawn.**  It is an artefact of this normalisation:
    under the canonical `[2]_q²` the h² coefficient is exactly 0, and
    `QOU.BraidsAndKnots.family_a_h_minus_bridge_explicit` proves the gap
    `λ_A − bridge = (3/4)h² + (12h⁴ + 4h⁶)/(h² + 4)`, strictly positive
    for every h ≠ 0 (`family_a_h_minus_bridge_pos`).  The factor also
    fails at h⁰ (5/2, not 4) and at h⁴ (production terminates, this does
    not) — a one-coefficient coincidence, not a renormalisation.

    Scope: this is a **scope-(a)** negative about the bridge claim — the
    two objects do not agree — not a claim that either object is wrong.

    Refs:
      - `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanMarkovTrace.lean`
      - `docs/audits/2026-06-01-vol-density-compute-vs-paper-audit.md` §1
      - `docs/audits/2026-06-01-vol-density-derivation-trace.md` (FITTED row)
      - `computations/audits/per_knot_density_compute_vs_paper_audit.py`
        (`paper_J_borromean_jones_norm`, the same expression inline)
      - `yekutieli_borromean_h2_extraction.py` (empirical computation)
    """
    qi = mpf(1) / q if q_inv is None else q_inv
    t = q ** 2
    ti = qi ** 2
    jones = -ti**3 + 3*ti**2 - 2*ti + 4 - 2*t + 3*t**2 - t**3
    # Convention-C loop value squared, (√q + 1/√q)², written without the
    # half-power. Deliberate: see the docstring — this is the alternative
    # normalisation, and the canonical one is [2]_q² = q² + 2 + q⁻².
    norm = q + 2 + qi
    return jones / norm


# ---------------------------------------------------------------------------
# `per_knot_density_*` aliases — a half-applied rename, repaired
#
# Commit a4d9906659 migrated the terminology "VolDensity" -> "PerKnotDensity"
# across CALLERS but never renamed the functions here. The result: four
# modules on `main` raise ImportError at import time and cannot run at all.
#
#     computations/mass_per_knot_density.py                  (both names)
#     computations/per_knot_density_per_block_wiring.py       (both names)
#     computations/per_knot_density_deuteron_perknot_probe.py (per_block)
#     computations/probes/per_knot_density_borromean_q_locality_probe.py
#
# Aliasing rather than renaming is deliberate. 71 call sites still use the
# `vol_density_*` spelling, so flipping which name is canonical is a churn
# with a real chance of a partial second pass -- i.e. exactly the failure
# being repaired. These two lines un-break all four modules, change no
# number, and prejudge nothing about which spelling should win.
#
# There is no behavioural difference: the alias IS the function object.
# ---------------------------------------------------------------------------
# Back-compat aliases, OLD -> NEW. Owner ruling 2026-08-22: `per_knot_density_*`
# is the canonical spelling. These keep the 170-odd historical call sites and
# any out-of-tree caller working; they are the deprecated direction now.
vol_density_per_block = per_knot_density_per_block
vol_density_borromean = per_knot_density_borromean
vol_density_borromean_spectral = per_knot_density_borromean_spectral
vol_density_borromean_bring_color_weighted = per_knot_density_borromean_bring_color_weighted


# ── self-test ──────────────────────────────────────────────────
#
# The docstring above has long referenced `--self-test`, but no entry point
# existed: `python3 _li_2_q_util.py --self-test` imported the module, did
# nothing, and exited 0 — so the claim "verified against li_2_q" was never
# actually being checked by anything. It is now, and it matters more than it
# did, because `li_2_q` dispatches between two DIFFERENT algorithms at
# |z| = 1/q. This pins them together across that boundary.

def _self_test() -> int:
    """Series and q-product must agree to full precision, especially at 1/q."""
    # `_precision` lives in computations/substrate/ in the source layout and
    # flat beside this file in the vendored one. Resolve it here rather than at
    # module scope: this is a LIBRARY module, and the vendor sync strips
    # `import _path_bridge`, so a module-scope bare import would break the
    # shipped copy (exactly the regression the qou-fl9i sweep hit).
    try:
        from _precision import COMPUTE_DPS
    except ModuleNotFoundError:
        import sys as _s2
        _s2.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
        from _precision import COMPUTE_DPS
    mp.dps = COMPUTE_DPS
    q, q_inv, _z = load_q_50dps()
    eps = mpf(10) ** (5 - mp.dps)

    def pure_series(z):
        """The series with NO dispatch — the reference implementation."""
        tot = mpf(0)
        z_pow = mpf(1)
        for n in range(1, 50_000):
            z_pow = z_pow * z
            term = z_pow / (mpf(n) * _q_int(n, q, q_inv))
            tot = tot + term
            if mp.fabs(term) < eps:
                return tot
        raise RuntimeError(f"reference series did not converge at z={z}")

    # straddle the |z| = 1/q dispatch boundary deliberately
    cases = ["-0.5", "-0.9", "-0.90091", "-0.90092", "-0.91", "-1", "-1.05",
             "-1.08837"]
    worst = mpf(0)
    fails = 0
    print(f"Li_2^q self-test at dps={mp.dps}, dispatch threshold 1/q="
          f"{mp.nstr(q_inv, 10)}")
    for c in cases:
        z = mpf(c)
        got = li_2_q(z, q, q_inv)
        ref = pure_series(z)
        rel = mp.fabs(got - ref) / mp.fabs(ref) if ref else mp.fabs(got - ref)
        worst = max(worst, rel)
        path = "closed" if mp.fabs(z) >= q_inv else "series"
        ok = rel < mpf(10) ** (10 - mp.dps)
        fails += not ok
        print(f"  z={c:>10}  path={path:>6}  rel={mp.nstr(rel, 4):>12}  "
              f"{'ok' if ok else 'FAIL'}")
    print(f"worst relative disagreement: {mp.nstr(worst, 4)}")
    return 1 if fails else 0


if __name__ == "__main__":
    import sys as _s
    if "--self-test" in _s.argv:
        _s.exit(_self_test())
    print("usage: python3 _li_2_q_util.py --self-test")
