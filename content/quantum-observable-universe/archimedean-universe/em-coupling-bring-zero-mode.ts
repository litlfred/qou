import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:em-coupling-bring-zero-mode",
  title:
    "Additive Bring zero-mode form $1/\\alpha_{EM} = q\\cdot[9]_q\\cdot[10]_q + 2g/(4\\pi(g-1))$ (conditional)",
  uses: [
    "prop:em-coupling-projection",
    "prop:force-carrier-bring-uniqueness",
    "prop:exterior-square-borromean",
    "prop:archimedean-functor-uniqueness",
    "rem:figure-8-archimedean-illustration",
    "conj:dilogarithm-archimedean-limit",
    "conj:bring-hyperbolic-knot-bloch-decomposition",
  ],
  cites: ["jones1987", "kassel1995", "suslin1991", "bloch2000"],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "alpha-em",
    "fine-structure",
    "brings-surface",
    "genus-4",
    "zero-mode",
    "gauss-bonnet",
    "conditional-class",
    "derivation-lead",
  ],
  lean: {
    ref: "qou:QOU.Descartes.bring_zero_mode_additive_form",
    validation: "not_checked",
  },
});
