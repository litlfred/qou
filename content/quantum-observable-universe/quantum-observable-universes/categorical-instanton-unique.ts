import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-instanton-unique",
  title: "Uniqueness of categorical instantons (moduli)",
  lean: { ref: "qou:QOU.CategoricalInstanton.unique_up_to_gauge",
    validation: "not_checked",
  },
  uses: ["prop:categorical-instanton-exists"],
  proofs: ["prf:categorical-instanton-unique"],
  tags: ["uniqueness", "instanton", "moduli"],
});
