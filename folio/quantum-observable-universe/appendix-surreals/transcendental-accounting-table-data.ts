import { table } from "../../schema/builders";
export default table({
  label: "tbl:transcendental-accounting-table-data",
  title: "Transcendental period accounting by depth",
  uses: ["rem:transcendental-accounting"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-24", body: "Relocated from the block prose by the reading-order drain (qou-d4kh): [Surreal bound for the Riemann hypothesis: why $\\delta = 0$ on the critical line](#rem:rh-surreal-bound) envelope" },
  ],
});
