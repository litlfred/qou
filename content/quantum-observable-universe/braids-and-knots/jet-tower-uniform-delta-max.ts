import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:jet-tower-uniform-delta-max",
  title:
    "Uniform per-level binding bound $|\\Delta^{(n)}(\\varrho)| \\le \\Delta_{\\max}(\\varrho)$ for the brane tower",
  lean: {
    ref: "qou:QOU.BraidKnot.JetTowerUniformDeltaMax",
    validation: "not_checked",
  },
  uses: [
    "prop:jet-tower-convergence",
    "prop:gb-spectral-sequence",
    "lem:tower-pair-equality-fixed-level",
    "def:recursive-brane-tower",
  ],
  cites: [
    "kassel1995",
    "yekutieli2010",
  ],
  tags: [
    "jet-tower",
    "uniform-bound",
    "convergence",
    "open-problem",
    "empirically-supported",
  ],
});
