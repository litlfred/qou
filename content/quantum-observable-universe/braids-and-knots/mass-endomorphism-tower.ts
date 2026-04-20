import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-endomorphism-tower",
  title:
    "Proton--electron mass ratio from the $\\Phi_q$ tower",
  lean: {
    decl: "QOU.MassEndomorphism.proton_electron_ratio",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-mass-element",
    "prop:hecke-mass-trace",
    "thm:topological-mass",
    "thm:jones-markov-trace",
    "def:algebraic-quantum-volume",
    "rem:photon-channel-wedderburn-chain",
    "thm:wedderburn-mass-formula",
    "cor:quantum-dilogarithm",
    "def:briggs-klein-chart",
    "def:quantum-bloch-group",
    "rem:mass-endomorphism-jet-tower",
    "thm:markov-trace-factorization",
  ],
});
