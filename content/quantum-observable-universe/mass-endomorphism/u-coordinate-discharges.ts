import { remark } from "../../schema/builders";

export default remark({
  label: "rem:u-coordinate-discharges",
  interprets: "rem:ck-extraction-from-algebraic-rules",
  title:
    "Macdonald coordinate $u = q^2$ discharges — closed-form rational identities replacing $\\mathtt{Real.sqrt}$-laden scalar invariants ($b^2 = (u^2+u+1)/(u+1)^2$, $\\dim_q^2 V_{(2,1)} = u + 2 + u^{-1}$, etc.)",
  uses: ["rem:h3-hecke-idempotents"],
  cites: [
    "macdonald1995",
    "hoefsmit1974",
    "wenzl1988",
  ],
  tags: [
    "lean-infrastructure",
    "macdonald-coordinate",
    "u-substitution",
    "rational-identities",
    "explicit-residual",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**All theorems sorry-free.** Six concrete scalar identities backed\nby `field_simp + ring` proofs. This addresses the reviewer's repeated\n\"vacuous True / concrete mathematical statement\" critiques at the\n**scalar-invariant** level. The full matrix-level proofs (Yang-Baxter\ncubic on the V_(2,1) Hoefsmit matrices, etc.) remain open R&D, but\nthe scalar discharges are now substantive.",
    },
  ],
});
