import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-resolvent-exists",
  title: "Existence of the $q$-resolvent",
  lean: { ref: "qou:QOU.QResolvent.exists",
    validation: "not_checked",
  },
  uses: [
    "def:q-resolvent",
    "prop:categorical-laplace-exists",
  ],
  proofs: ["prf:q-resolvent-exists"],
  tags: ["existence", "resolvent"],
});
