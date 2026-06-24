import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:depth-2-identification-bloch-suslin",
  proofs: ["prf:depth-2-identification-bloch-suslin"],
  title:
    "Depth-2 identification of $G^{(2)}(\\mathcal{H}_q)$ with $K_3^{\\mathrm{ind}}(F) \\otimes \\mathbb{Q}$ — provable via Bloch--Suslin",
  lean: {
    ref: "qou:QOU.AppendixSurreals.Depth2IdentificationBlochSuslin.depth_2_identification",
    validation: "not_checked",
  },
  uses: ["prop:borel-partial-resolution"],
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
