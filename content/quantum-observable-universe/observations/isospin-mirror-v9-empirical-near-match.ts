import { remark } from "../../schema/builders";

export default remark({
  label: "rem:isospin-mirror-v9-empirical-near-match",
  title:
    "Empirical near-match for the ³H/³He binding-energy mirror difference (forward-reference to audit)",
  interprets: "rem:option-e-isospin-test",
  uses: [
    "rem:option-e-isospin-test",
  ],
  tags: [
    "option-e",
    "isospin",
    "mirror",
    "binding-energy",
    "near-match",
    "audit-forward-reference",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-06-03",
      body: "**Primary content moved to [`docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md`](../../../docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md).** Per CLAUDE.md canonical-no-negative-result-in-paper discipline (PR #1758): the v9 isospin-mirror probe is a fitted near-match, not a substrate derivation; the audit doc carries the full assessment. This block remains in the paper as an interpretive cross-reference.",
      see: "https://github.com/litlfred/qou/pull/1758",
    },
  ],
});
