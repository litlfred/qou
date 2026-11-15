import { table } from "../../schema/builders";

export default table({
  label: "tbl:bring-embeddable-knots-table-data",
  title: "Bring-embeddable knot/link table by Seifert genus ($g = 0$ to $4$)",
  caption:
    "Canonical knots and links whose Seifert genus $g(K) \\leq 4$ " +
    "(the Bring's-surface genus bound). For each genus: canonical " +
    "representative(s), braid word, and hyperbolic volume (depth-2 period).",
  uses: ["rem:bring-embeddable-knots"],
  tags: ["bring-surface", "knot-table", "genus-bound", "braid-word"],
});
