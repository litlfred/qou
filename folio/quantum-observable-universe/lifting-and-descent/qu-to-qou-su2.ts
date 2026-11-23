import { example } from "../../schema/builders";

export default example({
  interprets: "thm:qu-to-qou",
  label: "ex:qu-to-qou-su2",
  title:
    "From quantum universe to QOU: $\\mathrm{SU}(2)$ verification",
  tags: ["su2", "main-theorem", "qou", "descent"],
  uses: ["thm:qu-to-qou", "ex:yekutieli-lifting-su2"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; see the [proof of QU-to-QOU](#prf:qu-to-qou)." },
  ],
});
