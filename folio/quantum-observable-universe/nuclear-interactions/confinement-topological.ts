import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-topological",
  title: "A matrix inequality in the standard representation of $H_3(q)$ (confinement LP evidence)",
  tags: [
    "confinement",
    "topological",
    "linear-programming",
    "gram-matrix",
    "negative-eigenvalue",
    "borromean",
  ],
  lean: { ref: "qou:QOU.Interactions.gram_indefinite_witness",
    validation: "not_checked",
  },
  uses: ["prop:confinement-lp"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** `gram_indefinite_witness` proves only that L₊² + L₋² ≠ 2·L₊L₋ in the 2×2 standard representation, by comparing (0,0) entries. It does not compute the 6×6 Gram matrix, its signature, any linear program, or any uniqueness over braids. The former statement made three claims (LP optimal value 0 via a negative Gram eigenvalue; the optimum is not a braid image; B₃ = (σ₀σ₁⁻¹)³ is the unique length-≤6 braid hitting n_target for proton and neutron) and titled the block 'Confinement is topological (LP proof)'; none of the three is proved here, and all are dropped. Note that L₊L₋ and L₋L₊ differ, so the inequality is not by itself the statement (L₊ − L₋)² ≠ 0. Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P16).",
    },
  ],
});
