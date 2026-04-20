import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crossing-graded-skein-expansion",
  title:
    "Crossing-graded expansion of the categorical mass",
  interprets: "conj:mass-volume-factorization",
  tags: [
    "crossing-expansion",
    "skein",
    "quantum-dilogarithm",
    "perturbative",
    "groebner-shirshov",
  ],
  uses: [
    "conj:mass-volume-factorization",
    "prop:thurston-volume-additivity",
    "prop:tower-binding-energy",
  ],
});
