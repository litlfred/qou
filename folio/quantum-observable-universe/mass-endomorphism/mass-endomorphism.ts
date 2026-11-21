import { chapter, section } from "../../schema/builders";

/**
 * The Mass Endomorphism.
 *
 * States the mass endomorphism conjecture and develops its algebraic
 * core: the categorical mass identity (existence + uniqueness), the
 * topological decomposition theorem (eigenspace, holonomy, transient,
 * dilogarithm), the Markov-trace endomorphism, and the Hecke
 * character closed-forms. Three-calibration discipline is a
 * categorical constraint stated here.
 *
 * This chapter sits BEFORE Particles — the mass derivation is the
 * generic Yekutieli path from the brane tower, independent of
 * specific particle assignments. Particles then APPLY the mass
 * formula to specific knots.
 *
 * The detailed mass analysis (geometric face, archimedean face,
 * physical predictions, compute) lives in Mass Analysis (after
 * Particles).
 */
export default chapter({
  title: "The Mass Endomorphism",
  label: "chap:mass-endomorphism",
  sections: [
    // ═══ CATEGORICAL OPENER ══════════════════════════════════════
    section({
      title: "The Mass Endomorphism",
      label: "sec:mass-endomorphism-opener",
      blocks: [
        "mass-endomorphism-opener-intro",
      ],
      // Over-weight split (P4): 28-block opener into 3 reading-order
      // sub-arcs (the mass identity / topological mass / its spectral
      // sequence). Order preserved; parent keeps the intro.
      subsections: [
        section({
          title: "The mass identity",
          label: "sec:mass-endomorphism-mass-identity",
          blocks: [
            "mass-endomorphism-conjecture",
            "higgs-vacuum-residual-graviton",
            "pairing-gauge-fluctuation-massless",
            "pairing-gauge-fluctuation-massless-interpretation",
            "mass-identity",
            "mass-identity-exists",
            "mass-identity-exists-proof",
            "mass-identity-unique",
            "mass-identity-unique-proof",
            "mass-identity-su2",
            "mass-geometric-drag",
            "mass-noncommutative-drag",
            "mass-identity-C",
            "mass-identity-C-proof",
          ],
        }),
        section({
          title: "Topological mass",
          label: "sec:mass-endomorphism-topological-mass",
          blocks: [
            "topological-mass-upper-bound",
            "topological-mass",
            "topological-mass-conjecture",
            "topological-mass-conjecture-proof",
            "topological-mass-eigenspace-decomp",
            "topological-mass-eigenspace-decomp-proof",
            "topological-mass-holonomy",
            "topological-mass-holonomy-proof",
            "topological-mass-transient-localisation",
            "topological-mass-transient-localisation-proof",
            "topological-mass-dilogarithm",
            "topological-mass-dilogarithm-proof",
            "topological-mass-proof",
          ],
        }),
        section({
          title: "Spectral sequence and shell condensation",
          label: "sec:mass-endomorphism-spectral-shell",
          blocks: [
            "topological-mass-su2",
            "gb-spectral-sequence-intro",
            "gb-spectral-sequence",
            "gb-spectral-sequence-table-data",
            "gb-spectral-sequence-mass-identification",
            "gb-spectral-sequence-interpretation",
            "homological-shell-condensation",
            "homological-shell-condensation-motivation",
            "homological-shell-condensation-interpretation",
            "hecke-length-limit-page-vanishing",
            "qou-motivic-galois-instance",
            "qou-motivic-galois-instance-verification",
            "qou-motivic-galois-instance-per-cell",
          ],
        }),
      ],
    }),

    // ═══ THE COMPLEX VOLUME $\mathfrak{V}$ ═══════════════════════════════════
    // Binding (Re $\mathfrak{V}$) and β-decay Q-value (Im $\mathfrak{V}$) are two real
    // shadows of one complex fibre observable. Frames the rest of
    // the mass + β-decay narrative as one derivation.
    section({
      title:
        "The complex volume $\\mathfrak{V}$: binding and decay as $\\operatorname{Re}$/$\\operatorname{Im}$",
      label: "sec:complex-volume",
      blocks: [
        "complex-volume-intro",
        "binding-qbeta-complex-volume",
        "channel-rotation-askey-lit",
        "whipple-rotation-intertwining",
        "complex-volume-character-variety-path",
        "color-spacetime-s5-factorization",
        "mass-modulus-em-phase-color-grading",
        "color-spacetime-s5-factorization-derivation",
      ],
    }),

    // ═══ ALGEBRAIC FACE ═════════════════════════════════════════
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
        "kz-connection-sl2",
        "categorical-mass-markov-proof",
        "markov-trace-gibbs-free-energy",
        "atomic-mass-gb-nf",
        "rho-k-graded-expansion",
        "atomic-mass-gb-nf-interpretation",
        "rho-k-graded-expansion-accuracy",
        "rho-k-graded-expansion-table2-data",
        "rho-k-graded-expansion-table1-data",
        "conj-rho-k-pair-gen-canonical-form",
        "hecke-branching-trace-decomposition",
        "hecke-branching-trace-decomposition-proof",
        "operator-valued-magnitude-budget",
      ],
    }),
    section({
      title: "Categorical mass foundations: Markov trace and endomorphism",
      label: "sec:categorical-mass-markov-trace-endomorphism",
      blocks: [
        "categorical-mass-markov-trace-endomorphism-intro",
        "markov-trace-antipode-polynomial-symmetry",
        "markov-trace-antipode-polynomial-symmetry-proof",
        "markov-trace-axiomatic-closed-form",
        "markov-trace-axiomatic-closed-form-table1-data",
        "markov-trace-axiomatic-closed-form-table2-data",
        "markov-trace-axiomatic-closed-form-proof",
        "markov-trace-axiomatic-closed-form-interpretation",
        "markov-trace-recursive-reducer",
        "markov-trace-recursive-reducer-interpretation",
        "q-hecke-seminormal-character-closure",
        "recomputed-low-isotope-mass-table",
        "recomputed-low-isotope-mass-table-table4-data",
        "recomputed-low-isotope-mass-table-table3-data",
        "recomputed-low-isotope-mass-table-table2-data",
        "recomputed-low-isotope-mass-table-table1-data",
        "markov-z-reconciliation",
        "categorical-neutrality-saturated-shells",
        "categorical-neutrality-saturated-shells-notation",
        "phi-n-global-section",
        "categorical-neutrality-saturated-shells-interpretation",
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
        "hecke-algebra-type-scaffold",
        "markov-trace-operator-construction",
        "chi-v3-closed-form-proof",
      ],
    }),
    section({
      title: "Cyclotomic $\\chi$-character closed forms and asymptotic representation theory",
      label: "sec:hecke-chi-closed-forms-chi-per-irrep",
      blocks: [
        "hecke-chi-closed-forms-chi-per-irrep-intro",
        "chi-v3-closed-form-proof-table-data",
        "chi-per-irrep-cyclotomic-closed-forms",
        "chi-per-irrep-cyclotomic-closed-forms-table2-data",
        "chi-per-irrep-cyclotomic-closed-forms-table1-data",
        "per-block-hopf-jones-absorption-pattern",
        "conj-qbeta-c-k-closed-forms",
        "conj-qbeta-c-k-closed-forms-derivation",
        "chi-v111-via-sign-substitution",
        "chi-v21-hoefsmit-matrix-derivation",
        "phi-d-syt-count-conjecture",
        "categorical-chain-convergence-mechanisms",
        "categorical-chain-convergence-mechanisms-neutron-truncation",
        "categorical-chain-convergence-mechanisms-table-data",
        "tau-M-asymptotic-rep-theory",
        "tau-M-asymptotic-rep-theory-proof",
        "tau-M-asymptotic-rep-theory-scope",
        "tau-M-asymptotic-rep-theory-interpretation",
      ],
    }),
    section({
      title:
        "Per-block $\\chi$ closed forms, $\\Delta\\mathrm{tr}_M$ machinery, and canonical Markov weights",
      label: "sec:hecke-chi-per-block-delta-tau-canonical-weights",
      blocks: [
        "qbeta-per-block-delta-tau-intro",
        "qbeta-per-block-chi-closed-forms",
        "qbeta-per-block-chi-closed-forms-proof",
        "qbeta-delta-tau-canonical-conditional-q2-minus-1-factor",
        "qbeta-delta-tau-canonical-conditional-q2-minus-1-factor-proof",
        "qbeta-delta-tau-surrogate-taylor-coefficients",
        "qbeta-delta-tau-surrogate-taylor-coefficients-formal-scope",
        "qbeta-canonical-markov-weights-explicit-instance",
        "qbeta-canonical-markov-weights-explicit-instance-proof",
      ],
    }),
    section({
      title: "Hecke-Baer-star foundation and chirality pairing",
      label: "sec:hecke-baer-star-chirality",
      blocks: [
        "intro-hecke-baer-star-chirality",
        "hecke-baer-star-generic",
        "hecke-baer-star-generic-proof",
        "hecke-baer-star-generic-interpretation",
        "explicit-central-idempotent-cross-checks",
        "explicit-central-idempotent",
        "hecke-baer-star-generic-corollary",
        "chirality-period-pairing",
        "bring-embeddable-knots",
        "bring-embeddable-knots-table-data",
        "outro-mass-endomorphism",
      ],
    }),
  ],
});
