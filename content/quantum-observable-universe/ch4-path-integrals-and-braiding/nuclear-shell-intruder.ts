import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-shell-intruder",
  title:
    "Stability pairs from Borromean spin-orbit intruder levels",
  tags: [
    "stability-pairs",
    "nuclear-shell",
    "harmonic-oscillator",
    "spin-orbit",
    "borromean",
    "intruder",
    "crossing-number",
  ],
  lean: {
    decl: "QOU.Braiding.nuclear_shell_intruder",
    validation: "not_checked",
  },
  uses: [
    "def:borromean-baryon",
    "def:crossing-energy",
    "prop:orbital-fourier-decomposition",
  ],
});
