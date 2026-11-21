import { proof } from "../../schema/builders";

export default proof({
  label: "prf:centre-cocentre-descent",
  title: "Proof of the centre–cocentre splitting",
  uses: ["thm:centre-cocentre-descent"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** The sibling file proves items 1–5 over a generic commutative ring (`decomp`, `decomp_unique`, `desc_idem`, `desc_mul_central`, `trace_eq_trace_desc`, `desc_map_auto`, `desc_map_anti`, `refl_involutive`). For item 7 it proves the retraction step and the matrix relations and non-commutation. The step \"the relations define a map out of $H_3(q)$\" is the presentation of $H_3(q)$, which is not formalised. `isCompl_of_comm` shows the splitting hypothesis is not vacuous. Item 6 is not formalised. $\\blacksquare$" },
  ],
});
