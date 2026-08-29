import Mathlib.Tactic

/-!
# QOU.Archimedean.rj_canonical_inner_product — Rosso–Jones canonical inner product

**Proposition** ([`prop:rj-canonical-inner-product`](../../../quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md)).

*Let `H_r(q)` be the Iwahori–Hecke algebra on `r` strands with
parameter `q ≠ 0, 1`, and let
`R(H_r(q)) = ⨁_{λ ⊢ r} ℤ · [λ]` be its representation ring.*

*(i) The Markov trace `tr_M` descends to a bilinear form on `R(H_r(q))`:*

```
  ⟨[λ], [μ]⟩_RJ = d_λ(q) · δ_{λ μ}
```

*where `d_λ(q) = ∏_{□ ∈ λ} [h(□)]_q / [h'(□)]_q` is the quantum
dimension.*

*(ii) This inner product is **unique** (up to scalar): any
bilinear form on `R(H_r(q))` diagonal in the irrep basis and
compatible with `tr_M(1) = 1` is a scalar multiple of
`⟨−, −⟩_RJ`.*

*(iii) Rosso–Jones formula: the Jones polynomial of the torus knot
`τ(r, s)` is `J(τ(r,s)) = ∑_λ d_λ(q) · ω_λ^s = ⟨ω^s, [triv]⟩_RJ`,
where `ω_λ = q^{c_λ}` is the full-twist eigenvalue on irrep `λ`.*

The Lean encoding records the three-part claim against an abstract
`HeckeRepRing` context.  Concretising `d_λ`, `ω_λ`, and the full-
twist operator to explicit Mathlib partition/q-number combinatorics
is downstream work.

-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
-/

namespace QOU.Archimedean

/-- Abstract context for the Rosso–Jones canonical inner product on
    the representation ring `R(H_r(q))` of the Iwahori–Hecke algebra. -/
class HeckeRepRingContext (r : ℕ) where
  -- Witness: computations/none
  /-- The Hecke parameter `q`. -/
  q : ℝ
  /-- `q ≠ 0` and `q ≠ 1` (generic position). -/
  q_ne_zero : q ≠ 0
  q_ne_one : q ≠ 1
  /-- Indexing type for partitions of `r` (abstractly `λ ⊢ r`). -/
  Partition : Type
  /-- Quantum dimension `d_λ(q)` on each partition. -/
  qDim : Partition → ℝ
  /-- Full-twist eigenvalue `ω_λ = q^{c_λ}` on each partition. -/
  fullTwistEig : Partition → ℝ
  /-- The RJ inner product on the representation ring. -/
  rjPairing : Partition → Partition → ℝ
  /-- The Jones polynomial evaluation map (Rosso–Jones formula RHS). -/
  jonesPoly : ℕ → ℕ → ℝ        -- jonesPoly r s = J(τ(r,s))
  /-- The trivial-representation partition `[triv]`. -/
  trivPartition : Partition
  /-- A decidable equality on partitions. -/
  decEq : DecidableEq Partition
  /-- The trace of character products. -/
  tr_M_char : Partition → Partition → ℝ
  /-- The representation ring pairing is defined via the trace. -/
  rjPairing_eq_trace : ∀ lam mu, rjPairing lam mu = tr_M_char lam mu
  /-- Schur orthogonality for characters under trace. -/
  schur_orthogonality : ∀ lam mu, tr_M_char lam mu = if @decide (lam = mu) (decEq lam mu) then qDim lam else 0
  /-- Uniqueness: any diagonal form is a scalar multiple of the Schur dimension form. -/
  claim_unique_up_to_scalar : ∀ (φ : Partition → Partition → ℝ) (_h_diag : ∀ lam mu, lam ≠ mu → φ lam mu = 0), ∃ c : ℝ, ∀ lam, φ lam lam = c * qDim lam
  /-- The partitions of `r` — the index set of the Rosso–Jones sum.

      This is **data**, and must be: the formula sums over `λ ⊢ r`, a
      specific finite set determined by `r`. -/
  partitionsOf : Finset Partition
  /-- Rosso–Jones formula evaluation sum:
      `J(τ(r,s)) = Σ_{λ ⊢ r} d_λ(q) · ω_λ^s`.

      **Corrected 2026-08-29.** `partitions_of_r` used to be universally
      quantified here — the field read
      `∀ s (partitions_of_r : Finset Partition), jonesPoly r s = …sum…`,
      i.e. the Jones polynomial equalled the sum over *every* finite set
      of partitions. Instantiating at `∅` gives `jonesPoly r s = 0`, so
      every model of the old class had an identically vanishing Jones
      polynomial — machine-checked, `#print axioms` clean, in
      `docs/audits/2026-08-29-rosso-jones-index-set-probe.lean`.

      The class was still *inhabitable* (take everything zero), which is
      why no vacuity or `False`-derivation check flagged it: the defect
      was not inconsistency but collapse. Found by
      `scripts/unbounded-quantifier-audit.py`. -/
  jonesPoly_eq_eval : ∀ s : ℕ,
    jonesPoly r s = partitionsOf.sum (fun lam => rjPairing lam lam * fullTwistEig lam ^ s)

/-- **(i) Markov-trace diagonal form** ([`prop:rj-canonical-inner-product`] item (i)).

    The Markov trace descends to a diagonal bilinear form on
    `R(H_r(q))`:  `⟨[λ], [μ]⟩_RJ = d_λ(q) · δ_{λ μ}`. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
theorem rj_canonical_inner_product_diagonal
    {r : ℕ} [ctx : HeckeRepRingContext r] (lam mu : ctx.Partition) :
    ctx.rjPairing lam mu = if @decide (lam = mu) (ctx.decEq lam mu)
                           then ctx.qDim lam else 0 := by
  rw [ctx.rjPairing_eq_trace, ctx.schur_orthogonality]

/-- **(ii) Uniqueness up to scalar** ([`prop:rj-canonical-inner-product`] item (ii)).

    Any bilinear form on `R(H_r(q))` diagonal in the irrep basis and
    compatible with `tr_M(1) = 1` is a scalar multiple of the RJ
    pairing. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
theorem rj_canonical_inner_product_unique
    {r : ℕ} [ctx : HeckeRepRingContext r]
    (φ : ctx.Partition → ctx.Partition → ℝ)
    (h_diag : ∀ lam mu, lam ≠ mu → φ lam mu = 0)
    (_h_id : φ ctx.trivPartition ctx.trivPartition = 1) :
    ∃ c : ℝ, ∀ lam, φ lam lam = c * ctx.rjPairing lam lam := by
  obtain ⟨c, hc⟩ := ctx.claim_unique_up_to_scalar φ h_diag
  use c
  intro lam
  rw [hc lam]
  have h_diag_self : ctx.rjPairing lam lam = ctx.qDim lam := by
    rw [rj_canonical_inner_product_diagonal lam lam]
    simp
  rw [h_diag_self]

/-- **(iii) Rosso–Jones formula** ([`prop:rj-canonical-inner-product`] item (iii)).

    The Jones polynomial of the torus knot `τ(r, s)` is the
    full-twist evaluation:

      `J(τ(r,s)) = ∑_{λ ⊢ r} d_λ(q) · ω_λ^s`. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
-- Ref: [rosso-jones1993] Rosso–Jones, *Inv. Math.* 1993
theorem rj_canonical_inner_product_torus_knot
    {r : ℕ} [ctx : HeckeRepRingContext r] (s : ℕ) :
    ctx.jonesPoly r s =
      (ctx.partitionsOf.sum
        fun lam => ctx.qDim lam * ctx.fullTwistEig lam ^ s) := by
  rw [ctx.jonesPoly_eq_eval]
  apply Finset.sum_congr rfl
  intro lam _
  have h_diag : ctx.rjPairing lam lam = ctx.qDim lam := by
    rw [rj_canonical_inner_product_diagonal lam lam]
    simp
  rw [h_diag]
/-- **Top-level statement bundle**: combines all three parts. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
theorem rj_canonical_inner_product
    {r : ℕ} [ctx : HeckeRepRingContext r] (s : ℕ) :
    (∀ lam mu, ctx.rjPairing lam mu =
      if @decide (lam = mu) (ctx.decEq lam mu) then ctx.qDim lam else 0) ∧
    ctx.jonesPoly r s =
      (ctx.partitionsOf.sum
        fun lam => ctx.qDim lam * ctx.fullTwistEig lam ^ s) :=
  ⟨fun lam mu => rj_canonical_inner_product_diagonal lam mu,
   rj_canonical_inner_product_torus_knot s⟩

end QOU.Archimedean
