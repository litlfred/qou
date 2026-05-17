import { remark } from "../../schema/builders";

export default remark({
  label: "rem:post-pr665-open-rd-inventory",
  lean: {
    ref: "qou:QOU.BraidKnot.post_pr665_open_rd_inventory",
    validation: "not_checked",
  },
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
