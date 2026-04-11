import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-endomorphism-tower",
  title:
    "Mass ratio $m_{\\mathfrak{p}}/m_e \\approx 1740$ from non-perturbative $\\Phi_q$ tower",
  lean: {
    decl: "QOU.MassEndomorphism.proton_electron_ratio",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-mass-element",
    "prop:hecke-mass-trace",
    "thm:topological-mass",
    "def:algebraic-quantum-volume",
    "prop:algebraic-volume-specialization",
    "rem:photon-channel-wedderburn-chain",
  ],
});
