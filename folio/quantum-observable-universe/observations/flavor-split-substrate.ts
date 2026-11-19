import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:flavor-split-substrate",
  lean: { ref: "qou:QOU.HadronicMass.flavor_split_substrate",
    validation: "not_checked",
  },
  title: "Aether-pure derivation of the $u$--$d$ flavor split",
  tags: ["flavor-split", "u-d-splitting", "substrate-only", "no-fit",
         "hecke-substrate-atoms", "categorical-derivation"],
  uses: [
    "lem:pair-skein-mass-formula",
  ],
  computation: {
    engine: "python",
    script: "computations/probes/flavor_split_substrate_probe.py",
    witness: "computations/probes/flavor-split-substrate-probe.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
  proofs: ["prf:flavor-split-substrate"],
});
