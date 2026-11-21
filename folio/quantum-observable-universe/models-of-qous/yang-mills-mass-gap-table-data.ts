import { table } from "../../schema/builders";
export default table({
  label: "tbl:yang-mills-mass-gap-table-data",
  title: "Data table from conj:yang-mills-mass-gap",
  uses: ["conj:yang-mills-mass-gap"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([vacuum state](#prop:vacuum-state))" },
  ],
  tags: ["extracted-table"],
});
