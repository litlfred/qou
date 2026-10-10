import { chapter, section } from "../../schema/builders";

/**
 * Chapter 0: Introduction.
 *
 * Written for a mathematically literate reader who has not met category
 * theory or the paper's physics vocabulary. The arc:
 *   1. Overview              — observations → the structure they force.
 *   2. The substrate parameter — one family of universes, labelled by q.
 *   3. State space and knots  — Bring's surface, the knot dictionary,
 *                               the Hecke algebra, the photon.
 *   4. From structure to numbers — the derivation chain in words.
 *   5. Mathematics and measurement — where the empirical claims live;
 *                               CAL-1/2/3 only, no fitting.
 *   6. Chapter overview       — chapter-by-chapter walkthrough.
 *   7. Author's note          — Lean/LLM authorship + Pascal.
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
      title: "The substrate parameter",
      label: "sec:introduction-substrate-parameter",
      blocks: [
        "intro-substrate-parameter",
      ],
    }),
    section({
      title: "State space and knots",
      label: "sec:introduction-state-space-knots",
      blocks: [
        "intro-particles-as-knots",
      ],
    }),
    section({
      title: "From structure to numbers",
      label: "sec:introduction-structure-to-numbers",
      blocks: [
        "intro-structure-to-numbers",
      ],
    }),
    section({
      title: "Mathematics and measurement",
      label: "sec:introduction-mathematics-measurement",
      blocks: [
        "intro-model-and-measurement",
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
