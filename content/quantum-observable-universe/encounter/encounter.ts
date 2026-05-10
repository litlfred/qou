import { chapter, section } from "../../schema/builders";

/**
 * Chapter: The Encounter.
 *
 * Bridges the algebraic Gröbner-Shirshov / SDP selection
 * machinery of Chapter `particle-interactions` to the
 * Picard-Lefschetz / hyperbolic-volume machinery of
 * Chapter `descartes-universe`.
 *
 * The chapter is exposition: every block is either prose, a
 * remark interpreting an existing block, or a single
 * conditional-class proposition (Mostow confinement) using the
 * §3b conditional-class pattern.  No new sorries, no new
 * theorems with unbacked claims.
 */
export default chapter({
  title: "The Encounter",
  label: "chap:encounter",
  sections: [
    section({
      title: "From base $M$ to fibre $\\mathcal{S}_p$",
      label: "sec:encounter-from-base-to-fibre",
      blocks: [
        "encounter-intro",
        "approach-to-exceptional-divisor",
      ],
    }),
    section({
      title: "Hyperbolic relaxation and SDP selection",
      label: "sec:encounter-hyperbolic-relaxation",
      blocks: [
        "thurston-relaxation",
        "sdp-as-thimble-flow",
      ],
    }),
    section({
      title: "Mostow confinement and the Archimedean wall",
      label: "sec:encounter-mostow-confinement",
      blocks: [
        "mostow-confinement",
        "algebraic-geometric-rigidity-pairing",
        "pre-tau-vs-post-tau",
        "encounter-literature-bridge",
      ],
    }),
  ],
});
