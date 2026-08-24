import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:descended-level-zero",
  title:
    "Descended mass contribution lives at level 0 only",
  tags: [
    "descent",
    "jet-tower",
    "mass-endomorphism",
    "level-counting",
    "audit",
  ],
  lean: {
    ref: "qou:QOU.Descent.descended_level_zero",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "**The sibling re-introduced the exact projection the library had " +
        "removed** (bean `qou-lo1t`). `QOU/Descent/descended_level_zero.lean` " +
        "records the decision: *\"The self-assuming `claim_descended_level_zero` " +
        "carrier field of the old encoding is removed; inhabiting the " +
        "proposition is the open conditional claim, not faked by a " +
        "projection.\"* It names the claim as a `Prop` and asserts nothing.\n\n" +
        "The sibling `descended-level-zero.lean` carried a " +
        "`DescendedLevelZeroContext` class whose `desc_contrib_zero` field is " +
        "the conclusion verbatim, and a theorem returning that field — the " +
        "§3b-cond item-5 degenerate shape. Per §0a the sibling resolves " +
        "*first*, so the block pointed at the projection rather than at the " +
        "repaired encoding.\n\n" +
        "Sibling deleted; nothing referenced it or its class. The ref now " +
        "resolves to the library's named `Prop`, which leaves the claim " +
        "visibly open instead of discharging it by assumption.",
    },
  ],
  uses: ["prf:topological-mass"],
  cites: ["leitner2026"],
});
