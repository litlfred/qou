import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Projection
import Mathlib.Topology.Instances.Matrix
import Mathlib.Topology.Instances.Int
import Mathlib.Topology.Homeomorph.Lemmas
import Mathlib.Topology.Connected.TotallyDisconnected
import Mathlib.Analysis.Complex.Basic

/-!
# Trace rigidity of continuous families of idempotent matrices

This file proves three abstract lemmas used as **step 3 of the rigidity route** in
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` §5 (the comparison of two
continuous families of representations of the semisimple Hecke algebra by their block
multiplicities, where a block multiplicity is the trace of the image of a central
idempotent divided by the block size).

* `trace_eq_rank` — over any field `K`, an idempotent square matrix `P` satisfies
  `trace P = (rank P : K)`. No characteristic hypothesis is needed for this identity
  (it is the statement in `K`; injectivity of `ℕ → K` is a separate matter). It is a
  repackaging of Mathlib's `LinearMap.IsProj.trace`.
* `rank_const_of_isPreconnected` / `trace_const_of_isPreconnected` — if
  `P : X → Matrix n n ℂ` is continuous on a preconnected set `S` and idempotent at every
  point of `S`, then `rank (P x)` and `trace (P x)` are constant on `S`.
  The trace is continuous and takes values in the image of `ℕ`, a discrete subset;
  continuity is only needed on `S`.
* `trace_eq_of_isPreconnected` — two such families (possibly of different sizes) whose
  traces agree at one point of `S` have equal traces at every point of `S`.

The first lemma is stated over a generic field (§7c); `ℂ` enters only for the topology.
-/

namespace QOU.Mass.IdempotentTraceRigidity

open Matrix

section Field

variable {K : Type*} [Field K] {n : Type*} [Fintype n] [DecidableEq n]

/-- The trace of an idempotent matrix over a field equals its rank (cast into the field). -/
theorem trace_eq_rank (P : Matrix n n K) (hP : IsIdempotentElem P) :
    P.trace = (P.rank : K) := by
  have hL : IsIdempotentElem (Matrix.toLinAlgEquiv' P) := hP.map Matrix.toLinAlgEquiv'
  have hproj := (LinearMap.IsIdempotentElem.isProj_range _ hL).trace
  rw [← Matrix.trace_toLin'_eq]
  exact hproj

/-- **Equal rank implies equal trace for idempotent matrices over `K` (`qou-cdx1`).**
If `P : Matrix n n K` and `Q : Matrix m m K` are idempotent with `P.rank = Q.rank`,
then `P.trace = Q.trace`. -/
theorem trace_eq_of_rank_eq {m : Type*} [Fintype m] [DecidableEq m]
    (P : Matrix n n K) (Q : Matrix m m K)
    (hP : IsIdempotentElem P) (hQ : IsIdempotentElem Q)
    (hrank : P.rank = Q.rank) :
    P.trace = Q.trace := by
  rw [trace_eq_rank P hP, trace_eq_rank Q hQ, hrank]

end Field

section Topology

variable {X : Type*} [TopologicalSpace X]

/-- `ℤ`, embedded in `ℝ`, has discrete range. -/
private lemma discrete_range_intCast : DiscreteTopology (Set.range ((↑) : ℤ → ℝ)) :=
  (Int.isClosedEmbedding_coe_real.isEmbedding.toHomeomorph).discreteTopology_iff.mp
    inferInstance

/-- **Rigidity of rank.** A family of idempotent complex matrices that is continuous on a
preconnected set has constant rank on that set. -/
theorem rank_const_of_isPreconnected {n : Type*} [Fintype n] [DecidableEq n]
    {S : Set X} (hS : IsPreconnected S) {P : X → Matrix n n ℂ} (hc : ContinuousOn P S)
    (hidem : ∀ x ∈ S, IsIdempotentElem (P x)) {x y : X} (hx : x ∈ S) (hy : y ∈ S) :
    (P x).rank = (P y).rank := by
  haveI := discrete_range_intCast
  -- the real part of the trace is continuous on `S` and equals the (integer-cast) rank
  have hre : ContinuousOn (fun z => (Matrix.trace (P z)).re) S :=
    Complex.continuous_re.comp_continuousOn
      ((continuous_id.matrix_trace).comp_continuousOn hc)
  have hval : ∀ z ∈ S, (Matrix.trace (P z)).re = (((P z).rank : ℤ) : ℝ) := by
    intro z hz
    rw [trace_eq_rank _ (hidem z hz)]
    simp
  have hmaps : Set.MapsTo (fun z => (Matrix.trace (P z)).re) S
      (Set.range ((↑) : ℤ → ℝ)) := fun z hz => ⟨_, (hval z hz).symm⟩
  have h := hS.constant_of_mapsTo hre hmaps hx hy
  simp only at h
  rw [hval x hx, hval y hy] at h
  exact_mod_cast h

/-- **Rigidity of trace.** A family of idempotent complex matrices that is continuous on a
preconnected set has constant trace on that set. -/
theorem trace_const_of_isPreconnected {n : Type*} [Fintype n] [DecidableEq n]
    {S : Set X} (hS : IsPreconnected S) {P : X → Matrix n n ℂ} (hc : ContinuousOn P S)
    (hidem : ∀ x ∈ S, IsIdempotentElem (P x)) {x y : X} (hx : x ∈ S) (hy : y ∈ S) :
    (P x).trace = (P y).trace := by
  rw [trace_eq_rank _ (hidem x hx), trace_eq_rank _ (hidem y hy),
    rank_const_of_isPreconnected hS hc hidem hx hy]

/-- **Two-family comparison.** Two continuous families of idempotent complex matrices (of
possibly different sizes) on a preconnected set whose traces agree at one point have equal
traces at every point of the set. -/
theorem trace_eq_of_isPreconnected {n m : Type*} [Fintype n] [DecidableEq n]
    [Fintype m] [DecidableEq m]
    {S : Set X} (hS : IsPreconnected S)
    {P : X → Matrix n n ℂ} (hPc : ContinuousOn P S) (hP : ∀ x ∈ S, IsIdempotentElem (P x))
    {Q : X → Matrix m m ℂ} (hQc : ContinuousOn Q S) (hQ : ∀ x ∈ S, IsIdempotentElem (Q x))
    {x₀ : X} (hx₀ : x₀ ∈ S) (h₀ : (P x₀).trace = (Q x₀).trace) :
    ∀ x ∈ S, (P x).trace = (Q x).trace := by
  intro x hx
  rw [trace_const_of_isPreconnected hS hPc hP hx hx₀,
    trace_const_of_isPreconnected hS hQc hQ hx hx₀, h₀]

/-- The rank version of the two-family comparison. -/
theorem rank_eq_of_isPreconnected {n m : Type*} [Fintype n] [DecidableEq n]
    [Fintype m] [DecidableEq m]
    {S : Set X} (hS : IsPreconnected S)
    {P : X → Matrix n n ℂ} (hPc : ContinuousOn P S) (hP : ∀ x ∈ S, IsIdempotentElem (P x))
    {Q : X → Matrix m m ℂ} (hQc : ContinuousOn Q S) (hQ : ∀ x ∈ S, IsIdempotentElem (Q x))
    {x₀ : X} (hx₀ : x₀ ∈ S) (h₀ : (P x₀).trace = (Q x₀).trace) :
    ∀ x ∈ S, (P x).rank = (Q x).rank := by
  intro x hx
  have h := trace_eq_of_isPreconnected hS hPc hP hQc hQ hx₀ h₀ x hx
  rw [trace_eq_rank _ (hP x hx), trace_eq_rank _ (hQ x hx)] at h
  exact_mod_cast h

end Topology

end QOU.Mass.IdempotentTraceRigidity
