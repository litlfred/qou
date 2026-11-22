import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:binding-closure-conditional",
  lean: {
    ref: "qou:QOU.Mass.binding_closure_conditional",
    validation: "validated",
  },
  title: "Binding closure, conditional on the per-term mass identity",
  uses: [
    // conj:bond-order-eq-jet-degree removed (qou-tm3c): input (C) is assumed explicitly (class field body_is_series); the theorem does not use the conjecture's truth.
    "prop:sw-period-residue-sum",
    "prop:binding-genfun-qdifference",
  ],
  proofs: ["prf:binding-closure-conditional"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is a **rigorous-conditional** result: it is fully verified by Lean\nmodulo the single named input (B) — the per-term mass identity — which is\naxiomatised as the class `BindingClosureInput`." },
  ],
});
