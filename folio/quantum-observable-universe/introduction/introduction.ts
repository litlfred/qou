import { chapter, section } from "../../schema/builders";

/**
 * Chapter 0: Introduction.
 *
 * Written for a mathematically literate reader who has not met category
 * theory or the paper's physics vocabulary. One Overview section carries
 * the opening and four titled subsections (owner ruling 2026-10-10: one
 * Overview, with the five parts kept as headings for navigation):
 *   1.   Overview (opening)        — observations → the structure they
 *                                    force; motivation from Einstein,
 *                                    Heisenberg, Wigner, Noether;
 *                                    constants that need not be constant.
 *   1.1  The aether parameter      — one family of universes, labelled by q.
 *   1.2  State space and knots     — Bring's surface, the knot dictionary,
 *                                    the Hecke algebra, the photon.
 *   1.3  From structure to numbers — the derivation chain in words.
 *   1.4  Mathematics and measurement — where the empirical claims live;
 *                                    CAL-1/2/3 only, no fitting.
 *   2.   Chapter overview          — chapter-by-chapter walkthrough.
 *   3.   Author's note             — Lean/LLM authorship + Pascal.
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
      subsections: [
        section({
          title: "The aether parameter",
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
