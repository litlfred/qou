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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): even when their defining formulas require `Real.sqrt` over $q$.\n\nThis provides concrete, closed-form Lean identities that algebraically verify the explicit-residual discharges\n\nWe export each scalar identity as a Lean theorem. Because the substitution removes square roots, the `field_simp + ring` tactic closes every proof without opaque axioms.\n\nPreviously, explicit-residual discharges at the class level (such as `⟨0, rfl⟩`) appeared abstractly trivial: the residual evaluates to $0$, but no concrete computation connects this to the underlying substrate arithmetic. The $u$-coordinate identities express the underlying scalars as rational functions in a single variable $u$. This enables `ring` and `field_simp` to verify the equalities mechanically.\n\nFor example, the abstract class field `HeckeQuadraticAllGenerators 3 q .hecke_quad_residual_eq_zero` mandates that the residual vanishes. The substantive reason for this vanishing lies in the identity `hecke_root_sum_times_q`: the relation $q \\cdot (q - q^{-1}) = u - 1$ constitutes a non-trivial rational identity closed by `field_simp + ring`.\n\n- `rem:ck-extraction-from-algebraic-rules` references these identities to justify its instances.\n\n- `rem:h3-hecke-idempotents` links its `dimQ_V21^2` computation to `dimQ_V21_sq_in_u`.\n\n- `prop:hoefsmit-V21-cos-symmetrization` establishes a no-sqrt closed form for the Hoefsmit coupling $b^2$ via `hoefsmit_b_sq_in_u`." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "**All theorems sorry-free.** Six concrete scalar identities backed\nby `field_simp + ring` proofs. This addresses the reviewer's repeated\n\"vacuous True / concrete mathematical statement\" critiques at the\n**scalar-invariant** level. The full matrix-level proofs (Yang-Baxter\ncubic on the V_(2,1) Hoefsmit matrices, etc.) remain open R&D, but\nthe scalar discharges are now substantive.",
    },
  ],
});
