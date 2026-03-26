import { chapter, section } from "../../schema/builders";

/**
 * Chapter 8: Information-Theoretic Perspectives.
 *
 * Emergent gravity from information geometry, Planck-scale information
 * units, information-theoretic time, Big Bang through an information
 * lens, computation at Planck time lengths, statistical mechanics,
 * and alternative Euler-characteristic scenarios.
 */
export default chapter({
  number: 8,
  title: "Information-Theoretic Perspectives",
  label: "chap:info-theory",
  sections: [
    section({
      title: "Emergent Gravity and Information Geometry",
      label: "sec:info-emergent-gravity",
      blocks: [
        "emergent-gravity-info",
        "planck-info-unit",
      ],
    }),
    section({
      title: "Time and Computation",
      label: "sec:info-time-computation",
      blocks: [
        "time-info",
        "big-bang-info",
        "planck-computation",
      ],
    }),
    section({
      title: "Computation at Planck Time Lengths",
      label: "sec:planck-scale-computation",
      blocks: [
        "planck-scale-computation",
      ],
    }),
    section({
      title: "Statistical Mechanics",
      label: "sec:stat-mech",
      blocks: [
        "stat-mech-intro",
      ],
    }),
    section({
      title: "Quantum Geometry Variants",
      label: "sec:info-geometry-variants",
      blocks: [
        "quantum-brings-intro",
        "other-euler-intro",
      ],
    }),
  ],
});
