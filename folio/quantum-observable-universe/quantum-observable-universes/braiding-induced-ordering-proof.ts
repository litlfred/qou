import { proof } from "../../schema/builders";

export default proof({
  label: "prf:braiding-induced-ordering",
  title: "Proof of braiding induced ordering",
  uses: ["prop:braiding-induced-ordering"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean declaration `QOU.braiding_induced_ordering_holds` proves both\nparts: well-foundedness (`degLex_wellOrdered`) and compatibility with\nconcatenation (`degLex_admissible`).  No braiding hypothesis is used." },
  ],
});
