import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qu-to-qou",
  title: "Proof of QU with observability and categorical lifting is a QOU",
  uses: ["thm:qu-to-qou"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is proved in Lean as `QOU.CentralExtension.PresheafCentralExtension.exists_lift_iff`, for a central extension of presheaves of groups that is exact and central on every section group, and a cocycle with a local lift on overlaps." },
  ],
});
