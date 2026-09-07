import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-jet-prolongation",
  lean: { ref: "qou:QOU.categorical_jet_prolongation",
    validation: "not_checked",
  },
  title: "Jet prolongation",
  proofs: ["prf:categorical-jet-prolongation"],
  tags: ["jet-bundle", "frobenius-hopf", "category-theory"],
  uses: ["def:categorical-jet"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-jet-prolongation-0.svg", blockIndex: 0, hash: "4cae20680c94" },
  ],

  authorNotes: [
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**Was an axiom, and a vacuous one; now a theorem.** " +
        "`categorical_jet_prolongation` asserted " +
        "`∃ jet : JetPreservesQU C, jet.original = fh`, which is " +
        "discharged by taking `jet := fh` with `jetEval` and " +
        "`unitSection` both the identity: `eval_preserves_mul` closes by " +
        "`tensor_id`, and the identity is a monomorphism. So the " +
        "existential said only that the trivial prolongation exists. " +
        "`JetPreservesQU` has no field distinguishing `jet` from " +
        "`original` -- no first-order structure, and nothing requiring " +
        "`jetEval` to be a genuine evaluation -- so the prolongation " +
        "content is nowhere in the type. Adding it is a structure " +
        "refactor and is not guessed at here. Separately, the library " +
        "declaration of the same name " +
        "(`QOU/QuantumObservableUniverse/Instanton.lean`) is a " +
        "self-assuming projection: it takes a " +
        "`CategoricalJetProlongation` and returns that record's own " +
        "`commutes` field, the §3b-cond item 5 shape. Recorded as an " +
        "observation; this block resolves to the sibling.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
