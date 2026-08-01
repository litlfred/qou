import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Logic.Equiv.Basic
import Mathlib.Data.Fintype.Perm
import Mathlib.Tactic

/-!
# Chord diagrams

A **chord diagram** of degree `n` is a way to pair up `2n` marked points
on an oriented circle by `n` chords.  Modelled here as a **fixed-point-free
involution** `pairing : Perm (Fin (2 * n))`: `pairing i` is the point joined
to `i` by a chord, `pairing (pairing i) = i` (involution) and `pairing i ≠ i`
(no chord joins a point to itself).

Chord diagrams are the target of the *symbol* map of a finite-type
(Vassiliev) invariant, and the space they span — modulo the one- and
four-term relations (`FourTermRelation.lean`) — carries the weight systems
(`WeightSystem.lean`).  This file builds only the combinatorial object and
its symmetric-group action; no invariant theory lives here.

## Main definitions

* `ChordDiagram n` — a fixed-point-free involution on `Fin (2 * n)`.
* `ChordDiagram.degree` — the number of chords, `= n` by construction.
* `ChordDiagram.conj` — the `Perm (Fin (2*n))`-action by conjugation
  (relabelling the marked points); the surgeries in the 1T/4T relators are
  expressed through it.
* `ChordDiagram.oneChord` — the unique degree-1 diagram (single chord).

## References

* Bar-Natan, *On the Vassiliev knot invariants*, Topology 34 (1995) 423–472,
  <https://doi.org/10.1016/0040-9383(95)93237-2>.
* Chmutov–Duzhin–Mostovoy, *Introduction to Vassiliev Knot Invariants*,
  Cambridge University Press, 2012.
-/

namespace QOU.KnotTheory.Vassiliev

open Equiv

/-- A **chord diagram** of degree `n`: a fixed-point-free involution on the
`2 * n` marked points `Fin (2 * n)`.  `pairing i` is the endpoint joined to
`i`; involutivity makes the chords well-defined and fixed-point-freeness
forbids a chord from both ending at the same point. -/
structure ChordDiagram (n : ℕ) where
  /-- The pairing permutation: sends each marked point to its chord partner. -/
  pairing : Perm (Fin (2 * n))
  /-- The pairing is an involution: applying it twice returns the point. -/
  involutive : Function.Involutive pairing
  /-- No point is its own partner (every chord has two distinct endpoints). -/
  fixedPointFree : ∀ i, pairing i ≠ i

namespace ChordDiagram

variable {n : ℕ}

/-- Two chord diagrams are equal once their pairings agree (the remaining
fields are propositions, equal by proof irrelevance). -/
@[ext] theorem ext {D E : ChordDiagram n} (h : D.pairing = E.pairing) : D = E := by
  cases D; cases E; cases h; rfl

/-- The chord partner of a marked point. -/
def partner (D : ChordDiagram n) (i : Fin (2 * n)) : Fin (2 * n) := D.pairing i

@[simp] theorem partner_partner (D : ChordDiagram n) (i : Fin (2 * n)) :
    D.partner (D.partner i) = i := D.involutive i

theorem partner_ne (D : ChordDiagram n) (i : Fin (2 * n)) : D.partner i ≠ i :=
  D.fixedPointFree i

/-- The **degree** of a chord diagram is its number of chords, `= n` by
construction (there are `2 n` endpoints, paired two at a time). -/
def degree (_D : ChordDiagram n) : ℕ := n

@[simp] theorem degree_eq (D : ChordDiagram n) : D.degree = n := rfl

/-! ## Symmetric-group action by relabelling

Relabelling the `2 n` marked points by `g : Perm (Fin (2*n))` carries a chord
diagram to another chord diagram: the new pairing is the conjugate
`g ∘ pairing ∘ g⁻¹`.  Conjugation preserves both the involution and
fixed-point-free properties, so this is well-defined.  Chord surgeries used in
the relators (`FourTermRelation.lean`) are instances of this action. -/

/-- Conjugation preserves involutivity. -/
theorem involutive_conj (σ : Perm (Fin (2 * n))) (hσ : Function.Involutive σ)
    (g : Perm (Fin (2 * n))) : Function.Involutive (g * σ * g⁻¹) := by
  intro i
  simp only [Perm.mul_apply, Perm.inv_apply_self]
  rw [hσ (g⁻¹ i), Perm.apply_inv_self]

/-- Conjugation preserves fixed-point-freeness. -/
theorem fixedPointFree_conj (σ : Perm (Fin (2 * n))) (hσ : ∀ i, σ i ≠ i)
    (g : Perm (Fin (2 * n))) : ∀ i, (g * σ * g⁻¹) i ≠ i := by
  intro i h
  rw [Perm.mul_apply, Perm.mul_apply] at h
  -- h : g (σ (g⁻¹ i)) = i, so σ (g⁻¹ i) = g⁻¹ i, contradicting hσ.
  have h2 : σ (g⁻¹ i) = g⁻¹ i := by
    apply g.injective
    rw [Perm.apply_inv_self]
    exact h
  exact hσ (g⁻¹ i) h2

/-- The relabelling action of `g : Perm (Fin (2*n))` on a chord diagram. -/
def conj (D : ChordDiagram n) (g : Perm (Fin (2 * n))) : ChordDiagram n where
  pairing := g * D.pairing * g⁻¹
  involutive := involutive_conj D.pairing D.involutive g
  fixedPointFree := fixedPointFree_conj D.pairing D.fixedPointFree g

@[simp] theorem conj_pairing (D : ChordDiagram n) (g : Perm (Fin (2 * n))) :
    (D.conj g).pairing = g * D.pairing * g⁻¹ := rfl

/-- The identity relabelling fixes a chord diagram. -/
@[simp] theorem conj_one (D : ChordDiagram n) : D.conj 1 = D := by
  apply ChordDiagram.ext; simp

/-- The relabelling action is a right action of the symmetric group. -/
theorem conj_mul (D : ChordDiagram n) (g h : Perm (Fin (2 * n))) :
    D.conj (h * g) = (D.conj g).conj h := by
  apply ChordDiagram.ext
  simp only [conj_pairing, mul_inv_rev, mul_assoc]

/-- Conjugation preserves degree (it is always `n`). -/
@[simp] theorem degree_conj (D : ChordDiagram n) (g : Perm (Fin (2 * n))) :
    (D.conj g).degree = D.degree := rfl

end ChordDiagram

/-! ## The single-chord diagram (degree 1)

`Fin 2` has a unique fixed-point-free involution, `swap 0 1`; it is the only
degree-1 chord diagram and witnesses that `ChordDiagram 1` is inhabited. -/

/-- The unique degree-1 chord diagram: the single chord on `Fin 2`. -/
def ChordDiagram.oneChord : ChordDiagram 1 where
  pairing := Equiv.swap (0 : Fin 2) 1
  involutive := fun x => Equiv.swap_apply_self 0 1 x
  fixedPointFree := by
    intro i
    fin_cases i <;> decide

instance : Inhabited (ChordDiagram 1) := ⟨ChordDiagram.oneChord⟩

end QOU.KnotTheory.Vassiliev
