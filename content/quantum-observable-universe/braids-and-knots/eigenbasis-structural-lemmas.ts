import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-categorical",
  label: "rem:eigenbasis-structural-lemmas",
  title: "Content/twist eigenbasis: structural lemmas behind the Wedderburn characters (Lean)",
  tags: ["hecke-character", "ribbon-eigenvalue", "eigenbasis", "confinement"],
  lean: {
    ref: "qou:QOU.BraidKnot.EigenbasisStructuralLemmas.character_support_parity",
    validation: "not_checked",
  },
  uses: ["prop:confinement-categorical"],
});
