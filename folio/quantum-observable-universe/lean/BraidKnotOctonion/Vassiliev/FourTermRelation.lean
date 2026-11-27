import BraidKnotOctonion.Vassiliev.ChordDiagram
import Mathlib.LinearAlgebra.Finsupp.Defs
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Tactic

/-!
# The one- and four-term relations on chord diagrams

Weight systems are linear functionals on the free module spanned by chord
diagrams that vanish on the **one-term (1T, framing-independence)** and
**four-term (4T)** relators.  This file builds:

* `CDModule R n` — the free `R`-module on `ChordDiagram n`.
* `oneTermSubmodule` — spanned by diagrams carrying an isolated (adjacent-
  endpoint) chord; the 1T / framing-independence relation.
* `fourTermSubmodule` — Bar-Natan's four-term relation: sliding one endpoint
  across both ends of another chord gives cancelling differences.
* `relationsSubmodule` — their join `1T ⊔ 4T`; the reduced diagram space `𝒜`
  (`WeightSystem.lean`) is the quotient by it.

## Honest scope of the 4T encoding

The 1T submodule is a faithful, elementary encoding of framing independence
(a chord with adjacent endpoints is genuinely isolated).  The 4T submodule is
Bar-Natan's relation written through endpoint re-insertion (`gapPerm`).  It was
corrected on 2026-11-27: the previous commutator-shaped encoding collapsed the
reduced space to zero (`FourTermEncodingCollapse.lean`).  The current form is
checked in degree 2 (`FourTermDegreeTwo.lean`), where the crossed two-chord
diagram survives; agreement with Bar-Natan's 4T in every degree is a reading of
the definition, not a theorem.  The structural results of `WeightSystem.lean`
are proved for an arbitrary relations submodule.

## References

* Bar-Natan, *On the Vassiliev knot invariants*, Topology 34 (1995) 423–472.
* Chmutov–Duzhin–Mostovoy, *Introduction to Vassiliev Knot Invariants*, CUP 2012.
* Kohno, *Monodromy representations of braid groups and Yang–Baxter equations*,
  Ann. Inst. Fourier 37 (1987) 139–160.
-/

namespace QOU.KnotTheory.Vassiliev

open scoped Classical
open Equiv Finsupp

variable (R : Type*) [CommRing R] {n : ℕ}

/-- The free `R`-module on chord diagrams of degree `n`. -/
abbrev CDModule (n : ℕ) := ChordDiagram n →₀ R

namespace CDModule

variable {R}

/-- The basis vector of a single chord diagram. -/
noncomputable def of (D : ChordDiagram n) : CDModule R n := Finsupp.single D 1

@[simp] theorem of_apply_self (D : ChordDiagram n) : (of (R := R) D) D = 1 := by
  simp [of]

end CDModule

/-! ## The one-term (framing-independence) relation

A chord whose two endpoints are cyclically adjacent (`pairing i = i + 1`) is
isolated: no other chord crosses it.  Framing independence sends any diagram
carrying such a chord to zero. -/

/-- `D` carries an *isolated (adjacent-endpoint) chord*: some marked point is
paired with its cyclic successor `finRotate (2n) i`. -/
def HasAdjacentChord (D : ChordDiagram n) : Prop :=
  ∃ i : Fin (2 * n), D.pairing i = finRotate (2 * n) i

/-- The 1T relators: basis vectors of diagrams with an isolated chord. -/
def oneTermRelators : Set (CDModule R n) :=
  {v | ∃ D : ChordDiagram n, HasAdjacentChord D ∧ v = CDModule.of D}

/-- The one-term (framing-independence) submodule. -/
def oneTermSubmodule : Submodule R (CDModule R n) :=
  Submodule.span R (oneTermRelators R)

/-! ## The four-term relation (Bar-Natan)

Put the moving endpoint `r` of a chord at the last marked point `2n − 1`, and let `gap k` be
the diagram obtained by re-inserting `r` just before the point that sits at position `k` among
the other `2n − 1` points (`gap (2n − 1)` is `D` itself).  For a second chord `{p, q}` with
`p, q ≠ 2n − 1`, sliding `r` across `p` is `⟨gap (p+1)⟩ − ⟨gap p⟩`, and across `q` is
`⟨gap (q+1)⟩ − ⟨gap q⟩`.  Bar-Natan's 4T relation says the two slides cancel:

`⟨gap (p+1)⟩ − ⟨gap p⟩ + ⟨gap (q+1)⟩ − ⟨gap q⟩ = 0`.

Every rotation of such a relator is also imposed, so `r` may sit at any marked point.
(Bar-Natan, *On the Vassiliev knot invariants*, §1.2; Chmutov–Duzhin–Mostovoy §4.1.)

**History.** Until 2026-11-27 this section imposed the commutator-shaped relator
`⟨D⟩ − ⟨D·sᵢ⟩ − ⟨D·sⱼ⟩ + ⟨D·sᵢsⱼ⟩` for every pair of adjacent transpositions, unrelated to
the chords of `D`.  That relation makes every weight system of positive degree zero when `2`
is a unit (`FourTermEncodingCollapse.lean`, bean `qou-bgq9`).  The present form is checked
against degree 2 in `FourTermDegreeTwo.lean`, where it leaves the crossed diagram non-zero. -/

/-- The adjacent transposition of marked points `i` and its cyclic successor. -/
def adjTransp (i : Fin (2 * n)) : Perm (Fin (2 * n)) :=
  Equiv.swap i (finRotate (2 * n) i)

/-- The transposition of positions `a` and `b` of `Fin N` (identity if either is out of range). -/
def natSwap (N a b : ℕ) : Perm (Fin N) :=
  if h : a < N ∧ b < N then Equiv.swap ⟨a, h.1⟩ ⟨b, h.2⟩ else 1

/-- `gapPerm N k = s_k s_{k+1} ⋯ s_{N−2}`: moves the last point to position `k` and shifts the
points at `k, …, N − 2` up by one. -/
def gapPerm (N k : ℕ) : Perm (Fin N) :=
  ((List.range (N - 1 - k)).map fun j => natSwap N (k + j) (k + j + 1)).prod

/-- A 4T configuration: `p` and its partner `q` both differ from the last marked point. -/
def FourTermAdmissible (D : ChordDiagram n) (p : Fin (2 * n)) : Prop :=
  p.val + 1 < 2 * n ∧ (D.pairing p).val + 1 < 2 * n

/-- Bar-Natan's four-term relator for the chord `{p, D p}`, the endpoint at the last marked
point, and the rotation `finRotate ^ m`. -/
noncomputable def fourTermRelator (D : ChordDiagram n) (p m : Fin (2 * n)) : CDModule R n :=
  let g : ℕ → ChordDiagram n := fun k =>
    D.conj (finRotate (2 * n) ^ (m : ℕ) * gapPerm (2 * n) k)
  CDModule.of (g (p.val + 1)) - CDModule.of (g p.val)
    + CDModule.of (g ((D.pairing p).val + 1)) - CDModule.of (g (D.pairing p).val)

/-- The set of all four-term relators. -/
def fourTermRelators : Set (CDModule R n) :=
  {v | ∃ (D : ChordDiagram n) (p m : Fin (2 * n)),
    FourTermAdmissible D p ∧ v = fourTermRelator R D p m}

/-- The four-term submodule. -/
def fourTermSubmodule : Submodule R (CDModule R n) :=
  Submodule.span R (fourTermRelators R)

/-- The full relations submodule imposed on weight systems: 1T together with 4T. -/
def relationsSubmodule : Submodule R (CDModule R n) :=
  oneTermSubmodule R ⊔ fourTermSubmodule R

/-! ## Structural facts (relation-agnostic) -/

theorem oneTermSubmodule_le_relations :
    oneTermSubmodule R ≤ relationsSubmodule (R := R) (n := n) :=
  le_sup_left

theorem fourTermSubmodule_le_relations :
    fourTermSubmodule R ≤ relationsSubmodule (R := R) (n := n) :=
  le_sup_right

/-- Each four-term relator lies in the relations submodule. -/
theorem fourTermRelator_mem_relations (D : ChordDiagram n) (p m : Fin (2 * n))
    (h : FourTermAdmissible D p) :
    fourTermRelator R D p m ∈ relationsSubmodule (R := R) (n := n) := by
  apply fourTermSubmodule_le_relations
  exact Submodule.subset_span ⟨D, p, m, h, rfl⟩

/-- The basis vector of an isolated-chord diagram lies in the relations
submodule (framing independence). -/
theorem of_mem_relations_of_hasAdjacentChord
    {D : ChordDiagram n} (h : HasAdjacentChord D) :
    CDModule.of D ∈ relationsSubmodule (R := R) (n := n) := by
  apply oneTermSubmodule_le_relations
  exact Submodule.subset_span ⟨D, h, rfl⟩

end QOU.KnotTheory.Vassiliev
