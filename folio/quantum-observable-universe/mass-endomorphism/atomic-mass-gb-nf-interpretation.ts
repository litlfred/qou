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
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: rho-k-markov-multiplicativity.witness.json, rho-k-codata-vs-six-term.witness.json, rho-k-scaling-structure.witness.json, atomic-tr-m-mpfr-50dps.witness.json, atom-mass-atomic-braid.witness.json, paper-six-term-isotope-sweep.witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/rho_k_markov_multiplicativity_probe.py",
    witness: [
      "computations/probes/rho-k-markov-multiplicativity.witness.json",
      "computations/atomic-tr-m-mpfr-50dps.witness.json",
      "computations/sweeps/paper-six-term-isotope-sweep.witness.json",
      "computations/rho-k-leading-order-verification.witness.json",
      "computations/canonical-tr-m-three-path-comparison.witness.json",
    ],
    status: "verified",
  },
});
