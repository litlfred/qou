import { chapter, section } from "../../schema/builders";

/**
 * Annex F: Notation Register, Categorical Glossary, and Index of Definitions.
 *
 * Consolidates `notation`, `glossary`, and `index-of-definitions` into a single
 * reference lookup annex (keeping `dir: "notation"` and `label: "chap:notation"`
 * so preview-chapter and reference-table audit exemptions remain intact).
 */
export default chapter({
  tabLabel: "F",
  title: "Notation Register, Categorical Glossary, and Index of Definitions",
  label: "chap:notation",
  sections: [
    section({
      title: "Symbol register and key collision avoidances",
      label: "sec:notation-register-section",
      blocks: [
        "notation-register-section-intro",
        "notation-register",
        "notation-register-table1-data",
        "notation-register-table2-data",
        "notation-register-table3-data",
        "notation-register-table4-data",
        "notation-register-table5-data",
        "notation-register-table6-data",
        "notation-register-table7-data",
        "notation-register-table8-data",
        "notation-register-table9-data",
        "notation-register-table10-data",
        "notation-collisions",
      ],
    }),
    section({
      title: "Glossary of monoidal, rigid, and enriched categorical notions",
      label: "sec:glossary-monoidal",
      blocks: [
        "glossary-hom-set",
        "glossary-monoidal-intro",
        "glossary-monoidal-category",
        "glossary-braided-monoidal-category",
        "glossary-symmetric-monoidal-category",
        "glossary-monoidal-functor",
        "glossary-rigidity-intro",
        "glossary-exact-pairing",
        "glossary-left-dual",
        "glossary-right-dual",
        "glossary-rigid-category",
        "glossary-pivotal-category",
        "glossary-compact-closed-category",
        "glossary-r-linear-category",
        "glossary-no-quasi-zeros",
        "glossary-cemetery-group",
      ],
    }),
    section({
      title: "Glossary of geometric, information-theoretic, and homological notions",
      label: "sec:glossary-geometry",
      blocks: [
        "glossary-geometry-intro",
        "glossary-quantum-flatness",
        "glossary-reeb-gauge-group",
        "glossary-categorical-transport",
        "glossary-categorical-q-torsion-leaf",
        "glossary-aether",
        "glossary-brane",
        "glossary-descent",
        "glossary-s3-group",
        "glossary-q-bit",
        "glossary-q-bit-skein",
        "glossary-distinguished-triangle",
        "glossary-derived-category",
        "glossary-dg-category",
        "glossary-fourier-mukai-transform",
        "glossary-observed-value",
        "glossary-weierstrass-projection",
      ],
    }),
    section({
      title: "Index of definitions, theorems, propositions, and conjectures",
      label: "sec:definition-index",
      blocks: [
        "definition-index",
      ],
    }),
  ],
});
