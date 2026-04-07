import { chapter, section } from "../../schema/builders";

/**
 * Chapter 0: Introduction.
 *
 * Motivation and statement of the main result.
 */
export default chapter({
  title: "Introduction",
  label: "chap:ugb-introduction",
  sections: [
    section({
      title: "Motivation",
      label: "sec:ugb-motivation",
      blocks: [
        "ugb-intro",
        "ugb-example-polynomial",
        "ugb-example-pbw",
      ],
    }),
    section({
      title: "Main result",
      label: "sec:ugb-main-result",
      blocks: [
        "ugb-main-theorem-statement",
      ],
    }),
  ],
});
