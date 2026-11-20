import { remark } from "../../schema/builders";

// Was prf:calibration-cohomology-alignment. The block it argued for is now the
// conjecture conj:calibration-cohomology-alignment (owner choice 2026-11-20,
// bean qou-tm3c), so the argument is recorded as a sketch (AGENTS.md §3b).
export default remark({
  label: "rem:calibration-cohomology-alignment-sketch",
  title: "Why the calibrations match the cohomological data (sketch)",
  interprets: "conj:calibration-cohomology-alignment",
  uses: ["conj:calibration-cohomology-alignment", "prop:meson-scale-independence"],
});
