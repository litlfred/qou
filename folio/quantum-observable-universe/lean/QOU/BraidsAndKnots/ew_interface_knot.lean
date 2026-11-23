import Mathlib.Tactic

/-!
# QOU.BraidsAndKnots.ew_interface_knot

**Canonical declaration** for content block EW interface knot.

This module defines the combinatorial skeleton of the EW interface knot and
proves it. Until 2026-11-20 (bean `qou-6qbv`) it carried a context class whose
fields were the bare equations `n_strands = 6`, `exp_W = 4 ∧ …`,
`n_adjacent_pair_generators = 2 ∧ …` on free `ℕ` fields, and the declaration
projected them back out: every instance chose the numbers, so nothing was
asserted. The numbers are now computed from the strand/generator data.

What stays prose: the physical identification of `σ_1^4, σ_3^6, σ_5^8` with
`W, Z, H` (`conj:hoefsmit-ew-cell-content`) and the bar-self-duality reading.

Note: the chapter-dir uses singular `QOU.BraidKnot` for most blocks;
this plural `QOU.BraidsAndKnots` namespace was inherited from existing
`.ts` lean.ref URIs (a pre-existing convention drift).
-/

namespace QOU.BraidsAndKnots

/-- Strands of `H_6(q)`, numbered `1 … 6`; generator `σ_i` (`i ∈ 1 … 5`)
crosses strands `i` and `i + 1`. -/
def ewStrands : Finset ℕ := Finset.Icc 1 6
def ewGenerators : Finset ℕ := Finset.Icc 1 5

/-- The EW carrier generators `σ_1, σ_3, σ_5` with exponents `4, 6, 8`
(`W, Z, H`). -/
def ewCarrierExponent : ℕ → ℕ
  | 1 => 4
  | 3 => 6
  | 5 => 8
  | _ => 0

def ewCarriers : Finset ℕ := ewGenerators.filter (fun i => ewCarrierExponent i ≠ 0)

/-- The strand pair a generator acts on. -/
def strandPair (i : ℕ) : Finset ℕ := {i, i + 1}

/-- The adjacent-pair generators: the generators that are not EW carriers. -/
def ewAdjacentPairGenerators : Finset ℕ := ewGenerators \ ewCarriers

/-- The carrier pairs containing a given strand. -/
def carrierOf (s : ℕ) : Finset ℕ := ewCarriers.filter (fun c => s ∈ strandPair c)

/-- An EW interface word: a non-empty signed braid word in the adjacent-pair
generators `σ_2, σ_4` only. -/
def IsEwInterfaceWord (w : List (ℕ × Bool)) : Prop :=
  w ≠ [] ∧ ∀ l ∈ w, l.1 ∈ ewAdjacentPairGenerators

/-- **Content statement** (from manuscript):

**Definition (electroweak interface knot $\Delta_I$).**
*Let $R$ be the categorical coefficient ring with $q \in R$
generic (not a root of unity in $R$, $q \neq 1$). Inside the
$n = 6$ Hecke algebra $H_6(q)$ over $R$, the **electroweak
interface knot** $\Delta_I$ is a non-empty word in the
**adjacent-pair generators** $\sigma_2$ and $\sigma_4$ — i.e. the
generators that connect the disjoint strand-pairs $(1,2),
(3,4), (5,6)$ on which the EW carriers
$W \leftrightarrow \sigma_1^{\,4}$, $Z \leftrightarrow \sigma_3^{\,6}$,
$H \leftrightarrow \sigma_5^{\,8}$ act
([`conj:hoefsmit-ew-cell-content`](#conj:hoefsmit-ew-cell-content)).*

    Proved below: the carriers are `σ_1, σ_3, σ_5`; their strand pairs are
    pairwise disjoint and cover the six strands; the non-carrier generators
    are exactly `σ_2, σ_4`; and each of these crosses between two different
    carrier pairs. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/ew-interface-knot.ts
theorem ew_interface_knot :
    ewCarriers = {1, 3, 5} ∧
    (ewCarrierExponent 1 = 4 ∧ ewCarrierExponent 3 = 6 ∧ ewCarrierExponent 5 = 8) ∧
    ((ewCarriers : Set ℕ).PairwiseDisjoint strandPair) ∧
    ewCarriers.biUnion strandPair = ewStrands ∧
    ewAdjacentPairGenerators = {2, 4} ∧
    (∀ g ∈ ewAdjacentPairGenerators, ∃ c ∈ ewCarriers, ∃ c' ∈ ewCarriers,
        c ≠ c' ∧ g ∈ strandPair c ∧ g + 1 ∈ strandPair c') := by
  refine ⟨by decide, ⟨rfl, rfl, rfl⟩, ?_, by decide, by decide, by decide⟩
  intro a ha b hb hab
  simp only [Finset.coe_insert, Finset.coe_singleton, Set.mem_insert_iff,
    Set.mem_singleton_iff, show ewCarriers = {1, 3, 5} by decide] at ha hb
  rcases ha with rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl <;>
    first | exact absurd rfl hab | (simp [Function.onFun, strandPair])

/-- The word `σ_2 σ_4⁻¹` is an EW interface word, so the class is non-empty;
`σ_1` alone is not one. -/
theorem ew_interface_word_examples :
    IsEwInterfaceWord [(2, true), (4, false)] ∧ ¬ IsEwInterfaceWord [(1, true)] := by
  refine ⟨⟨by simp, by decide⟩, fun h => ?_⟩
  have := h.2 (1, true) (by simp)
  revert this; decide

end QOU.BraidsAndKnots
