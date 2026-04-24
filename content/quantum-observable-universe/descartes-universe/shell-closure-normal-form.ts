import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-closure-normal-form",
  title:
    "Shell closure as symmetric Poincaré distribution in the Hecke normal form",
  tags: [
    "shell-closure",
    "normal-form",
    "hecke-algebra",
    "poincare-polynomial",
    "magic-numbers",
    "bruhat-order",
    "nuclear-structure",
    "groebner-basis",
  ],
  lean: {
    decl: "QOU.OptimalNF.optimal_nf_is_standard_basis",
    validation: "stub",
  },
  uses: [
    "prop:nuclear-groebner-reduction",
    "thm:groebner-shirshov-energy",
    "prop:integer-stability",
    "def:stable-nucleus",
    "prop:beta-stability",
    "prop:skein-polynomial-transfer-matrix",
  ],
});
