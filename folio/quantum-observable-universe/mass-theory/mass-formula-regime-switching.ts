import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-formula-regime-switching",
  title:
    "Mass formula regime switch: SW+Frob for $A \\leq 2$, BW+$\\chi$ for $A \\geq 3$ (non-additive)",
  lean: {
    ref: "qou:QOU.BraidKnot.mass_formula_regime_switching",
    validation: "not_checked",
  },
  uses: [
    "rem:np-discrepancy-resolution",
    "prop:chirality-from-frobenius-self-pairing",
  ],
  tags: [
    "mass-formula",
    "unification",
    "regime-switching",
    "bethe-weizsacker",
    "schur-weyl",
    "chirality",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:mass-formula-regime-switching -> conj:mass-formula-regime-switching." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "Per-A regime dispatch (A=2 / 3-4 / >=5) is selected against AME (Table 2), which AGENTS.md counts as fitting by per-case dispatch. The earlier claim that each regime is a convergent limit of an exact unified mass functional is unproved and was removed. Queued for demotion to a conjecture or remark; the Lean hardcodes AME values and proves nothing about a derivation.",
    },
  ],
});
