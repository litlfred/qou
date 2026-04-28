import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-q-ext-deriv-exists",
  title: "Existence of the categorical $q$-exterior derivative",
  lean: { ref: "qou:QOU.CategoricalQExtDeriv.exists",
    validation: "not_checked",
  },
  uses: ["def:categorical-q-ext-deriv"],
  proofs: ["prf:categorical-q-ext-deriv-exists"],
  tags: ["existence", "q-ext-deriv", "q-deformed"],
});
