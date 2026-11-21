import { proof } from "../../schema/builders";

export default proof({
  label: "prf:shell-closure-normal-form",
  title: "Proof of shell closure normal form",
  uses: ["prop:shell-closure-normal-form"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We formally prove this in Lean." },
  ],
});
