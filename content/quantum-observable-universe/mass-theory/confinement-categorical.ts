import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-categorical",
  title: "Confinement = spectral-sequence collapse (only Wedderburn-central observables survive)",
  lean: {
    ref: "qou:QOU.WedderburnMass.confinement_categorical",
    validation: "not_checked",
  },
  uses: ["prop:unified-curvature-rank-mass-formula"],
  computation: {
    engine: "python",
    script: "computations/atomic_chirality_residue.py",
    witness: "computations/atomic-chirality-residue.witness.json",
    status: "verified",
    requires: ["mpmath", "numpy"],
  },
});
