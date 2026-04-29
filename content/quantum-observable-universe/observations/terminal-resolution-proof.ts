import { proof } from "../../schema/builders";

export default proof({
  label: "prf:terminal-resolution",
  title: "Proof of Terminal Resolution of Hadronic Mass",
  uses: [
    "prop:skein-generation",
    "prf:knot-volumes-verification",
    "lem:deuteron-binding-energy",
  ],
  lean: { ref: "qou:QOU.HadronicMass.terminal_resolution_hadronic_mass",
    validation: "leanok",
  },
  computation: {
    engine: "snappea",
    script: "folio-assistant/computations/knot-volumes.py",
    witness: "folio-assistant/computations/knot-volumes.witness.json",
    status: "verified",
    requires: ["snappy>=3.3"],
  },
});
