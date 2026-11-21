import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:jet-prolongation-categorical-jet",
  lean: { ref: "qou:QOU.LiftingDescent.kahlerOmega_isCompl" },
  title: "The jet object $J^1(A)$ is built from a direct summand of $A \\otimes A$",
  tags: ["kahler-differential", "jet-bundle", "direct-summand"],
  uses: [],
  examples: ["rem:jet-comul-does-not-restrict"],
  proofs: ["prf:jet-prolongation-categorical-jet"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Retracted on owner instruction (option 1, 2026-11-21). The lemma used to say that $J^1(A)$ " +
        "strictly inherits a Frobenius–Hopf structure $(\\Delta', \\varepsilon', S')$ from $A$. Read as " +
        "\"$\\Delta$ restricts to $\\Omega^1(A)$\", that is false for every bialgebra whose multiplication is " +
        "not injective (`QOU.LiftingDescent.kahlerOmega_eq_bot_of_comul_restricts`; see " +
        "`rem:jet-comul-does-not-restrict`). Only the object-level part is kept. The proof of " +
        "`prop:jet-prolongation` cited the inheritance and now has a gap there.",
    },
  ],
});
