import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-q-ext-deriv-unique",
  title: "Uniqueness of the categorical $q$-exterior derivative",
  lean: { ref: "qou:QOU.CategoricalQExtDeriv.unique",
    validation: "not_checked",
  },
  uses: ["prop:categorical-q-ext-deriv-exists"],
  proofs: ["prf:categorical-q-ext-deriv-unique"],
  tags: ["uniqueness", "q-ext-deriv"],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
