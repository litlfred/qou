import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.LinearAlgebra.Trace
import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtStandardBasis
import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.SpechtFinrankWired
import QOU.BraidKnot.IdentityIContentDecomposition
import QOU.BraidKnot.JucysMurphyOV
import QOU.BraidKnot.RegularRepBlockTrace
import QOU.BraidKnot.OVTopAssembly

/-!
# Piece A: Specht Module Character Evaluation

This file scaffolds the representation-theoretic route for Piece A
(`Σ_c h_c² = Σ_c c(c)² + n²`) using Specht module characters.

By evaluating the character of central elements (like the sum of Jucys-Murphy
squares) on the Specht module $S^\lambda$, one can extract the sum of squared contents
and relate it to the hook lengths via the dimension formula.
-/

namespace QOU.BraidKnot.PieceA

open scoped BigOperators
open QOU.BraidKnot.JucysMurphy
open QOU.BraidKnot.Specht

variable {k : Type} [Field k] [CharZero k]

/-- The endomorphism `ρ(C₂) = (Mtab.rep μ).asAlgebraHom (centralC2 …)` maps the
Specht submodule `S^μ` into itself: on `S^μ` it acts by the scalar `contentSqSum μ`
(`centralC2_acts_by_contentSqSum`), and `S^μ` is closed under that scalar. This is
the invariance hypothesis needed to `LinearMap.restrict` `ρ(C₂)` to `S^μ`. -/
theorem centralC2_mapsTo_specht (μ : YoungDiagram) :
    ∀ x ∈ Specht.SpechtSubmodule (k := k) μ,
      (Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)) x
        ∈ Specht.SpechtSubmodule (k := k) μ := by
  intro x hx
  rw [centralC2_acts_by_contentSqSum (k := k) μ x hx, ← Int.cast_smul_eq_zsmul k]
  exact Submodule.smul_mem _ _ hx

/-- The trace of `centralC2` on the Specht module `S^μ`.
Since `centralC2` acts by the scalar `contentSqSum μ` on the Specht module,
the restricted operator is `(contentSqSum μ) • id`, so its trace evaluates to
`contentSqSum μ * dim(S^μ)`. -/
theorem trace_centralC2_specht_module (μ : YoungDiagram) :
    LinearMap.trace k _ (LinearMap.restrict
      ((Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)))
      (centralC2_mapsTo_specht (k := k) μ)) =
    (contentSqSum μ : k) * Module.finrank k (Specht.SpechtSubmodule (k := k) μ) := by
  -- Ref: [macdonald1995] Symmetric Functions and Hall Polynomials
  -- The restricted operator equals the scalar `(contentSqSum μ : k) • id` on `S^μ`
  -- (`centralC2_acts_by_contentSqSum`); the trace of a scalar multiple of the identity
  -- is that scalar times the dimension (`LinearMap.trace_id`).
  have hg :
      LinearMap.restrict
        ((Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)))
        (centralC2_mapsTo_specht (k := k) μ)
        = (contentSqSum μ : k) • LinearMap.id := by
    refine LinearMap.ext fun x => ?_
    apply Subtype.ext
    rw [LinearMap.restrict_coe_apply, LinearMap.smul_apply, LinearMap.id_apply,
        Submodule.coe_smul,
        centralC2_acts_by_contentSqSum (k := k) μ (x : Specht.Mtab (k := k) μ) x.2,
        ← Int.cast_smul_eq_zsmul k]
  rw [hg, map_smul, LinearMap.trace_id, smul_eq_mul]

/-- The central element `C_2` evaluated on the full group algebra is given by 
a sum of dimensions and squared contents, bridging representation theory to hooks. -/
lemma trace_centralC2_regular_rep (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit k] :
    LinearMap.trace k _ (LinearMap.mulLeft k (centralC2 (k := k) n)) =
    ∑ μ : SpechtClassification.PartitionIndex n,
      (contentSqSum μ.val : k) * (Module.finrank k (Specht.SpechtSubmodule (k := k) μ.val))^2 := by
  -- Ref: [macdonald1995] Symmetric Functions and Hall Polynomials
  -- The Artin–Wedderburn / Jucys–Murphy block spectral decomposition of the regular
  -- representation is the assembled datum `OVTopAssembly.snSpectralData n`
  -- (`Idx = PartitionIndex n`, `ω i = contentSqSum i.diagram`, `d i = numSYT i.diagram`); side 2
  -- of the trace equation is `RegularRepBlockTrace.blockTrace_eq` applied to it. `centralC2` here
  -- is defeq to `RegularRepTrace.centralC2` (`centralC2_eq_sum_jucysMurphy_sq`), and the wired
  -- dimension identity `finrank Sᵘ = numSYT` (`specht_finrank_eq_numSYT_wired`) matches the
  -- per-block factor. The residual Okounkov–Vershik / Wedderburn content stays in those bricks'
  -- own cited sorries — nothing new is assumed here.
  rw [JucysMurphy.centralC2_eq_sum_jucysMurphy_sq,
    RegularRepBlockTrace.blockTrace_eq (OVTopAssembly.snSpectralData (R := k) n)]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [SpechtFinrankWired.specht_finrank_eq_numSYT_wired (k := k) i.val]
  rfl

/-- Piece A fundamental identity (representation-theoretic route):
`Σ_c h_c² = Σ_c c(c)² + n²`.
Here we state the equivalence between the representation-theoretic evaluation
and the combinatorial formula `sumSqHooks_eq_sumSqContents_add_sq`. 
The list `l` corresponds to the row lengths of the partition. -/
lemma pieceA_hook_sq_eq_content_sq_add_n_sq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    IdentityI.sumSqHooks l = IdentityI.sumSqContents l + (IdentityI.sz l : ℤ) ^ 2 :=
  -- The combinatorial route already proves this outright (the representation-theoretic
  -- trace route and the combinatorial route converge on the same identity).
  IdentityI.sumSqHooks_eq_sumSqContents_add_sq l hl

end QOU.BraidKnot.PieceA
