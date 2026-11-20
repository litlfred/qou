import { proof } from "../../schema/builders";

export default proof({
  label: "prf:nuclear-groebner-reduction",
  title: "Proof of nuclear groebner reduction",
  uses: ["prop:nuclear-groebner-reduction"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling states `nuclear_groebner_reduction` and defers the confluence certificate via `sorry` (`-- Ref: [leitner2026]`). This certificate reduces to the admissible-system machinery already formalised in the unital-Gröbner-bases paper." },
  ],
});
