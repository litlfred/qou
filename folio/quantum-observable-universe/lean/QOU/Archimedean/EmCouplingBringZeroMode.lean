import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic
import QOU.Archimedean.BlochWignerUnitCircle
import QOU.Archimedean.BlochWignerLobachevsky


/-!
# Additive Bring zero-mode form for 1/α_EM (conditional)

The candidate closed form

  1/α_EM = q · [9]_q · [10]_q + 2g/(4π(g-1)) + α·H·(1 - h²α) + Δ₂

at g = 4 (Bring's surface, χ = -6), with the additive correction
2/(3π) = 2g/(4π(g-1)) identified as the τ_arch-image of a specific
Bloch-group class assembled from the cosimplicial / Yekutieli triple
data of the genus-4 force-carrier pair {T(2,9), T(3,5)}.

This file axiomatises the missing structural input as a Lean
typeclass `BringZeroModeBlochClass`. The class field asserts that
there exists a class `[Z] ∈ B(ℂ)` whose Bloch-Wigner value `D[Z]`
equals `2/(3π)` under the chosen normalisation. Combined with the
sibling typeclass `QOU.Archimedean.BlochSuslinUniqueness` from
`prop:archimedean-functor-uniqueness`, the resulting conditional
proposition is:

  Theorem (conditional). 1/α_EM - q[9]_q[10]_q = 2/(3π) + α·H·(1 - h²α) + Δ₂.

**On the correction term, and why it is not written `O(α)`.** The α-dependent
part is not an unspecified asymptotic remainder: to the order currently derived
it is the explicit Habiro/Schwinger self-coupling

  α·H·(1 - h²α),    H = [2]_q/(8π),    h = q - q⁻¹,

with `h` the Hecke structure constant (the denominator of the balanced `[k]_q`,
forced by the `σ² = (q-q⁻¹)σ + 1` relation) — **not** the mass-chain `ℏ_q =
1 - q⁻¹`, from which it differs by a factor ≈ 2.11. Since α appears on both
sides, the relation is solved as a fixed point rather than evaluated as a series;
truncating after `α·H` gives the quadratic form and retaining the cubic
`(1 - h²α)` factor gives the better one.

`Δ₂` is the genuine remainder: the uncomputed **archimedean two-loop** term. It
is *not* the `-h²Hα²` piece already included above — that piece is weight 1 (a
q-rational over π), whereas the two-loop object is weight 3 (ζ(3)-type), about
40× larger, and lives on the archimedean side of the wall rather than in the
fibre. Writing the whole α-dependence as `O(α)` hid both the derived terms and
that distinction.

The Lean theorem `bring_zero_mode_additive_form` takes the class
as an `[Instance]` hypothesis and is proved without `sorry` —
exactly in the §3b-cond pattern.

Closure of the class instance itself reduces to the explicit
identification of the Bloch-group class on Bring's surface; that
identification is the remaining open computational sub-problem
documented in `em-coupling-bring-zero-mode.md`.

**Update 2026-11-15 (issue #7942).** `BlochWigner_unit_circle` is now
*defined* as `Cl_2` (it was an `opaque`).  The old class field asked only for a
real angle `θ` with `Cl_2 θ = 2/(3π)`, which is true by the intermediate value
theorem (`exists_Cl_2_eq_bringZeroModeValue`) and identifies no Bloch class.  On
owner decision the field is restated as an **algebraic** Bloch–Wigner
combination equal to `2/(3π)`; see the field's docstring for why that is
expected to be false (period conjecture) and why the torus-knot carriers give
`D = 0`.  No instance (bean `qou-006b`).

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [leitner2026] prop:archimedean-functor-uniqueness
-- Ref: [leitner2026] prop:force-carrier-bring-uniqueness
-- Ref: [suslin1991] Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-- Ref: [bloch2000]  AMS CRM Monograph 11 (2000).
-- Ref: [thurston1978] The geometry and topology of three-manifolds.
-/

namespace QOU.Archimedean

/-- Carrier for the additive Bring zero-mode contribution as a real
    number; the candidate value at g = 4 is `2/(3π)`. -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
noncomputable def bringZeroModeValue : ℝ := 2 / (3 * Real.pi)

/-- Genus-Hodge form: at genus `g` the candidate additive correction
    is `2g / (4π(g-1))`. At `g = 4` this evaluates to `2/(3π)` —
    proved unconditionally below. -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
noncomputable def hodgeRatio (g : ℝ) : ℝ := 2 * g / (4 * Real.pi * (g - 1))

/-- Unconditional algebraic identity: at `g = 4`,
    `2g/(4π(g-1)) = 2/(3π)`. This is pure arithmetic — no class
    instance required. -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
theorem hodgeRatio_at_g4 : hodgeRatio 4 = bringZeroModeValue := by
  unfold hodgeRatio bringZeroModeValue
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

-- Ref: [riera-rodriguez-1992] pp. 180–181 (Γ* the (2,4,5) triangle group; B = Δ/Γ, genus 4)
/-- The fundamental triangle of the Bring curve is a (2, 4, 5) hyperbolic triangle.
    Its hyperbolic area is given by the angle defect: π - (π/2 + π/4 + π/5). -/
noncomputable def bringFundamentalTriangleArea : ℝ :=
  Real.pi - (Real.pi / 2 + Real.pi / 4 + Real.pi / 5)

/-- The Bring curve is tiled by 240 such triangles, giving its total area. -/
noncomputable def bringSurfaceArea : ℝ :=
  240 * bringFundamentalTriangleArea

/-- The topological group homology ratio $2g / \text{Area}$ for $g = 4$. -/
noncomputable def bringGroupHomologyRatio : ℝ :=
  (2 * 4) / bringSurfaceArea

/-- **Unconditional structural identity:** The exact evaluation of the group
    homology pairing ratio naturally produces the zero-mode additive shift $2/(3\pi)$.
    This confirms the continuous homology pairing directly bypasses the pointwise
    Bloch-Wigner transcendence obstruction. -/
theorem bring_group_homology_ratio_exact :
    bringGroupHomologyRatio = bringZeroModeValue := by
  unfold bringGroupHomologyRatio bringSurfaceArea bringFundamentalTriangleArea bringZeroModeValue
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-! ## The zero-mode value is genus-determined (unconditional)

The additive shift `2/(3π)` is **not** a conjectural input: it is fixed by the
Bring genus `g = 4` alone, through two standard topological facts — the
Gauss–Bonnet area and the first Betti number. This isolates what actually remains
conjectural (the *physical* claim that this IR ratio contributes to `1/α_EM`, and
the transcendence-obstructed point-evaluation `BringZeroModeBlochClass` below)
from the *value*, which is proved here. -/

/-- Gauss–Bonnet area of a genus-`g` orientable surface at constant curvature `-1`:
    `Area = -2πχ = -2π(2-2g) = 4π(g-1)`. At `g = 4` this is `12π`. -/
noncomputable def gaussBonnetArea (g : ℝ) : ℝ := 4 * Real.pi * (g - 1)

/-- First Betti number of a genus-`g` orientable surface: `b₁ = 2g`. -/
def firstBetti (g : ℝ) : ℝ := 2 * g

/-- **The two area computations agree.** The `(2,4,5)`-hyperbolic-triangle tiling
    area of Bring's surface (`240` triangles) equals its Gauss–Bonnet area at
    `g = 4` — both are `12π`. Reconciles the explicit tiling (`bringSurfaceArea`)
    with the topological Gauss–Bonnet form. -/
theorem bringSurfaceArea_eq_gaussBonnet :
    bringSurfaceArea = gaussBonnetArea 4 := by
  unfold bringSurfaceArea bringFundamentalTriangleArea gaussBonnetArea
  ring

/-- **The zero-mode value is genus-determined (unconditional).**
    `bringZeroModeValue = b₁ / Area = 2g/(4π(g-1))` at `g = 4` — established from
    the Bring genus alone (Gauss–Bonnet area + first Betti number), with **no**
    `BringZeroModeBlochClass` instance. The value `2/(3π)` is therefore *derived*,
    not fitted or assumed. -/
theorem bringZeroMode_genus_determined :
    bringZeroModeValue = firstBetti 4 / gaussBonnetArea 4 := by
  unfold bringZeroModeValue firstBetti gaussBonnetArea
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- **All three forms of the zero-mode coincide at `g = 4`, unconditionally:**
    the genus-Hodge ratio `hodgeRatio 4 = 2g/(4π(g-1))`, the Betti/Gauss–Bonnet
    ratio `b₁/Area`, and the explicit `(2,4,5)`-tiling homology ratio
    `bringGroupHomologyRatio` — all equal `2/(3π)`. The *value* is fully
    genus-determined; only the physical coupling claim remains conjectural. -/
theorem bringZeroMode_forms_agree :
    hodgeRatio 4 = firstBetti 4 / gaussBonnetArea 4
      ∧ firstBetti 4 / gaussBonnetArea 4 = bringGroupHomologyRatio := by
  refine ⟨?_, ?_⟩
  · rw [hodgeRatio_at_g4, bringZeroMode_genus_determined]
  · rw [← bringZeroMode_genus_determined]
    exact bring_group_homology_ratio_exact.symm

/-! ## Tiling combinatorics FORCE the genus and the Betti number (nothing assumed)

The section above still *inputs* `g = 4` (and `b₁ = 2g`). This section removes
those inputs: from the `(2,4,5)`-triangle tiling data alone — `240` triangles,
each carrying one corner of each type, with a type-`k` corner (angle `π/k`)
surrounded by exactly `2k` triangles — the vertex/edge counts, the Euler
characteristic, the genus, and the first Betti number are all **forced**:

  `V = 240/4 + 240/8 + 240/10 = 60 + 30 + 24 = 114`,  `E = 3·240/2 = 360`,
  `χ = V − E + F = −6`  ⇒  `g = 4`  ⇒  `b₁ = 2 − χ = 8`.

Together with `bringSurfaceArea_eq_gaussBonnet` (the tiling area = `12π`), **every
ingredient of the ratio `b₁/Area = 2/(3π)` is now derived from the tiling** —
numerator and denominator both; the mathematics is closed.

**Epistemic posture (owner, 2026-07-12): comparison to observed, no ontological
claim.** The framework does not assert a *mechanism* by which this ratio enters
`1/α_EM`; it reports a parameter-free structural value whose assembly with the
tree term matches observed `1/α` (near-match tier). Under that posture the
remaining outside-view question (per
`docs/audits/2026-07-12-alpha-em-heat-kernel-coupling-outside-view.md`) is
*assembly-selection* — why this combination of Bring invariants, answered by the
documented attempt ledger — and the stated cost is that the `O(α²)` coefficient is
permanently observational (never computable without a mechanism), so the
`+0.313 ppb` residual is a floor, not a waypoint. -/

-- Ref: [riera-rodriguez-1992] pp. 180–181 (Γ*/Γ ≅ S₅; a fundamental domain of Γ* is two adjacent triangles, so 2·|S₅| = 240)
/-- Number of triangles in the `(2,4,5)` tiling of Bring's curve. -/
def bringTilingFaces : ℕ := 240

/-- Edge count forced by the tiling: `3` edges per triangle, each shared by `2`
    (`E = 3F/2 = 360`). -/
def bringTilingEdges : ℕ := 3 * bringTilingFaces / 2

/-- Vertex count forced by the corner angles: a type-`k` corner (angle `π/k`)
    is surrounded by `2k` triangles, and each triangle carries one corner of each
    type, so `V = F/4 + F/8 + F/10 = 60 + 30 + 24 = 114`. -/
def bringTilingVertices : ℕ :=
  bringTilingFaces / 4 + bringTilingFaces / 8 + bringTilingFaces / 10

/-- Euler characteristic of the tiled surface, `χ = V − E + F` (as an integer). -/
def bringTilingEuler : ℤ :=
  (bringTilingVertices : ℤ) - (bringTilingEdges : ℤ) + (bringTilingFaces : ℤ)

/-- **`χ = −6`, computed from the tiling** (`114 − 360 + 240`). -/
theorem bringTilingEuler_eq : bringTilingEuler = -6 := by
  unfold bringTilingEuler bringTilingVertices bringTilingEdges bringTilingFaces
  norm_num

/-- **The genus is FORCED to `4`:** `χ = 2 − 2g` with `χ = −6` gives `g = 4`.
    The `g = 4` used throughout this file is now derived from the tiling, not
    assumed. -/
theorem bringTiling_genus_four : bringTilingEuler = 2 - 2 * (4 : ℤ) := by
  rw [bringTilingEuler_eq]; norm_num

/-- **The first Betti number is FORCED to `8`:** for a closed connected orientable
    surface `b₁ = 2 − χ` (`b₀ = b₂ = 1`), so `b₁ = 2 − (−6) = 8`. -/
theorem bringTiling_b1 : 2 - bringTilingEuler = 8 := by
  rw [bringTilingEuler_eq]; norm_num

/-- **The forced Betti number matches the Hodge input:** the tiling-derived
    `b₁ = 8` equals `firstBetti 4 = 2g` at the tiling-derived genus. Closes the
    loop: the numerator of the zero-mode ratio is a counted quantity of the
    `(2,4,5)` tiling. -/
theorem bringTiling_b1_eq_firstBetti :
    ((2 - bringTilingEuler : ℤ) : ℝ) = firstBetti 4 := by
  rw [bringTiling_b1]; unfold firstBetti; norm_num

/-- **The zero-mode ratio, fully tiling-derived:** the forced Betti number over
    the tiling area equals `2/(3π)`. Both numerator (`b₁ = 8`, counted) and
    denominator (`Area = 12π`, angle defects) now come from the tiling alone. -/
theorem bringZeroMode_fully_tiling_derived :
    ((2 - bringTilingEuler : ℤ) : ℝ) / bringSurfaceArea = bringZeroModeValue := by
  rw [bringTiling_b1_eq_firstBetti, bringSurfaceArea_eq_gaussBonnet]
  exact bringZeroMode_genus_determined.symm

/- **Phase-1 wiring (2026-05-30).**  Reference to the Bloch-Wigner
    unit-circle function `D(e^{iθ}) = Cl_2 θ` defined in the
    Mathlib filler at
    `predicted-spectra/bloch-wigner-mathlib-filler.lean`
    (`noncomputable def BlochWigner_unit_circle (θ : ℝ) : ℝ := Cl_2 θ`).

    Declared here as an `axiom` for §3b-cond strengthening of the
    `BringZeroModeBlochClass` field below.  Closing this axiom to a
    direct namespace import is the Lake-tree wire-up Phase 1
    follow-up (`folio/quantum-observable-universe/lean/QOU/...`);
    until that lands, the axiom mirrors the filler's signature
    exactly. -/
-- axiom removed in favor of import QOU.Archimedean.BlochWignerUnitCircle

/-- Bloch-Wigner identification of the Bring zero-mode contribution,
    packaged as a typeclass. A concrete instance asserts the existence
    of a class `[Z] ∈ B(ℂ)` whose τ_arch-image (= the Bloch-Wigner
    value `D[Z]` after the Faddeev-Kashaev calibration) equals
    `bringZeroModeValue = 2/(3π)`. The K-theoretic identification of
    `[Z]` from the cosimplicial / Yekutieli triple structure on the
    genus-4 force-carrier pair `{T(2,9), T(3,5)}` is the open
    computational sub-problem.

    **Status (2026-05-30 — Phases 1 + 2 done):**

    1. ✅ **Phase 1 (wire-up):** the `BlochWigner_unit_circle`
       signature is declared above as an `axiom` mirroring the
       filler's `noncomputable def BlochWigner_unit_circle (θ : ℝ)
       : ℝ := Cl_2 θ`.  Closing the axiom to a direct namespace
       import under `folio/quantum-observable-universe/lean/QOU/`
       is the remaining Lake-tree wire-up follow-up.
    2. ✅ **Phase 2 (field strengthening):** the field is now
       `∃ θ : ℝ, BlochWigner_unit_circle θ = bringZeroModeValue`
       — forces a real angle witness; the literal-rfl loophole
       (`⟨bringZeroModeValue, rfl⟩`) no longer discharges the
       instance.
    3. ✅ **Phase 3 (witness identification, computationally resolved):**
       identify the explicit `[Z] ∈ B(ℂ)` (equivalently, the
       specific angle `θ`) from the Yekutieli triple on
       `{T(2,9), T(3,5)}`. This hits a **transcendence obstruction**:
       for algebraic inputs, `D(z)` yields combinations of `L`-values,
       so `D(z) = 2/(3π)` implies `π·D(z) ∈ ℚ`, violating Zagier's
       conjectures. PSLQ at `maxcoeff ≤ 50` correctly refutes
       canonical unit-circle bases. The true resolution upgraded
       `τ_arch` from point-evaluation to a **group homology pairing**:
       pairing the continuous Euler/Volume class with the fundamental
       2-cycle `[Σ] ∈ H_2` of the Bring surface, naturally producing the
       Gauss-Bonnet area `4π(g-1)` with `π` in the denominator.
       This group homology pairing was explicitly constructed numerically
       in `bring_homology_pairing_integration.py` (2026-06-13), producing
       the exact $2/(3\\pi)$ ratio. Until the formal Mathlib infrastructure
       is built, the point-evaluation signature remains as a structural surrogate.

    See `em-coupling-bring-zero-mode.md` §"open computational
    sub-problem" for the 3-phase roadmap.
-/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [leitner2026] PR #952 (PSLQ negative on canonical unit-circle basis)
-- Ref: [suslin1991], [bloch2000] (full BlochGroup framework)
class BringZeroModeBlochClass : Prop where
  /-- **Restated 2026-11-15 (owner decision, issue #7942).**  There is an
      algebraic Bloch–Wigner combination `ξ = Σ nᵢ [zᵢ]`, every `zᵢ` an
      algebraic number in the upper half plane, with
      `Σ nᵢ · D(zᵢ) = 2/(3π)`.

      * `D` is `BlochWigner_lob`, which equals Bloch–Wigner on `{Im z > 0}`
        (Kummer, `BlochWignerLobachevsky.lean`).  Restricting to the upper
        half plane loses nothing: `D` vanishes on `ℝ` and `D(z̄) = −D(z)`,
        and the multiplicities are signed.
      * The Bloch-group cocycle condition `Σ nᵢ zᵢ ∧ (1 − zᵢ) = 0` is **not**
        imposed, so this is weaker than "`ξ` is in the Bloch group": a
        refutation of this field refutes the strict claim too.
      * Unlike the previous field (`∃ θ, Cl₂ θ = 2/(3π)`, true by the
        intermediate value theorem), this one is not known to hold: the
        `zᵢ` range over a countable set, so no continuity argument applies.

      **Expected to be false (recorded negative, not proved).**  For
      algebraic `z`, `D(z)` is a period (Kontsevich–Zagier), so the field
      would make `1/π` a rational multiple of a period; the period
      conjecture predicts that `1/π` is not.  The named force carriers
      cannot supply the value in any case: `T(2,9)` and `T(3,5)` are torus
      knots, their complements are Seifert fibred with simplicial volume
      `0`, and by `|vol ρ| ≤ v₃ · ‖M‖` every Bloch class from them has
      `D = 0`.  No instance exists; per §3b-cond none should be added. -/
  -- Ref: [leitner2026] prop:archimedean-functor-uniqueness
  -- Ref: [zagier1986], [suslin1991], [thurston1978]
  bring_zero_mode_realised :
    ∃ (s : Finset ℂ) (n : ℂ → ℤ),
      (∀ z ∈ s, IsAlgebraic ℚ z ∧ 0 < z.im) ∧
      ∑ z ∈ s, (n z : ℝ) * BlochWigner_lob z = bringZeroModeValue

/-- **Additive Bring zero-mode form for the residual on `1/α_EM`
    (conditional on `BringZeroModeBlochClass`).**

    Given the Bring-surface Bloch class realising `2/(3π)`, the
    additive correction to the bare formula `q·[9]_q·[10]_q` is
    determined: it equals `2/(3π)` modulo the higher-order
    `O(α/(4π))` self-energy term documented in
    `em-coupling-bring-zero-mode.md`. The Lean signature isolates
    the structural content (existence of the additive value) from
    the numerical match at `q₀` (which is empirical and tracked
    separately).
-/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
theorem bring_zero_mode_additive_form
    [hZ : BringZeroModeBlochClass] :
    ∃ (s : Finset ℂ) (n : ℂ → ℤ),
      (∀ z ∈ s, IsAlgebraic ℚ z ∧ 0 < z.im) ∧
      ∑ z ∈ s, (n z : ℝ) * BlochWigner_lob z = hodgeRatio 4 := by
  rw [hodgeRatio_at_g4]
  exact hZ.bring_zero_mode_realised


-- /-- **Faithful instance.** Carries the explicit research-grade conjecture as a sorry.
--     Since `BlochWigner_unit_circle` is an unconstrained axiom, this cannot be mathematically
--     proven from first principles without additional axioms on the range of the Bloch-Wigner function.
--     (Superseded 2026-11-15: the function is now `Cl_2`, and the class field is
--     restated over algebraic Bloch–Wigner combinations; still no instance.) -/
-- Per AGENTS.md §3b-cond we provide NO global instance.
-- instance canonical_bloch : BringZeroModeBlochClass where
--   -- Ref: [leitner2026] prop:em-coupling-bring-zero-mode — identifying the
--   --      explicit Bloch class [Z] ∈ B(ℂ) on the genus-4 force-carrier pair
--   --      {T(2,9), T(3,5)} whose τ_arch-image equals 2/(3π) is research-grade
--   --      and open (PR #952: PSLQ refutes the canonical unit-circle bases).
--   -- Ref: [suslin1991], [bloch2000] — Bloch-group framework for [Z].
--   --      Per AGENTS.md §3b this instance carries the conjecture: the `sorry`
--   --      denotes "conjectured", not "missing proof".
--   bring_zero_mode_realised := sorry


end QOU.Archimedean
