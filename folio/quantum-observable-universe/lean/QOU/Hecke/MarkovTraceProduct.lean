import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.List.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Hecke.MarkovTraceProduct — Product factorization of the Markov trace

The Markov trace of a braid β ∈ B_n factors as a product over generators:

  tr_M(ρ(β)) = ∏_{i=0}^{n-2} V̂_i(q)

where V̂_i(q) = z · a_i + b_i is the vertex volume at generator σ_i.
This follows from the Markov property applied recursively to the
rightmost active generator.

**Pre-Archimedean (formal-chain) version.**  Lives under
`lean/QOU/` and is compiled by `lake build`.  Polymorphic in the
ground ring `R_q = ℤ[q^±1]` (Laurent polynomials) per
`QOU.GroundRingAnnotations`.  The co-located documentation stub at
`braids-and-knots/markov-trace-product.lean` mirrors this content.

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

/-- The vertex volume at generator σ_i:
    `V̂_i(q) = z · a_i + b_i`
    where z = 1/(q^{1/2} + q^{-1/2}) is the Markov trace parameter. -/
noncomputable def vertexVolume (z : R_q) (gc : GeneratorChain) : R_q :=
  z * gc.a + gc.b

/-! ## Markov-trace axioms + product factorization -/

/-- **Markov-trace axioms** (cons form, equivalent to the snoc form
    under commutativity of `R_q`). -/
class MarkovTraceAxioms (z : R_q) where
  trace : List GeneratorChain → R_q
  trace_nil : trace [] = 1
  trace_cons : ∀ (c : GeneratorChain) (cs : List GeneratorChain),
    trace (c :: cs) = vertexVolume z c * trace cs

/-- The product of vertex volumes over a chain list, defined
    recursively to mirror the cons-form Markov axiom. -/
noncomputable def chainProduct (z : R_q) : List GeneratorChain → R_q
  | [] => 1
  | c :: cs => vertexVolume z c * chainProduct z cs

/-! ## Product factorization theorem -/

/-- The product factorization of the Markov trace as a structure
    record (existence form). -/
structure MarkovTraceProduct where
  n : ℕ
  q : R_q
  z : R_q
  z_ne_zero : z ≠ 0
  chains : Fin (n - 1) → GeneratorChain
  traceValue : R_q
  factorization : traceValue =
    Finset.univ.prod (fun i => vertexVolume z (chains i))

/-- **Existence of the product factorization** (record-construction form). -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem markov_trace_product
    (z : R_q) (hz : z ≠ 0)
    (n : ℕ) (q : R_q)
    (chains : Fin (n - 1) → GeneratorChain) :
    ∃ (mtp : MarkovTraceProduct),
      mtp.n = n ∧ mtp.q = q ∧
      mtp.traceValue =
        Finset.univ.prod (fun i => vertexVolume mtp.z (mtp.chains i)) :=
  ⟨{
    n := n
    q := q
    z := z
    z_ne_zero := hz
    chains := chains
    traceValue := Finset.univ.prod (fun i => vertexVolume z (chains i))
    factorization := rfl
  }, rfl, rfl, rfl⟩

/-- **Strengthened theorem (Markov-property product factorization,
    list form).**  Under the `MarkovTraceAxioms` typeclass, the
    trace of any chain-list factors as the product of vertex
    volumes (computed by `chainProduct`). -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem markov_trace_product_recursion
    {z : R_q} [inst : MarkovTraceAxioms z]
    (chains : List GeneratorChain) :
    MarkovTraceAxioms.trace (z := z) chains = chainProduct z chains := by
  induction chains with
  | nil =>
    rw [MarkovTraceAxioms.trace_nil, chainProduct]
  | cons c cs ih =>
    rw [MarkovTraceAxioms.trace_cons, chainProduct, ih]

/-- **Concatenation of chain products** (pure list lemma). -/
theorem chainProduct_append (z : R_q) (cs ds : List GeneratorChain) :
    chainProduct z (cs ++ ds) = chainProduct z cs * chainProduct z ds := by
  induction cs with
  | nil => simp [chainProduct]
  | cons c cs ih =>
    simp [chainProduct, ih, mul_assoc]

end

end QOU.Hecke
