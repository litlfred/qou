import { chapter, section } from "../../schema/builders";

/**
 * Chapter 0: Introduction.
 *
 * A guide to the paper's structure and main results.
 */
export default chapter({
  tabLabel: "I",
  title: "Introduction",
  label: "chap:introduction",
  sections: [
    section({
      title: "Overview",
      label: "sec:introduction-overview",
      blocks: [
        "ch0-intro",
        "roadmap-diagram",
      ],
    }),
  ],
});
