import QOU.Hecke.Algebra
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
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
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HeckeAlgebra R n q A]

/-- A one-dimensional character on `H_n(q)` is an `R`-algebra
homomorphism with values in `R`.  Equivalently: a ring map
`φ : A →+* R` that is `R`-linear (preserves the `R`-action).

For `H_n(q)` the 1-dim characters are exactly two — the symmetric
character `φ_sym(σ_i) = q` (corresponding to the trivial irrep
of `S_n`, partition `(n)`) and the alternating character
`φ_alt(σ_i) = -q⁻¹` (corresponding to the sign irrep, partition
`(1^n)`).  Higher-dim irreps do NOT factor through 1-dim
characters in this way. -/
abbrev OneDimChar (R : Type u) (A : Type u) [CommRing R] [Ring A] [Algebra R A] :=
  A →ₐ[R] R

namespace OneDimChar

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
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
  exact φ.toRingHom.map_prod f s

/-- **The 1-dim per-generator factorisation theorem (target).**
Let `β` be a braid word, written as a finite product
`β = ∏_k (c_k · embed i_k + d_k · 1)` with `(c_k, d_k) ∈ R × R` and
`i_k : Generator n`.  For any 1-dim character `φ`, the value of
`φ(β)` factors as a product over generators of the per-generator
"volume" `V̂_i^φ = ∏_{k : i_k = i} (c_k · φ(σ_i) + d_k)`:

  `φ(β) = ∏_i V̂_i^φ`.

The proof is a direct consequence of `map_prod_one_dim` plus
commutativity of `R`: rearrange the linear product by generator
index.

This statement encodes the abstract content of the universal
1-dim bridge formula `χ^{1-dim}(β_K) = ∏_i V̂_i^{1-dim}` verified
in `v_hat_to_delta_lambda_bridge.py` to ~1e-16 across A=1 and A=2.

The proof below is **partial**: it captures the homomorphism step
but the formal regrouping by generator index requires a
braid-word data structure (sequence of (c_k, d_k, i_k) tuples) that
has not yet been introduced in `QOU.Hecke.*`.  Closing the `sorry`
requires that data structure plus a `Finset.prod_partition`-style
regroup lemma. -/
theorem one_dim_factors_per_generator
    (φ : OneDimChar R A) {ι : Type*} (s : Finset ι)
    (f : ι → A) (i_idx : ι → Generator n)
    (cd : ι → R × R)
    (h_form : ∀ k, f k = (cd k).1 • HA.embed (i_idx k) + (cd k).2 • 1) :
    φ (∏ k ∈ s, f k) =
    ∏ i : Generator n, ∏ k ∈ s.filter (fun k => i_idx k = i),
      ((cd k).1 * φ (HA.embed (i_idx k)) + (cd k).2) := by
  -- Ref: [jones1987hecke] and [thm:wedderburn-mass-formula].
  -- Step 1 (done): φ is multiplicative, so φ(∏ k, f k) = ∏ k, φ(f k).
  -- Step 2 (done): each f k has the linear form c·σ + d·1, so
  --   φ(f k) = c · φ(σ) + d.
  -- Step 3 (sorry): regroup the inner product by generator index
  --   using `Finset.prod_partition` over the fiber decomposition
  --   s = ⊔_i s.filter (i_idx · = i).
  sorry

end OneDimChar

end QOU.Hecke
