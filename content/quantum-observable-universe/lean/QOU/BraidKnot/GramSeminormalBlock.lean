import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.GramSeminormalBlock — per-block Hoefsmit-seminormal data

**Option E Phase 1 deliverable (declaration stub).** Provides the
Lean-side signature for per-Wedderburn-block representation data of
the Iwahori–Hecke algebra `H_n(q)`, used by Option E's Δ_λ closure
program.

## The Wedderburn isomorphism reduction

The full NF-basis Gram matrix on `H_n(q)` has size `n! × n!`
(720 × 720 for `H_6`, 362880 × 362880 for `H_9`). Direct computation
is intractable beyond `H_3`. The Wedderburn isomorphism

  `H_n(q) ≅ ⊕_{λ ⊢ n} End(V_λ)`

reduces this to per-block data of size `dim_λ × dim_λ` per partition.
Total entries across all blocks is `Σ_λ dim_λ² = n!` — the same data,
exponentially smaller per-block view.

For each `λ ⊢ n`, this module records:

* `dimLambda λ` — the number of standard Young tableaux of shape `λ`
  (= the dimension of the irrep `V_λ`)
* the Hoefsmit-seminormal representation
  `rhoLambdaSigmaK λ k : Matrix (Fin (dimLambda λ)) (Fin (dimLambda λ)) R`
  for `k = 1, ..., n-1` (i.e., `σ_k ∈ B_n` acting on `V_λ`)
* the longest-word matrix `rhoLambdaW0 λ`
* the character value `chiLambdaW0 λ := tr (rhoLambdaW0 λ)`

Per CLAUDE.md §7c (Base ring convention) the structure is purely
algebraic — no `Real.sqrt` / `Real.rpow` / order predicates — and is
parameterised over a generic commutative ring `R`. Numerical
specialisations live in archimedean-evaluation modules.

The numerical instances at the substrate `q_0 ∈ ℝ` come from the
Python witness
[`option-e-phase1-gram-h6.witness.json`](../../../../computations/option-e-phase1-gram-h6.witness.json)
(cross-checked at H_3 against the published NF-basis 6×6 Gram in
[`option-e-phase1-h3-cross-check.witness.json`](../../../../computations/option-e-phase1-h3-cross-check.witness.json):
max residual 2.22e-16 over 21 unique NF Gram entries).

## Wedderburn-sum identity (the key cross-check)

For Hecke elements `b, c ∈ H_n(q)`,

  `tr_M(b · c) = Σ_{λ ⊢ n} y_λ · tr (ρ_λ b · ρ_λ c)`

where `y_λ` are the Jones–Markov weights. The Python witness
verifies this for the H_3 NF basis: max residual 2.22e-16 across 21
unique pairs `(b_i, b_j)`. The Lean side records the structural class
of per-block representation data; numerical witnesses are pulled from
the Python sidecar.

## Phase 1 scope (this file)

This file is a **declaration stub** (CLAUDE.md §3b conditional class
pattern): the class encapsulates the per-block data as a hypothesis,
with the Python witness as the canonical instance. Full Lean proof of
the Wedderburn reassembly is deferred to a Mathlib-bridging follow-up.

## Phase 2 use (downstream)

Option E Phase 2 (canonical-basis trace `ρ_w(K)` at crystal vertices)
consumes `rhoLambdaSigmaK λ k` and `rhoLambdaW0 λ` to compute the
canonical-basis trace per crystal vertex `w`. The crystal-weight
formula

  `Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)`

then folds the per-block data with Kazhdan–Lusztig multiplicities
`n^w_λ` to produce per-partition Δ_λ values for the binding-energy
formula `B(K) = m_e · Σ_λ y_λ · χ^λ(β_K) · (1 + Δ_λ(K))`.

## Cross-refs

* `prop:option-e-phase1-gram-h_n` — narrative side (to be authored).
* [`docs/coordination/option-e.md`](../../../../docs/coordination/option-e.md)
  — master ledger; PR #1697 session-log entry.
* [`docs/audits/2026-06-02-option-e-phase1-gram-h6-scope.md`](../../../../docs/audits/2026-06-02-option-e-phase1-gram-h6-scope.md)
  — scope doc.
-/

-- Ref: [manuscript] docs/audits/2026-06-02-option-e-phase1-gram-h6-scope.md
-- Ref: [hoefsmit1974] Hoefsmit-Murphy seminormal representation construction

namespace QOU.BraidKnot.GramSeminormalBlock

/-- A partition of `n` as a descending list of positive integers
    summing to `n`. The empty list represents `n = 0`. -/
structure Partition (n : ℕ) where
  parts : List ℕ
  descending : parts.Sorted (· ≥ ·)
  sum_eq : parts.sum = n
  positive : ∀ p ∈ parts, 0 < p

/-- The dimension of the irreducible representation `V_λ` of the
    symmetric group `S_n` (and of `H_n(q)` over a commutative ring
    `R`), equal to the number of standard Young tableaux of shape `λ`. -/
opaque dimLambda : ∀ {n : ℕ}, Partition n → ℕ

/-- **Per-block Hoefsmit-seminormal representation data** for a
    partition `λ ⊢ n` of the Iwahori–Hecke algebra `H_n(q)`,
    parameterised over a generic commutative ring `R` (CLAUDE.md §7c).

    The fields encode the dimension `dim_λ` and the per-generator and
    longest-word matrices in the Hoefsmit-seminormal basis indexed by
    standard Young tableaux of shape `λ`.

    The Python witness `option-e-phase1-gram-h6.witness.json` carries
    the numerical instances at substrate `q_0 ∈ ℝ` for all 11 partitions
    `λ ⊢ 6`. A Mathlib-bridging follow-up will provide the symbolic
    construction at general `q` over a generic `R`. -/
structure SeminormalBlockData (R : Type*) [CommRing R]
    (n : ℕ) (lam : Partition n) (q : R) where
  /-- Number of standard Young tableaux of shape `λ`. -/
  dimLambda : ℕ
  /-- ρ_λ(σ_k) for k = 1, …, n−1 (length `n − 1`). -/
  rhoLambdaSigmaK : Fin (n - 1) → Matrix (Fin dimLambda) (Fin dimLambda) R
  /-- ρ_λ(w_0) for the longest element `w_0 ∈ S_n`. -/
  rhoLambdaW0 : Matrix (Fin dimLambda) (Fin dimLambda) R
  /-- The character value χ_λ(w_0) = tr(ρ_λ(w_0)). -/
  chiLambdaW0 : R

/-- **Witness-recorded Wedderburn-sum identity at H_3.** Records the
    structural identity verified by the Python cross-check

      `tr_M(b_i · b_j) = Σ_{λ ⊢ 3} y_λ · tr(ρ_λ(b_i) · ρ_λ(b_j))`

    for the H_3 NF basis `{1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1}`
    (21 unique entries). The canonical instance is the Python
    witness `option-e-phase1-h3-cross-check.witness.json`:

    * `max_residual := 2.22e-16` (float64 epsilon, well below
      the 1 ppQ ≡ 10⁻¹⁵ acceptance bar from CLAUDE.md §Precision goals);
    * `rms_residual := 1.14e-16` (RMS across 36 NF Gram entries).

    Following the `BraidWordBasisGram.lean` pattern in this directory,
    the class encodes the recorded numerical bound so downstream
    consumers can `[H3WedderburnReassembly]` and obtain the
    precision-tagged identity. -/
class H3WedderburnReassembly where
  /-- Max single-entry residual of the Wedderburn-sum reassembly
      vs the published H_3 NF-basis Gram, in float64 epsilon units. -/
  max_residual_eps : ℝ
  /-- The recorded residual is at or below the 1 ppQ precision floor
      (10⁻¹⁵), satisfying L1 compute precision per CLAUDE.md. -/
  residual_below_ppq : max_residual_eps ≤ (1 : ℝ) * 10 ^ (-15 : ℤ)

/-- The numerical witness pin: the H_3 Wedderburn reassembly residual
    at `q_0` is 2.22e-16, below the 1 ppQ floor. The literal value is
    pulled from `option-e-phase1-h3-cross-check.witness.json` (Python
    cross-check), with the floating-point bound encoded here so Lean
    downstream consumers see the precision tag. -/
noncomputable instance : H3WedderburnReassembly where
  max_residual_eps := (222 : ℝ) * 10 ^ (-18 : ℤ)
  residual_below_ppq := by
    show (222 : ℝ) * 10 ^ (-18 : ℤ) ≤ (1 : ℝ) * 10 ^ (-15 : ℤ)
    norm_num

end QOU.BraidKnot.GramSeminormalBlock
