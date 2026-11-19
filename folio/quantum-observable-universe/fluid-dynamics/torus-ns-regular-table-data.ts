import { table } from "../../schema/builders";
export default table({
  label: "tbl:torus-ns-regular-table-data",
  title: "Topological and gauge-theoretic contrast between the genus-1 torus and genus-4 Bring surface",
  uses: ["ex:torus-ns-regular"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Updated per owner decision (Q-VO9T-2 = 1, beans qou-nzyr, qou-507c, qou-fm7s): " +
        "row 'NS obstruction | 0 (regular) | != 0 (singular)' is specified as the global surface Euler class " +
        "$e(\\xi) \\in H^2(\\mathcal{S}, \\mathbb{Z})$ (internal model label), and row " +
        "'Contact structure at collision | Degenerates | Non-degenerate' (withdrawn Levi-flattening reading) " +
        "is replaced by the topological Reeb-section property 'Nowhere-vanishing Reeb section on $\\mathcal{S}$ | Exists ($e(\\xi) = 0$) | None ($e(\\xi) = -6$)'.",
    },
  ],
});
