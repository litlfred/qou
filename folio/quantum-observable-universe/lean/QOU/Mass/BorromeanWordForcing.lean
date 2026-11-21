import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import QOU.MathlibExt.BraidGroup
import QOU.Mass.GammaGammaWordSelection

/-!
# What singles out the Borromean word `β_Bor = (σ₀σ₁⁻¹)³`

Thread "Derive the proton's Borromean braid" (2026-11-21). The proton mass identity
`m_p/m_e = 2(Vol/ℏ_q²)·F_Bor − 12`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`, takes the
word `β_Bor` as input. This file records which properties of a three-strand word
force it, and which freedom the mass identity leaves.

## What is proved (sorry-free)

* `pureZeroLinking_short` — **no reduced three-strand word of length `1 … 5` is pure
  with all three pairwise linking numbers zero.** A finite check over every word.
* `pureZeroLinking_six` — at length `6` exactly **16** reduced words are pure with
  zero pairwise linking, listed in `lengthSixList`.
* `lengthSix_split` — of those 16, four are the words of `borOrbit` (`β_Bor`, its
  cyclic rotation, its mirror, and the mirror's rotation), and twelve are in `trivSix`.
* `eval_trivSix` — each of the twelve is the identity of `B₃`
  (`QOU.MathlibExt.Braid.BraidGroup 2`); each is a rotation of `Δ·Δ'⁻¹` with
  `Δ = σ₀σ₁σ₀`, `Δ' = σ₁σ₀σ₁`, and the braid relation `Δ = Δ'` kills it.
* `eval_borOrbit_conj` — the four words of `borOrbit` are conjugate in `B₃`.
* `eval_borromean_ne_one` — `β_Bor ≠ 1` in `B₃`. The witness is the integer
  Burau representation at `t = −1` (`burauNeg`), where `β_Bor ↦ [[13, 8], [8, 5]]`.
* `minimal_pure_zeroLinking` — **combining these: the shortest reduced three-strand
  words that are pure, have zero pairwise linking, and are not the identity of `B₃`
  have length 6, and every one of them is conjugate in `B₃` to `β_Bor`.**
* `markovTrace_writhe_zero` — for weights with `y₍₃₎ + 2y₍₂,₁₎ + y₍₁³₎ = 1`, the
  Markov trace of a writhe-0 word is `1 + y₍₂,₁₎(χ − 2)`, with `χ` its `(2,1)`
  character. So **the mass identity sees the word only through `χ`** (and the writhe).

## How this reads as "Brunnian" (a topological dictionary, cited, not proved here)

For a pure three-strand braid, deleting one strand leaves the two-strand braid
`σ^{2k}` with `k` the linking number of the other two, whose closure is the unlink
exactly when `k = 0`. So the closure of a pure three-braid is Brunnian
(every proper sub-link trivial, `QOU.Mass.BrunnianTierDisambiguation` tier T1) exactly
when all three linking numbers vanish and the closure is not the three-component
unlink. That dictionary is standard knot theory (closure of braids, linking numbers)
and is cited, not formalised; the theorems above are stated about words and `B₃`
only. "Closure of `β_Bor` is not the unlink" also needs a link invariant
(Markov's theorem plus the trace); it is not used in any statement here.

## What is NOT proved, and what the companion probe measured

* That the minimum is unique **up to conjugacy among all words**, not only reduced
  words of length 6: longer words representing a length-6 element are conjugates of
  the same group elements, so this is covered by the group-level statement, but
  nothing here enumerates `B₃` conjugacy classes.
* That `χ` separates `β_Bor`'s conjugacy class. The probe
  `computations/probes/borromean_word_forcing/` (exact Laurent arithmetic,
  pre-registered) finds every writhe-0 word of length `≤ 10` with `χ = χ(β_Bor)`
  conjugate to `β_Bor` (Burau faithfulness on `B₃`, Magnus–Peluso, cited), and no word
  with `tr_M = −tr_M(β_Bor)`. This is a finite measurement, not a theorem.
* **Brunnian alone does not force `β_Bor`.** The same probe finds twenty pure,
  zero-linking words of length 10 with a different character (other Brunnian
  closed three-braids), and more at length 12. What singles out `β_Bor` is
  *minimal crossing number* among them; that cost is the same crossing-count cost the
  γγ route uses (`QOU.Mass.GammaGammaSelectionAllK`), and it is an input, not derived.

Nothing here reads CODATA, AME or PDG.
-/

namespace QOU.Mass.BorromeanWordForcing

open QOU.Mass.GammaGammaWordSelection
open QOU.MathlibExt.Braid

/-! ## Strand tracking and pairwise linking -/

/-- Strand labels at positions `0, 1, 2`, and twice the signed crossing count for
each pair of labels (`l01`, `l02`, `l12`). -/
structure St where
  p0 : ℕ
  p1 : ℕ
  p2 : ℕ
  l01 : ℤ
  l02 : ℤ
  l12 : ℤ
  deriving DecidableEq, Repr

/-- The start state: identity positions, no crossings. -/
def St.init : St := ⟨0, 1, 2, 0, 0, 0⟩

/-- Add `s` to the pair `{a, b}` of labels. -/
def bump (a b : ℕ) (s : ℤ) (st : St) : St :=
  if (a = 0 ∧ b = 1) ∨ (a = 1 ∧ b = 0) then { st with l01 := st.l01 + s }
  else if (a = 0 ∧ b = 2) ∨ (a = 2 ∧ b = 0) then { st with l02 := st.l02 + s }
  else { st with l12 := st.l12 + s }

/-- One crossing: swap the two strands at positions `gen, gen+1` and record the sign
against their pair of labels. Only generators `0, 1` occur on three strands. -/
def step (st : St) (c : Crossing) : St :=
  let s : ℤ := if c.pos then 1 else -1
  if c.gen = 0 then bump st.p0 st.p1 s { st with p0 := st.p1, p1 := st.p0 }
  else bump st.p1 st.p2 s { st with p1 := st.p2, p2 := st.p1 }

/-- The state after reading a word left to right. -/
def run (w : Word) : St := w.foldl step St.init

/-- **Pure with all three pairwise linking numbers zero**: every strand ends where it
started and, for each pair of strands, the crossings between them have signed sum `0`. -/
def PureZeroLinking (w : Word) : Bool := run w = St.init

/-- Freely reduced: no letter is followed by its own inverse. -/
def Reduced : Word → Bool
  | [] => true
  | [_] => true
  | a :: b :: t => !(a.gen = b.gen && a.pos != b.pos) && Reduced (b :: t)

/-- The four letters of `B₃`. -/
def letters : List Crossing := [⟨0, true⟩, ⟨0, false⟩, ⟨1, true⟩, ⟨1, false⟩]

/-- Every word of length `n` in the four letters. -/
def wordsOfLength : ℕ → List Word
  | 0 => [[]]
  | n + 1 => (wordsOfLength n).flatMap fun w => letters.map fun c => c :: w

/-- Reduced, pure, zero-linking words of length `n`. -/
def candidates (n : ℕ) : List Word :=
  (wordsOfLength n).filter fun w => Reduced w && PureZeroLinking w

theorem mem_wordsOfLength {n : ℕ} {w : Word} (h : w ∈ wordsOfLength n) :
    w.length = n ∧ ∀ c ∈ w, c ∈ letters := by
  induction n generalizing w with
  | zero => simp [wordsOfLength] at h; subst h; simp
  | succ n ih =>
    simp only [wordsOfLength, List.mem_flatMap, List.mem_map] at h
    obtain ⟨v, hv, c, hc, rfl⟩ := h
    obtain ⟨hl, hall⟩ := ih hv
    refine ⟨by simp [hl], ?_⟩
    intro x hx
    rcases List.mem_cons.mp hx with rfl | hx
    · exact hc
    · exact hall x hx

theorem mem_wordsOfLength_of {w : Word} (hl : ∀ c ∈ w, c ∈ letters) :
    w ∈ wordsOfLength w.length := by
  induction w with
  | nil => simp [wordsOfLength]
  | cons c w ih =>
    simp only [List.length_cons, wordsOfLength, List.mem_flatMap, List.mem_map]
    exact ⟨w, ih fun x hx => hl x (List.mem_cons_of_mem _ hx), c,
      hl c List.mem_cons_self, rfl⟩

/-! ## The finite checks -/

/-- **No short candidate.** Lengths 1 to 5 carry no reduced, pure, zero-linking word. -/
theorem pureZeroLinking_short :
    candidates 1 = [] ∧ candidates 2 = [] ∧ candidates 3 = [] ∧
      candidates 4 = [] ∧ candidates 5 = [] := by
  decide +kernel

/-- Shorthand letters. -/
abbrev a : Crossing := ⟨0, true⟩
abbrev a' : Crossing := ⟨0, false⟩
abbrev b : Crossing := ⟨1, true⟩
abbrev b' : Crossing := ⟨1, false⟩

set_option maxRecDepth 100000

/-- The four words of the Borromean orbit: `β_Bor = (σ₀σ₁⁻¹)³`, its rotation
`(σ₁⁻¹σ₀)³`, the mirror `(σ₀⁻¹σ₁)³` and its rotation `(σ₁σ₀⁻¹)³`. -/
def borOrbit : List Word :=
  [[a, b', a, b', a, b'], [b', a, b', a, b', a],
   [a', b, a', b, a', b], [b, a', b, a', b, a']]

/-- The twelve trivial length-6 candidates. -/
def trivSix : List Word :=
  [[a, b, a, b', a', b'], [a, b, a', b', a', b], [a, b', a', b', a, b],
   [a', b, a, b, a', b'], [a', b', a, b, a, b'], [a', b', a', b, a, b],
   [b, a, b, a', b', a'], [b, a, b', a', b', a], [b, a', b', a', b, a],
   [b', a, b, a, b', a'], [b', a', b, a, b, a'], [b', a', b', a, b, a]]

/-- At length 6 there are exactly sixteen candidates, and each is one of the four
Borromean words or one of the twelve words of `trivSix`. -/
theorem pureZeroLinking_six :
    (candidates 6).length = 16 ∧
      ∀ w ∈ candidates 6, w ∈ borOrbit ∨ w ∈ trivSix := by
  decide +kernel

/-- Conversely every word of `borOrbit` and of `trivSix` is a length-6 candidate. -/
theorem borOrbit_trivSix_sub :
    (∀ w ∈ borOrbit, w ∈ candidates 6) ∧ (∀ w ∈ trivSix, w ∈ candidates 6) := by
  decide +kernel

/-! ## Evaluation in `B₃` -/

/-- A letter as an element of `B₃ = BraidGroup 2`. -/
def evalLetter (c : Crossing) : BraidGroup 2 :=
  if c.pos then σ (if c.gen = 0 then 0 else 1) else (σ (if c.gen = 0 then 0 else 1))⁻¹

/-- A word as an element of `B₃`. -/
def eval (w : Word) : BraidGroup 2 := (w.map evalLetter).prod

/-- The braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` in `B₃`. -/
theorem braid_rel : (σ 0 * σ 1 * σ 0 : BraidGroup 2) = σ 1 * σ 0 * σ 1 := by
  have hmem : (FreeGroup.of (0 : Fin 2) * FreeGroup.of 1 * FreeGroup.of 0 *
      (FreeGroup.of 1 * FreeGroup.of 0 * FreeGroup.of 1)⁻¹) ∈ braidRelators 2 := by
    right
    exact ⟨0, by decide, rfl⟩
  have h1 := PresentedGroup.one_of_mem (rels := braidRelators 2) hmem
  have h2 : (σ 0 * σ 1 * σ 0 : BraidGroup 2) * (σ 1 * σ 0 * σ 1)⁻¹ = 1 := by
    simpa [σ, map_mul, map_inv] using h1
  exact mul_inv_eq_one.mp h2

theorem eval_append (u v : Word) : eval (u ++ v) = eval u * eval v := by
  simp [eval, List.map_append, List.prod_append]

/-- Rotating a word conjugates its value. -/
theorem eval_rotate (u v : Word) : eval (v ++ u) = (eval u)⁻¹ * eval (u ++ v) * eval u := by
  rw [eval_append, eval_append]; group

@[simp] theorem eval_a : eval [a] = σ 0 := by simp [eval, evalLetter]
@[simp] theorem eval_a' : eval [a'] = (σ 0)⁻¹ := by simp [eval, evalLetter]
@[simp] theorem eval_b : eval [b] = σ 1 := by simp [eval, evalLetter]
@[simp] theorem eval_b' : eval [b'] = (σ 1)⁻¹ := by simp [eval, evalLetter]

/-- `eval` of a six-letter word, letter by letter. -/
theorem eval_six (c₁ c₂ c₃ c₄ c₅ c₆ : Crossing) :
    eval [c₁, c₂, c₃, c₄, c₅, c₆] =
      eval [c₁] * eval [c₂] * eval [c₃] * eval [c₄] * eval [c₅] * eval [c₆] := by
  simp [eval, mul_assoc]

/-- `R = σ₀σ₁σ₀ (σ₁σ₀σ₁)⁻¹` is the identity of `B₃`. -/
theorem eval_R : eval [a, b, a, b', a', b'] = 1 := by
  rw [eval_six]; simp only [eval_a, eval_a', eval_b, eval_b']
  have r := braid_rel
  calc σ 0 * σ 1 * σ 0 * (σ 1)⁻¹ * (σ 0)⁻¹ * (σ 1)⁻¹
      = (σ 0 * σ 1 * σ 0) * (σ 1 * σ 0 * σ 1)⁻¹ := by group
    _ = 1 := by rw [r]; group

/-- `R⁻¹ = σ₁σ₀σ₁ (σ₀σ₁σ₀)⁻¹` is the identity of `B₃`. -/
theorem eval_Ri : eval [b, a, b, a', b', a'] = 1 := by
  rw [eval_six]; simp only [eval_a, eval_a', eval_b, eval_b']
  have r := braid_rel
  calc σ 1 * σ 0 * σ 1 * (σ 0)⁻¹ * (σ 1)⁻¹ * (σ 0)⁻¹
      = (σ 1 * σ 0 * σ 1) * (σ 0 * σ 1 * σ 0)⁻¹ := by group
    _ = 1 := by rw [r]; group

/-- **The twelve non-Borromean length-6 candidates are the identity of `B₃`.**
Each is a rotation of `R` or `R⁻¹`. -/
theorem eval_trivSix : ∀ w ∈ trivSix, eval w = 1 := by
  have hR := eval_R
  have hRi := eval_Ri
  intro w hw
  simp only [trivSix, List.mem_cons, List.mem_nil_iff, or_false] at hw
  rcases hw with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact hR
  · rw [show ([a, b, a', b', a', b] : Word) = [a, b, a', b', a'] ++ [b] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hRi]; group
  · rw [show ([a, b', a', b', a, b] : Word) = [a, b', a', b'] ++ [a, b] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hR]; group
  · rw [show ([a', b, a, b, a', b'] : Word) = [a'] ++ [b, a, b, a', b'] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hRi]; group
  · rw [show ([a', b', a, b, a, b'] : Word) = [a', b'] ++ [a, b, a, b'] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hR]; group
  · rw [show ([a', b', a', b, a, b] : Word) = [a', b', a'] ++ [b, a, b] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hRi]; group
  · exact hRi
  · rw [show ([b, a, b', a', b', a] : Word) = [b, a, b', a', b'] ++ [a] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hR]; group
  · rw [show ([b, a', b', a', b, a] : Word) = [b, a', b', a'] ++ [b, a] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hRi]; group
  · rw [show ([b', a, b, a, b', a'] : Word) = [b'] ++ [a, b, a, b', a'] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hR]; group
  · rw [show ([b', a', b, a, b, a'] : Word) = [b', a'] ++ [b, a, b, a'] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hRi]; group
  · rw [show ([b', a', b', a, b, a] : Word) = [b', a', b'] ++ [a, b, a] from rfl, eval_rotate]
    simp only [List.cons_append, List.nil_append, hR]; group

/-! ## `β_Bor` is not the identity: the integer Burau representation at `t = −1` -/

/-- Images of the generators: `σ₀ ↦ [[1, 1], [0, 1]]`, `σ₁ ↦ [[1, 0], [−1, 1]]`
(reduced Burau at `t = −1`). -/
def burauGen : Fin 2 → Matrix.SpecialLinearGroup (Fin 2) ℤ
  | 0 => ⟨!![1, 1; 0, 1], by simp [Matrix.det_fin_two]⟩
  | 1 => ⟨!![1, 0; -1, 1], by simp [Matrix.det_fin_two]⟩

theorem burauGen_relators :
    ∀ r ∈ braidRelators 2, (FreeGroup.lift burauGen) r = 1 := by
  rintro r (⟨i, j, hij, rfl⟩ | ⟨i, h, rfl⟩)
  · exfalso; have := i.isLt; have := j.isLt; omega
  · have hi : i = 0 := by ext; have := i.isLt; simp at h ⊢; omega
    subst hi
    simp only [map_mul, map_inv, FreeGroup.lift_apply_of, mul_inv_eq_one]
    ext k l
    fin_cases k <;> fin_cases l <;>
      simp [burauGen, Matrix.SpecialLinearGroup.coe_mul, Matrix.mul_apply, Fin.sum_univ_two]

/-- The representation `B₃ → SL(2, ℤ)`. -/
def burauNeg : BraidGroup 2 →* Matrix.SpecialLinearGroup (Fin 2) ℤ :=
  PresentedGroup.toGroup burauGen_relators

theorem burauNeg_σ (i : Fin 2) : burauNeg (σ i) = burauGen i :=
  PresentedGroup.toGroup.of _

/-- `β_Bor ↦ [[13, 8], [8, 5]]`. -/
theorem burauNeg_borromean :
    ((burauNeg (eval [a, b', a, b', a, b']) : Matrix.SpecialLinearGroup (Fin 2) ℤ) :
      Matrix (Fin 2) (Fin 2) ℤ) = !![13, 8; 8, 5] := by
  rw [eval_six]
  simp only [eval_a, eval_b', map_mul, map_inv, burauNeg_σ]
  ext k l
  fin_cases k <;> fin_cases l <;>
    simp [burauGen, Matrix.SpecialLinearGroup.coe_mul, Matrix.SpecialLinearGroup.coe_inv,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.adjugate_fin_two]

/-- **`β_Bor` is not the identity of `B₃`.** -/
theorem eval_borromean_ne_one : eval [a, b', a, b', a, b'] ≠ 1 := by
  intro h
  have := burauNeg_borromean
  rw [h, map_one] at this
  have h00 := congrFun (congrFun this 0) 0
  simp at h00

/-! ## The four Borromean words are conjugate in `B₃` -/

/-- `Δ = σ₀σ₁σ₀` swaps the generators by conjugation. -/
theorem delta_conj_σ0 :
    (σ 0 * σ 1 * σ 0 : BraidGroup 2) * σ 0 * (σ 0 * σ 1 * σ 0)⁻¹ = σ 1 := by
  have r := braid_rel
  calc (σ 0 * σ 1 * σ 0 : BraidGroup 2) * σ 0 * (σ 0 * σ 1 * σ 0)⁻¹
      = (σ 1 * σ 0 * σ 1) * σ 0 * (σ 0 * σ 1 * σ 0)⁻¹ := by rw [r]
    _ = σ 1 := by group

theorem delta_conj_σ1 :
    (σ 0 * σ 1 * σ 0 : BraidGroup 2) * σ 1 * (σ 0 * σ 1 * σ 0)⁻¹ = σ 0 := by
  have r := braid_rel
  calc (σ 0 * σ 1 * σ 0 : BraidGroup 2) * σ 1 * (σ 0 * σ 1 * σ 0)⁻¹
      = σ 0 * (σ 1 * σ 0 * σ 1) * (σ 0 * σ 1 * σ 0)⁻¹ := by group
    _ = σ 0 * (σ 0 * σ 1 * σ 0) * (σ 0 * σ 1 * σ 0)⁻¹ := by rw [r]
    _ = σ 0 := by group

/-- `(σ₁σ₀⁻¹)³ = Δ (σ₀σ₁⁻¹)³ Δ⁻¹`, `Δ = σ₀σ₁σ₀`. -/
theorem conj_flip : IsConj (eval [b, a', b, a', b, a']) (eval [a, b', a, b', a, b']) := by
  rw [eval_six, eval_six]; simp only [eval_a, eval_a', eval_b, eval_b']
  rw [isConj_comm, isConj_iff]
  refine ⟨σ 0 * σ 1 * σ 0, ?_⟩
  have h0 := delta_conj_σ0
  have h1 := delta_conj_σ1
  set D : BraidGroup 2 := σ 0 * σ 1 * σ 0 with hD
  have h1' : D * (σ 1)⁻¹ * D⁻¹ = (σ 0)⁻¹ := by
    rw [show D * (σ 1)⁻¹ * D⁻¹ = (D * σ 1 * D⁻¹)⁻¹ by group, h1]
  calc D * (σ 0 * (σ 1)⁻¹ * σ 0 * (σ 1)⁻¹ * σ 0 * (σ 1)⁻¹) * D⁻¹
      = (D * σ 0 * D⁻¹) * (D * (σ 1)⁻¹ * D⁻¹) * (D * σ 0 * D⁻¹) *
        (D * (σ 1)⁻¹ * D⁻¹) * (D * σ 0 * D⁻¹) * (D * (σ 1)⁻¹ * D⁻¹) := by group
    _ = _ := by rw [h0, h1']

/-- The mirror `(σ₀⁻¹σ₁)³` is the rotation of `(σ₁σ₀⁻¹)³` by one letter. -/
theorem conj_mirror : IsConj (eval [a', b, a', b, a', b]) (eval [a, b', a, b', a, b']) := by
  refine IsConj.trans ?_ conj_flip
  rw [isConj_iff]
  refine ⟨σ 1, ?_⟩
  rw [show ([a', b, a', b, a', b] : Word) = [a', b, a', b, a'] ++ [b] from rfl, eval_rotate]
  simp only [List.cons_append, List.nil_append, eval_b]
  group

theorem eval_borOrbit_conj : ∀ w ∈ borOrbit, IsConj (eval w) (eval [a, b', a, b', a, b']) := by
  have e6 := eval_six
  intro w hw
  simp only [borOrbit, List.mem_cons, List.mem_nil_iff, or_false] at hw
  rcases hw with rfl | rfl | rfl | rfl
  · exact IsConj.refl _
  · -- rotation: (σ₁⁻¹σ₀)³ = σ₀⁻¹ β_Bor σ₀
    rw [isConj_iff]; refine ⟨σ 0, ?_⟩
    rw [e6, e6]; simp only [eval_a, eval_b']; group
  · exact conj_mirror
  · exact conj_flip

/-! ## The minimality theorem -/

/-- A word uses only the three-strand letters. -/
def InB3Letters (w : Word) : Prop := ∀ c ∈ w, c ∈ letters

/-- **The shortest non-trivial pure zero-linking three-strand words are the
Borromean words.** For a reduced word in the `B₃` letters that is pure with all
pairwise linking numbers zero:
* if its length is between 1 and 5 — impossible;
* if its length is 6 — it is the identity of `B₃` or conjugate to `β_Bor`;
and `β_Bor` itself is not the identity. -/
theorem minimal_pure_zeroLinking :
    (∀ w : Word, InB3Letters w → Reduced w = true → PureZeroLinking w = true →
        w.length ≤ 5 → w = []) ∧
    (∀ w : Word, InB3Letters w → Reduced w = true → PureZeroLinking w = true →
        w.length = 6 → eval w = 1 ∨ IsConj (eval w) (eval borromean)) ∧
    eval borromean ≠ 1 := by
  have hb : borromean = [a, b', a, b', a, b'] := rfl
  obtain ⟨h1, h2, h3, h4, h5⟩ := pureZeroLinking_short
  have hmem : ∀ w : Word, InB3Letters w → Reduced w = true → PureZeroLinking w = true →
      w ∈ candidates w.length := fun w hl hr hp => by
    simp only [candidates, List.mem_filter, hr, hp, Bool.and_self, and_true]
    exact mem_wordsOfLength_of hl
  refine ⟨?_, ?_, ?_⟩
  · intro w hl hr hp hlen
    have hw := hmem w hl hr hp
    rcases Nat.lt_or_ge w.length 1 with h0 | h0
    · exact List.length_eq_zero_iff.mp (by omega)
    · exfalso
      interval_cases hn : w.length <;> simp_all
  · intro w hl hr hp hlen
    have hw := hmem w hl hr hp
    rw [hlen] at hw
    rcases pureZeroLinking_six.2 w hw with ho | ht
    · right; rw [hb]; exact eval_borOrbit_conj w ho
    · left; exact eval_trivSix w ht
  · rw [hb]; exact eval_borromean_ne_one

/-! ## The mass identity sees a writhe-0 word only through its `(2,1)` character -/

section Trace

variable {R : Type*} [Field R]

/-- The trivial one-dimensional character `σᵢ^{±1} ↦ q^{±1}`. -/
def trivChar (q : R) (w : Word) : R :=
  (w.map fun c => if c.pos then q else q⁻¹).prod

theorem trivChar_eq_zpow {q : R} (hq : q ≠ 0) (w : Word) : trivChar q w = q ^ writhe w := by
  induction w with
  | nil => simp [trivChar, writhe]
  | cons c w ih =>
    have hw : writhe (c :: w) = sign c + writhe w := by simp [writhe]
    rw [show trivChar q (c :: w) = (if c.pos then q else q⁻¹) * trivChar q w by
      simp [trivChar], ih, hw, zpow_add₀ hq]
    rcases c with ⟨g, _ | _⟩ <;> simp [sign]

theorem altChar_eq_zpow {q : R} (hq : q ≠ 0) (w : Word) :
    altChar q w = (-1) ^ w.length * q ^ (-writhe w) := by
  induction w with
  | nil => simp [altChar, writhe]
  | cons c w ih =>
    have hw : writhe (c :: w) = sign c + writhe w := by simp [writhe]
    rw [show altChar q (c :: w) = (if c.pos then -q⁻¹ else -q) * altChar q w by
      simp [altChar], ih, hw, neg_add, zpow_add₀ hq, List.length_cons, pow_succ]
    rcases c with ⟨g, _ | _⟩ <;> simp [sign] <;> ring

theorem length_even_of_writhe_zero (w : Word) (h : writhe w = 0) : Even w.length := by
  have key : ∀ w : Word, Even ((w.length : ℤ) - writhe w) := by
    intro w
    induction w with
    | nil => simp [writhe]
    | cons c w ih =>
      have hw : writhe (c :: w) = sign c + writhe w := by simp [writhe]
      rw [hw, List.length_cons, Nat.cast_succ,
        show (w.length : ℤ) + 1 - (sign c + writhe w) = (w.length - writhe w) + (1 - sign c) by ring]
      refine ih.add ?_
      cases hc : c.pos
      · simp [sign, hc]
      · simp [sign, hc]
  have := key w
  rw [h, sub_zero] at this
  exact (Int.even_coe_nat _).mp this

/-- The Wedderburn form of the `H₃` Markov trace on a word: weights `y₍₃₎, y₍₂,₁₎,
y₍₁³₎` on the blocks `(3), (2,1), (1³)`, and `χ` the `(2,1)` character of the word. -/
def markovTraceH3 (q y3 y21 y111 χ : R) (w : Word) : R :=
  y3 * trivChar q w + y111 * altChar q w + y21 * χ

/-- **At writhe 0 the trace depends on the word only through `χ`:**
`tr = 1 + y₍₂,₁₎·(χ − 2)` whenever `y₍₃₎ + 2y₍₂,₁₎ + y₍₁³₎ = 1`. Two writhe-0 words with
the same `(2,1)` character therefore have the same `tr_M`, and the same `F_Bor`. -/
theorem markovTrace_writhe_zero {q : R} (hq : q ≠ 0) (y3 y21 y111 χ : R)
    (hsum : y3 + 2 * y21 + y111 = 1) (w : Word) (hw : writhe w = 0) :
    markovTraceH3 q y3 y21 y111 χ w = 1 + y21 * (χ - 2) := by
  have he := length_even_of_writhe_zero w hw
  simp only [markovTraceH3, trivChar_eq_zpow hq, altChar_eq_zpow hq, hw, neg_zero,
    zpow_zero, he.neg_one_pow, mul_one]
  linear_combination hsum

end Trace

end QOU.Mass.BorromeanWordForcing
