import { proof } from "../../schema/builders";

export default proof({
  label: "prf:terminal-resolution",
  title: "Proof of Terminal Resolution of Hadronic Mass",
  uses: [
    "prop:terminal-resolution",
    "rem:skein-mass-relation",
    "prop:skein-generation",
    "prop:knot-eigenbasis-complete",
    "prf:knot-volumes-verification",
  ],
  lean: {
    decl: "QOU.HadronicMass.terminal_resolution_hadronic_mass",
    validation: "leanok",
  },
  computation: {
    engine: "snappea",
    script: "computations/knot-volumes.py",
    witness: "computations/knot-volumes.witness.json",
    status: "verified",
    requires: ["snappy>=3.3"],
  },
});
