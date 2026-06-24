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
        "intro",
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
            "hecke-satisfies-blitvic-hypothesis",
            "hecke-satisfies-blitvic-hypothesis-proof",
            "trace-locality-meets-gs-nonlocality",
            "trace-locality-meets-gs-nonlocality-proof",
            "jones-markov-trace",
            "markov-disambiguation",
            "bar-involution",
            "braid-group-n-strand",
            "h3-hecke-idempotents",
            "braid-link-types",
          ],
        }),
        section({
          title: "Markov trace and normal form",
          label: "sec:categorical-braiding-markov-trace-nf",
          blocks: [
            "markov-axioms-primitive",
            "markov-trace-inductive-limit",
            "trm-hopf-sigma1-sq-closed-form",
            "trm-hopf-sigma1-sq-closed-form-table2-data",
            "trm-hopf-sigma1-sq-closed-form-table1-data",
            "hecke-log-decomposition-table-data",
            "hecke-algebra-from-braiding",
            "f-bor-borromean-observable",
            "hecke-normal-form",
            "dark-vision-strand-bandwidth",
            "markov-moves-brane-tower",
          ],
        }),
        section({
          title: "The knot eigenbasis",
          label: "sec:categorical-braiding-knot-eigenbasis",
          blocks: [
            "knot-eigenbasis-complete",
            "knot-eigenbasis-complete-proof",
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
        "q-casimir-exists",
        "q-casimir-exists-proof",
        "q-casimir-unique",
        "q-casimir-unique-proof",
        "r-matrix-braiding-structure",
        "r-matrix-braiding",
        "pontryagin-dual-coxeter-character",
      ],
    }),

    // ── Lepton–meson parallel ──────────────────────────────────────────
    Object.freeze({
      title: "Leptons, mesons, and the Frobenius bridge",
      label: "sec:lepton-meson-parallel",
      blocks: [
        "lepton-meson-parallel-intro",
        "frobenius-lepton-meson-bridge",
        "hoefsmit-binding-amplitude",
        "meson-em-sinh-closed-form",
        "meson-qcg-fusion-identity",
        "q-difference-viewpoint-method",
        "alpha-em-habiro-bar-involution",
        "figure-eight-reeb-rotation",
        "pion-half-figure-eight",
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
