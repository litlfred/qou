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
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "**Anomaly route (bean qou-qvpl, PR #9729).** " +
        "QOU/StandardModel/AnomalyFreeHyperchargeUniqueness.lean " +
        "(0 sorry): on the SU(3)×SU(2) content of one generation with " +
        "five independent U(1) charges, the four perturbative anomaly " +
        "conditions hold iff the charges are yQ·(1,−4,2,−3,6) up to the " +
        "u↔d label, or vector-like; one neutral lepton then gives " +
        "yQ = ±1/6 and the 3/8 trace ratio. So Y is not a free second " +
        "datum once the representation content and anomaly freedom are " +
        "given. Still open: both of those inputs from the QOU axioms, " +
        "carried by the zero-instance class " +
        "CategoricalRibbonHyperchargeDerivationHypothesis (restated " +
        "2026-11-27; its old field was provable by rfl).",
    },
  ],
});
