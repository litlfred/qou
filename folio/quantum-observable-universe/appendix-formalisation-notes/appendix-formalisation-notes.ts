import { chapter } from "../../schema/builders";

/**
 * Appendix: Formalisation notes.
 *
 * Owner ruling 2026-11-20 (second [W14 ask] on #8526, answer 1b): blocks
 * whose subject is the Lean / Mathlib infrastructure itself — library
 * gaps, filler constructions, typeclass carriers and formalisation-status
 * tables — are collected here instead of interrupting the chapters. The
 * voice-leak audit does not check L1/L2 in this appendix (CODE_BY_DESIGN).
 * Labels are unchanged, so every existing `(#label)` link and `uses[]`
 * reference still resolves.
 */
export default chapter({
  label: "app:formalisation-notes",
  title: "Formalisation notes",
  sections: [
    {
      title: "Coverage",
      blocks: [
        "formalisation-coverage",
      ],
    },
    {
      title: "Mathlib infrastructure for the dilogarithm chain",
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
        "bloch-group-quotient-construction",
        "bloch-group-quotient-construction-table-data",
        "cl2-pentagon-and-faddeev-partial-formalization-status",
        "cl2-pentagon-and-faddeev-partial-table1-data",
        "cl2-pentagon-and-faddeev-partial-table2-data",
        "cl2-pentagon-and-faddeev-partial-table3-data",
        "type-b-folded-crystal-combinatorics-table-data",
      ],
    },
    {
      title: "Lean infrastructure for the mass chapter",
      blocks: [
        "q-beta-bar-even-kernel-typeclass",
        "mass-side-kernel-formalize-first-gates",
        "mass-tower-deeper-fillers",
        "confinement-nf-structure-forcing-table-data",
      ],
    },
    {
      title: "Computation provenance of the knot atlas",
      blocks: [
        "recursive-atom-knot-atlas-interpretation",
      ],
    },
  ],
});
