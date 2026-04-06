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

    section({
      title: "Categorical origin of braiding",
      label: "sec:categorical-braiding",
      blocks: [
        "categorical-braiding-intro",
        "braid-action-tensor",
        "braid-action-tensor-proof",
        "why-b3",
        "categorical-boson-fermion",
        "symmetric-quotient-colour",
        "braid-base-field",
        "braid-lifting-compatibility",
        "jones-markov-trace",
        "markov-moves-brane-tower",
        "knot-eigenbasis-complete",
        "knot-eigenbasis-complete-proof",
        "knot-exhaustiveness",
        "feynman-eigenbasis",
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
      ],
    }),

    section({
      title: "$\\mathrm{SU}(2)$ and $\\mathrm{SO}(3)$ framework",
      label: "sec:su2-so3",
      blocks: [
        "su2-so3-intro",
        "su2-basis",
        "first-order-taylor",
        "su2-generators",
        "so3-generators",
        "quaternion-so3-motivation",
      ],
    }),

    section({
      title: "Braid involutions and holonomy",
      label: "sec:braid-involutions",
      blocks: [
        "braid-involutions-intro",
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
        "r-matrix-braiding-structure",
        "r-matrix-braiding",
        "skein-crossing-asymmetry-prop",
        "skein-crossing-asymmetry",
      ],
    }),

    section({
      title: "Categorical Möbius energy and self-avoidance",
      label: "sec:mobius-energy",
      blocks: [
        "mobius-energy",
        "mobius-energy-proof",
        "non-self-intersection",
        "non-self-intersection-proof",
      ],
    }),

    // ── Crossing energy and stability ───────────────────────────────────
    section({
      title: "Crossing energy and Coulomb charge",
      label: "sec:crossing-energy",
      blocks: [
        "crossing-energy",
        "crossing-energy-trefoil",
        "coulomb-charge",
      ],
    }),

    // ── Lagrange resolvents (categorical DFT) ─────────────────────────
    section({
      title: "Lagrange Resolvents and $q$-Deformed Kinematics",
      label: "sec:lagrange-q-kinematics",
      blocks: [
        // DFT decomposition of cyclic representations
        "lagrange-resolvent-transform",
        "lagrange-resolvents",
        // q-deformed physical quantities (general QOU)
        "q-momentum",
        "q-angular-momentum",
        "q-angular-momentum-interpretation",
        "q-energy",
        "noether-theorem-callout",
      ],
    }),

    // ── Vertex operators and the Markov trace ────────────────────────
    section({
      title: "Vertex Operators and the Markov Trace",
      label: "sec:vertex-operators-markov",
      blocks: [
        // Exceptional divisor and Reeb bundle (general QOU)
        "exceptional-divisor",
        "reeb-bundle",
        "reeb-exceptional-divisor",
        // Vertex operator algebra
        "vertex-operator",
        "vertex-operator-dictionary",
        // Vertex operators factor through E_p
        "vertex-is-exceptional-divisor",
        "vertex-is-exceptional-divisor-proof",
        // Product factorization of the Markov trace
        "markov-trace-product",
        "markov-trace-product-interpretation",
        // Categorical transfer matrix and level independence
        "categorical-transfer-matrix",
        "transfer-matrix-level-independence",
        "transfer-matrix-level-independence-proof",
        // Topological mass (archimedean specialization)
        "topological-mass-formula",
        "skein-decomposition",
        "topological-field-ansatz",
        // Categorical vs archimedean braiding
        "skein-archimedean-shadow",
        // QU/QUO axioms as relations on Hecke generators
        "vertex-algebra-relations",
        // Relations lifted to the jet bundle
        "vertex-algebra-jet-relations",
        // T_{2,11} annihilation by the spectral filter ideal
        "t211-ideal-annihilation",
      ],
    }),

    // ── Hadrons and knot composites ──────────────────────────────────
    section({
      title: "Hadrons and Knot Composites",
      label: "sec:hadrons-knot-composites",
      blocks: [
        "hadron",
        "hadron-interpretation",
        "hadron-operations-closure",
        "hadron-operations",
        "knot-factorization",
        "localized-hadron",
        "hadron-fibre-embedding",
        "skein-generation",
        "skein-generation-proof",
        "knot-particle-generation",
        "knot-particle-generation-interpretation",
        "knot-particle-correspondence",
        "knot-particle-dictionary",
        "quarks-borromean-picture",
        "bundle-initial-conditions",
        "observation-braid",
        "sorting-color-energy",
        "bundle-isotopy-equivalence",
        "torsion-knot-flow",
        "bundle-category",
      ],
    }),

    // ── Borromean baryons and fermion/boson classification ─────────────
    section({
      title: "Borromean Baryons and Reidemeister Invariance",
      label: "sec:borromean-reidemeister",
      blocks: [
        "borromean-baryon",
        "borromean-baryon-interpretation",
        "hadron-proton-example",
        "fermion-boson-knot-link",
        "reidemeister-mass-invariance",
        "nuclear-shell-intruder",
        "nuclear-shell-intruder-interpretation",
      ],
    }),

    // ── Topological mass + nuclear binding (from lifting-and-descent §12) ───
    section({
      title: "Topological Mass and Nuclear Binding",
      label: "sec:topological-mass-binding",
      blocks: [
        "topological-mass",
        "topological-mass-categorical-proof",
        "topological-mass-trefoil",
        "skein-binding-lagrangian",
        "beta-stability",
        "beta-stability-interpretation",
      ],
    }),

    // ── Varying Euler + mirror bundle (merged — 2+2 blocks) ──────────
    section({
      title: "Varying Euler Characteristic and the Mirror Bundle",
      label: "sec:varying-euler-mirror",
      blocks: [
        "varying-euler-intro",
        "genus-2-intro",
        "descent-mirror-intro",
        "e-minus-one",
      ],
    }),
  ],
});
