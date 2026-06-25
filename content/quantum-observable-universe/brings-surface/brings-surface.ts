import { chapter, section } from "../../schema/builders";

/**
 * Chapter 7 — Bring's Surface (deep).
 *
 * The canonical archimedean model: the genus-4 surface $\Sigma_4$ with
 * $\chi = -6$, on which an $S_5$ action exchanges the five
 * quark–lepton families and a cohomological defect produces the three
 * QCD colours. This chapter develops the deep structural facts; the
 * basics are inlined in the framing chapter Ch 3 §4.
 *
 * Phase 5 (2026-05-25): created by splitting archimedean-universe.
 * Receives 15 sections (129 blocks, including opener): physical-regime
 * preamble, Bring's algebraic substructure, color tube coordinates,
 * color fibration, smoothness, spectral and gauge structures, $\chi =
 * -6$ Descartes condition (statement, leptons, genus completeness),
 * cohomological defect, Descartes theorem, orbital symmetry embedding.
 *
 * Story-arc placement: Part II "Structural Mechanics" Ch 7 — the
 * geometric step's canonical surface. Consumes the Hecke algebra (Ch 5)
 * and the climax volume identity (Ch 6); hands off to Statistics &
 * Symmetrisation (Ch 8), Particles (Ch 9), and Mass — Theory (Ch 10).
 */
export default chapter({
  title: "Bring's Surface",
  label: "chap:brings-surface",
  sections: [
    section({
      title: "Why this universe",
      label: "sec:archimedean-preamble",
      blocks: [
        "archimedean-preamble",
      ],
    }),
    section({
      title: "Physical regimes and limiting context",
      label: "sec:physical-regimes",
      blocks: [
        "physical-regimes-intro",
        "brings-surface-unit-circle",
        "primordial-vortex",
        "geometric-drag",
      ],
    }),
    section({
      title: "Bring's surface algebraic substructure",
      label: "sec:bring-algebraic-substructure",
      blocks: [
        "bring-algebraic-substructure-intro",
        "su2-generators",
        "hyperelliptic-quintic",
        "x5-z5-automorphism",
        "x5-bring-weight-identification",
      ],
    }),
    section({
      title: "Bring's surface as a QOU",
      label: "sec:brings-surface-qou",
      blocks: [
        "brings-surface-qou-intro",
        "brings-surface-def",
        "brings-surface-example",
        "brings-realisations",
        "brings-physics-interpretations",
        "brings-is-qou",
        "brings-euler-characteristic",
        "brings-euler-characteristic-proof",
        "brings-riemann-hurwitz",
        "brings-riemann-hurwitz-proof",
        "brings-is-qou-proof",
        "brings-qou-4tuple",
        "brings-qou-axiom-map",
        "braid-group-action",
      ],
    }),
    section({
      title: "Color tube coordinates",
      label: "sec:color-tube-coords",
      blocks: [
        "color-tube-coords-intro",
        "color-tube-coordinates",
        "aggregate-color-quantities",
        "color-tube-constraints",
        "color-tube-interpretation",
        "c5-color-tube",
        "intrinsic-color-cubic-pairing",
      ],
    }),
    section({
      title: "Color fibration and elliptic curves",
      label: "sec:color-fibration-elliptic",
      blocks: [
        "color-fibration-elliptic-intro",
        "color-elliptic",
        "color-elliptic-proof",
        "t-duality-elliptic",
        "color-tube-cubic",
        "color-tube-fibers",
        "t-duality-color-tube",
        "color-tube-subloci",
        "pure-colour-sublocus",
      ],
    }),
    section({
      title: "Bundle structures and smoothness",
      label: "sec:brings-smoothness",
      blocks: [
        "brings-smoothness-intro",
        "color-bundles",
        "brings-smoothness-resolution",
        "brings-smoothness",
        "approach-to-exceptional-divisor",
        "thurston-relaxation",
        "briggs-klein-chart",
        "radial-projection",
        "four-colourability",
        "four-colour-theorem",
        "cyclotomic-reduction",
      ],
    }),
    section({
      title: "Spectral resolvents and gauge structures",
      label: "sec:spectral-gauge",
      blocks: [
        "spectral-gauge-intro",
        "quaternionic-spectral-resolvents",
        "omega-constraints",
        "spectral-dynamics",
        "mi-sw-abelianisation",
        "mi-sw-abelianisation-cartan",
        "mi-sw-abelianisation-cartan-proof",
        "mi-sw-abelianisation-proof",
        "sw-period-residue-sum",
        "sw-period-residue-sum-proof",
        "jet-sw-tau-decomposition",
        "jet-sw-tau-decomposition-proof",
        "color-sector-coords",
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "descartes-knot-eigenbasis",
        "descartes-elliptic-curve",
      ],
    }),
    section({
      title: "The Descartes condition $\\\\chi = -6$",
      label: "sec:archimedean-condition-statement",
      blocks: [
        "archimedean-condition-intro",
        "descent-to-zero",
        "archimedean-condition",
        "chi-minus-six-chain",
        "archimedean-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
      ],
    }),
    section({
      title: "Descartes condition: leptons and chirality",
      label: "sec:archimedean-condition-leptons",
      blocks: [
        "archimedean-condition-leptons-intro",
        "archimedean-leptons",
        "archimedean-chirality",
        "light-cone-affine",
        "chirality-trefoil",
        "brings-curve",
      ],
    }),
    section({
      title: "Descartes condition: torus-knot generators and genus completeness",
      label: "sec:archimedean-condition-genus-completeness",
      blocks: [
        "archimedean-condition-genus-intro",
        "torus-knot-generators",
        "torus-knot-generators-table-data",
        "embeddability-closure",
        "embeddability-closure-table-data",
        "genus-from-hecke-completeness",
        "genus-from-hecke-completeness-proof",
        "chebyshev-degree-genus",
        "chebyshev-degree-genus-proof",
        "genus-ideal-characterisation",
      ],
    }),
    section({
      title: "The genus-ideal filtration",
      label: "sec:archimedean-condition-genus-completeness-genus-ideal-characterisation",
      blocks: [
        "archimedean-condition-genus-completeness-genus-ideal-characterisation-intro",
        "genus-ideal-characterisation-proof",
        "yekutieli-leading-coefficient",
        "yekutieli-leading-coefficient-proof",
        "genus-filtration-ideal",
        "genus-filtration-ideal-table2-data",
        "genus-filtration-ideal-table1-data",
        "genus-filtration-ideal-proof",
        "genus-filtration-interpretation",
        "torus-embeddable-complete",
        "bring-trefoil-cinquefoil-channel",
        "generation-completeness",
      ],
    }),
    section({
      title: "The unit particle as a cohomological defect",
      label: "sec:cohomological-defect",
      blocks: [
        "cohomological-defect-intro",
        "levi-form-defect",
        "maximal-ideal-defect",
        "local-cohomology-group",
        "unit-particle-state",
        "topological-charge-quantization",
        "defect-legendrian-knot",
      ],
    }),
    section({
      title: "The Descartes theorem",
      label: "sec:descartes-theorem",
      blocks: [
        "descartes-theorem-intro",
        "descartes",
        "descartes-proof",
        "terminal-morphism-brings",
        "universality-general",
        "archimedean-yekutieli",
        "observation-brings",
      ],
    }),
    section({
      title: "Orbital Symmetry and Cohomological Embedding",
      label: "sec:orbital-symmetry-embedding",
      blocks: [
        "orbital-symmetry-embedding-intro",
        "orbital-space-normal-bundle",
        "orbital-fourier-decomposition",
        "fivefold-symmetry",
        "fivefold-symmetry-table2-data",
        "fivefold-symmetry-table1-data",
        "cohomological-embedding",
        "cohomological-embedding-table1-data",
        "cohomological-embedding-table2-data",
        "knot-basis-color-content",
        "trivial-knot-photon-interpretation",
        "trivial-knot-photon-interpretation-table5-data",
        "trivial-knot-photon-interpretation-table4-data",
        "trivial-knot-photon-interpretation-table3-data",
        "trivial-knot-photon-interpretation-table2-data",
        "trivial-knot-photon-interpretation-table1-data",
        "outro-archimedean-universe",
      ],
    }),
    section({
      title: "Reconnected orphan blocks (Phase 7)",
      label: "sec:brings-surface-orphan-reconnect",
      blocks: [
        "brings-surface-orphan-reconnect-intro",
        "bring-fibre-q0-figure",
        "bring-fibre-qhalf-figure",
        "inter-nucleon-channel-color-tube",
        "c-from-color-flavor-swap",
        "outro-brings-surface",
      ],
    }),
  ],
});
