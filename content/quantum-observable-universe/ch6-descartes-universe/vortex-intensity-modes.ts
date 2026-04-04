import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:vortex-intensity-modes",
  title: "Vortex intensity modes: from classical fluids to $q$-deformation",
  uses: [
    "sec:brane-fluid",
    "rem:geodesic-vortices",
    "rem:planck-reynolds",
    "rem:primordial-vortex",
  ],
  tags: ["vortex", "fluid-dynamics", "modes", "classical-bridge"],
});
