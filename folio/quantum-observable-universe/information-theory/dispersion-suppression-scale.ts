import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:dispersion-suppression-scale",
  title:
    "Archimedean suppression of the substrate $q$-dispersion below the gamma-ray-burst bounds",
  uses: [
    "def:information-speed-of-light",
    "def:one-dim-qou-channel",
    "rem:dsr-planck-scale-phenomenology",
  ],
  cites: ["abdo2009"],
  lean: {
    ref: "qou:QOU.Information.DispersionSuppressionScale.dispersion_suppression_scale"
  },
  tags: [
    "dispersion",
    "lorentz-invariance",
    "planck-scale",
    "falsifiability",
    "information-theory",
  ],
});
