/-
Copyright (c) 2026. All rights reserved.

# Which strand counts can carry a γγ-produced lepton pair e⁻ ⊔ ν̄

Owner, 2026-11-21: *"Resolve the anti-neutrino by checking the gamma gamma production to get
there."* The electron is σ₀σ₁σ₀ (closure: the Hopf link, two components), and the antineutrino
is the unknot (`predicted-spectra/antineutrino-knot`). So e⁻ ⊔ ν̄ is a three-component link.

A γγ-produced word is a product of vertices `σᵢσᵢ₊₁⁻¹`
(`QOU.Mass.GammaGammaWordSelection.GammaGammaWord`). Each vertex permutes the strands by two
adjacent transpositions, so a γγ word is an even permutation. For a permutation of `n` strands
the number of closure components `c` satisfies `sign = (−1)^(n + c)`. Hence:

* `gammaGamma_components_parity` : the closure of a γγ word on `n` strands has
  `n + c` even.
* `no_lepton_pair_on_four_strands` : no γγ word on four strands closes to three components,
  so e⁻ ⊔ ν̄ cannot be γγ-produced on four strands (and, by the same parity, on any even
  number of strands).

Purely combinatorial; no ring, no q, no empirical input.
-/
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.Perm.Sign
import QOU.Mass.GammaGammaWordSelection

namespace QOU.QBeta.GammaGammaLeptonPair

open Equiv QOU.Mass.GammaGammaWordSelection

/-- Number of closure components of a braid with strand permutation `σ`: one per cycle,
fixed points included. -/
def numComponents {n : ℕ} (σ : Perm (Fin n)) : ℕ :=
  Multiset.card σ.cycleType + (n - σ.support.card)

theorem sign_eq_neg_one_pow {n : ℕ} (σ : Perm (Fin n)) :
    (Perm.sign σ : ℤˣ) = (-1) ^ (n + numComponents σ) := by
  have hle : σ.support.card ≤ n := by
    simpa using Finset.card_le_univ σ.support
  have e : n + numComponents σ =
      (σ.cycleType.sum + Multiset.card σ.cycleType) + 2 * (n - σ.support.card) := by
    rw [numComponents, Perm.sum_cycleType]
    omega
  rw [Perm.sign_of_cycleType, e, pow_add, pow_add, pow_mul]
  simp [← pow_add]

/-- The strand permutation of one crossing on `n` strands (identity if out of range). -/
def crossingPerm (n : ℕ) (c : Crossing) : Perm (Fin n) :=
  if h : c.gen + 1 < n then swap ⟨c.gen, by omega⟩ ⟨c.gen + 1, h⟩ else 1

/-- The strand permutation of a word. -/
def wordPerm (n : ℕ) (w : Word) : Perm (Fin n) := (w.map (crossingPerm n)).prod

/-- Every crossing acts on strands `0 … n−1`. -/
def InRange (n : ℕ) (w : Word) : Prop := ∀ c ∈ w, c.gen + 1 < n

theorem sign_crossingPerm {n : ℕ} {c : Crossing} (h : c.gen + 1 < n) :
    Perm.sign (crossingPerm n c) = -1 := by
  rw [crossingPerm, dif_pos h, Perm.sign_swap]
  intro heq
  have := congrArg Fin.val heq
  simp at this

theorem wordPerm_append (n : ℕ) (u v : Word) :
    wordPerm n (u ++ v) = wordPerm n u * wordPerm n v := by
  simp [wordPerm, List.map_append, List.prod_append]

theorem sign_wordPerm_gammaGamma {n : ℕ} {w : Word} (hw : GammaGammaWord w)
    (hr : InRange n w) : Perm.sign (wordPerm n w) = 1 := by
  induction hw with
  | nil => simp [wordPerm]
  | cons i hw ih =>
    have h0 : (⟨i, true⟩ : Crossing).gen + 1 < n := hr _ (by simp [vertex])
    have h1 : (⟨i + 1, false⟩ : Crossing).gen + 1 < n := hr _ (by simp [vertex])
    have hr' : InRange n _ := fun c hc => hr c (List.mem_append_right _ hc)
    rw [wordPerm_append, Perm.sign_mul, ih hr']
    simp only [vertex, wordPerm, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      mul_one, Perm.sign_mul, sign_crossingPerm h0, sign_crossingPerm h1]
    decide

/-- **Parity.** A γγ word on `n` strands closes to `c` components with `n + c` even. -/
theorem gammaGamma_components_parity {n : ℕ} {w : Word} (hw : GammaGammaWord w)
    (hr : InRange n w) : Even (n + numComponents (wordPerm n w)) := by
  have h := sign_eq_neg_one_pow (wordPerm n w)
  rw [sign_wordPerm_gammaGamma hw hr] at h
  exact (neg_one_pow_eq_one_iff_even (by decide)).mp h.symm

/-- e⁻ ⊔ ν̄ (three components) is not the closure of any γγ word on four strands. -/
theorem no_lepton_pair_on_four_strands {w : Word} (hw : GammaGammaWord w)
    (hr : InRange 4 w) : numComponents (wordPerm 4 w) ≠ 3 := by
  intro h3
  have := gammaGamma_components_parity hw hr
  rw [h3] at this
  exact (by decide : ¬ Even (4 + 3)) this

/-- More generally: three components need an odd number of strands. -/
theorem lepton_pair_needs_odd_strands {n : ℕ} {w : Word} (hw : GammaGammaWord w)
    (hr : InRange n w) (h3 : numComponents (wordPerm n w) = 3) : Odd n := by
  have := gammaGamma_components_parity hw hr
  rw [h3] at this
  rcases Nat.even_or_odd n with he | ho
  · exfalso
    obtain ⟨k, hk⟩ := he
    obtain ⟨m, hm⟩ := this
    omega
  · exact ho

end QOU.QBeta.GammaGammaLeptonPair
