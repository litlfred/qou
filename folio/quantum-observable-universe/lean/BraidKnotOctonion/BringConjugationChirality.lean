/-
# Bring's surface: the conjugation involution and the chirality of the C₅ rotation

Owner, 2026-10-12: derive a chiral Bring term on `UT(Σ₄)` (bean `qou-jfx8`, follow-up to
`QOU/MassTheory/SegmentCollisionDatum.lean`, Part D: a chiral selection at the collision
must come from the Bring term, because the local O'Hara term is achiral).

## The exclusion (scope (b), invariant: the real structure)

Bring's curve `Σ x = Σ x² = Σ x³ = 0` in `ℙ⁴` has rational equations, so complex
conjugation `ι` maps it to itself. `ι` is antiholomorphic, hence orientation-reversing, and
it is an isometry of the uniformising hyperbolic metric (the metric is unique in its
conformal class). It is fixed-point free: a real point would have `Σ x = Σ x² = 0` with
`x` real, forcing `x = 0`. Any energy built from the metric alone satisfies
`E_{ιp}(φ) = E_p(−φ)` for the oriented angle `φ` between the incoming directions, so its
average over a conjugate pair is even in `φ` (`pairAverage_even`), and an even energy with
a unique minimiser selects `φ = 0` (`even_unique_minimiser_eq_zero`): neither crossing sign.
**No metric-only Bring term is chiral.** It can be chiral only at a point that has been
singled out from its conjugate.

## 🛑 Scope of that exclusion: Σ × I, NOT UT(Σ₄) (added 2026-10-12)

The exclusion reads a crossing sign off the surface picture (two segments on Σ, over/under
by the normal coordinate), i.e. links in `Σ × I`. There `ι × id` reverses the 3-manifold's
orientation (`sigmaI_lift_reverses`, Jacobian `diag(1, −1, 1)`), so it swaps `σ ↔ σ⁻¹`.

The corpus places the Reeb flow on `UT(Σ₄)`. The natural lift of `ι` there is its
differential, which in local coordinates `(x, y, θ)` is `(x, −y, −θ)`: it reverses the base
AND the fibre angle, so its Jacobian `diag(1, −1, −1)` has determinant `+1`
(`ut_lift_preserves`). **On `UT(Σ₄)` conjugation preserves orientation, hence preserves
crossing signs.** So on `UT(Σ₄)` the argument above does not exclude a chiral metric term, and
the `letterSign_conj` clause of `ChiralityMatching` below is the `Σ × I` reading; under the
natural lift to `UT(Σ₄)` it fails. Pointed out by a literature check (skein theory:
an orientation-reversing map of the 3-manifold sends `A ↦ A⁻¹` and links to mirrors;
arXiv:1610.04728), and verified here.

## The chiral datum that IS there (generic, exact, `ZMod 5`)

Let `g` be the 5-cycle `x_k ↦ x_{k+1}`. Its fixed points on the curve are `p_j = (ζ^{jk})_k`
for `j = 1,2,3,4`. In the eigenbasis `e_m = (ζ^{mk})_k` of `g`, the tangent cone at `p_j`
is cut out by the vanishing of the frequencies `0, −j, −2j` (the three Jacobian rows), so
the cone is `span(e_j, e_{2j})` (`residues_distinct` shows the five residues
`0, −j, −2j, j, 2j` are distinct). The tangent line is `e_{2j}` modulo `p_j = e_j`, and
`g` rotates it by `ζ^{j − 2j} = ζ^{−j}` (`rotExp`). So:

* the four fixed points of one 5-cycle carry four distinct rotations `ζ^{−j}`;
* conjugation swaps `p_j ↔ p_{−j}` and the rotations `ζ^{−j} ↔ ζ^{j}` (`rotExp_neg`);
* no fixed point has a self-conjugate rotation (`rotExp_ne_rotExp_neg`).

The corpus's single-knot Reeb angle `θ_λ = arccos(χ_λ(C₅)/dim λ)`
(`BringFiberActionInstance.reebAngle`) keeps only the real part of this rotation, which is
the conjugation-invariant half. The sign of the imaginary part, the direction in which
`g` turns the fibre of `UT(Σ₄)` at its fixed point, is the chiral datum the corpus
discards.

## What is NOT derived

A chiral ENERGY term. Turning the rotation sign into an energy that prefers `σ` over `σ⁻¹`
needs a rule matching the curve's conjugation `ι` (`ζ ↦ ζ̄`) with the Hecke bar involution
(`q ↦ q⁻¹`, `σ ↔ σ⁻¹`). That rule is stated below as a primary conjecture class with no
instance (`ChiralityMatching`). Choosing it is a decision about the framework, not a
computation.

§7c: Parts 1 and 3 are over `ZMod 5` and an abstract type; Part 2 is over `ℝ` because it
uses the order on angles.

-- Ref: [manuscript] lem:bring-cone-reeb-quaternionic-twist (link = UT(Σ₄));
   bean qou-rydq; bean qou-jfx8. Holomorphic Lefschetz fixed-point data of automorphisms
   of curves: [manuscript] (standard; Farkas–Kra, Riemann Surfaces, §V.2).
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

namespace QOU.Brings.ConjugationChirality

/-! ## Part 1 — the C₅ fixed-point rotations (exact) -/

/-- The five Fourier residues at the fixed point `p_j` are pairwise distinct for `j ≠ 0`:
`0`, `−j`, `−2j` (killed by the Jacobian), `j` (the point), `2j` (the tangent line). -/
theorem residues_distinct (j : ZMod 5) (hj : j ≠ 0) :
    (0 : ZMod 5) ≠ -j ∧ (0 : ZMod 5) ≠ -2 * j ∧ (0 : ZMod 5) ≠ j ∧ (0 : ZMod 5) ≠ 2 * j ∧
    -j ≠ -2 * j ∧ -j ≠ j ∧ -j ≠ 2 * j ∧ -2 * j ≠ j ∧ -2 * j ≠ 2 * j ∧ j ≠ 2 * j := by
  revert hj
  revert j
  decide

/-- The rotation exponent of the 5-cycle at `p_j`: the tangent line `e_{2j}` against the
point `e_j`, i.e. `ζ^{j − 2j}`. -/
def rotExp (j : ZMod 5) : ZMod 5 := j - 2 * j

theorem rotExp_eq_neg (j : ZMod 5) : rotExp j = -j := by
  unfold rotExp; ring

/-- **Conjugation reverses the rotation.** `p_{−j}` is the conjugate of `p_j`. -/
theorem rotExp_neg (j : ZMod 5) : rotExp (-j) = -rotExp j := by
  simp only [rotExp_eq_neg]

/-- **No fixed point is chirally neutral**: its rotation differs from its conjugate's. -/
theorem rotExp_ne_rotExp_neg (j : ZMod 5) (hj : j ≠ 0) : rotExp j ≠ rotExp (-j) := by
  revert hj
  revert j
  decide

/-- **The four fixed points of one 5-cycle carry four distinct rotations.** -/
theorem rotExp_injective : Function.Injective rotExp := by
  intro a b h
  simpa [rotExp_eq_neg] using h

/-! ## Part 2 — metric-only energies are achiral -/

/-- The energy at a point and at its conjugate, as functions of the oriented angle,
averaged over the pair. -/
noncomputable def pairAverage (Ep Eιp : ℝ → ℝ) (φ : ℝ) : ℝ := (Ep φ + Eιp φ) / 2

/-- **Conjugation-invariant energies average to an even function.** -/
theorem pairAverage_even (Ep Eιp : ℝ → ℝ) (hι : ∀ φ, Eιp φ = Ep (-φ)) (φ : ℝ) :
    pairAverage Ep Eιp (-φ) = pairAverage Ep Eιp φ := by
  simp only [pairAverage, hι, neg_neg]
  ring

/-- **An even energy with a unique minimiser on a symmetric interval selects `φ = 0`**:
neither crossing sign. -/
theorem even_unique_minimiser_eq_zero (E : ℝ → ℝ) (hE : ∀ φ, E (-φ) = E φ) (a φs : ℝ)
    (hmem : φs ∈ Set.Ioo (-a) a)
    (huniq : ∀ φ ∈ Set.Ioo (-a) a, E φ = E φs → φ = φs) : φs = 0 := by
  have hmem' : -φs ∈ Set.Ioo (-a) a := ⟨by linarith [hmem.2], by linarith [hmem.1]⟩
  have h := huniq (-φs) hmem' (hE φs)
  linarith

/-! ## Part 2b — which lift reverses orientation -/

/-- `ι × id` on `Σ × I`, locally `(x, y, t) ↦ (x, −y, t)`: orientation-REVERSING. -/
theorem sigmaI_lift_reverses :
    (Matrix.diagonal ![(1 : ℤ), -1, 1]).det = -1 := by
  simp [Matrix.det_diagonal, Fin.prod_univ_three]

/-- The differential of `ι` on `UT(Σ)`, locally `(x, y, θ) ↦ (x, −y, −θ)`:
orientation-PRESERVING. -/
theorem ut_lift_preserves :
    (Matrix.diagonal ![(1 : ℤ), -1, -1]).det = 1 := by
  simp [Matrix.det_diagonal, Fin.prod_univ_three]

/-! ## Part 3 — the matching rule, a primary conjecture class (no instance) -/

/-- **Chirality matching.** Over an abstract set `X` of collision configurations with an
oriented-angle map, the curve's conjugation and the Hecke bar involution act compatibly:
the bar involution on the letter (`σ ↔ σ⁻¹`, encoded as `letterSign`) is the conjugation on
the configuration. With this, a configuration pinned to one member of a conjugate pair
fixes a crossing sign. No instance: nothing in the corpus derives it. -/
class ChiralityMatching (X : Type*) where
  /-- The curve's conjugation acting on configurations. -/
  conj : X → X
  conj_invol : ∀ x, conj (conj x) = x
  /-- The C₅ rotation exponent at the configuration's fixed point. -/
  rot : X → ZMod 5
  rot_conj : ∀ x, rot (conj x) = -rot x
  /-- The crossing sign selected at the configuration (`true` = `σ`, `false` = `σ⁻¹`). -/
  letterSign : X → Bool
  /-- The matching: conjugation is the bar involution on the selected letter. -/
  letterSign_conj : ∀ x, letterSign (conj x) = !letterSign x

/-- Under the matching, a configuration and its conjugate select opposite letters: so the
selection is chiral exactly when the configuration is pinned to one side. -/
theorem letterSign_ne_conj {X : Type*} [M : ChiralityMatching X] (x : X) :
    M.letterSign (M.conj x) ≠ M.letterSign x := by
  rw [M.letterSign_conj]
  cases M.letterSign x <;> decide

end QOU.Brings.ConjugationChirality
