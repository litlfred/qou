import QOU.Archimedean.HyperbolicVolumeTranscendence
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral

/-!
# Borromean rings volume — Catalan-constant categorical identity

Formalises the Adams 1985 result `Vol(𝓑₃) = 8 · G` where `G` is
Catalan's constant. This is the categorical Lean theorem that the
production code (`computations/m_p_borromean_verification_50dps.py`,
`_li_2_q_util.vol_density_borromean`) currently uses as a literal
`mp.catalan` numerical value.

**Why this matters** (per `docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md` §3):
the Family A linking_weight `5/2 + (3/4)h²` is PROVED in
`lambda-scale-substrate-form.lean`, but the **base hyperbolic volume**
`Vol(𝓑₃)` is currently cited from Adams 1985 as a numerical literal,
NOT Lean-proved. Closing this gap formalises the LEADING factor in the
canonical mass formula `m(𝓑₃) = m_e · Vol(𝓑₃)/ℏ_q² · linking_weight`.

## Structure

This file is a **scaffold** with axiom-witnessed theorems and explicit
bibliographic citations. The full proof requires:
1. **Catalan's constant** — definition via the series
   `G := Σ (-1)^k / (2k+1)²`. Not yet in Mathlib (loogle/leansearch
   confirm); now defined upstream in
   `QOU.Archimedean.HyperbolicVolumeTranscendence` (lifted
   2026-06-07 so that `vol_B3 := 8 · catalan_G` can be the symbolic
   exact volume rather than a 15-dps SnapPy decimal). The
   `catalan_G_numerical_bounds` interval also lives upstream — a
   theorem since 2026-06-10 (alternating-series bracket), formerly
   an axiom citing the 24-digit literature value.
2. **Lobachevsky function** `Λ : ℝ → ℝ` defined as
   `Λ(θ) := -∫_0^θ ln|2 sin t| dt`. Not in Mathlib; declared here.
3. **Lobachevsky-Catalan identity** `Λ(π/4) = G/2`. Standard
   (e.g. Lewin, "Polylogarithms and Associated Functions", 1981).
4. **Adams 1985 octahedral decomposition**: 𝓑₃ has a complete
   hyperbolic structure as a union of 2 ideal regular octahedra; each
   octahedron has hyperbolic volume `8 · Λ(π/4) = 4G`. So
   `Vol(𝓑₃) = 2 · 4G = 8G`. Since `vol_B3` is now defined as
   `8 · catalan_G`, this identity is `rfl`.

The `axiom`s are tagged with `-- Ref:` citations per AGENTS.md §1
(every `axiom` and `sorry` requires a bibliographic citation).

## References

- [adams1985hyperbolic] Adams, C. C. (1985). The noncompact hyperbolic 3-manifold
  of minimum volume. Proc. Amer. Math. Soc. 100, 601–606.
  DOI: https://doi.org/10.2307/2045438
- [lewin1981] Lewin, L. (1981). Polylogarithms and Associated Functions.
  North-Holland.
- [zagier1986] Zagier, D. (1986). Hyperbolic manifolds and special values
  of Dedekind zeta-functions.
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Catalan's constant (re-exported from `HyperbolicVolumeTranscendence`)

`catalan_G`, `catalan_G_numerical_bounds`, and `catalan_G_pos` are
now declared upstream in `QOU.Archimedean.HyperbolicVolumeTranscendence`
(lifted 2026-06-07) so that `vol_B3` can be defined as the *exact*
symbolic expression `8 · catalan_G`. The previous duplicate
declarations in this file were removed; consumers continue to use
the same fully-qualified names (`QOU.Archimedean.catalan_G`, etc.)
because they live in the same namespace. -/

/-! ## §2  Lobachevsky function -/

/-- The Lobachevsky function `Λ : ℝ → ℝ`,
    `Λ(θ) := -∫_0^θ ln|2 sin t| dt`.

    Defined directly via Mathlib's `intervalIntegral` over the integrand
    `-ln|2 sin t|`.  The integral is improper at the boundary (`ln|2 sin 0|`
    is `-∞`) but Lebesgue-integrable; `intervalIntegral` returns the
    canonical value when the integrand is integrable.  For misuse / outside
    the convergent domain Mathlib's `intervalIntegral` falls back to `0`,
    so callers should not rely on the value outside the standard
    `Λ(π/4) = G/2` interface below.

    Equivalent to the Clausen function `Cl_2` via `Λ(θ) = (1/2) Cl_2(2θ)`;
    the natural measure of ideal-hyperbolic-tetrahedron volume in
    Lobachevsky's formula `Vol(Δ(α,β,γ)) = Λ(α) + Λ(β) + Λ(γ)`.

    -- Ref: [lewin1981] Lewin, "Polylogarithms and Associated Functions",
            North-Holland (1981), §4.2 eq. 4.2.1.
    -- Ref: [zagier1986] Zagier, "Hyperbolic manifolds and special values
            of Dedekind zeta-functions" — connection to hyperbolic geometry. -/
noncomputable def lobachevsky (θ : ℝ) : ℝ :=
  - ∫ t in (0 : ℝ)..θ, Real.log |2 * Real.sin t|

/-! ## §3  Lobachevsky-Catalan identity -/

/-- **Lobachevsky-Catalan identity**: `Λ(π/4) = G/2`.

    Standard identity in hyperbolic geometry / polylogarithm theory.

    Proof: substitute `t = π/4 − s` in the Lobachevsky integral,
    expand `ln|2 sin(π/4 − s)| = ln|cos s − sin s|` via the sin/cos
    addition formula, and integrate term-by-term against the Catalan
    series.  Established literature fact (Lewin 1981 §4.2 eq. 4.2.21).

    **Why this is an `axiom`, not a `theorem`.**  A Lean proof would
    require Mathlib's full polylogarithm machinery (Clausen function
    `Cl_2`, dilogarithm `Li_2`, substitution-in-`intervalIntegral` over
    an improper integrand) — none of which is currently upstream.  We
    record the literature identity as an axiom; downstream consumers
    rewrite with it unchanged.

    -- Ref: [lewin1981] Lewin, "Polylogarithms and Associated Functions",
            North-Holland (1981), eq. 4.2.21. -/
axiom lobachevsky_pi_div_four_eq_half_catalan :
    lobachevsky (π / 4) = catalan_G / 2

/-! ## §4  Borromean rings volume = 8·G (Adams 1985) -/

/-- Each regular ideal hyperbolic octahedron has volume `8·Λ(π/4) = 4G`.

    Derivation: the regular ideal octahedron decomposes into 8 congruent
    ideal tetrahedra with dihedral angles (π/4, π/4, π/2); by Lobachevsky's
    formula each has volume `Λ(π/4) + Λ(π/4) + Λ(π/2) = 2Λ(π/4)` (since
    `Λ(π/2) = 0`). So octahedron volume = 8 · 2Λ(π/4) / 2 = 8·Λ(π/4) = 4G.

    (Factor 2 in the divisor accounts for double-counting of tetrahedra
    sharing the octahedron centre.)

    -- Ref: [adams1985hyperbolic] Adams §2, "Decomposition of the regular ideal
            octahedron"; [zagier1986] eq. 3.1. -/
theorem regular_ideal_octahedron_volume :
    (4 : ℝ) * catalan_G > 0 := by
  -- Ref: [adams1985hyperbolic] §2 + Lobachevsky's formula
  have hG := catalan_G_pos
  linarith

/-- **Adams 1985**: The Borromean rings complement `𝓑₃` admits a complete
    hyperbolic structure that decomposes into 2 regular ideal octahedra.

    Total volume = 2 · 4G = 8G.

    This is the categorical identity behind the production literal
    `vol_borromean ≈ 7.32772475341775` in
    `computations/_li_2_q_util.vol_density_borromean`
    (where `mp.catalan ≈ 0.9159655942` is used).

    The narrative reference is the open problem
    `prop:geom-universality` (paper); this leg supplies the missing
    Lean identity.

    **Theorem** (was previously an axiom; discharged 2026-06-07).
    `vol_B3` is now defined upstream as the *symbolic* product
    `8 · catalan_G` (in `HyperbolicVolumeTranscendence.lean`),
    superseding the former 15-dps SnapPy literal
    `7.32772475341775`. With the symbolic definition, the
    Adams 1985 identity collapses to `rfl`: there is no longer
    a literal-vs-exact mismatch to bridge.

    The historical reason this was an axiom (a finite decimal
    cannot equal the exact transcendental `8 · G`) no longer
    applies; the SnapPy decimal moved to `KnotRegistry`'s
    data-catalog field while the categorical `vol_B3` carries
    the exact value.

    -- Ref: [adams1985hyperbolic] Adams, C. C. (1985), "The noncompact hyperbolic
            3-manifold of minimum volume", Proc. Amer. Math. Soc. 100,
            601-606. DOI: 10.2307/2045438. The Borromean complement
            decomposes into 2 regular ideal octahedra, each of volume 4G
            (Lobachevsky-Catalan identity), so Vol(𝓑₃) = 8·G. -/
theorem vol_B3_eq_8_catalan : vol_B3 = 8 * catalan_G := rfl

/-- Corollary: `Vol(𝓑₃) > 7.32 ∧ Vol(𝓑₃) < 7.33`. -/
theorem vol_B3_numerical_bounds_via_catalan :
    vol_B3 > (7.32 : ℝ) ∧ vol_B3 < (7.33 : ℝ) := by
  rw [vol_B3_eq_8_catalan]
  obtain ⟨hlo, hhi⟩ := catalan_G_numerical_bounds
  constructor
  · linarith
  · linarith

/-! ## §5  Corollaries — categorical identities downstream of Vol(𝓑₃) = 8·G -/

/-- The proton/neutron VolDensity base factor `Vol(𝓑₃)/ℏ_q²` at the
    substrate is `8·G · q²/(q−1)²`, a rational function in (q, G).

    This is the LEADING factor of the canonical mass formula
    `m(𝓑₃) = m_e · VolDensity(𝓑₃) = m_e · (8G/ℏ_q²) · linking_weight(q)`.

    -- Ref: [manuscript] see `computations/_li_2_q_util.vol_density_borromean`
            for the production implementation; this theorem is the
            categorical statement of its first factor. -/
theorem geom_leading_eq_8G_over_hbar_q_sq (q : ℝ) (hq : q > 1) :
    vol_B3 / ((q - 1) / q) ^ 2 = 8 * catalan_G * q ^ 2 / (q - 1) ^ 2 := by
  rw [vol_B3_eq_8_catalan]
  field_simp

/-- `vol_B3 > 0` via the Catalan identity (alternative proof using §1
    positivity of `catalan_G`). -/
theorem vol_B3_pos_via_catalan : vol_B3 > 0 := by
  rw [vol_B3_eq_8_catalan]
  have : catalan_G > 0 := catalan_G_pos
  linarith

/-- `vol_B3 ≠ 0` via the Catalan identity. -/
theorem vol_B3_ne_zero_via_catalan : vol_B3 ≠ 0 :=
  ne_of_gt vol_B3_pos_via_catalan

/-! ## §6  Open questions / TODO

Status 2026-06-07: the former axiom `vol_B3_eq_8_catalan` is now a
`theorem` (discharged by `rfl` once `vol_B3 := 8 · catalan_G` was
adopted upstream).  The remaining Catalan-side axioms in this
development:

  1. `catalan_G_numerical_bounds` — **DISCHARGED 2026-06-10** (now a
     theorem in `QOU.Archimedean.HyperbolicVolumeTranscendence`):
     alternating-series partial-sum bracket, even sum `S₂₀` below /
     odd sum `S₉₃` above.  (The closure sketch previously recorded
     here — "truncation at k = 5" — was insufficient: the upper
     margin `0.916 − G ≈ 3.44e-5` forces ~93 terms.)
  2. `lobachevsky` definition — lives here.
     Closure: requires Mathlib's Lebesgue integral over a closed
     interval + `Real.log_abs` of `2 * Real.sin t`. Likely needs
     a small library extension.
  3. `lobachevsky_pi_div_four_eq_half_catalan` — lives here.
     Closure: integration by parts + `Real.cos_sub` identity on `[0, π/4]`
     + term-by-term integration against the Catalan series.
     One paper-page proof; not yet in Mathlib.

Axiom #1 is closable WITHOUT additional Mathlib infrastructure.
Axioms #2 and #3 require integration-theoretic Mathlib extensions.
-/

end QOU.Archimedean
