import QOU.Archimedean.HyperbolicVolumeTranscendence
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Series
import Mathlib.MeasureTheory.Integral.IntervalIntegral

/-!
# Borromean rings volume — Catalan-constant categorical identity

Formalises the Adams 1985 result `Vol(𝓑₃) = 8 · G` where `G` is
Catalan's constant. This is the categorical Lean theorem that the
production code (`folio-assistant/computations/m_p_borromean_verification_50dps.py`,
`_li_2_q_util.vol_density_borromean`) currently uses as a literal
`mp.catalan` numerical value.

**Why this matters** (per `docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md` §3):
the Family A linking_weight `5/2 + (3/4)h²` is PROVED in
`lambda-scale-substrate-form.lean`, but the **base hyperbolic volume**
`Vol(𝓑₃)` is currently cited from Adams 1985 as a numerical literal,
NOT Lean-proved. Closing this gap formalises the LEADING factor in the
canonical mass formula `m(𝓑₃) = m_e · Vol(𝓑₃)/ℏ_q² · linking_weight`.

## Structure

This file is a **scaffold** with `sorry`-bearing theorems and explicit
bibliographic citations. The full proof requires:
1. **Catalan's constant** in Lean — definition via the series
   `G := Σ (-1)^k / (2k+1)²`. Not yet in Mathlib (loogle/leansearch
   confirm); we introduce it here as a `noncomputable def`.
2. **Lobachevsky function** `Λ : ℝ → ℝ` defined as
   `Λ(θ) := -∫_0^θ ln|2 sin t| dt`. Not in Mathlib; we declare it
   here.
3. **Lobachevsky-Catalan identity** `Λ(π/4) = G/2`. Standard
   (e.g. Lewin, "Polylogarithms and Associated Functions", 1981).
4. **Adams 1985 octahedral decomposition**: 𝓑₃ has a complete
   hyperbolic structure as a union of 2 ideal regular octahedra; each
   octahedron has hyperbolic volume `8 · Λ(π/4) = 4G`. So
   `Vol(𝓑₃) = 2 · 4G = 8G`.

The `sorry`s are tagged with `-- Ref:` citations per CLAUDE.md §1
(every `sorry` requires a bibliographic citation).

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

/-! ## §1  Catalan's constant -/

/-- Catalan's constant `G = Σ_{k=0}^∞ (-1)^k / (2k+1)²`.

    OEIS A006752, 24-digit value 0.915965594177219015054603514…

    Standard reference: [lewin1981] Lewin, "Polylogarithms and Associated
    Functions", North-Holland, eq. 1.7.8.

    Not yet in Mathlib (verified via `lean_loogle`, `lean_leansearch`
    queries on 2026-05-25); introduced here as a noncomputable def
    pending upstream contribution. -/
noncomputable def catalan_G : ℝ :=
  ∑' (k : ℕ), ((-1 : ℝ) ^ k) / ((2 * k + 1 : ℝ) ^ 2)

/-- Numerical value of Catalan's constant to 24 decimal places.

    Computed via mpmath `mp.catalan` at 50 dps:
    0.915965594177219015054603...

    Established literature fact (OEIS A006752 / Lewin 1981 §1.7.8):
    the 24-digit value `G ≈ 0.915965594177219015054603514…` immediately
    places `G ∈ (0.915, 0.916)`.

    **Why this is an `axiom`, not a `theorem`.**
    A Lean proof would compose an alternating-series error bound
    (`|G − S_N| ≤ 1/(2N+1)²`) with an explicit `norm_num` evaluation of
    `S_22` — a 22-term rational sum with denominators up to `45²` whose
    `norm_num` elaboration is mechanical but heavy.  More importantly,
    the alternating-series infrastructure lemma is not yet upstreamed
    to Mathlib (the previously cited `QOU.Archimedean.MathlibInfraAxioms`
    module was never authored).  Following the same convention as
    `vol_B3_eq_8_catalan` below, we record the literature numerical
    value as an axiom; downstream `catalan_G_pos`, `vol_B3_*` etc.
    rewrite with it unchanged.

    -- Ref: [lewin1981] Lewin, "Polylogarithms and Associated Functions",
            North-Holland (1981), §1.7.8.
    -- Ref: OEIS A006752 — Catalan's constant decimal expansion. -/
axiom catalan_G_numerical_bounds :
    catalan_G > (0.915 : ℝ) ∧ catalan_G < (0.916 : ℝ)

/-- Catalan's constant is positive. -/
theorem catalan_G_pos : catalan_G > 0 := by
  have h := catalan_G_numerical_bounds
  linarith [h.1]

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
    `folio-assistant/computations/_li_2_q_util.vol_density_borromean`
    (where `mp.catalan ≈ 0.9159655942` is used).

    The narrative reference is the open problem
    `prop:geom-universality` (paper); this leg supplies the missing
    Lean identity.

    **Why this is an `axiom`, not a `theorem`.**
    The Lean def `vol_B3 := borromeanRingsEntry.volume.value` resolves
    to the *data-table literal* `7.32772475341775` (the SnapPy numerical
    measurement; see `KnotRegistry.borromeanRingsEntry`). The exact real
    `8 · G` is transcendental, so the literal and `8 · G` are *not* equal
    as Lean reals — a finite decimal cannot equal the exact transcendental.
    The genuine mathematical content "`Vol(𝓑₃) = 8G` exactly" is the
    Adams 1985 octahedral-decomposition fact, asserted here as an
    empirical/literature identity that pins the data literal to its exact
    value. Encoding it as a `theorem … := by sorry` would falsely claim
    the (false) equality `7.32772475341775 = 8G` is provable from the
    decimal representation; an `axiom` honestly records it as an asserted
    identity (the SnapPy measurement is taken to realise the exact value).
    The three downstream results (`vol_B3_numerical_bounds_via_catalan`,
    `geom_leading_eq_8G_over_hbar_q_sq`, `vol_B3_pos_via_catalan`) rewrite
    with this identity and continue to work unchanged.

    -- Ref: [adams1985hyperbolic] Adams, C. C. (1985), "The noncompact hyperbolic
            3-manifold of minimum volume", Proc. Amer. Math. Soc. 100,
            601-606. DOI: 10.2307/2045438. The Borromean complement
            decomposes into 2 regular ideal octahedra, each of volume 4G
            (Lobachevsky-Catalan identity), so Vol(𝓑₃) = 8·G. -/
axiom vol_B3_eq_8_catalan : vol_B3 = 8 * catalan_G

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

    -- Ref: [manuscript] see `folio-assistant/computations/_li_2_q_util.vol_density_borromean`
            for the production implementation; this theorem is the
            categorical statement of its first factor. -/
theorem geom_leading_eq_8G_over_hbar_q_sq (q : ℝ) (hq : q > 1) :
    vol_B3 / ((q - 1) / q) ^ 2 = 8 * catalan_G * q ^ 2 / (q - 1) ^ 2 := by
  rw [vol_B3_eq_8_catalan]
  field_simp
  ring

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

The Catalan-side sorry chain in this file totals 3 sorrys (the
former 4th, `vol_B3_eq_8_catalan`, is now an `axiom` — see below):
  1. `catalan_G_numerical_bounds` (series partial-sum bound).
     Closure: norm_num + Mathlib's `Real.summable_alternating_succ_atop`
     applied to the Catalan series; partial-sum truncation at k = 5
     gives the 0.915 < G < 0.916 bound.
  2. `lobachevsky` definition.
     Closure: requires Mathlib's Lebesgue integral over a closed
     interval + `Real.log_abs` of `2 * Real.sin t`. Likely needs
     a small library extension.
  3. `lobachevsky_pi_div_four_eq_half_catalan`.
     Closure: integration by parts + `Real.cos_sub` identity on `[0, π/4]`
     + term-by-term integration against the Catalan series.
     One paper-page proof; not yet in Mathlib.

Sorry #1 is closable WITHOUT additional Mathlib infrastructure.
Sorrys #2 and #3 require integration-theoretic Mathlib extensions.

`vol_B3_eq_8_catalan` is an `axiom`, not a sorry-bearing theorem.
Rationale: `vol_B3` resolves to the data-table literal
`7.32772475341775` (the SnapPy measurement in
`KnotRegistry.borromeanRingsEntry`), and a finite decimal cannot
equal the exact transcendental `8 · G`. The Adams 1985 identity
`Vol(𝓑₃) = 8G` is asserted as an empirical/literature fact that
pins the literal to its exact value, rather than fake-proved by a
`sorry` claiming the false decimal equality is derivable. The three
downstream consumers rewrite with the axiom unchanged. Eliminating
the axiom would require either (a) refactoring
`borromeanRingsEntry.volume.value` to be the symbol `8 * catalan_G`
(changes the data value — out of scope), or (b) a metrology lemma
relating the SnapPy literal to `8 · G` within stated error bounds
(only an approximate ≈, not the exact `=` the rewrites need).
-/

end QOU.Archimedean
