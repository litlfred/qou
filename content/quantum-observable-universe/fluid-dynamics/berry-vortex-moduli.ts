import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:geodesic-vortices",
  label: "rem:berry-vortex-moduli",
  title: "Berry phase on the vortex moduli space",
  uses: [
    "rem:geodesic-vortices",
    "rem:braid-fluid",
    "prop:helicity-conservation",
    "prop:discrete-vortex-spectrum",
    "prop:braid-action-tensor",
  ],
  tags: ["berry-phase", "geometric-phase", "moduli-space", "vortex", "adiabatic"],
});
