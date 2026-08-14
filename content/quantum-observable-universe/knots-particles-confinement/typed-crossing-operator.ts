import { definition } from "../../schema/builders";

export default definition({
  label: "def:typed-crossing-operator",
  title: "Typed crossing operator",
  tags: [
    "crossing",
    "quark",
    "hecke-algebra",
    "borromean",
    "flavor",
    "skein",
  ],
  lean: { ref: "qou:QOU.Braiding.TypedCrossingOperator",
    validation: "not_checked",
  },
  // The operator is defined per *pair* of strands. That this is enough to
  // resolve every crossing in the link — that no three-strand vertex needs
  // an operator of its own — is prop:pairwise-interaction-decomposition.
  uses: ["prop:pairwise-interaction-decomposition"],
});
