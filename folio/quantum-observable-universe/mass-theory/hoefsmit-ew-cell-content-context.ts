import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hoefsmit-ew-cell-content-context",
  title: "Electroweak naming, minimality, interface-knot refinement, and further structure of the Hoefsmit electroweak cell content",
  interprets: "thm:hoefsmit-ew-cell-content",
  tags: ["hoefsmit", "electroweak", "torus-link", "plancherel"],
  uses: [
    "thm:hoefsmit-ew-cell-content",
    "conj:electroweak-higgs-torus-link-triplet",
    "conj:categorical-higgs-mechanism",
    "prop:weak-spectral-completeness",
  ],
  cites: ["morita1982"],
});
