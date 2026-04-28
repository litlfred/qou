import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-resolvent-unique",
  title: "Uniqueness of the $q$-resolvent",
  lean: { ref: "qou:QOU.QResolvent.unique",
    validation: "not_checked",
  },
  uses: ["prop:q-resolvent-exists"],
  proofs: ["prf:q-resolvent-unique"],
  tags: ["uniqueness", "resolvent"],
});
