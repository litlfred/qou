import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:em-coupling-fixed-point",
  title:
    "$\\alpha_{EM}$ as the root of the self-consistent fixed-point cubic $-h^2H\\alpha^3 + H\\alpha^2 + T\\alpha - 1 = 0$ (conditional on the $B_3(\\mathbb{C})$ $\\mathcal{O}(\\alpha^2)$ normalization)",
  uses: [
    "prop:em-coupling-projection",
    "prop:em-coupling-bring-zero-mode",
    "prop:photon-ir-zero-mode-bring",
  ],
  cites: ["jones1987", "suslin1991", "bloch2000"],
  tags: [
    "alpha-em",
    "fine-structure",
    "fixed-point",
    "cubic",
    "brings-surface",
    "genus-4",
    "habiro",
    "bloch-group",
    "conditional-class",
    "derivation-lead",
  ],
  lean: {
    ref: "qou:QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Assume the typeclass [`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean) is inhabited at $(q,\\alpha)$." },
    {
      kind: "status",
      body: "Lean file `em-coupling-fixed-point.lean` compiles sorry-free (lean-direct, exit 0). The conditional theorem `alpha_em_is_fixed_point_root` derives the cubic-root characterization `P(α)=0` from the class hypothesis `AlphaEmFixedPointNormalization.b3_normalization` via the sorry-free algebraic equivalence `fixedPoint_iff_cubic` — no stored conclusion field is projected (§3b-cond item 5). The B₃(ℂ) O(α²) normalization is the single open input; the class is left uninhabited (honest open-primary state, §3b-tax) rather than closed by a fabricated `sorry` instance. Tree term `q[9]_q[10]_q` (prop:em-coupling-projection) and zero-mode `2/(3π)` (prop:photon-ir-zero-mode-bring, reused as `QOU.Archimedean.bringZeroModeValue`) enter sorry-free. This route does NOT use the refuted multiplicative Chern-Simons / gluon-octet form.",
    },
  ],
});
