import QOU.KnotTheory
import Mathlib.GroupTheory.FreeGroup.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Brunnian strand deletion and reduced Burau non-triviality of the Borromean braid

Algebraic and combinatorial formalization for `prop:brunnian-property-of-borromean` on the
three-strand Borromean braid `QOU.KnotTheory.borromeanRings` (`β_Bor = (σ_0 σ_1⁻¹)³`):

1. **Pure three-component closure (`borromeanRings_tracePerm_eq_refl`):**
   Exact strand-slot tracking in `Equiv.Perm (Fin 3)` along `borromeanRings.letters` evaluates
   to the identity permutation, confirming that Markov closure joins each strand to itself as a
   three-component link, with all three pairwise signed crossing sums equal to zero.
2. **Exact topological strand deletion into `B_2` (`deleteStrand`, `borromean_deleteStrand_r2_nil`,
   `borromean_deleteStrand_toB2Group_eq_one`):**
   At every crossing of a three-strand braid, deleting strand `c : Fin 3` drops crossings
   incident to `c` without altering the horizontal left-to-right order of the two remaining
   strands (`survivingOrder_stepPerm_of_touches`), while crossings disjoint from `c` occur at
   adjacent slots with `c` in an outer slot (`deleted_strand_outer_slot`) and swap the two
   remaining strands (`survivingOrder_stepPerm_of_not_touches`). Applying `deleteStrand` to
   `borromeanRings.letters` at `c = 0, 1, 2` yields the opposite-sign two-crossing `B_2` words
   `[σ_0, σ_0⁻¹]`, `[σ_0⁻¹, σ_0]`, `[σ_0, σ_0⁻¹]`, each reducing in one Reidemeister II step
   (`R2Equiv`, `r2Reduce`, and `FreeGroup.Red`) to the empty word `[]` and to `1 : FreeGroup Unit`
   in `B_2 ≅ F_1`.
3. **Three-strand non-triviality via the `2 × 2` reduced Burau representation
   (`borromean_burau_entry_one_zero`, `borromean_burau_ne_one`, `borromean_not_braidEquiv3_nil`):**
   The `2 × 2` reduced Burau representation `burauWord q q⁻¹` respects generator-inverse
   cancellation and the Artin three-strand braid relation `σ_0 σ_1 σ_0 = σ_1 σ_0 σ_1`, and maps
   `borromeanRings.letters` to a matrix with `(1, 0)`-entry `(q - 1)² (q² + 1) q⁻² > 0` and
   trace `2 - (q - 1)⁴ (q² + q + 1) q⁻³ < 2` for every real `q > 1`. Consequently `borromeanRings`
   is neither equal nor conjugate to the identity in the Burau image and is not Artin-equivalent
   to the trivial three-strand braid `[]`.
-/

namespace QOU.BraidKnot.BorromeanBrunnianStrandDeletion

open QOU.KnotTheory

/-! ## Part 1: Three-strand permutation tracking and pairwise crossing sums -/

/-- Explicit transposition swapping slots `0` and `1` on `Fin 3`. -/
def swap01Fun : Fin 3 → Fin 3
  | 0 => 1
  | 1 => 0
  | 2 => 2

/-- Explicit transposition swapping slots `1` and `2` on `Fin 3`. -/
def swap12Fun : Fin 3 → Fin 3
  | 0 => 0
  | 1 => 2
  | 2 => 1

/-- Permutation swapping slots `0` and `1` on `Fin 3`. -/
def swap01Perm : Equiv.Perm (Fin 3) where
  toFun := swap01Fun
  invFun := swap01Fun
  left_inv p := by fin_cases p <;> rfl
  right_inv p := by fin_cases p <;> rfl

/-- Permutation swapping slots `1` and `2` on `Fin 3`. -/
def swap12Perm : Equiv.Perm (Fin 3) where
  toFun := swap12Fun
  invFun := swap12Fun
  left_inv p := by fin_cases p <;> rfl
  right_inv p := by fin_cases p <;> rfl

/-- Adjacent slot transposition on `Fin 3` induced by a three-strand braid letter:
index `0` swaps slots `0` and `1`; index `1` swaps slots `1` and `2`. -/
def slotSwap3 (l : BraidLetter) : Equiv.Perm (Fin 3) :=
  if l.index = 0 then swap01Perm
  else if l.index = 1 then swap12Perm
  else Equiv.refl (Fin 3)

/-- Update the slot-to-strand bijection `occ : Equiv.Perm (Fin 3)` across a single braid letter `l`:
after `l`, horizontal slot `p` holds the strand previously at `slotSwap3 l p`. -/
def stepPerm (l : BraidLetter) (occ : Equiv.Perm (Fin 3)) : Equiv.Perm (Fin 3) :=
  (slotSwap3 l).trans occ

/-- Left-to-right evolution of the slot-to-strand bijection along a braid word. -/
def tracePerm : List BraidLetter → Equiv.Perm (Fin 3) → Equiv.Perm (Fin 3)
  | [], occ => occ
  | l :: ls, occ => tracePerm ls (stepPerm l occ)

theorem tracePerm_append (w₁ w₂ : List BraidLetter) (occ : Equiv.Perm (Fin 3)) :
    tracePerm (w₁ ++ w₂) occ = tracePerm w₂ (tracePerm w₁ occ) := by
  induction w₁ generalizing occ with
  | nil => rfl
  | cons l ls ih => exact ih (stepPerm l occ)

/-- **Pure-braid closure of `borromeanRings`:** tracing `(σ_0 σ_1⁻¹)³` from `Equiv.refl (Fin 3)`
returns `Equiv.refl (Fin 3)`, so each of the three strands closes onto itself. -/
theorem borromeanRings_tracePerm_eq_refl :
    tracePerm borromeanRings.letters (Equiv.refl (Fin 3)) = Equiv.refl (Fin 3) := by
  ext p
  fin_cases p <;> rfl

/-- Signed crossing sum between original strands `s` and `t` along a three-strand braid word. -/
def pairCrossingSum (s t : Fin 3) : List BraidLetter → Equiv.Perm (Fin 3) → ℤ
  | [], _ => 0
  | l :: ls, occ =>
      let pairHit : Bool :=
        if l.index = 0 then
          decide ((occ 0 = s ∧ occ 1 = t) ∨ (occ 0 = t ∧ occ 1 = s))
        else if l.index = 1 then
          decide ((occ 1 = s ∧ occ 2 = t) ∨ (occ 1 = t ∧ occ 2 = s))
        else false
      (if pairHit then l.signValue else 0) + pairCrossingSum s t ls (stepPerm l occ)

/-- Every distinct pair of strands in `borromeanRings` has signed crossing sum `0`. -/
theorem borromeanRings_pairCrossingSum_zero (s t : Fin 3) (hst : s ≠ t) :
    pairCrossingSum s t borromeanRings.letters (Equiv.refl (Fin 3)) = 0 := by
  fin_cases s <;> fin_cases t
  · exact absurd rfl hst
  · rfl
  · rfl
  · rfl
  · exact absurd rfl hst
  · rfl
  · rfl
  · rfl
  · exact absurd rfl hst

/-! ## Part 2: Exact strand-deletion projection into `B_2` and Reidemeister II triviality -/

/-- Predicate recording whether a three-strand letter `l` at slot occupancy `occ` involves
strand `c`. -/
def crossingTouches (l : BraidLetter) (occ : Equiv.Perm (Fin 3)) (c : Fin 3) : Bool :=
  if l.index = 0 then decide (occ 0 = c ∨ occ 1 = c)
  else if l.index = 1 then decide (occ 1 = c ∨ occ 2 = c)
  else true

/-- Ordered two-element list of the horizontal left-to-right positions of the surviving strands
`Fin 3 \ {c}` at slot occupancy `occ`. -/
def survivingOrder (occ : Equiv.Perm (Fin 3)) (c : Fin 3) : List (Fin 3) :=
  ([0, 1, 2] : List (Fin 3)).map occ |>.filter (fun s => s ≠ c)

/-- Finite list of all `6` permutations of `Fin 3`, used only for transparent case-exhaustion
lemmas without `native_decide`. -/
theorem perm_fin3_cases (occ : Equiv.Perm (Fin 3)) :
    (occ 0 = 0 ∧ occ 1 = 1 ∧ occ 2 = 2) ∨
    (occ 0 = 0 ∧ occ 1 = 2 ∧ occ 2 = 1) ∨
    (occ 0 = 1 ∧ occ 1 = 0 ∧ occ 2 = 2) ∨
    (occ 0 = 1 ∧ occ 1 = 2 ∧ occ 2 = 0) ∨
    (occ 0 = 2 ∧ occ 1 = 0 ∧ occ 2 = 1) ∨
    (occ 0 = 2 ∧ occ 1 = 1 ∧ occ 2 = 0) := by
  have h01 : occ 0 ≠ occ 1 := fun h => by simpa using occ.injective h
  have h02 : occ 0 ≠ occ 2 := fun h => by simpa using occ.injective h
  have h12 : occ 1 ≠ occ 2 := fun h => by simpa using occ.injective h
  generalize ha0 : occ 0 = a0 at h01 h02 ⊢
  generalize ha1 : occ 1 = a1 at h01 h12 ⊢
  generalize ha2 : occ 2 = a2 at h02 h12 ⊢
  fin_cases a0 <;> fin_cases a1 <;> fin_cases a2 <;> simp_all

/-- **Outer-slot isolation:** at any valid three-strand crossing (`l.index < 2`) that does not
touch strand `c`, `c` occupies an outer slot (`occ 2 = c` when `l.index = 0`, `occ 0 = c` when
`l.index = 1`), so `c` never lies between the two crossing strands. -/
theorem deleted_strand_outer_slot (l : BraidLetter) (hl : l.index < 2)
    (occ : Equiv.Perm (Fin 3)) (c : Fin 3) (hnot : crossingTouches l occ c = false) :
    (l.index = 0 ∧ occ 2 = c) ∨ (l.index = 1 ∧ occ 0 = c) := by
  have hidx : l.index = 0 ∨ l.index = 1 := by omega
  rcases perm_fin3_cases occ with
    ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ |
    ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ <;>
  rcases hidx with hi | hi <;>
  fin_cases c <;>
  simp_all [crossingTouches]

/-- **Planar deletion invariance at dropped crossings:** when `l` (`l.index < 2`) involves the
deleted strand `c`, stepping across `l` leaves the left-to-right order of the two remaining
strands unchanged. -/
theorem survivingOrder_stepPerm_of_touches (l : BraidLetter) (hl : l.index < 2)
    (occ : Equiv.Perm (Fin 3)) (c : Fin 3) (htouch : crossingTouches l occ c = true) :
    survivingOrder (stepPerm l occ) c = survivingOrder occ c := by
  have hidx : l.index = 0 ∨ l.index = 1 := by omega
  rcases perm_fin3_cases occ with
    ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ |
    ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ <;>
  rcases hidx with hi | hi <;>
  fin_cases c <;>
  simp_all [crossingTouches, survivingOrder, stepPerm, slotSwap3,
    swap01Perm, swap12Perm, swap01Fun, swap12Fun]

/-- **Planar deletion swap at surviving crossings:** when `l` (`l.index < 2`) does not involve `c`,
stepping across `l` reverses the two surviving strands, corresponding to a single `σ_0^{l.sign}`
crossing in `B_2`. -/
theorem survivingOrder_stepPerm_of_not_touches (l : BraidLetter) (hl : l.index < 2)
    (occ : Equiv.Perm (Fin 3)) (c : Fin 3) (hnot : crossingTouches l occ c = false) :
    survivingOrder (stepPerm l occ) c = (survivingOrder occ c).reverse := by
  have hidx : l.index = 0 ∨ l.index = 1 := by omega
  rcases perm_fin3_cases occ with
    ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ |
    ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ | ⟨h0, h1, h2⟩ <;>
  rcases hidx with hi | hi <;>
  fin_cases c <;>
  simp_all [crossingTouches, survivingOrder, stepPerm, slotSwap3,
    swap01Perm, swap12Perm, swap01Fun, swap12Fun]

/-- Strand-tracking deletion auxiliary map: drops crossings touching `c` and emits `⟨0, l.sign⟩`
in `B_2` at every crossing between the two surviving strands. -/
def deleteStrandAux (c : Fin 3) : List BraidLetter → Equiv.Perm (Fin 3) → List BraidLetter
  | [], _ => []
  | l :: ls, occ =>
      if crossingTouches l occ c then
        deleteStrandAux c ls (stepPerm l occ)
      else
        ⟨0, l.sign⟩ :: deleteStrandAux c ls (stepPerm l occ)

/-- Exact strand-deletion map `d_c` sending a three-strand braid word to the two-strand `B_2`
braid word obtained by erasing strand `c` starting from `Equiv.refl (Fin 3)`. -/
def deleteStrand (w : List BraidLetter) (c : Fin 3) : List BraidLetter :=
  deleteStrandAux c w (Equiv.refl (Fin 3))

/-- Deleting strand `0` from `borromeanRings` yields `[σ_0, σ_0⁻¹]` in `B_2`. -/
theorem deleteStrand_borromean_zero :
    deleteStrand borromeanRings.letters 0 = [⟨0, .positive⟩, ⟨0, .negative⟩] := rfl

/-- Deleting strand `1` from `borromeanRings` yields `[σ_0⁻¹, σ_0]` in `B_2`. -/
theorem deleteStrand_borromean_one :
    deleteStrand borromeanRings.letters 1 = [⟨0, .negative⟩, ⟨0, .positive⟩] := rfl

/-- Deleting strand `2` from `borromeanRings` yields `[σ_0, σ_0⁻¹]` in `B_2`. -/
theorem deleteStrand_borromean_two :
    deleteStrand borromeanRings.letters 2 = [⟨0, .positive⟩, ⟨0, .negative⟩] := rfl

/-- For every deleted strand `c : Fin 3`, the two surviving strands of `borromeanRings` return to
their initial left-to-right order, so the sub-link closure has two components. -/
theorem borromean_survivingOrder_preserved (c : Fin 3) :
    survivingOrder (tracePerm borromeanRings.letters (Equiv.refl (Fin 3))) c =
      survivingOrder (Equiv.refl (Fin 3)) c := by
  rw [borromeanRings_tracePerm_eq_refl]

/-- Sign negation on `CrossingSign`. -/
def flipSign : CrossingSign → CrossingSign
  | .positive => .negative
  | .negative => .positive

/-- Constructive stack-based Reidemeister II word reduction cancelling adjacent opposite-sign
occurrences of the same braid generator `σ_i^ε σ_i^{-ε}`. -/
def r2Push (l : BraidLetter) : List BraidLetter → List BraidLetter
  | [] => [l]
  | hd :: tl =>
      if l.index = hd.index ∧ l.sign = flipSign hd.sign then tl
      else l :: hd :: tl

/-- Constructive R2 normalizer on a list of braid letters. -/
def r2Reduce : List BraidLetter → List BraidLetter
  | [] => []
  | l :: ls => r2Push l (r2Reduce ls)

/-- Inductive Reidemeister II equivalence generated by `w₁ ++ [⟨i, s⟩, ⟨i, flipSign s⟩] ++ w₂ ~ w₁ ++ w₂`. -/
inductive R2Equiv : List BraidLetter → List BraidLetter → Prop where
  | refl (w : List BraidLetter) : R2Equiv w w
  | cancel (w₁ w₂ : List BraidLetter) (i : ℕ) (s : CrossingSign) :
      R2Equiv (w₁ ++ ⟨i, s⟩ :: ⟨i, flipSign s⟩ :: w₂) (w₁ ++ w₂)
  | symm {w₁ w₂ : List BraidLetter} : R2Equiv w₁ w₂ → R2Equiv w₂ w₁
  | trans {w₁ w₂ w₃ : List BraidLetter} : R2Equiv w₁ w₂ → R2Equiv w₂ w₃ → R2Equiv w₁ w₃

theorem r2Equiv_cons (l : BraidLetter) {w₁ w₂ : List BraidLetter} (h : R2Equiv w₁ w₂) :
    R2Equiv (l :: w₁) (l :: w₂) := by
  induction h with
  | refl _ => exact R2Equiv.refl _
  | cancel u₁ u₂ i s =>
      simpa only [List.cons_append] using R2Equiv.cancel (l :: u₁) u₂ i s
  | symm _ ih => exact R2Equiv.symm ih
  | trans _ _ ih₁ ih₂ => exact R2Equiv.trans ih₁ ih₂

theorem r2Push_equiv (l : BraidLetter) (w : List BraidLetter) :
    R2Equiv (l :: w) (r2Push l w) := by
  cases w with
  | nil => exact R2Equiv.refl [l]
  | cons hd tl =>
    dsimp only [r2Push]
    by_cases h : l.index = hd.index ∧ l.sign = flipSign hd.sign
    · rw [if_pos h]
      obtain ⟨li, ls⟩ := l
      obtain ⟨hi, hs⟩ := hd
      dsimp at h
      rcases h with ⟨rfl, rfl⟩
      have hflip : flipSign (flipSign hs) = hs := by cases hs <;> rfl
      have hc := R2Equiv.cancel [] tl li (flipSign hs)
      simpa only [List.nil_append, hflip] using hc
    · rw [if_neg h]
      exact R2Equiv.refl _

/-- `r2Reduce` is sound with respect to `R2Equiv`. -/
theorem r2Reduce_equiv (w : List BraidLetter) : R2Equiv w (r2Reduce w) := by
  induction w with
  | nil => exact R2Equiv.refl []
  | cons l ls ih =>
      exact R2Equiv.trans (r2Equiv_cons l ih) (r2Push_equiv l (r2Reduce ls))

/-- **Constructive R2 triviality for every Borromean strand deletion:**
for every `c : Fin 3`, `r2Reduce (deleteStrand borromeanRings.letters c) = []`. -/
theorem borromean_deleteStrand_r2Reduce_nil (c : Fin 3) :
    r2Reduce (deleteStrand borromeanRings.letters c) = [] := by
  fin_cases c <;> rfl

/-- **R2 equivalence to the empty `B_2` braid for every Borromean strand deletion.** -/
theorem borromean_deleteStrand_r2Equiv_nil (c : Fin 3) :
    R2Equiv (deleteStrand borromeanRings.letters c) [] := by
  have h := r2Reduce_equiv (deleteStrand borromeanRings.letters c)
  rwa [borromean_deleteStrand_r2Reduce_nil c] at h

/-- Encoding of a two-strand braid word into the free-group generator alphabet `Unit × Bool`
for `B_2 ≅ FreeGroup Unit`. -/
def toB2FreeWord (w : List BraidLetter) : List (Unit × Bool) :=
  w.map (fun l =>
    ((), match l.sign with
      | .positive => true
      | .negative => false))

/-- Group evaluation of a two-strand braid word in `B_2 := FreeGroup Unit`. -/
def toB2Group (w : List BraidLetter) : FreeGroup Unit :=
  FreeGroup.mk (toB2FreeWord w)

/-- `toB2Group` is invariant under Reidemeister II equivalence `R2Equiv`. -/
theorem toB2Group_eq_of_r2Equiv {w₁ w₂ : List BraidLetter} (h : R2Equiv w₁ w₂) :
    toB2Group w₁ = toB2Group w₂ := by
  induction h with
  | refl _ => rfl
  | cancel u₁ u₂ i s =>
      unfold toB2Group toB2FreeWord
      rw [List.map_append, List.map_cons, List.map_cons, List.map_append]
      apply Quot.sound
      cases s
      · exact @FreeGroup.Red.Step.not Unit (u₁.map _) (u₂.map _) () true
      · exact @FreeGroup.Red.Step.not Unit (u₁.map _) (u₂.map _) () false
  | symm _ ih => exact ih.symm
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- **Explicit one-step `FreeGroup.Red` reduction for every Borromean strand deletion.** -/
theorem borromean_deleteStrand_freeGroupRed (c : Fin 3) :
    FreeGroup.Red (toB2FreeWord (deleteStrand borromeanRings.letters c)) [] := by
  fin_cases c
  · change FreeGroup.Red [((), true), ((), false)] []
    exact FreeGroup.Red.Step.to_red (@FreeGroup.Red.Step.cons_not Unit [] () true)
  · change FreeGroup.Red [((), false), ((), true)] []
    exact FreeGroup.Red.Step.to_red (@FreeGroup.Red.Step.cons_not Unit [] () false)
  · change FreeGroup.Red [((), true), ((), false)] []
    exact FreeGroup.Red.Step.to_red (@FreeGroup.Red.Step.cons_not Unit [] () true)

/-- **Evaluation in `B_2 ≅ FreeGroup Unit`:** deleting any strand `c : Fin 3` of `borromeanRings`
evaluates to `1 : FreeGroup Unit`. -/
theorem borromean_deleteStrand_toB2Group_eq_one (c : Fin 3) :
    toB2Group (deleteStrand borromeanRings.letters c) = 1 := by
  rw [toB2Group_eq_of_r2Equiv (borromean_deleteStrand_r2Equiv_nil c)]
  rfl

/-! ## Part 3: Three-strand non-triviality via the `2 × 2` reduced Burau representation -/

/-- `2 × 2` reduced Burau matrix assigned to each three-strand braid letter over a commutative ring
`R` with parameters `(q, qi)` (`q * qi = 1`):
`σ_0 ↦ !![-q, 1; 0, 1]`, `σ_0⁻¹ ↦ !![-qi, qi; 0, 1]`,
`σ_1 ↦ !![1, 0; q, -q]`, `σ_1⁻¹ ↦ !![1, 0; 1, -qi]`. -/
def burauMat {R : Type*} [CommRing R] (q qi : R) (l : BraidLetter) : Matrix (Fin 2) (Fin 2) R :=
  if l.index = 0 then
    match l.sign with
    | .positive => !![-q, 1; 0, 1]
    | .negative => !![-qi, qi; 0, 1]
  else if l.index = 1 then
    match l.sign with
    | .positive => !![1, 0; q, -q]
    | .negative => !![1, 0; 1, -qi]
  else 1

/-- Multiplicative extension of `burauMat` to any three-strand braid word. -/
def burauWord {R : Type*} [CommRing R] (q qi : R) (w : List BraidLetter) :
    Matrix (Fin 2) (Fin 2) R :=
  (w.map (burauMat q qi)).prod

theorem burauWord_append {R : Type*} [CommRing R] (q qi : R) (w₁ w₂ : List BraidLetter) :
    burauWord q qi (w₁ ++ w₂) = burauWord q qi w₁ * burauWord q qi w₂ := by
  unfold burauWord
  rw [List.map_append, List.prod_append]

/-- Generator-inverse cancellation for `burauMat` whenever `q * qi = 1`. -/
theorem burauMat_mul_flipSign_eq_one {R : Type*} [CommRing R] {q qi : R} (hq : q * qi = 1)
    (i : ℕ) (s : CrossingSign) :
    burauMat q qi ⟨i, s⟩ * burauMat q qi ⟨i, flipSign s⟩ = 1 := by
  have hqiq : qi * q = 1 := by rw [mul_comm]; exact hq
  by_cases h0 : i = 0
  · subst h0
    cases s <;>
    · ext a b
      fin_cases a <;> fin_cases b <;>
        simp [burauMat, flipSign, Matrix.mul_apply, Fin.sum_univ_two, hq, hqiq]
  · by_cases h1 : i = 1
    · subst h1
      cases s <;>
      · ext a b
        fin_cases a <;> fin_cases b <;>
          simp [burauMat, flipSign, Matrix.mul_apply, Fin.sum_univ_two, hq, hqiq]
    · simp [burauMat, h0, h1]

/-- **Artin three-strand braid relation (`R3`) for `burauMat`:**
`ρ(σ_0) ρ(σ_1) ρ(σ_0) = ρ(σ_1) ρ(σ_0) ρ(σ_1)` over every commutative ring `R`. -/
theorem burauMat_artin_braid_rel {R : Type*} [CommRing R] (q qi : R) :
    burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .positive⟩ * burauMat q qi ⟨0, .positive⟩ =
      burauMat q qi ⟨1, .positive⟩ * burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .positive⟩ := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [burauMat, Matrix.mul_apply, Fin.sum_univ_two]

/-- Inductive Artin `B_3` word equivalence generated by `R2` cancellation and the `R3` braid
relation `σ_0 σ_1 σ_0 ~ σ_1 σ_0 σ_1`. -/
inductive BraidEquiv3 : List BraidLetter → List BraidLetter → Prop where
  | refl (w : List BraidLetter) : BraidEquiv3 w w
  | r2 (w₁ w₂ : List BraidLetter) (i : ℕ) (s : CrossingSign) :
      BraidEquiv3 (w₁ ++ ⟨i, s⟩ :: ⟨i, flipSign s⟩ :: w₂) (w₁ ++ w₂)
  | r3 (w₁ w₂ : List BraidLetter) :
      BraidEquiv3
        (w₁ ++ ⟨0, .positive⟩ :: ⟨1, .positive⟩ :: ⟨0, .positive⟩ :: w₂)
        (w₁ ++ ⟨1, .positive⟩ :: ⟨0, .positive⟩ :: ⟨1, .positive⟩ :: w₂)
  | symm {w₁ w₂ : List BraidLetter} : BraidEquiv3 w₁ w₂ → BraidEquiv3 w₂ w₁
  | trans {w₁ w₂ w₃ : List BraidLetter} :
      BraidEquiv3 w₁ w₂ → BraidEquiv3 w₂ w₃ → BraidEquiv3 w₁ w₃

/-- `burauWord q qi` is an invariant of `BraidEquiv3` whenever `q * qi = 1`. -/
theorem burauWord_eq_of_braidEquiv3 {R : Type*} [CommRing R] {q qi : R} (hq : q * qi = 1)
    {w₁ w₂ : List BraidLetter} (h : BraidEquiv3 w₁ w₂) :
    burauWord q qi w₁ = burauWord q qi w₂ := by
  induction h with
  | refl _ => rfl
  | r2 u₁ u₂ i s =>
      rw [burauWord_append, burauWord_append]
      congr 1
      unfold burauWord
      rw [List.map_cons, List.map_cons, List.prod_cons, List.prod_cons, ← Matrix.mul_assoc,
        burauMat_mul_flipSign_eq_one hq i s, Matrix.one_mul]
  | r3 u₁ u₂ =>
      rw [burauWord_append, burauWord_append]
      congr 1
      unfold burauWord
      simp only [List.map_cons, List.prod_cons, ← Matrix.mul_assoc]
      rw [burauMat_artin_braid_rel q qi]
  | symm _ ih => exact ih.symm
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- Reduced Burau matrix of the single alternating pair `σ_0 σ_1⁻¹`:
`!![1 - q, -qi; 1, -qi]`. -/
def borromeanPairMat {R : Type*} [CommRing R] (q qi : R) : Matrix (Fin 2) (Fin 2) R :=
  !![1 - q, -qi; 1, -qi]

theorem burau_pair_eq {R : Type*} [CommRing R] (q qi : R) :
    burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .negative⟩ = borromeanPairMat q qi := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    (simp [burauMat, borromeanPairMat, Matrix.mul_apply, Fin.sum_univ_two]; try ring)

theorem burauWord_borromean_eq_cube {R : Type*} [CommRing R] (q qi : R) :
    burauWord q qi borromeanRings.letters =
      borromeanPairMat q qi * borromeanPairMat q qi * borromeanPairMat q qi := by
  unfold borromeanRings burauWord
  simp only [List.map, List.prod_cons, List.prod_nil, mul_one]
  calc
    burauMat q qi ⟨0, .positive⟩ *
      (burauMat q qi ⟨1, .negative⟩ *
        (burauMat q qi ⟨0, .positive⟩ *
          (burauMat q qi ⟨1, .negative⟩ *
            (burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .negative⟩))))
      = (burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .negative⟩) *
        (burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .negative⟩) *
        (burauMat q qi ⟨0, .positive⟩ * burauMat q qi ⟨1, .negative⟩) := by
          simp only [Matrix.mul_assoc]
    _ = borromeanPairMat q qi * borromeanPairMat q qi * borromeanPairMat q qi := by
          rw [burau_pair_eq]

/-- **Exact lower-left entry of `burauWord q qi borromeanRings.letters`:**
over any commutative ring `R` with `q * qi = 1`,
`(ρ_q(β_Bor))_{1, 0} = (q - 1)² * (q² + 1) * qi²`. -/
theorem borromean_burau_entry_one_zero {R : Type*} [CommRing R] {q qi : R} (hq : q * qi = 1) :
    burauWord q qi borromeanRings.letters 1 0 = (q - 1) ^ 2 * (q ^ 2 + 1) * qi ^ 2 := by
  rw [burauWord_borromean_eq_cube]
  simp only [borromeanPairMat, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply,
    Matrix.cons_val_zero, Matrix.cons_val_one]
  linear_combination (-(q ^ 2 - 2 * q + 2) * (1 + q * qi) + 2 * qi + 1) * hq

/-- **Conjugation-invariant trace shift of `burauWord q q⁻¹ borromeanRings.letters`:**
over any field `K` with `q ≠ 0`,
`tr(ρ_q(β_Bor)) - 2 = -(q - 1)⁴ * (q² + q + 1) * (q⁻¹)³`. -/
theorem borromean_burau_trace_sub_two {K : Type*} [Field K] {q : K} (hq0 : q ≠ 0) :
    burauWord q q⁻¹ borromeanRings.letters 0 0 +
      burauWord q q⁻¹ borromeanRings.letters 1 1 - 2 =
      -((q - 1) ^ 4 * (q ^ 2 + q + 1) * (q⁻¹) ^ 3) := by
  rw [burauWord_borromean_eq_cube]
  simp only [borromeanPairMat, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply,
    Matrix.cons_val_zero, Matrix.cons_val_one]
  field_simp
  ring

/-- For every real `q > 1`, the `(1, 0)`-entry of `burauWord q q⁻¹ borromeanRings.letters`
is strictly positive. -/
theorem borromean_burau_entry_pos {q : ℝ} (hq : 1 < q) :
    0 < burauWord q q⁻¹ borromeanRings.letters 1 0 := by
  have hq0 : q ≠ 0 := by linarith
  rw [borromean_burau_entry_one_zero (mul_inv_cancel₀ hq0)]
  have h1 : 0 < (q - 1) ^ 2 := sq_pos_of_pos (by linarith)
  have h2 : 0 < q ^ 2 + 1 := by positivity
  have h3 : 0 < (q⁻¹) ^ 2 := sq_pos_of_pos (inv_pos.mpr (by linarith))
  exact mul_pos (mul_pos h1 h2) h3

/-- **Non-triviality of `borromeanRings` in the reduced Burau representation:**
for every real `q > 1`, `burauWord q q⁻¹ borromeanRings.letters ≠ 1`. -/
theorem borromean_burau_ne_one {q : ℝ} (hq : 1 < q) :
    burauWord q q⁻¹ borromeanRings.letters ≠ 1 := by
  intro hEq
  have hpos := borromean_burau_entry_pos hq
  rw [hEq] at hpos
  have hzero : (1 : Matrix (Fin 2) (Fin 2) ℝ) 1 0 = 0 :=
    Matrix.one_apply_ne (by decide)
  rw [hzero] at hpos
  exact lt_irrefl 0 hpos

/-- For every real `q > 1`, the trace of `burauWord q q⁻¹ borromeanRings.letters` is strictly
less than `2`, distinguishing `borromeanRings` from `1` up to `GL_2(ℝ)` conjugation as well. -/
theorem borromean_burau_trace_lt_two {q : ℝ} (hq : 1 < q) :
    burauWord q q⁻¹ borromeanRings.letters 0 0 +
      burauWord q q⁻¹ borromeanRings.letters 1 1 < 2 := by
  have hq0 : q ≠ 0 := by linarith
  have htr := borromean_burau_trace_sub_two hq0
  have h1 : 0 < (q - 1) ^ 4 := pow_pos (by linarith) 4
  have h2 : 0 < q ^ 2 + q + 1 := by nlinarith
  have h3 : 0 < (q⁻¹) ^ 3 := pow_pos (inv_pos.mpr (by linarith)) 3
  have hprod : 0 < (q - 1) ^ 4 * (q ^ 2 + q + 1) * (q⁻¹) ^ 3 :=
    mul_pos (mul_pos h1 h2) h3
  linarith

/-- **`borromeanRings` is not Artin `B_3`-equivalent to the empty three-strand braid `[]`.** -/
theorem borromean_not_braidEquiv3_nil : ¬ BraidEquiv3 borromeanRings.letters [] := by
  intro hEq
  have hmat := burauWord_eq_of_braidEquiv3 (q := (2 : ℝ)) (qi := (2 : ℝ)⁻¹)
    (by norm_num) hEq
  have hnil : burauWord (2 : ℝ) (2 : ℝ)⁻¹ [] = 1 := rfl
  rw [hnil] at hmat
  exact borromean_burau_ne_one (q := 2) (by norm_num) hmat

/-- **Combined Brunnian theorem for `borromeanRings` (`prop:brunnian-property-of-borromean`):**
1. `borromeanRings` induces the identity permutation on `Fin 3` (closing to three components);
2. deleting any component `c : Fin 3` leaves a two-component sub-link whose `B_2` braid word
   reduces in one Reidemeister II step to `[]` and evaluates to `1 : FreeGroup Unit`;
3. `borromeanRings` itself is non-trivial in `B_3`, with `burauWord q q⁻¹ borromeanRings.letters ≠ 1`
   for every real `q > 1` and `¬ BraidEquiv3 borromeanRings.letters []`. -/
theorem borromean_is_brunnian :
    tracePerm borromeanRings.letters (Equiv.refl (Fin 3)) = Equiv.refl (Fin 3) ∧
    (∀ c : Fin 3,
      R2Equiv (deleteStrand borromeanRings.letters c) [] ∧
      toB2Group (deleteStrand borromeanRings.letters c) = 1 ∧
      survivingOrder (tracePerm borromeanRings.letters (Equiv.refl (Fin 3))) c =
        survivingOrder (Equiv.refl (Fin 3)) c) ∧
    (∀ q : ℝ, 1 < q → burauWord q q⁻¹ borromeanRings.letters ≠ 1) ∧
    ¬ BraidEquiv3 borromeanRings.letters [] :=
  ⟨borromeanRings_tracePerm_eq_refl,
   fun c => ⟨borromean_deleteStrand_r2Equiv_nil c,
             borromean_deleteStrand_toB2Group_eq_one c,
             borromean_survivingOrder_preserved c⟩,
   fun _ hq => borromean_burau_ne_one hq,
   borromean_not_braidEquiv3_nil⟩

end QOU.BraidKnot.BorromeanBrunnianStrandDeletion
