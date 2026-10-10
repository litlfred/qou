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
`lean/QOU/` and is compiled by `lake build`.  Stated over the
ground ring `R_q = ℤ[q^±1]` (Laurent polynomials) per
`QOU.GroundRingAnnotations` — a formal ring, no archimedean input.

**Canonical home (bean `qou-ekga`, 2026-10-10).** This is the ONE
content-bearing `MarkovTraceAxioms` class. The content-block sibling
`mass-theory/markov-trace-product.lean` previously held a near-duplicate
under `QOU.Braiding`; it now imports this module and re-exports these
declarations, so the two copies cannot drift. The trivially-inhabited
scalar-pin class formerly named `QOU.BraidKnot.MarkovTraceAxioms` is
deprecated as `QOU.BraidKnot.MarkovScalarPins`; its intended claims
(k-fold stabilisation, disjoint factorisation) are restated against
`trace` below (`markov_trace_stabilise`, `markov_trace_disjoint_stabilise`).

**Scope of the class — read before citing anything here.**
`MarkovTraceAxioms z` has exactly one inhabitant for each `z`: its
`trace` is forced to be `chainProduct z` (`markov_trace_product_recursion`),
and that function does satisfy the axioms (`chainProductMarkovTrace`).
So the class axiomatises the **chain-list model** of the Markov trace,
not the Hecke-algebra trace itself, and every theorem in this file is a
statement about that model. That a braid's Hecke-algebra Markov trace
equals the chain-list trace of its Hecke-reduced generator chains is the
step this file does NOT formalise.

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
    where `z` is the Markov trace parameter (supplied, not fixed here). -/
noncomputable def vertexVolume (z : R_q) (gc : GeneratorChain) : R_q :=
  z * gc.a + gc.b

/-! ## Markov-trace axioms + product factorization -/

/-- **Markov-trace axioms** — abstract structure capturing the
    Markov property of `tr_M` on `H_n(q)`-style chain lists.

    A Markov trace at parameter `z` is a function
    `trace : List GeneratorChain → R_q` satisfying:

    - `trace [] = 1` (identity Hecke element traces to 1)
    - `trace (c :: cs) = vertexVolume z c · trace cs` (the **Markov
      property**: prepending a chain multiplies the trace by that chain's
      vertex volume).

    Jones 1987 states the Markov property peeling from the right
    (`trace (cs ++ [c]) = trace cs · vertexVolume z c`); since `R_q` is
    commutative the cons- and snoc-forms are equivalent and the cons form
    is more tractable in Lean.

    The class has exactly one inhabitant per `z` (see the module
    docstring §Scope): `trace = chainProduct z`.

    Ref: [jones1987] https://doi.org/10.2307/1971403
    Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 -/
class MarkovTraceAxioms (z : R_q) where
  /-- The Markov trace of a chain list. -/
  trace : List GeneratorChain → R_q
  /-- Empty chain list traces to the identity element. -/
  trace_nil : trace [] = 1
  /-- **Markov property** (cons form): prepending a chain multiplies
      the trace by that chain's vertex volume. -/
  trace_cons : ∀ (c : GeneratorChain) (cs : List GeneratorChain),
    trace (c :: cs) = vertexVolume z c * trace cs

/-- The product of vertex volumes over a chain list, defined
    recursively to mirror the cons-form Markov axiom. -/
noncomputable def chainProduct (z : R_q) : List GeneratorChain → R_q
  | [] => 1
  | c :: cs => vertexVolume z c * chainProduct z cs

/-- **The class is inhabited, by the explicit product.** Recorded so the
    conditionality of every `[MarkovTraceAxioms z]` result below is
    visibly *not* an open hypothesis: the axioms are satisfiable, and by
    `markov_trace_product_recursion` this is their only model. A `def`,
    not an `instance`, so it never silently enters instance search. -/
def chainProductMarkovTrace (z : R_q) : MarkovTraceAxioms z where
  trace := chainProduct z
  trace_nil := rfl
  trace_cons := fun _ _ => rfl

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

/-- **Existence of the product factorization** (record-construction form).

    NOTE on strength: this is the structure-existence form, provable by
    construction (`traceValue` is set to the product). The form that
    captures the Markov-property recursion is
    `markov_trace_product_recursion` below. -/
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
    volumes (computed by `chainProduct`). Proof: cons-induction,
    applying `trace_cons` at each step. -/
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

/-- **Concatenation of chain products** (pure list lemma; does not
    involve `MarkovTraceAxioms`). -/
theorem chainProduct_append (z : R_q) (cs ds : List GeneratorChain) :
    chainProduct z (cs ++ ds) = chainProduct z cs * chainProduct z ds := by
  induction cs with
  | nil => simp [chainProduct]
  | cons c cs ih =>
    simp [chainProduct, ih, mul_assoc]

/-- **Markov trace of the empty chain** — the axiom `trace_nil`. -/
theorem markov_trace_nil {z : R_q} [inst : MarkovTraceAxioms z] :
    MarkovTraceAxioms.trace (z := z) [] = 1 :=
  MarkovTraceAxioms.trace_nil

/-- **Markov trace of a singleton chain**: `trace [c] = vertexVolume z c`. -/
theorem markov_trace_singleton {z : R_q} [inst : MarkovTraceAxioms z]
    (c : GeneratorChain) :
    MarkovTraceAxioms.trace (z := z) [c] = vertexVolume z c := by
  rw [markov_trace_product_recursion]
  simp [chainProduct]

/-- **Markov trace of a two-chain**: `trace [c₁, c₂] = V̂(c₁) · V̂(c₂)`. -/
theorem markov_trace_pair {z : R_q} [inst : MarkovTraceAxioms z]
    (c₁ c₂ : GeneratorChain) :
    MarkovTraceAxioms.trace (z := z) [c₁, c₂]
      = vertexVolume z c₁ * vertexVolume z c₂ := by
  rw [markov_trace_product_recursion]
  simp [chainProduct]

/-- **Markov-trace multiplicativity over concatenation**:
    `trace (cs ++ ds) = trace cs · trace ds`, from
    `markov_trace_product_recursion` + `chainProduct_append`.

    Ref: [jones1987] https://doi.org/10.2307/1971403 -/
theorem markov_trace_append {z : R_q} [inst : MarkovTraceAxioms z]
    (cs ds : List GeneratorChain) :
    MarkovTraceAxioms.trace (z := z) (cs ++ ds)
      = MarkovTraceAxioms.trace (z := z) cs * MarkovTraceAxioms.trace (z := z) ds := by
  simp only [markov_trace_product_recursion, chainProduct_append]

/-- **`chainProduct` over `List.flatten`** (pure list lemma). -/
theorem chainProduct_flatten (z : R_q) (lls : List (List GeneratorChain)) :
    chainProduct z lls.flatten = (lls.map (chainProduct z)).prod := by
  induction lls with
  | nil => simp [chainProduct]
  | cons l ls ih => simp [List.flatten_cons, chainProduct_append, List.map_cons,
      List.prod_cons, ih]

/-- **Constituent/composite Markov-trace agreement** (chain-list model) —
    the realisation of `lem:tmli-constituent-composite-agreement`: the
    trace of a concatenation of constituent words is the product of the
    constituent traces, `tr_M(β_𝔥) = ∏_i tr_M(β_i)`.

    Ref: [jones1987] https://doi.org/10.2307/1971403
    Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 -/
theorem markov_trace_flatten {z : R_q} [inst : MarkovTraceAxioms z]
    (lls : List (List GeneratorChain)) :
    MarkovTraceAxioms.trace (z := z) lls.flatten
      = (lls.map (MarkovTraceAxioms.trace (z := z))).prod := by
  rw [markov_trace_product_recursion, chainProduct_flatten]
  congr 1
  apply List.map_congr_left
  intro l _
  rw [markov_trace_product_recursion]

/-! ## Stabilisation and disjoint factorisation (restated from the
retired `QOU.BraidKnot.MarkovTraceAxioms`, bean `qou-ekga`)

Markov axiom M3, `tr(x σ_n) = z · tr(x)`, is the case of `trace_cons`
for a **bare** generator chain — `σ_i` with Hecke-reduced coefficients
`a = 1`, `b = 0`, whose vertex volume is exactly `z`. -/

/-- The bare stabilising generator chain at index `i`: `σ_i` itself,
    Hecke-reduced to `1 · σ_i + 0`. -/
def stabChain (i : ℕ) : GeneratorChain := ⟨i, 1, 0⟩

/-- A bare generator chain has vertex volume `z`. -/
theorem vertexVolume_stabChain (z : R_q) (i : ℕ) :
    vertexVolume z (stabChain i) = z := by
  simp [vertexVolume, stabChain]

/-- The trace of a word made only of bare stabilising generators is
    `z ^ (number of generators)`. -/
theorem markov_trace_stabChains {z : R_q} [inst : MarkovTraceAxioms z]
    (is : List ℕ) :
    MarkovTraceAxioms.trace (z := z) (is.map stabChain) = z ^ is.length := by
  induction is with
  | nil => simp [MarkovTraceAxioms.trace_nil]
  | cons i is ih =>
    rw [List.map_cons, MarkovTraceAxioms.trace_cons, ih, vertexVolume_stabChain,
      List.length_cons, pow_succ]
    ring

/-- **k-fold Markov stabilisation (M3 iterated).** Appending `k` bare
    stabilising generators (at any indices `is`, `k = is.length`) to a
    chain word multiplies its trace by `z ^ k`.

    Derived from the class's `trace_nil` / `trace_cons`; replaces the
    vacuous `∃ τ_k, τ_k = τ * z^k` of the retired scalar-pin class. -/
-- Ref: [jones1985] doi:10.2307/1971403   (Markov axiom M3)
theorem markov_trace_stabilise {z : R_q} [inst : MarkovTraceAxioms z]
    (cs : List GeneratorChain) (is : List ℕ) :
    MarkovTraceAxioms.trace (z := z) (cs ++ is.map stabChain)
      = MarkovTraceAxioms.trace (z := z) cs * z ^ is.length := by
  rw [markov_trace_append, markov_trace_stabChains]

/-- **Disjoint-product factorisation with stabilisation** (chain-list
    model): the trace of `K₁`'s chains followed by `K₂`'s chains followed
    by `k` bare stabilising generators is `tr(K₁) · tr(K₂) · z^k`.

    **What this does and does not say.** In the chain-list model the
    trace is multiplicative on *every* concatenation, so no
    strand-disjointness hypothesis is needed or used — disjointness is
    invisible to this model. The physical claim, that the Hecke-algebra
    trace of `K₁ ⊔ K₂` is modelled by this concatenation, is the
    unformalised bridge named in the module docstring. In particular this
    theorem does NOT discharge the content-block class
    `MarkovDisjointStabilisation` (`mass-endomorphism/
    categorical-chain-convergence-mechanisms.lean`), which is stated over
    `ℝ` with convention-D `markovZ q` and carries its own `stab` map. -/
-- Ref: [manuscript] prop:categorical-chain-convergence-mechanisms §"Mechanism 2"
-- Ref: [jones1985] doi:10.2307/1971403   (Markov axioms M1–M4)
theorem markov_trace_disjoint_stabilise {z : R_q} [inst : MarkovTraceAxioms z]
    (cs ds : List GeneratorChain) (is : List ℕ) :
    MarkovTraceAxioms.trace (z := z) (cs ++ ds ++ is.map stabChain)
      = MarkovTraceAxioms.trace (z := z) cs * MarkovTraceAxioms.trace (z := z) ds
          * z ^ is.length := by
  rw [markov_trace_stabilise, markov_trace_append]

/-! ## Degree bound -/

/-- **Degree bound `≤ n² − 1`.** Each of the `n − 1` vertex volumes
    contributes degree `d i ≤ 2·k i + 1` (`hw`), and these per-vertex
    bounds sum within the budget `n² − 1` (`hbudget`); both are carried
    as hypotheses (conformal-weight data from the Hecke representation,
    [kassel1995] Ch. X). The bound on the total degree is derived by
    `Finset.sum_le_sum` + transitivity.

    Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 -/
theorem markovTraceProduct_degree_bound (mtp : MarkovTraceProduct)
    (d k : Fin (mtp.n - 1) → ℕ)
    (hw : ∀ i, d i ≤ 2 * k i + 1)
    (hbudget : (∑ i, (2 * k i + 1)) ≤ mtp.n ^ 2 - 1) :
    (∑ i, d i) ≤ mtp.n ^ 2 - 1 :=
  le_trans (Finset.sum_le_sum (fun i _ => hw i)) hbudget

end

end QOU.Hecke
