import { remark } from "../../schema/builders";

export default remark({
  label: "rem:groebner-nf-computation",
  title: "Gröbner--Shirshov normal form computation with quotient ideals",
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
  uses: ["prop:beta-decay-transfer-matrix"],
});
