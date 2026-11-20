import { proof } from "../../schema/builders";

export default proof({
  label: "prf:residue-at-root",
  title: "Proof of residue at root",
  uses: ["prop:residue-at-root", "conj:gs-residue-at-root-existence"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): on the Habiro completion (the class `ResidueAtRoot` in the Lean encoding); every" },
  ],
});
