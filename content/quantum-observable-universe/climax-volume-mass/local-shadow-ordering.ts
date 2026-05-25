import { definition } from "../../schema/builders";

export default definition({
  label: "def:local-shadow-ordering",
  title: "Local shadow-price ordering $\\preceq_q$",
  lean: { ref: "qou:QOU.BraidKnot.LocalShadowOrdering",
    validation: "not_checked",
  },
  uses: ["def:unstable-atom"],
  tags: [
    "ordering",
    "shadow-price",
    "open-neighborhood",
    "continuity",
    "phase-boundary",
  ],
});
