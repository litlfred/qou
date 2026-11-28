import Mathlib.Tactic

/-!
# Bring's sign twist exchanges hypercharge with its negative

Bean `qou-h0zz` (owner pick "Sign twist = hypercharge sign", 2026-11-28).
`prop:strand-charges-are-holomorphic-differentials` shows that Bring's holomorphic
differentials `H⁰(K) = [2,1,1,1]` are the traceless strand charges twisted by the sign
character: `g · y = sgn(g) · (y ∘ g⁻¹)`. This file asks whether that twist fixes the sign of
hypercharge. It does not: it exchanges `Y` and `−Y`.

## Results

1. `untwisted_fixes_Y`: the colour and isospin swaps fix `Y = (−2,−2,−2,3,3)` under plain
   relabelling.
2. `twist_flips_Y_isospin`, `twist_flips_Y_colour`: under the twisted action, the odd elements
   of `S₃ × S₂` send `Y` to `−Y`.
3. `twist_fixes_Y_even`: the even element `(01)(34)` fixes `Y`. So `S₃ × S₂` acts on the line
   `ℚ·Y` by its sign character.
4. `twisted_colour_invariant_eq_zero`: a charge vector fixed by the twisted action of the two
   colour swaps `(01)`, `(12)` is zero. No nonzero charge, hypercharge included, is invariant.

## Reading

If the strand charges carry `H⁰(K)` rather than `[4,1]`, the colour and isospin symmetries
exchange `Y` with `−Y`. Then the sign of hypercharge is not invariant data of the
`S₃ × S₂`-module. Choosing it breaks the symmetry to the even subgroup. This is a structural
exclusion for one ingredient: nothing built only from the twisted `S₃ × S₂` action can fix the
sign, because that action provably carries `Y` to `−Y`. It does not exclude other upstream
sources of the sign.

All arithmetic is over `ℚ`. No empirical value enters.
-/

namespace QOU.StandardModel.BringTwist

open Equiv

/-- The twisted action `g · y = sgn(g) · (y ∘ g⁻¹)` on charge vectors. -/
def twist (g : Perm (Fin 5)) (y : Fin 5 → ℚ) : Fin 5 → ℚ :=
  fun i => ((Perm.sign g : ℤˣ) : ℤ) * y (g⁻¹ i)

/-- Hypercharge in units of `1/6`. -/
def Y : Fin 5 → ℚ := ![-2, -2, -2, 3, 3]

theorem untwisted_fixes_Y :
    (fun i => Y ((swap (3 : Fin 5) 4)⁻¹ i)) = Y ∧ (fun i => Y ((swap (0 : Fin 5) 1)⁻¹ i)) = Y := by
  constructor <;> funext i <;> fin_cases i <;> simp [Y, swap_apply_def]

theorem twist_flips_Y_isospin : twist (swap 3 4) Y = -Y := by
  funext i; fin_cases i <;> simp [twist, Y, Perm.sign_swap', swap_apply_def]

theorem twist_flips_Y_colour : twist (swap 0 1) Y = -Y := by
  funext i; fin_cases i <;> simp [twist, Y, Perm.sign_swap', swap_apply_def]

theorem twist_fixes_Y_even : twist (swap 0 1 * swap 3 4) Y = Y := by
  funext i; fin_cases i <;> simp [twist, Y, swap_apply_def]

theorem twisted_colour_invariant_eq_zero (y : Fin 5 → ℚ)
    (h1 : twist (swap 0 1) y = y) (h2 : twist (swap 1 2) y = y) : y = 0 := by
  have e := fun i => congrFun h1 i
  have f := fun i => congrFun h2 i
  have e0 := e 0; have e2 := e 2; have e3 := e 3; have e4 := e 4; have f0 := f 0
  simp [twist, Perm.sign_swap', swap_apply_def] at e0 e2 e3 e4 f0
  have e1 := e 1
  simp [twist, swap_apply_def] at e1
  funext i; fin_cases i <;> simp <;> linarith

end QOU.StandardModel.BringTwist
