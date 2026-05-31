import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shell-transition-knot",
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
  uses: ["conj:orbital-fourier-decomposition"],
});
