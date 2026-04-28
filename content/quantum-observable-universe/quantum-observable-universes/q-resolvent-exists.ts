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
    "prop:q-heat-kernel-peter-weyl",
  ],
  proofs: ["prf:q-resolvent-exists"],
  tags: ["existence", "resolvent"],
});
