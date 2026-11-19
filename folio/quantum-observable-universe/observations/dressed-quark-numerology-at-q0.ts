import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dressed-quark-numerology-at-q0",
  title: "Dressed-quark numerology at $q_0$",
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "numerology",
    "q0",
  ],
  interprets: "prop:flavor-dressed-mass-from-substrate-split",
  uses: ["thm:flavor-mass-splitting-bound"],
  computation: {
    engine: "mpmath",
    script: "computations/probe_flavor_dressed_mass_from_substrate_split.py",
    witness: "computations/flavor-dressed-mass-from-substrate-split.witness.json",
    status: "verified",
  },
});
