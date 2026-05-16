import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-chain-convergence-mechanisms",
  lean: {
    ref: "qou:QOU.BraidKnot.categorical_chain_convergence_mechanisms",
    validation: "not_checked",
  },
  title:
    "Convergence of $Q_\\beta^{\\text{cat}}$'s infinite product: per-knot c(K) brane-tower bound + inter-knot linking-number locality (Habiro-ring interpretation)",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "conj:archimedean-remainder-exponential-decay",
    "prop:markov-trace-frobenius-selection",
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
    witness: [
      "../../folio-assistant/computations/c-k-beta-decay-bound.witness.json",
    ],
  },
});
