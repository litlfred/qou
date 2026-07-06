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
    "prop:fermion-boson-knot-link",
    "prop:confinement-sdp",
    // SDP-uniqueness wiring (2026-05-31): the atlas's per-atom T_w
    // canonical-knot identifications are certified at the abstract-
    // framework level by the parameterised SDP-uniqueness theorems
    // (PRs #1537/#1542/#1546). Each atlas entry's T_w uniqueness is
    // `qou:QOU.BraidKnot.nucleus_uniqueness_closed (3*A)`; named
    // wrappers exist at per-isotope (10), per-element (118), and
    // per-stable-isotope (252) granularities.
    "conj:canonical-knot-id-sdp",
  ],
  cites: ["wenzl1988"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
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
  authorNotes: [
    {
      kind: "note",
      date: "2026-05-31",
      body: "SDP-uniqueness wiring: `NucleusEmptySDPUniqueness` landed via PR #1537; the per-stable-isotope `StableIsotopeUniqueness.lean` was pending PR #1542.",
    },
  ],
});
