import { paper, chapterRef } from "../schema/builders";

/**
 * Visualizer — Interactive views of QOU content.
 *
 * A companion folio providing interactive visualizations of the same
 * mathematical structures described in the QOU paper.  Definitions and
 * theorems here either re-export from the main paper (via `uses[]`) or
 * introduce visualizer-specific objects (e.g. SnapPea triangulations,
 * Bring's surface viewport state).
 *
 * This is intentionally lightweight — most content lives in the QOU
 * paper.  The visualizer folio exists to give the viewer/assistant
 * apps a separate entry point with its own chapter structure.
 */
export default paper({
  title: "QOU Visualizer",
  authors: ["litlfred"],
  chapters: [
    chapterRef({ dir: "overview" }),
  ],
});
