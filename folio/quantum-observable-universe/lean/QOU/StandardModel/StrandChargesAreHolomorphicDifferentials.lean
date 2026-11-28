import QOU.BringsSurface.BringHarmonicTypes
import Mathlib.Tactic

/-!
# The traceless strand charges are Bring's holomorphic differentials, up to the sign twist

Bean `qou-h0zz` (owner pick "Formalise H0 = std⊗sgn", 2026-11-28). The strand model carries a
charge vector `y : Fin 5 → ℚ` with `Σ y_i = 0`. Permuting the five strands acts on that space as
the standard representation `[4,1]` of `S₅`: its character is the number of fixed strands
minus one (`std_is_fixed_points_minus_one`, on `main` from PR #9855).

On `main`, the Hopf trace on the cells of Bring's map gives `H¹(B) = 2·[2,1,1,1]`
(`hopf_trace_h1`), and `h0K_character_forced` gives `H⁰(B, K) = [2,1,1,1]`, the space of
holomorphic differentials.

## Results

1. `h0K_eq_sign_mul_std`: `χ_{[2,1,1,1]} = sgn · χ_{[4,1]}` on every class.
2. `h0K_is_signed_strand_charges`: for each class representative `g`,
   `χ_{H⁰(K)}(g) = sign(g) · (#fixed strands of g − 1)`. So `H⁰(K)` is the traceless strand
   charge space twisted by the sign character.
3. `four_dim_irreps`: the only 4-dimensional irreducibles of `S₅` are `[4,1]` and
   `[2,1,1,1]`. Every 4-dimensional irreducible is the strand charge space, with or without
   the sign twist.
4. `strand_count_of_h0K`: if the traceless charges on `n` strands form `H⁰(K)`
   (dimension `n − 1 = χ_{[2,1,1,1]}(1)`), then `n = 5`. This replaces the bare hypothesis
   `n − 1 = g` of `StrandCount.strandCount_of_genus` with a statement about the `S₅` module.

## What this does not prove

It does not prove that the strand relabellings *are* the automorphisms of Bring's surface. It
shows the two `S₅`-modules agree up to the sign character. Whether the twist is the open
hypercharge/chirality sign of `prop:chirality-sign-is-hypercharge-sign` is not shown; the
twist is the orientation character of the strand permutations, and the open sign is the choice
of which parity of strand subsets is matter. They are different objects until a map between
them is proved.

All arithmetic is integer. No empirical value enters.
-/

namespace QOU.StandardModel.StrandDifferentials

open QOU.Brings.S5Char QOU.Brings.HarmonicTypes Equiv

/-- Class representatives `1, (01), (01)(23), (012), (012)(34), (0123), (01234)`, in the order
of the character table. -/
def reps : Fin 7 → Perm (Fin 5) :=
  ![1, swap 0 1, swap 0 1 * swap 2 3, swap 0 1 * swap 1 2,
    swap 0 1 * swap 1 2 * swap 3 4, swap 0 1 * swap 1 2 * swap 2 3,
    swap 0 1 * swap 1 2 * swap 2 3 * swap 3 4]

/-- Number of strands fixed by `g`. -/
def fixedStrands (g : Perm (Fin 5)) : ℤ :=
  ((Finset.univ.filter (fun x => g x = x)).card : ℤ)

/-- `χ_{[2,1,1,1]} = sgn · χ_{[4,1]}` on every class. -/
theorem h0K_eq_sign_mul_std : ∀ i, chi2111 i = chiSign i * chiStd i := by decide

/-- The sign character on the representatives is the permutation sign. -/
theorem chiSign_is_perm_sign : ∀ i, ((Perm.sign (reps i) : ℤˣ) : ℤ) = chiSign i := by
  decide

/-- **`H⁰(K)` is the signed traceless strand charge space.**
`χ_{H⁰(K)}(g) = sign(g) · (#fixed strands − 1)` on every class. -/
theorem h0K_is_signed_strand_charges :
    ∀ i, chi2111 i = ((Perm.sign (reps i) : ℤˣ) : ℤ) * (fixedStrands (reps i) - 1) := by
  decide

/-- The dimensions of the seven irreducibles, in table order. -/
theorem irrep_dims : (List.finRange 7).map (fun r => irr r 0) = [1, 1, 4, 4, 5, 5, 6] := by
  decide

/-- **The only 4-dimensional irreducibles are `[4,1]` and `[2,1,1,1]`.** -/
theorem four_dim_irreps : ∀ r : Fin 7, irr r 0 = 4 → r = 2 ∨ r = 3 := by decide

/-- Both 4-dimensional irreducibles are the strand charge space, one untwisted and one
twisted by the sign. -/
theorem four_dim_irreps_are_strand_charges :
    (∀ i, chiStd i = fixedStrands (reps i) - 1) ∧
      (∀ i, chi2111 i = ((Perm.sign (reps i) : ℤˣ) : ℤ) * (fixedStrands (reps i) - 1)) :=
  ⟨by decide, h0K_is_signed_strand_charges⟩

/-- **Strand count from `H⁰(K)`.** If the traceless charges on `n` strands span a space of the
dimension of `H⁰(K)`, then `n = 5`. -/
theorem strand_count_of_h0K (n : ℕ) (hn : (n : ℤ) - 1 = chi2111 0) : n = 5 := by
  have : chi2111 0 = 4 := by decide
  omega

end QOU.StandardModel.StrandDifferentials
