import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-instanton-exists",
  title: "Existence of categorical instantons",
  lean: {
    decl: "QOU.CategoricalInstanton.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-instanton",
    "def:categorical-connection",
    "def:q-hodge-star",
  ],
  proofs: ["prf:categorical-instanton-exists"],
  tags: ["existence", "instanton", "self-duality"],
});
