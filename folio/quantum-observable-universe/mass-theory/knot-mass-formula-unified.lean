import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Unified knot mass formula

The categorical mass of a vortex ρ with braid T_w ∈ H_n(q) is
(`knot-mass-formula-unified.md`):

  m(ρ) = |tr_M(T_w)|
         − [ Σ_{i=0}^{n−2} Li₂^q(−|V̂_i|) + z² Σ_{0≤i<j≤n−2} Li₂^q(−|V̂_i V̂_j|) ]
         + m_e · tr_M(C_{dim_q}^{H_n(q)}),      tr_M(C_{dim_q}) = Σ_{λ⊢n} 1/dim_q(λ)

  1. Descended:  |tr_M(T_w)|                  — prop:categorical-mass-markov
  2. Brane tower (subtracted): the two Li₂^q sums — prop:mass-endomorphism-tower
  3. Frobenius co-Casimir: m_e · Σ_λ 1/dim_q(λ) — thm:frobenius-codim-universal

## What changed on 2026-09-03 (bean `qou-08zf`; audit
`docs/audits/2026-08-27-unified-knot-mass-class-is-unsatisfiable.md`)

* The class fields `descended = |descendedMarkov q braid|` and
  `tower = braneTower q braid` pointed at stubs that were **identically
  zero**, so every instance had two of its three terms forced to `0`, and
  `trivial_vortex_vacuum_mass` (which assumes `descended = 1`) had
  contradictory hypotheses.  The stubs are gone; the class now carries the
  Markov-trace value, the resolved-defect magnitudes `|V̂_i|`, the coupling
  `z` and the symmetric `q`-dilogarithm as **data**, and the tower field
  states the `.md`'s sum.
* The sign of the brane tower matched the `.md` (subtracted), not the
  previous Lean (added) — a `proof-statement-integrity` defect, fixed.
* `electronMass : ℝ := 0.510998` (a CODATA literal inside a class field)
  is replaced by the scale parameter `mE` — the mass is an `m_e`-scaled
  realisation of the dimensionless ratio (AGENTS.md, absolute mass excised),
  and formal statements carry no empirical input.
* `frobeniusCoCasimirTrace` was a `match` whose arms held typed-in values
  read back by `rfl` ("an axiom relocated, not discharged").  It is now the
  **partition sum** `Σ_λ 1/dim_q(λ)` over the explicit `q`-hook dimensions
  (`qHookDims`, labelled by partition), and the closed forms are *proved*
  by evaluating that sum.  For `n ≥ 6` the corpus has no formalised closed
  form; the class carries the trace as data constrained to the proved sum
  only for `n ≤ 5` — an honest open field, not a fabricated value
  (previously `(n : ℝ)` under a docstring that said `0`).
* The self-certifying `s3_bridge_audit_status : String` is removed.

Tower status (owner ruling 2026-09-03): MIXED — the Frobenius piece is a
genuine sum over the full partition lattice at fixed `n ≤ 5`; the tower over
`n` is not taken.

Ref: [leitner2026] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `thm:knot-mass-formula-unified`
-/

namespace QOU.BraidKnot

/-- **The `q`-hook dimensions `dim_q(λ)`, `λ ⊢ n`, for `n ∈ {2,3,4,5}`**, as
    a list in the order of `frobenius-codim-universal.lean`'s
    `heckeH{n}DimQ` (partitions in reverse-lexicographic order; conjugate
    partitions share a dimension).  These are the *inputs* of the partition
    sum, computed there from the `q`-hook-length formula:

      n = 2: (2), (1,1)                                  → 1, 1
      n = 3: (3), (2,1), (1³)                            → 1, [2]_q, 1
      n = 4: (4), (3,1), (2,2), (2,1,1), (1⁴)            → 1, [3]_q, [4]_q/[2]_q, [3]_q, 1
      n = 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1³), (1⁵)
                                                         → 1, [4]_q, [5]_q, [4]_q[3]_q/[2]_q, [5]_q, [4]_q, 1

    with `[4]_q/[2]_q = q² + q⁻²` and `[4]_q[3]_q/[2]_q = (q²+q⁻²)·[3]_q`.
    Empty for every other `n`: the corpus has no formalised list there. -/
noncomputable def qHookDims (q : ℝ) : ℕ → List ℝ
  | 2 => [1, 1]
  | 3 => [1, q + q⁻¹, 1]
  | 4 => [1, q ^ 2 + 1 + (q ^ 2)⁻¹, q ^ 2 + (q ^ 2)⁻¹, q ^ 2 + 1 + (q ^ 2)⁻¹, 1]
  | 5 => [1, q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹,
          q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹,
          (q ^ 2 + (q ^ 2)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹),
          q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹,
          q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹, 1]
  | _ => []

/-- **The Frobenius co-Casimir trace `τ(C_{dim_q}) = Σ_{λ⊢n} 1/dim_q(λ)`** on
    `H_n(q)`, as the partition sum over `qHookDims` — meaningful for
    `n ∈ {2,3,4,5}` (every consumer below guards on `n ≤ 5`). -/
noncomputable def partitionInverseDimSum (q : ℝ) (n : ℕ) : ℝ :=
  ((qHookDims q n).map fun d => 1 / d).sum

/-- `n = 2`: both partitions have `dim_q = 1`, so the sum is `2`. -/
theorem partitionInverseDimSum_two (q : ℝ) : partitionInverseDimSum q 2 = 2 := by
  simp [partitionInverseDimSum, qHookDims]
  norm_num

/-- `n = 3`: `Σ_{λ⊢3} 1/dim_q(λ) = 2 + 1/[2]_q = 2 + 1/(q + q⁻¹)`. -/
theorem partitionInverseDimSum_three (q : ℝ) :
    partitionInverseDimSum q 3 = 2 + 1 / (q + q⁻¹) := by
  simp [partitionInverseDimSum, qHookDims]
  ring

/-- `n = 4`: `2 + 2/[3]_q + 1/(q² + q⁻²)`. -/
theorem partitionInverseDimSum_four (q : ℝ) :
    partitionInverseDimSum q 4
      = 2 + 2 / (q ^ 2 + 1 + (q ^ 2)⁻¹) + 1 / (q ^ 2 + (q ^ 2)⁻¹) := by
  simp [partitionInverseDimSum, qHookDims]
  ring

/-- `n = 5`: `2 + 2/[4]_q + 2/[5]_q + 1/((q²+q⁻²)·[3]_q)`. -/
theorem partitionInverseDimSum_five (q : ℝ) :
    partitionInverseDimSum q 5
      = 2 + 2 / (q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹)
          + 2 / (q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹)
          + 1 / ((q ^ 2 + (q ^ 2)⁻¹) * (q ^ 2 + 1 + (q ^ 2)⁻¹)) := by
  simp [partitionInverseDimSum, qHookDims]
  ring

/-- **The unified knot mass, as data plus the identities the `.md` states.**

    A `UnifiedKnotMass` packages, for one vortex with braid `T_w ∈ H_n(q)`:
    the substrate `q`, the strand count `n`, the unit scale `mE` (`m_e`,
    CAL-1 — a parameter, never a literal), the Markov-trace value
    `markovTrace = tr_M(T_w)`, the Frobenius co-Casimir trace
    `coCasimirTrace = tr_M(C_{dim_q})`, the brane-tower data (`vhat i =
    |V̂_i^{full}|` for `i = 0, …, n−2`, the coupling `z`, and the symmetric
    `q`-dilogarithm `li2q` — archimedean, hence a parameter), and the three
    terms with the identities relating them:

      total_mass = descended − tower + frobenius_correction
      descended  = |tr_M(T_w)|
      tower      = Σ_i Li₂^q(−|V̂_i|) + z² Σ_{i<j} Li₂^q(−|V̂_i V̂_j|)
      frobenius_correction = m_e · tr_M(C_{dim_q})
      tr_M(C_{dim_q}) = Σ_{λ⊢n} 1/dim_q(λ)   whenever n ≤ 5 (proved sums)

    For `n ≥ 6` the co-Casimir trace is genuinely open in Lean (no
    formalised partition sum); the field `coCasimir_small_n` constrains it
    only where the corpus has proved it, instead of pinning a fabricated
    value.  Nothing here forces any term to `0`.

    Ref: [leitner2026] §Nuclear Binding and Beta Stability,
    prop:mass-endomorphism-tower, thm:frobenius-codim-universal. -/
structure UnifiedKnotMass where
  /-- Substrate parameter. -/
  q : ℝ
  /-- Strand count of the braid `T_w ∈ H_n(q)`. -/
  n : ℕ
  /-- The unit scale `m_e` (CAL-1). -/
  mE : ℝ
  /-- The Markov trace `tr_M(T_w)` of the braid. -/
  markovTrace : ℝ
  /-- The Frobenius co-Casimir trace `tr_M(C_{dim_q})` on `H_n(q)`. -/
  coCasimirTrace : ℝ
  /-- Resolved-defect magnitudes `|V̂_i^{full}|`, `i = 0, …, n−2`. -/
  vhat : Fin (n - 1) → ℝ
  /-- The tower coupling `z`. -/
  z : ℝ
  /-- The symmetric `q`-dilogarithm `Li₂^q` (archimedean; a parameter). -/
  li2q : ℝ → ℝ
  /-- Descended term. -/
  descended : ℝ
  /-- Brane-tower term (subtracted). -/
  tower : ℝ
  /-- Frobenius co-Casimir correction. -/
  frobenius_correction : ℝ
  /-- The total categorical mass. -/
  total_mass : ℝ
  /-- `m(ρ) = descended − tower + frobenius`. -/
  unified_identity : total_mass = descended - tower + frobenius_correction
  /-- `descended = |tr_M(T_w)|`. -/
  descended_is_markov : descended = |markovTrace|
  /-- `tower = Σ_i Li₂^q(−|V̂_i|) + z² Σ_{i<j} Li₂^q(−|V̂_i V̂_j|)`. -/
  tower_is_li2q_sum :
    tower = (∑ i, li2q (-(vhat i)))
      + z ^ 2 * ∑ i, ∑ j, if i < j then li2q (-(vhat i * vhat j)) else 0
  /-- `frobenius_correction = m_e · tr_M(C_{dim_q})`. -/
  frobenius_is_codim_trace : frobenius_correction = mE * coCasimirTrace
  /-- For `n ≤ 5` the co-Casimir trace is the proved partition sum. -/
  coCasimir_small_n : n ≤ 5 → coCasimirTrace = partitionInverseDimSum q n

/-- **Unified knot mass formula (`n ≤ 5`).**  For every `UnifiedKnotMass`
    with at most five strands,

      m(ρ) = |tr_M(T_w)| − tower + m_e · Σ_{λ⊢n} 1/dim_q(λ),

    derived by composing the four identities the structure carries. -/
-- Ref: [leitner2026] thm:knot-mass-formula-unified
theorem knot_mass_unified_small (U : UnifiedKnotMass) (hn : U.n ≤ 5) :
    U.total_mass = |U.markovTrace| - U.tower + U.mE * partitionInverseDimSum U.q U.n := by
  rw [U.unified_identity, U.descended_is_markov, U.frobenius_is_codim_trace,
    U.coCasimir_small_n hn]

/-- **Unified knot mass formula at `n = 3`** (single nucleon, trefoil):

      m(ρ) = |tr_M(T_w)| − tower + m_e · (2 + 1/[2]_q),   [2]_q = q + q⁻¹.

    This is the `.md`'s boxed formula with the Frobenius piece evaluated;
    `lean.ref` target of `thm:knot-mass-formula-unified`. -/
-- Ref: [leitner2026] thm:knot-mass-formula-unified, conj:partition-sum-proton-residual
theorem knot_mass_unified (U : UnifiedKnotMass) (hn : U.n = 3) :
    U.total_mass = |U.markovTrace| - U.tower + U.mE * (2 + 1 / (U.q + U.q⁻¹)) := by
  rw [knot_mass_unified_small U (by omega), hn, partitionInverseDimSum_three]

/-- Specialisation to `n = 2`: the Frobenius piece is exactly `2 m_e` (both
    partitions have `dim_q = 1`, saturating the self-dual lower bound). -/
-- Ref: [leitner2026] conj:partition-sum-proton-residual
theorem two_strand_frobenius_correction (U : UnifiedKnotMass) (hn : U.n = 2) :
    U.frobenius_correction = U.mE * 2 := by
  rw [U.frobenius_is_codim_trace, U.coCasimir_small_n (by omega), hn,
    partitionInverseDimSum_two]

/-- Specialisation to `n = 4` (e.g. the four-strand Borromean closure):
    the Frobenius piece is `m_e · (2 + 2/[3]_q + 1/(q²+q⁻²))`. -/
-- Ref: [leitner2026] conj:partition-sum-proton-residual
theorem four_strand_frobenius_correction (U : UnifiedKnotMass) (hn : U.n = 4) :
    U.frobenius_correction
      = U.mE * (2 + 2 / (U.q ^ 2 + 1 + (U.q ^ 2)⁻¹) + 1 / (U.q ^ 2 + (U.q ^ 2)⁻¹)) := by
  rw [U.frobenius_is_codim_trace, U.coCasimir_small_n (by omega), hn,
    partitionInverseDimSum_four]

/-- **Trivial-vortex (identity braid) mass = Frobenius vacuum.**

    Hypotheses: the Markov trace of the braid is `1` (the trace of the
    identity element of `H_n(q)`) and the brane tower at the identity
    contributes `0`.  Then the total mass is `1 + m_e · tr_M(C_{dim_q})` —
    the "vacuum mass" of the unit object.  The hypotheses are now
    **satisfiable**: nothing in the structure forces the Markov trace to
    vanish (previously the class pinned it to `0`, so this theorem's
    antecedent was `False`). -/
theorem trivial_vortex_vacuum_mass (U : UnifiedKnotMass)
    (h_desc : U.markovTrace = 1) (h_tower : U.tower = 0) :
    U.total_mass = 1 + U.mE * U.coCasimirTrace := by
  rw [U.unified_identity, U.descended_is_markov, h_desc, h_tower,
    U.frobenius_is_codim_trace]
  simp

end QOU.BraidKnot
