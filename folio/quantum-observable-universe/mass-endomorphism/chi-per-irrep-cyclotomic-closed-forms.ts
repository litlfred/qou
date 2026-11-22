import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-per-irrep-cyclotomic-closed-forms",
  interprets: "rem:chi-v3-closed-form-proof",
  title:
    "All three $V_\\lambda$ per-irrep character difference closed forms with **cyclotomic factor pattern**: $V_{(3)}, V_{(1,1,1)}$ → $\\Phi_4^2$; $V_{(2,1)}$ → $\\Phi_8$; denominator powers $q, q^3, q^5$ track content sum",
  uses: ["rem:chi-v3-closed-form-proof"],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "per-wedderburn-block",
    "closed-form",
    "cyclotomic",
    "v21-hoefsmit-matrix",
    "conjugate-partition-symmetry",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probe_per_wedderburn_block_ck.py",
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): canonical word order\nfrom `atomic_braid_to_crossings`.\n\n## Lean theorems exported\n\nAll proved by `field_simp + ring` after unfolding:" },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "**All three V_λ formally closed**, cyclotomic pattern documented,\ncompute wired, lit pointers in place. The substantive next R&D step\nis to derive the Hoefsmit-matrix-expansion formula for V_(2,1)\n**from the matrix algebra directly** in Lean (currently the closed\nform is recorded as a verified rational identity, with the\nmatrix-product derivation backed empirically by sympy in the probe).",
    },
  ],
});
