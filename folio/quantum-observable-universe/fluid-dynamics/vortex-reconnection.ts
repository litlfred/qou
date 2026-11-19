import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:madelung-fluid",
  label: "rem:vortex-reconnection",
  title: "Vortex reconnection as divisor surgery",
  uses: [
    "prop:helicity-conservation",
    "rem:trefoil-vortex-chirality-flip",
  ],
  cites: ["enciso2017", "scheeler2014"],
  tags: ["vortex", "reconnection", "divisor", "topology-change", "pair-creation"],
  authorNotes: [
    {
      kind: "status",
      body: "Crossing-change and Reidemeister invariance of mutual helicity formalized in `QOU.FluidDynamics.VortexLink` (`crossingChange_lk`, `crossingChange_mutualHelicity`, `mutualHelicity_R2`, `mutualHelicity_braid`).",
    },
  ],
});
