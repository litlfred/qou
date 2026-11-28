import QOU.StandardModel.BringTwistFlipsHypercharge

/-!
# The hypercharge sign is the orientation of Bring's surface

Bean `qou-h0zz` (recommended option "Sign from Bring's orientation", 2026-11-28).

`QOU/BringsSurface/BringReflectionParity.lean` (PR #9874) gives the full isometry group
`S₅ × C₂` of Bring's surface, with `c` the central orientation reversal (complex conjugation),
and `H¹ = [2,1,1,1]⁺ ⊕ [2,1,1,1]⁻` (`hopf_trace_h1_reversing`, `h1_parity_balanced`). On the
copy `ε ∈ {+1, −1}` the element `(g, cᵏ)` acts on charge vectors by

  `(g, cᵏ) · y = εᵏ · sgn(g) · (y ∘ g⁻¹)`.

`ε = −1` is the reflection-odd copy, spanned by the forms `ω − c^* ω̄`.

## Results

1. `plus_copy_odd_flips`: in the `⁺` copy, the colour swap `(01)` and the isospin swap `(34)`
   send `Y` to `−Y`, with or without `c`. No orientation-reversing isometry rescues them.
2. `minus_copy_restores_colour_isospin`: in the `⁻` copy, the orientation-reversing
   isometries `((01), c)` and `((34), c)` fix `Y`, and so does the orientation-preserving even
   element `((01)(34), 1)`. So colour and isospin symmetry of hypercharge survives in the
   reflection-odd copy.
3. `minus_copy_c_flips`: in the `⁻` copy, `c` alone sends `Y` to `−Y`. `minus_copy_odd_flips`
   gives the same for `((01), 1)` and `((34), 1)`.

## Reading

Requiring hypercharge to keep its colour and isospin symmetry selects the `⁻` copy. In that
copy, reversing the orientation of Bring's surface reverses the sign of hypercharge. So the
open sign of `prop:chirality-sign-is-hypercharge-sign` is identified with the orientation of
Bring's surface, i.e. the choice of complex structure `H⁰(K)` against `conj H⁰(K)`.

This converts the open sign into a choice upstream. It does not fix the value, because both
orientations are isometric.

`stabiliser_of_Y`, `minus_copy_diagonal_fixes` and `plus_copy_odd_flips_all` extend the
generator checks to all twelve elements of `S₃ × S₂`, and show `S₃ × S₂` is exactly the
stabiliser of `Y` among the 120 permutations. Integer and rational arithmetic only. No empirical value enters.
-/

namespace QOU.StandardModel.BringOrientation

open Equiv QOU.StandardModel.BringTwist

/-- `(g, cᵏ)` on the copy `ε`: `εᵏ · sgn(g) · (y ∘ g⁻¹)`, `k = 1` when `rev`. -/
def act (ε : ℚ) (g : Perm (Fin 5)) (rev : Bool) (y : Fin 5 → ℚ) : Fin 5 → ℚ :=
  fun i => (if rev then ε else 1) * twist g y i

theorem act_eq (ε : ℚ) (g) (rev : Bool) (y : Fin 5 → ℚ) :
    act ε g rev y = (if rev then ε else 1) • twist g y := by
  funext i; simp [act]

theorem plus_copy_odd_flips (rev : Bool) :
    act 1 (swap 0 1) rev Y = -Y ∧ act 1 (swap 3 4) rev Y = -Y := by
  cases rev <;> simp [act_eq, twist_flips_Y_colour, twist_flips_Y_isospin]

theorem minus_copy_restores_colour_isospin :
    act (-1) (swap 0 1) true Y = Y ∧ act (-1) (swap 3 4) true Y = Y ∧
      act (-1) (swap 0 1 * swap 3 4) false Y = Y := by
  refine ⟨?_, ?_, ?_⟩ <;> simp [act_eq, twist_flips_Y_colour, twist_flips_Y_isospin,
    twist_fixes_Y_even]

theorem minus_copy_c_flips : act (-1) 1 true Y = -Y := by
  funext i; simp [act, twist]

theorem minus_copy_odd_flips :
    act (-1) (swap 0 1) false Y = -Y ∧ act (-1) (swap 3 4) false Y = -Y := by
  simp [act_eq, twist_flips_Y_colour, twist_flips_Y_isospin]

/-! ## All twelve elements of `S₃ × S₂` -/

/-- The permutations preserving the colour strands `{0,1,2}` (hence also `{3,4}`). -/
def colourIsospin : Finset (Perm (Fin 5)) :=
  Finset.univ.filter (fun g => ∀ x : Fin 5, (g x < 3 ↔ x < 3))

theorem colourIsospin_card : colourIsospin.card = 12 := by decide

/-- Integer twin of `twist`, for kernel evaluation. -/
def twistZ (g : Perm (Fin 5)) (y : Fin 5 → ℤ) : Fin 5 → ℤ :=
  fun i => ((Perm.sign g : ℤˣ) : ℤ) * y (g⁻¹ i)

/-- Integer hypercharge. -/
def YZ : Fin 5 → ℤ := ![-2, -2, -2, 3, 3]

theorem twist_Y_cast (g : Perm (Fin 5)) : twist g Y = fun i => ((twistZ g YZ i : ℤ) : ℚ) := by
  funext i; simp only [twist, twistZ, Int.cast_mul]; congr 1
  generalize g⁻¹ i = j; fin_cases j <;> simp [Y, YZ]

/-- **`S₃ × S₂` is exactly the stabiliser of hypercharge under plain relabelling**, over all
120 permutations. -/
theorem stabiliser_of_Y : ∀ g : Perm (Fin 5), (fun i => YZ (g⁻¹ i)) = YZ ↔ g ∈ colourIsospin := by
  decide +kernel

theorem twistZ_colourIsospin :
    ∀ g ∈ colourIsospin, twistZ g YZ = ((Perm.sign g : ℤˣ) : ℤ) • YZ := by
  decide +kernel

/-- Under the sign twist, every element of `S₃ × S₂` acts on `Y` by its sign. -/
theorem twist_colourIsospin (g : Perm (Fin 5)) (hg : g ∈ colourIsospin) :
    twist g Y = (((Perm.sign g : ℤˣ) : ℤ) : ℚ) • Y := by
  rw [twist_Y_cast, twistZ_colourIsospin g hg]
  funext i; fin_cases i <;> simp [YZ, Y]

/-- **The twisted diagonal fixes `Y` in the `⁻` copy.** Pairing each odd element of
`S₃ × S₂` with `c` fixes hypercharge, for all twelve elements. -/
theorem minus_copy_diagonal_fixes (g : Perm (Fin 5)) (hg : g ∈ colourIsospin) :
    act (-1) g (decide (Perm.sign g = -1)) Y = Y := by
  rw [act_eq, twist_colourIsospin g hg]
  rcases Int.units_eq_one_or (Perm.sign g) with h | h <;> simp [h]

/-- **In the `⁺` copy every odd element of `S₃ × S₂` sends `Y` to `−Y`**, with or without `c`. -/
theorem plus_copy_odd_flips_all (g : Perm (Fin 5)) (hg : g ∈ colourIsospin)
    (hodd : Perm.sign g = -1) (rev : Bool) : act 1 g rev Y = -Y := by
  rw [act_eq, twist_colourIsospin g hg, hodd]; cases rev <;> simp

end QOU.StandardModel.BringOrientation
