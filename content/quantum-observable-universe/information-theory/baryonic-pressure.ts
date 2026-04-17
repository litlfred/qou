import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:baryonic-pressure",
  title:
    "Information-theoretic confinement pressure at every jet level (baryon, nucleus, atom, molecule)",
  tags: [
    "pressure",
    "phase-transition",
    "lp-dual",
    "confinement",
    "information-theory",
    "bandwidth",
    "ideal-gas-law",
    "jet-tower",
    "hecke-algebra",
    "hopf-link",
    "gram-matrix",
  ],
  lean: {
    decl: "QOU.Information.confinementPressure",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-pressure",
    "def:quantum-temperature",
    "def:quantum-volume",
    "prop:quantum-ideal-gas-law",
    "prop:confined-knot-binding",
    "prop:lp-dual-stability",
    "prop:confinement-lp",
    "prop:frobenius-gram-matrix",
    "prop:toffoli-transfer-matrix",
    "prop:eos-borromean-cfl",
    "def:hopf-diquark",
    "def:information-speed-of-light",
    "def:operational-entropy",
  ],
});
