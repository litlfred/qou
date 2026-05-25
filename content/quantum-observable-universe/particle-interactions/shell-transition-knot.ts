import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-transition-knot",
  title:
    "Stability pairs from Borromean spin-orbit shell-transition knots",
  tags: [
    "stability-pairs",
    "nuclear-shell",
    "harmonic-oscillator",
    "spin-orbit",
    "borromean",
    "shell-transition",
    "crossing-number",
  ],
  lean: { ref: "qou:QOU.Braiding.stability_pairs_correct",
    validation: "not_checked",
  },
  uses: ["prop:orbital-fourier-decomposition"],
});
