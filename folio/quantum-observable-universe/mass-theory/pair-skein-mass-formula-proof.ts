import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pair-skein-mass-formula",
  title: "Proof of the pair Skein mass formula",
  uses: ["lem:pair-skein-mass-formula"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean module names it `skeinNormaliserC` for the same reason." },
  ],
});
