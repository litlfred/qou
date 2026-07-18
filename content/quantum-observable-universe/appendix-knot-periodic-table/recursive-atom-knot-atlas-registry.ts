import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-registry",
  title:
    "Atlas registry — methodology, notation, braid-closure gallery, and per-element AME 2020 cross-reference",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
    "prop:confinement-sdp",
    "prop:fermion-boson-knot-link",
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
    "registry",
    "atom-knot",
    "particle-registry",
    "q0",
    "braid-word",
    "markov-closure",
    "hyperbolic-knot",
    "per-element",
    "appendix",
  ],
});
