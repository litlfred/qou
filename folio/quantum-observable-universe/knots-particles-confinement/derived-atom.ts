import { definition } from "../../schema/builders";

export default definition({
  label: "def:derived-atom",
  title: "Derived atom $\\mathcal{A}(Z, N)$ from pair production",
  lean: {
    ref: "qou:QOU.Interactions.DerivedAtom",
    validation: "not_checked",
  },
  tags: [
    "atom",
    "derived",
    "pair-production",
    "nucleon",
    "confinement",
    "normal-form",
    "general",
  ],
  uses: ["def:quark-antiquark-production", "def:photon"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body:
        "**Edge re-pointed.** This definition used `prop:four-term-pair-nucleon`, now the conjecture conj:four-term-pair-nucleon (owner card 2026-11-21). " +
        "The six steps name the γγ → qq̄ → 𝓑₃ construction, which needs the pair-production and photon definitions, not the conjectured nucleon net values; " +
        "the Lean `QOU.Interactions.DerivedAtom` does not import the nucleon file. Whether 𝓑₃ is the right confinement operator is a separate question, not settled by this edge.",
    },
  ],
});
