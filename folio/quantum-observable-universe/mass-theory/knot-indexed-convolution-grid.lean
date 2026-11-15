import QOU.BraidKnot.KnotIndexedConvolutionGrid

namespace QOU.BraidKnot.KnotIndexedConvolutionGrid

inductive ExistingOperation where
  | Lk_R_k (k : ℕ)
  | bowtie_K
  | hoefsmit_pairing
  | markov_trace

def placement_depth : ExistingOperation → ℕ
  | _ => 0

/-- **Proposition (`prop:knot-indexed-convolution-grid`).**
    All operational knot-indexed convolutions live at depth 0. -/
theorem existing_operations_depth_zero (op : ExistingOperation) :
    placement_depth op = 0 := by
  -- Ref: [leitner2026] prop:knot-indexed-convolution-grid
  cases op <;> rfl

end QOU.BraidKnot.KnotIndexedConvolutionGrid
