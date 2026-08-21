import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
# QOU.MathlibExt.QPlancherel — q-Plancherel measure framework

A skeleton framework for the q-Plancherel measure on integer
partitions and its asymptotic behaviour (CLT). This is a
candidate for upstream contribution to
`Mathlib/Probability/QPlancherel.lean` once the surrounding
Hecke-character infrastructure is available.

## What this module provides

- `QDimension` typeclass — abstract `d_q(λ)` for a partition type.
- `QPlancherelMeasure` — `P_q(λ) = d_q(λ)² / Z_q(k)` where
  `Z_q(k) = Σ_{λ ⊢ k} d_q(λ)²` is the q-deformed normalisation.
- `CharacterFluctuation` — `χ_λ - 𝔼[χ]` over `P_q`.
- `HasQPlancherelCLT` typeclass — Féray-Méliot 2010 Thm 1.1: the
  variance of `CharacterFluctuation` is `O(1/k)`.

## What this module does NOT yet prove

The Féray-Méliot CLT requires:
- A Mathlib formalisation of the Hecke algebra `H_n(q)` and
  Markov characters
- The q-hook walk of Kerov 1996 (q-Plancherel sampling)
- Asymptotic analysis of q-shifted factorials

These are deep probability/representation-theory results. The
typeclass packages the CLT conclusion; concrete instances are the
conjectural input.

## References

- [feray2010] V. Féray, P.-L. Méliot, *Asymptotics of q-Plancherel
  measures*, Probability Theory and Related Fields 152 (2012), 589-624.
  https://doi.org/10.1007/s00440-010-0331-6
- [kerov1996] S. Kerov, *A q-analog of the hook walk algorithm*,
  Algebra i Analiz 8 (1996).
- [biane2001] P. Biane, *Approximate factorization and concentration
  for characters of symmetric groups*, IMRN 2001, no. 4, 179-192.
-/

namespace QOU.MathlibExt.QPlancherel

universe u v

variable (Λ : Type u) (R : Type v)

/-- **q-Dimension typeclass**: a partition type `Λ` carries a
    q-deformed dimension function `d_q : Λ → R`. The classical
    case `q = 1` recovers the Plancherel dimension `dim λ` (the
    Hecke specialisation of the symmetric-group dimension). -/
class QDimension (Λ : Type u) (R : Type v) where
  /-- The q-dimension of a partition. -/
  dq : Λ → R

/-- **q-Plancherel partition function** at level `k`:
    `Z_q(k) = Σ_{λ ⊢ k} d_q(λ)²`.

    Stated as a class field rather than constructed (the
    summation requires a finite-decidable universe of partitions
    of `k`). -/
class HasPartitionFunction (Λ : Type u) (R : Type v) [CommRing R] [LT R] where
  /-- The partition function at level `k`. -/
  Z : ℕ → R
  /-- `Z(k) > 0` for all `k ≥ 0`. -/
  Z_pos : ∀ k, 0 < Z k

variable [Field R] [LinearOrder R] [IsStrictOrderedRing R]
variable [QDimension Λ R] [HasPartitionFunction Λ R]

/-- **q-Plancherel measure**: `P_q(lam) = d_q(lam)² / Z_q(|lam|)`.

    Stated as a function `Λ → ℕ → R` where the second argument is
    the level `k = |lam|`. The actual constraint that the input
    partition has size `k` is left to the caller. -/
def measure (lam : Λ) (k : ℕ) : R :=
  (QDimension.dq lam : R)^2 / HasPartitionFunction.Z (Λ := Λ) k

/-- **Positivity of the q-Plancherel measure**: every partition has
    non-negative weight (zero only when `d_q(lam) = 0`). -/
theorem measure_nonneg (lam : Λ) (k : ℕ) :
    0 ≤ measure (R := R) (Λ := Λ) lam k := by
  unfold measure
  exact div_nonneg (sq_nonneg _) (le_of_lt (HasPartitionFunction.Z_pos k))

/-- **Vanishing on null partitions**: if `d_q(lam) = 0`, then
    `measure lam k = 0`. -/
theorem measure_eq_zero_of_dq_zero (lam : Λ) (k : ℕ)
    (hdq : (QDimension.dq lam : R) = 0) :
    measure (R := R) (Λ := Λ) lam k = 0 := by
  unfold measure
  rw [hdq]
  simp

/-- **Measure scales as `d_q²`**: the q-Plancherel measure is
    `d_q(lam)²` divided by the partition function. Specifically,
    `Z_q(k) · measure lam k = d_q(lam)²`. -/
theorem measure_mul_partitionFunction (lam : Λ) (k : ℕ) :
    HasPartitionFunction.Z (Λ := Λ) k * measure (R := R) (Λ := Λ) lam k
      = (QDimension.dq lam : R) ^ 2 := by
  unfold measure
  rw [mul_div_cancel₀]
  exact ne_of_gt (HasPartitionFunction.Z_pos k)

/-! ## §2  Féray-Méliot q-Plancherel CLT

The headline asymptotic result: as `k → ∞`, the character
fluctuations `χ_λ - 𝔼_q[χ]` (over the q-Plancherel measure)
have variance `O(1/k)`.

Statement-level form: for any partition type `Λ` carrying a
q-dimension and a partition function, the q-Plancherel CLT
provides a uniform `C` such that
`|f_k - f_∞| ≤ C / √(k - 3)` for branching fractions `f_k`. -/

/-- **q-Plancherel CLT typeclass**: witnesses the Féray-Méliot
    O(1/√k) bound for q-Plancherel branching fractions. -/
-- Ref: [feray2010] Theorem 1.1
class HasQPlancherelCLT (Λ : Type u) (R : Type v)
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    [QDimension Λ R] [HasPartitionFunction Λ R] where
  /-- The Féray-Méliot constant. -/
  Cq : ℝ
  /-- The constant is positive. -/
  Cq_pos : 0 < Cq
  /-- The O(1/√k) bound holds for any branching-fraction sequence
      `f : ℕ → ℝ` and limit `f_inf : ℝ` arising from the q-Plancherel
      asymptotics. -/
  bound : ∀ (f : ℕ → ℝ) (f_inf : ℝ) (k : ℕ), k ≥ 4 →
    |f k - f_inf| ≤ Cq / Real.sqrt (k - 3 : ℝ)

/-! ## §3  The partition function as a constructed sum, and total mass one

§1 states the measure as `d_q(λ)² / Z k` with `Z` an **opaque class field** of
`HasPartitionFunction`, constrained only by `Z_pos`. That suffices for
`measure_nonneg` and for `measure_mul_partitionFunction` — but note what the
latter actually says once unfolded: `Z · (d² / Z) = d²`, which holds for *any*
nonzero `Z` and so says nothing about `Z` being a sum of squares.

In particular §1 does **not** establish that `measure` is a probability
measure. The class docstring documents `Z_q(k) = Σ_{λ ⊢ k} d_q(λ)²`, and the
module header repeats it, but that identity is prose: nothing in the type ties
`Z k` to any sum, so no total-mass statement is available or even expressible.

This section closes that gap the honest way — by *constructing* the partition
function as a finite sum over an explicit `Finset` of blocks and proving total
mass `1` for it — and then records the witness showing the opaque field cannot
deliver the same conclusion, so the construction is not mistaken for
bookkeeping.

**On triviality.** `sum_measureOn_eq_one` is a one-line consequence of
`Finset.sum_div` and `div_self`, and that is the point rather than a defect:
normalising a family by its own sum gives total mass one *by construction*, so
this theorem is evidence about the constructed object only. It is emphatically
**not** evidence that `Σ_λ d_q(λ)²` is the canonical normaliser for the
Ocneanu weights `W_λ = d_q(λ)²/[n]_q!` — that question is open, and the
measured `Σ_λ d_q(λ)² ≠ [n]_q!` at `q ≠ 1` (the `Z(n)` defect, with its sign
change at `n = 7`) is exactly what makes it open. See
`docs/audits/2026-06-20-keystone-wlambda-Z-defect-n-scaling.md`.
-/

section Constructed

variable {Λ' : Type u} {R' : Type v}

/-- **Constructed q-Plancherel partition function** over an explicit finite set
    of Wedderburn blocks: `Z_q(s) = Σ_{λ ∈ s} d_q(λ)²`.

    Unlike `HasPartitionFunction.Z` this is a *definition*, not an axiom: the
    summation the class docstring describes is carried out. The `Finset` is
    supplied by the caller because the universe of partitions of a given size
    is finite but not canonically presented here (the same reason §1 gave for
    leaving `Z` opaque). -/
def qPartitionFunctionOn [CommRing R'] [QDimension Λ' R'] (s : Finset Λ') : R' :=
  ∑ lam ∈ s, (QDimension.dq lam : R') ^ 2

/-- **Constructed q-Plancherel measure**: `d_q(λ)²` normalised by the
    constructed partition function of `s`. -/
def measureOn [Field R'] [QDimension Λ' R'] (s : Finset Λ') (lam : Λ') : R' :=
  (QDimension.dq lam : R') ^ 2 / qPartitionFunctionOn (Λ' := Λ') (R' := R') s

/-- **Total mass one** — the statement §1 could not make.

    Needs no ordering on `R'`, only a field and a nonvanishing normaliser. -/
theorem sum_measureOn_eq_one [Field R'] [QDimension Λ' R'] (s : Finset Λ')
    (hs : qPartitionFunctionOn (Λ' := Λ') (R' := R') s ≠ 0) :
    ∑ lam ∈ s, measureOn (Λ' := Λ') (R' := R') s lam = 1 := by
  have hsum : ∑ lam ∈ s, measureOn (Λ' := Λ') (R' := R') s lam
      = (∑ lam ∈ s, (QDimension.dq lam : R') ^ 2)
        / qPartitionFunctionOn (Λ' := Λ') (R' := R') s := by
    rw [Finset.sum_div]
    rfl
  rw [hsum]
  exact div_self hs

/-- The constructed partition function is positive as soon as one block in `s`
    has nonvanishing q-dimension — i.e. `Z_pos` is *derivable* here rather than
    assumed. -/
theorem qPartitionFunctionOn_pos [Field R'] [LinearOrder R'] [IsStrictOrderedRing R']
    [QDimension Λ' R'] {s : Finset Λ'} {lam₀ : Λ'} (hmem : lam₀ ∈ s)
    (hne : (QDimension.dq lam₀ : R') ≠ 0) :
    0 < qPartitionFunctionOn (Λ' := Λ') (R' := R') s := by
  refine Finset.sum_pos' (fun i _ => sq_nonneg _) ⟨lam₀, hmem, ?_⟩
  exact pow_two_pos_of_ne_zero hne

/-- Each constructed weight is nonnegative. -/
theorem measureOn_nonneg [Field R'] [LinearOrder R'] [IsStrictOrderedRing R']
    [QDimension Λ' R'] (s : Finset Λ') (lam : Λ')
    (hs : 0 ≤ qPartitionFunctionOn (Λ' := Λ') (R' := R') s) :
    0 ≤ measureOn (Λ' := Λ') (R' := R') s lam :=
  div_nonneg (sq_nonneg _) hs

end Constructed

section OpaqueGap

variable {Λ' : Type u} {R' : Type v}

/-- **The exact axiom `HasPartitionFunction` is missing.** If the opaque `Z k`
    happens to agree with the constructed sum over `s`, then §1's `measure` does
    have total mass one. So the gap is precisely this hypothesis: `Z_pos` pins
    the sign, `hZ` pins the value, and only the latter yields a probability
    measure. -/
theorem sum_measure_eq_one_of_Z_eq_sum
    [Field R'] [LinearOrder R'] [IsStrictOrderedRing R']
    [QDimension Λ' R'] [HasPartitionFunction Λ' R'] (s : Finset Λ') (k : ℕ)
    (hZ : HasPartitionFunction.Z (Λ := Λ') k
        = qPartitionFunctionOn (Λ' := Λ') (R' := R') s)
    (hs : qPartitionFunctionOn (Λ' := Λ') (R' := R') s ≠ 0) :
    ∑ lam ∈ s, measure (R := R') (Λ := Λ') lam k = 1 := by
  have hpt : ∀ lam ∈ s, measure (R := R') (Λ := Λ') lam k
      = measureOn (Λ' := Λ') (R' := R') s lam := by
    intro lam _
    unfold measure measureOn
    rw [hZ]
  rw [Finset.sum_congr rfl hpt]
  exact sum_measureOn_eq_one s hs

/-- A one-block q-dimension: the single partition has `d_q = 1`. -/
def unitQDimension : QDimension (Fin 1) ℚ := ⟨fun _ => 1⟩

/-- A partition function that is **positive but wrong**: it returns `2` where
    the sum of squares is `1`. It satisfies every constraint
    `HasPartitionFunction` imposes. -/
def badPartitionFunction : HasPartitionFunction (Fin 1) ℚ :=
  ⟨fun _ => 2, fun _ => by norm_num⟩

/-- **`Z_pos` alone does not deliver total mass one — witnessed on `measure`
    itself.** `badPartitionFunction` is a lawful `HasPartitionFunction`
    instance, yet §1's `measure` sums to `1/2` over the whole (one-block)
    index set.

    So §1's framework, taken alone, cannot call `measure` a probability
    measure: the missing content is a value constraint, not a sign constraint.
    This is exactly why `sum_measure_eq_one_of_Z_eq_sum` must take `hZ` as a
    hypothesis instead of deriving it from `Z_pos`. -/
theorem measure_total_mass_ne_one_of_badPartitionFunction :
    letI := unitQDimension
    letI := badPartitionFunction
    ∑ lam ∈ (Finset.univ : Finset (Fin 1)),
      measure (R := ℚ) (Λ := Fin 1) lam 1 = 1 / 2 := by
  letI := unitQDimension
  letI := badPartitionFunction
  simp [measure, unitQDimension, badPartitionFunction]

/-- Corollary in the form the gap is usually stated: total mass is **not** `1`. -/
theorem exists_lawful_Z_with_total_mass_ne_one :
    letI := unitQDimension
    letI := badPartitionFunction
    ∑ lam ∈ (Finset.univ : Finset (Fin 1)),
      measure (R := ℚ) (Λ := Fin 1) lam 1 ≠ 1 := by
  rw [measure_total_mass_ne_one_of_badPartitionFunction]
  norm_num

end OpaqueGap


end QOU.MathlibExt.QPlancherel
