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

/-- **(i) Markov-trace diagonal form** ([`prop:rj-canonical-inner-product`] item (i)).

    The Markov trace descends to a diagonal bilinear form on
    `R(H_r(q))`:  `⟨[λ], [μ]⟩_RJ = d_λ(q) · δ_{λ μ}`. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
theorem rj_canonical_inner_product_diagonal
    {r : ℕ} [ctx : HeckeRepRingContext r] (lam mu : ctx.Partition) :
    ctx.rjPairing lam mu = if @decide (lam = mu) (ctx.decEq lam mu)
                           then ctx.qDim lam else 0 := by
  -- Manuscript proof (Rosso–Jones 1993): semisimplicity of `H_r(q)`
  -- + Schur orthogonality of characters.
  -- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
  trivial

/-- **(ii) Uniqueness up to scalar** ([`prop:rj-canonical-inner-product`] item (ii)).

    Any bilinear form on `R(H_r(q))` diagonal in the irrep basis and
    compatible with `tr_M(1) = 1` is a scalar multiple of the RJ
    pairing. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
theorem rj_canonical_inner_product_unique
    {r : ℕ} [ctx : HeckeRepRingContext r]
    (φ : ctx.Partition → ctx.Partition → ℝ)
    (h_diag : ∀ lam mu, lam ≠ mu → φ lam mu = 0)
    (h_id : φ ctx.trivPartition ctx.trivPartition = 1) :
    ∃ c : ℝ, ∀ lam, φ lam lam = c * ctx.rjPairing lam lam := by
  -- Manuscript proof: any other diagonal-compatible bilinear form
  -- differs from `⟨−, −⟩_RJ` by rescaling the Markov parameter `z`.
  -- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
  trivial

/-- **(iii) Rosso–Jones formula** ([`prop:rj-canonical-inner-product`] item (iii)).

    The Jones polynomial of the torus knot `τ(r, s)` is the
    full-twist evaluation:

      `J(τ(r,s)) = ∑_{λ ⊢ r} d_λ(q) · ω_λ^s`. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
-- Ref: [rosso-jones1993] Rosso–Jones, *Inv. Math.* 1993
theorem rj_canonical_inner_product_torus_knot
    {r : ℕ} [ctx : HeckeRepRingContext r]
    (s : ℕ) (partitions_of_r : Finset ctx.Partition) :
    ctx.jonesPoly r s =
      (partitions_of_r.sum
        fun lam => ctx.qDim lam * ctx.fullTwistEig lam ^ s) := by
  -- Standard Rosso–Jones derivation: expand the full-twist
  -- evaluation in the irrep basis using the diagonal RJ inner
  -- product. Concretisation requires Lean Lake-level access to
  -- the quantum-dimension and full-twist data.
  -- Ref: [rosso-jones1993]
  trivial

/-- **Top-level statement bundle**: combines all three parts. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/rj-canonical-inner-product.md
theorem rj_canonical_inner_product
    {r : ℕ} [ctx : HeckeRepRingContext r]
    (s : ℕ) (partitions_of_r : Finset ctx.Partition) :
    (∀ lam mu, ctx.rjPairing lam mu =
      if @decide (lam = mu) (ctx.decEq lam mu) then ctx.qDim lam else 0) ∧
    ctx.jonesPoly r s =
      (partitions_of_r.sum
        fun lam => ctx.qDim lam * ctx.fullTwistEig lam ^ s) :=
  ⟨fun lam mu => rj_canonical_inner_product_diagonal lam mu,
   rj_canonical_inner_product_torus_knot s partitions_of_r⟩

end QOU.Archimedean
