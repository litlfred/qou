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
  cites: [
    "neumann-zagier1985",
    "kashaev1997",
    "murakami-murakami2001",
    "witten1989",
    "witten2011",
    "reshetikhin1991",
    "zagier2010",
    "faddeev1994",
    "jones1985",
    "frobenius-schur1906",
    "takesaki1970",
    "weil1958",
    "gamow1928",
    "breit-wigner1936",
    "kronig1926",
  ],
});
