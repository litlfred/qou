import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:flavor-mass-splitting-bound",
  lean: { ref: "qou:QOU.FlavorDressing.flavor_mass_splitting_bound",
    validation: "not_checked",
  },
  title: "Two-sided substrate bound on the dressed-quark splitting",
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "substrate-bound",
    "splitting-only",
  ],
  uses: ["prop:flavor-dressed-mass-from-substrate-split", "conj:flavor-split-substrate-mass"],
  computation: {
    engine: "mpmath",
    script: "computations/probe_flavor_dressed_mass_from_substrate_split.py",
    witness: "computations/flavor-dressed-mass-from-substrate-split.witness.json",
    status: "verified",
  },
});
