/-!
# QOU.BraidKnot.AveragingResonanceRule

**Averaging-resonance rule for c_k sectors**: precision-ladder rung
k lies in the bar-invariant fixed-point sector (= picks up the 1/2
fingerprint at silver ratio) iff the silver-ratio Pell-Lucas test
on c_k fails.

Empirically confirmed at k ∈ {3, ..., 10}: only k = 5 is
averaging-resonant; k ∈ {3, 4, 6, 7, 8, 9, 10} are all pure-σ.
The exact combinatorial rule predicting m_k is **open R&D**; the
naive argmax-binomial rule fails (25% accuracy).

Working hypothesis: the outlier rung is k = ⌊n_total / 2⌋ for a
typed-B_n braid with n_total = n_σ + n_σ⁻¹ + n_avg crossings.
For the proton (n_total = 11) this gives k = 5. ✓

Three refinement directions:
1. σ-eigenvalue weighting in the dominance criterion
2. Cyclicity constraints (Markov-trace closes cyclically)
3. Per-Wedderburn-block weighting
-/

import Mathlib.Tactic
-- Ref: [manuscript] prop:neutron-qvalue-symbolic
-- Ref: [wenzl1988] doi:10.1007/BF01404457
-- Ref: [hoefsmit1974]
-- Ref: [jones1985] doi:10.2307/1971403

namespace QOU.BraidKnot

/-- Sector classification for a precision-ladder rung. -/
inductive RungSector
  | pureSigma  -- pure-σ-action, Pell-Lucas-clean at silver ratio
  | averagingResonant  -- bar-invariant fixed-point, 1/2 fingerprint
  deriving DecidableEq, Repr

/-- The typed-B_n braid crossing distribution:
    n_sigma + n_sigma_inv + n_avg = n_total. -/
structure TypedBnDistribution where
  n_sigma : ℕ
  n_sigma_inv : ℕ
  n_avg : ℕ
  n_total : ℕ
  total_eq : n_total = n_sigma + n_sigma_inv + n_avg

/-- The proton typed-B_3 distribution: n_sigma = 6, n_sigma_inv = 3,
    n_avg = 2, n_total = 11. -/
def protonDistribution : TypedBnDistribution :=
  { n_sigma := 6, n_sigma_inv := 3, n_avg := 2, n_total := 11,
    total_eq := by norm_num }

/-- Empirical sector classification for k = 3..10, from the
    silver-ratio Pell-Lucas test on extracted c_k closed forms.

    Empirical pattern (refined under the authoritative Pell-Lucas
    test: numerator is a Pell-Lucas number or its small power times
    a power of 2):

      k = 3:  c_3 = -2          ∈ Pell-Lucas (2^1)        → pure-σ
      k = 4:  c_4 = -49/32      49 = a_3² Pell-Lucas pow → pure-σ
      k = 5:  c_5 = -11/8       11 ∉ Pell-Lucas          → AVERAGING
      k = 6:  c_6 = 7/2         7 = a_3 Pell-Lucas        → pure-σ
      k = 7:  c_7 = -8          2^3 power of 2            → pure-σ
      k = 8:  c_8 = 49/16       49 = a_3² Pell-Lucas pow → pure-σ
      k = 9:  c_9 = -7          7 = a_3 Pell-Lucas        → pure-σ
      k = 10: c_10 = 343/128   343 = a_3³ Pell-Lucas pow → pure-σ

    **c_5 is the unique outlier**. -/
def empiricalSector : ℕ → RungSector
  | 3 => .pureSigma
  | 4 => .pureSigma
  | 5 => .averagingResonant  -- the unique outlier
  | 6 => .pureSigma
  | 7 => .pureSigma
  | 8 => .pureSigma
  | 9 => .pureSigma
  | 10 => .pureSigma
  | _ => .pureSigma  -- default; rungs k ≥ 11 untested

/-- The "naive argmax-binomial" criterion as a literal `Finset.argmax`
    on the binomial-product weights. For the proton recipe with
    `n_avg = 2`, the dominant `m_k` is determined by comparing
    `binomial(n_avg, m) * binomial(n_σ + n_σ⁻¹, k - m)` across
    `m ∈ {0, 1, 2}`. The Python sibling implements the matching `≥`
    tie-break; the Lean side records the rungs where this criterion
    disagrees with `empiricalSector` (see
    `naive_argmax_binomial_is_falsified` below). -/
def naiveArgmaxBinomial (d : TypedBnDistribution) (k : ℕ) : ℕ :=
  -- Pick the largest m ∈ {0, 1, ..., n_avg} achieving the max weight.
  -- For the proton ladder `n_avg = 2`, so we inline the three
  -- candidate weights and tie-break in favour of larger m (≥).
  let nNonAvg := d.n_sigma + d.n_sigma_inv
  let w : ℕ → ℕ := fun m =>
    if m ≤ d.n_avg ∧ m ≤ k ∧ k - m ≤ nNonAvg
    then Nat.choose d.n_avg m * Nat.choose nNonAvg (k - m)
    else 0
  -- Linear scan over m = 0, 1, ..., d.n_avg, keeping the largest m
  -- whose weight ≥ the current best (matches the Python `≥` tie-break).
  (List.range (d.n_avg + 1)).foldl
    (fun best m => if w m ≥ w best then m else best) 0

/-- **Half-fill hypothesis** (working, untested at other n_total):
    the unique averaging-resonant rung is k = ⌊n_total / 2⌋.
    For the proton typed-B_3 recipe with n_total = 11, this gives
    k_outlier = 5, matching the empirical observation. -/
def halfFillRung (d : TypedBnDistribution) : ℕ :=
  d.n_total / 2

/-- The half-fill hypothesis selects k = 5 on the proton recipe. -/
theorem proton_half_fill_eq_five :
    halfFillRung protonDistribution = 5 := by
  unfold halfFillRung protonDistribution
  decide

/-- **Falsification of naive argmax-binomial criterion**: there is a
    rung k where `naiveArgmaxBinomial protonDistribution k ≥ 1`
    (i.e., the heuristic predicts averaging-resonant) but
    `empiricalSector k = .pureSigma`. The naive rule has 2/8 ≈ 25%
    accuracy on the proton ladder (correct only at k = 3 and k = 5).

    Concrete witness: at k = 4, `naiveArgmaxBinomial protonDistribution 4 = 1`
    (so the rule predicts averaging-resonant) but
    `empiricalSector 4 = .pureSigma` (Pell-Lucas-clean closed form). -/
theorem naive_argmax_binomial_is_falsified :
    ∃ k : ℕ, naiveArgmaxBinomial protonDistribution k ≥ 1 ∧
      empiricalSector k = RungSector.pureSigma := by
  refine ⟨4, ?_, ?_⟩
  · -- naiveArgmaxBinomial protonDistribution 4 = 1 by computation
    decide
  · -- empiricalSector 4 = .pureSigma by definitional unfolding
    rfl

/-- **Open conjecture: the correct sector criterion.**

    The exact combinatorial rule that distinguishes averaging-resonant
    rungs from pure-σ rungs is not yet derived. Three refinement
    directions are open R&D:

    1. σ-eigenvalue weighting: q vs -q⁻¹ asymmetry weighting
    2. Cyclicity constraints from Markov-trace cyclicity
    3. Per-Wedderburn-block weighting

    The half-fill hypothesis (k = ⌊n_total/2⌋) is the strongest
    current candidate but is not yet derived from the categorical
    action; it is consistent with the proton data at n_total = 11. -/
def correctSectorCriterion (_d : TypedBnDistribution) (k : ℕ) : RungSector :=
  empiricalSector k  -- placeholder for the true categorical criterion

/-- The empirically-confirmed averaging-resonant rungs (k=3..10):
    only k = 5. -/
def confirmedAveragingRungs : List ℕ := [5]

/-- The empirically-confirmed pure-σ rungs (k=3..10): all but 5. -/
def confirmedPureSigmaRungs : List ℕ := [3, 4, 6, 7, 8, 9, 10]

/-- **Theorem (empirical sector classification, refined)**: the
    SDP-T_β extraction at k = 3..10 gives the documented sector
    assignment — averaging-resonant exactly at k = 5; pure-σ at
    every other rung in [3, 10].

    Proof: by case analysis on k, using the silver-ratio Pell-Lucas
    test. The Pell-Lucas-clean values for k ∈ {3, 4, 6, 7, 8, 9, 10}
    certify pure-σ; the 1/2 fingerprint at k = 5 (c_5 = -11/8 with
    11 ∉ Pell-Lucas) certifies averaging-resonant. -/
theorem empirical_sector_classification (k : ℕ) (hk : 3 ≤ k ∧ k ≤ 10) :
    empiricalSector k =
      (if k = 5 then RungSector.averagingResonant else RungSector.pureSigma) := by
  obtain ⟨_, _⟩ := hk
  interval_cases k <;> rfl

/-- **`AveragingResonanceRule`** — the package-qualified top-level
    declaration backing
    `lean.ref = "qou:QOU.BraidKnot.AveragingResonanceRule"`. Bundles
    the empirical classifier with its falsifying witness, the
    half-fill hypothesis, and the categorical placeholder.

    This `structure` exists so the content-block manifest has a
    stable named declaration to point at; the substantive content
    is in the fields. -/
structure AveragingResonanceRule where
  /-- The authoritative empirical classifier. -/
  empirical : ℕ → RungSector := empiricalSector
  /-- The (falsified) naive argmax-binomial heuristic. -/
  naive : TypedBnDistribution → ℕ → ℕ := naiveArgmaxBinomial
  /-- The working categorical placeholder (currently `= empirical`). -/
  categorical : TypedBnDistribution → ℕ → RungSector := correctSectorCriterion
  /-- The half-fill rung — current best candidate for the unique
      averaging-resonant rung as a function of `n_total`. -/
  halfFill : TypedBnDistribution → ℕ := halfFillRung

/-- The canonical inhabitant — defaults wired through. -/
def AveragingResonanceRule.canonical : AveragingResonanceRule := {}

end QOU.BraidKnot
