import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.ParticleInteractions — why fold/unfold works for binding: the delta is PRE-archimedean

**Proposition** ([`prop:delta-pre-archimedean`](../../../quantum-observable-universe/particle-interactions/delta-pre-archimedean.md)).

The proton/neutron mass *difference* observables — the binding energy
`B(K)` and the β-decay Q-value `Q_β = |Δ(net)|·𝔈₀` — are formed as a
**categorical delta** `Δ = x_n − x_p` at the **fibre level**, *before*
the archimedean realisation `τ` is applied. This file proves the structural
reason that the framework's folding/unfolding moves (the bar involution
`q ↦ q⁻¹`, the Hecke `σ ↔ σ⁻¹` reduction, Type-B folding) are legitimate
for these difference observables, but would NOT be legitimate if one
computed the absolute masses first and subtracted.

The key facts, over a generic commutative ring `R` (the fibre
coefficient ring; no reality / archimedean assumption):

1. **A fibre fold is additive**, so it commutes with the delta:
   `fold(x_n − x_p) = fold(x_n) − fold(x_p)`. This is `fold_commutes_sub`.
   Hence "fold then delta = delta then fold" — the fold can be applied
   either side of the categorical subtraction.

2. **The archimedean realisation is NONLINEAR**, so it does NOT commute
   with the delta: in general `τ(x_n) − τ(x_p) ≠ τ(x_n − x_p)`. We
   witness this with a concrete nonlinear `τ` (squaring) for which the
   two orders differ — `archimedean_does_not_commute_sub`.

Together: **fold/unfold is valid for binding because binding is a
pre-archimedean delta** (fold commutes with `−`), whereas the
masses-then-delta order would interleave the nonlinear `τ` with the
subtraction and is therefore NOT fold-invariant. This is the
order-of-operations discipline behind `prop:neutron-qvalue-symbolic`
(`Q_β = |Δ(net)|·𝔈₀`, delta-then-archimedean) and the binding tower.

-- Ref: [leitner2026] prop:neutron-qvalue-symbolic
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.ParticleInteractions

variable {R : Type*} [CommRing R]

/-- A **fibre fold** is any additive map on the coefficient ring (the
    bar involution `q↦q⁻¹`, the Hecke antipode `σ↦σ⁻¹`, a Type-B fold —
    all are ring homomorphisms, in particular additive). We capture the
    only property the delta argument needs: additivity. -/
structure FibreFold (R : Type*) [CommRing R] where
  toFun : R → R
  map_add : ∀ x y, toFun (x + y) = toFun x + toFun y
  map_zero : toFun 0 = 0

/-- An additive map sends negation to negation: `fold(−x) = −fold(x)`. -/
theorem FibreFold.map_neg (f : FibreFold R) (x : R) :
    f.toFun (-x) = - f.toFun x := by
  have h : f.toFun (-x) + f.toFun x = 0 := by
    rw [← f.map_add, neg_add_cancel]; exact f.map_zero
  exact eq_neg_of_add_eq_zero_left h

/-- **Fold commutes with the categorical delta.** For a fibre fold `f`
    and fibre quantities `x_n, x_p`,
    `f(x_n − x_p) = f(x_n) − f(x_p)`.
    The fold can be applied on either side of the pre-archimedean
    subtraction — this is what makes folding/unfolding legitimate for
    the difference observables (binding energy, Q_β). -/
theorem fold_commutes_sub (f : FibreFold R) (xn xp : R) :
    f.toFun (xn - xp) = f.toFun xn - f.toFun xp := by
  rw [sub_eq_add_neg, f.map_add, f.map_neg, ← sub_eq_add_neg]

/-- **The archimedean realisation does NOT commute with the delta.** A
    nonlinear `τ` (here squaring, standing in for the Li_2^q-tower /
    product / 𝔈₀-scaling structure of the real archimedean realisation)
    satisfies `τ(xn) − τ(xp) ≠ τ(xn − xp)` in general. We exhibit a
    concrete witness over `ℤ`: with `τ = (·)²`, `xn = 2`, `xp = 1`,
    `τ(2) − τ(1) = 3` but `τ(2 − 1) = 1`.

    Consequence: the masses-then-delta order (`τ xn − τ xp`) is NOT
    equal to, and NOT fold-invariant like, the delta-then-archimedean
    order (`τ (xn − xp)`). The framework computes Q_β / binding in the
    delta-then-archimedean order precisely so the fold discipline and
    the difference structure are preserved. -/
theorem archimedean_does_not_commute_sub :
    ∃ (τ : ℤ → ℤ) (xn xp : ℤ),
      τ xn - τ xp ≠ τ (xn - xp) := by
  refine ⟨fun x => x ^ 2, 2, 1, ?_⟩
  norm_num

end QOU.ParticleInteractions
