/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# `(w − n) mod 2` is the complete Markov invariant of the level pair, and it is
# the component parity of the closure

Bean `qou-owft` (V12), under epic `qou-qia8`.  Companion to
`WritheMarkovInvariance.lean`, which shows the writhe is Markov-I invariant but
not Markov-II invariant.

`markov-moves-brane-tower.md` calls conjugation the *horizontal* direction and
stabilisation the *vertical* one.  Markov II acts on the pair `(w, n)` — writhe
and strand number — as `(w ± 1, n + 1)`.  This file settles exactly what
survives that action.

## What is proved (all sorry-free)

**Parity of the pair.**

* `markovPair_parity` — `(w − n) mod 2` is invariant under both moves
  (soundness).
* `markovPair_of_even` — and it is **complete**: any two level pairs with the
  same `(w − n)` parity are Markov-equivalent.  So `(w − n) mod 2` is *the*
  invariant of the pair, not merely *an* invariant.
* `writhe_not_pair_invariant`, `writhe_sub_level_not_pair_invariant`,
  `writhe_add_level_not_pair_invariant` — `w`, `w − n` and `w + n` are each
  **not** invariant, so nothing coarser than the parity survives.

**Why it is the component parity.**

* `writhe_sub_length_even` — `writhe β ≡ length β (mod 2)`, because every
  crossing sign is `±1` and `±1 ≡ 1 (mod 2)`.  This is the only step of the
  bridge that is framework-side, and it is proved outright.
* `component_parity_of_permSign` — **conditional** on the classical
  cycle-sign identity `sign(π) = (−1)^{n−c}` for a permutation of `n` letters
  with `c` cycles (carried as an explicit hypothesis, `_of_` named per
  §3b-cond): the closure of `β ∈ B_n` has `c` components with
  `c ≡ (w − n) (mod 2)`.
* `carrier_component_parity` — the identity verified by kernel computation on
  every carrier the corpus names, with the component count computed from the
  braid word's underlying permutation (nothing assumed).

**The statistics reading is refuted.**

* `statistics_reading_fails_on_gluon` — reading component parity as
  fermion/boson statistics matches the leptons (1 component, odd, fermion) and
  the Borromean baryon (3 components, odd, fermion), but the gluon unit
  `σ₁σ₂⁻¹ ∈ B₃` closes to a **single** component, hence odd, hence "fermion".
  The gluon is a boson.  The identity is a theorem; the physical reading is
  not.

## Honest scope

`markovPair_parity` / `markovPair_of_even` are statements about the pair
`(w, n)` under the moves' *action on that pair*, which is all Markov II
determines.  They do not claim every pair of braids with matching parity is
Markov-equivalent as braids — that is false, and much stronger.

`component_parity_of_permSign` is **conditional**, and `(w − n) mod 2` carries
exactly one bit.  It cannot carry `Q`, `I₃`, or a `δ_q` magnitude; it is a
*consistency check* on level-crossing claims, not a substitute for the writhe.
Under the owner ruling (`WritheMarkovInvariance.lean`) the substitute for the
writhe is its value at the braid index, not this parity.

`Int`/`Nat` arithmetic throughout; no `Real`, no ordering, no division (§7c).
-/

import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Algebra.Group.Even
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace QOU.StandardModel.LevelParity

/-- A braid word: entry `±i` denotes `σᵢ^{±1}`.  Same convention as
`ChiralFermionBraidWords.lean` and `WritheMarkovInvariance.lean`. -/
abbrev BraidWord := List ℤ

/-- The writhe: the sum of the crossing signs. -/
def writhe (β : BraidWord) : ℤ := (β.map Int.sign).sum

/-! ### 1. The writhe has the parity of the word length -/

/-- **`writhe β ≡ length β (mod 2)`.**

Every letter of a braid word is a nonzero generator, so contributes `±1` to the
writhe and `1` to the length; `±1 − 1 ∈ {0, −2}` is even.  This is the one
framework-side step of the bridge to component parity, and it is unconditional. -/
theorem writhe_sub_length_even (β : BraidWord) (h : ∀ g ∈ β, g ≠ 0) :
    Even (writhe β - (β.length : ℤ)) := by
  induction β with
  | nil => exact ⟨0, by simp [writhe]⟩
  | cons x xs ih =>
      have hx : x ≠ 0 := h x (by simp)
      have hxs : ∀ g ∈ xs, g ≠ 0 := fun g hg => h g (List.mem_cons_of_mem x hg)
      obtain ⟨r, hr⟩ := ih hxs
      -- `Int.sign x = 1` or `-1`
      have hsign : Int.sign x = 1 ∨ Int.sign x = -1 := by
        rcases lt_trichotomy x 0 with hlt | heq | hgt
        · exact Or.inr (Int.sign_eq_neg_one_iff_neg.mpr hlt)
        · exact absurd heq hx
        · exact Or.inl (Int.sign_eq_one_iff_pos.mpr hgt)
      have hw : writhe (x :: xs) = Int.sign x + writhe xs := by
        simp [writhe]
      have hlen : ((x :: xs).length : ℤ) = 1 + (xs.length : ℤ) := by
        simp [List.length_cons]; ring
      rcases hsign with hs | hs
      · exact ⟨r, by rw [hw, hlen, hs]; linarith [hr]⟩
      · exact ⟨r - 1, by rw [hw, hlen, hs]; linarith [hr]⟩

/-! ### 2. The Markov action on the level pair `(w, n)` -/

/-- The equivalence generated by the two Markov-II moves on the level pair
`(writhe, strand number)`.  Markov I acts trivially on the pair (it changes
neither coordinate, by `WritheMarkovInvariance.writhe_conj`), so it contributes
no generator here. -/
inductive MarkovPair : ℤ × ℤ → ℤ × ℤ → Prop where
  | refl (p : ℤ × ℤ) : MarkovPair p p
  | symm {p q : ℤ × ℤ} : MarkovPair p q → MarkovPair q p
  | trans {p q r : ℤ × ℤ} : MarkovPair p q → MarkovPair q r → MarkovPair p r
  /-- Positive stabilisation `β ↦ βσₙ`. -/
  | stab (w n : ℤ) : MarkovPair (w, n) (w + 1, n + 1)
  /-- Negative stabilisation `β ↦ βσₙ⁻¹`. -/
  | destab (w n : ℤ) : MarkovPair (w, n) (w - 1, n + 1)

/-- **Soundness: `(w − n) mod 2` is Markov-invariant.**

Positive stabilisation leaves `w − n` alone outright; negative stabilisation
shifts it by `−2`.  Either way the parity is untouched. -/
theorem markovPair_parity {p q : ℤ × ℤ} (h : MarkovPair p q) :
    Even ((p.1 - p.2) - (q.1 - q.2)) := by
  induction h with
  | refl p => exact ⟨0, by ring⟩
  | symm _ ih => obtain ⟨r, hr⟩ := ih; exact ⟨-r, by linarith⟩
  | trans _ _ ih₁ ih₂ =>
      obtain ⟨r₁, h₁⟩ := ih₁
      obtain ⟨r₂, h₂⟩ := ih₂
      exact ⟨r₁ + r₂, by linarith⟩
  | stab w n => exact ⟨0, by simp⟩
  | destab w n => exact ⟨1, by simp; ring⟩

/-- Stabilisation with the target pair given up to arithmetic normalisation. -/
private theorem stab' (w n w' n' : ℤ) (hw : w' = w + 1) (hn : n' = n + 1) :
    MarkovPair (w, n) (w', n') := by
  subst hw; subst hn; exact MarkovPair.stab w n

/-- Negative stabilisation, likewise. -/
private theorem destab' (w n w' n' : ℤ) (hw : w' = w - 1) (hn : n' = n + 1) :
    MarkovPair (w, n) (w', n') := by
  subst hw; subst hn; exact MarkovPair.destab w n

/-- Stabilising then destabilising back shifts the writhe by `2` at fixed level. -/
private theorem shift_two_one (w n : ℤ) : MarkovPair (w, n) (w + 2, n) :=
  MarkovPair.trans (stab' w n (w + 1) (n + 1) rfl rfl)
    (MarkovPair.symm (destab' (w + 2) n (w + 1) (n + 1) (by ring) rfl))

/-- Hence the writhe may be shifted by any even amount at fixed level. -/
private theorem shift_two (w n k : ℤ) : MarkovPair (w, n) (w + 2 * k, n) := by
  refine Int.induction_on k ?_ ?_ ?_
  · simpa using MarkovPair.refl (w, n)
  · intro m ih
    have h2 : MarkovPair (w + 2 * (m : ℤ), n) (w + 2 * ((m : ℤ) + 1), n) := by
      have hone := shift_two_one (w + 2 * (m : ℤ)) n
      have e : w + 2 * (m : ℤ) + 2 = w + 2 * ((m : ℤ) + 1) := by ring
      rwa [e] at hone
    exact MarkovPair.trans ih h2
  · intro m ih
    have h2 : MarkovPair (w + 2 * (-(m : ℤ) - 1), n) (w + 2 * (-(m : ℤ)), n) := by
      have hone := shift_two_one (w + 2 * (-(m : ℤ) - 1)) n
      have e : w + 2 * (-(m : ℤ) - 1) + 2 = w + 2 * (-(m : ℤ)) := by ring
      rwa [e] at hone
    exact MarkovPair.trans ih (MarkovPair.symm h2)

/-- Climbing the tower `k` levels by positive stabilisation. -/
private theorem climb (w n : ℤ) : ∀ k : ℕ, MarkovPair (w, n) (w + k, n + k)
  | 0 => by simpa using MarkovPair.refl (w, n)
  | k + 1 =>
      MarkovPair.trans (climb w n k)
        (stab' (w + (k : ℤ)) (n + (k : ℤ)) (w + ((k + 1 : ℕ) : ℤ))
          (n + ((k + 1 : ℕ) : ℤ))
          (by simp only [Nat.cast_succ]; ring)
          (by simp only [Nat.cast_succ]; ring))

/-- **Completeness, upward case.**  If `n ≤ n'` and the two pairs have the same
`(w − n)` parity, they are Markov-equivalent: climb to level `n'`, then shift
the writhe by the residual even amount. -/
theorem markovPair_of_even_of_le {w n w' n' : ℤ} (hle : n ≤ n')
    (h : Even ((w' - n') - (w - n))) : MarkovPair (w, n) (w', n') := by
  obtain ⟨r, hr⟩ := h
  set k : ℕ := (n' - n).toNat with hk
  have hkc : (k : ℤ) = n' - n := Int.toNat_of_nonneg (by linarith)
  have hclimb : MarkovPair (w, n) (w + (k : ℤ), n + (k : ℤ)) := climb w n k
  have hlvl : n + (k : ℤ) = n' := by rw [hkc]; ring
  have hshift : MarkovPair (w + (k : ℤ), n') (w + (k : ℤ) + 2 * r, n') :=
    shift_two _ _ r
  have hw : w + (k : ℤ) + 2 * r = w' := by rw [hkc]; linarith
  rw [hlvl] at hclimb
  rw [hw] at hshift
  exact MarkovPair.trans hclimb hshift

/-- **Completeness.**  `(w − n) mod 2` is *the* invariant of the level pair:
two pairs are Markov-equivalent exactly when their parities agree. -/
theorem markovPair_of_even {w n w' n' : ℤ}
    (h : Even ((w' - n') - (w - n))) : MarkovPair (w, n) (w', n') := by
  rcases le_total n n' with hle | hle
  · exact markovPair_of_even_of_le hle h
  · obtain ⟨r, hr⟩ := h
    refine MarkovPair.symm (markovPair_of_even_of_le hle ⟨-r, by linarith⟩)

/-! ### 3. Nothing coarser than the parity survives -/

/-- The writhe itself is not invariant. -/
theorem writhe_not_pair_invariant :
    ¬ (∀ p q : ℤ × ℤ, MarkovPair p q → p.1 = q.1) := by
  intro hall
  have := hall (0, 0) (1, 1) (stab' 0 0 1 1 (by norm_num) (by norm_num))
  norm_num at this

/-- `w − n` — invariant under *positive* stabilisation — is destroyed by the
negative one, which shifts it by `−2`.  Only its parity survives. -/
theorem writhe_sub_level_not_pair_invariant :
    ¬ (∀ p q : ℤ × ℤ, MarkovPair p q → p.1 - p.2 = q.1 - q.2) := by
  intro hall
  have := hall (0, 0) (-1, 1) (destab' 0 0 (-1) 1 (by norm_num) (by norm_num))
  norm_num at this

/-- `w + n` is not invariant either. -/
theorem writhe_add_level_not_pair_invariant :
    ¬ (∀ p q : ℤ × ℤ, MarkovPair p q → p.1 + p.2 = q.1 + q.2) := by
  intro hall
  have := hall (0, 0) (1, 1) (stab' 0 0 1 1 (by norm_num) (by norm_num))
  norm_num at this

/-! ### 4. The bridge to component parity -/

/-- **`(w − n) mod 2` is the component parity of the closure.**

Conditional on the classical cycle-sign identity, carried as `hcycle`: the
underlying permutation of `β ∈ B_n` is a product of `length β` transpositions
(one per letter), and a permutation of `n` letters with `c` cycles has sign
`(−1)^{n−c}`; equating the two exponents gives `length β ≡ n − c (mod 2)`.
Combined with `writhe_sub_length_even` this yields `c ≡ w − n (mod 2)`.

The hypothesis is the *only* unproved input, and it is textbook.
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9 (§1.3, braid
-- group to symmetric group; §1.1, parity of permutations) -/
theorem component_parity_of_permSign
    (β : BraidWord) (hne : ∀ g ∈ β, g ≠ 0) (n c : ℤ)
    (hcycle : Even ((β.length : ℤ) - (n - c))) :
    Even ((writhe β - n) + c) := by
  obtain ⟨r, hr⟩ := writhe_sub_length_even β hne
  obtain ⟨s, hs⟩ := hcycle
  exact ⟨r + s, by linarith⟩

/-! ### 5. Component counts computed from the braid words -/

/-- Swap the entries at positions `i` and `i+1` of a one-line permutation. -/
def swapAt (l : List ℕ) (i : ℕ) : List ℕ :=
  match l[i]?, l[i + 1]? with
  | some a, some b => (l.set i b).set (i + 1) a
  | _, _ => l

/-- The underlying permutation of a braid word on `n` strands, in one-line
notation: generator `σᵢ^{±1}` acts as the transposition of strands `i` and
`i+1`, independently of the sign. -/
def permOf (n : ℕ) (β : BraidWord) : List ℕ :=
  β.foldl (fun l g => swapAt l (g.natAbs - 1)) (List.range n)

/-- Does the orbit of `j` under `p` reach an index below `j`?  Iterating `n`
times suffices for a permutation of `n` letters. -/
def orbitReachesBelow (p : List ℕ) (n j : ℕ) : Bool :=
  ((List.range n).foldl
      (fun (acc : Bool × ℕ) _ =>
        let x := (p[acc.2]?).getD acc.2
        (acc.1 || decide (x < j), x))
      (false, j)).1

/-- The number of cycles of `p`, counted by their minima — that is, the number
of components of the braid closure. -/
def numCycles (n : ℕ) (p : List ℕ) : ℕ :=
  ((List.range n).filter (fun j => !orbitReachesBelow p n j)).length

/-- Components of the closure of `β ∈ B_n`. -/
def components (n : ℕ) (β : BraidWord) : ℕ := numCycles n (permOf n β)

/-- `σ₁ⁿ ∈ B₂`, whose closure is the torus knot/link `T(2, n)`. -/
def sigma1Pow (k : ℕ) : BraidWord := List.replicate k 1

/-- The gluon unit `σ₁σ₂⁻¹ ∈ B₃`. -/
def gluonUnit : BraidWord := [1, -2]

/-- The Borromean baryon `𝓑₃ = (σ₁σ₂⁻¹)³ ∈ B₃`. -/
def borromean : BraidWord := gluonUnit ++ gluonUnit ++ gluonUnit

/-- **The component counts, computed.**

Each row is evaluated by the kernel from the braid word alone.  The Borromean
count `3` is a genuine check: the Borromean rings have three components. -/
theorem carrier_components :
    components 2 (sigma1Pow 1) = 1 ∧
    components 2 (sigma1Pow 2) = 2 ∧
    components 2 (sigma1Pow 3) = 1 ∧
    components 2 (sigma1Pow 5) = 1 ∧
    components 2 (sigma1Pow 7) = 1 ∧
    components 3 gluonUnit = 1 ∧
    components 3 borromean = 3 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> rfl

/-- **The identity `c ≡ w − n (mod 2)` on every carrier the corpus names.**

`νₑ = σ₁`, the Hopf link `σ₁²`, `e⁻ = σ₁³`, the higher generations `σ₁⁵`,
`σ₁⁷`, the gluon unit and the Borromean baryon.  Both sides are computed; the
writhes come from `writhe`, the component counts from `components`. -/
theorem carrier_component_parity :
    (writhe (sigma1Pow 1) - 2) % 2 = (components 2 (sigma1Pow 1) : ℤ) % 2 ∧
    (writhe (sigma1Pow 2) - 2) % 2 = (components 2 (sigma1Pow 2) : ℤ) % 2 ∧
    (writhe (sigma1Pow 3) - 2) % 2 = (components 2 (sigma1Pow 3) : ℤ) % 2 ∧
    (writhe (sigma1Pow 5) - 2) % 2 = (components 2 (sigma1Pow 5) : ℤ) % 2 ∧
    (writhe (sigma1Pow 7) - 2) % 2 = (components 2 (sigma1Pow 7) : ℤ) % 2 ∧
    (writhe gluonUnit - 3) % 2 = (components 3 gluonUnit : ℤ) % 2 ∧
    (writhe borromean - 3) % 2 = (components 3 borromean : ℤ) % 2 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-! ### 6. REFUTATION of the statistics reading -/

/-- **Component parity is not fermion/boson statistics.**

The tempting physical reading — odd component count ↔ fermion — matches the
leptons (`σ₁`, `σ₁³`: one component, odd) and the Borromean baryon (three
components, odd), all fermions.  It fails on the gluon unit: `σ₁σ₂⁻¹ ∈ B₃` has
underlying permutation a 3-cycle, so its closure is a **single** component,
hence odd, hence "fermion" — but the gluon is a boson.

So `carrier_component_parity` is a theorem about permutation cycles with no
framework content, and the statistics reading of it is refuted.  **Scope-(a)**:
this refutes *this* reading of component parity, not the possibility that some
other level-independent datum tracks statistics. -/
theorem statistics_reading_fails_on_gluon :
    components 3 borromean % 2 = 1 ∧
    components 2 (sigma1Pow 3) % 2 = 1 ∧
    components 3 gluonUnit % 2 = 1 := by
  refine ⟨?_, ?_, ?_⟩ <;> rfl

/-! ### 7. The minimal-level ruling closes the lepton-number escape -/

/-- **`L = sign(writhe)` does not survive the minimal-level ruling either.**

`ChiralFermionBraidWords.lean` rescued `L` from
`LeptonNumberCarrierChirality.lean`'s amphichirality obstruction by taking the
carrier to be the *braid word* rather than the knot type: `νₑ = σ₁` and
`ν̄ₑ = σ₁⁻¹` are distinct words, so the mirror acts freely on them even though
both close to the amphichiral unknot.

The owner ruling in `WritheMarkovInvariance.lean` — states are Gröbner–Shirshov
normal forms, and the observable is evaluated at the **lowest level of the
tower** — closes that escape.  The corpus assigns `νₑ = K_{0₁} = T(2,1)`, the
unknot, whose braid index is `1`; its minimal-level normal form is the *empty*
word, and so is its mirror's.  At the level where the framework says observables
live, the neutrino and the antineutrino are the **same state**, and no function
of the state can give them `+1` and `−1`.

The two hypotheses are exactly the two braid-index facts, carried explicitly.
The result is that `L` must come from something other than the writhe — the
Markov-II failure (`leptonNumber_not_markov_invariant`) and this one leave no
reading in which `sign(w)` is lepton number.

**Scope-(a)**: `L = sign(writhe)` is refuted under both readings of the gauge
freedom.  Lepton number itself, and the `Y = B − L` route, are untouched. -/
theorem leptonNumber_collapses_at_minimal_level
    (NF : BraidWord → BraidWord) (f : BraidWord → ℤ)
    (hnu : NF [1] = []) (hanu : NF [-1] = [])
    (hparticle : f (NF [1]) = 1) (hanti : f (NF [-1]) = -1) :
    False := by
  rw [hnu] at hparticle
  rw [hanu] at hanti
  rw [hparticle] at hanti
  norm_num at hanti

end QOU.StandardModel.LevelParity
