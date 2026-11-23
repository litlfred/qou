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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): When $\\mathbf{C}$ is monoidal and $U = \\mathbf{1}$, this is the vacuum datum $(\\varrho_\\Phi, \\varrho_\\Phi^{*})$ of Constraints (G-3)–(G-4) of [the $G$-action conjecture](#conj:g-action-on-substrate), where $t$ is the endomorphism $\\varrho_\\Phi^{*} \\circ \\varrho_\\Phi$ of $\\mathbf{1}$ read as a scalar; it equals the normalisation $\\mathrm{tr}_F(\\varrho_\\Phi^{*}\\varrho_\\Phi)$ of (G-3) when the trace satisfies $\\mathrm{tr}_F(\\mathrm{id}_{\\mathbf{1}}) = 1$." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3):  All items are checked in Lean, without `sorry`." },
    {
      kind: "note",
      body: "Lean module `QOU.QuantumObservableUniverses.HiggsVacuumResidual` (sorry-free). Item map: (a)1 `PointCopoint.proj_idem`, `pt_comp_proj`, `proj_comp_copt`; (a)2 `resid_idem`, `proj_comp_resid`, `resid_comp_proj`, `proj_add_resid`; (a)3 `pt_comp_resid`, `resid_comp_copt`; (b) `symPart_idem`, `altPart_idem`, `symPart_add_altPart`, `symPart_comp_altPart`, `symPart_comp_sigma`, `altPart_comp_sigma`, `comp_symPart_comm`, `comp_altPart_comm`; 4 `tensorProj_idem`, `tensorResid_idem`, `tensorResid_comm_symPart`, `tensorResid_comm_altPart`; 5 `tensorResid_split`, `tensorResid_symPart_idem`, `tensorResid_altPart_idem`, `tensorResid_symPart_comp_altPart`; 6 `tensorResid_eq`; 7 `residSq_symPart_idem`; (c)8 `CyclicTrace`, `PointCopoint.tr_proj`, `PointCopoint.tr_resid`, `VacuumPairing.tr_proj_eq_one`, `VacuumPairing.eq_one_of_tr_proj_eq`. Mathlib's `≫` is diagrammatic: the paper's $\\varrho \\circ \\varrho^{*}$ is `copt ≫ pt`. Deliberately no `uses` edge to `conj:g-action-on-substrate`: the statement is unconditional and only gives the morphism-level form of the (G-4) definition; the body links the conjecture in prose.",
    },
  ],
});
