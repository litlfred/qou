import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-formula-regime-switching",
  title:
    "Mass formula regime switch: an $A$-uniform evaluation whose dominant term changes at the pair-graph regime boundaries $A = 2 \\mid 3$ and $4 \\mid 5$",
  lean: {
    ref: "qou:QOU.BraidKnot.mass_formula_regime_switching",
    validation: "not_checked",
  },
  uses: [
    "rem:np-discrepancy-resolution",
    "prop:chirality-from-frobenius-self-pairing",
    "prop:pair-graph-regime-trichotomy",
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
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    { kind: "status", date: "2026-11-16", body: "Restated (issue #8094): the conjecture is now the existence of an A-uniform evaluation that changes character at the boundaries of prop:pair-graph-regime-trichotomy, which proves the cut-offs from A alone. The AME selection, the 5% tolerance and the 'non-additive' wording are moved to a marked comparison paragraph or dropped. The sibling Lean holds AME tables and if-branch evaluations; it is data for the comparison, not support for the conjecture." },
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:mass-formula-regime-switching -> conj:mass-formula-regime-switching." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "Per-A regime dispatch (A=2 / 3-4 / >=5) is selected against AME (Table 2), which AGENTS.md counts as fitting by per-case dispatch. The earlier claim that each regime is a convergent limit of an exact unified mass functional is unproved and was removed. Queued for demotion to a conjecture or remark; the Lean hardcodes AME values and proves nothing about a derivation.",
    },
  ],
});
