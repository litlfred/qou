import { remark } from "../../schema/builders";

export default remark({
  label: "rem:groebner-nf-computation",
  title: "Gröbner normal form computation with quotient ideals",
  tags: [
    "groebner-basis",
    "normal-form",
    "hecke-algebra",
    "quotient-ideal",
    "transfer-matrix",
    "shell-closure",
    "pauli-exclusion",
    "computational-witness",
  ],
  interprets: "prop:shell-closure-normal-form",
  uses: [
    "prop:nuclear-groebner-reduction",
    "prop:beta-decay-transfer-matrix",
    "prop:skein-polynomial-transfer-matrix",
    "thm:groebner-shirshov-energy",
    "def:stable-nucleus",
  ],
});
