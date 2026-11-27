import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qu-to-qou",
  title: "Proof of QU with observability and categorical lifting is a QOU",
  uses: ["thm:qu-to-qou"],
  authorNotes: [
    { kind: "note", date: "2026-11-24", body: "Relocated from block prose (paper-commentary-audit drain): earlier versions of this theorem asserted a perpetual obstruction $\\kappa_n \\neq 0$ at every level of the jet-prolongation tower via a complementary-subgroup decomposition in $H^2(\\mathcal{S}, \\mathcal{B})$; that claim does not hold on closed surfaces." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is proved in Lean as `QOU.CentralExtension.PresheafCentralExtension.exists_lift_iff`, for a central extension of presheaves of groups that is exact and central on every section group, and a cocycle with a local lift on overlaps." },
  ],
});
