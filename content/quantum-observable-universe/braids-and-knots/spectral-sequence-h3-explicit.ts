import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectral-sequence-h3-explicit",
  title:
    "Explicit $d_1, d_2$ on $H_3(q)$ over $\\mathbb{R}[q, q^{-1}]$",
  lean: {
    decl: "QOU.BraidKnot.spectral_sequence_h3_explicit",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:e-infinity-page-identifications",
    "def:hecke-normal-form",
    "def:confinement-level",
    "thm:jones-markov-trace",
  ],
  tags: [
    "spectral-sequence",
    "explicit-differentials",
    "hecke-h3",
    "computation",
  ],
});
