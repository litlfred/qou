import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:spin-from-so3-fiber",
  title:
    "Spin $\\mathrm{SU}(2)_S$ from full $\\mathrm{SO}(3)$ fiber action on color-sheet rotations",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.SpinFromSO3Fiber",
    validation: "not_checked",
  },
  uses: [
    "def:color-tube-coordinates",
    "def:color-tube-fibers",
    "prop:inter-nucleon-channel-color-tube",
    "def:categorical-proton",
    "def:categorical-neutron",
    "thm:jones-markov-trace",
  ],
  cites: [
    "klein1884vorlesungen",
    "kashiwara1991",
    "khovanov-lauda2009",
    "wigner1937",
  ],
  tags: [
    "spin",
    "duality-d10",
    "so3-fiber",
    "color-tube",
    "spherical-harmonic-h4",
    "bring-surface",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
