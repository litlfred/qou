import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-endomorphism-tower",
  title:
    "Proton--electron mass ratio from the $\\Phi_q$ tower",
  lean: { ref: "qou:QOU.MassEndomorphism.proton_electron_ratio",
    validation: "not_checked",
  },
  uses: [
    "rem:kashaev-volume-density",
    "rem:photon-channel-wedderburn-chain",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/habiro/habiro_exact_mass_endomorphism.py",
    witness: "computations/habiro/habiro-exact-mass-endomorphism.witness.json",
    status: "experimental",
  },
});
