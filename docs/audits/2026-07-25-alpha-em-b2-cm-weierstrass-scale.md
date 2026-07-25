# α_EM B2 τ-scale — CM/Weierstrass route (bean qou-m117): CM refuted, gate certified, scale gate narrowed to a discrete set

**Date:** 2026-07-25 · **Bean:** `qou-m117` (parent epic `qou-k42c`) · **Axis:** α_EM
per-loop measure, the B2 τ-identification's scalar `c` (τ-scale) ·
**Discipline:** standing 2026-07-19 owner ruling respected — the per-loop
identification is NOT derived-proved; no fit; nothing wired; no
`TauRhoHodgeLift` instance; `1/(8π)` stays phase-4. Route C's refutation
([`alpha-em-b2-invariant-c.witness.json`](../../computations/alpha-em-b2-invariant-c.witness.json))
stands untouched.

**Probe:** [`computations/alpha_em/alpha_em_b2_cm_weierstrass_scale_probe.py`](../../computations/alpha_em/alpha_em_b2_cm_weierstrass_scale_probe.py)
· **Witness:** [`alpha-em-b2-cm-weierstrass-scale.witness.json`](../../computations/alpha_em/alpha-em-b2-cm-weierstrass-scale.witness.json)
(7/7, mpmath 50 dps + 10 guard, certification tolerance 1e-45).

## 1. The bean's premise, and the immediate structural point (W1)

The bean proposed bypassing the Braden–Northover normalization convention "via CM
theory": if the Bring elliptic factors were CM curves, their periods would carry an
absolute arithmetic normalization independent of any period-matrix convention.

**The literal CM leg dies instantly.** The corpus j-invariants
(Braden–Disney-Hogg, conductor-50 ℚ-isogeny class 50a; recorded in the
[`BringEllipticFactor.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringEllipticFactor.lean)
docstring) are

$$j(\tau_0) = -\tfrac{121945}{32}, \qquad j(5\tau_0) = -\tfrac{25}{2},$$

both **non-integral rationals**. A CM elliptic curve's j-invariant is an
**algebraic integer** (classical CM theory — the j of a CM point is integral and
generates the ring class field). Denominators 32 and 2 ≠ 1 ⇒ **neither factor has
CM**. Scope-(a) recording: this kills the CM *mechanism as-stated*, not the
convention-bypass *goal* — which survives via the ℚ-model leg below. (It is a
scope-limited negative, not a structural exclusion of anything else; the invariant
cited — CM ⇒ integral j — is the classical theorem, so the CM-leg closure itself
is a proved exclusion of *CM on these two curves*.)

## 2. What survives and works: the ℚ-model / Weierstrass leg (W2–W4)

The curves are ℚ-curves in class 50a with ℚ-rational Weierstrass models; period
**ratios** (lattice shape) are twist-independent, so the scale-free content is
recoverable from `j` alone, with zero period-matrix input:

- **W2 — exact ℚ-models.** The standard j-parametrized model
  `E_j : y² + xy = x³ − 36/(j−1728)·x − 1/(j−1728)` built in exact `Fraction`
  arithmetic for both j's; `c₄³/Δ == j` round-trips **exactly**. Both have
  `Δ < 0` (rhombic lattice — consistent with `Re τ = −1/2`).
- **W4a — j-inversion at 50 dps.** Inverting `1728·kleinj` on the boundary line
  `Re τ = −1/2` (where real `j < 0` lives):
  `τ_A^fund = −1/2 + 1.33921543563536042951730502885…·i` (`j = −121945/32`),
  `τ_B^fund = −1/2 + 0.933382312314049616030814406816…·i` (`j = −25/2`);
  residuals ~1e-58.
- **W3 — AGM periods from the models.** The period lattice of each ℚ-model
  computed by AGM from the Weierstrass cubic's roots, reduced to the SL₂(ℤ)
  fundamental domain, self-certified by j round-trip: **agrees with the
  j-inversion route to < 1e-45** (measured 0 at working precision). This is the
  "period ratio from the Weierstrass model, documented independent of the
  Braden–Northover normalization" deliverable.
- **W4b — τ₀ recovered at 50 dps by an exact SL₂(ℤ) word.** Reducing the
  literature τ₀ to the fundamental domain fixes the word
  `γ′ = [[1,1],[−2,−1]]` with `γ′(τ₀) = τ_A^fund`, giving the closed form

  $$\tau_0 = -\tfrac12 + \frac{i}{4\,\mathrm{Im}\,\tau_A^{\mathrm{fund}}}
    = -0.5 + 0.186676462462809923206162881363\ldots i,$$

  matching the corpus literature `−0.5 + 0.186676·i` to the quoted 6 digits
  (|diff| = 4.6e-7), with `Re τ₀ = −1/2` exact by the word structure.

## 3. The (1,5,5,5) gate self-certified (W5)

- `reduce(5·τ₀_recovered) = τ_B^fund` to **7.8e-62** — the X₀(5) 5-isogeny and
  the Braden–Disney-Hogg j-labelling (`j(τ₀) = −121945/32`, `j(5τ₀) = −25/2`)
  confirmed from j-inversion alone.
- `Im(τ_B^fund)/Im(τ₀) = 4·t_A·t_B = 5` **exactly at 50 dps** — the
  (1,5,5,5) gate's ratio-5 is the isogeny degree, certified **independently of
  the Braden–Northover period matrix** (which was never consumed by the probe).

## 4. The honest τ-scale finding (W6) — what this does and does NOT fix

- **Fixed:** each elliptic factor now has a canonical per-curve normalization
  (ℚ-model / Néron differential); the lattice **shape** data (τ₀, the 5-isogeny,
  the ratio 5) is convention-free and machine-certified.
- **NOT fixed:** the absolute Hodge scale on `H^{1,0}(Bring)` still passes
  through the isogeny `Jac(Bring) → E_{5τ₀}³ × E_{τ₀}` with **unknown pullback
  degree**. Under Néron normalization the remaining freedom is **discrete**: an
  isogeny pullback `φ*` scales the induced form by `deg(φ) ∈ ℤ_{>0}` (natural
  support: powers of 5, given the conductor-50 / X₀(5) structure). The τ-scale
  gate narrows from a continuous unknown to that discrete set. This does not
  close route C's refutation — no single convention-free scalar `c` exists —
  it constrains which *discrete* rescalings a legitimate τ-identification could
  introduce.

## 5. The deg² = 25 observation (W7) — scope-(a), OPEN, owner-level

The landed route-C witness records the canonical geometric-mean representative
`c_geo = 0.9947074314…` with `c_geo/(1/(8π)) = 24.9997244717`. The measured
τ-scale gate ratio **24.9997244717 is within 1.1e-5 (relative) of
25 = deg(5-isogeny)² = 5²** — the square of exactly the X₀(5) degree certified
in §3. **Recorded as a candidate discrete origin for the scale — OPEN,
owner-level, NO identification, no tuning**, and **double-gated**:

1. **Normalization-carrying.** Route C proved the ratio depends on the
   entry-`[0,0] = 1` convention used to normalize both Grams; "25" is a
   candidate only if that convention is the natural one — itself an open
   question.
2. **Observation, not derivation.** Even granting the convention, a 1.1e-5
   near-match of a discrete integer is an observation to be adjudicated, not a
   wire-able result. The residual is reported as-is.

## 6. Status table

| item | status |
|---|---|
| CM on either 50a factor | **excluded** (proved: non-integral j vs CM-integrality) |
| ℚ-model exact `j` round-trip (both curves) | certified (exact `Fraction`) |
| AGM periods ≡ j-inversion (both curves) | certified (< 1e-45; residuals ~1e-58) |
| τ₀ = −1/2 + i/(4·Im τ_A^fund), corpus match | certified (6-digit literature match) |
| X₀(5) 5-isogeny + (1,5,5,5) Im-ratio = 5 | certified at 50 dps, B–N-independent |
| τ-scale gate | **narrowed to discrete isogeny-degree set** (still OPEN) |
| ratio 24.9997 ≈ 25 = deg² | **observation, OPEN, owner-level, double-gated** |
| τ-identification / scalar `c` / `1/(8π)` | **unchanged: OPEN / phase-4** (2026-07-19 ruling) |

## Cross-references

- Attack plan: [`2026-07-24-alpha-em-b2-tau-identification-attack-options.md`](2026-07-24-alpha-em-b2-tau-identification-attack-options.md)
- Consolidation: [`2026-07-25-alpha-em-b2-tau-id-consolidation.md`](2026-07-25-alpha-em-b2-tau-id-consolidation.md)
- Route-C refutation (input): [`../../computations/alpha_em_b2_invariant_c_probe.py`](../../computations/alpha_em_b2_invariant_c_probe.py)
- Corpus facts: [`BringEllipticFactor.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringEllipticFactor.lean) (j-values, τ₀, 50a, X₀(5))
- Ruling (read-first): [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
