import QOU.FeynmanPathIntegrals.markov_identification
import QOU.SchurWeyl.MarkovTraceInstance
import Mathlib.Algebra.BigOperators.Fin
import QOU.SchurWeyl.OcneanuWeight

/-!
# QOU.FeynmanPathIntegrals.MarkovIdentificationInstance — the branching identity, derived

`markov_identification.lean` carries the Wenzl-bridge / branching decomposition

  `tr_M = ∑_λ w_λ · tr_{S_λ}`

as the named proposition `markovTrace_branching nPart w trS trM` — *"named, not asserted"* — and
its module docstring lists the identity itself as **Open**: nothing there constructs the Hecke
algebra, the Specht modules, or the quantum dimensions in `w_λ`; they are reals the caller
supplies, and `markov_identification` derives clause (ii) from the identity as a hypothesis.

At convention D — `z_D = q³/(q²+1)`, the canonical Markov parameter per the 2026-08-15 owner
ruling — the hypothesis is a theorem of this repo. `QOU.SchurWeyl.MarkovTraceInstance` proves,
for every `n`, that **every** Markov trace on the Hecke tower equals the Ocneanu-weighted
seminormal trace (`eq_wtrace_of_markov`), and `wtrace_apply` unfolds that trace to exactly the
weighted sum of per-block traces. That *is* the branching decomposition, so this file supplies
the hypothesis from it:

* `diagIndex n` enumerates the Young diagrams of size `n + 1` by a natural index
  (`Fintype.equivFin`), because the proposition indexes blocks by `ℕ` and sums over
  `Finset.range`;
* `indexed n f` transports a function on diagrams to `ℕ → ℝ` (zero off-range), and
  `sum_indexed` shows the range sum is the Fintype sum;
* `markovTrace_branching_of_markovTrace T x` **proves** `markovTrace_branching` at the data
  (number of blocks, Ocneanu weights, seminormal block traces of `x`, `T.tr n x`) for any Markov
  trace `T` at `z_D` and any Hecke element `x`;
* `markov_identification_of_markovTrace` is `lem:feynman-markov-identification` at that data —
  the eigenbasis amplitude equals `T.tr n x` — with no assumption beyond the hypotheses of
  `MarkovTraceInstance` (`q ≠ 0`, `q` not a root of unity, `q² + 1 ≠ 0`, `q²` not a root of
  unity).

## What this does and does not claim

* It closes the *decomposition* gap at the data the lemma is about: the weights are the Ocneanu
  weights and the partial traces are the seminormal-representation traces, both concrete, and
  the identity is a theorem. `not_markovTrace_branching_of_free_data` in the base file is
  unaffected — the identity is false at *free* data and true at *this* data; the two are
  different claims.
* It is convention D only. For an arbitrary Markov parameter `z` the per-corner identity is still
  open (`MarkovConventionD` module docstring); nothing here bears on that.

## Base ring (§7c)

`ℝ`, forced by `seminormalRep` and by the base file (whose data are `ℝ`-valued). Nothing here is
archimedean beyond that inheritance.
-/

namespace QOU.FeynmanPathIntegrals

open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep

/-- The Young diagrams of size `n + 1` — the Wedderburn blocks of `H_{n+1}(q)`. -/
abbrev Diag (n : ℕ) := {ν : YoungDiagram // ν.cells.card = n + 1}

/-- An enumeration of the blocks by a natural index. -/
noncomputable def diagIndex (n : ℕ) : Diag n ≃ Fin (Fintype.card (Diag n)) :=
  Fintype.equivFin _

/-- Transport a function on blocks to a function on `ℕ`, zero off-range. -/
noncomputable def indexed (n : ℕ) (f : Diag n → ℝ) (l : ℕ) : ℝ :=
  if h : l < Fintype.card (Diag n) then f ((diagIndex n).symm ⟨l, h⟩) else 0

theorem indexed_of_lt (n : ℕ) (f : Diag n → ℝ) (i : Fin (Fintype.card (Diag n))) :
    indexed n f i = f ((diagIndex n).symm i) := by
  unfold indexed
  rw [dif_pos i.isLt]

/-- The range sum of the transported function is the Fintype sum over blocks. -/
theorem sum_indexed (n : ℕ) (f : Diag n → ℝ) :
    ∑ l ∈ Finset.range (Fintype.card (Diag n)), indexed n f l = ∑ ν, f ν := by
  rw [← Fin.sum_univ_eq_sum_range, ← Equiv.sum_comp (diagIndex n).symm f]
  exact Finset.sum_congr rfl fun i _ => indexed_of_lt n f i

/-- Transport respects pointwise products. -/
theorem indexed_mul (n : ℕ) (f g : Diag n → ℝ) (l : ℕ) :
    indexed n f l * indexed n g l = indexed n (fun ν => f ν * g ν) l := by
  unfold indexed
  split_ifs <;> simp

variable (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- **The branching decomposition, as a theorem.** Every Markov trace at `z_D` is the
Ocneanu-weighted sum of the seminormal per-block traces. -/
theorem markovTrace_eq_weighted_sum (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (x : Hecke ℝ q q⁻¹ n) :
    T.tr n x = ∑ ν : Diag n,
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace := by
  rw [eq_wtrace_of_markov q hq0 hq2 hq21 hgen T n x, wtrace_apply]

/-- **The branching identity, proved at the Markov-trace data.** For any Markov trace `T` at `z_D`
and any `x ∈ H_{n+1}(q)`: with the blocks indexed by `diagIndex`, the weights the Ocneanu weights,
the partial traces the seminormal block traces of `x`, and the Markov trace `T.tr n x`,
`markovTrace_branching` holds — it is derived, not supplied. -/
theorem markovTrace_branching_of_markovTrace (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (x : Hecke ℝ q q⁻¹ n) :
    markovTrace_branching (Fintype.card (Diag n))
      (indexed n fun ν => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1)
      (indexed n fun ν => (seminormalRep q hq0 hq2 n ν.2 x).trace)
      (T.tr n x) := by
  unfold markovTrace_branching
  rw [markovTrace_eq_weighted_sum q hq0 hq2 n hq21 hgen T x, ← sum_indexed]
  exact Finset.sum_congr rfl fun l _ => (indexed_mul n _ _ l).symm

/-- `lem:feynman-markov-identification`, unconditionally at convention D: the Markov-weighted
eigenbasis amplitude built from the Ocneanu weights and the seminormal block traces equals the
Markov trace of `x`. -/
theorem markov_identification_of_markovTrace (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (x : Hecke ℝ q q⁻¹ n) :
    amplitudeEigenbasis (Fintype.card (Diag n))
        (indexed n fun ν => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1)
        (indexed n fun ν => (seminormalRep q hq0 hq2 n ν.2 x).trace)
      = T.tr n x :=
  markov_identification (markovTrace_branching_of_markovTrace q hq0 hq2 n hq21 hgen T x)

/-- **Only diagrams with at most two rows contribute.** At `z_D` the Ocneanu weight of a diagram
with a nonempty third row is zero (`ocneanuWeight_conventionD_eq_zero_of_three_rows`), so the
Markov trace is the weighted sum over the diagrams with `rowLen 2 = 0` alone. -/
theorem markovTrace_eq_two_row_sum (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (x : Hecke ℝ q q⁻¹ n) :
    T.tr n x = ∑ ν ∈ Finset.univ.filter (fun ν : Diag n => ν.1.rowLen 2 = 0),
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq0 hq2 n ν.2 x).trace := by
  rw [markovTrace_eq_weighted_sum q hq0 hq2 n hq21 hgen T x, Finset.sum_filter]
  refine Finset.sum_congr rfl fun ν _ => ?_
  split_ifs with h
  · rfl
  · rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 ν.1 (Nat.pos_of_ne_zero h),
      zero_mul]

/-- `prop:feynman-categorical-trace` at convention D: the absolute value of the eigenbasis
amplitude equals the absolute value of the Markov trace, `|amplitude| = |tr_M(x)|`. -/
theorem abs_amplitude_eq_abs_markovTrace (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)
    (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (x : Hecke ℝ q q⁻¹ n) :
    |amplitudeEigenbasis (Fintype.card (Diag n))
        (indexed n fun ν => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1)
        (indexed n fun ν => (seminormalRep q hq0 hq2 n ν.2 x).trace)|
      = |T.tr n x| := by
  rw [markov_identification_of_markovTrace q hq0 hq2 n hq21 hgen T x]

end QOU.FeynmanPathIntegrals
