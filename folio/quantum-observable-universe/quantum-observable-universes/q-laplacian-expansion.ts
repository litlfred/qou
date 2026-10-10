import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:q-laplacian-expansion",
  title: "Three-term expansion of the $q$-Laplacian",
  uses: ["def:q-harmonic-form", "rem:q-codifferential-formula"],
  tags: ["q-laplacian", "expansion", "coriolis"],
});
