import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.Tactic.CategoryTheory.Monoidal.Basic

/-!
# The mass trace as a functional of the multiplicative integral

`def:mass-identity` defines the inertial mass of a closed cycle `ϱ` through the
composite `Ψ = (∫_A ⊗ id) ∘ Δ` and the categorical trace on `End(A)`, and its
proof block for the archimedean model (`mass-identity-C`) identifies the same
mass with a non-abelian multiplicative integral, i.e. a holonomy. As written the
block applies `tr` to `Ψ ∘ ϱ : 𝟙 → A`, which is not an endomorphism (bean
`qou-puwe`, defect 1). This file states the identity in a form that typechecks
and proves it, over an arbitrary braided monoidal category, from the axioms of
`FrobeniusHopfData` alone.

## Statement

A cycle enters through its left-multiplication endomorphism
`L_x = λ_A⁻¹ ≫ (x ▷ A) ≫ μ`. The discrete multiplicative integral of a word
`w = [g₁, …, g_k]` of transports `gᵢ : 𝟙 ⟶ A` is their ordered product
`hol w = g₁ * ⋯ * g_k` in the convolution monoid `Hom(𝟙, A)`; this is the
`List.prod` holonomy of `QOU.MathlibExt.YekutieliIntegration.holonomy`, read in
`A`. The theorems are:

1. `massIntegrand_eq_leftMul_density`: `Ψ = L_u` with `u = Ψ ∘ η`. The mass
   integrand is left multiplication by one fixed element, the *density* `u` of
   the Frobenius form `∫_A` relative to the coalgebra. Only the unit law and
   the Frobenius relation are used.
2. `density_eq_unit_of_frobeniusForm_eq_counit`: if `∫_A` is the counit, then
   `u = η` and `Ψ = id`. This is the correct reason for the step
   "`Ψ = id`" in `prop:categorical-mass-markov`; it is the counit law, not the
   Nakayama automorphism or `S² = id`.
3. `leftTrace_leftMul`: `tr(L_y) = ∫_A(y · c)` with `c = μ ∘ coev`, the
   Casimir element of the self-duality.
4. `massTrace_eq_functional_hol` (the mass identity): for every word `w`,

       tr(L_{hol w} ≫ Ψ) = ∫_A(u · hol w · c).

   The trace of the mass endomorphism of a cycle is a fixed linear functional,
   `x ↦ ∫_A(u · x · c)`, evaluated on the multiplicative integral of the cycle.

## What this does not say

The functional `x ↦ ∫_A(u · x · c)` is the categorical trace of `A` acting on
itself. Under a fibre functor to free `R`-modules it is the regular trace
`x ↦ Tr_A(L_{u x})`, not the Jones–Markov trace: for `A = H_n(q)` the
normalised regular trace fails the Markov property at `n = 3`
(`tr(σ₁σ₂) = h²/6` against `(tr σ₁)² = h²/4`, `h = q − q⁻¹`). The Markov trace is
the quantum trace of the module `V^{⊗n}`, not of `A`
(see `QOU.MassEndomorphism.MassLeftMulEndomorphism`). This file makes no claim
about that identification.

**Base ring (§7c).** No ring, order or norm appears: everything is a morphism
identity in a monoidal category. No archimedean structure is used.

## References

- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 — Frobenius objects,
  the Frobenius relation, and the self-duality `ev = ∫_A ∘ μ`.
- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — multiplicative integration;
  only its discrete (ordered-product) layer is used here.
-/

open CategoryTheory MonoidalCategory

namespace QOU.Torsion.MassTraceIdentity

universe u v

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
variable (F : QOU.FrobeniusHopfData C)

/-- The mass integrand `Ψ = (∫_A ⊗ id) ∘ Δ : A → A`, with the left unitor made
    explicit. -/
def massIntegrand : F.obj ⟶ F.obj :=
  F.comul ≫ (F.frobeniusForm ▷ F.obj) ≫ (λ_ F.obj).hom

/-- Left multiplication `L_x : A → A` by a generalised element `x : 𝟙 ⟶ A`. -/
def leftMul (x : 𝟙_ C ⟶ F.obj) : F.obj ⟶ F.obj :=
  (λ_ F.obj).inv ≫ (x ▷ F.obj) ≫ F.mul

/-- The convolution product `x * y` on generalised elements `𝟙 ⟶ A`. -/
def conv (x y : 𝟙_ C ⟶ F.obj) : 𝟙_ C ⟶ F.obj :=
  (λ_ (𝟙_ C)).inv ≫ (x ⊗ₘ y) ≫ F.mul

/-- The discrete multiplicative integral (path-ordered product) of a word of
    transports, `hol [g₁, …, g_k] = g₁ * (g₂ * ⋯ (g_k * η))`. -/
def hol : List (𝟙_ C ⟶ F.obj) → (𝟙_ C ⟶ F.obj)
  | [] => F.unit
  | g :: w => conv F g (hol w)

/-- The density `u = Ψ ∘ η` of the Frobenius form relative to the coalgebra. -/
def density : 𝟙_ C ⟶ F.obj := F.unit ≫ massIntegrand F

/-- The Casimir element `c = μ ∘ coev` of the self-duality of `A`. -/
def casimir : 𝟙_ C ⟶ F.obj := F.coevaluation ≫ F.mul

/-- `L_η = id`. -/
theorem leftMul_unit : leftMul F F.unit = 𝟙 F.obj := by
  simp [leftMul, F.one_mul]

/-- `L_x ∘ η = x`. -/
theorem unit_leftMul (x : 𝟙_ C ⟶ F.obj) : F.unit ≫ leftMul F x = x := by
  simp only [leftMul]
  rw [leftUnitor_inv_naturality_assoc, whisker_exchange_assoc, F.mul_one,
    rightUnitor_naturality, unitors_inv_equal]
  simp

/-- `L_{x * y} = L_x ∘ L_y`, written in diagrammatic order. -/
theorem leftMul_conv (x y : 𝟙_ C ⟶ F.obj) :
    leftMul F (conv F x y) = leftMul F y ≫ leftMul F x := by
  simp only [leftMul, conv, tensorHom_def', comp_whiskerRight, Category.assoc, F.mul_assoc]
  rw [leftUnitor_inv_naturality_assoc, whisker_exchange_assoc]
  monoidal

/-- `x ↦ L_x` is injective: `x = η ≫ L_x`. -/
theorem leftMul_injective {x y : 𝟙_ C ⟶ F.obj} (h : leftMul F x = leftMul F y) : x = y := by
  rw [← unit_leftMul F x, ← unit_leftMul F y, h]

/-- The convolution product is associative, so `Hom(𝟙, A)` is a monoid. -/
theorem conv_assoc (x y z : 𝟙_ C ⟶ F.obj) :
    conv F (conv F x y) z = conv F x (conv F y z) :=
  leftMul_injective F (by simp only [leftMul_conv, Category.assoc])

/-- `η` is a left unit for the convolution product. -/
theorem unit_conv (x : 𝟙_ C ⟶ F.obj) : conv F F.unit x = x :=
  leftMul_injective F (by rw [leftMul_conv, leftMul_unit, Category.comp_id])

/-- `η` is a right unit for the convolution product. -/
theorem conv_unit (x : 𝟙_ C ⟶ F.obj) : conv F x F.unit = x :=
  leftMul_injective F (by rw [leftMul_conv, leftMul_unit, Category.id_comp])

/-- The multiplicative integral is multiplicative under concatenation of words. -/
theorem hol_append (w w' : List (𝟙_ C ⟶ F.obj)) :
    hol F (w ++ w') = conv F (hol F w) (hol F w') := by
  induction w with
  | nil => simp [hol, unit_conv]
  | cons g w ih => simp [hol, ih, conv_assoc]

@[simp] theorem hol_nil : hol F [] = F.unit := rfl

@[simp] theorem hol_cons (g : 𝟙_ C ⟶ F.obj) (w : List (𝟙_ C ⟶ F.obj)) :
    hol F (g :: w) = conv F g (hol F w) := rfl

@[simp] theorem hol_singleton (g : 𝟙_ C ⟶ F.obj) : hol F [g] = g := by
  simp [hol, conv_unit]

/-- The endomorphism of a word is the composite of the letters' endomorphisms,
    last letter acting first. -/
theorem leftMul_hol_cons (g : 𝟙_ C ⟶ F.obj) (w : List (𝟙_ C ⟶ F.obj)) :
    leftMul F (hol F (g :: w)) = leftMul F (hol F w) ≫ leftMul F g :=
  leftMul_conv F g (hol F w)

/-- Concatenation of transport words composes their left-multiplication
    endomorphisms in diagrammatic order. -/
theorem leftMul_hol_append (w w' : List (𝟙_ C ⟶ F.obj)) :
    leftMul F (hol F (w ++ w')) = leftMul F (hol F w') ≫ leftMul F (hol F w) := by
  rw [hol_append, leftMul_conv]

/-- **The mass integrand is left multiplication by the density.**
    `Ψ = L_u` with `u = Ψ ∘ η`. -/
theorem massIntegrand_eq_leftMul_density :
    massIntegrand F = leftMul F (density F) := by
  conv_lhs => rw [← Category.id_comp (massIntegrand F), ← leftMul_unit F]
  simp only [leftMul, density, massIntegrand, comp_whiskerRight, Category.assoc]
  rw [reassoc_of% F.frobenius_relation, whisker_exchange_assoc, leftUnitor_naturality]
  monoidal

/-- If the Frobenius form is the counit, the density is the unit. -/
theorem density_eq_unit_of_frobeniusForm_eq_counit
    (h : F.frobeniusForm = F.counit) : density F = F.unit := by
  simp [density, massIntegrand, h, reassoc_of% F.counit_comul]

/-- If the Frobenius form is the counit, the mass integrand is the identity. -/
theorem massIntegrand_eq_id_of_frobeniusForm_eq_counit
    (h : F.frobeniusForm = F.counit) : massIntegrand F = 𝟙 F.obj := by
  simp [massIntegrand, h, reassoc_of% F.counit_comul]

/-- Left multiplication applied to an element is the convolution product:
    `x ≫ L_y = y * x`. -/
theorem comp_leftMul (x y : 𝟙_ C ⟶ F.obj) : x ≫ leftMul F y = conv F y x := by
  conv_lhs => rw [← unit_leftMul F x]
  rw [Category.assoc, ← leftMul_conv, unit_leftMul]

/-- **The mass integrand applied to a cycle, then integrated.** For `x : 𝟙 ⟶ A`,
    `∫_A(Ψ ∘ x) = ∫_A(u · x)`. This is the well-typed reading of
    `∫_A((∫_A ⊗ id) ∘ Δ ∘ ϱ)`: the composite `𝟙 → A → A → 𝟙` needs no trace. -/
theorem frobeniusForm_massIntegrand (x : 𝟙_ C ⟶ F.obj) :
    x ≫ massIntegrand F ≫ F.frobeniusForm = conv F (density F) x ≫ F.frobeniusForm := by
  rw [massIntegrand_eq_leftMul_density, ← Category.assoc, comp_leftMul]

/-- If the Frobenius form is the counit, `∫_A(Ψ ∘ x) = ∫_A(x)`: the mass of a cycle is the
    Frobenius form of the cycle itself. -/
theorem frobeniusForm_massIntegrand_of_frobeniusForm_eq_counit
    (h : F.frobeniusForm = F.counit) (x : 𝟙_ C ⟶ F.obj) :
    x ≫ massIntegrand F ≫ F.frobeniusForm = x ≫ F.frobeniusForm := by
  rw [massIntegrand_eq_id_of_frobeniusForm_eq_counit F h, Category.id_comp]

/-- **Frobenius mass functional on the non-abelian holonomy product (Option 1).**
    The cycle is formed first as the ordered convolution product `hol F w` in `Hom(𝟙, A)`,
    and then integrated through `Ψ` and `∫_A`. -/
theorem frobeniusForm_massIntegrand_hol (w : List (𝟙_ C ⟶ F.obj)) :
    hol F w ≫ massIntegrand F ≫ F.frobeniusForm =
      conv F (density F) (hol F w) ≫ F.frobeniusForm :=
  frobeniusForm_massIntegrand F (hol F w)

/-- When `∫_A = ε`, the Frobenius mass functional of a transport word `w` is `∫_A(hol w)`. -/
theorem frobeniusForm_massIntegrand_hol_of_frobeniusForm_eq_counit
    (h : F.frobeniusForm = F.counit) (w : List (𝟙_ C ⟶ F.obj)) :
    hol F w ≫ massIntegrand F ≫ F.frobeniusForm = hol F w ≫ F.frobeniusForm :=
  frobeniusForm_massIntegrand_of_frobeniusForm_eq_counit F h (hol F w)

/-- **Trace of a left multiplication.** `tr(L_y) = ∫_A(y · c)`. -/
theorem leftTrace_leftMul (y : 𝟙_ C ⟶ F.obj) :
    F.leftTrace (leftMul F y) = casimir F ≫ leftMul F y ≫ F.frobeniusForm := by
  simp only [QOU.FrobeniusHopfData.leftTrace, QOU.FrobeniusHopfData.ev, leftMul, casimir,
    comp_whiskerRight, Category.assoc]
  rw [reassoc_of% F.mul_assoc, leftUnitor_inv_naturality_assoc, whisker_exchange_assoc]
  monoidal

/-- **Mass identity.** The categorical trace of the mass endomorphism of a
    cycle is the functional `x ↦ ∫_A(u · x · c)` evaluated on the cycle's
    multiplicative integral `x = hol w`. -/
theorem massTrace_eq_functional_hol (w : List (𝟙_ C ⟶ F.obj)) :
    F.leftTrace (leftMul F (hol F w) ≫ massIntegrand F) =
      casimir F ≫ leftMul F (conv F (density F) (hol F w)) ≫ F.frobeniusForm := by
  rw [massIntegrand_eq_leftMul_density, ← leftMul_conv, leftTrace_leftMul]

/-- With the Frobenius form equal to the counit, the mass is `∫_A(hol w · c)`. -/
theorem massTrace_eq_functional_hol_of_frobeniusForm_eq_counit
    (h : F.frobeniusForm = F.counit) (w : List (𝟙_ C ⟶ F.obj)) :
    F.leftTrace (leftMul F (hol F w) ≫ massIntegrand F) =
      casimir F ≫ leftMul F (hol F w) ≫ F.frobeniusForm := by
  rw [massIntegrand_eq_id_of_frobeniusForm_eq_counit F h, Category.comp_id,
    leftTrace_leftMul]

end QOU.Torsion.MassTraceIdentity
