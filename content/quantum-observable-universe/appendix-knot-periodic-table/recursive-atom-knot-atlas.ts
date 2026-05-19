import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:recursive-atom-knot-atlas",
  title:
    "Recursive atom-knot atlas at $q_0$ — particles to atoms via Markov-NF braids and hyperbolic-knot closures",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.recursive_atom_knot_atlas",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "rem:knot-particle-dictionary",
    "def:atomic-braid",
    "def:borromean-baryon",
    "prop:fermion-boson-knot-link",
    "prop:confinement-sdp",
    "thm:jones-markov-trace",
  ],
  cites: ["wenzl1988"],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "atlas",
    "recursive",
    "atom-knot",
    "particle-registry",
    "q0",
    "braid-word",
    "markov-closure",
    "hyperbolic-knot",
    "appendix",
  ],
});
