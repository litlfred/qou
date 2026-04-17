import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-resolvent-exists",
  title: "Existence of the $q$-resolvent",
  lean: {
    decl: "QOU.QResolvent.exists",
    validation: "not_checked",
  },
  uses: [
    "def:q-resolvent",
    "def:q-heat-equation",
    "prop:categorical-laplace-exists",
  ],
  proofs: ["prf:q-resolvent-exists"],
  tags: ["existence", "resolvent"],
});
