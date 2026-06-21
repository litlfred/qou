import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v21-hoefsmit-matrix-derivation",
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "V_(2,1) Hoefsmit 2×2 matrix derivation scaffolding: scalar trace + Hecke-quadratic identities + Laurent decomposition of the closed form $-(q^4+1)(q^2-1)/(4q^3)$",
  uses: ["rem:chi-per-irrep-cyclotomic-closed-forms"],
  cites: ["hoefsmit1974", "jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "v21-hoefsmit",
    "matrix-derivation",
    "laurent-decomposition",
    "scaffolding",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probe_per_wedderburn_block_ck.py",
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "**Closed at the rational-identity level** (5 theorems sorry-free):\nfactored $\\leftrightarrow$ polynomial, Laurent decomposition, numerical checks\nat q=1, q=2.\n\n**Matrix-product trace identity STATED** with explicit matrices\nand word; proof marked sorry with `-- Ref:` to the sympy\nverification per AGENTS.md §1.\n\nThis honestly captures both what's formally proved and what's\nempirically backed.",
    },
  ],
});
