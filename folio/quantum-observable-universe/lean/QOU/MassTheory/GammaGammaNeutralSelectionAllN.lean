import QOU.MassTheory.GammaGammaSelectionAllK
import QOU.StandardModel.PhotonU1NeutralCut

/-!
# The neutrality rule selects `β_Bor` in the full photon-term grammar, for every crossing count

Bean `qou-99qc`. Owner 2026-11-22: "Find proof of the selection as well. Can we do it for all n?"

The adopted γγ rule (owner-rulings 2026-11-21) keeps the linking-neutral words of the photon
product grammar and then applies reading-3 Frobenius selection. The probe
`computations/probes/gg_photon_cut/u1_neutral_cut_probe.py` checked this only up to 10
crossings. Here it is proved for words of every length.

## The argument

The non-identity terms of the ruled photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` are the blocks
`σ₀`, `σ₁` and `V = σ₀σ₁⁻¹`. A word of the photon-term grammar is a concatenation of blocks.
Its writhe is the number of `σ₀` and `σ₁` blocks, because `V` has writhe `0`
(`writhe_photonTermWord`). A linking-neutral word has writhe `0`
(`QOU.PhotonU1NeutralCut.writhe_eq_zero_of_neutral`). So a neutral word has no `σ₀` or `σ₁`
block and is `V^k` (`eq_vertexPow_of_writhe_zero`). Free reduction does not change the writhe, and
`V^k` has no adjacent inverse pair, so the same holds for the freely reduced word
(`eq_vertexPow_of_reduces`). On `V^k`, `GammaGammaSelectionAllK` already proves that reading 3
selects `V³ = β_Bor` uniquely.

## What is proved (sorry-free)

* `writhe_zero_cands_eq`: the non-empty writhe-0 words of the grammar, before or after free
  reduction, are exactly `gammaGammaH3Cands` (the `V^k`, `k ≥ 1`).
* `frobeniusSelected_neutral_full_grammar` and `..._eq_borromean`: on `1 < q ≤ 23/20`, reading 3
  selects `β_Bor` among them, and nothing else.
* `neutralCands_subset`, `frobeniusSelected_linkingNeutral` and `..._eq_borromean`: the same with
  the candidates filtered by linking neutrality itself (`QOU.PhotonU1NeutralCut.Neutral`, every
  self-writhe and pairwise crossing count of the closure zero), so the step from neutrality to
  writhe `0` is mechanised, not prose.

## Scope

* The first pair of theorems filters by writhe `0`; the second by linking neutrality. Neutrality
  implies writhe `0`, so the result holds for the neutrality rule and the weaker writhe-0 rule.
* The window `1 < q ≤ 23/20` is inherited from `GammaGammaSelectionAllK`.
* Three strands (`H₃`) only. Four or more strands is a different grammar and is not covered.
* The probe's reduced words are cost-ranked by reduced length; on `V^k` reduced and unreduced
  length agree, so the cost is the same.
-/

namespace QOU.Mass.GammaGammaNeutralSelectionAllN

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaFrobeniusSelection
open QOU.Mass.GammaGammaSelectionAllK

/-- The three non-identity photon terms on three strands. -/
inductive Block
  | s0
  | s1
  | v
  deriving DecidableEq

/-- The braid word of a photon term. -/
def Block.word : Block → Word
  | .s0 => [⟨0, true⟩]
  | .s1 => [⟨1, true⟩]
  | .v => vertex 0

/-- The word of a list of photon terms (the expansion of a photon product, before reduction). -/
def termWord (bs : List Block) : Word := (bs.map Block.word).flatten

theorem termWord_cons (b : Block) (bs : List Block) :
    termWord (b :: bs) = b.word ++ termWord bs := by
  simp [termWord]

/-- Writhe of a photon-term word: the number of `σ₀` and `σ₁` blocks. -/
theorem writhe_photonTermWord (bs : List Block) :
    writhe (termWord bs) = (bs.filter (fun b => b ≠ .v)).length := by
  induction bs with
  | nil => simp [termWord, writhe]
  | cons b bs ih =>
    rw [termWord_cons, writhe_append, ih]
    cases b <;> simp [Block.word, writhe, sign, vertex] <;> omega

theorem termWord_all_v (k : ℕ) : termWord (List.replicate k .v) = vertexPow k := by
  induction k with
  | zero => rfl
  | succ k ih => rw [List.replicate_succ, termWord_cons, ih]; rfl

/-- **A writhe-0 photon-term word is `V^k`.** -/
theorem eq_vertexPow_of_writhe_zero (bs : List Block) (h : writhe (termWord bs) = 0) :
    termWord bs = vertexPow bs.length := by
  rw [writhe_photonTermWord] at h
  have hlen : (bs.filter (fun b => b ≠ .v)).length = 0 := by exact_mod_cast h
  have hall : ∀ b ∈ bs, b = .v := by
    intro b hb
    by_contra hne
    have : b ∈ bs.filter (fun b => b ≠ .v) := List.mem_filter.2 ⟨hb, by simpa using hne⟩
    rw [List.length_eq_zero_iff] at hlen
    rw [hlen] at this
    simp at this
  rw [List.eq_replicate_iff.2 ⟨rfl, hall⟩, termWord_all_v, List.length_replicate]

/-! ## Free reduction -/

/-- The inverse of a crossing. -/
def inv (c : Crossing) : Crossing := ⟨c.gen, !c.pos⟩

/-- One free-reduction step: delete an adjacent pair `c c⁻¹`. -/
inductive Step : Word → Word → Prop
  | cancel (u v : Word) (c : Crossing) : Step (u ++ c :: inv c :: v) (u ++ v)

/-- Free reduction: any number of steps. -/
inductive Reduces : Word → Word → Prop
  | refl (w : Word) : Reduces w w
  | step {w w' r : Word} : Step w w' → Reduces w' r → Reduces w r

theorem writhe_step {w w' : Word} (h : Step w w') : writhe w' = writhe w := by
  cases h with
  | cancel u v c =>
    simp only [writhe, List.map_append, List.map_cons, List.sum_append, List.sum_cons, inv, sign]
    cases c.pos <;> simp

theorem writhe_reduces {w r : Word} (h : Reduces w r) : writhe r = writhe w := by
  induction h with
  | refl => rfl
  | step hs _ ih => rw [ih, writhe_step hs]

/-- No two adjacent crossings of `V^k` are inverse to each other. -/
def NoCancel (w : Word) : Prop := List.IsChain (fun a b => b ≠ inv a) w

theorem noCancel_vertexPow (k : ℕ) : NoCancel (vertexPow k) := by
  induction k with
  | zero => exact List.isChain_nil
  | succ k ih =>
    unfold NoCancel at *
    show List.IsChain _ ([⟨0, true⟩, ⟨1, false⟩] ++ vertexPow k)
    refine List.isChain_append.2 ⟨by simp [inv], ih, ?_⟩
    intro x hx y hy
    simp at hx
    subst hx
    cases k with
    | zero => simp [vertexPow] at hy
    | succ k =>
      simp [vertexPow, vertex] at hy
      subst hy; simp [inv]

theorem not_step_of_noCancel {w w' : Word} (hw : NoCancel w) : ¬ Step w w' := by
  intro h
  cases h with
  | cancel u v c =>
    unfold NoCancel at hw
    have h2 : List.IsChain (fun a b => b ≠ inv a) (c :: inv c :: v) :=
      (List.isChain_append.1 hw).2.1
    exact (List.isChain_cons_cons.1 h2).1 rfl

theorem reduces_eq_of_noCancel {w r : Word} (hw : NoCancel w) (h : Reduces w r) : r = w := by
  cases h with
  | refl => rfl
  | step hs _ => exact absurd hs (not_step_of_noCancel hw)

/-- **The same holds after free reduction.** -/
theorem eq_vertexPow_of_reduces (bs : List Block) {r : Word}
    (hr : Reduces (termWord bs) r) (h : writhe r = 0) :
    r = vertexPow bs.length := by
  rw [writhe_reduces hr] at h
  have hw := eq_vertexPow_of_writhe_zero bs h
  rw [hw] at hr
  exact reduces_eq_of_noCancel (noCancel_vertexPow _) hr

/-! ## The selection -/

/-- Candidates: non-empty, freely reduced forms of photon-term words, with writhe `0`. -/
def writheZeroCands : Set Word :=
  {r | ∃ bs, Reduces (termWord bs) r ∧ writhe r = 0 ∧ r ≠ []}

theorem writhe_zero_cands_eq : writheZeroCands = gammaGammaH3Cands := by
  ext r
  constructor
  · rintro ⟨bs, hr, h0, hne⟩
    rw [eq_vertexPow_of_reduces bs hr h0] at hne ⊢
    refine mem_cands_iff_vertexPow.2 ⟨bs.length, ?_, rfl⟩
    rcases Nat.eq_zero_or_pos bs.length with h | h
    · rw [h] at hne; exact absurd rfl hne
    · exact h
  · intro hr
    obtain ⟨k, _, rfl⟩ := mem_cands_iff_vertexPow.1 hr
    refine ⟨List.replicate k .v, ?_, ?_, hr.2.2⟩
    · rw [termWord_all_v]; exact .refl _
    · exact writhe_eq_zero (vertexPow_gammaGamma k)

/-- **Reading 3 selects `β_Bor` in the full photon-term grammar, for every crossing count.** -/
theorem frobeniusSelected_neutral_full_grammar {q b : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (hbr : HoefsmitRoot q b)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusSelected (hoefsmitH3 q b) y writheZeroCands (fun w => (w.length : ℝ)) borromean := by
  rw [writhe_zero_cands_eq]; exact frobeniusSelected_borromean_all hq1 hq2 hbr y hy

theorem frobeniusSelected_neutral_full_grammar_eq_borromean {q b : ℝ} (hq1 : 1 < q)
    (hq2 : q ≤ 23 / 20)
    (hbr : HoefsmitRoot q b) (y : H3Block → ℝ) (hy : 0 < y .std) {w : Word}
    (hw : FrobeniusSelected (hoefsmitH3 q b) y writheZeroCands (fun w => (w.length : ℝ)) w) :
    w = borromean := by
  rw [writhe_zero_cands_eq] at hw; exact frobeniusSelected_all_eq_borromean hq1 hq2 hbr y hy hw

/-! ## Linking neutrality itself, not only writhe `0` -/

/-- A crossing as a letter of `QOU.PhotonU1NeutralCut` (generator, sign). -/
def toLetter (c : Crossing) : QOU.PhotonU1NeutralCut.Letter := (c.gen, sign c)

theorem u1Writhe_map_toLetter (w : Word) :
    QOU.PhotonU1NeutralCut.writhe (w.map toLetter) = writhe w := by
  induction w with
  | nil => simp [QOU.PhotonU1NeutralCut.writhe, writhe]
  | cons c w ih =>
    simp only [List.map_cons, QOU.PhotonU1NeutralCut.writhe, toLetter, ih]
    simp [writhe]

/-- Candidates: non-empty freely reduced photon-term words that are linking-neutral. -/
def neutralCands : Set Word :=
  {r | ∃ bs, Reduces (termWord bs) r ∧ QOU.PhotonU1NeutralCut.Neutral (r.map toLetter) ∧ r ≠ []}

theorem neutralCands_subset : neutralCands ⊆ writheZeroCands := by
  rintro r ⟨bs, hr, hn, hne⟩
  refine ⟨bs, hr, ?_, hne⟩
  rw [← u1Writhe_map_toLetter]
  exact QOU.PhotonU1NeutralCut.writhe_eq_zero_of_neutral _ hn

theorem borromean_mem_neutralCands : borromean ∈ neutralCands := by
  refine ⟨List.replicate 3 .v, ?_, ?_, by simp [borromean, vertex]⟩
  · rw [termWord_all_v, vertexPow_three]; exact .refl _
  · decide

/-- **Reading 3 selects `β_Bor` among the linking-neutral words, for every crossing count.** -/
theorem frobeniusSelected_linkingNeutral {q b : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (hbr : HoefsmitRoot q b)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusSelected (hoefsmitH3 q b) y neutralCands (fun w => (w.length : ℝ)) borromean := by
  have h := frobeniusSelected_neutral_full_grammar hq1 hq2 hbr y hy
  exact ⟨borromean_mem_neutralCands, h.feasible,
    fun w' hw' hf => h.minimal w' (neutralCands_subset hw') hf⟩

theorem frobeniusSelected_linkingNeutral_eq_borromean {q b : ℝ} (hq1 : 1 < q)
    (hq2 : q ≤ 23 / 20)
    (hbr : HoefsmitRoot q b) (y : H3Block → ℝ) (hy : 0 < y .std) {w : Word}
    (hw : FrobeniusSelected (hoefsmitH3 q b) y neutralCands (fun w => (w.length : ℝ)) w) :
    w = borromean := by
  have hb := frobeniusSelected_neutral_full_grammar hq1 hq2 hbr y hy
  have hle : (w.length : ℝ) ≤ (borromean.length : ℝ) :=
    hw.minimal _ borromean_mem_neutralCands hb.feasible
  refine frobeniusSelected_neutral_full_grammar_eq_borromean hq1 hq2 hbr y hy
    ⟨neutralCands_subset hw.mem, hw.feasible, fun w' hw' hf => ?_⟩
  exact le_trans hle (hb.minimal w' hw' hf)

end QOU.Mass.GammaGammaNeutralSelectionAllN
