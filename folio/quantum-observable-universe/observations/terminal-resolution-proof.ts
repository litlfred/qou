import { proof } from "../../schema/builders";

export default proof({
  label: "prf:terminal-resolution",
  title: "Proof of Terminal Resolution of Hadronic Mass",
  uses: [
    "prop:skein-generation",
    "prf:knot-volumes-verification",
  ],
  lean: { ref: "qou:QOU.HadronicMass.terminal_resolution_hadronic_mass",
    validation: "leanok",
  },
  computation: {
    engine: "snappea",
    script: "computations/knot-volumes.py",
    witness: "computations/substrate/knot-volumes.witness.json",
    status: "verified",
    requires: ["snappy>=3.3"],
  },
});
