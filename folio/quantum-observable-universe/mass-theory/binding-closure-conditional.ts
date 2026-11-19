import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:binding-closure-conditional",
  lean: {
    ref: "qou:QOU.Mass.binding_closure_conditional",
    validation: "validated",
  },
  title: "Binding closure, conditional on the per-term mass identity",
  uses: [
    "conj:binding-manybody-eq-jet-filtration",
    "lem:bond-order-eq-jet-degree",
    "prop:sw-period-residue-sum",
    "prop:binding-genfun-qdifference",
  ],
  proofs: ["prf:binding-closure-conditional"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
