import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:kummer-tower",
  title: "The Kummer tower and persistence of the obstruction",
  tags: [
    "kummer",
    "filtration",
    "obstruction",
    "euler-characteristic",
  ],
  uses: [
    "thm:qu-to-qou",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; see the [proof of QU-to-QOU](#prf:qu-to-qou)." },
  ],
});
