import Mathlib.GroupTheory.Coxeter.Length
import QOU.Hecke.SymmetricCoxeter

/-!
# QOU.BraidKnot.HeckeMaxLength — a maximal-length element of a finite set of permutations

Murphy's leading term is `d(s)⁻¹ · w_λ · d(t)`, where `w_λ` is the **longest element** of the Young
subgroup `S_λ`. That object exists nowhere in this corpus and nowhere in the pinned Mathlib:
measured against a positive control, `CoxeterSystem` is 3 oleans, `IsReduced` 58, and
`longestElement` is **0**. So the (C1) triangularity argument has a missing prerequisite, and this
file supplies the part of it that is actually needed.

## Existence, not uniqueness — and why that is enough

The classical statement is that a finite Coxeter group has a **unique** longest element. Uniqueness
is a real theorem and is *not* proved here.

It is also not required. The consumer is `Triangular` (`SpechtStandardBasis`), whose three fields
ask for *some* injective `lead` with a unit diagonal and support bounded above — not for a
canonical one. So a choice of maximiser suffices, and existence of a maximiser in a nonempty finite
set is elementary.

Stating this explicitly because the gap between "exists" and "the" is exactly where a formalisation
quietly acquires an unproved uniqueness assumption.

## What this does NOT settle

`lead_inj` — that distinct tableau pairs give distinct leading permutations — is **not** made easier
by having a maximiser. It is the hard field of `Triangular`, and it is what forces something
canonical in the classical treatment. This file removes one prerequisite; it does not touch that.

Ground ring: none — pure combinatorics on `Equiv.Perm (Fin (n+1))` and `ℕ` lengths.
-/

namespace QOU.BraidKnot.HeckeMaxLength

open QOU.Hecke.SymmetricCoxeter

variable (n : ℕ)

/-- The Coxeter length of a permutation, in the type-`A` system used by the `T_w` basis. -/
noncomputable def len (w : Equiv.Perm (Fin (n + 1))) : ℕ :=
  (permCoxeterSystem n).length w

/-- **A maximal-length element exists** in any nonempty finite set of permutations.

Elementary — a maximiser of an `ℕ`-valued function on a nonempty `Finset`. It is the existence half
of "the longest element of `S_λ`"; uniqueness is a separate, genuinely harder statement and is not
claimed. -/
theorem exists_maxLength (S : Finset (Equiv.Perm (Fin (n + 1)))) (hS : S.Nonempty) :
    ∃ w ∈ S, ∀ v ∈ S, len n v ≤ len n w := by
  classical
  obtain ⟨w, hwS, hw⟩ := S.exists_max_image (len n) hS
  exact ⟨w, hwS, hw⟩

/-- **A choice of maximal-length element.** Noncomputable, and deliberately *a* choice rather than
*the* longest element: uniqueness is not proved here and `Triangular` does not need it. -/
noncomputable def maxLenElt (S : Finset (Equiv.Perm (Fin (n + 1)))) (hS : S.Nonempty) :
    Equiv.Perm (Fin (n + 1)) :=
  (exists_maxLength n S hS).choose

theorem maxLenElt_mem (S : Finset (Equiv.Perm (Fin (n + 1)))) (hS : S.Nonempty) :
    maxLenElt n S hS ∈ S :=
  (exists_maxLength n S hS).choose_spec.1

theorem le_len_maxLenElt (S : Finset (Equiv.Perm (Fin (n + 1)))) (hS : S.Nonempty)
    {v : Equiv.Perm (Fin (n + 1))} (hv : v ∈ S) :
    len n v ≤ len n (maxLenElt n S hS) :=
  (exists_maxLength n S hS).choose_spec.2 v hv

/-- A subgroup's underlying `Finset` is nonempty — it contains `1`. This is the instance the Young
subgroup needs to feed the above. -/
theorem subgroup_finset_nonempty (H : Subgroup (Equiv.Perm (Fin (n + 1))))
    [DecidablePred (· ∈ H)] : ({w | w ∈ H} : Finset (Equiv.Perm (Fin (n + 1)))).Nonempty :=
  ⟨1, by simp⟩

end QOU.BraidKnot.HeckeMaxLength
