import { proof } from "../../schema/builders";

export default proof({
  authorNotes: [
    { kind: "status", date: "2026-09-04", body: "Item 1 corrected: it asserted $\\mathcal{W}(1) = 0$ as the mechanism for the classical vanishing of beta decay. The derived closed form gives $\\mathcal{W}(1) = 1/4$ (Lean `QOU.Braiding.WeakVertexT35.weakVertexTrace_one`); the classical vanishing is carried by the $q$-prefactor (`qPrefactor_classical` in the proposition's Lean), which the sentence now says. Bean `qou-4x7c`." },
  ],
  label: "prf:hadron-half-life",
  title: "Decay rate from $q$ and $\\mu_0$",
  uses: ["prop:hadron-half-life", "prop:trace-ratio-observable", "thm:markov-trace-factorization"],
});
