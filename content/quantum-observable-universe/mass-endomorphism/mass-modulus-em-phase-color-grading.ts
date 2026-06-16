import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-modulus-em-phase-color-grading",
  title:
    "Mass is the modulus, electromagnetism the phase, color the $S_3$ grading of one trace",
  interprets: "prop:color-spacetime-s5-factorization",
  uses: [
    "prop:color-spacetime-s5-factorization",
    "conj:binding-qbeta-complex-volume",
  ],
  tags: [
    "color",
    "electromagnetism",
    "mass",
    "complex-volume",
    "chern-simons",
    "interpretation",
  ],
});
