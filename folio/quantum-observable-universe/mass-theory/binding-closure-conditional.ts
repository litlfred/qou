import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:binding-closure-conditional",
  lean: {
    ref: "qou:QOU.Mass.binding_closure_conditional",
    validation: "validated",
  },
  title: "Binding closure, conditional on the per-term mass identity",
  uses: [
    // conj:binding-manybody-eq-jet-filtration removed (qou-tm3c): the theorem assumes the per-term identity (B) explicitly and derives the conjecture's statement from it; it does not use the conjecture.
    "lem:bond-order-eq-jet-degree",
    "prop:sw-period-residue-sum",
    "prop:binding-genfun-qdifference",
  ],
  proofs: ["prf:binding-closure-conditional"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is a **rigorous-conditional** result: it is fully verified by Lean\nmodulo the single named input (B) — the per-term mass identity — which is\naxiomatised as the class `BindingClosureInput`." },
  ],
});
