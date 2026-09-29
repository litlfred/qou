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
  // prop:graded-trace-residue-split is NOT listed: `interprets` above
  // already records it.
  uses: [
    // The residue sum the shell correction is identified with, applied to
    // the atomic braid. (No quotation marks in comments inside these
    // arrays: the manifest parsers extract every quoted string in the
    // array region, so quoted prose becomes a phantom entry.)
    "prop:gb-residue-spectral-sum",
    "rem:bw-mass-decomposition-dictionary",
    // The factorisation of H_q(lambda) behind the magic-number enhancement.
    "prop:shell-schur-weyl-self-duality",
  ],
});
