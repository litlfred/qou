import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:direct-limit-algebra",
  label: "rem:direct-limit-lusztig",
  title: "Direct limit algebra and the Lusztig integral form",
  tags: ["lusztig", "integral-form", "divided-power"],
  uses: ["def:quaternionic-spectral-resolvents"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This ensures that the quaternionic jet embedding ([quaternionic spectral resolvents](#def:quaternionic-spectral-resolvents)) remains robust under the arithmetic :refterm[descent]{#descent} to $M_0$." },
  ],
  cites: [
    "lusztig1993",
  ],
});
