import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pair-graph-regime-trichotomy",
  title: "Proof of the pair-graph regime trichotomy",
  uses: ["prop:pair-graph-regime-trichotomy"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** `two_mul_choose_two`, `choose_two_sub_euler` (the identity), `choose_three_eq_zero_iff`, `regime_trichotomy`, `cutoffs_eq_structural` and `maxContacts_eq_choose_two_iff` in the sibling file. Sorry-free, lean-direct exit 0. $\\blacksquare$" },
  ],
});
