import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-connection-exists",
  title: "Existence of categorical connections",
  lean: { ref: "qou:QOU.CategoricalConnection.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-connection",
    "def:quantum-universe",
  ],
  proofs: ["prf:categorical-connection-exists"],
  tags: ["existence", "connection"],
});
