import QOU.Hecke.Algebra
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Algebra.Hom

/-!
# 1-dim character ↔ per-generator volume bridge

For any 1-dimensional representation φ : H_n(q) → R, the character
χ^φ on a braid word β factorises as a product of per-generator
contributions:

  χ^φ(β) = ∏_i V̂_i^φ

where V̂_i^φ collects the φ-image of all crossings at generator i.

This is the **universal 1-dim formula** verified numerically at
A = 1 (proton, neutron) and A = 2 (deuteron) to ~1e-16 precision
in [`v_hat_to_delta_lambda_bridge.py`].  The proof relies only on
two facts:

  1. φ is an `R`-algebra homomorphism: φ(a · b) = φ(a) · φ(b).
  2. R is commutative, so individual scalar factors commute and
     can be regrouped by generator index.

The companion proof in
[`docs/audits/2026-05-09-kite-tail-reconciliation.md`]
gives the full reasoning.

For multi-dim irreps the analogue does NOT hold — the trace of a
matrix product does not factor as a product of traces.  Closure
in the multi-dim sector requires the operator-valued
A^λ_{μ,ν}(I) interface coefficient from the refined Sub-lemma 2.1
([`docs/audits/2026-05-04-sublemma-2-1-refined.md`]).

## References

- `wedderburn_pair_volumes.atom_per_generator_full_matrices`
  (numerical V̂_i^λ extraction per generator).
- `v_hat_to_delta_lambda_bridge.py` (numerical verification at
  A=1 and A=2 to ~1e-16).
- [thm:wedderburn-mass-formula] (the per-channel decomposition this
  bridge specialises).
-/

namespace QOU.Hecke

universe u

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [CommRing A] [Algebra R A]
  [HeckeAlgebra R n q A]

/-- A one-dimensional character on `H_n(q)` is an `R`-algebra
homomorphism with values in `R`.  Equivalently: a ring map
`φ : A →+* R` that is `R`-linear (preserves the `R`-action).

For `H_n(q)` the 1-dim characters are exactly two — the symmetric
character `φ_sym(σ_i) = q` (corresponding to the trivial irrep
of `S_n`, partition `(n)`) and the alternating character
`φ_alt(σ_i) = -q⁻¹` (corresponding to the sign irrep, partition
`(1^n)`).  Higher-dim irreps do NOT factor through 1-dim
characters in this way.

The per-generator factorisation below is stated for the
*commutative* (abelianised) algebra `A`: a 1-dim character lands in
the commutative ring `R` and factors through the abelianisation of
`H_n(q)`, so the `Finset`-indexed (order-free) product over the word
factors is well-defined exactly in this regime.  This is the
algebraic content of "individual scalar factors commute and can be
regrouped" — the multi-dim sector (non-commutative `A`) requires the
operator-valued interface coefficient instead. -/
abbrev OneDimChar (R : Type u) (A : Type u) [CommRing R] [CommRing A] [Algebra R A] :=
  A →ₐ[R] R

namespace OneDimChar

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [CommRing A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]

/-- **Multiplicativity.**  Any 1-dim character `φ` is multiplicative:
`φ(a · b) = φ(a) · φ(b)`.  This is just the `RingHom.map_mul` of
the underlying algebra map.  Listed as a lemma here to expose the
specific flavour used in the per-generator bridge proof. -/
theorem map_mul_one_dim (φ : OneDimChar R A) (a b : A) :
    φ (a * b) = φ a * φ b := by
  exact φ.map_mul a b

/-- **1-dim character of an iterated product.**  For any list of
crossing operators `c_k σ_{i_k} + d_k · 1` (the elementary form a
braid-word factor takes), the character of the product is the
product of the individual character values.  Direct consequence of
`map_mul_one_dim` applied iteratively (`Finset.prod_hom`). -/
theorem map_prod_one_dim (φ : OneDimChar R A) {ι : Type*}
    (s : Finset ι) (f : ι → A) :
    φ (∏ k ∈ s, f k) = ∏ k ∈ s, φ (f k) := by
  exact map_prod φ f s

/-- **The 1-dim per-generator factorisation theorem.**
Let `β = ∏_{k ∈ s} f k` be a braid word written as a finite
product of crossing operators
`f k = (cd k).1 • embed (i_idx k) + (cd k).2 • 1`.  For any
1-dim character `φ`,

  `φ(β) = ∏_{i ∈ s.image i_idx} ∏_{k ∈ s.filter (i_idx · = i)}
           ((cd k).1 · φ(embed i) + (cd k).2)`

i.e. the per-generator factorisation of the φ-image.  This is
the universal product formula
`χ^{1-dim}(β_K) = ∏_i V̂_i^{1-dim}` verified numerically at
A=1 + A=2 to ~1e-16 in `v_hat_to_delta_lambda_bridge.py`.

The proof is three steps:

  1. `φ` is multiplicative (algebra-hom), so
     `φ(∏_k f k) = ∏_k φ(f k)` (`AlgHom.toRingHom.map_prod`).
  2. Each `f k` has the linear form `c·σ + d·1`, so
     `φ(f k) = c · φ(σ) + d` (`AlgHom.map_add`, `map_smul`,
     `map_one`).
  3. Regroup the product by generator index using
     `Finset.prod_fiberwise` (Mathlib lemma): for any
     `g : ι → γ` with decidable equality on γ,
     `∏_{a ∈ s} f a = ∏_{b ∈ s.image g} ∏_{a ∈ s.filter (g · = b)} f a`.

The statement here uses the "fiber form" indexed by
`s.image i_idx` so the outer product ranges only over
generators that actually appear in the word — matching the
content of `wedderburn_pair_volumes.atom_per_generator_full_matrices`,
which iterates only over generators with non-empty crossing
chains. -/
theorem one_dim_factors_per_generator
    (φ : OneDimChar R A) {ι : Type*} [DecidableEq ι]
    [DecidableEq (Generator n)]
    (s : Finset ι)
    (f : ι → A) (i_idx : ι → Generator n) (cd : ι → R × R)
    (h_form : ∀ k ∈ s, f k = (cd k).1 • HA.embed (i_idx k) + (cd k).2 • 1) :
    φ (∏ k ∈ s, f k) =
    ∏ i ∈ s.image i_idx,
      ∏ k ∈ s.filter (fun k => i_idx k = i),
        ((cd k).1 * φ (HA.embed i) + (cd k).2) := by
  -- 1. φ is multiplicative (algebra hom over the commutative algebra A),
  --    so the character of the product is the product of characters.
  rw [map_prod]
  -- 2. Regroup the product over the word by generator index
  --    (`Finset.prod_fiberwise_of_maps_to`).
  rw [← Finset.prod_fiberwise_of_maps_to (g := i_idx)
        (fun k hk => Finset.mem_image_of_mem i_idx hk)]
  -- 3. Each factor has the linear form `c • σ + d • 1`, so its φ-image
  --    is `c · φ(σ) + d`; rewrite `i_idx k = i` inside each fibre.
  refine Finset.prod_congr rfl (fun i _ => Finset.prod_congr rfl (fun k hk => ?_))
  rw [Finset.mem_filter] at hk
  rw [h_form k hk.1, map_add, map_smul, map_smul, map_one, smul_eq_mul,
    smul_eq_mul, mul_one, hk.2]

end OneDimChar

end QOU.Hecke
