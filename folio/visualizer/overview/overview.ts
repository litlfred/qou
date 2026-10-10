import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Overview — entry point for the interactive visualizer.
 *
 * Sections here correspond to the main visualization modes:
 * - Bring's surface (quaternionic spectral resolvents)
 * - Knot complements (SnapPea hyperbolic 3-manifolds)
 * - Dependency graph (content-object DAG)
 */
export default chapter({
  title: "Overview",
  label: "chap:viz-overview",
  sections: [
    section({
      title: "Introduction",
      label: "sec:viz-intro",
      blocks: [
        "viz-intro",
      ],
    }),
    section({
      title: "Bring's Surface",
      label: "sec:viz-brings",
      blocks: [
        "viz-brings-surface",
      ],
    }),
    section({
      title: "Knot Complements",
      label: "sec:viz-knots",
      blocks: [
        "viz-knot-complement",
      ],
    }),
  ],
});
