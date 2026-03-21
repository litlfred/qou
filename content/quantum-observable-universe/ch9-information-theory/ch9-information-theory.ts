import { chapter, section } from "../../schema/builders";

/**
 * Chapter 9: Information-Theoretic Perspective.
 *
 * Five sections exploring the QOU from an information-theoretic viewpoint:
 * emergent gravity, Planck length as minimal information unit, time as
 * information transfer, Big Bang as initial information state, and Planck
 * units in computational mechanics.
 */
export default chapter({
  number: 9,
  title: "Information-Theoretic Perspective",
  label: "chap:information-theory",
  sections: [
    section({
      title: "Emergent Gravity from Information Theory",
      label: "sec:emergent-gravity-info",
      blocks: [
        "emergent-gravity-info",
      ],
    }),

    section({
      title: "Local Planck Length as Minimal Information Unit",
      label: "sec:planck-info-unit",
      blocks: [
        "planck-info-unit",
      ],
    }),

    section({
      title: "Time as Information Transfer",
      label: "sec:time-info",
      blocks: [
        "time-info",
      ],
    }),

    section({
      title: "Big Bang as Initial Information State",
      label: "sec:big-bang-info",
      blocks: [
        "big-bang-info",
      ],
    }),

    section({
      title: "Planck Units and Computational Mechanics",
      label: "sec:planck-computation",
      blocks: [
        "planck-computation",
      ],
    }),
  ],
});
