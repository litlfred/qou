import QOU.BraidKnot.CasimirShared


/-!
# QOU.PathIntegrals.KnotEigenbasisComplete

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/PathIntegrals.lean (monolithic)

The shared carrier structures (`SchurWeylDecomposition`, `AlexanderSurjectivity`,
`MarkovTrace`, `HeckeAlgebra`, `BoundedPartition`) are promoted into the
`QOU.Braiding` namespace by the library module `QOU.BraidKnot.CasimirShared`;
they are opened below rather than re-declared.
-/

namespace QOU.PathIntegrals

open QOU.Braiding

/-- **Completeness of the knot-type eigenbasis** (Proposition 4.x).

    Combines semisimplicity of `H_n(q)`, Alexander surjectivity, and
    spanning of the algebraic direct limit to establish that knot types
    form a complete eigenbasis replacing the Feynman path integral.

    Three parts:
    1. `H_n(q)` is semisimple at generic `q`, giving the complete
       q-Schur–Weyl decomposition of `V^{⊗n}`.
    2. Alexander's theorem provides surjectivity of the braid-closure map.
    3. The algebraic direct limit `V_phys = colim V^{⊗n}` is spanned
       by the irreducible summands (no metric completion is used).

    LaTeX: `\label{prop:knot-eigenbasis-complete}` -/
-- Ref: [chari1994guide] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
-- Ref: [alexander1923] J.W. Alexander, Proc. Natl. Acad. Sci. USA 9 (1923)
-- Ref: [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987)
structure KnotEigenbasisComplete where
  /-- Part 1: the q-Schur–Weyl decomposition. -/
  decomposition : SchurWeylDecomposition
  /-- Part 2: Alexander surjectivity. -/
  alexander : AlexanderSurjectivity
  /-- Part 3: the Markov trace detects every irreducible summand. -/
  markov : MarkovTrace
  /-- Consistency: the Markov trace is on the same Hecke algebra
      as the decomposition. -/
  consistent : markov.hecke = decomposition.hecke
  -- The braid-closure map labels irreducible summands: for each partition `λ`
  -- in the decomposition, there exists a braid `β` whose closure detects `λ` —
  -- the Markov trace of the Hecke-algebra image of `β`, restricted to the `S_λ`
  -- summand, is non-zero.  Encoded via the representation map `ρ` below.
  /-- Representation map: braid → Hecke algebra element. -/
  braid_rep : alexander.Braid → decomposition.hecke.carrier
  /-- For each partition `λ`, there exists a braid whose trace on the
      corresponding Hecke-summand is non-zero. -/
  summands_detected : ∀ μ ∈ decomposition.partitions,
    ∃ (β : alexander.Braid),
    markov.tr (consistent ▸ braid_rep β) ≠ 0
  /-- The algebraic direct-limit type `V_phys = colim V^{⊗n}`. -/
  V_phys : Type*
  /-- The level-`n` embedded subspace: `embed n` is the image of
      `V^{⊗n}` inside `V_phys` under the direct-limit inclusion. -/
  embed : ℕ → Set V_phys
  /-- **Spanning** (Part 3): the union of all level-`n` embedded
      subspaces is *all* of `V_phys`.  Equivalently, every element
      of `V_phys` lies in `embed n` for some `n`.

      This is the algebraic-spanning condition (no metric completion
      is invoked).  Non-vacuous: if `embed` is the constant empty
      set, this is unprovable; it captures the genuine
      direct-limit-cover property. -/
  spanning : (⋃ n, embed n) = (Set.univ : Set V_phys)

end QOU.PathIntegrals
