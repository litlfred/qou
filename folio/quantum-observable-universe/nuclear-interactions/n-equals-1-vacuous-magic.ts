import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:n-equals-1-vacuous-magic",
  title: "Vacuous primality at $n = 1$",
  lean: {
    ref: "qou:QOU.Interactions.AlgebraicPrimality.one_isAlgebraicallyPrime",
    validation: "not_checked",
  },
  uses: ["def:algebraic-primality"],
  tags: [
    "magic-numbers",
    "primality",
    "base-case",
    "vacuous-truth",
    "proved",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
