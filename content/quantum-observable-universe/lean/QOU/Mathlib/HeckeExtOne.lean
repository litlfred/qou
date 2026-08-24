import QOU.Mathlib.ExtensionClass
import QOU.GroundRingCore
import Mathlib.RingTheory.Ideal.Span
import Mathlib.Tactic

/-!
# QOU.Mathlib.HeckeExtOne — `Ext¹(V_asym, V_sym) ≅ R/(α − β)`, and why that is `ℤ`

Bean `qou-zut2`. `phase-transition-boundary` asserts that the mixed-channel
Hecke representation is a **non-split** extension

    0 → V_sym → V_mixed → V_asym → 0

classified by `Ext¹_{H_n(q)}(V_asym, V_sym) ≅ ℤ`, while
`skein-resolution-obstruction` states that `H_n(q₀)` is **semisimple**
(`Rad = 0`) at the physical `q₀ ≈ 1.1099`. A semisimple algebra has
`Ext¹ = 0`, so the two looked inconsistent.

**They are not, and this file is the reason.** The Ext group is computed here
by hand, and it is `R/(α − β)` — a *torsion* `R`-module supported exactly on the
locus where the two eigenvalues collide, which is exactly the locus where the
algebra fails to be semisimple. Specialising at a semisimple point kills it.
Both claims are true; they are statements about different fibres.

## The computation, which is elementary

The Hecke quadratic relation the corpus uses is `(T - q)(T + 1) = 0`
(`HeckeAnyonicSubstrate.heckeQuadratic`), so the two one-dimensional modules are
`V_sym` with `T ↦ q` and `V_asym` with `T ↦ -1`. Here they are carried as
general eigenvalues `α, β`, because the corpus uses two normalisations in
different chapters and the answer depends on which — see the caution below.

An extension of `V_β` by `V_α` is free of rank two: `T e₁ = α e₁` and
`T e₂ = β e₂ + c e₁` for some `c : R`. `extAction_quadratic` shows the quadratic
relation holds for **every** `c`, so every `c` really does give an extension —
there is no hidden constraint. Rebasing `e₂ ↦ e₂ + λ e₁` sends `c ↦ c + λ(β−α)`,
so the classification is `R` modulo the ideal `(α − β)`:

    Ext¹(V_β, V_α) ≅ R / (α − β).

`splits_iff_mem_span` is that statement in the form actually proved: the
extension splits precisely when `c` lies in the ideal.

## Why `ℤ`, and why it does not contradict semisimplicity

With `α = q`, `β = -1` the ideal is `(q + 1)`, and

    R_q / (q + 1) = ℤ[q, q⁻¹] / (q + 1) ≅ ℤ

by `q ↦ -1`, which is legitimate in the Laurent ring because `-1` is a unit. So
the corpus's `≅ ℤ` is **right**.

And `isUnit_sub_eigenvalues → every extension splits`
(`splits_of_isUnit_sub`) is the semisimple half: wherever `α − β` is invertible
the ideal is everything, the quotient is zero, and there is nothing to classify.
At `q₀ ≈ 1.1099`, `q₀ + 1 ≈ 2.11` is invertible in `ℝ`, so `Ext¹ = 0` there —
which is what semisimplicity demands.

The `ℤ` is therefore not a group of extensions existing *at* `q₀`. It is the
generic classification over `R_q`, and it is supported at `q = -1`, the point
where `(T − q)(T + 1)` acquires a double root and the algebra degenerates.

## A caution about normalisation — the answer is convention-dependent

The corpus carries two Hecke normalisations. `HeckeAnyonicSubstrate` uses
`(T − q)(T + 1) = 0`, giving eigenvalues `q, -1`, ideal `(q + 1)`, and `ℤ`.
But `categorical-meson` uses `σᵢ² = h σᵢ + 1` with `h = q − q⁻¹`, whose roots
are `q` and `-q⁻¹`; there the ideal is `(q + q⁻¹) = (q² + 1)` up to the unit
`q⁻¹`, and the quotient is `ℤ[q]/(q² + 1) ≅ ℤ[i]` — the **Gaussian integers,
not ℤ**.

So `≅ ℤ` holds in the first normalisation and fails in the second. This file
proves the general statement and leaves the choice explicit rather than picking
one silently; anyone quoting `ℤ` should say which relation they mean.

-- Ref: [manuscript] quantum-observable-universe/information-theory
-/

namespace QOU.Mathlib.HeckeExtOne

universe u

variable {R : Type u} [CommRing R]

/-- **The rank-two extension** `M_c` of `V_β` by `V_α`.

    Carrier `R × R`, with `e₁ = (1,0)` spanning the sub-object `V_α` and
    `e₂ = (0,1)` lifting `V_β`. The generator acts by

        T (x, y) = (α x + c y, β y).

    Read off the matrix: `T e₁ = α e₁` and `T e₂ = c e₁ + β e₂`. -/
def extAction (α β c : R) : (R × R) →ₗ[R] (R × R) where
  toFun p := (α * p.1 + c * p.2, β * p.2)
  map_add' p r := by
    simp only [Prod.fst_add, Prod.snd_add, Prod.mk_add_mk, Prod.mk.injEq]
    constructor <;> ring
  map_smul' r p := by
    simp only [Prod.smul_fst, Prod.smul_snd, Prod.smul_mk, smul_eq_mul,
      RingHom.id_apply, Prod.mk.injEq]
    constructor <;> ring

@[simp] theorem extAction_apply (α β c : R) (p : R × R) :
    extAction α β c p = (α * p.1 + c * p.2, β * p.2) := rfl

/-- **Every `c` gives a genuine extension.**

    `(T − α)(T − β) = 0` holds for all `c`, so the Hecke quadratic relation
    places no constraint on the extension parameter. This is what makes the
    classification a full quotient of `R` rather than of a subset. -/
theorem extAction_quadratic (α β c : R) :
    ((extAction α β c) - α • LinearMap.id).comp
      ((extAction α β c) - β • LinearMap.id) = 0 := by
  ext <;>
  · simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.smul_apply,
      LinearMap.id_apply, extAction_apply, Prod.smul_fst, Prod.smul_snd,
      smul_eq_mul, Prod.fst_sub, Prod.snd_sub, LinearMap.zero_apply,
      Prod.fst_zero, Prod.snd_zero]
    ring

/-- The extension **splits** when the quotient generator lifts equivariantly:
    a section `y ↦ (λ y, y)` commuting with `T`. -/
def Splits (α β c : R) : Prop := ∃ lam : R, c = lam * (β - α)

/-- **The classification.** `M_c` splits exactly when `c` lies in the ideal
    generated by `α − β`.

    The section must be `y ↦ (λ y, y)` for some `λ`, and equivariance forces
    `α λ + c = λ β`. So the splittings are parametrised by solutions of
    `c = λ(β − α)`, and the extension classes by `R / (α − β)`. -/
theorem splits_iff_mem_span (α β c : R) :
    Splits α β c ↔ c ∈ Ideal.span ({α - β} : Set R) := by
  rw [Ideal.mem_span_singleton]
  constructor
  · rintro ⟨lam, rfl⟩
    exact ⟨-lam, by ring⟩
  · rintro ⟨k, rfl⟩
    exact ⟨-k, by ring⟩

/-- **The semisimple half.** If the two eigenvalues differ by a unit, every
    extension splits — the ideal is everything and the quotient is zero.

    This is why `Ext¹ = 0` at the physical point: `q₀ ≈ 1.1099` makes
    `q₀ + 1 ≈ 2.11` invertible, and `skein-resolution-obstruction`'s
    `Rad = 0` is the same fact. -/
theorem splits_of_isUnit_sub (α β c : R) (h : IsUnit (α - β)) :
    Splits α β c := by
  rw [splits_iff_mem_span]
  rw [Ideal.span_singleton_eq_top.mpr h]
  trivial

/-- **The degenerate half.** Where the eigenvalues collide the ideal is zero,
    so `c` classifies on the nose and every nonzero `c` is a non-split
    extension.

    `α = β` is exactly where `(T − α)(T − β)` acquires a double root, i.e.
    where the algebra stops being semisimple. The extensions live there and
    nowhere else. -/
theorem not_splits_of_eq_of_ne_zero {α β c : R} (hαβ : α = β) (hc : c ≠ 0) :
    ¬ Splits α β c := by
  rintro ⟨lam, rfl⟩
  exact hc (by rw [hαβ]; ring)

/-! ### The two normalisations, and the two answers -/

/-- With the corpus's `(T − q)(T + 1) = 0`, the classifying ideal is `(q + 1)`. -/
theorem span_eq_q_add_one (q : R) :
    Ideal.span ({q - (-1)} : Set R) = Ideal.span ({q + 1} : Set R) := by
  norm_num

/-- The extension is non-split exactly at `q = -1` — the double-root point of
    `(T − q)(T + 1)`, hence the non-semisimple point.

    Stated for `c = 1`, the generator of the classification. -/
theorem hecke_not_splits_at_neg_one {R : Type u} [CommRing R] [Nontrivial R]
    (q : R) (hq : q = -1) : ¬ Splits q (-1) (1 : R) :=
  not_splits_of_eq_of_ne_zero (by rw [hq]) one_ne_zero

/-! ### The nontriviality hypothesis is free over the QOU ground ring

    `hecke_not_splits_at_neg_one` carries `[Nontrivial R]`, and over an
    arbitrary `CommRing` it has to: in the zero ring `1 = 0` and every
    extension splits vacuously.

    It is **not** an added assumption in the QOU setting.
    `R_q = LaurentPolynomial ℤ` is nontrivial by instance search, so the
    hypothesis is discharged rather than assumed — recorded here as a checked
    fact instead of left for a reader to wonder about. -/

example : Nontrivial QOU.GroundRing.R_q := by infer_instance

/-- The non-split extension at `q = -1`, over the actual ground ring.

    No hypothesis beyond `q = -1`: nontriviality of `R_q` is supplied by
    instance search, so this is the corpus's own statement rather than a
    statement about some ring that might be trivial. -/
theorem groundRing_not_splits_at_neg_one (q : QOU.GroundRing.R_q) (hq : q = -1) :
    ¬ Splits q (-1) (1 : QOU.GroundRing.R_q) :=
  hecke_not_splits_at_neg_one q hq

end QOU.Mathlib.HeckeExtOne
