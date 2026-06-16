import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-volume-factorization",
  title:
    "Mass-volume factorization of the categorical mass endomorphism",
  tags: [
    "tier:S",
    "mass-endomorphism",
    "hyperbolic-volume",
    "density",
    "frobenius-packing",
    "jsj-decomposition",
    "categorical-action",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.MassVolumeFactorization",
    validation: "not_checked",
  },
  uses: [
    "rem:frobenius-packing-density",
    "prop:thurston-volume-additivity",
  ],
  cites: ["thurston1978", "murakami-murakami2001"],
  computation: {
    engine: "closed-form",
    script: "computations/d_density_derivation.py",
    witness: "computations/d-density-derivation.witness.json",
    status: "verified",
  },
});
