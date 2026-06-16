import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-chain-convergence-mechanisms",
  lean: {
    ref: "qou:QOU.BraidKnot.categorical_chain_convergence_mechanisms",
    validation: "not_checked",
  },
  title:
    "Convergence of $\\mathfrak{Q}_\\beta^{\\text{cat}}$'s infinite product: per-knot c(K) brane-tower bound + inter-knot linking-number locality (Habiro-ring interpretation)",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  cites: [
    "habiro2002",
    "jones1985",
  ],
  tags: [
    "habiro-ring",
    "pre-archimedean",
    "convergence",
    "linking-number",
    "locality",
    "asymptotic-freedom",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_inter_knot_decoupling.py",
    witness: [
      "folio-assistant/computations/c-k-beta-decay-bound.witness.json",
      "folio-assistant/computations/inter-knot-decoupling.witness.json",
      "folio-assistant/computations/q-beta-cat-per-factor-decomposition.witness.json",
    ],
    status: "experimental",
  },
});
