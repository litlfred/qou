import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-q-ext-deriv-unique",
  title: "Uniqueness of the categorical $q$-exterior derivative",
  lean: {
    decl: "QOU.CategoricalQExtDeriv.unique",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-q-ext-deriv",
    "prop:categorical-q-ext-deriv-exists",
  ],
  proofs: ["prf:categorical-q-ext-deriv-unique"],
  tags: ["uniqueness", "q-ext-deriv"],
});
