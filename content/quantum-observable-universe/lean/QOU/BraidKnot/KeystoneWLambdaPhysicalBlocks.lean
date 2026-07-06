import QOU.BraidKnot.WLambdaMTCLocalizationObligation

/-!
# W_λ keystone — the localization obligation at the **physical** blocks (n = 4, 5)

[`WLambdaMTCLocalizationObligation.lean`](WLambdaMTCLocalizationObligation.lean) states the
owner-gated residual-(i) matching obligation as a `§3b-cond` class `BeasleyWittenLocalization`,
derives the keystone's necessary conditions C1 (normalization), C2 (chirality-blindness), C6
(full support), and gives `heckeLocalizationOfPos` — the construction of the **genuine** Hecke
q-Plancherel localization `loc = d_q²/D²` on *any* conjugate-closed sorted block set at `q > 1`.
Its only worked model is the trivial `n = 2` case where every `d_q = 1` (so `loc ≡ 1/2`); that
file flags **"a stronger `n=4` witness with the genuine non-trivial `d_q` values is future work."**

This file supplies that, at the **two physically relevant sizes**:

* **`n = 5`** — the s5-so3 keystone proper (`S₅`): the seven Hecke blocks `λ ⊢ 5`, including the
  **electron** block `(3,1,1)` (self-conjugate) and the **muon** block `(3,2)` (transpose
  `(2,2,1)`). These are the blocks whose q-Plancherel weights `W_λ = d_q(λ)²/D²` the gauge datum
  on `S³/2I` must reproduce.
* **`n = 4`** — the file's named warm-up, with genuinely non-trivial `d_q` (the blocks `(3,1)` /
  `(2,1,1)` have `d_q ≠ 1`).

For each size we instantiate `heckeLocalizationOfPos` on the actual partition combinatorics
(conjugate-closure + sortedness discharged by `decide`) and specialise the **derived** keystone
necessary conditions to the physical blocks:

* **C1** `keystone{Four,Five}_normalized` — `Σ_λ W_λ = 1` over the real blocks.
* **C2** `keystone_muon_transpose_eq` — the muon block and its transpose carry equal weight,
  `W_{(3,2)} = W_{(2,2,1)}` (chirality-blindness on a genuine non-self-conjugate pair).
* **C6** `keystone_{electron,muon}_pos` — the electron and muon blocks carry **strictly positive**
  Plancherel weight (no physical block is dropped).

Nothing here is fitted or owner-gated: it is the formalize-first specialisation of already-proved
machinery to the physical partition blocks, making the keystone's necessary conditions concrete at
the electron/muon weights the geometric realization must hit.

**Base ring.** `ℝ` is genuine here (§7c): the construction needs `1 < q` (positivity of `d_q`,
`qDim_pos`/`sum_qDimSq_pos`), an archimedean fact. No `q₀` literal; `q` stays a free real `> 1`.
-/

open Finset QOU.MathlibExt.QPartitionCombinatorics

namespace QOU.BraidKnot.Keystone

/-! ## n = 5 — the s5-so3 keystone blocks (electron, muon) -/

/-- The seven Hecke partition blocks `λ ⊢ 5` of the s5-so3 keystone:
`[5]`, `[4,1]`, **`[3,2]` (muon)**, **`[3,1,1]` (electron, self-conjugate)**, `[2,2,1]`,
`[2,1,1,1]`, `[1,1,1,1,1]`. Closed under transpose. -/
def keystonePartitionsFive : Finset (List ℕ) :=
  {[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]}

theorem keystoneFive_sorted :
    ∀ l ∈ keystonePartitionsFive, l.Sorted (· ≥ ·) := by decide

theorem keystoneFive_conj_closed :
    ∀ l ∈ keystonePartitionsFive, Partition.conjugate l ∈ keystonePartitionsFive := by decide

theorem keystoneFive_nonempty : keystonePartitionsFive.Nonempty := by decide

/-- The muon block `(3,2)` is one of the keystone blocks. -/
theorem keystoneFive_mem_muon : ([3, 2] : List ℕ) ∈ keystonePartitionsFive := by decide

/-- The genuine Hecke q-Plancherel localization on the seven `n = 5` keystone blocks, for any
`q > 1`. Its `loc` is exactly `W_λ = d_q(λ)²/D²`, and it satisfies C1/C2/C6 by the derived
theorems of [`WLambdaMTCLocalizationObligation.lean`](WLambdaMTCLocalizationObligation.lean). -/
noncomputable def keystoneLocalizationFive (q : ℝ) (hq : 1 < q) :
    BeasleyWittenLocalization ℝ :=
  heckeLocalizationOfPos q hq keystonePartitionsFive
    keystoneFive_sorted keystoneFive_conj_closed keystoneFive_nonempty

/-- **C1 at n = 5.** The seven keystone q-Plancherel weights sum to `1`:
`Σ_{λ ⊢ 5} W_λ = 1`. -/
theorem keystoneFive_normalized (q : ℝ) (hq : 1 < q) :
    (∑ p ∈ (keystoneLocalizationFive q hq).parts, (keystoneLocalizationFive q hq).loc p) = 1 :=
  loc_isProbabilityMeasure (h := keystoneLocalizationFive q hq)

/-- **C6 — the electron block carries strictly positive weight.** `W_{(3,1,1)} > 0`. -/
theorem keystone_electron_pos (q : ℝ) (hq : 1 < q) :
    0 < (keystoneLocalizationFive q hq).loc [3, 1, 1] :=
  heckeLocalizationOfPos_loc_pos q hq keystonePartitionsFive
    keystoneFive_sorted keystoneFive_conj_closed keystoneFive_nonempty [3, 1, 1]

/-- **C6 — the muon block carries strictly positive weight.** `W_{(3,2)} > 0`. -/
theorem keystone_muon_pos (q : ℝ) (hq : 1 < q) :
    0 < (keystoneLocalizationFive q hq).loc [3, 2] :=
  heckeLocalizationOfPos_loc_pos q hq keystonePartitionsFive
    keystoneFive_sorted keystoneFive_conj_closed keystoneFive_nonempty [3, 2]

/-- **C2 on the muon block — chirality-blindness on a genuine non-self-conjugate pair.**
The muon block `(3,2)` and its transpose `(2,2,1)` carry equal Plancherel weight:
`W_{(3,2)} = W_{(2,2,1)}`. (Unlike the electron `(3,1,1)`, which is self-conjugate, this is a
non-trivial instance of `loc λ′ = loc λ`.) -/
theorem keystone_muon_transpose_eq (q : ℝ) (hq : 1 < q) :
    (keystoneLocalizationFive q hq).loc [2, 2, 1] = (keystoneLocalizationFive q hq).loc [3, 2] := by
  have hc : Partition.conjugate ([3, 2] : List ℕ) = [2, 2, 1] := by decide
  have key := loc_conj_eq (h := keystoneLocalizationFive q hq) [3, 2] keystoneFive_mem_muon
  rwa [show (keystoneLocalizationFive q hq).conj [3, 2] = ([2, 2, 1] : List ℕ) from hc] at key

/-! ## n = 4 — the named warm-up witness (genuinely non-trivial `d_q`) -/

/-- The five Hecke partition blocks `λ ⊢ 4`: `[4]`, `[3,1]`, `[2,2]`, `[2,1,1]`, `[1,1,1,1]`.
Closed under transpose (`[4]↔[1^4]`, `[3,1]↔[2,1,1]`, `[2,2]` self-conjugate). -/
def keystonePartitionsFour : Finset (List ℕ) :=
  {[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]}

theorem keystoneFour_sorted :
    ∀ l ∈ keystonePartitionsFour, l.Sorted (· ≥ ·) := by decide

theorem keystoneFour_conj_closed :
    ∀ l ∈ keystonePartitionsFour, Partition.conjugate l ∈ keystonePartitionsFour := by decide

theorem keystoneFour_nonempty : keystonePartitionsFour.Nonempty := by decide

/-- The block `(3,1)` is one of the `n = 4` blocks. -/
theorem keystoneFour_mem_31 : ([3, 1] : List ℕ) ∈ keystonePartitionsFour := by decide

/-- The genuine Hecke q-Plancherel localization on the five `n = 4` blocks, for any `q > 1`. -/
noncomputable def keystoneLocalizationFour (q : ℝ) (hq : 1 < q) :
    BeasleyWittenLocalization ℝ :=
  heckeLocalizationOfPos q hq keystonePartitionsFour
    keystoneFour_sorted keystoneFour_conj_closed keystoneFour_nonempty

/-- **C1 at n = 4.** `Σ_{λ ⊢ 4} W_λ = 1`. -/
theorem keystoneFour_normalized (q : ℝ) (hq : 1 < q) :
    (∑ p ∈ (keystoneLocalizationFour q hq).parts, (keystoneLocalizationFour q hq).loc p) = 1 :=
  loc_isProbabilityMeasure (h := keystoneLocalizationFour q hq)

/-- **C2 at n = 4 — `[3,1]` and its transpose `[2,1,1]` carry equal weight** (genuinely
non-trivial `d_q`). -/
theorem keystoneFour_transpose_eq (q : ℝ) (hq : 1 < q) :
    (keystoneLocalizationFour q hq).loc [2, 1, 1] = (keystoneLocalizationFour q hq).loc [3, 1] := by
  have hc : Partition.conjugate ([3, 1] : List ℕ) = [2, 1, 1] := by decide
  have key := loc_conj_eq (h := keystoneLocalizationFour q hq) [3, 1] keystoneFour_mem_31
  rwa [show (keystoneLocalizationFour q hq).conj [3, 1] = ([2, 1, 1] : List ℕ) from hc] at key

end QOU.BraidKnot.Keystone
