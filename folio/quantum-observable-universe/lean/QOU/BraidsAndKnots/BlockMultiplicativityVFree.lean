import HeckeTemperleyLieb.BraidedBlockShiftTrace

/-!
# Block multiplicativity of the per-generator `V̂` on the disjoint Hecke product

Content block
[`prop:block-multiplicativity-v-free`](../../../mass-theory/block-multiplicativity-v-free.md).

## 2026-11-27 rewrite: the conjecture is a theorem, under convention D

Until this date the file carried a class `BlockMultiplicativityVFree` whose one
conjectural field was discharged by choosing its predicate to be `q = 1`, a
`def` that inhabited it with `v_p = v_n = 1`, and a theorem comparing the float
literals `0.7084 / 0.6005`. None of that is kept: the class assumed nothing, and
float literals do not belong in a proof.

Since the 2026-11-18 owner ruling (`weight_scheme = "jones_wenzl"`, convention D),
the producer `computations/mass_at_3A_proper.py::per_generator_V_hat_3A` computes
`V̂_i` as the **Markov trace** of the generator's accumulated word
`W_i = α_i σ_i + β_i` (its own comment: "`V_hat_i = z*a_i + b_i`, the Markov trace
of the generator's word"). With that reading the block is proved here over a
generic commutative ring:

* `vhat_eq` — **`V̂` is independent of the strand count and of the position.**
  For every generator index `n`, `tr(a·1 + b·g_n) = a + b·z`. Nothing about
  `A = Z + N`, the block, or the other blocks enters.
* `tr_block_word` — the trace of a 3-strand block word with ascending letters
  `(a₀ + b₀ g₀)(a₁ + b₁ g₁)` is the product `V̂₀ · V̂₁` of its per-generator values.
  This is the producer's `v = V₀ · V₁`.
* `block_multiplicativity_v_free` — **the constituent vacuum.** For any
  arrangement of `Z` proton and `N` neutron blocks on disjoint 3-strand windows,
  `tr(𝓑_K^vac) = v_p^Z · v_n^N` with `v = V̂₀ V̂₁` read at offset `0`. This is the
  block's `T₁^free(K) = v_p^Z v_n^N`; it rests on the disjoint-block trace law
  `BraidedBlockShiftTrace.tr_blockProd_pn`, proved from the three Hecke relations.

## What this does not cover

* The `.md` writes the weights as `w_λ = dim_q(λ)² / [3A]_q!` ("plancherel"). That
  scheme is no longer the producer default, and it is not a Markov trace, so
  nothing here is about it.
* `tr_block_word` needs the letters in **ascending** generator order. The
  producer groups a block's factors by generator before multiplying, so
  `Π_g V̂_g` is the trace of the reordered word, which differs from the trace of
  the interleaved braid word whenever the order matters. Example: `σ₁σ₂σ₁σ₂`
  and its reordering `σ₁²σ₂²` carry the same per-generator data, and
  `tr(σ₁²σ₂²) = (hz + 1)²`, while `σ₁σ₂σ₁σ₂ = σ₂σ₁σ₂²` (braid relation) gives
  `tr(σ₁σ₂σ₁σ₂) = tr(σ₁σ₂³) = (h² + 1) z² + h z` (cyclicity, Hecke, Markov). The
  difference is `z² − hz − 1`, which at `z = q³/(q²+1)` equals
  `−(q⁴ + q² + 1)/(q² + 1)²`, never zero. The block's statement is
  about the producer's quantity, which is the reordered one.
* The numbers `0.7084`, `0.6005` are evaluations at the calibration point and
  are not used.

Base ring: generic `[CommRing R]`, generic `R`-algebra `A`; no ordering, no
numerics.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] mass-theory/block-multiplicativity-v-free.md
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
  QOU.MathlibExt.HeckeSandwichReduces QOU.MathlibExt.BraidedBlockShiftTrace

/-- Flavor of a nucleon block. -/
inductive NucleonFlavor
  | proton
  | neutron
deriving DecidableEq, Inhabited

/-- The block-factor product `v_p^Z · v_n^N`. -/
def blockFactorProduct {R : Type*} [CommSemiring R] (v_p v_n : R) (Z N : ℕ) : R :=
  v_p ^ Z * v_n ^ N

/-- The block-factor product is multiplicative in `(Z, N)`. -/
theorem blockFactorProduct_add {R : Type*} [CommSemiring R] (v_p v_n : R) (Z N Z' N' : ℕ) :
    blockFactorProduct v_p v_n (Z + Z') (N + N') =
      blockFactorProduct v_p v_n Z N * blockFactorProduct v_p v_n Z' N' := by
  unfold blockFactorProduct
  rw [pow_add, pow_add]
  ring

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- **`V̂` does not see the strand count or the position.** For every generator
index `n`, the Markov trace of `a·1 + b·g_n` is `a + b·z`. -/
theorem vhat_eq (n : ℕ) (a b : R) : T.tr (a • (1 : A) + b • T.g n) = a + b * T.z := by
  have hz : T.tr (T.g n) = T.z := by
    have := T.markov n 1 (Subalgebra.one_mem _)
    rwa [one_mul, T.tr_one, mul_one] at this
  rw [map_add, map_smul, map_smul, T.tr_one, hz, smul_eq_mul, smul_eq_mul, mul_one]

/-- **A 3-strand block word with ascending letters has trace `V̂₀ · V̂₁`.** -/
theorem tr_block_word (a₀ b₀ a₁ b₁ : R) :
    T.tr (wordVal T 0 [(0, a₀, b₀), (1, a₁, b₁)]) = (a₀ + b₀ * T.z) * (a₁ + b₁ * T.z) := by
  set x : A := letterVal T 0 (0, a₀, b₀)
  have hx : x ∈ T.H 1 := by
    simpa using letterVal_mem_H T 0 0 (0, a₀, b₀) le_rfl
  have htx : T.tr x = a₀ + b₀ * T.z := by
    simpa [x, letterVal] using vhat_eq T 0 a₀ b₀
  simp only [wordVal_cons, wordVal_nil, mul_one]
  change T.tr (x * letterVal T 0 (1, a₁, b₁)) = _
  simp only [letterVal, zero_add, mul_add, mul_smul_comm, mul_one, map_add, map_smul,
    smul_eq_mul]
  rw [T.markov 1 x hx, htx]
  ring

/-- **Block multiplicativity on the constituent vacuum.** Blocks `k = 0, …, n` sit on
disjoint 3-strand windows (generators `3k, 3k+1`); block `k` is a proton block when
`isP k`. Then the trace of the vacuum is `v_p^Z · v_n^N`, with
`v_p = V̂^p₀ V̂^p₁` and `v_n = V̂^n₀ V̂^n₁` the per-generator values of the two
block words, independent of `A = n + 1` and of the arrangement. -/
theorem block_multiplicativity_v_free [BraidedTower T] (isP : ℕ → Prop) [DecidablePred isP]
    (p₀ p₁ n₀ n₁ : R × R) (n : ℕ) :
    T.tr (blockProd (fun k => wordVal T (3 * k)
        (if isP k then [(0, p₀.1, p₀.2), (1, p₁.1, p₁.2)]
          else [(0, n₀.1, n₀.2), (1, n₁.1, n₁.2)])) n)
      = blockFactorProduct
          ((p₀.1 + p₀.2 * T.z) * (p₁.1 + p₁.2 * T.z))
          ((n₀.1 + n₀.2 * T.z) * (n₁.1 + n₁.2 * T.z))
          ((Finset.range (n + 1)).filter isP).card
          ((Finset.range (n + 1)).filter (fun k => ¬ isP k)).card := by
  have hw : ∀ l ∈ ([(0, p₀.1, p₀.2), (1, p₁.1, p₁.2)] : List (ℕ × R × R)), l.1 ≤ 1 := by
    simp
  have hw' : ∀ l ∈ ([(0, n₀.1, n₀.2), (1, n₁.1, n₁.2)] : List (ℕ × R × R)), l.1 ≤ 1 := by
    simp
  rw [tr_blockProd_pn T isP _ _ hw hw' n, tr_block_word, tr_block_word, blockFactorProduct]

end QOU.BraidKnot
