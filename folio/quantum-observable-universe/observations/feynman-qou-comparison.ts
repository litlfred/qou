import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:atom-mass-full-hecke",
  label: "rem:feynman-qou-comparison",
  title:
    "Feynman vs QOU: term-by-term atomic mass comparison",
  tags: [
    "mass",
    "feynman",
    "bethe-weizsacker",
    "SEMF",
    "wedderburn",
    "binding-energy",
    "comparison",
  ],
  uses: ["rem:atom-mass-full-hecke"],
  cites: [
    "hammer2019",
    "jones1985",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness**: `feynman-qou-comparison.witness.json`." },
  ],
});
