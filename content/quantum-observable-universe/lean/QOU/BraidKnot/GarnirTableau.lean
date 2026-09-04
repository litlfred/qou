import QOU.BraidKnot.TableauPerm
import QOU.BraidKnot.IntervalRotate

/-!
# The Garnir tableau `g_{ij}`, and descent nodes

Mathas' Lemma 3.13 says: for a row-standard non-standard `t` there are a Garnir
tableau `g` and `w` with `t = g · w` and `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`.  This file
supplies the two objects the statement names — `g_{ij}` and the descent nodes
that index the `(i,j)` to use.

## `g_{ij}` is a rotation

`refTab_symm_apply` (`QOU.BraidKnot.TableauPerm`) puts the label
`rowPrefix μ i + j` in cell `(i,j)` of the reference tableau, and the companion
probe measures that `g_{ij}` rotates the label block
`[rowPrefix μ i + j, rowPrefix μ (i+1) + j]` by `j+1` — 108 Garnir tableaux over
all partitions of `n = 3..7`, zero mismatches.  So `g_{ij}` is defined here as
`garnirPerm • t^μ` with `garnirPerm` an `intervalRotate`, and **bijectivity is
free**: nothing has to be shown surjective.

The block has width `rowLen μ i + 1` — the tail of row `i` from column `j`, plus
the head of row `i+1` up to column `j`.

## Scope

Mathas 3.13 is **not** proved here.  What this adds is that both of its objects
are now definable, and `length_garnir_eq_add_iff` reduces its length condition
to inversion containment against a *concrete* `g`.  Which descent node to pick
is still open — measured, the first always works (1789/1789 at `n = 3..6`), but
that is evidence, not a proof.
-/

open Equiv

namespace QOU.BraidKnot.GarnirTableau

open QOU.BraidKnot.IntervalRotate QOU.BraidKnot.TableauPerm

variable {μ : YoungDiagram}

/-! ### The Garnir permutation -/

/-- The rotated block `[a, a+m)` fits inside the labels: `a + m = b + 1 ≤ n`. -/
theorem garnir_bound {i j : ℕ} (h : (i + 1, j) ∈ μ) :
    (QOU.BraidKnot.rowPrefix μ i + j) + (μ.rowLen i + 1) ≤ Specht.nOf μ := by
  have h1 : QOU.BraidKnot.rowPrefix μ (i + 1 + 1) ≤ μ.cells.card :=
    QOU.BraidKnot.rowPrefix_succ_le_card μ h
  have h2 : j < μ.rowLen (i + 1) := YoungDiagram.mem_iff_lt_rowLen.1 h
  have e1 : QOU.BraidKnot.rowPrefix μ (i + 1)
      = QOU.BraidKnot.rowPrefix μ i + μ.rowLen i := QOU.BraidKnot.rowPrefix_succ μ i
  have e2 : QOU.BraidKnot.rowPrefix μ (i + 1 + 1)
      = QOU.BraidKnot.rowPrefix μ (i + 1) + μ.rowLen (i + 1) :=
    QOU.BraidKnot.rowPrefix_succ μ (i + 1)
  show _ ≤ μ.cells.card
  omega

/-- **The Garnir permutation** `d(g_{ij})`: rotate the label block
`[rowPrefix μ i + j, rowPrefix μ (i+1) + j]` by `j+1`, fixing every other label. -/
def garnirPerm (i j : ℕ) (h : (i + 1, j) ∈ μ) : Perm (Fin (Specht.nOf μ)) :=
  intervalRotate (QOU.BraidKnot.rowPrefix μ i + j) (μ.rowLen i + 1) (j + 1) (garnir_bound h)

/-- **The Garnir tableau** `g_{ij}`, as the reference tableau moved by that rotation.
Bijectivity is inherited from `intervalRotate`; nothing is proved surjective here. -/
noncomputable def garnirTab (i j : ℕ) (h : (i + 1, j) ∈ μ) : Specht.Tableau μ :=
  garnirPerm i j h • refTab μ

/-- `d(g_{ij})` is the Garnir permutation — the two definitions agree. -/
@[simp] theorem dOf_garnirTab (i j : ℕ) (h : (i + 1, j) ∈ μ) :
    dOf (garnirTab i j h) = garnirPerm i j h :=
  dOf_smul_refTab _

/-- Labels outside the block are untouched by `g_{ij}`. -/
theorem garnirPerm_eq_self {i j : ℕ} (h : (i + 1, j) ∈ μ) {x : Fin (Specht.nOf μ)}
    (hx : ¬(QOU.BraidKnot.rowPrefix μ i + j ≤ (x : ℕ) ∧
          (x : ℕ) < QOU.BraidKnot.rowPrefix μ i + j + (μ.rowLen i + 1))) :
    garnirPerm i j h x = x :=
  intervalRotate_eq_self _ hx

/-! ### Non-vacuity: `g_{ij}` is never the reference tableau

The rotation amount is `j + 1` and the block width is `rowLen μ i + 1`.  Since
`(i+1, j) ∈ μ` forces `j < rowLen μ (i+1) ≤ rowLen μ i`, the shift is strictly
between `0` and the width — so it never reduces to the identity, for any `μ`,
`i`, `j`.  This is what stops every result below from being vacuous. -/

/-- The rotation amount is a proper shift: `0 < j + 1 < rowLen μ i + 1`. -/
theorem garnir_shift_lt {i j : ℕ} (h : (i + 1, j) ∈ μ) : j + 1 < μ.rowLen i + 1 := by
  have h2 : j < μ.rowLen (i + 1) := YoungDiagram.mem_iff_lt_rowLen.1 h
  have h3 : μ.rowLen (i + 1) ≤ μ.rowLen i := μ.rowLen_anti i (i + 1) (Nat.le_succ i)
  omega

/-- **`g_{ij}` genuinely moves something**: the Garnir permutation is never `1`. -/
theorem garnirPerm_ne_one {i j : ℕ} (h : (i + 1, j) ∈ μ) : garnirPerm i j h ≠ 1 := by
  intro hone
  have hlt : j + 1 < μ.rowLen i + 1 := garnir_shift_lt h
  have hbound := garnir_bound h
  set a := QOU.BraidKnot.rowPrefix μ i + j with ha
  have hax : a < Specht.nOf μ := by omega
  have happ : (garnirPerm i j h) ⟨a, hax⟩ = ⟨a, hax⟩ := by rw [hone]; rfl
  have hval : ((garnirPerm i j h) ⟨a, hax⟩ : ℕ)
      = rotNat a (μ.rowLen i + 1) (j + 1) a := rfl
  rw [happ] at hval
  rw [rotNat_of_mem ⟨le_refl a, by omega⟩] at hval
  simp only [Nat.sub_self, Nat.zero_add, Nat.mod_eq_of_lt hlt] at hval
  omega

/-- Hence the Garnir tableau differs from the reference tableau. -/
theorem garnirTab_ne_refTab {i j : ℕ} (h : (i + 1, j) ∈ μ) :
    garnirTab i j h ≠ refTab μ := by
  intro hEq
  refine garnirPerm_ne_one h ?_
  have := congrArg dOf hEq
  rwa [dOf_garnirTab, dOf_refTab] at this

/-! ### Descent nodes -/

/-- `(i, j)` is a **descent node** of `t`: `(i+1, j)` is a cell and the label in
`(i, j)` exceeds the label in `(i+1, j)` — i.e. column-strictness fails there.

A standard tableau has none; Mathas 3.13 picks its Garnir tableau at one. -/
def IsDescentNode (t : Specht.Tableau μ) (i j : ℕ) : Prop :=
  ∃ h : (i + 1, j) ∈ μ,
    (t.symm ⟨(i + 1, j), (YoungDiagram.mem_cells _).2 h⟩ : Fin (Specht.nOf μ))
      < t.symm ⟨(i, j), (YoungDiagram.mem_cells _).2
          (μ.up_left_mem (Nat.le_succ i) (le_refl j) h)⟩

/-- The reference tableau has no descent node: it is row-superstandard, so labels
increase down every column. -/
theorem not_isDescentNode_refTab (i j : ℕ) : ¬ IsDescentNode (refTab μ) i j := by
  rintro ⟨h, hlt⟩
  have hij : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) h
  have hb : ((refTab μ).symm ⟨(i + 1, j), (YoungDiagram.mem_cells _).2 h⟩ : ℕ)
      = QOU.BraidKnot.rowPrefix μ (i + 1) + j := refTab_symm_apply h
  have ha : ((refTab μ).symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩ : ℕ)
      = QOU.BraidKnot.rowPrefix μ i + j := refTab_symm_apply hij
  have e1 : QOU.BraidKnot.rowPrefix μ (i + 1)
      = QOU.BraidKnot.rowPrefix μ i + μ.rowLen i := QOU.BraidKnot.rowPrefix_succ μ i
  have := Fin.lt_def.1 hlt
  omega

/-! ### Mathas' length condition against a concrete `g` -/

/-- **The length half of Mathas 3.13, against the actual Garnir tableau.**

For `t = w • g_{ij}`, length is additive exactly when `w` undoes none of
`g_{ij}`'s inversions.  Both sides are now concrete: the right-hand side is a
containment between inversion sets of explicit permutations, with no lengths and
no reduced words in it. -/
theorem length_garnir_eq_add_iff {n : ℕ} (hn : Specht.nOf μ = n + 1)
    (i j : ℕ) (h : (i + 1, j) ∈ μ) (w : Perm (Fin (Specht.nOf μ))) :
    (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length
          (toFinSucc hn (dOf (w • garnirTab i j h)))
        = (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length (toFinSucc hn w)
          + (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length
              (toFinSucc hn (garnirPerm i j h))
      ↔ QOU.Hecke.Inversions.invSet (toFinSucc hn (garnirPerm i j h))
          ⊆ QOU.Hecke.Inversions.invSet (toFinSucc hn (dOf (w • garnirTab i j h))) := by
  have := length_dOf_smul_eq_add_iff hn w (garnirTab i j h)
  rwa [dOf_garnirTab] at this

end QOU.BraidKnot.GarnirTableau
