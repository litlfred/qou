import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:higgs-vacuum-residual-idempotent",
  title:
    "The vacuum idempotent $e = t^{-1}\\varrho\\varrho^{*}$, its residual, and the symmetric split of $\\mathrm{id} - e \\otimes e$",
  lean: {
    ref: "qou:QOU.QuantumObservableUniverses.PointCopoint.tensorResid_split",
    validation: "not_checked",
  },
  uses: [],
  tags: [
    "categorical-higgs",
    "idempotent",
    "residual",
    "symmetric-monoidal",
    "frobenius-hopf-substrate",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Lean module `QOU.QuantumObservableUniverses.HiggsVacuumResidual` (sorry-free). Item map: (a)1 `PointCopoint.proj_idem`, `pt_comp_proj`, `proj_comp_copt`; (a)2 `resid_idem`, `proj_comp_resid`, `resid_comp_proj`, `proj_add_resid`; (a)3 `pt_comp_resid`, `resid_comp_copt`; (b) `symPart_idem`, `altPart_idem`, `symPart_add_altPart`, `symPart_comp_altPart`, `symPart_comp_sigma`, `altPart_comp_sigma`, `comp_symPart_comm`, `comp_altPart_comm`; 4 `tensorProj_idem`, `tensorResid_idem`, `tensorResid_comm_symPart`, `tensorResid_comm_altPart`; 5 `tensorResid_split`, `tensorResid_symPart_idem`, `tensorResid_altPart_idem`, `tensorResid_symPart_comp_altPart`; 6 `tensorResid_eq`; 7 `residSq_symPart_idem`. Mathlib's `≫` is diagrammatic: the paper's $\\varrho \\circ \\varrho^{*}$ is `copt ≫ pt`. Deliberately no `uses` edge to `conj:g-action-on-substrate`: the statement is unconditional and only gives the morphism-level form of the (G-4) definition; the body links the conjecture in prose.",
    },
  ],
});
