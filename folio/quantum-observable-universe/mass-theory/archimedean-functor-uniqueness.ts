import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:archimedean-functor-uniqueness",
  title:
    "Uniqueness of the archimedean realization functor (Bloch-Suslin pentagon, conditional)",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "archimedean",
    "realization-functor",
    "uniqueness",
    "bloch-wigner",
    "pentagon-identity",
    "dilogarithm",
    "motivic",
    "kashaev",
    "alpha-em",
    "fine-structure-constant",
    "pre-archimedean",
    "conditional-class",
  ],
  foreshadows: ["conj:dilogarithm-archimedean-limit"],
  uses: [
    "prop:quantum-dilogarithm-volume",
    "conj:dilogarithm-archimedean-limit",
    "conj:mass-endomorphism",
    "prop:cosimplicial-crossed-groupoid",
  ],
  cites: [
    "suslin1991",
    "bloch2000",
    "zagier1986",
    "kashaev1997",
    "murakami-murakami2001",
    "faddeev1994",
    "thurston1978",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.archimedean_functor_uniqueness",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > The upstream conjecture is axiomatised in Lean as the typeclass\n> [`QOU.QPochhammer.ArchimedeanLimit`](dilogarithm-archimedean-limit.lean);\n> the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`,\n> `bloch2000`] is similarly axiomatised as\n> [`QOU.Archimedean.BlochSuslinUniqueness`](archimedean-functor-uniqueness.lean).\n> The Lean theorem\n> [`QOU.Archimedean.archimedean_functor_uniqueness`](archimedean-functor-uniqueness.lean)\n> takes both classes as `[Instance]` hypotheses and is proved\n> **without `sorry`**; the uniqueness statement therefore qualifies as a\n> *rigorous conditional result* rather than an unproved\n> conjecture." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): together with the archimedean-limit class `QOU.QPochhammer.ArchimedeanLimit`" },
  ],
});
