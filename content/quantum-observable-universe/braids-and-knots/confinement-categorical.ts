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
    script: "folio-assistant/computations/atomic_chirality_residue.py",
    witness: "folio-assistant/computations/atomic-chirality-residue.witness.json",
    status: "not_run",
    requires: ["mpmath", "numpy"],
  },
});
