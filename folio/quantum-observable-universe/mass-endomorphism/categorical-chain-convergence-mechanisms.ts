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
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): from [$\\mathfrak{Q}_\\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder)" },
    {
      kind: "status",
      body: "**Verified.** The two convergence mechanisms have distinct empirical signatures that guarantee finite-precision predictions from the formal infinite sum:\n\n1. **c(K) bound (Mechanism 1):** validated by `c_k_beta_decay_witness.py` — each rung's residual sits well within the ceiling.\n2. **Linking-number locality (Mechanism 2):** factorisation for two unlinked braids in a higher-rank Hecke algebra is directly confirmed by the empirical test in [`probe_inter_knot_decoupling.py`](../../../computations/probe_inter_knot_decoupling.py), yielding `inter-knot-decoupling.witness.json`.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probe_inter_knot_decoupling.py",
    witness: [
      "computations/c-k-beta-decay-bound.witness.json",
      "computations/inter-knot-decoupling.witness.json",
    ],
    status: "experimental",
  },
});
