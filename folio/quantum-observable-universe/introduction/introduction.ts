import { chapter, section } from "../../schema/builders";

/**
 * Chapter 0: Introduction.
 *
 * Three sections:
 *   1. Overview        — narrative story of the paper's claim.
 *   2. Chapter overview — chapter-by-chapter walkthrough + roadmap.
 *   3. Author's note    — postscript on Lean/LLM authorship + Pascal.
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
        "intro",
      ],
    }),
    section({
      title: "Chapter overview",
      label: "sec:chapter-overview",
      blocks: [
        "chapter-overview",
      ],
    }),
    section({
      title: "Author's note",
      label: "sec:authors-note",
      blocks: [
        "authors-note",
      ],
    }),
  ],
});
