import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-q-connection-unique",
  title: "Uniqueness of the categorical $q$-connection",
  lean: { ref: "qou:QOU.CategoricalQConnection.unique",
    validation: "not_checked",
  },
  uses: [
    "prop:categorical-q-connection-exists",
    "prop:categorical-connection-unique",
  ],
  proofs: ["prf:categorical-q-connection-unique"],
  tags: ["uniqueness", "q-connection"],
});
