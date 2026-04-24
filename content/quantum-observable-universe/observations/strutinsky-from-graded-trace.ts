import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:graded-trace-residue-split",
  label: "rem:strutinsky-from-graded-trace",
  title:
    "Strutinsky's shell correction as the categorical residue sum",
  tags: [
    "strutinsky",
    "shell-correction",
    "nuclear-physics",
    "liquid-drop",
    "graded-trace",
    "interpretation",
  ],
  uses: [
    "prop:graded-trace-residue-split",
    "prop:gb-residue-spectral-sum",
    "prop:shell-schur-weyl-self-duality",
    "rem:bw-mass-decomposition-dictionary",
  ],
});
