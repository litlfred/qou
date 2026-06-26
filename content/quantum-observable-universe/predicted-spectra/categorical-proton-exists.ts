import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "status", date: "2026-06-26", body: "The current Lean formalization relies on a `sorry`-free weak proxy theorem (`CategoricalProton.exists`), which instantiates a structure with unconstrained real fields instead of rigorous LP-stability bounds. Expanding this proxy into a complete proof of the stated Frobenius-stability is a highly plausible formalization goal. The obstacle is solely computational—implementing the Hecke normal form (NF) and linear-programming dual verification within the proof assistant. The underlying mathematics guarantees the stability of the $(\\mathfrak{u}, \\mathfrak{u}, \\mathfrak{d})$ Borromean configuration, so this is a technical formalization gap rather than a conceptual one." },
  ],
  label: "prop:categorical-proton-exists",
  title: "Existence of the categorical proton",
  lean: { ref: "qou:QOU.CategoricalProton.exists",
    validation: "not_checked",
  },
  proofs: ["prf:categorical-proton-exists"],
  tags: ["existence", "proton", "baryon"],
});
