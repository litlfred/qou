import QOU.MathlibExt.RegTraceGram
import Mathlib.RingTheory.SimpleRing.Basic

/-!
# QOU.MathlibExt.RegTraceGramNondegenerate — the CONVERSE of the Gram criterion

Bean `qou-kwoa`.

`QOU/MathlibExt/RegTraceGram.lean` proves one direction:

    det (Gram of regTraceBilin in a basis) ≠ 0   ⟹   A is semisimple

and its docstring records the intended next step as *computing* that determinant —
`det = [n]_q!`, i.e. Geck–Pfeiffer 7.2.6, `det(Gram) = ∏_λ (Schur_λ)^{f^λ}`.  That is the
hard half, and bean `qou-0y6h` was closed against it.

**The other direction makes the computation unnecessary for non-vanishing.**  Semisimplicity
of `H_n(q)` is now proved independently — via the Wedderburn decomposition
(`QOU.SchurWeyl.isSemisimpleRing_hecke_generic`), which owes the Gram determinant nothing.
So `det ≠ 0` follows from semisimplicity rather than the reverse, and the Schur-element
product is needed only for the determinant's **value**.

This file supplies the missing implication.  It is *not* a corollary of the forward one, and
it is not in Mathlib: `Algebra.traceForm_nondegenerate` is about **separable field
extensions**, whereas `regTraceForm x y = trace (L_{xy})` is the regular trace of a
possibly-noncommutative algebra.

## Where the characteristic hypothesis enters, and why it is not removable

On a block `Matrix (Fin d) (Fin d) K` the regular trace is `d ·` the ordinary matrix trace,
because left multiplication acts on `d` copies of the column space.  So the form is
`d · tr(xy)`, and it **degenerates exactly when `d = 0` in `K`**.  That is why the statement
carries a characteristic assumption and why the `[CharZero K]` on the Hecke side is
load-bearing rather than inherited noise: at `char p ∣ d_λ` the Gram determinant of a
genuinely semisimple algebra vanishes.

## Contents

* `regTraceForm_algEquiv` — the regular trace form is an algebra invariant.
* `regTraceBilin_nondegenerate_congr` — nondegeneracy transports along an `AlgEquiv`.
* `regTraceForm_mul_assoc` / `regTraceForm_one_one` — the two structural facts the radical
  argument runs on: associativity of the form, and `B(1,1) = finrank`.
* `regTraceBilin_nondegenerate_of_isSimpleRing` — **the key step.**  On a simple ring the
  radical is a two-sided ideal, hence `⊥` or `⊤`; `⊤` is excluded by `B(1,1) ≠ 0`.
-/

namespace QOU.MathlibExt

open Algebra LinearMap

variable {K A B : Type*} [Field K] [Ring A] [Ring B] [Algebra K A] [Algebra K B]

/-- **The regular trace form is an algebra invariant.**

`L_{e x} = e ∘ L_x ∘ e⁻¹` as a `K`-linear endomorphism, so the two traces agree by
`LinearMap.trace_conj'`.  Stated for the *product* `x * y` directly, since that is the shape
`regTraceForm` is defined in. -/
theorem regTraceForm_algEquiv [FiniteDimensional K A] [FiniteDimensional K B]
    (e : A ≃ₐ[K] B) (x y : A) :
    regTraceForm K B (e x) (e y) = regTraceForm K A x y := by
  have hmul : e x * e y = e (x * y) := (map_mul e x y).symm
  have hconj : lmul K B (e (x * y)) = e.toLinearEquiv.conj (lmul K A (x * y)) := by
    ext z
    simp [LinearEquiv.conj_apply]
  rw [regTraceForm, hmul, hconj, LinearMap.trace_conj', regTraceForm]

/-- **Nondegeneracy of the regular trace form transports along an algebra isomorphism.**

This is the step that lets a Gram determinant on one presentation of an algebra be settled
on another — here, transporting from the Wedderburn block product back to the `T_w` basis. -/
theorem regTraceBilin_nondegenerate_congr [FiniteDimensional K A] [FiniteDimensional K B]
    (e : A ≃ₐ[K] B) (h : (regTraceBilin K B).Nondegenerate) :
    (regTraceBilin K A).Nondegenerate := by
  intro x hx
  have hex : ∀ w : B, regTraceForm K B (e x) w = 0 := by
    intro w
    have := hx (e.symm w)
    rw [regTraceBilin_apply] at this
    rw [← regTraceForm_algEquiv e x (e.symm w), AlgEquiv.apply_symm_apply] at this
    exact this
  have : e x = 0 := h (e x) fun w => (regTraceBilin_apply (e x) w).trans (hex w)
  simpa using congrArg e.symm this

/-- **Associativity of the regular trace form.**  Both sides are `trace (L_z)` for the same
`z`, by `mul_assoc`.  This is what makes the form's radical a *two-sided* ideal rather than
merely a subspace. -/
theorem regTraceForm_mul_assoc [FiniteDimensional K A] (x y z : A) :
    regTraceForm K A (x * y) z = regTraceForm K A x (y * z) := by
  rw [regTraceForm, regTraceForm, mul_assoc]

/-- **`B(1, 1)` is the dimension.**  `L_1 = id`, so the trace is `finrank K A` in `K`.

This is the whole of the characteristic input: the radical argument below excludes the
degenerate case by `B(1,1) ≠ 0`, and `B(1,1)` is a *natural number cast into `K`*.  In
characteristic `p ∣ finrank K A` it vanishes and the argument genuinely fails — as it must,
since the Gram determinant of a semisimple algebra really does vanish there. -/
theorem regTraceForm_one_one [FiniteDimensional K A] :
    regTraceForm K A 1 1 = (Module.finrank K A : K) := by
  have hid : (lmul K A) ((1 : A) * 1) = LinearMap.id := by
    ext z; simp
  rw [regTraceForm, hid, LinearMap.trace_id]

/-- **The radical of the regular trace form, as a two-sided ideal.**

`{x | ∀ y, B(x, y) = 0}`.  Closure on the right is `regTraceForm_mul_assoc`; closure on the
left needs it *together with* the symmetry `regTraceForm_comm`, since the form is only
associative in the shape `B(xy, z) = B(x, yz)`. -/
noncomputable def regTraceRadical (K A : Type*) [Field K] [Ring A] [Algebra K A]
    [FiniteDimensional K A] : TwoSidedIdeal A :=
  TwoSidedIdeal.mk' {x : A | ∀ y, regTraceForm K A x y = 0}
    (fun y => by simp [regTraceForm])
    (fun {x y} hx hy z => by
      have h2 : regTraceForm K A (x + y) z = regTraceForm K A x z + regTraceForm K A y z := by
        simp [regTraceForm, add_mul]
      rw [h2, hx z, hy z, add_zero])
    (fun {x} hx y => by
      have h2 : regTraceForm K A (-x) y = -regTraceForm K A x y := by
        simp [regTraceForm, neg_mul]
      rw [h2, hx y, neg_zero])
    (fun {x y} hy z => by
      rw [regTraceForm_comm, ← regTraceForm_mul_assoc, regTraceForm_comm]
      exact hy (z * x))
    (fun {x y} hx z => by
      rw [regTraceForm_mul_assoc]
      exact hx (y * z))

@[simp] theorem mem_regTraceRadical [FiniteDimensional K A] {x : A} :
    x ∈ regTraceRadical K A ↔ ∀ y, regTraceForm K A x y = 0 :=
  TwoSidedIdeal.mem_mk' _ _ _ _ _ _ x

/-- **Nondegeneracy of the regular trace form on a simple ring, given `B(1,1) ≠ 0`.**

The radical is a two-sided ideal (`regTraceRadical`), so simplicity forces it to be `⊥` or
`⊤`; `⊤` would put `1` in it and give `B(1, 1) = 0`.  This is the converse of
`isSemisimpleRing_of_regTraceBilin_nondegenerate`, and it is the direction that makes the
Gram-determinant *computation* unnecessary for non-vanishing. -/
theorem regTraceBilin_nondegenerate_of_isSimpleRing [FiniteDimensional K A] [IsSimpleRing A]
    (h : regTraceForm K A 1 1 ≠ 0) : (regTraceBilin K A).Nondegenerate := by
  have hbot : regTraceRadical K A = ⊥ := by
    by_contra hne
    exact h (mem_regTraceRadical.mp
      (IsSimpleRing.one_mem_of_ne_bot (regTraceRadical K A) hne) 1)
  intro x hx
  have hmem : x ∈ regTraceRadical K A :=
    mem_regTraceRadical.mpr fun y => (regTraceBilin_apply x y).symm.trans (hx y)
  rw [hbot] at hmem
  simpa using hmem

/-- **Simple + characteristic zero ⟹ the regular trace form is nondegenerate.**

The dimension hypothesis of `regTraceBilin_nondegenerate_of_isSimpleRing` is automatic here:
`B(1,1) = finrank K A` by `regTraceForm_one_one`, and a nontrivial finite-dimensional algebra
has positive dimension, which is nonzero in `K` exactly because `K` has characteristic zero. -/
theorem regTraceBilin_nondegenerate_of_isSimpleRing_charZero
    [FiniteDimensional K A] [IsSimpleRing A] [CharZero K] :
    (regTraceBilin K A).Nondegenerate := by
  refine regTraceBilin_nondegenerate_of_isSimpleRing ?_
  rw [regTraceForm_one_one]
  exact_mod_cast (Module.finrank_pos (R := K) (M := A)).ne'

end QOU.MathlibExt
