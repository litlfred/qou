/-!
# QOU.WedderburnMass.ShellCorrectionTermSeven

Conjectural axiomatisation of the **seventh-term shell correction** to
the unified knot-mass formula.  The unified six-term formula
(`thm:knot-mass-formula-unified`) under-predicts isotope masses for
`A ≥ 5` by ~10%; the diagnostic at `rem:higher-a-shell-diagnostic`
identifies a structured residual whose best single-feature predictor
is the GB-filtration level `ℓ = 5` (height-6 partitions).  The
companion narrative is `shell-correction-term-seven.md`.

**Conjectural-class convention** (AGENTS.md §3b).  The conjecture
itself is encoded as a `class` whose fields capture its content:

  * a height parameter `h_star` selecting the GB-filtration channel,
  * a shadow-price coefficient assignment `shadow_price`,
  * a scaling function `scaling : (Z N A : ℕ) → ℝ`,
  * a closed-form Term-7 functional,
  * a sub-percent-accuracy bound at `A ≥ 5`.

`sorry` in any *instance* of this class is understood as
**conjecture**, not missing proof.  Downstream conditional results
take `[ShellCorrectionTermSeven]` as a hypothesis and are fully
verified.

LaTeX label: `conj:shell-correction-term-seven`

## References

- Ref: [manuscript] §Shell correction term seven
- Ref: [mayer1949] https://doi.org/10.1103/PhysRev.75.1969
- Ref: [mayer1955] https://doi.org/10.1063/1.3061984
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic

namespace QOU.WedderburnMass

/-- A height-`h` partition of `n` represented as a list of part-sizes
    of length `h` summing to `n`.  No sortedness constraint is
    imposed at the conjecture-statement level — concrete partition
    combinatorics enter only through `shadow_price` and `scaling`. -/
structure HeightPartition (n h : ℕ) where
  parts : List ℕ
  parts_sum : parts.sum = n
  height_eq : parts.length = h

/-- Atomic-braid Wedderburn datum: the inputs Term 7 needs at each
    nucleus `(Z, N, A)`.  `partitions` enumerates the height-`h`
    partitions of `3A` carrying non-negative q-deformed Wedderburn
    weight tilde w_λ = dim_q²/[n]_q!; `m_codata` is the
    experimentally measured mass; `m_other` is the sum of the other
    six terms of the unified mass formula evaluated on the same
    nucleus. -/
structure AtomicWedderburnDatum (h : ℕ) where
  Z : ℕ
  N : ℕ
  A : ℕ
  mass_number : Z + N = A
  partitions : List (HeightPartition (3 * A) h)
  m_codata : ℝ
  m_other : ℝ

/-- **Conjecture class.**  An instance asserts the existence of a
    height parameter `h_star`, a shadow-price coefficient
    `shadow_price λ q`, a scaling function `scaling Z N A`, a
    Term-7 functional matching the Plancherel decomposition, and a
    sub-percent accuracy bound at `A ≥ 5`.

    Two fields are `Prop`-valued: `term_seven_decomposition` (an
    equality fixing the closed-form expansion of `term_seven_value`)
    and `sub_percent_accuracy` (the conjectural accuracy bound).  The
    decomposition is provable in concrete instances by `rfl` once
    `term_seven_value` is given by the fold expression; the accuracy
    bound is the conjecture proper, and may be discharged by `sorry`. -/
class ShellCorrectionTermSeven where
  /-- Height of the GB-filtration channel.  Empirically `h_star = 6`
      (level-5 GB-filtration; height-6 partitions). -/
  h_star : ℕ
  /-- Shadow-price coefficient `C_λ(q) = w_λ(q) · τ_λ(σ_g)` for a
      height-`h_star` partition of `n`. -/
  shadow_price : ∀ {n : ℕ}, HeightPartition n h_star → ℝ → ℝ
  /-- Scaling function determined by the content sum
      `c(λ) = Σ_{(i,j) ∈ λ} (j − i)`. -/
  scaling : ℕ → ℕ → ℕ → ℝ
  /-- Closed-form Term-7 contribution, given Wedderburn data, the
      substrate parameter `q`, and the electron mass `m_e`. -/
  term_seven_value :
    AtomicWedderburnDatum h_star → ℝ → ℝ → ℝ
  /-- Decomposition: Term 7 is `m_e` times the sum over height-`h_star`
      partitions of `shadow_price λ q · scaling Z N A`. -/
  term_seven_decomposition :
    ∀ (D : AtomicWedderburnDatum h_star) (q m_e : ℝ),
      term_seven_value D q m_e
        = m_e *
          (D.partitions.foldl
            (fun acc λ =>
              acc + shadow_price λ q * scaling D.Z D.N D.A) 0)
  /-- **Conjectural accuracy bound.**  For every nucleus with
      `A ≥ 5`, the extended formula matches the experimental mass to
      sub-percent precision.  The datum `D` carries the target
      `D.m_codata` and the sum of other terms `D.m_other`; existence
      of a uniform `δ` with `|δ| ≤ 1%` is the conjecture. -/
  sub_percent_accuracy :
    ∀ (D : AtomicWedderburnDatum h_star) (q m_e : ℝ),
      5 ≤ D.A →
      ∃ δ : ℝ, |δ| ≤ (1 : ℝ) / 100 ∧
        D.m_codata = (1 + δ) * (term_seven_value D q m_e + D.m_other)

/-- **Downstream conditional theorem (A = 2 single-partition reduction).**

    Conditional on `[ShellCorrectionTermSeven]`, Term 7 at any nucleus
    is the q-deformed Wedderburn-weighted sum specified by
    `term_seven_decomposition`.  At `A = 2` and `h_star = 6` the only
    height-6 partition of `6 = 3·2` is `(3,2,1)`, so the sum collapses
    to a single shadow-price contribution — but that combinatorial
    fact is encoded by the caller via `D.partitions = [(3,2,1)]` and
    *not* re-proved here.  This statement is fully verified once an
    instance is fixed. -/
theorem term_seven_decomposition_apply
    [inst : ShellCorrectionTermSeven]
    (D : AtomicWedderburnDatum inst.h_star)
    (q m_e : ℝ) :
    inst.term_seven_value D q m_e
      = m_e *
        (D.partitions.foldl
          (fun acc λ =>
            acc + inst.shadow_price λ q * inst.scaling D.Z D.N D.A) 0) :=
  inst.term_seven_decomposition D q m_e

/-- **Downstream conditional theorem (sub-percent at `A ≥ 5`).**

    Conditional on `[ShellCorrectionTermSeven]`, the extended formula
    matches CODATA to within 1% for every nucleus with `A ≥ 5`. -/
theorem term_seven_sub_percent
    [inst : ShellCorrectionTermSeven]
    (D : AtomicWedderburnDatum inst.h_star)
    (hA : 5 ≤ D.A) (q m_e : ℝ) :
    ∃ δ : ℝ, |δ| ≤ (1 : ℝ) / 100 ∧
      D.m_codata = (1 + δ) *
        (inst.term_seven_value D q m_e + D.m_other) :=
  inst.sub_percent_accuracy D q m_e hA

end QOU.WedderburnMass
