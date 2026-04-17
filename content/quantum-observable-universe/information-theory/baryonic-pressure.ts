import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:baryonic-pressure",
  title:
    "Information-theoretic confinement pressure at every jet level (baryon, nucleus, atom, molecule)",
  tags: [
    "pressure",
    "baryon",
    "atom",
    "molecule",
    "confinement",
    "information-theory",
    "bandwidth",
    "ideal-gas-law",
    "jet-tower",
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
    "def:information-speed-of-light",
    "def:operational-entropy",
  ],
});
