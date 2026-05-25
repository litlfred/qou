import { chapter, section } from "../../schema/builders";

/**
 * Chapter 11 — Mass --- Application (heavy).
 *
 * Compute, algorithms, and sweep applications of the mass machinery:
 * Hoefsmit-representation construction, Wenzl projectors, Markov-peel
 * algorithms, Gröbner–Shirshov reductions, φ_q convergence, residue
 * computations, magic-shell extractions.
 *
 * Phase 4 chunk 3 (2026-05-25): 73 blocks moved from braids-and-knots
 * across 6 sections.
 *
 * Story-arc placement: Part II "Structural Mechanics" Ch 11 — the
 * compute face of the mass step. Consumes the statements from Mass --- Theory.
 */
export default chapter({
  title: "Mass --- Application",
  label: "chap:mass-application",
  sections: [
    section({
      title: "Hoefsmit convergence: construction",
      label: "sec:hoefsmit-convergence-construction",
      blocks: [
        "intro-hoefsmit-convergence-atomic",
        "operator-selection-lp",
        "universal-braid-branching",
        "hoefsmit-scattering-pipeline",
        "hecke-convergence-bound",
        "algebraic-quantum-volume",
        "habiro-ring",
        "habiro-expansion-atomic",
        "z-habiro-ring",
        "brane-tower-z-habiro",
        "brane-tower-z-habiro-table1-data",
      ],
    }),
    section({
      title: "Hoefsmit convergence: construction : generation",
      label: "sec:hoefsmit-convergence-construction-per-partition-k",
      blocks: [
        "hoefsmit-convergence-construction-per-partition-k-intro",
        "brane-tower-z-habiro-table2-data",
        "brane-tower-z-habiro-table3-data",
        "brane-tower-z-habiro-table4-data",
        "brane-tower-z-habiro-table5-data",
        "brane-tower-z-habiro-table6-data",
        "brane-tower-z-habiro-table7-data",
        "brane-tower-z-habiro-table8-data",
        "brane-tower-z-habiro-table9-data",
        "brane-tower-z-habiro-table10-data",
        "brane-tower-z-habiro-table11-data",
        "per-partition-k-lambda-rule",
      ],
    }),
    section({
      title: "Hoefsmit convergence: magic-shell consequences",
      label: "sec:hoefsmit-convergence-magic-shells",
      blocks: [
        "hoefsmit-convergence-magic-shells-intro",
        "two-row-stratum",
        "he4-channel-active-set",
        "he4-two-row-dominance",
        "schur-weyl-vanishing",
        "schur-weyl-vanishing-table-data",
        "markov-trace-frobenius-selection",
        "hecke-1d-irrep-closed-form-character",
        "hoefsmit-V21-cos-symmetrization",
      ],
    }),
    section({
      title: "$\\\\varphi_q$ resummation, Markov trace, Schur-Weyl: foundations",
      label: "sec:phi-q-markov-schur-weyl-foundations",
      blocks: [
        "intro-phi-q-markov-schur-weyl-tower",
        "markov-trace-factorization",
        "markov-trace-ratio-exact",
        "vassiliev-filtration-mass-tower",
        "hecke-quandle",
        "knot-operator-bring-action",
        "phi-q-resums-trace-series",
        "phi-q-resums-trace-series-table-data",
        "markov-axiom-recursive-ascent",
        "per-braid-mass-tower",
        "lepton-mass-tower-canonical",
        "lepton-bring-surface-h3-3channel",
        "conj-lepton-tower-h-n-plus-1-branching",
        "conj-atom-braid-exterior-algebra",
        "conj-psd-trace-orthogonality",
        "three-halves-structural-factor",
        "rem-im-q-vs-p-skew",
        "conj-im-q-physical-role",
        "schur-weyl-mass-decomposition",
        "gb-residue-spectral-sum",
        "categorical-mass-positivity",
        "mass-spectrum-generating-function",
        "graded-markov-trace-from-gs-filtration",
        "residue-at-root",
      ],
    }),
    section({
      title: "$\\\\varphi_q$ resummation: residue and Habiro identifications",
      label: "sec:phi-q-markov-residue-habiro",
      blocks: [
        "phi-q-markov-residue-habiro-intro",
        "vhat-pair-commutation-trace",
        "tower-pair-equality-fixed-level",
        "jet-tower-uniform-delta-max",
        "topological-mass-formula-algebraic",
        "residue-as-braid-holonomy",
        "graded-trace-residue-split",
        "term6-binding-density",
        "term6-binding-density-table2-data",
        "term6-binding-density-table1-data",
        "full-pole-structure-mass-trace",
        "habiro-residue-sum-equivalence",
      ],
    }),
    section({
      title: "Gröbner-Shirshov axiomatic backing",
      label: "sec:gs-axiomatic-backing",
      blocks: [
        "intro-gs-axiomatic-backing",
        "gs-graded-markov-trace-existence",
        "gs-residue-at-root-existence",
        "gs-spectral-decomposition-existence",
        "gs-spectral-sum-finite",
        "gs-archimedean-agreement-trace",
        "gs-archimedean-agreement-residue",
      ],
    }),
  ],
});
