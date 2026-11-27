import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import QOU.BraidsAndKnots.RationalAssociator.DrinfeldKohno

/-!
# The universal truncated Drinfeld–Kohno algebra on four strands

Bean `qou-3fdg` (stage 3a of the rational-associator plan, epic `qou-dk7p`).

The earlier files state every result in an arbitrary `ℚ`-algebra holding a `DK4` family in
which all words of a given length vanish. This file builds the **universal** such algebra,
`U4 N = ℚ⟨t₁₂, t₁₃, t₁₄, t₂₃, t₂₄, t₃₄⟩ / (Drinfeld–Kohno relations, words of length ≥ N)`,
which is `U(𝔱₄)` truncated at degree `N`, and proves:

* `dk4`: its generators form a `DK4` family;
* `word_eq_zero`: every word of length `N` in the generators vanishes;
* `lift`, `lift_t`: for every `ℚ`-algebra `R` with a `DK4` family whose words of length `N`
  vanish there is an algebra map `U4 N →ₐ[ℚ] R` sending generators to the family.

So the universal algebra exists, and the earlier statements, proved for all such families,
hold in it. The construction is a quotient of a free algebra; nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open FreeAlgebra

/-- The free algebra on the six generators `t₁₂, t₁₃, t₁₄, t₂₃, t₂₄, t₃₄` (indices `0 … 5`). -/
abbrev F4 := FreeAlgebra ℚ (Fin 6)

/-- The generators of `F4`, in the order `t₁₂, t₁₃, t₁₄, t₂₃, t₂₄, t₃₄`. -/
abbrev g (i : Fin 6) : F4 := ι ℚ i

/-- The fifteen pairs whose commutators the Drinfeld–Kohno relations kill:
three far relations and twelve near relations, in the order of the fields of `DK4`. -/
def dkPairs : List (F4 × F4) :=
  [(g 0, g 5), (g 1, g 4), (g 2, g 3),
   (g 0, g 1 + g 3), (g 1, g 0 + g 3), (g 3, g 0 + g 1),
   (g 0, g 2 + g 4), (g 2, g 0 + g 4), (g 4, g 0 + g 2),
   (g 1, g 2 + g 5), (g 2, g 1 + g 5), (g 5, g 1 + g 2),
   (g 3, g 4 + g 5), (g 4, g 3 + g 5), (g 5, g 3 + g 4)]

/-- The defining relation of `U4 N`: the Drinfeld–Kohno commutators and every word of length
`N` are identified with zero. -/
inductive Rel4 (N : ℕ) : F4 → F4 → Prop
  | comm (p : F4 × F4) (hp : p ∈ dkPairs) : Rel4 N (p.1 * p.2) (p.2 * p.1)
  | word (w : List (Fin 6)) (hw : w.length = N) : Rel4 N (w.map g).prod 0

/-- `U(𝔱₄)` truncated at degree `N`. -/
abbrev U4 (N : ℕ) := RingQuot (Rel4 N)

/-- The generator `tᵢⱼ` of `U4 N`. -/
def t (N : ℕ) (i : Fin 6) : U4 N := RingQuot.mkAlgHom ℚ (Rel4 N) (g i)

private theorem commute_of_mem {N : ℕ} {a b : F4} (h : (a, b) ∈ dkPairs) :
    Commute (RingQuot.mkAlgHom ℚ (Rel4 N) a) (RingQuot.mkAlgHom ℚ (Rel4 N) b) := by
  have := RingQuot.mkAlgHom_rel ℚ (Rel4.comm (N := N) (a, b) h)
  simpa [Commute, SemiconjBy, map_mul] using this

/-- The generators of `U4 N` form a Drinfeld–Kohno family. -/
theorem dk4 (N : ℕ) : DK4 (t N 0) (t N 1) (t N 2) (t N 3) (t N 4) (t N 5) := by
  exact
  ⟨by simpa [t, map_add] using commute_of_mem (N := N) (a := g 0) (b := g 5) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 1) (b := g 4) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 2) (b := g 3) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 0) (b := g 1 + g 3) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 1) (b := g 0 + g 3) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 3) (b := g 0 + g 1) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 0) (b := g 2 + g 4) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 2) (b := g 0 + g 4) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 4) (b := g 0 + g 2) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 1) (b := g 2 + g 5) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 2) (b := g 1 + g 5) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 5) (b := g 1 + g 2) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 3) (b := g 4 + g 5) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 4) (b := g 3 + g 5) (by simp [dkPairs]),
    by simpa [t, map_add] using commute_of_mem (N := N) (a := g 5) (b := g 3 + g 4) (by simp [dkPairs])⟩

/-- Every word of length `N` in the generators of `U4 N` vanishes. -/
theorem word_eq_zero (N : ℕ) (w : List (Fin 6)) (hw : w.length = N) :
    (w.map (t N)).prod = 0 := by
  have := RingQuot.mkAlgHom_rel ℚ (Rel4.word (N := N) w hw)
  simpa [t, map_list_prod, List.map_map, Function.comp_def] using this

section Lift

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- **Universal property.** A `DK4` family in which every word of length `N` vanishes is the
image of the generators of `U4 N` under a unique-on-generators algebra map. -/
noncomputable def lift (N : ℕ) (s : Fin 6 → R)
    (hdk : DK4 (s 0) (s 1) (s 2) (s 3) (s 4) (s 5))
    (hw : ∀ w : List (Fin 6), w.length = N → (w.map s).prod = 0) : U4 N →ₐ[ℚ] R :=
  RingQuot.liftAlgHom ℚ ⟨FreeAlgebra.lift ℚ s, by
    intro a b h
    cases h with
    | comm p hp =>
      simp only [dkPairs, List.mem_cons, List.not_mem_nil, or_false] at hp
      rcases hp with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl |
        rfl | rfl | rfl <;> simp only [map_mul, map_add, lift_ι_apply] <;>
      first
      | exact hdk.f12_34.eq | exact hdk.f13_24.eq | exact hdk.f14_23.eq
      | exact hdk.n12_3.eq | exact hdk.n13_2.eq | exact hdk.n23_1.eq
      | exact hdk.n12_4.eq | exact hdk.n14_2.eq | exact hdk.n24_1.eq
      | exact hdk.n13_4.eq | exact hdk.n14_3.eq | exact hdk.n34_1.eq
      | exact hdk.n23_4.eq | exact hdk.n24_3.eq | exact hdk.n34_2.eq
    | word w hw' =>
      simpa [map_list_prod, List.map_map, Function.comp_def] using hw w hw'⟩

@[simp] theorem lift_t (N : ℕ) (s : Fin 6 → R) (hdk) (hw) (i : Fin 6) :
    lift N s hdk hw (t N i) = s i := by
  simp [lift, t]

end Lift

end QOU.BraidsAndKnots.RationalAssociator
