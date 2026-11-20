import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bring-residue-resolvent-context",
  title: "Scaffolded open math, Lean structure, and downstream consequence of the Bring-residue resolvent",
  interprets: "prop:bring-residue-resolvent",
  tags: ["bring-surface", "residue", "resolvent", "alpha-shift"],
  uses: ["prop:bring-residue-resolvent"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the hypothesis is `class BringResidueAtOrder {R} [Field R] (n : ℕ) (q : R)` with sole field `pole_nonzero`; the consequence is `bring_residue_equation` (proof `mul_inv_cancel₀ h.pole_nonzero`); specialisations `bring_residue_at_T_3_5`, `bring_residue_at_T_2_9`, `bring_residue_meson_pair`; uniqueness `bring_residue_subsingleton`.",
    },
  ],
});
