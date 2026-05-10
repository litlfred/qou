import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:depth-2-identification-bloch-suslin",
  title:
    "Depth-2 identification of $G^{(2)}(\\mathcal{H}_q)$ with $K_3^{\\mathrm{ind}}(F) \\otimes \\mathbb{Q}$ — provable via Bloch--Suslin",
  uses: [
    "conj:gb-depth-period-correspondence",
    "rem:k-theory-period-rosetta",
    "prop:borel-partial-resolution",
    "def:frobenius-hopf-substrate",
    "prop:categorical-laplace-unique",
    "conj:bring-figure-eight-depth-2-witness",
    "rem:transcendental-accounting",
  ],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "bloch-suslin",
    "k_3-indecomposable",
    "depth-2-identification",
    "keystone-discharge",
    "graded-mikusinski",
    "theorem-level",
  ],
});
