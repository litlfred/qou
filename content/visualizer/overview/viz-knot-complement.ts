import { definition } from "../../schema/builders";

/**
 * Knot complement — hyperbolic 3-manifold associated to a knot
 * in the QOU particle registry.
 *
 * Uses the SnapPea kernel (WASM) for volume, homology, and
 * fundamental group computations.
 */
export default definition({
  label: "def:viz-knot-complement",
  title: "Knot complement (SnapPea)",
  tags: ["visualizer", "knot-theory", "snappea", "hyperbolic"],
  lean: { ref: "qou:QOU.KnotComplement",
    validation: "not_checked",
  },
  uses: [],
});
