/-
# The τ-assignment at every rank — cell restriction and the parabolic naturality square

The general-rank leg of the assignment functor, closing the shape left
open by the tower square (#4291): a `TauAssignmentData` exists at EVERY
rank — on the length-rule module of any Coxeter system with a marked
`M i j = 3` pair — and at every parabolic containing the pair, with the
restriction naturality square along the abstract tower inclusion
`iotaPar`. Everything factors STRUCTURALLY through the base-rung
assignment (`tauAssignmentH3`, merged #4102) via restriction to the
trivial-coset cell:

* **`cellRestrict`** — restriction of a state to the six cell elements
  of the `{i,j}` parabolic (the trivial coset of the transversal).
* **`monodromyN_cellRestrict`** — the cell is a `q = i` Jordan
  sub-datum: restriction intertwines the full-group nilpotent with the
  H3-cell nilpotent (via the right-multiplication tables and the cell
  lengths, both provided by the transversal under the collapsed residue
  `σᵢ ≠ σⱼ`).
* **`tauAssignmentAtRank`** — the assignment at every rank:
  `toFun := tauAssignmentH3.toFun ∘ cellRestrict`. All four laws
  TRANSPORT from the base rung — nothing is re-proved.
* **`tauAssignmentParabolic`** — the same construction on the parabolic
  subtype for any `J' ⊇ {i, j}`.
* **`tauAssignment_iotaPar_natural` / `_bar`** — THE NATURALITY SQUARE:
  the full-group assignment restricted along `iotaPar` IS the parabolic
  assignment, for every parabolic containing the pair. The merged
  concrete ι₃₄ square is the `A₂ ⊂ A₃` shadow of this statement.

HONESTY (STRICT): sorry-free; hypotheses are exactly `M i j = 3` and
the collapsed Tits residue `σᵢ ≠ σⱼ` (plus `{i,j} ⊆ J'` for the
parabolic leg). What remains open of the assignment functor: canonicity
(the construction depends on the marked pair; different pairs give
different assignments) and the Tits residue itself at non-concrete
systems. Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/
import QOU.Machinery.CoxeterTitsResidueCollapse
import QOU.Machinery.CoxeterParabolicInclusion
import QOU.Machinery.HeckeTauAssignmentH3

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

variable (i j : B)

/-! ## Cell restriction and the Jordan sub-datum -/

/-- Restriction of a state to the six cell elements of the `{i,j}`
parabolic — the trivial coset of the transversal. -/
noncomputable def cellRestrict (v : W → ℂ) : Fin 6 → ℂ :=
  fun k => v (cellElem3 cs i j k)

lemma cellRestrict_add (v v' : W → ℂ) :
    cellRestrict cs i j (v + v')
      = cellRestrict cs i j v + cellRestrict cs i j v' := rfl

/-- The cell lengths equal the `descentH3σ₀` table, under the collapsed
residue. -/
lemma length_cellElem3 (hm : M i j = 3) (hne : σ i ≠ σ j) (k : Fin 6) :
    ℓ (cellElem3 cs i j k) = descentH3σ₀.len k := by
  have hred := isReduced_iji_of_simple_ne cs i j hm hne
  have h1 : ℓ (cellElem3 cs i j k) = (cellWord3 i j k).length :=
    cellWord3_isReduced cs i j hred k
  rw [h1, cellWord3_length]

/-- **The cell is a `q = i` Jordan sub-datum**: restriction intertwines
the full-group monodromy nilpotent with the H3-cell nilpotent. -/
lemma monodromyN_cellRestrict (hm : M i j = 3) (hne : σ i ≠ σ j)
    (v : W → ℂ) :
    cellRestrict cs i j (monodromyN (descentRight cs i) v)
      = monodromyN descentH3σ₀ (cellRestrict cs i j v) := by
  funext k
  show monodromyN (descentRight cs i) v (cellElem3 cs i j k)
    = monodromyN descentH3σ₀ (cellRestrict cs i j v) k
  unfold monodromyN mulStep descentRight cellRestrict
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul,
    cell3_mul_simple_i cs i j, length_cellElem3 cs i j hm hne]

/-- **The τ-assignment at every rank**: the base-rung assignment
composed with cell restriction; all four laws transport. -/
noncomputable def tauAssignmentAtRank (hm : M i j = 3) (hne : σ i ≠ σ j) :
    TauAssignmentData (descentRight cs i) where
  toFun v := tauAssignmentH3.toFun (cellRestrict cs i j v)
  toFunBar w := tauAssignmentH3.toFunBar (cellRestrict cs i j w)
  map_add v v' := by
    rw [cellRestrict_add, tauAssignmentH3.map_add]
  kills_nilpotent v := by
    show tauAssignmentH3.toFun
        (cellRestrict cs i j (monodromyN (descentRight cs i) v)) = 0
    rw [monodromyN_cellRestrict cs i j hm hne,
      tauAssignmentH3.kills_nilpotent]
  rho_compat v u := by
    show star (tauAssignmentH3.toFun (cellRestrict cs i j v) u)
      = tauAssignmentH3.toFunBar
          (cellRestrict cs i j (fun x => star (v x))) u
    rw [tauAssignmentH3.rho_compat]
    rfl

/-! ## The parabolic assignment and the naturality square -/

variable (J' : Set B)

/-- The cell lies in every parabolic containing the pair. -/
lemma cellElem3_mem_parabolic (hij : i ∈ J') (hjj : j ∈ J') (k : Fin 6) :
    cellElem3 cs i j k ∈ parabolic cs J' := by
  apply wordProd_mem_parabolic
  intro l hl
  have hmem := cellWord3_mem i j k l hl
  rw [Set.mem_insert_iff, Set.mem_singleton_iff] at hmem
  rcases hmem with rfl | rfl <;> assumption

/-- Cell restriction on the parabolic subtype. -/
noncomputable def cellRestrictPar (hij : i ∈ J') (hjj : j ∈ J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) : Fin 6 → ℂ :=
  fun k => v ⟨cellElem3 cs i j k, cellElem3_mem_parabolic cs i j J' hij hjj k⟩

lemma cellRestrictPar_add (hij : i ∈ J') (hjj : j ∈ J')
    (v v' : {w : W // w ∈ parabolic cs J'} → ℂ) :
    cellRestrictPar cs i j J' hij hjj (v + v')
      = cellRestrictPar cs i j J' hij hjj v
        + cellRestrictPar cs i j J' hij hjj v' := rfl

/-- The parabolic-level Jordan sub-datum. -/
lemma monodromyN_cellRestrictPar (hm : M i j = 3) (hne : σ i ≠ σ j)
    (hij : i ∈ J') (hjj : j ∈ J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) :
    cellRestrictPar cs i j J' hij hjj
        (monodromyN (descentParabolic cs J' hij) v)
      = monodromyN descentH3σ₀ (cellRestrictPar cs i j J' hij hjj v) := by
  funext k
  show monodromyN (descentParabolic cs J' hij) v
      ⟨cellElem3 cs i j k, _⟩
    = monodromyN descentH3σ₀ (cellRestrictPar cs i j J' hij hjj v) k
  unfold monodromyN mulStep descentParabolic cellRestrictPar
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul,
    cell3_mul_simple_i cs i j, length_cellElem3 cs i j hm hne]

/-- **The τ-assignment on every parabolic containing the pair.** -/
noncomputable def tauAssignmentParabolic (hm : M i j = 3)
    (hne : σ i ≠ σ j) (hij : i ∈ J') (hjj : j ∈ J') :
    TauAssignmentData (descentParabolic cs J' hij) where
  toFun v := tauAssignmentH3.toFun (cellRestrictPar cs i j J' hij hjj v)
  toFunBar w := tauAssignmentH3.toFunBar (cellRestrictPar cs i j J' hij hjj w)
  map_add v v' := by
    rw [cellRestrictPar_add, tauAssignmentH3.map_add]
  kills_nilpotent v := by
    show tauAssignmentH3.toFun (cellRestrictPar cs i j J' hij hjj
        (monodromyN (descentParabolic cs J' hij) v)) = 0
    rw [monodromyN_cellRestrictPar cs i j J' hm hne hij hjj,
      tauAssignmentH3.kills_nilpotent]
  rho_compat v u := by
    show star (tauAssignmentH3.toFun
        (cellRestrictPar cs i j J' hij hjj v) u)
      = tauAssignmentH3.toFunBar
          (cellRestrictPar cs i j J' hij hjj (fun x => star (v x))) u
    rw [tauAssignmentH3.rho_compat]
    rfl

/-- Restriction along the tower inclusion is parabolic restriction. -/
lemma cellRestrict_iotaPar (hij : i ∈ J') (hjj : j ∈ J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) :
    cellRestrict cs i j (iotaPar cs J' v)
      = cellRestrictPar cs i j J' hij hjj v := by
  funext k
  show iotaPar cs J' v (cellElem3 cs i j k) = _
  unfold iotaPar cellRestrictPar
  rw [dif_pos (cellElem3_mem_parabolic cs i j J' hij hjj k)]

/-- **THE NATURALITY SQUARE AT EVERY RANK**: the full-group assignment
restricted along the abstract tower inclusion IS the parabolic
assignment, for every parabolic containing the marked pair. The merged
concrete ι₃₄ square is the `A₂ ⊂ A₃` shadow. -/
theorem tauAssignment_iotaPar_natural (hm : M i j = 3) (hne : σ i ≠ σ j)
    (hij : i ∈ J') (hjj : j ∈ J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) :
    (tauAssignmentAtRank cs i j hm hne).toFun (iotaPar cs J' v)
      = (tauAssignmentParabolic cs i j J' hm hne hij hjj).toFun v := by
  show tauAssignmentH3.toFun (cellRestrict cs i j (iotaPar cs J' v)) = _
  rw [cellRestrict_iotaPar cs i j J' hij hjj]
  rfl

/-- The ρ-partner square. -/
theorem tauAssignment_iotaPar_natural_bar (hm : M i j = 3)
    (hne : σ i ≠ σ j) (hij : i ∈ J') (hjj : j ∈ J')
    (w : {w : W // w ∈ parabolic cs J'} → ℂ) :
    (tauAssignmentAtRank cs i j hm hne).toFunBar (iotaPar cs J' w)
      = (tauAssignmentParabolic cs i j J' hm hne hij hjj).toFunBar w := by
  show tauAssignmentH3.toFunBar (cellRestrict cs i j (iotaPar cs J' w)) = _
  rw [cellRestrict_iotaPar cs i j J' hij hjj]
  rfl

end QOU.Machinery.CoxeterParabolic
