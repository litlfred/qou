import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:jet-prolongation-categorical-jet",
  lean: { ref: "qou:QOU.LiftingDescent.LiftingDescentRoot.jetRetract_comp_jetSection" },
  title: "The base object is a direct summand of the jet object $J^1(S)$",
  tags: ["kahler-differential", "jet-bundle", "direct-summand"],
  uses: ["def:categorical-jet"],
  examples: ["rem:jet-comul-does-not-restrict"],
  proofs: ["prf:jet-prolongation-categorical-jet"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body:
        "Restated on the owner ruling of 2026-11-22 (card \"Switch to (S⊗S)/I²\"): the jet object is " +
        "$(S \\otimes S)/I^2$. Lean: `QOU.LiftingDescent.jetRetract_comp_jetSection` ($r \\circ \\ell = \\mathrm{id}$) " +
        "and `ker_jetRetract` ($\\ker r = I/I^2$), file `QOU/LiftingDescent/JetModuleSplitting.lean`, sorry-free. " +
        "The failure of the old object is `not_injective_into_naiveJet_self`. The previous statement (the " +
        "complement of $\\ker m$ in $A \\otimes A$, `kahlerOmega_isCompl`) stays true and proved, but no " +
        "longer describes the jet object.",
    },
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
