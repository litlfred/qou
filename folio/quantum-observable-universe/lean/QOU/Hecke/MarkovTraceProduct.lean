import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.List.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.MathlibExt.OcneanuChainFactorisation

/-!
# QOU.Hecke.MarkovTraceProduct — Product factorization of the Markov trace

For any genuine Markov (Ocneanu) trace `T` and an **ascending** word with one
affine letter `a_i σ_i + b_i` per generator, used once each in increasing
order, the trace factors as a product over generators:

  tr_M((a_n σ_n + b_n) ⋯ (a_{n+k-1} σ_{n+k-1} + b_{n+k-1})) = ∏ V̂_i,

where V̂_i = z · a_i + b_i is the vertex volume. This follows from the Markov
property applied recursively to the rightmost letter
(`QOU.MathlibExt.OcneanuTrace.MarkovTrace.tr_chainWord`).

**Scope.** This holds for ascending words only. For a general braid word the
factorisation is false: a Markov trace is not multiplicative over generators.

**History (bean `qou-ltwg`, owner options 2 + 3, 2026-11-20).** Until this
date the statement here was conditional on a class `MarkovTraceAxioms z`. That
class's two axioms were exactly the recursion defining `chainProduct`, so
`⟨chainProduct z, rfl, fun _ _ => rfl⟩` inhabited it and the "factorisation"
held by definition. The record `MarkovTraceProduct`, which stored a
`traceValue` defined as the product it then claimed equal to the product, was
removed for the same reason. The theorems below take a real trace `T` on a real
algebra `A` instead. The `index` field of `GeneratorChain` is not used by them:
a chain list is placed on consecutive generators, in list order.

**Pre-Archimedean (formal-chain) version.**  Lives under
`lean/QOU/` and is compiled by `lake build`.  Polymorphic in the
ground ring `R_q = ℤ[q^±1]` (Laurent polynomials) per
`QOU.GroundRingAnnotations`.  The co-located documentation stub at
`mass-theory/markov-trace-product.lean` duplicated this content under
`QOU.Braiding` until 2026-11-20 and was removed.

LaTeX label: `thm:markov-trace-product`

## References

- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.Hecke

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ). -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Generator chain reduction -/

/-- A generator chain: the Hecke reduction of all crossings at σ_i
    to a linear form a_i σ_i + b_i. -/
structure GeneratorChain where
  /-- Index i of the generator σ_i. -/
  index : ℕ
  /-- Coefficient of σ_i after Hecke reduction. -/
  a : R_q
  /-- Constant term after Hecke reduction. -/
  b : R_q

/-- The vertex volume at generator σ_i: `V̂_i = z · a_i + b_i`, for the
    abstract Markov parameter `z` (convention-neutral). -/
noncomputable def vertexVolume (z : R_q) (gc : GeneratorChain) : R_q :=
  z * gc.a + gc.b

/-- The product of vertex volumes over a chain list. -/
noncomputable def chainProduct (z : R_q) : List GeneratorChain → R_q
  | [] => 1
  | c :: cs => vertexVolume z c * chainProduct z cs

/-- **Concatenation of chain products** (pure list lemma). -/
theorem chainProduct_append (z : R_q) (cs ds : List GeneratorChain) :
    chainProduct z (cs ++ ds) = chainProduct z cs * chainProduct z ds := by
  induction cs with
  | nil => simp [chainProduct]
  | cons c cs ih =>
    simp [chainProduct, ih, mul_assoc]

/-- The zero chain, used as the out-of-range default. -/
def GeneratorChain.zero : GeneratorChain := ⟨0, 0, 0⟩

/-- `chainProduct` as a product over list positions. -/
theorem chainProduct_eq_prod_range (z : R_q) (cs : List GeneratorChain) :
    chainProduct z cs
      = ∏ i ∈ Finset.range cs.length, vertexVolume z (cs.getD i GeneratorChain.zero) := by
  induction cs with
  | nil => simp [chainProduct]
  | cons c cs ih =>
    rw [chainProduct, ih, List.length_cons, Finset.prod_range_succ', mul_comm]
    simp

variable {A : Type*} [Ring A] [Algebra R_q A]

/-- The ascending affine word of a chain list, placed on the consecutive
    generators `σ_n, σ_{n+1}, …` of the tower of `T`. -/
noncomputable def chainListWord (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace R_q A)
    (cs : List GeneratorChain) (n : ℕ) : A :=
  T.chainWord (fun m => (cs.getD (m - n) GeneratorChain.zero).a)
    (fun m => (cs.getD (m - n) GeneratorChain.zero).b) n cs.length

/-- **Product factorisation of the Markov trace** on an ascending chain word,
    for every genuine Markov trace `T`:

      `tr_M(chainListWord T cs n) = ∏_{c ∈ cs} (z · a_c + b_c) = chainProduct z cs`.

    Proved from the Markov stabilisation axiom of `T`, not assumed. -/
-- Ref: [jones1987] §5 (The Markov trace)
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
theorem markov_trace_product (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace R_q A)
    (cs : List GeneratorChain) (n : ℕ) :
    T.tr (chainListWord T cs n) = chainProduct T.z cs := by
  rw [chainListWord, T.tr_chainWord, chainProduct_eq_prod_range]
  refine Finset.prod_congr rfl (fun i _ => ?_)
  simp only [Nat.add_sub_cancel_left, vertexVolume]
  ring

/-- **Concatenation** (the real content of the removed `markov_trace_append`):
    for two chain lists placed one after the other, the trace is the product of
    the two chain products. -/
theorem markov_trace_append (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace R_q A)
    (cs ds : List GeneratorChain) (n : ℕ) :
    T.tr (chainListWord T (cs ++ ds) n) = chainProduct T.z cs * chainProduct T.z ds := by
  rw [markov_trace_product, chainProduct_append]

end

end QOU.Hecke
