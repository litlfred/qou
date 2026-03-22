import { chapter, section } from "../../schema/builders";

/**
 * Chapter 8: Glossary of Rigid Monoidal Terms.
 *
 * Light terminological wrappers mapping paper terminology to Mathlib
 * declarations. These entries introduce no new semantic content — they
 * clarify naming conventions and point the reader (and formalization
 * pipeline) to the canonical Mathlib types.
 *
 * Policy: a glossary entry is appropriate when the paper uses a term
 * that is either (a) a synonym for a Mathlib declaration, or (b) a
 * lightweight notational wrapper around one. If the paper's concept
 * involves genuinely new mathematics, it belongs as a `definition`
 * block in the relevant chapter, not here.
 */
export default chapter({
  number: 8,
  title: "Glossary of Rigid Monoidal Terms",
  label: "chap:glossary",
  sections: [
    section({
      title: "Monoidal structure",
      label: "sec:glossary-monoidal",
      blocks: [
        "glossary-monoidal-category",
        "glossary-braided-monoidal-category",
        "glossary-symmetric-monoidal-category",
        "glossary-monoidal-functor",
      ],
    }),

    section({
      title: "Duality and rigidity",
      label: "sec:glossary-rigidity",
      blocks: [
        "glossary-exact-pairing",
        "glossary-left-dual",
        "glossary-right-dual",
        "glossary-rigid-category",
        "glossary-pivotal-category",
        "glossary-compact-closed-category",
      ],
    }),

    section({
      title: "Enrichment",
      label: "sec:glossary-enrichment",
      blocks: [
        "glossary-r-linear-category",
      ],
    }),
  ],
});
