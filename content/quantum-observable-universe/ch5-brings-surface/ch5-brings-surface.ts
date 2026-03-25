import { chapter, section } from "../../schema/builders";

/**
 * Chapter 5 (was 4): Bring's Surface.
 *
 * The classical and quantum geometry of Bring's surface as a
 * quantum observable universe: spectral resolvents, color tube
 * coordinates, chiral fibrations, and Seiberg--Witten theory.
 */
export default chapter({
  number: 5,
  title: "Bring's Surface",
  label: "chap:brings-surface",
  sections: [
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

    section({
      title: "Quantum Brings",
      label: "sec:quantum-brings",
      blocks: [
        "quantum-brings-intro",
      ],
    }),

    section({
      title: "Other Euler characteristics",
      label: "sec:other-euler",
      blocks: [
        "other-euler-intro",
      ],
    }),
  ],
});
