import { proof } from "../../schema/builders";

export default proof({
  label: "prf:nuclear-groebner-reduction",
  title: "Proof of nuclear groebner reduction",
  uses: [
    "prop:nuclear-groebner-reduction",
    "def:hecke-normal-form",
    "prop:tm-gs-normal-form",
    "unital-groebner-bases:def:groebner-basis",
    "unital-groebner-bases:def:division-algorithm",
    "unital-groebner-bases:def:admissible-system",
  ],
  cites: ["bergman1978"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: the Lean sibling states `nuclear_groebner_reduction` and defers the confluence certificate via `sorry` (`-- Ref: [leitner2026]`), reducing to the admissible-system machinery formalised in the unital-Gröbner-bases module.",
    },
  ],
});
