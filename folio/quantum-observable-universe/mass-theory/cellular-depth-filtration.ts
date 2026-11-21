import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cellular-depth-filtration",
  title:
    "Cell-depth filtration of $Z(H_n(q))$: GB-depth as Lusztig's $a$-function, a filtration by ideals that the Goldman involution carries to the $n(\\lambda)$-filtration; conditional parity transfer",
  lean: {
    ref: "qou:QOU.MassCore.CellularDepth.map_mem_F_comp",
  },
  uses: ["prop:shell-schur-weyl-self-duality"],
  cites: ["kazhdan-lusztig1979", "mathas1999", "dipper-james1986", "macdonald1995"],
  tags: ["two-filtration", "gb-depth", "a-function", "kazhdan-lusztig", "centre", "goldman-involution"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , and the values $2$ and $3$ of that conjecture need an additional non-vanishing that item 4 does not give" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): is the provable part of [Two-filtration bridge map in full generality](#conj:two-filtration-bridge-general). It" },
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved algebraic core of conj:two-filtration-bridge-general (issue #8094). GB-depth is fixed as Lusztig's a-function (owner ruling 2026-11-16, card 'Fix GB-depth as which definition?'). The former max-hook statistic is kept under the name max-hook depth. Inputs cited, not formalised: #(e_lambda) = e_lambda' and the identification of the cell a-value with sum_i C(lambda_i, 2). Sibling .lean sorry-free, lean-direct exit 0.",
    },
  ],
});
