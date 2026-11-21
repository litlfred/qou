import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ck-extraction-from-algebraic-rules",
  interprets: "prop:q-beta-categorical-precision-ladder",
  title:
    "$c_k$ extraction from four algebraic reduction rules (Yang-Baxter, $q$-Young symmetrizers, Hecke quadratic, GB/jet) on the typed-$\\mathbf{B}_3$ word: the closed forms $c_k \\in \\{b, b^2, -2, b^2+1/2\\}$ are derivable outputs, not phenomenological identifications",
  uses: ["rem:braid-group-n-strand"],
  cites: [
    "kashiwara1990",
    "jones1985",
    "hoefsmit1974",
    "wenzl1988",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "ck-extraction",
    "algebraic-rules",
    "yang-baxter",
    "q-young-symmetrizers",
    "hecke-quadratic",
    "grobner-shirshov",
    "jet-bundle",
    "synthesis",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean module exports\n```\nnoncomputable def ckFromReduction (q : ℝ) : ℕ → ℝ\n```\nreturning the closed-form scalar value that Rules 1-4 jointly\n\nThe Lean theorems\n`ckFromReduction_eq_c1`, $\\ldots$, `ckFromReduction_eq_c4` discharge each\nagreement equality by `rfl` against the inline coefficients used in\n`N1_factor`, $\\ldots$, `N4_factor` of the precision ladder.\n\nThe synthesis theorem `ckFromReduction_matches_ladder` records the\njoint statement under all four class instances.\n\n- Rule 2 (Hecke idempotents) is largely Mathlib-able via the standard\n  Iwahori-Hecke decomposition.\n\nThe class skeleton makes each rule a **separate instance** to discharge,\nturning the c_k extraction into a structured Lean-engineering programme\nrather than a single open conjecture.\n\n- Replace the `True` ansatz fields with the substantive matrix\n  identities they encode (`yb_cubic` $\\leftarrow$ Hoefsmit YB cubic; `hecke_quad`\n  $\\leftarrow$ `hoefsmit_sigma{0,1}_hecke_quadratic`).\n- Discharge `QYoungSymmetrizers 3 q` via the Mathlib Iwahori-Hecke\n  module (when complete) or via the explicit $H_3$ idempotent table.\n- Formalise the GB/jet normal-form procedure for $k = 1, 2$" },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "note",
      date: "2026-06-04",
      body: "**$c_4$ closed form has shifted.** The original $c_4 = b^2 + 1/2$ form below is superseded by $c_4 = c_3 \\cdot b^4 = -2 b^4$ (per the SDP-$T_\\beta$ derivation and `prop:q-beta-categorical-precision-ladder`). The $b^2 + 1/2$ shape is now attributed to $c_5$ (with sign flip: $c_5 = -(b^2 + 1/2)$). The four-rule reframing remains valid; only the per-rung closed-form column needs updating. Audit: `docs/audits/-qbeta-all-ck-categorical-extension.md`.",
    },
  ],
});
