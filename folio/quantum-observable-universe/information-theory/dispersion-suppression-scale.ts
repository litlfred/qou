import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:dispersion-suppression-scale",
  title:
    "Planck-scale identification $\\mathfrak{E}_* \\ge E_{\\mathrm{Pl}}$ of the channel dispersion cutoff",
  uses: [
    "def:information-speed-of-light",
    "def:one-dim-qou-channel",
    "rem:photon-propagation-1d",
    "rem:dsr-planck-scale-phenomenology",
  ],
  cites: ["abdo2009"],
  lean: {
    ref: "qou:QOU.Information.DispersionSuppressionScale.dispersion_suppression_scale",
  },
  tags: [
    "dispersion",
    "lorentz-invariance",
    "planck-scale",
    "falsifiability",
    "information-theory",
  ],
});
