import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:atomic-mass-gb-nf",
  label: "rem:atomic-mass-gb-nf-interpretation",
  title: "Three equivalent forms, the density factor $\\rho_K$, and Class-A discipline status",
  tags: [
    "mass",
    "atomic-mass",
    "markov-trace",
    "categorical-density",
    "three-calibration-discipline",
  ],
  uses: [
    "prop:atomic-mass-gb-nf",
    "prop:categorical-mass-markov",
    "prop:rho-k-graded-expansion",
    "prop:alpha-shift-torus-knot",
    "prop:alpha-em-shift-multiplicative-chain",
    "conj:binding-scale-catalan",
    "sec:atomic-braid-mass-foundations",
    "prop:per-nucleon-shift-additive-linearity",
    "thm:wedderburn-mass-formula",
    "thm:knot-mass-formula-unified",
  ],
  cites: ["kassel1995", "jones1987"],
});
