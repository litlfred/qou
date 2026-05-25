import { chapter, section } from "../../schema/builders";

/**
 * Chapter 10 — Mass — Theory (light).
 *
 * Conceptual framework for the mass endomorphism: Wedderburn
 * decomposition, Frobenius pairing $\mathrm{tr}_M = \sum_\lambda
 * y_\lambda \chi^\lambda$, transfer matrices, Markov-trace properties,
 * crystal-basis statements, mass-formula derivation. The chapter holds
 * the **statements** of the mass machinery; the **algorithms and
 * compute** live in Mass — Application (Ch 11).
 *
 * Phase 4 chunk 2 (2026-05-25): 90 blocks moved from braids-and-knots
 * across 7 sections (transfer-matrix, categorical-mass eigenspaces +
 * Markov-trace endomorphism, mass-formula derivation, Hecke χ
 * closed-forms).
 *
 * Story-arc placement: Part II "Structural Mechanics" Ch 10 — the
 * theoretical face of the mass step. Consumes the Hecke algebra (Ch 5),
 * the climax volume/mass identity (Ch 6), and Bring's geometric
 * structure (Ch 7); hands off to Mass — Application (Ch 11) for the
 * compute infrastructure.
 */
export default chapter({
  title: "Mass --- Theory",
  label: "chap:mass-theory",
  sections: [
    section({
      title: "Transfer Matrix and Topological Mass",
      label: "sec:transfer-matrix-mass",
      blocks: [
        "transfer-matrix-mass-intro",
        "categorical-transfer-matrix",
        "transfer-matrix-level-independence",
        "tmli-constituent-composite-agreement",
        "tmli-constituent-composite-agreement-proof",
        "transfer-matrix-level-independence-proof",
        "topological-mass-formula",
        "motivic-mass-measure",
        "hecke-mass-element",
        "hecke-mass-trace",
        "hecke-charge-mass-duality",
        "skein-decomposition",
        "topological-field-ansatz",
        "topological-field-ansatz-table-data",
      ],
    }),
    section({
      title: "Categorical mass foundations: eigenspace decompositions",
      label: "sec:categorical-mass-eigenspaces",
      blocks: [
        "categorical-mass-foundations-intro",
        "topological-mass-cat-eigenspace",
        "topological-mass-cat-eigenspace-proof",
        "topological-mass-cat-descended",
        "topological-mass-cat-descended-proof",
        "topological-mass-cat-transient",
        "topological-mass-cat-transient-proof",
        "topological-mass-categorical-proof",
        "categorical-mass-markov",
        "atomic-mass-gb-nf",
        "rho-k-graded-expansion",
        "rho-k-graded-expansion-table2-data",
        "rho-k-graded-expansion-table1-data",
        "conj-rho-k-pair-gen-canonical-form",
        "operator-valued-magnitude-budget",
        "q-hecke-seminormal-character-closure",
      ],
    }),
    section({
      title: "Categorical mass foundations: Markov trace and endomorphism",
      label: "sec:categorical-mass-markov-trace-endomorphism",
      blocks: [
        "categorical-mass-markov-trace-endomorphism-intro",
        "recomputed-low-isotope-mass-table",
        "recomputed-low-isotope-mass-table-table4-data",
        "recomputed-low-isotope-mass-table-table3-data",
        "recomputed-low-isotope-mass-table-table2-data",
        "recomputed-low-isotope-mass-table-table1-data",
        "markov-trace-antipode-polynomial-symmetry",
        "markov-trace-axiomatic-closed-form",
        "markov-trace-axiomatic-closed-form-table1-data",
        "markov-trace-axiomatic-closed-form-table2-data",
        "markov-trace-recursive-reducer",
        "markov-z-reconciliation",
        "mass-endomorphism-conjecture",
        "categorical-neutrality-saturated-shells",
        "phi-n-global-section",
      ],
    }),
    section({
      title: "Mass-formula derivation",
      label: "sec:mass-formula-derivation",
      blocks: [
        "calibration-algebraic-mass-intro",
        "mass-element-nf",
        "calibration-inputs",
        "two-tier-scaling-pq",
        "three-calibration-inputs",
        "three-parameters-wedderburn",
        "wedderburn-trace-identity",
        "binding-scale-catalan",
        "wedderburn-mass-formula",
        "frobenius-s-classification",
        "frobenius-s-classification-table3-data",
      ],
    }),
    section({
      title: "Mass-formula derivation (generation)",
      label: "sec:mass-formula-derivation-commutative-chirality-vanishes",
      blocks: [
        "mass-formula-derivation-commutative-chirality-vanishes-intro",
        "frobenius-s-classification-table2-data",
        "frobenius-s-classification-table1-data",
        "commutative-chirality-vanishes",
        "derived-mass-formula-light-isotopes",
        "derived-mass-formula-light-isotopes-table1-data",
        "derived-mass-formula-light-isotopes-table2-data",
        "deuteron-binding-frobenius-codim",
        "deuteron-binding-frobenius-codim-table-data",
        "hoefsmit-seminormal-form",
        "figure-eight-branching-rule",
        "figure-eight-branching-rule-table2-data",
        "figure-eight-branching-rule-table1-data",
      ],
    }),
    section({
      title: "Hecke $u$-coordinate and $\\chi$-character closed-forms",
      label: "sec:hecke-chi-closed-forms",
      blocks: [
        "intro-hecke-chi-closed-forms",
        "u-coordinate-discharges",
        "u-coordinate-discharges-table-data",
        "multi-link-jones-q1-extension",
        "per-wedderburn-block-c5-c6",
        "hecke-algebra-type-scaffold",
        "markov-trace-operator-construction",
        "chi-v3-closed-form-proof",
      ],
    }),
    section({
      title: "Hecke $\\chi$-character closed-forms (generation)",
      label: "sec:hecke-chi-closed-forms-chi-per-irrep",
      blocks: [
        "hecke-chi-closed-forms-chi-per-irrep-intro",
        "chi-v3-closed-form-proof-table-data",
        "chi-per-irrep-cyclotomic-closed-forms",
        "chi-per-irrep-cyclotomic-closed-forms-table2-data",
        "chi-per-irrep-cyclotomic-closed-forms-table1-data",
        "per-block-hopf-jones-absorption-pattern",
        "conj-qbeta-c-k-closed-forms",
        "chi-v111-via-sign-substitution",
        "chi-v21-hoefsmit-matrix-derivation",
        "phi-d-syt-count-conjecture",
        "categorical-chain-convergence-mechanisms",
        "categorical-chain-convergence-mechanisms-table-data",
        "tau-M-asymptotic-rep-theory",
      ],
    }),
  ],
});
