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
  tabLabel: "G",
  title: "Glossary",
  label: "chap:glossary",
  sections: [
    section({
      title: "Basic categorical notions",
      label: "sec:glossary-basic",
      blocks: [
        "glossary-hom-set",
      ],
    }),

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
        "glossary-no-quasi-zeros",
        "glossary-cemetery-group",
      ],
    }),

    section({
      title: "Geometry and transport",
      label: "sec:glossary-geometry",
      blocks: [
        "glossary-quantum-flatness",
        "glossary-reeb-gauge-group",
        "glossary-categorical-transport",
        "glossary-categorical-q-torsion-leaf",
        "glossary-descent",
      ],
    }),

    section({
      title: "Groups and symmetry",
      label: "sec:glossary-groups",
      blocks: [
        "glossary-s3-group",
      ],
    }),

    section({
      title: "Information theory",
      label: "sec:glossary-information",
      blocks: [
        "glossary-q-bit",
        "glossary-q-bit-skein",
      ],
    }),

    section({
      title: "Elliptic and surface geometry",
      label: "sec:glossary-elliptic",
      blocks: [
        "glossary-observed-value",
        "glossary-weierstrass-projection",
      ],
    }),
  ],
});
