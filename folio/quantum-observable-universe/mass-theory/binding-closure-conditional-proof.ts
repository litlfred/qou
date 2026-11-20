import { proof } from "../../schema/builders";

export default proof({
  label: "prf:binding-closure-conditional",
  title: "Proof of binding closure conditional on the per-term mass identity",
  uses: [
    "thm:binding-closure-conditional",
    "lem:bond-order-eq-jet-degree",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The\nLean witness [`QOU.Mass.binding_closure_conditional`](#thm:binding-closure-conditional)\ncarries (C) and (B) as the fields of the class `BindingClosureInput` and\nderives the closed form by `Finset.mul_sum` and `Finset.sum_congr` — fully\nverified modulo the class instance, which is exactly input (B)." },
  ],
});
