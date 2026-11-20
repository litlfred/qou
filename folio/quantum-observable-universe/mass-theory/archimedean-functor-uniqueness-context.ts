import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-functor-uniqueness-context",
  title:
    "Pre-archimedean separation, corollaries, and open problems for the archimedean functor uniqueness",
  interprets: "prop:archimedean-functor-uniqueness",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "archimedean",
    "realization-functor",
    "bloch-wigner",
    "pentagon-identity",
    "pre-archimedean",
    "alpha-em",
  ],
  uses: ["prop:archimedean-functor-uniqueness"],
  cites: ["suslin1991", "bloch2000"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): 3. **Lean formalisation of Suslin1991.** Mathlib has neither\n   `Real.dilog` nor `BlochGroup`. The Lean stub records this as\n   a sorry keyed to [`suslin1991`]; closure depends on upstream\n   Mathlib work." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The two classes taken as `[Instance]` hypotheses by the Lean theorem\n[`QOU.Archimedean.archimedean_functor_uniqueness`](archimedean-functor-uniqueness.lean)\nare the only unproved inputs; both are well-established results\nawaiting Mathlib formalisation (`Real.dilog`, `BlochGroup`, the\nSuslin map)." },
    {
      kind: "deprecated",
      body: "The multiplicative gluon-octet PSLQ form was a legacy conjecture, removed from the corpus and superseded by prop:em-coupling-bring-zero-mode.",
    },
  ],
});
