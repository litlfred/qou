/-
# The face-size obstruction: `H_4`'s universal map is 4-gonal

`qou-brfy` asks whether the Floyd-Hatcher / Gueritaud layering theorem --
which turns a *word* into an *ideal triangulation* -- transfers from the
modular group `H_3 = PSL(2,Z)` to the Hecke group `H_4`, since Bring's
surface is presented by the latter.

It does not, and the reason is a face-size invariant rather than a failed
search.  The layering machinery consumes a **diagonal flip in a triangulated
surface**: one flip is dual to exactly one ideal tetrahedron.  Kattan-Singerman
(`kattan2024`, arXiv:2402.08782v1) record the relevant contrast as the premise
of their own paper -- the Farey map is the universal **triangular** map, while
Bring's surface comes from the universal **4-gonal** map with `H_4` replacing
the modular group, of type `{5,4}`: quadrilateral faces, vertices of valency 5.

A quadrangulation has no diagonal to exchange, so the theorem has no input.
This file supplies the arithmetic that turns that qualitative statement into a
counted one:

* `regularMap_edge_relation` -- the Euler identity for a regular map, over any
  commutative ring (no ordering, no division, no archimedean structure: §7c).
* `bring_VEF` -- its specialisation to Bring's `{5,4}` map at genus 4, giving
  `V = 24`, `E = 60`, `F = 30`.
* `bring_aut_orientation_preserving` -- `2E = 120 = |S_5|`, matching the
  paper's Theorem 2.1.  Recorded because `4E = 240` (the flag count, i.e. the
  full group *including* reflections) is the easy error here; an earlier draft
  of the companion probe made it.
* `diagonalRefinements_card` -- a choice of one diagonal per quadrilateral face
  is exactly a function `Fin F -> Fin 2`, so there are `2 ^ F` of them.
* `bring_refinement_count` -- hence `2 ^ 30 = 1073741824` refinements of
  Bring's map.

**Scope.**  This is a scope-(a) negative with a *proved obstruction to the
specific transfer*, in the AGENTS.md sense: it shows the Floyd-Hatcher /
Gueritaud route does not carry from `H_3` to `H_4` because its input does not
exist there.  It is NOT a scope-(b) structural exclusion -- it does not rule
out some other `H_4 -> 3-manifold` construction, and says nothing about
Bring's role elsewhere in the framework.

The relevance of the final count is the anti-fit discipline: manufacturing a
triangulation costs ~10^9 free binary choices, and selecting among them to
match a target is *selection against the target*, which is fitting even though
no continuous parameter is tuned.

-- Ref: [kattan2024] https://arxiv.org/abs/2402.08782
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

namespace QOU.Brings

/-! ## The Euler identity for a regular map -/

/-- **Euler identity for a regular map.**  For a map on a closed orientable
surface of genus `g` whose faces are all `p`-gons and whose vertices all have
valency `q`, the incidence counts `p * F = 2 * E` (each face has `p` edges,
each edge borders two faces) and `q * V = 2 * E` (each vertex has `q` edge-ends,
each edge has two ends) combine with `V - E + F = 2 - 2 * g` to give

  `E * (2 * p + 2 * q - p * q) = p * q * (2 - 2 * g)`.

Stated over an arbitrary commutative ring: the content is the elimination of
`V` and `F`, which needs no ordering and no division.  (§7c -- do not
specialise to `Real` or even `Int` here; the Bring instance below does that.) -/
theorem regularMap_edge_relation {R : Type*} [CommRing R] (p q V E F g : R)
    (hface : p * F = 2 * E) (hvert : q * V = 2 * E)
    (heuler : V - E + F = 2 - 2 * g) :
    E * (2 * p + 2 * q - p * q) = p * q * (2 - 2 * g) := by
  linear_combination p * q * heuler - p * hvert - q * hface

/-! ## Bring's surface: the `{5,4}` map at genus 4 -/

/-- **Bring's map has 24 vertices, 60 edges and 30 quadrilateral faces.**

Kattan-Singerman Theorem 2.1: the unique regular map of type `{5,4}` of genus
4, with automorphism group `S_5`.  Their convention (stated explicitly in the
paper) is that `{5,4}` means *faces are quadrilaterals and vertices have
valency 5* -- so `p = 4`, `q = 5`.

Given the two incidence relations and Euler's formula at `g = 4`, the counts
are forced.  Note the hypotheses are exactly those of
`regularMap_edge_relation`; nothing about hyperbolic geometry enters. -/
theorem bring_VEF (V E F : ℤ)
    (hface : (4 : ℤ) * F = 2 * E) (hvert : (5 : ℤ) * V = 2 * E)
    (heuler : V - E + F = 2 - 2 * 4) :
    V = 24 ∧ E = 60 ∧ F = 30 := by
  refine ⟨by linarith, by linarith, by linarith⟩

/-- **The paper's 120 automorphisms is `2E`, not `4E`.**

For a regular map the orientation-preserving automorphism group acts simply
transitively on the `2E` *directed* edges, so `|Aut^+| = 2E`.  The flag count
is `4E`, which counts the full group *including* reflections.

At `E = 60` these are `120` and `240`; Kattan-Singerman's `|S_5| = 120` is the
orientation-preserving count.  Both are recorded so the distinction cannot be
re-lost -- an earlier draft of the companion probe asserted `4E = 120`, which
is false, and the probe's own check caught it. -/
theorem bring_aut_orientation_preserving :
    2 * (60 : ℤ) = 120 ∧ 4 * (60 : ℤ) = 240 ∧ (120 : ℤ) ≠ 240 := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-! ## The cost of manufacturing a triangulation -/

/-- **A diagonal-refinement of a quadrangulation is a choice of one of the two
diagonals in each face**, i.e. a function from the faces to a two-element set;
there are `2 ^ F` of them.

This is the step that prices the transfer.  The layering theorem wants a
triangulated surface; a quadrangulation can be turned into one, but only by
making an independent binary choice per face, and this counts those choices. -/
theorem diagonalRefinements_card (F : ℕ) :
    Fintype.card (Fin F → Fin 2) = 2 ^ F := by
  rw [Fintype.card_fun, Fintype.card_fin, Fintype.card_fin]

/-- **Bring's map admits `2 ^ 30 = 1073741824` diagonal refinements.**

With `F = 30` quadrilateral faces, manufacturing a triangulation to feed the
layering machinery costs ~10^9 free binary choices.  Selecting among them to
reproduce a target is *selection against the target* -- fitting under the
NO-FITTING directive, with no continuous parameter tuned. -/
theorem bring_refinement_count :
    Fintype.card (Fin 30 → Fin 2) = 1073741824 := by
  rw [diagonalRefinements_card]
  norm_num

/-- **The face sizes differ, which is the whole obstruction.**

`H_3`'s universal map is triangular (`p = 3`); `H_4`'s is 4-gonal (`p = 4`).
A diagonal flip -- the move dual to one ideal tetrahedron -- is defined for the
former and not the latter.  Trivial as arithmetic; recorded because it is the
load-bearing step, and because stating it makes the two `p` values explicit
rather than leaving them in prose. -/
theorem universal_map_face_sizes_differ : (3 : ℕ) ≠ 4 := by norm_num

/-- **Concrete Euler-characteristic check for Bring's `{5,4}` map (`bean qou-0jcd`):**
    `V - E + F = 24 - 60 + 30 = -6 = 2 - 2 · 4`. -/
theorem bring_euler_characteristic_from_VEF :
    (24 : ℤ) - 60 + 30 = -6 ∧ 2 - 2 * (4 : ℤ) = -6 := by
  decide

/-- **Doubling of diagonal-refinement choices per added quadrilateral face (`bean qou-0jcd`).** -/
theorem diagonalRefinements_card_succ (F : ℕ) :
    Fintype.card (Fin (F + 1) → Fin 2) = 2 * Fintype.card (Fin F → Fin 2) := by
  rw [diagonalRefinements_card (F + 1), diagonalRefinements_card F, pow_succ']

end QOU.Brings
