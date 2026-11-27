import QOU.EightfoldWay.NeutralLeptonFixesCharges

/-!
# QOU.EightfoldWay.FermiPairWedge — Fermi exchange puts a strand pair in `Λ²5`

The proposition `prop:neutral-lepton-fixes-charges` takes the matter content `5̄ ⊕ Λ²5` as an
input. This module splits that input into smaller pieces and proves the steps between them.

Two strands, each labelled by an index of `5 = C ⊕ V` (colour `0,1,2`, isospin `3,4`), carry a
pair state `f : Fin 5 → Fin 5 → ℚ`. **Fermi exchange** is the condition `f j i = -f i j`.

* `fermi_diag_zero`, `fermi_ext` — a Fermi pair state vanishes on equal labels and is fixed by
  its values on `i < j`. So the Fermi channel is indexed by the ten wedges `eᵢ ∧ eⱼ`.
* `card_colourColour`, `card_colourIso`, `card_isoIso` — the ten wedges split by label type as
  `3 + 6 + 1`: no colour sextet, and exactly one colour singlet.
* `fermi_removes_charge_two` — the symmetric pair `e₃ ⊗ e₃`, which Fermi exchange removes, is a
  colour singlet of charge `2` at `α = 1/6`; the Fermi channel's only colour singlet has charge `1`.
* `cubic_5bar`, `cubic_wedge`, `cubic_sym` — the cubic trace of `Y₀` is `-30` on `5̄`, `30` on
  `Λ²5` and `270` on `Sym²5`.
* `cubic_cancel_iff` — `a·5̄ ⊕ c·Λ²5` has vanishing cubic `Y₀`-trace iff `a = c`.

## What stays an input

1. **Fermi exchange** on strand pairs (spin–statistics is not derived here; same input as
   `ColourSingletSelectionRule`).
2. **That matter is one strand (`5̄`) and one strand pair (`Λ²5`)** — the count of strands per
   multiplet is not derived.
3. **Vanishing of the cubic trace** is a consistency condition imposed, not derived. It pairs
   `5̄` with `Λ²5` one to one, and `5 ⊕ 5̄` cancels too (`cubic_5_add_5bar`), so it does not by
   itself exclude vector-like content.

Base ring `ℚ`; no empirical input.
-/

namespace QOU.EightfoldWay.FermiPairWedge

open QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant QOU.EightfoldWay.NeutralLeptonFixesCharges

/-- Fermi exchange on a two-strand state. -/
def IsFermi (f : Fin 5 → Fin 5 → ℚ) : Prop := ∀ i j, f j i = -f i j

theorem fermi_diag_zero {f : Fin 5 → Fin 5 → ℚ} (hf : IsFermi f) (i : Fin 5) : f i i = 0 := by
  have := hf i i
  linarith

/-- A Fermi pair state is determined by its values on `i < j`. -/
theorem fermi_ext {f g : Fin 5 → Fin 5 → ℚ} (hf : IsFermi f) (hg : IsFermi g)
    (h : ∀ i j, i < j → f i j = g i j) : f = g := by
  funext i j
  rcases lt_trichotomy i j with hij | rfl | hij
  · exact h _ _ hij
  · rw [fermi_diag_zero hf, fermi_diag_zero hg]
  · rw [← neg_neg (f i j), ← hf i j, ← neg_neg (g i j), ← hg i j, h _ _ hij]

/-- Wedge labels `i < j`. -/
def wedges : Finset (Fin 5 × Fin 5) := Finset.univ.filter fun p => p.1 < p.2

def colourColour : Finset (Fin 5 × Fin 5) := wedges.filter fun p => p.2.val < 3
def colourIso : Finset (Fin 5 × Fin 5) := wedges.filter fun p => p.1.val < 3 ∧ 3 ≤ p.2.val
def isoIso : Finset (Fin 5 × Fin 5) := wedges.filter fun p => 3 ≤ p.1.val

theorem card_wedges : wedges.card = 10 := by decide
theorem card_colourColour : colourColour.card = 3 := by decide
theorem card_colourIso : colourIso.card = 6 := by decide
theorem card_isoIso : isoIso.card = 1 := by decide

/-- Fermi exchange removes the charge-`2` colour singlet `e₃ ⊗ e₃`; the Fermi channel's only
colour singlet `e₃ ∧ e₄` has charge `1`. -/
theorem fermi_removes_charge_two :
    qWeight10 (1 / 6 : ℚ) 3 3 = 2 ∧ qWeight10 (1 / 6 : ℚ) 3 4 = 1 ∧
      isoIso = {((3 : Fin 5), (4 : Fin 5))} := by
  obtain ⟨-, -, -, h3, h4⟩ := qWeight5_apply (K := ℚ) (1 / 6)
  refine ⟨?_, ?_, by decide⟩ <;>
  · rw [qWeight10, h3]
    try rw [h4]
    norm_num

/-- The `Y₀` weights on `5`. -/
def y (i : Fin 5) : ℚ := Y0 ℚ i i

theorem y_apply : y 0 = -2 ∧ y 1 = -2 ∧ y 2 = -2 ∧ y 3 = 3 ∧ y 4 = 3 := by
  simp [y, Y0]

/-- Cubic `Y₀`-trace on `5`. -/
def cubic5 : ℚ := ∑ i, y i ^ 3
/-- Cubic `Y₀`-trace on `5̄`. -/
def cubic5bar : ℚ := ∑ i, (-y i) ^ 3
/-- Cubic `Y₀`-trace on `Λ²5`. -/
def cubicWedge : ℚ := ∑ i, ∑ j, if i < j then (y i + y j) ^ 3 else 0
/-- Cubic `Y₀`-trace on `Sym²5`. -/
def cubicSym : ℚ := ∑ i, ∑ j, if i ≤ j then (y i + y j) ^ 3 else 0

theorem cubic_5 : cubic5 = 30 := by
  simp [cubic5, y, Y0, Fin.sum_univ_five]; norm_num

theorem cubic_5bar : cubic5bar = -30 := by
  simp [cubic5bar, y, Y0, Fin.sum_univ_five]; norm_num

theorem cubic_wedge : cubicWedge = 30 := by
  simp [cubicWedge, y, Y0, Fin.sum_univ_five]; norm_num

theorem cubic_sym : cubicSym = 270 := by
  simp [cubicSym, y, Y0, Fin.sum_univ_five]; norm_num

/-- `a` copies of `5̄` and `c` copies of `Λ²5` have vanishing cubic `Y₀`-trace iff `a = c`. -/
theorem cubic_cancel_iff (a c : ℚ) : a * cubic5bar + c * cubicWedge = 0 ↔ a = c := by
  rw [cubic_5bar, cubic_wedge]
  constructor <;> intro h <;> linarith

/-- The vector-like pair `5 ⊕ 5̄` also cancels: the cubic trace alone does not force chirality. -/
theorem cubic_5_add_5bar : cubic5 + cubic5bar = 0 := by
  rw [cubic_5, cubic_5bar]; norm_num

end QOU.EightfoldWay.FermiPairWedge
