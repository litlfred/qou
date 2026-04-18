import { definition } from "../../schema/builders";

export default definition({
  label: "def:confinement-category",
  title: "The confinement category $\\mathbf{Conf}$",
  lean: {
    decl: "QOU.BraidKnot.ConfinementCategory",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "prop:confinement-sdp",
    "def:hecke-normal-form",
  ],
  tags: [
    "category",
    "confinement",
    "morphism",
    "folding",
    "unfolding",
    "dressing",
  ],
});
