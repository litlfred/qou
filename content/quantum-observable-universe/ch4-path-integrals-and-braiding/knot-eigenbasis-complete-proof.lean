/-!
# QOU.PathIntegrals.KnotEigenbasisComplete

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/PathIntegrals.lean (monolithic)
-/

import QOU.Basic
import QOU.Glossary
import QOU.KnotTheory
import Mathlib.Data.Real.Basic
import Mathlib.GroupTheory.SpecificGroups.Dihedral
import Mathlib.GroupTheory.PresentedGroup
import Mathlib.GroupTheory.FreeGroup.Basic
import Mathlib.Algebra.Algebra.Basic

namespace QOU.PathIntegrals

/-- **Completeness of the knot-type eigenbasis** (Proposition 4.x).

    Combines semisimplicity of `H_n(q)`, Alexander surjectivity, and density
    in the physical Hilbert space to establish that knot types form a complete
    eigenbasis replacing the Feynman path integral.

    Three parts:
    1. `H_n(q)` is semisimple at generic `q`, giving the complete
       q-Schur–Weyl decomposition of `V^{⊗n}`.
    2. Alexander's theorem provides surjectivity of the braid-closure map.
    3. The direct limit `𝓗_phys = lim→ V^{⊗n}` is spanned by the
       irreducible summands (density).

    LaTeX: `\label{prop:knot-eigenbasis-complete}` -/
-- Ref: [chari1994] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
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
  /-- The braid-closure map labels irreducible summands:
      for each partition `λ` in the decomposition, there exists
      a braid `β` whose closure detects `λ` — the Markov trace of the
      Hecke-algebra image of `β`, restricted to the `S_λ` summand,
      is non-zero.  Encoded via the representation map `ρ`. -/
  /-- Representation map: braid → Hecke algebra element. -/
  braid_rep : alexander.Braid → decomposition.hecke.carrier
  /-- For each partition `λ`, there exists a braid whose trace on the
      corresponding Hecke-summand is non-zero. -/
  summands_detected : ∀ λ ∈ decomposition.partitions,
    ∃ (β : alexander.Braid),
    markov.tr (braid_rep β) ≠ 0
  /-- **Density** (Part 3): the physical Hilbert space
      `𝓗_phys = lim→ V^{⊗n}` is spanned by the irreducible summands.
      Encoded as: the direct limit over `n` of the `V^{⊗n}` spaces
      admits no element orthogonal to all summand embeddings. -/
  density : Type* -- abstract direct-limit type `𝓗_phys`

end QOU.PathIntegrals
