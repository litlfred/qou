/-
# Coherence groupoid, edges two and three — conjugation coherent, pair-swap obstructed

Continues the coherence program on the τ-assignment family
(`tauAssignmentAtRank`), after the diagram-symmetry edge
(`tauAssignment_diagram_coherent`) and the strict-independence
refutation (`tauAssignment_pair_dependent`). Two results, one per
remaining edge class:

**W-conjugation edges are COHERENT (positive, general).** If an
element `u` conjugates one marked pair onto another —
`u σᵢ u⁻¹ = σᵢ'`, `u σⱼ u⁻¹ = σⱼ'` — then the six-element cell
transports along the inner automorphism
(`cellElem3_conj`), and the assignment at the target pair is the
pullback of the assignment at the source pair
(`tauAssignment_conj_coherent`, `_bar`), exactly parallel to the
diagram edge. Simple-distinctness transports for free
(`simple_ne_conj`).

**The pair-swap edge is OBSTRUCTED at the isotypic target (negative,
general, proved).** The swap `(i, j) ↦ (j, i)` DOES transport the cell —
`cellElem3_swap`: the `(j,i)`-cell is the `(i,j)`-cell re-indexed by the
involution `0↔0, 1↔2, 3↔4, 5↔5`, the last entry closing by the braid
relation. But no transition map on the isotypic slot completes the
square: `tauAssignment_swap_no_target_transition` shows there is **no
function whatsoever** `T : (Fin 4 → ℂ) → (Fin 4 → ℂ)` with
`τ_{(j,i)} = T ∘ τ_{(i,j)}`, because a state in the kernel of the
`(i,j)`-assignment (indicator mix of `1` and `σᵢ` with coefficients
`−I, 1`) survives the `(j,i)`-assignment. So the swap transition lives
one level up — on the six-cell (an index permutation) — and provably
does not descend through the base-rung `H₃` assignment.

Resulting picture of the coherence groupoid: objects are marked pairs;
**coherent** morphism classes proved so far are diagram symmetries and
W-conjugations (transition = pullback along the induced automorphism);
the swap is proved NOT to be a coherent edge at the target level. Still
open: assembling the proved edges into a single functor object
(pairs-groupoid → assignments), and whether any *non-pullback* notion
of transition could accommodate the swap.

HONESTY (STRICT): sorry-free, no axioms, no `decide` beyond none —
every statement is general-rank over an arbitrary Coxeter system. The
negative is a proved exclusion of target-side transitions for the swap
edge (a genuine (b)-scope exclusion: the witness computation IS the
invariant); it does not exclude cell-level or source-side
reformulations, which is exactly what `cellElem3_swap` provides.
Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeTauAssignmentCoherence

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List Complex
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "πW" => cs.wordProd
local prefix:100 "σW" => cs.simple

/-- Simple reflections are nontrivial (length 1 vs length 0). -/
lemma simple_ne_one' (i : B) : σW i ≠ 1 := by
  intro h
  have hl := cs.length_simple i
  rw [h, cs.length_one] at hl
  exact Nat.zero_ne_one hl

/-! ## Edge two: W-conjugation is coherent -/

/-- Simple-distinctness transports along a conjugation of pairs. -/
theorem simple_ne_conj {u : W} {i j i' j' : B}
    (hci : u * σW i * u⁻¹ = σW i') (hcj : u * σW j * u⁻¹ = σW j')
    (hne : σW i ≠ σW j) : σW i' ≠ σW j' := by
  intro h
  rw [← hci, ← hcj] at h
  exact hne (mul_left_cancel (mul_right_cancel h))

/-- The cell transports along the inner automorphism of a
pair-conjugating element. -/
lemma cellElem3_conj {u : W} {i j i' j' : B}
    (hci : u * σW i * u⁻¹ = σW i') (hcj : u * σW j * u⁻¹ = σW j')
    (k : Fin 6) :
    cellElem3 cs i' j' k = u * cellElem3 cs i j k * u⁻¹ := by
  fin_cases k
  · show πW [] = u * πW [] * u⁻¹
    rw [wordProd_nil, mul_one, mul_inv_cancel]
  · show πW [i'] = u * πW [i] * u⁻¹
    rw [wordProd_singleton, wordProd_singleton, ← hci]
  · show πW [j'] = u * πW [j] * u⁻¹
    rw [wordProd_singleton, wordProd_singleton, ← hcj]
  · show πW [j', i'] = u * πW [j, i] * u⁻¹
    rw [wordProd_ij cs j' i', wordProd_ij cs j i, ← hci, ← hcj]
    group
  · show πW [i', j'] = u * πW [i, j] * u⁻¹
    rw [wordProd_ij cs i' j', wordProd_ij cs i j, ← hci, ← hcj]
    group
  · show πW [i', j', i'] = u * πW [i, j, i] * u⁻¹
    rw [wordProd_iji cs i' j', wordProd_iji cs i j, ← hci, ← hcj]
    group

/-- **W-conjugation edges are coherent**: the assignment at the
conjugated pair is the pullback of the assignment at the source pair
along the inner automorphism. -/
theorem tauAssignment_conj_coherent {u : W} {i j i' j' : B}
    (hci : u * σW i * u⁻¹ = σW i') (hcj : u * σW j * u⁻¹ = σW j')
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M i' j' = 3) (hne' : σW i' ≠ σW j') (v : W → ℂ) :
    (tauAssignmentAtRank cs i' j' hm' hne').toFun v
      = (tauAssignmentAtRank cs i j hm hne).toFun
          (fun x => v (u * x * u⁻¹)) := by
  show tauAssignmentH3.toFun (cellRestrict cs i' j' v)
    = tauAssignmentH3.toFun
        (cellRestrict cs i j (fun x => v (u * x * u⁻¹)))
  congr 1
  funext k
  show v (cellElem3 cs i' j' k) = v (u * cellElem3 cs i j k * u⁻¹)
  rw [cellElem3_conj cs hci hcj k]

/-- The conjugate `H^{0,1}` partner square. -/
theorem tauAssignment_conj_coherent_bar {u : W} {i j i' j' : B}
    (hci : u * σW i * u⁻¹ = σW i') (hcj : u * σW j * u⁻¹ = σW j')
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M i' j' = 3) (hne' : σW i' ≠ σW j') (w : W → ℂ) :
    (tauAssignmentAtRank cs i' j' hm' hne').toFunBar w
      = (tauAssignmentAtRank cs i j hm hne).toFunBar
          (fun x => w (u * x * u⁻¹)) := by
  show tauAssignmentH3.toFunBar (cellRestrict cs i' j' w)
    = tauAssignmentH3.toFunBar
        (cellRestrict cs i j (fun x => w (u * x * u⁻¹)))
  congr 1
  funext k
  show w (cellElem3 cs i' j' k) = w (u * cellElem3 cs i j k * u⁻¹)
  rw [cellElem3_conj cs hci hcj k]

/-! ## Edge three: the pair swap — cell-level transport … -/

/-- The index involution realizing the pair swap on the six-cell. -/
def swap6 : Fin 6 → Fin 6 := ![0, 2, 1, 4, 3, 5]

/-- The `(j,i)`-cell is the `(i,j)`-cell re-indexed by `swap6`; the
longest entry closes by the braid relation. -/
lemma cellElem3_swap {i j : B} (hm : M i j = 3) (k : Fin 6) :
    cellElem3 cs j i k = cellElem3 cs i j (swap6 k) := by
  fin_cases k
  · rfl
  · rfl
  · rfl
  · rfl
  · rfl
  · show πW [j, i, j] = πW [i, j, i]
    rw [wordProd_iji cs j i, wordProd_iji cs i j, braid3 cs i j hm]

/-- Cell restriction intertwines the swap with the index involution. -/
lemma cellRestrict_swap {i j : B} (hm : M i j = 3) (v : W → ℂ) :
    cellRestrict cs j i v = fun k => cellRestrict cs i j v (swap6 k) := by
  funext k
  show v (cellElem3 cs j i k) = v (cellElem3 cs i j (swap6 k))
  rw [cellElem3_swap cs hm k]

/-! ## … and the target-level obstruction -/

/-- **The swap edge admits NO transition map on the isotypic target**:
there is no function `T` — linear or otherwise — with
`τ_{(j,i)} = T ∘ τ_{(i,j)}`. The witness state (coefficients `−I` at
the identity and `1` at `σᵢ`) lies in the kernel of the
`(i,j)`-assignment but not of the `(j,i)`-assignment, so the swap
transition exists only at cell level (`cellRestrict_swap`) and provably
does not descend. -/
theorem tauAssignment_swap_no_target_transition {i j : B}
    (hm : M i j = 3) (hm' : M j i = 3) (hne : σW i ≠ σW j) :
    ¬ ∃ T : (Fin 4 → ℂ) → (Fin 4 → ℂ), ∀ v : W → ℂ,
      (tauAssignmentAtRank cs j i hm' hne.symm).toFun v
        = T ((tauAssignmentAtRank cs i j hm hne).toFun v) := by
  rintro ⟨T, hT⟩
  -- distinctness of the relevant cell elements from `1` and `σᵢ`
  have hi1 : σW i ≠ 1 := simple_ne_one' cs i
  have hj1 : σW j ≠ 1 := simple_ne_one' cs j
  have hjσi : σW j ≠ σW i := fun h => hne h.symm
  have hji1 : σW j * σW i ≠ 1 := by
    intro h
    have h2 : σW j = (σW i)⁻¹ := eq_inv_of_mul_eq_one_left h
    rw [cs.inv_simple] at h2
    exact hne h2.symm
  have hjii : σW j * σW i ≠ σW i := by
    intro h
    have h' : σW j * σW i = 1 * σW i := by rw [one_mul]; exact h
    exact hj1 (mul_right_cancel h')
  have hij1 : σW i * σW j ≠ 1 := by
    intro h
    have h2 : σW i = (σW j)⁻¹ := eq_inv_of_mul_eq_one_left h
    rw [cs.inv_simple] at h2
    exact hne h2
  have hiji : σW i * σW j ≠ σW i := by
    intro h
    have h' : σW i * σW j = σW i * 1 := by rw [mul_one]; exact h
    exact hj1 (mul_left_cancel h')
  have hiji1 : σW i * σW j * σW i ≠ 1 := by
    intro h
    have h2 : σW i * σW j = (σW i)⁻¹ := eq_inv_of_mul_eq_one_left h
    rw [cs.inv_simple] at h2
    exact hiji h2
  have hijii : σW i * σW j * σW i ≠ σW i := by
    intro h
    have h' : (σW i * σW j) * σW i = 1 * σW i := by rw [one_mul]; exact h
    exact hij1 (mul_right_cancel h')
  -- the kernel witness state
  set w : W → ℂ := fun x => if x = 1 then -I else if x = σW i then 1 else 0
    with hwdef
  have hw1 : w 1 = -I := by
    simp [hwdef]
  have hwσi : w (σW i) = 1 := by
    simp [hwdef, hi1]
  have hwx0 : ∀ x : W, x ≠ 1 → x ≠ σW i → w x = 0 := by
    intro x hx1 hx2
    simp [hwdef, hx1, hx2]
  -- the witness is killed by the (i,j)-assignment …
  have hzero : (tauAssignmentAtRank cs i j hm hne).toFun w
      = (tauAssignmentAtRank cs i j hm hne).toFun (fun _ => 0) := by
    funext u
    fin_cases u
    · show w (πW []) + I * w (πW [i]) = (0 : ℂ) + I * 0
      rw [wordProd_nil, wordProd_singleton, hw1, hwσi]
      ring
    · show w (πW [j]) + I * w (πW [j, i]) = (0 : ℂ) + I * 0
      rw [wordProd_singleton, wordProd_ij cs j i, hwx0 _ hj1 hjσi,
        hwx0 _ hji1 hjii]
    · show w (πW [i, j]) + I * w (πW [i, j, i]) = (0 : ℂ) + I * 0
      rw [wordProd_ij cs i j, wordProd_iji cs i j, hwx0 _ hij1 hiji,
        hwx0 _ hiji1 hijii]
    · rfl
  -- … so any transition forces the (j,i)-outputs to agree
  have h1 := hT w
  have h2 := hT (fun _ => 0)
  rw [hzero] at h1
  have h3 : (tauAssignmentAtRank cs j i hm' hne.symm).toFun w
      = (tauAssignmentAtRank cs j i hm' hne.symm).toFun (fun _ => 0) := by
    rw [h1, h2]
  -- but they differ at the first coordinate: `−I ≠ 0`
  have h5 : w (πW []) + I * w (πW [j]) = (0 : ℂ) + I * 0 := congrFun h3 0
  rw [wordProd_nil, wordProd_singleton, hw1, hwx0 _ hj1 hjσi] at h5
  have hI : (I : ℂ) = 0 := by linear_combination -h5
  exact Complex.I_ne_zero hI

end QOU.Machinery.CoxeterParabolic
