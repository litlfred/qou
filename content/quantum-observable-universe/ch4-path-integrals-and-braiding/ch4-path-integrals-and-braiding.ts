import { chapter, section } from "../../schema/builders";

/**
 * Chapter 4: Path Integrals and Braiding.
 *
 * Categorical origin of braiding, braid group representations,
 * SU(2)/SO(3) framework, knot groups, quantum groups, and
 * varying Euler characteristic.
 */
export default chapter({
  number: 4,
  title: "Path Integrals and Braiding",
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
      ],
    }),

    section({
      title: "Categorical Möbius energy and self-avoidance",
      label: "sec:mobius-energy",
      blocks: [
        "mobius-energy",
        "non-self-intersection",
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
  ],
});
