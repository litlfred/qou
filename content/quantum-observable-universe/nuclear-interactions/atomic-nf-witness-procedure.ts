import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:atomic-nf-witness",
  label: "rem:atomic-nf-witness-procedure",
  title: "Construction and certification procedure for the atomic normal-form witness",
  tags: ["atomic-braid", "normal-form", "witness", "diamond-lemma", "pauli-character"],
  uses: ["prop:atomic-nf-witness", "def:atomic-braid"],
});
