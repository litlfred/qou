import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:sm-hypercharge-invariant",
  title: "The hypercharge invariant",
  lean: {
    ref: "qou:QOU.StandardModel.HyperchargeInvariant",
    validation: "not_checked",
  },
  uses: ["def:gauge-action-groupoid", "def:coulomb-charge"],
  tags: [
    "appendix",
    "standard-model",
    "hypercharge",
    "electroweak",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-31",
      body:
        "**Primary conjecture, no instance (bean qou-q377).** " +
        "Formalize-first artifact for the hypercharge gap: the class " +
        "states the required properties (gauge-orbit invariance, " +
        "Gell-Mann–Nishijima, non-factorization through writhe); the " +
        "factorization criterion and the writhe-degenerate-pair " +
        "consequence are proved sorry-free. Candidate direction on " +
        "file (ribbon-framing twist, helon-model precedent) — " +
        "untested; see docs/audits/2026-07-31-sm-lit-analysis-" +
        "bean-workplan.md §1.",
    },
  ],
});
