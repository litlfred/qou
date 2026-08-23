-- Probe: are the free-`Prop`-field carriers trivially inhabited?
-- Reproduced VERBATIM from their source files (paths in each comment) so this
-- file is self-contained and does not depend on a block's .lean staying put.

namespace Probe

/-- content/quantum-observable-universe/mass-theory/dim-master-pentagon.lean -/
class DimMasterPentagon where
  holds : Prop

/-- content/quantum-observable-universe/brings-surface/brings-smoothness-resolution.lean -/
class BringSurfaceSmoothness where
  transverse : Prop
  intrinsic_resolution : Prop
  regular_foliation : Prop

/-- content/quantum-observable-universe/lean/QOU/Habiro/FlowSolution.lean -/
class HabiroFlowSolution where
  expQ_solves_base_reeb : Prop
  fourier_diagonalises_qheat : Prop
  liTwoQ_volumetric : Prop
  all_hold : expQ_solves_base_reeb ∧ fourier_diagonalises_qheat
              ∧ liTwoQ_volumetric

-- Each is discharged with no mathematics whatsoever.
instance : DimMasterPentagon := ⟨True⟩
instance : BringSurfaceSmoothness := ⟨True, True, True⟩
instance : HabiroFlowSolution := ⟨True, True, True, ⟨trivial, trivial, trivial⟩⟩

-- Consequence: a downstream theorem conditioned on any of them is
-- unconditional -- the instance is synthesised from `⟨True, ...⟩` above, so
-- the hypothesis contributes nothing to the proof term.
theorem conditional_on_habiro [HabiroFlowSolution] (P : Prop) (hP : P) : P := hP

-- The instance argument resolves with no mathematics, at every call site.
example (P : Prop) (hP : P) : P := conditional_on_habiro P hP

end Probe
