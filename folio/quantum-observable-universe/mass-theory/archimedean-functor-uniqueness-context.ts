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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **(a) Resolves the pre-archimedean concern in\n[additive Bring zero-mode form of $1/\\alpha_{EM}$](#prop:em-coupling-bring-zero-mode).**\nThe $\\pi$ in the additive correction $2/(3\\pi) = 2g/(4\\pi(g-1))$\nat $g=4$ is the unique archimedean shadow of pentagon-coherent\nsubstrate data on Bring's surface. The substrate's pentagon\ncoherence forces the archimedean image to involve $D$ (and hence\n$\\pi$ via $D$'s functional equation); no other transcendental\nshape is admissible. The additive correction is therefore *not*\noutside $R$ — it is the canonical $\\tau_{\\text{arch}}$-image of\n$R$-internal pentagon data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The\n[`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)\ncandidate satisfies this; the gluon-octet PSLQ candidate does not." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , which\n[additive Bring zero-mode form of $1/\\alpha_{EM}$](#prop:em-coupling-bring-zero-mode) replaces" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The additive Bring zero-mode candidate\n[additive Bring zero-mode form of $1/\\alpha_{EM}$](#prop:em-coupling-bring-zero-mode)\nillustrates the second point: the $2/(3\\pi) = 2g/(4\\pi(g-1))$\ncorrection at $g = 4$ is the archimedean shadow of pentagon\ndata on Bring's surface, not a $\\pi$-import outside $R$." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): 3. **Lean formalisation of Suslin1991.** Mathlib has neither\n   `Real.dilog` nor `BlochGroup`. The Lean stub records this as\n   a sorry keyed to [`suslin1991`]; closure depends on upstream\n   Mathlib work." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The two classes taken as `[Instance]` hypotheses by the Lean theorem\n[`QOU.Archimedean.archimedean_functor_uniqueness`](archimedean-functor-uniqueness.lean)\nare the only unproved inputs; both are well-established results\nawaiting Mathlib formalisation (`Real.dilog`, `BlochGroup`, the\nSuslin map)." },
    {
      kind: "deprecated",
      body: "The multiplicative gluon-octet PSLQ form was a legacy conjecture, removed from the corpus and superseded by prop:em-coupling-bring-zero-mode.",
    },
  ],
});
