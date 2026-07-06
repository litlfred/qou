import { definition } from "../../schema/builders";

export default definition({
  label: "def:confinement-category",
  title: "The confinement category $\\mathbf{Conf}$",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementCategory",
    validation: "not_checked",
  },
  tags: [
    "category",
    "confinement",
    "morphism",
    "folding",
    "unfolding",
    "dressing",
  ],
  uses: ["def:confined-particle", "prop:level-sufficiency"],
});
