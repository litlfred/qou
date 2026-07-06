import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "rem:post-pr665-open-rd-inventory",
  interprets: "rem:ck-extraction-from-algebraic-rules",
  title:
    "Post-PR-#665 open R&D inventory: 6 items + initial finding that the chapter $\\sigma_1$ Hoefsmit convention does NOT satisfy the Yang-Baxter cubic with $\\sigma_0 = \\mathrm{diag}(q, -q^{-1})$, requiring $d_1, d_2$ revision",
  uses: [
    "rem:ck-extraction-from-algebraic-rules",
    "prop:hoefsmit-V21-cos-symmetrization",
  ],
  cites: [
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "open-rd",
    "negative-result",
    "yang-baxter",
    "hoefsmit-convention",
    "post-pr665",
  ],
});
