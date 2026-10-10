import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectral-sequence-h3-explicit",
  title:
    "Explicit $d_1, d_2$ on $H_3(q)$ over $\\mathbb{R}[q, q^{-1}]$",
  lean: {
    ref: "qou:QOU.BraidKnot.spectral_sequence_h3_explicit",
    validation: "not_checked",
  },
  uses: ["prop:e-infinity-page-identifications"],
  tags: [
    "spectral-sequence",
    "explicit-differentials",
    "hecke-h3",
    "computation",
  ],
});
