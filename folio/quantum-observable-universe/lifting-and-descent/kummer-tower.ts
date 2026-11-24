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
    { kind: "note", date: "2026-11-24", body: "Relocated from block prose (paper-commentary-audit drain): earlier versions of this remark derived a perpetual obstruction at every level of the jet-prolongation tower from a complementary-subgroup decomposition $\\kappa_n = \\kappa_0 + \\delta_n$; that decomposition was retracted." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; see the [proof of QU-to-QOU](#prf:qu-to-qou)." },
  ],
});
