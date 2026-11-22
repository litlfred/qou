import { proof } from "../../schema/builders";

export default proof({
  label: "prf:residue-at-root",
  title: "Proof of residue at root",
  uses: [
    // conj:gs-residue-at-root-existence removed (qou-tm3c): the projection is constructed in the proof; membership is a hypothesis of the statement.
    "prop:residue-at-root",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): on the Habiro completion (the class `ResidueAtRoot` in the Lean encoding); every" },
  ],
});
