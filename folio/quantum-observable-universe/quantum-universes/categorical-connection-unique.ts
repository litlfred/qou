import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-connection-unique",
  title: "Uniqueness of categorical connections (up to gauge)",
  lean: { ref: "qou:QOU.CategoricalConnection.unique_up_to_gauge",
    validation: "not_checked",
  },
  uses: ["prop:categorical-connection-exists"],
  proofs: ["prf:categorical-connection-unique"],
  tags: ["uniqueness", "connection", "gauge"],
});
