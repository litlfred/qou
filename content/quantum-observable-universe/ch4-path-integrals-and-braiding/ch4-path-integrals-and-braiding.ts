import { chapter, section } from "../../schema/builders";

/**
 * Chapter 4: Braids, Knots and Fluid Dynamics.
 *
 * Categorical origin of braiding, braid group representations,
 * SU(2)/SO(3) framework, knot groups, quantum groups,
 * varying Euler characteristic, gauge-field fluid dynamics,
 * and information-theoretic perspectives.
 */
export default chapter({
  number: 3,
  title: "Braids, Knots and Fluid Dynamics",
  label: "chap:path-integrals-braiding",
  sections: [
    section({
      title: "Introduction",
      label: "sec:path-integrals-intro",
      blocks: [
        "ch4-intro",
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
        "symmetric-quotient-colour",
        "braid-base-field",
        "braid-lifting-compatibility",
        "jones-markov-trace",
        "markov-moves-brane-tower",
        "knot-eigenbasis-complete",
        "knot-eigenbasis-complete-proof",
        "feynman-eigenbasis",
      ],
    }),

    section({
      title: "Braid group and symmetric group",
      label: "sec:braid-symmetric",
      blocks: [
        "braid-symmetric-intro",
        "braid-group",
        "s3-group",
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
      ],
    }),

    section({
      title: "Braid involutions and holonomy",
      label: "sec:braid-involutions",
      blocks: [
        "braid-involutions-intro",
        "braid-twist-flip",
        "holonomy-trefoil",
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
        "r-matrix-braiding",
        "skein-crossing-asymmetry",
      ],
    }),

    section({
      title: "Nuclear Binding Lagrangian",
      label: "sec:nuclear-binding-lagrangian",
      blocks: [
        "skein-binding-lagrangian",
        "beta-stability",
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

    section({
      title: "Varying Euler characteristic",
      label: "sec:varying-euler",
      blocks: [
        "varying-euler-intro",
        "genus-2-intro",
      ],
    }),

    section({
      title: "Descent from $E_1$ to $E_0$ and the mirror bundle $E_{-1}$",
      label: "sec:descent-mirror",
      blocks: [
        "descent-mirror-intro",
        "e-minus-one",
      ],
    }),

    // ── Gauge-field fluid dynamics (formerly Ch. 8) ──────────────

    section({
      title: "Fluid Dynamics of the Brane",
      label: "sec:brane-fluid",
      blocks: ["brane-fluid"],
    }),
    section({
      title: "Geodesics as Stable Vortex Points",
      label: "sec:geodesic-vortices",
      blocks: ["geodesic-vortices"],
    }),
    section({
      title: "Braid Operators in the Fluid Picture",
      label: "sec:braid-fluid",
      blocks: ["braid-fluid"],
    }),
    section({
      title: "$q$-Parameter, Planck Limit, and Reynolds Number",
      label: "sec:planck-reynolds",
      blocks: ["planck-reynolds"],
    }),

    // ── Information-theoretic perspective (formerly Ch. 9) ───────

    section({
      title: "Emergent Gravity from Information Theory",
      label: "sec:emergent-gravity-info",
      blocks: ["emergent-gravity-info"],
    }),
    section({
      title: "Local Planck Length as Minimal Information Unit",
      label: "sec:planck-info-unit",
      blocks: ["planck-info-unit"],
    }),
    section({
      title: "Time as Information Transfer",
      label: "sec:time-info",
      blocks: ["time-info"],
    }),
    section({
      title: "Big Bang as Initial Information State",
      label: "sec:big-bang-info",
      blocks: ["big-bang-info"],
    }),
    section({
      title: "Planck Units and Computational Mechanics",
      label: "sec:planck-computation",
      blocks: ["planck-computation"],
    }),
  ],
});
