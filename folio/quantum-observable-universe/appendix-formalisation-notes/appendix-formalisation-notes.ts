import { chapter } from "../../schema/builders";

/**
 * Annex E: Lean 4 Formalization Architecture and Reusable Community Libraries (qou-lanx).
 *
 * Evolves `appendix-formalisation-notes` in place (preserving `label: "app:formalisation-notes"`
 * for `authors-note` compatibility and `CODE_BY_DESIGN` voice exemption):
 *   - §E.1 Four-tier knowledge-graph DAG, kernel axiom discipline, and vacuity gates;
 *   - §E.2 Tier-A Mathlib4 core upstreaming additions (Laurent units, PL links, dilogarithms);
 *   - §E.3 Tier-B six standalone Reservoir-ready community libraries.
 */
export default chapter({
  tabLabel: "E",
  label: "app:formalisation-notes",
  title: "Lean 4 Formalization Architecture and Reusable Community Libraries",
  sections: [
    {
      title: "Four-tier formalisation DAG, kernel trust boundary, and mass-kernel gates",
      label: "sec:lean-dag-trust-boundary",
      blocks: [
        "formalisation-coverage",
        "q-beta-bar-even-kernel-typeclass",
        "mass-side-kernel-formalize-first-gates",
        "mass-tower-deeper-fillers",
        "confinement-nf-structure-forcing-table-data",
      ],
    },
    {
      title: "Tier-A Mathlib4 core upstreaming targets",
      label: "sec:lean-mathlib-upstreaming",
      blocks: [],
      subsections: [
        {
          title: "Clausen and Bloch--Wigner dilogarithm infrastructure",
          label: "sec:lean-mathlib-dilog",
          blocks: [
            "three-substantive-mathlib-fillers",
            "clausen-function-mathlib-filler",
            "clausen-function-mathlib-filler-table1-data",
            "clausen-function-mathlib-filler-table2-data",
            "bloch-wigner-mathlib-filler",
            "bloch-wigner-mathlib-filler-table1-data",
            "bloch-wigner-mathlib-filler-table2-data",
            "bloch-wigner-mathlib-filler-table3-data",
            "upstream-mathlib-additions",
            "upstream-mathlib-additions-detail",
            "upstream-mathlib-additions-table1-data",
            "upstream-mathlib-additions-table2-data",
            "mathlib-upstreaming-laurent-pl-links",
          ],
        },
        {
          title: "Bloch-group quotients, pentagon closure, and crystal combinatorics",
          label: "sec:lean-mathlib-bloch-pentagon",
          blocks: [
            "bloch-group-quotient-construction",
            "bloch-group-quotient-construction-table-data",
            "cl2-pentagon-and-faddeev-partial-table1-data",
            "cl2-pentagon-and-faddeev-partial-table2-data",
            "cl2-pentagon-and-faddeev-partial-table3-data",
            "cl2-pentagon-and-faddeev-partial-formalization-status",
            "type-b-folded-crystal-combinatorics-table-data",
          ],
        },
      ],
    },
    {
      title: "Tier-B: Six standalone Lean 4 Reservoir community libraries",
      label: "sec:lean-community-libraries",
      blocks: [
        "lean-community-libraries-dag",
        "lean-lib-hecke-temperley-lieb",
        "lean-lib-twisted-frobenius-hopf",
        "lean-lib-toric-conic-opt",
        "lean-lib-compact-quantum-metrics",
        "lean-lib-q-calculus",
        "lean-lib-braid-knot-octonion",
      ],
    },
  ],
});
