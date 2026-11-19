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
    {
      kind: "note",
      body: "Tabulated comparison data recorded in witness feynman-qou-comparison.witness.json.",
    },
  ],
});
