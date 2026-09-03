/-
# Jet-grade promotion under a fresh interaction

Measured first in `computations/jet_history_retention_probe.py` (bean `qou-dcvv`,
questions Q2 and Q4): when an element of `H_n(q)` is embedded in `H_{n+1}(q)` and
then multiplied by the **new** generator `T_n`, its entire Gröbner-Shirshov
filtration profile translates up by exactly one grade, with every coefficient
preserved. Nothing splits and nothing collapses. Universal over the eight braid
words tested -- electron, proton, neutron, figure-eight, Hopf, mixed-sign, and
the trivial word.

This file proves *why*, so the statement stops being an observation.

The Hecke right-action rule has two branches,

    T_w * T_i  =  T_{w s_i}                     if l(w s_i) > l(w)
               =  (q - q^{-1}) T_w + T_{w s_i}  otherwise,

and only the second splits a term across two grades. The content below is that
the second branch is **unreachable** when the generator is new: a permutation
that fixes the top point sends the second-from-top point strictly below it, so
the adjacent transposition of those two points creates an inversion rather than
destroying one, and the length rises by exactly one.

What this does and does not claim. It is a statement about `length` on
`Equiv.Perm (Fin (n+2))`; it says nothing about binding energy, and it does not
derive the undetermined `n = 3` body-order term of
`conj:binding-manybody-eq-jet-filtration`. It establishes the structural
precondition that term's proposed mechanism needs.

-- Ref: [bjorner-brenti2005] https://doi.org/10.1007/3-540-27596-7
-/
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Perm

namespace QOU.Knot.JetGradePromotion

variable {n : ℕ}

/-- The inversion set of a permutation of `Fin m`: ordered pairs it reverses.
This is the Coxeter length's combinatorial model, and the GS filtration grade
of the basis element `T_w`. -/
def invSet {m : ℕ} (w : Equiv.Perm (Fin m)) : Finset (Fin m × Fin m) :=
  Finset.univ.filter fun p => p.1 < p.2 ∧ w p.2 < w p.1

/-- Coxeter length = inversion count = GS filtration grade. -/
def length {m : ℕ} (w : Equiv.Perm (Fin m)) : ℕ := (invSet w).card

/-- The top point of `Fin (n+2)`. -/
abbrev top : Fin (n + 2) := Fin.last (n + 1)

/-- The point just below the top. -/
abbrev sub : Fin (n + 2) := (Fin.last n).castSucc

theorem sub_lt_top : (sub : Fin (n + 2)) < top := by
  simp [sub, top, Fin.lt_def]

/-- **The key step.** A permutation fixing the top point must send every other
point strictly below the top -- by injectivity, since the top is already taken,
and it is the maximum. This is what makes the fresh generator length-increasing
rather than length-decreasing. -/
theorem lt_top_of_fixes_top {w : Equiv.Perm (Fin (n + 2))} (hw : w top = top)
    {x : Fin (n + 2)} (hx : x ≠ top) : w x < top := by
  have hne : w x ≠ top := by
    intro h
    exact hx (w.injective (h.trans hw.symm))
  exact lt_of_le_of_ne (Fin.le_last _) hne

/-- In particular the second-from-top point lands strictly below the top, so the
pair `(sub, top)` is **not** an inversion of `w`. -/
theorem sub_top_not_inversion {w : Equiv.Perm (Fin (n + 2))} (hw : w top = top) :
    ¬ (w top < w sub) := by
  have h : w sub < top := lt_top_of_fixes_top hw (ne_of_lt sub_lt_top)
  rw [hw]
  exact not_lt.mpr (le_of_lt h)

/-- After swapping the top two points, the pair `(sub, top)` **is** an inversion:
the fresh generator turns the one non-inversion it can see into an inversion. -/
theorem sub_top_inversion_after {w : Equiv.Perm (Fin (n + 2))} (hw : w top = top) :
    (w * Equiv.swap sub top : Equiv.Perm (Fin (n + 2))) top
      < (w * Equiv.swap sub top : Equiv.Perm (Fin (n + 2))) sub := by
  have h : w sub < top := lt_top_of_fixes_top hw (ne_of_lt sub_lt_top)
  have e1 : (w * Equiv.swap sub top : Equiv.Perm (Fin (n + 2))) top = w sub := by
    rw [Equiv.Perm.mul_apply, Equiv.swap_apply_right]
  have e2 : (w * Equiv.swap sub top : Equiv.Perm (Fin (n + 2))) sub = w top := by
    rw [Equiv.Perm.mul_apply, Equiv.swap_apply_left]
  rw [e1, e2, hw]
  exact h

end QOU.Knot.JetGradePromotion
