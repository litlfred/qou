import QOU.Hecke.TwBasis
import QOU.Hecke.PermLength

/-!
# QOU.Hecke.TwBasisPerm — the `Rs` branch, made concrete for type `Aₙ`

The bridge between the two halves of the `T_w` programme (bean `qou-twwf`).

`QOU.Hecke.TwBasis` defines `Rs i` for an arbitrary Coxeter system, with its
branch condition stated in terms of `cs.length`.  `QOU.Hecke.PermLength` proves
that for the type-`Aₙ` system that condition is a **comparison of `w` at two
adjacent points**.  This file joins them.

## What is proved

* `rsFun_perm` — `Rs i` acts on `T_w` by `T_{w sᵢ}` when `w(i) < w(i+1)` and by
  `(q-1)T_w + q T_{w sᵢ}` otherwise.

## Why it matters

Every branch in the braid relation `Rs i ∘ Rs j ∘ Rs i = Rs j ∘ Rs i ∘ Rs j` is
now decidable by the relative order of `w(i)`, `w(i+1)`, `w(i+2)` — a finite case
analysis, rather than the parabolic-coset argument the abstract route would
need (and which Mathlib has no machinery for: its `GroupTheory/Coxeter/`
directory has no strong exchange property, no parabolic subgroups and no
minimal coset representatives).

**The case analysis itself is not done here**, nor the distant-generator
commuting case, nor the algebra map `H_n(q) → End (W →₀ R)` and the `T_w`
independence that would follow from both.
-/

open Equiv Classical
namespace QOU.Hecke.TwBasis
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.Inversions

variable {n : ℕ} {R : Type*} [CommRing R] (q : R)

/-- **The branch condition, made concrete.**  For the type-`Aₙ` system the
    `Rs` branch is decided by comparing `w` at two adjacent points. -/
theorem rsFun_perm (i : Fin n) (w : Perm (Fin (n + 1))) :
    rsFun (permCoxeterSystem n) q i w =
      if w i.castSucc < w i.succ then
        Finsupp.single (w * Equiv.swap i.castSucc i.succ) (1 : R)
      else (q - 1) • Finsupp.single w (1 : R)
             + q • Finsupp.single (w * Equiv.swap i.castSucc i.succ) (1 : R) := by
  unfold rsFun
  simp only [permCox_simple, s_eq_swap, length_mul_swap_eq_succ_iff]

end QOU.Hecke.TwBasis
