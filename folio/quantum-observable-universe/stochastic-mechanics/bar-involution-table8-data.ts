import { table } from "../../schema/builders";
export default table({
  label: "tbl:bar-involution-table8-data",
  title: "Data table 8 from def:bar-involution",
  uses: ["def:bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | `IsBarSymmetric x` | Lean predicate $\\overline x = x$ |\n| `IsBarAntiSymmetric x` | Lean predicate $\\overline x = -x$ |" },
  ],
});
