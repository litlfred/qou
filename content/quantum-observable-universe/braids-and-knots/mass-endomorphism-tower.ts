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
    "cor:quantum-dilogarithm",
  ],
});
