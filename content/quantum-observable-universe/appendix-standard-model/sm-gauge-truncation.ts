import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:sm-gauge-truncation",
  title:
    "Standard-Model truncation: $\\mathrm{SU}(3) \\times \\mathrm{SU}(2) \\times \\mathrm{U}(1)$ in the archimedean gauge image",
  lean: {
    ref: "qou:QOU.StandardModel.StandardModelTruncation",
    validation: "not_checked",
  },
  uses: [
    "def:gauge-action-groupoid",
    "thm:su2-emergence",
    "def:coulomb-charge",
    "conj:g-action-on-substrate",
    "conj:electroweak-higgs-torus-link-triplet",
  ],
  tags: [
    "appendix",
    "standard-model",
    "gauge-theory",
    "electroweak",
    "color",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-31",
      body:
        "**Primary conjecture, no instance; per-factor status is " +
        "uneven.** $\\mathrm{SU}(2)$: the fibre gauge group is proved " +
        "(`thm:su2-emergence`) — which is also the structural " +
        "obstruction: the embedding cannot land in a single fibre. " +
        "$\\mathrm{U}(1)$: $Q = w/2$ and $w \\mapsto I_3$ are derived; " +
        "hypercharge $Y$ is open (falsified as a writhe map; missing " +
        "second crossing invariant — see the 2026-06-02 hypercharge " +
        "audit). $\\mathrm{SU}(3)$: open; only octonion/" +
        "colour-complex-structure Lean fragments exist. The " +
        "freeze-out/truncation mechanism has no derivation.",
    },
  ],
});
