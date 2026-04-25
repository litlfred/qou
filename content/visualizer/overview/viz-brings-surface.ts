import { definition } from "../../schema/builders";

/**
 * Bring's surface viewport state — describes the serialisable configuration
 * for the interactive 3D visualizer.
 *
 * TypeScript types: schemas/qou-types.ts §10 VizState
 */
export default definition({
  label: "def:viz-brings-surface",
  title: "Bring's surface viewport",
  tags: ["visualizer", "brings-surface", "snappea"],
  lean: {
    decl: "QOU.BringsSurface.ViewportState",
    file: "QOU/BringsSurface/Viewport.lean",
    validation: "not_checked",
  },
  uses: [],
});
