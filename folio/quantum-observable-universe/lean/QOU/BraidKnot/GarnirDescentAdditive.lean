import QOU.BraidKnot.GarnirTableau
import QOU.BraidKnot.RowStandardTableau

/-!
# Length additivity holds at *every* descent node

This closes the length half of Mathas' Lemma 3.13.

## What is proved

For a **row-standard** tableau `t` and **any** descent node `(i,j)` of it,

  `invSet (garnirPerm i j) ⊆ invSet (dOf t)`

which by `length_dOf_smul_eq_add_iff` (`QOU.BraidKnot.TableauPerm`, from
`QOU.Hecke.Inversions.length_mul_eq_add_iff`) is exactly

  `ℓ(d(t)) = ℓ(d(g_{ij})) + ℓ(w)`   where `t = w • g_{ij}`.

## No minimality hypothesis

Mathas' statement, and the corpus probe built from it, ask only that *some*
descent node work, and the probe reports that the *first* one always does.  The
proof below shows the condition holds at **every** descent node, so no
minimality, ordering, or choice is needed anywhere.

That is visible once the containment is unfolded.  The rotation's inversions are
exactly the pairs (label in row `i` from column `j` on, label in row `i+1` up to
column `j`), and `dOf t` sends a reference label to `t`'s entry in that cell, so
the containment says precisely

  `t(i,c) > t(i+1,c')`   for all `c ≥ j`, `c' ≤ j`,

and row-standardness chains it out of the single descent inequality:

  `t(i,c) ≥ t(i,j) > t(i+1,j) ≥ t(i+1,c')`.

Corroborated before it was proved:
`computations/hecke/garnir_all_descent_nodes_probe.py` finds additivity at
**3685 of 3685** descent nodes over the 1789 row-standard non-standard tableaux
with `n = 3..6`.

## What is still open

Mathas 3.13 also asserts that a non-standard row-standard tableau *has* a descent
node.  That is a separate statement (a failure of column-standardness produces
one) and is not proved here.
-/

open Equiv

namespace QOU.BraidKnot.GarnirDescentAdditive

open QOU.BraidKnot.IntervalRotate QOU.BraidKnot.TableauPerm
open QOU.BraidKnot.GarnirTableau QOU.BraidKnot.RowStandardTableau
open QOU.Hecke.Inversions

variable {μ : YoungDiagram}

/-! ### Which pairs a rotation inverts -/

/-- **The inversions of an interval rotation are exactly the "unwrapped × wrapped"
pairs.**  With block `[a, a+m)` and shift `k < m`, a pair is inverted only if the
smaller entry lies in the part that does not wrap and the larger in the part that
does. -/
theorem mem_invSet_intervalRotate {n a m k : ℕ} (hb : a + m ≤ n) (hk : k < m)
    {p : Fin n × Fin n} (hp : p ∈ invSet (intervalRotate a m k hb)) :
    (a ≤ (p.1 : ℕ) ∧ (p.1 : ℕ) < a + (m - k)) ∧
      (a + (m - k) ≤ (p.2 : ℕ) ∧ (p.2 : ℕ) < a + m) := by
  obtain ⟨hlt, hinv⟩ := mem_invSet.1 hp
  have hlt' : (p.1 : ℕ) < (p.2 : ℕ) := hlt
  have hinv' : ((intervalRotate a m k hb p.2 : Fin n) : ℕ)
      < ((intervalRotate a m k hb p.1 : Fin n) : ℕ) := hinv
  rw [intervalRotate_apply, intervalRotate_apply] at hinv'
  have hm : 0 < m := lt_of_le_of_lt (Nat.zero_le k) hk
  have hsplit : ∀ x : ℕ, ¬(a ≤ x ∧ x < a + m) → (x < a ∨ a + m ≤ x) := by
    intro x hx
    by_contra hc
    push_neg at hc
    exact hx ⟨hc.1, hc.2⟩
  by_cases h1 : a ≤ (p.1 : ℕ) ∧ (p.1 : ℕ) < a + m
  · by_cases h2 : a ≤ (p.2 : ℕ) ∧ (p.2 : ℕ) < a + m
    · -- both inside: the shift must wrap for `p.2` and not for `p.1`
      rw [rotNat_of_mem h1, rotNat_of_mem h2] at hinv'
      have e1 : ((p.1 : ℕ) - a + k) % m = if (p.1 : ℕ) - a + k < m
          then (p.1 : ℕ) - a + k else (p.1 : ℕ) - a + k - m := by
        split_ifs with hc
        · exact Nat.mod_eq_of_lt hc
        · rw [Nat.mod_eq_sub_mod (by omega)]
          exact Nat.mod_eq_of_lt (by omega)
      have e2 : ((p.2 : ℕ) - a + k) % m = if (p.2 : ℕ) - a + k < m
          then (p.2 : ℕ) - a + k else (p.2 : ℕ) - a + k - m := by
        split_ifs with hc
        · exact Nat.mod_eq_of_lt hc
        · rw [Nat.mod_eq_sub_mod (by omega)]
          exact Nat.mod_eq_of_lt (by omega)
      rw [e1, e2] at hinv'
      split_ifs at hinv' with hA hB hB <;> omega
    · -- `p.1` inside, `p.2` outside: then `p.2 ≥ a + m`, above the whole image
      exfalso
      rw [rotNat_of_mem h1, rotNat_of_not_mem h2] at hinv'
      have hmod := Nat.mod_lt ((p.1 : ℕ) - a + k) hm
      rcases hsplit _ h2 with hc | hc <;> omega
  · -- `p.1` outside: then `p.1 < a`, but every image is `≥ a`
    exfalso
    rw [rotNat_of_not_mem h1] at hinv'
    rcases hsplit _ h1 with hc | hc
    · by_cases h2 : a ≤ (p.2 : ℕ) ∧ (p.2 : ℕ) < a + m
      · rw [rotNat_of_mem h2] at hinv'; omega
      · rw [rotNat_of_not_mem h2] at hinv'; omega
    · by_cases h2 : a ≤ (p.2 : ℕ) ∧ (p.2 : ℕ) < a + m
      · omega
      · rw [rotNat_of_not_mem h2] at hinv'; omega

/-! ### Reading a reference label off its cell -/

/-- The inverse of `refTab_symm_apply`: the label `rowPrefix μ i + c` sits in cell
`(i, c)`. -/
theorem refTab_apply_rowPrefix {i c : ℕ} (h : (i, c) ∈ μ)
    (hlt : QOU.BraidKnot.rowPrefix μ i + c < Specht.nOf μ) :
    refTab μ ⟨QOU.BraidKnot.rowPrefix μ i + c, hlt⟩
      = ⟨(i, c), (YoungDiagram.mem_cells _).2 h⟩ := by
  have hsym : ((refTab μ).symm ⟨(i, c), (YoungDiagram.mem_cells _).2 h⟩ : ℕ)
      = QOU.BraidKnot.rowPrefix μ i + c := refTab_symm_apply h
  have : (refTab μ).symm ⟨(i, c), (YoungDiagram.mem_cells _).2 h⟩
      = ⟨QOU.BraidKnot.rowPrefix μ i + c, hlt⟩ := Fin.ext hsym
  rw [← this, Equiv.apply_symm_apply]

/-- `dOf t` reads off `t`'s label in the cell that carries the given reference
label. -/
theorem dOf_apply_rowPrefix {t : Specht.Tableau μ} {i c : ℕ} (h : (i, c) ∈ μ)
    (hlt : QOU.BraidKnot.rowPrefix μ i + c < Specht.nOf μ) :
    dOf t ⟨QOU.BraidKnot.rowPrefix μ i + c, hlt⟩
      = t.symm ⟨(i, c), (YoungDiagram.mem_cells _).2 h⟩ := by
  rw [dOf_apply, refTab_apply_rowPrefix h hlt]

/-! ### The chain out of row-standardness -/

/-- Along a row, later column means larger label. -/
theorem le_of_col_le {t : Specht.Tableau μ} (hrs : IsRowStandard t) {i c c' : ℕ}
    (hc : (i, c) ∈ μ) (hc' : (i, c') ∈ μ) (hle : c ≤ c') :
    (t.symm ⟨(i, c), (YoungDiagram.mem_cells _).2 hc⟩ : Fin (Specht.nOf μ))
      ≤ t.symm ⟨(i, c'), (YoungDiagram.mem_cells _).2 hc'⟩ := by
  rcases eq_or_lt_of_le hle with rfl | hlt
  · exact le_refl _
  · refine le_of_lt (hrs _ _ ?_ ?_)
    · show ((t (t.symm _) : μ.cells) : ℕ × ℕ).1 = ((t (t.symm _) : μ.cells) : ℕ × ℕ).1
      simp
    · show ((t (t.symm _) : μ.cells) : ℕ × ℕ).2 < ((t (t.symm _) : μ.cells) : ℕ × ℕ).2
      simpa using hlt

/-! ### The theorem -/

/-- **Length additivity holds at every descent node.**

For a row-standard `t` and *any* descent node `(i,j)`, every inversion of the
Garnir permutation is an inversion of `d(t)` — which by
`length_dOf_smul_eq_add_iff` is exactly `ℓ(d(t)) = ℓ(d(g_{ij})) + ℓ(w)`.

No minimality hypothesis: the argument never compares `(i,j)` with any other
descent node. -/
theorem invSet_garnirPerm_subset_of_descent
    {t : Specht.Tableau μ} (hrs : IsRowStandard t)
    {i j : ℕ} (h : (i + 1, j) ∈ μ) (hd : IsDescentNode t i j) :
    invSet (garnirPerm i j h) ⊆ invSet (dOf t) := by
  obtain ⟨hcell, hdesc⟩ := hd
  intro p hp
  have hk : j + 1 < μ.rowLen i + 1 := garnir_shift_lt h
  have hbnd := garnir_bound h
  have hj1 : j < μ.rowLen (i + 1) := YoungDiagram.mem_iff_lt_rowLen.1 h
  -- locate `p.1` in row `i` and `p.2` in row `i+1`
  obtain ⟨⟨hA1, hA2⟩, ⟨hB1, hB2⟩⟩ :=
    mem_invSet_intervalRotate (a := QOU.BraidKnot.rowPrefix μ i + j)
      (m := μ.rowLen i + 1) (k := j + 1) hbnd hk hp
  have hpref : QOU.BraidKnot.rowPrefix μ (i + 1)
      = QOU.BraidKnot.rowPrefix μ i + μ.rowLen i := QOU.BraidKnot.rowPrefix_succ μ i
  -- normalise the block width: `omega` holds `rowLen i + 1 - (j+1)` as one opaque
  -- atom, so `hpref` never reaches the constraint set until this is rewritten
  have hjle : j ≤ μ.rowLen i := by omega
  have hsub : μ.rowLen i + 1 - (j + 1) = μ.rowLen i - j := by omega
  rw [hsub] at hA2 hB1
  have hA1' : QOU.BraidKnot.rowPrefix μ i + j ≤ (p.1 : ℕ) := hA1
  have hA2' : (p.1 : ℕ) < QOU.BraidKnot.rowPrefix μ (i + 1) := by rw [hpref]; omega
  have hB1' : QOU.BraidKnot.rowPrefix μ (i + 1) ≤ (p.2 : ℕ) := by rw [hpref]; omega
  have hB2' : (p.2 : ℕ) < QOU.BraidKnot.rowPrefix μ (i + 1) + j + 1 := by
    rw [hpref]; omega
  have hp1lt := p.1.isLt
  have hp2lt := p.2.isLt
  -- name the column indices by an explicit equation rather than `set`, which
  -- hides the relation from `omega`
  obtain ⟨c, hc⟩ : ∃ c, (p.1 : ℕ) = QOU.BraidKnot.rowPrefix μ i + c :=
    ⟨(p.1 : ℕ) - QOU.BraidKnot.rowPrefix μ i, by omega⟩
  obtain ⟨c', hc'⟩ : ∃ c', (p.2 : ℕ) = QOU.BraidKnot.rowPrefix μ (i + 1) + c' :=
    ⟨(p.2 : ℕ) - QOU.BraidKnot.rowPrefix μ (i + 1), by omega⟩
  have hcj : j ≤ c := by omega
  have hcL : c < μ.rowLen i := by omega
  have hc'j : c' ≤ j := by omega
  have hmemc : (i, c) ∈ μ := YoungDiagram.mem_iff_lt_rowLen.2 hcL
  have hmemc' : (i + 1, c') ∈ μ := YoungDiagram.mem_iff_lt_rowLen.2 (by omega)
  have hmemj : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) h
  -- rewrite the two indices in reference-label form
  have hlt1 : QOU.BraidKnot.rowPrefix μ i + c < Specht.nOf μ := by omega
  have hlt2 : QOU.BraidKnot.rowPrefix μ (i + 1) + c' < Specht.nOf μ := by omega
  have e1 : p.1 = ⟨QOU.BraidKnot.rowPrefix μ i + c, hlt1⟩ := Fin.ext hc
  have e2 : p.2 = ⟨QOU.BraidKnot.rowPrefix μ (i + 1) + c', hlt2⟩ := Fin.ext hc'
  refine mem_invSet.2 ⟨?_, ?_⟩
  · show (p.1 : ℕ) < (p.2 : ℕ)
    omega
  · rw [e1, e2, dOf_apply_rowPrefix hmemc, dOf_apply_rowPrefix hmemc']
    -- the chain: t(i+1,c') ≤ t(i+1,j) < t(i,j) ≤ t(i,c)
    have hup : (t.symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hmemj⟩ : Fin (Specht.nOf μ))
        ≤ t.symm ⟨(i, c), (YoungDiagram.mem_cells _).2 hmemc⟩ :=
      le_of_col_le hrs hmemj hmemc hcj
    have hdown : (t.symm ⟨(i + 1, c'), (YoungDiagram.mem_cells _).2 hmemc'⟩ :
        Fin (Specht.nOf μ))
        ≤ t.symm ⟨(i + 1, j), (YoungDiagram.mem_cells _).2 hcell⟩ :=
      le_of_col_le hrs hmemc' hcell hc'j
    exact lt_of_le_of_lt hdown (lt_of_lt_of_le hdesc hup)

end QOU.BraidKnot.GarnirDescentAdditive
