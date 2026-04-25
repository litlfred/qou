import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-q-connection-exists",
  title: "Existence of the categorical $q$-connection",
  lean: { ref: "qou:QOU.CategoricalQConnection.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-q-connection",
    "prop:categorical-connection-exists",
    "def:substrate-parameter",
  ],
  proofs: ["prf:categorical-q-connection-exists"],
  tags: ["existence", "q-connection"],
});
