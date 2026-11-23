import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-coupling-fixed-point-derivation-status",
  title: "Component assembly, derivation, and open-input status of the $\\alpha_{EM}$ fixed point",
  interprets: "prop:em-coupling-fixed-point",
  uses: [
    "prop:em-coupling-fixed-point",
    "prop:em-coupling-projection",
    "prop:alpha-em-categorical-trace-ratio",
    "prop:em-coupling-bring-zero-mode",
    "prop:photon-ir-zero-mode-bring",
  ],
  tags: ["alpha-em", "fine-structure", "fixed-point", "bloch-group", "formalization-status"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Lean proves the tree/zero-mode assembly of $T$, the algebraic equivalence of the fixed-point, and the derivation of $P(\\alpha)=0$. The class remains uninhabited. No fabricated instance attempts to close the primary conjecture." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The class carries the hypothesis, and the theorem derives the conclusion. The lemma [`QOU.ArchimedeanUniverse.fixedPoint_iff_cubic`](em-coupling-fixed-point.lean) establishes the equivalence between the fixed-point equation and the cubic root for $\\alpha \\neq 0$. The main theorem [`QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root`](em-coupling-fixed-point.lean) composes this equivalence with the `b3_normalization` field. The proof is a genuine derivation." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The `b3_normalization` class field axiomatises this." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Its categorical-trace refactoring is proved ([Algebraic identity](#prop:alpha-em-categorical-trace-ratio))." },
  ],
});
