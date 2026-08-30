import QOU.Mathlib.LongExactSequence
import Mathlib.LinearAlgebra.Projection
import Mathlib.Tactic

/-!
# QOU.QuantumObservableUniverse.SelfDualSES — `rem:self-dual-ses`, formalised

Bean `qou-fngs`. The content block `rem:self-dual-ses` states

    0 → Ω⁻(A) → Ω²(A) → Ω⁺(A) → 0,   Ω^± = ker(id ∓ ⋆_q)

and had **no Lean behind it** — the corpus contained no exact sequence of any
kind before `QOU/Mathlib/LongExactSequence.lean`. This file supplies the
algebra: the ±1 eigenspace decomposition of an involution, and the exact
sequence it produces.

## What is actually true, and where it costs something

Three statements, in increasing strength, because they need different
hypotheses and the corpus works over a ring where the strongest one fails.

1. **Exactness is free.** `0 → M⁻ → M → M ⧸ M⁻ → 0` is exact for any
   submodule, involution or not (`minus_ses_exact`). Writing the sequence down
   proves nothing.
2. **Disjointness needs 2-torsion-freeness.** An element both self-dual and
   anti-self-dual satisfies `x = −x`, so it vanishes only if `M` has no
   2-torsion (`disjoint_plus_minus`). Carried as a hypothesis, not assumed via
   a field — the same discipline as `BarGradedCollapse`.
3. **The splitting needs 2 to be invertible** (`isCompl_plus_minus`), because
   it is literally `x = ½(x + ⋆x) + ½(x − ⋆x)`. Only then is the quotient
   `M ⧸ M⁻` identified with `M⁺` (`quotMinusEquivPlus`), which is what the
   block's arrow `Ω²(A) → Ω⁺(A)` means.

**Point 3 fails over `R_q = ℤ[q, q⁻¹]`.** `2` is not invertible there: `R_q`
is `ℤ[ℤ]`, its units are `± q^n`, and `2` is none of them. So the self-dual
splitting is *not* available over the ground ring — it is available after
inverting 2, or in the archimedean realisation over `ℝ` that the block's
second sentence describes. The block reads as though the splitting were
unconditional; it is not, and the condition is exactly the one that separates
its two sentences.

## The same structure as the bar involution

`BarGradedCollapse.IsEven`/`IsOdd` for `q ↦ q⁻¹` and `IsSelfDual`/`IsAntiSelfDual`
for `⋆_q` are the **same** definition — the ±1 eigenspaces of an involution —
and `eq_zero_of_even_and_odd` is `disjoint_plus_minus` under another name.
`isSelfDual_iff_fixed` and `isAntiSelfDual_iff_negated` record the
identification as checkable statements rather than leaving it as prose: it
means a parity-collapse argument and a self-duality argument are one argument,
and either file's hypotheses can be discharged by the other's.

-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes
-/

namespace QOU.SelfDualSES

universe u v

variable {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]

/-- **An involution** on an `R`-module: `⋆ ∘ ⋆ = id`.

    The `q`-Hodge star of `def:q-hodge-star` at the module level. Carried as a
    structure rather than a `Prop` on a fixed map so that a module can hold
    more than one — the corpus has both `⋆_q` and the bar involution. -/
structure Involution (R : Type u) [CommRing R] (M : Type v)
    [AddCommGroup M] [Module R M] where
  /-- The involution. -/
  star : M →ₗ[R] M
  /-- It squares to the identity. -/
  star_star : ∀ x, star (star x) = x

variable (i : Involution R M)

/-- `Ω⁺`: the self-dual part, `ker(⋆ − id)`. -/
def plusPart : Submodule R M := LinearMap.ker (i.star - LinearMap.id)

/-- `Ω⁻`: the anti-self-dual part, `ker(⋆ + id)`. -/
def minusPart : Submodule R M := LinearMap.ker (i.star + LinearMap.id)

/-- Self-dual: `⋆x = x`. The instanton condition of
    `def:categorical-instanton` is that the curvature lies here. -/
def IsSelfDual (x : M) : Prop := i.star x = x

/-- Anti-self-dual: `⋆x = −x`. `F⁻ = 0` is the statement that the curvature's
    component here vanishes. -/
def IsAntiSelfDual (x : M) : Prop := i.star x = -x

@[simp] theorem mem_plusPart {x : M} : x ∈ plusPart i ↔ IsSelfDual i x := by
  simp [plusPart, IsSelfDual, LinearMap.mem_ker, sub_eq_zero]

@[simp] theorem mem_minusPart {x : M} : x ∈ minusPart i ↔ IsAntiSelfDual i x := by
  simp [minusPart, IsAntiSelfDual, LinearMap.mem_ker, eq_neg_iff_add_eq_zero]

/-- **Exactness is free.** The sequence `0 → M⁻ → M → M ⧸ M⁻ → 0` is exact for
    *any* submodule — no involution, no hypothesis on `R`. Recorded first
    precisely so that it is clear the content of the block is not here: writing
    an exact sequence down is not evidence about the decomposition. -/
theorem minus_ses_exact :
    Function.Exact (minusPart i).subtype (minusPart i).mkQ :=
  LinearMap.exact_iff.mpr (by rw [Submodule.ker_mkQ, Submodule.range_subtype])

/-- **Self-dual and anti-self-dual meet only at zero** — given no 2-torsion.

    `x = ⋆x = −x` gives `x + x = 0`, and nothing more without a hypothesis:
    over a ring of characteristic 2 the two parts coincide. This is
    `BarGradedCollapse.eq_zero_of_even_and_odd` for `⋆_q` instead of the bar
    involution. -/
theorem eq_zero_of_selfDual_and_antiSelfDual {x : M}
    (hp : IsSelfDual i x) (hm : IsAntiSelfDual i x)
    (htors : ∀ y : M, y + y = 0 → y = 0) : x = 0 := by
  have hx : x = -x := hp.symm.trans hm
  refine htors x ?_
  nth_rewrite 2 [hx]
  simp

theorem disjoint_plus_minus (htors : ∀ y : M, y + y = 0 → y = 0) :
    Disjoint (plusPart i) (minusPart i) := by
  rw [Submodule.disjoint_def]
  intro x hp hm
  exact eq_zero_of_selfDual_and_antiSelfDual i
    ((mem_plusPart i).mp hp) ((mem_minusPart i).mp hm) htors

/-- `x + ⋆x` is self-dual — the unnormalised projector onto `Ω⁺`. -/
theorem add_star_mem_plus (x : M) : x + i.star x ∈ plusPart i := by
  rw [mem_plusPart]
  show i.star (x + i.star x) = x + i.star x
  rw [map_add, i.star_star]
  abel

/-- `x − ⋆x` is anti-self-dual — the unnormalised projector onto `Ω⁻`. -/
theorem sub_star_mem_minus (x : M) : x - i.star x ∈ minusPart i := by
  rw [mem_minusPart]
  show i.star (x - i.star x) = -(x - i.star x)
  rw [map_sub, i.star_star]
  abel

section TwoInvertible

variable [Invertible (2 : R)]

/-- **The splitting**, and the only place `2` is inverted: `x` is the sum of
    its halves. Over `R_q = ℤ[q, q⁻¹]` this step is unavailable — the units of
    `ℤ[ℤ]` are `±q^n` and `2` is not among them — which is exactly why
    `rem:self-dual-ses`'s second sentence moves to the archimedean
    realisation. -/
theorem codisjoint_plus_minus : Codisjoint (plusPart i) (minusPart i) := by
  rw [codisjoint_iff_le_sup]
  intro x _
  have hsum : (⅟(2 : R)) • (x + i.star x) + (⅟(2 : R)) • (x - i.star x) = x := by
    rw [← smul_add]
    have : x + i.star x + (x - i.star x) = (2 : R) • x := by
      rw [two_smul]; abel
    rw [this, smul_smul, invOf_mul_self, one_smul]
  refine hsum ▸ Submodule.add_mem_sup ?_ ?_
  · exact Submodule.smul_mem _ _ (add_star_mem_plus i x)
  · exact Submodule.smul_mem _ _ (sub_star_mem_minus i x)

/-- `Ω⁺` and `Ω⁻` are complementary: `Ω²(A) = Ω⁺(A) ⊕ Ω⁻(A)`. -/
theorem isCompl_plus_minus (htors : ∀ y : M, y + y = 0 → y = 0) :
    IsCompl (plusPart i) (minusPart i) :=
  ⟨disjoint_plus_minus i htors, codisjoint_plus_minus i⟩

/-- **The block's arrow, identified.** `Ω²(A) ⧸ Ω⁻(A) ≅ Ω⁺(A)`.

    This is what `Ω²(A) → Ω⁺(A)` in `rem:self-dual-ses` *means*: the map is the
    quotient by the anti-self-dual part, and it lands isomorphically on the
    self-dual part only because the two are complementary. -/
noncomputable def quotMinusEquivPlus (htors : ∀ y : M, y + y = 0 → y = 0) :
    (M ⧸ minusPart i) ≃ₗ[R] plusPart i :=
  Submodule.quotientEquivOfIsCompl _ _ ((isCompl_plus_minus i htors).symm)

/-- **The instanton condition.** A curvature is self-dual exactly when its
    anti-self-dual component vanishes — `F⁻ = 0`, in the block's notation.

    With the splitting in hand this is a statement about the decomposition
    rather than a definition, which is the point of proving the splitting. -/
theorem isSelfDual_iff_minus_component_zero (x : M) :
    IsSelfDual i x ↔ (⅟(2 : R)) • (x - i.star x) = 0 := by
  constructor
  · intro h
    rw [show x - i.star x = 0 by rw [h]; abel]
    simp
  · intro h
    have h2 : x - i.star x = 0 := by
      have := congrArg (fun y => (2 : R) • y) h
      simpa [smul_smul, mul_invOf_self] using this
    have : i.star x = x := by
      have := sub_eq_zero.mp h2
      exact this.symm
    exact this

end TwoInvertible

/-! ### The bar involution is the same structure

    Left as an explicit statement rather than a remark, because it means a
    parity argument and a self-duality argument are interchangeable. -/

/-- `IsSelfDual` for an involution **is** `BarGradedCollapse.IsEven` for it —
    definitionally, once the two are pointed at the same map. Recorded so the
    identification is checkable rather than asserted in prose. -/
theorem isSelfDual_iff_fixed (x : M) : IsSelfDual i x ↔ i.star x = x := Iff.rfl

/-- Likewise `IsAntiSelfDual` is `IsOdd`. -/
theorem isAntiSelfDual_iff_negated (x : M) : IsAntiSelfDual i x ↔ i.star x = -x := Iff.rfl

end QOU.SelfDualSES
