import { chapter, section } from "../../schema/builders";

/**
 * Chapter 3: Braids and Knots.
 *
 * Categorical origin of braiding, braid group representations,
 * SU(2)/SO(3) framework, knot groups, quantum groups, abstract hadron
 * composites and topological mass, Möbius energy, and varying Euler
 * characteristic.
 *
 * Hadron/knot/bundle blocks absorbed from lifting-and-descent §11-12 during
 * chapter restructuring (2026-03).  Proton/neutron definitions moved
 * to the Descartes chapter (Option A: nuclear binding references the
 * abstract hadron, not specific particles).
 * Fluid dynamics and information theory moved to their own chapters.
 */
export default chapter({
  title: "Braids and Knots",
  label: "chap:path-integrals-braiding",
  sections: [
    section({
      title: "Introduction",
      label: "sec:path-integrals-intro",
      blocks: [
        "braids-and-knots-intro",
      ],
    }),

    // Detangler P5 split (2026-05-23): 19-block sec:categorical-braiding
    // split into braid-action + Hecke-eigenbasis.
    section({
      title: "Categorical origin of braiding: the braid action",
      label: "sec:categorical-braiding-action",
      blocks: [
        "categorical-braiding-intro",
        "braid-action-tensor",
        "braid-action-tensor-proof",
        "why-b3",
        "categorical-boson-fermion",
        "symmetric-quotient-colour",
        "braid-base-field",
        "braid-lifting-compatibility",
      ],
    }),
    section({
      title: "Categorical braiding: Hecke quotient and knot eigenbasis",
      label: "sec:categorical-braiding-hecke-eigenbasis",
      blocks: [
        "categorical-braiding-hecke-eigenbasis-intro",
        "eigenbasis-structural-lemmas",
      ],
      // Over-weight split (P4): 27-block section broken into 3
      // reading-order sub-arcs (Hecke quotient / Markov trace + normal
      // form / knot eigenbasis), matching the compound title. Order
      // preserved; parent keeps the intro.
      subsections: [
        section({
          title: "The Hecke quotient",
          label: "sec:categorical-braiding-hecke-quotient",
          blocks: [
            "skein-resolution-obstruction",
            "markov-axioms-primitive",
            "jones-markov-trace",
            "jones-markov-trace-stabilisation",
            "jones-markov-trace-formalization-note",
            "markov-disambiguation",
            "trace-locality-meets-gs-nonlocality",
            "trace-locality-product-factorisation-check",
            "trace-locality-gs-non-locality",
            "trace-locality-gs-reconciliation",
            "trace-locality-meets-gs-nonlocality-proof",
            "trace-locality-nc-probability-reading",
            "hecke-satisfies-blitvic-hypothesis",
            "hecke-blitvic-pair-partition-mechanism",
            "hecke-satisfies-blitvic-hypothesis-proof",
            "hecke-satisfies-blitvic-hypothesis-interpretation",
            "bar-involution",
            "bar-involution-properties",
            "bar-involution-c5-algebraic-identities",
            "bar-involution-geometric-kac-sunada",
            "bar-involution-grading-lean-proofs",
            "braid-group-n-strand",
            "h3-hecke-idempotents",
            "coxeter-strong-exchange",
            "coxeter-parabolic-transversal",
            "coxeter-tits-residue-collapse",
            "coxeter-geometric-representation",
            "tau-assignment-tower-square",
            "braid-link-types",
          ],
        }),
        section({
          title: "Markov trace and normal form",
          label: "sec:categorical-braiding-markov-trace-nf",
          blocks: [
            "markov-trace-inductive-limit",
            "trm-hopf-sigma1-sq-closed-form",
            "trm-hopf-sigma1-sq-closed-form-table1-data",
            "trm-hopf-sigma1-sq-closed-form-proof",
            "trm-hopf-sigma1-sq-closed-form-table2-data",
            "hecke-log-decomposition-table-data",
            "hecke-algebra-from-braiding",
            "f-bor-borromean-observable",
            "hecke-normal-form",
            "dark-vision-strand-bandwidth",
            "markov-moves-brane-tower",
            "markov-trace-ambient-s3",
            "substrate-massive-regime",
            "tl-is-the-xxz-chain",
            "chi-sym-alt-closed-form",
          ],
        }),
        section({
          title: "The knot eigenbasis",
          label: "sec:categorical-braiding-knot-eigenbasis",
          blocks: [
            "knot-eigenbasis-complete",
            "knot-eigenbasis-complete-proof",
            "knot-eigenbasis-complete-reading",
            "knot-exhaustiveness",
            "feynman-eigenbasis",
          ],
        }),
      ],
    }),

    section({
      title: "Braid group and symmetric group",
      label: "sec:braid-symmetric",
      blocks: [
        "braid-symmetric-intro",
        "braid-group",
        "braid-group-su2",
        "knot-notation-convention",
        "knot-notation-convention-table2-data",
        "knot-notation-convention-table1-data",
        "fundamental-knots-operator-basis",
      ],
    }),

    section({
      title: "$\\mathrm{SU}(2)$ and $\\mathrm{SO}(3)$ framework",
      label: "sec:su2-so3",
      blocks: [
        "su2-so3-intro",
        "su2-basis",
        "first-order-taylor",
        // su2-generators relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "so3-generators",
        "quaternion-so3-motivation",
        "su2-generators",
      ],
    }),

    section({
      title: "Braid involutions and holonomy",
      label: "sec:braid-involutions",
      blocks: [
        "braid-involutions-intro",
        // prop:lagrange-resolvent-transform moved here from
        // archimedean-universe/sec:bring-algebraic-substructure per
        // detangler P37 (2026-05-22). 6 H1 fwd-refs cleared.
        // Emits new H2 to def:brings-surface @ archimedean-universe
        // (accepted §5).
        "lagrange-resolvent-transform",
        "braid-twist-flip",
        "holonomy-trefoil",
        "rho-s3-holonomy-exposition",
      ],
    }),

    section({
      title: "The trefoil knot",
      label: "sec:trefoil-knot",
      blocks: [
        "trefoil-knot-intro",
        "trefoil-knot-group",
        "trefoil-operator-algebra",
      ],
    }),

    section({
      title: "Knot fundamental groups",
      label: "sec:knot-fundamental-groups",
      blocks: [
        "knot-fundamental-groups-intro",
        "knot-complement-group",
        "kronheimer-mrowka",
        "reducible-reps",
        // conj:jsj-decomposition-linearity relocated to
        // knots-particles-confinement §9 sec:atom-isotope-knots (2026-08-09,
        // decision 5). It landed here as a 2026-07-12 Ledger §5 orphan
        // integration, i.e. its home here was recent and incidental; its
        // statement is over isotopes (Z, N) and its dep def:atom-knot lives
        // in that section, so the CONSUMER moved rather than the definition.
      ],
    }),

    section({
      title: "Universal enveloping algebras and quantum groups",
      label: "sec:enveloping-algebras",
      blocks: [
        "enveloping-algebras-intro",
        "enveloping-algebra",
        "quantum-su2",
        "q-casimir",
        "q-casimir-classical-limit",
        "q-casimir-exists",
        "q-casimir-exists-proof",
        "q-casimir-unique",
        "q-casimir-unique-proof",
        "r-matrix-braiding-structure",
        "r-matrix-braiding",
        "pontryagin-dual-coxeter-character",
        "pontryagin-dual-coxeter-character-proof",
      ],
    }),

    // ── Lepton–meson parallel ──────────────────────────────────────────
    Object.freeze({
      title: "Leptons, mesons, and the Frobenius bridge",
      label: "sec:lepton-meson-parallel",
      blocks: [
        "lepton-meson-parallel-intro",
        "frobenius-lepton-meson-bridge",
        "frobenius-lepton-meson-bridge-proof",
        "frobenius-lepton-meson-bridge-interpretation",
        "hoefsmit-binding-amplitude",
        "hoefsmit-binding-amplitude-proof",
        "hoefsmit-binding-amplitude-pion-reading",
        "hoefsmit-toroidal-ladder-locus",
        "hoefsmit-toroidal-ladder-locus-proof",
        "three-strand-color-winding-rigidity",
        "three-strand-color-winding-rigidity-proof",
        // Keystone: 4₁ (Higgs) amphichiral ⇒ CS=0 ⇒ real complex volume;
        // the bare Higgs gives only the mass face, Q_β is the binding defect.
        "self-dual-higgs-real-volume",
        // Cusp-shape bar-parity: Φ₆ modulus splits Vol⊕i·CS (barEven ω=1,
        // barOdd ω²=−3); meridian holonomy is a boost (rapidity ln q₀); the
        // per-operation tick is the Compton time, not the Planck time.
        "cusp-shape-bar-parity",
        "meridian-holonomy-boost",
        "meridian-exceptional-divisor-note",
        // Braid-word geodesic on the cusp torus: Im 𝔙₄₁ collapses onto the
        // disc-12 norm form of ℤ[√3] (Pell = the boost hyperbola), so the sign
        // is arithmetic in the winding class, not a function of q₀; the golden
        // order's N(φⁿ)=(−1)ⁿ is the parity mechanism the cusp torus lacks.
        "winding-lattice-norm-form",
        "winding-parity-sign-transport",
        "meson-em-sinh-closed-form",
        "meson-em-sinh-closed-form-proof",
        "meson-em-sinh-ratio-reading",
        "meson-qcg-fusion-identity",
        "meson-qcg-fusion-identity-proof",
        "meson-qcg-fusion-identity-mass-reading",
        "q-difference-viewpoint-method",
        "alpha-em-habiro-bar-involution",
        "figure-eight-reeb-rotation",
        "figure-eight-reeb-rotation-proof",
        "figure-eight-reeb-rotation-reeb-reading",
        "figure-eight-reeb-theta-value",
        "figure-eight-reeb-novelty-note",
        "figure-eight-muon-anchor-reading",
        "pion-half-figure-eight",
        "pion-half-figure-eight-proof",
        "pion-half-figure-eight-formalization-note",
        "pion-half-figure-eight-decay-reading",
        "outro-braids-and-knots",
      ],
    }),

    // ── Calibration and algebraic mass formula ──────────────────────────
    // ── Calibration and algebraic mass formula (P2 split 2026-05-19,
    //    phase 1): the 134-block sec:calibration-algebraic-mass
    //    (7.4× over the 3-18 band) split into 7 topical sub-sections
    //    following the mass-formula pedagogy: derivation → Hoefsmit
    //    & convergence → q-beta precision ladder → Archimedean
    //    realization → cyclotomic depth-3 → Hecke-Baer-star →
    //    mutant Jones falsifiability. The existing
    //    calibration-algebraic-mass-intro stays at the top of A as
    //    the umbrella narrative. Phase-1 densities 15/19/37/12/10/4/13.
    //    Section C (37) remains over the upper bound; phase-2
    //    follow-up will internal-split.

    // §C — q-beta precision ladder (PHASE-2 split 2026-05-19): the
    //   37-block sec:q-beta-precision-ladder from the phase-1
    //   calibration-algebraic-mass split is split into 3 topical
    //   sub-sections (Markov + braid-link foundations / chi-character
    //   closed-forms / Kashiwara-Jones interpretations and quantum-
    //   dilogarithm). The 12/13/12 densities all land in the 3-18 band.

    // ── Atom, isotope, and confinement levels (P1 split 2026-05-19):
    //    the 43-block sec:atom-isotope-confinement is split into six
    //    topical sub-sections following the natural pedagogy:
    //    energy → confinement → pair production → particles & shells →
    //    atoms & isotopes → magic shells. The existing
    //    atom-isotope-confinement-intro stays at the top of A and
    //    previews all six sub-sections as an umbrella narrative.

    // ── Nuclear binding and beta stability ──────────────────────────────
    // ── Nuclear binding and beta stability (P2 split 2026-05-19,
    //    phase 1): the paper's largest section (sec:nuclear-binding-
    //    beta-stability, 134 blocks, 7.4× over the 3-18 band) split
    //    into 7 topical sub-sections following the substrate-binding
    //    pedagogy: setup → LP-dual → phi_q/Markov/Schur-Weyl tower →
    //    GS axiomatic backing → Frobenius nuclear structure →
    //    Plancherel/alpha/ribbon → alpha_k/Wenzl bridge. The
    //    existing nuclear-binding-beta-stability-intro stays at the
    //    top of A as the umbrella narrative for the whole 7-section
    //    arc. Densities 12/9/18/6/27/18/46. Sections E (27) and G
    //    (46) remain over the upper bound; phase 2 follow-up will
    //    apply internal splits to each.

    // §E — Frobenius nuclear structure (PHASE-2 split 2026-05-19):
    //   the 27-block sec:frobenius-nuclear-structure from the phase-1
    //   nuclear-binding split is split into 2 sub-sections: parity-
    //   classification-and-discrepancy (~12) and spectral-sequence-
    //   chirality-and-confinement (~15). Both within the 3-18 band.

    // §G — alpha_k derivation, Wenzl bridge, beta stability (PHASE-2
    //   split 2026-05-19): the 43-block sec:alpha-k-wenzl-bridge from
    //   the phase-1 nuclear-binding split is split into 4 sub-sections:
    //   alpha_k procedure (~9) / Wenzl bridge & cyclotomic (~13) /
    //   crystal & isospin & chirality (~9) / beta-stability closure
    //   (~12). All within the 3-18 band.

  ],
});
