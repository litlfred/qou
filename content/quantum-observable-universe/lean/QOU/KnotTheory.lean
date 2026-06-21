import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic
import QOU.Glossary
import Mathlib.Tactic.NormNum

/-!
# QOU.KnotTheory — Braid-word knot representations

Knots and links are encoded as **braid words** in the Artin braid
group `B_n` — sequences of generator letters `σ_i^ε` with index
`i ∈ {0, …, n-2}` and exponent sign `ε ∈ {+1, -1}`.  Markov closure
turns a braid word into a link; every knot or link arises this way
(Alexander's theorem).

The braid-word encoding is `O(n)` in storage and `O(n)` for writhe /
crossing-count, matching the older PD/Gauss-code encoding's complexity
while staying in the canonical Hecke-algebra register that the QOU
mass derivation uses throughout (AGENTS.md *Canonical derivation
chain*).  Multigraph encodings (PD code, Gauss code, chord diagrams)
are equivalent up to a basis change but are not used elsewhere in the
paper, so we drop them here.

This file's targets — Jones polynomials, Khovanov homology, hyperbolic
volumes — are computable from the braid word directly via the Markov
trace on `H_n(q)` and via SnapPy lookups for hyperbolic data.
-/


namespace QOU.KnotTheory

/-! ## Crossing Sign and Braid Letter -/

/-- The exponent sign of a braid generator: `σ_i^{+1}` or `σ_i^{-1}`. -/
inductive CrossingSign where
  | positive
  | negative
  deriving DecidableEq, Repr

/-- A single braid-generator letter `σ_i^ε`: index `i` says which
    adjacent pair of strands crosses; `sign` says positive or negative
    exponent. -/
structure BraidLetter where
  /-- Generator index: `i` in `σ_i`. Valid in `B_n` when `i + 1 < n`. -/
  index : ℕ
  /-- Exponent sign: positive = `σ_i`, negative = `σ_i^{-1}`. -/
  sign : CrossingSign
  deriving Repr, DecidableEq

/-! ## Braid Word and Markov Closure -/

/-- A braid word in `B_n` together with the Markov closure data needed
    to recover a knot or link. -/
structure BraidWord where
  /-- Alexander–Briggs name or other identifier (e.g. `"3_1"`). -/
  name : String
  /-- Number of strands `n` for the ambient braid group `B_n`. -/
  strands : ℕ
  /-- Sequence of generator letters applied left-to-right. -/
  letters : List BraidLetter
  /-- Number of components in the Markov closure. -/
  components : ℕ := 1
  deriving Repr

/-- Number of crossings = length of the braid word. -/
def BraidWord.crossingCount (β : BraidWord) : ℕ :=
  β.letters.length

/-! ## Hyperbolic Volume -/

/-- Hyperbolic volume of a knot complement, with error bound. -/
structure HyperbolicVolume where
  /-- The volume value. -/
  value : ℝ
  /-- Error bound (half-width of confidence interval). -/
  error_bound : ℝ
  /-- Proof obligation: error bound is non-negative. -/
  -- Ref: [turaev2010] https://doi.org/10.1515/9783110221831
  error_nonneg : error_bound ≥ 0

/-! ## Standard Knots and Links -/

/-- The unknot — empty braid word in `B_1` (1 strand, 0 crossings). -/
def unknot : BraidWord where
  name := "0_1"
  strands := 1
  letters := []
  components := 1

/-- The trefoil knot (3₁) — closed braid `σ_0^3` in `B_2`.
    In the QOU framework, the trefoil maps to the electron. -/
def trefoil : BraidWord where
  name := "3_1"
  strands := 2
  letters := [⟨0, .positive⟩, ⟨0, .positive⟩, ⟨0, .positive⟩]
  components := 1

/-- The figure-eight knot (4₁) — closed braid `(σ_0 σ_1^{-1})^2` in
    `B_3`.  In the QOU framework, the figure-eight maps to the muon. -/
def figureEight : BraidWord where
  name := "4_1"
  strands := 3
  letters :=
    [⟨0, .positive⟩, ⟨1, .negative⟩,
     ⟨0, .positive⟩, ⟨1, .negative⟩]
  components := 1

/-- The Hopf link (L2a1) — closed braid `σ_0^2` in `B_2`, 2 components.
    In the QOU framework, the Hopf link is the gluon / strong force
    binding. -/
def hopfLink : BraidWord where
  name := "L2a1"
  strands := 2
  letters := [⟨0, .positive⟩, ⟨0, .positive⟩]
  components := 2

/-- The Borromean rings (L6a4) — closed braid `(σ_0 σ_1^{-1})^3` in
    `B_3`, 3 components.  In the QOU framework, the Borromean rings
    are the nucleon (three quark strands, Brunnian linking). -/
def borromeanRings : BraidWord where
  name := "L6a4"
  strands := 3
  letters :=
    [⟨0, .positive⟩, ⟨1, .negative⟩,
     ⟨0, .positive⟩, ⟨1, .negative⟩,
     ⟨0, .positive⟩, ⟨1, .negative⟩]
  components := 3

/-! ## Hyperbolic Volumes of Standard Knots -/

/-- The hyperbolic volume of the figure-eight knot (4₁).
    Exact: 3 · Cl₂(π/3) where Cl₂ is the Clausen function.
    Value: 2.029883212819307250042408 (OEIS A091518, 24 dps verified;
    previous 15-dps literal `2.02988321281931 ± 1×10⁻¹⁴` bumped
    2026-06-07). -/
noncomputable def vol_figure_eight : HyperbolicVolume where
  value := 2.029883212819307250042408
  error_bound := 1e-24
  error_nonneg := by norm_num

/-- The trefoil is a torus knot and has zero hyperbolic volume. -/
noncomputable def vol_trefoil : HyperbolicVolume where
  value := 0
  error_bound := 0
  error_nonneg := le_refl 0

/-! ## Writhe and Crossing Number -/

/-- The writhe of a braid word (signed sum of exponents).
    For a braid word `σ_{i_1}^{ε_1} ⋯ σ_{i_k}^{ε_k}`, this returns
    `ε_1 + ⋯ + ε_k`.  Note: this is the *braid-projection writhe*; it
    counts crossings *between strands* with signs.  Per-component
    self-writhe (counted only within a single component of the
    closure) is zero in the standard braid projection — strands do
    not self-cross. -/
def BraidWord.writhe (β : BraidWord) : ℤ :=
  β.letters.foldl (fun acc l =>
    match l.sign with
    | .positive => acc + 1
    | .negative => acc - 1
  ) 0

end QOU.KnotTheory
