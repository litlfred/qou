import { chapter, section } from "../../schema/builders";

/**
 * Chapter 5: The Descartes Universe.
 *
 * Opens with a physical preamble (three observable colors, time,
 * rotation on a sphere), then develops Bring's surface (χ = −6),
 * color-tube coordinates, chiral fibrations, Seiberg--Witten theory,
 * the Descartes condition, and the categorical definitions of proton
 * and neutron.
 *
 * The Archimedean wall sits after the Descartes theorem;
 * all observational content is in the following Observations chapter.
 */
export default chapter({
  number: 6,
  title: "The Descartes Universe",
  label: "chap:descartes-universe",
  sections: [
    // ── Physical preamble ─────────────────────────────────────────────
    section({
      title: "Why this universe",
      label: "sec:descartes-preamble",
      blocks: [
        "descartes-preamble",
      ],
    }),

    // ── Bring's surface geometry ──────────────────────────────────────
    section({
      title: "Bring's surface as a QOU",
      label: "sec:brings-qou",
      blocks: [
        "brings-surface",
        "brings-realisations",
        "brings-is-qou",
        "brings-is-qou-proof",
        "brings-qou-4tuple",
        "brings-qou-axiom-map",
      ],
    }),

    section({
      title: "Lagrange resolvents and braid-group action",
      label: "sec:resolvents-braid",
      blocks: [
        "lagrange-resolvents",
        "braid-group-action",
      ],
    }),

    section({
      title: "Color tube coordinates",
      label: "sec:color-tube",
      blocks: [
        "color-tube-coordinates",
        "aggregate-color-quantities",
        "color-tube-constraints",
        "color-tube-interpretation",
        "c5-color-tube",
        "intrinsic-color-cubic-pairing",
      ],
    }),

    section({
      title: "Chiral fibration and elliptic curves",
      label: "sec:chiral-fibration",
      blocks: [
        "chiral-elliptic",
        "chiral-elliptic-proof",
        "t-duality-elliptic",
        "color-tube-cubic",
        "color-tube-fibers",
        "observed-value",
        "t-duality-color-tube",
        "color-tube-subloci",
      ],
    }),

    section({
      title: "Bundle structures and smoothness",
      label: "sec:bundle-structures",
      blocks: [
        "chiral-bundles",
        "brings-smoothness",
        "briggs-klein-chart",
        "radial-projection",
        "four-colourability",
        "four-colour-theorem",
        "cyclotomic-reduction",
      ],
    }),

    section({
      title: "Quaternionic spectral resolvents",
      label: "sec:quaternionic-resolvents",
      blocks: [
        "quaternion-so3-motivation",
        "quaternionic-spectral-resolvents",
        "omega-constraints",
        "spectral-dynamics",
        "primordial-vortex",
        "geometric-drag",
      ],
    }),

    section({
      title: "Geometric resolution and Seiberg--Witten theory",
      label: "sec:seiberg-witten",
      blocks: [
        "seiberg-witten",
        "reeb-exceptional-divisor",
        "generation-dependent-sw",
        "mi-sw-abelianisation",
        "mi-sw-abelianisation-proof",
      ],
    }),

    // ── Descartes condition and structure (from ch11 §1-6) ────────────
    section({
      title: "The Descartes condition",
      label: "sec:descartes-condition",
      blocks: [
        "descent-to-zero",
        "descartes-condition",
        "descartes-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
      ],
    }),

    // (Trefoil subgroups merged with leptons — both ≤3 blocks)
    section({
      title: "Leptons, chirality, and trefoil subgroups",
      label: "sec:descartes-leptons-chirality",
      blocks: [
        "descartes-leptons",
        "descartes-chirality",
        "light-cone-affine",
        "chirality-trefoil",
        "brings-curve",
      ],
    }),

    // (Colour-sector coords merged with braid structure)
    section({
      title: "Categorical braid structure and colour sectors",
      label: "sec:descartes-braid",
      blocks: [
        "exceptional-divisor",
        "chiral-sector-coords",
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "descartes-knot-eigenbasis",
        "skein-archimedean-shadow",
      ],
    }),

    // ── Torus knot generators and embeddability (from ch3) ────────────
    // χ(A) = −6 ⟹ genus 4 ⟹ only finitely many torus knots embed,
    // selecting the specific generator set that produces all particles.
    section({
      title: "Torus knot generators from $\\chi = -6$",
      label: "sec:torus-knot-generators",
      blocks: [
        "torus-knot-generators",
        "embeddability-closure",
      ],
    }),

    // ── Categorical proton, neutron, stable nucleus (from ch3) ────────
    section({
      title: "Categorical proton, neutron, and stable nucleus",
      label: "sec:categorical-particles",
      blocks: [
        "categorical-proton",
        "categorical-neutron",
        "stable-nucleus",
        "torus-hopf-stability",
      ],
    }),

    // ── The Descartes theorem ─────────────────────────────────────────
    section({
      title: "The Descartes theorem",
      label: "sec:descartes-theorem",
      blocks: [
        "descartes",
        "descartes-proof",
        "universality-general",
        "descartes-yekutieli",
        "observation-brings",
      ],
    }),

    // ── Misc (stub remarks) ──────────────────────────────────────────
    section({
      title: "Further directions",
      label: "sec:brings-misc",
      blocks: [
        "quantum-brings-intro",
        "other-euler-intro",
      ],
    }),
  ],
});
