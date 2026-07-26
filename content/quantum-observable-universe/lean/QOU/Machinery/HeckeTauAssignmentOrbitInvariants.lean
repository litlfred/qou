/-
# Orbit invariants and the pasted two-direction square

First enforcement of the gauge discipline that the assembled functor
licenses, in two parts:

**Part 1 — the pasted square (tower × groupoid).** The rank-tower
naturality (`tauAssignment_iotaPar_natural`, restriction along
extension-by-zero) and the groupoid coherence
(`tauAssignment_hom_coherent`, pullback along a marking morphism)
compose: for a marking morphism `φ` between two pairs inside the same
parabolic, with `φ` mapping the parabolic into itself, the full-group
assignment at the target pair evaluated on an extended state equals
the parabolic assignment at the source pair on the transported state
(`tauAssignment_paste`). The proof is literally the two proved squares
pasted — no new computation.

**Part 2 — orbit invariants.** `PairCoherent` names the gauge
discipline: a pair-indexed family of functionals on states is
*coherent* when every marking morphism intertwines it by pullback —
such a family descends to marked-pair orbits, so its values may be
quoted without naming the pair. Proved instances:

* `tauAssignment_pairCoherent` (+`_bar`) — the assignment family
  itself (restatement of the engine in the invariant language);
* `cellMarkovTrace_pairCoherent` — **the Markov trace of the cell
  restriction is an orbit invariant**: the trace law of the tower
  square, transported along every groupoid edge. This is the first
  quantity certified safe for pair-anonymous downstream consumption.

Honest boundary: coherence is proved for functionals that factor
through the cell restriction. The ambient `q = i` monodromy operator
`monodromyN (descentRight cs i)` acts through the length rule on the
FULL group, and marking morphisms need not preserve length, so its
equivariance is NOT claimed here — deciding it is the natural next
question, not an implicit corollary.

HONESTY (STRICT): sorry-free, no axioms, no `decide`; general-rank.
Everything here composes already-proved squares; nothing manufactures
new assignments and nothing is wired. `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeTauAssignmentGroupoidFunctor

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List Complex
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B}
  (cs : CoxeterSystem M W)

local prefix:100 "σW" => cs.simple

/-! ## Part 1 — the pasted two-direction square -/

/-- Parabolic cell restriction transports along a marking morphism that
preserves the parabolic. -/
lemma cellRestrictPar_hom (φ : W →* W) {i j i' j' : B} {J' : Set B}
    (hi : φ (σW i) = σW i') (hj : φ (σW j) = σW j')
    (hij : i ∈ J') (hjj : j ∈ J') (hii' : i' ∈ J') (hjj' : j' ∈ J')
    (hφ : ∀ x, x ∈ parabolic cs J' → φ x ∈ parabolic cs J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) :
    cellRestrictPar cs i' j' J' hii' hjj' v
      = cellRestrictPar cs i j J' hij hjj
          (fun x => v ⟨φ x.1, hφ x.1 x.2⟩) := by
  funext k
  show v ⟨cellElem3 cs i' j' k, _⟩ = v ⟨φ (cellElem3 cs i j k), _⟩
  exact congrArg v (Subtype.ext (cellElem3_hom cs φ hi hj k))

/-- Groupoid coherence at the parabolic level. -/
theorem tauAssignmentParabolic_hom_coherent (φ : W →* W)
    {i j i' j' : B} {J' : Set B}
    (hi : φ (σW i) = σW i') (hj : φ (σW j) = σW j')
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M i' j' = 3) (hne' : σW i' ≠ σW j')
    (hij : i ∈ J') (hjj : j ∈ J') (hii' : i' ∈ J') (hjj' : j' ∈ J')
    (hφ : ∀ x, x ∈ parabolic cs J' → φ x ∈ parabolic cs J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) :
    (tauAssignmentParabolic cs i' j' J' hm' hne' hii' hjj').toFun v
      = (tauAssignmentParabolic cs i j J' hm hne hij hjj).toFun
          (fun x => v ⟨φ x.1, hφ x.1 x.2⟩) := by
  show tauAssignmentH3.toFun (cellRestrictPar cs i' j' J' hii' hjj' v)
    = tauAssignmentH3.toFun (cellRestrictPar cs i j J' hij hjj
        (fun x => v ⟨φ x.1, hφ x.1 x.2⟩))
  rw [cellRestrictPar_hom cs φ hi hj hij hjj hii' hjj' hφ v]

/-- **THE PASTED SQUARE**: rank-tower restriction composed with a
groupoid edge. The full-group assignment at the target pair, evaluated
on a state extended by zero from a parabolic containing both pairs,
equals the parabolic assignment at the source pair on the transported
state. Proof: paste `tauAssignment_iotaPar_natural` with
`tauAssignmentParabolic_hom_coherent`. -/
theorem tauAssignment_paste (φ : W →* W) {i j i' j' : B} {J' : Set B}
    (hi : φ (σW i) = σW i') (hj : φ (σW j) = σW j')
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M i' j' = 3) (hne' : σW i' ≠ σW j')
    (hij : i ∈ J') (hjj : j ∈ J') (hii' : i' ∈ J') (hjj' : j' ∈ J')
    (hφ : ∀ x, x ∈ parabolic cs J' → φ x ∈ parabolic cs J')
    (v : {w : W // w ∈ parabolic cs J'} → ℂ) :
    (tauAssignmentAtRank cs i' j' hm' hne').toFun (iotaPar cs J' v)
      = (tauAssignmentParabolic cs i j J' hm hne hij hjj).toFun
          (fun x => v ⟨φ x.1, hφ x.1 x.2⟩) := by
  rw [tauAssignment_iotaPar_natural cs i' j' J' hm' hne' hii' hjj' v]
  exact tauAssignmentParabolic_hom_coherent cs φ hi hj hm hne hm' hne'
    hij hjj hii' hjj' hφ v

/-! ## Part 2 — orbit invariants -/

/-- **The gauge discipline**: a pair-indexed family of functionals on
states is *pair-coherent* when every marking morphism intertwines it
by pullback. A pair-coherent family descends to orbits of the
marked-pair groupoid — its values may be quoted without naming the
pair. -/
def PairCoherent {α : Type*}
    (F : MarkedPair cs → (W → ℂ) → α) : Prop :=
  ∀ {p p' : MarkedPair cs} (f : p ⟶ p') (v : W → ℂ),
    F p' v = F p (fun x => v (f.hom x))

/-- The assignment family is pair-coherent — the engine restated in
the invariant language. -/
theorem tauAssignment_pairCoherent :
    PairCoherent cs (fun p v =>
      (tauAssignmentAtRank cs p.i p.j p.bond p.ne).toFun v) :=
  fun f v => tauAssignment_hom_coherent cs f.hom f.map_i f.map_j
    _ _ _ _ v

/-- The conjugate leg is pair-coherent. -/
theorem tauAssignmentBar_pairCoherent :
    PairCoherent cs (fun p w =>
      (tauAssignmentAtRank cs p.i p.j p.bond p.ne).toFunBar w) :=
  fun f w => tauAssignment_hom_coherent_bar cs f.hom f.map_i f.map_j
    _ _ _ _ w

/-- The Markov trace of the cell restriction at a marked pair — the
trace law of the tower square, as a pair-indexed functional. -/
noncomputable def cellMarkovTrace (z h : ℂ) (p : MarkedPair cs)
    (v : W → ℂ) : ℂ :=
  QOU.Machinery.H3.trM z h (cellRestrict cs p.i p.j v)

/-- **The cell Markov trace is an orbit invariant**: every marking
morphism intertwines it by pullback, so trace values are well-defined
on marked-pair orbits — the first quantity certified safe for
pair-anonymous downstream consumption. -/
theorem cellMarkovTrace_pairCoherent (z h : ℂ) :
    PairCoherent cs (cellMarkovTrace cs z h) := by
  intro p p' f v
  unfold cellMarkovTrace
  congr 1
  funext k
  show v (cellElem3 cs p'.i p'.j k)
    = v (f.hom (cellElem3 cs p.i p.j k))
  rw [cellElem3_hom cs f.hom f.map_i f.map_j k]

end QOU.Machinery.CoxeterParabolic
