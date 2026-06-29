import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:optimal-normal-form-valley",
  title:
    "Optimal Gröbner–Shirshov normal form has exactly $A$ terms in the valley of stability",
  tags: [
    "groebner-basis",
    "normal-form",
    "optimal-basis",
    "valley-of-stability",
    "transfer-matrix",
    "markov-trace",
    "nuclear-structure",
  ],
  lean: {
    ref: "qou:QOU.OptimalNF.optimal_nf_is_standard_basis",
    validation: "stub",
  },
  uses: [
    "def:gs-quotient-ideals-I8-I9",
    "prop:shell-closure-normal-form",
  ],
});
