import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:levi-degeneracy",
  label: "rem:hyperbolic-overlap-saturation",
  title:
    "Hyperbolic-overlap strain saturation: $\\kappa^2 = \\pi\\nu/(2\\Gamma+\\pi\\nu)$ preserves Levi non-degeneracy",
  uses: [
    "conj:levi-degeneracy",
    "conj:ns-counterexample",
    "def:ns-obstruction",
    "prop:core-levi-form",
    "rem:townsend-biot-savart-strain",
    "rem:vortex-reconnection",
  ],
  cites: ["townsend1951", "saffman1992", "moffatt1994"],
  tags: [
    "townsend",
    "hyperbolic-stagnation",
    "vortex-core",
    "levi-form",
    "strain-saturation",
    "fluid-dynamics",
    "navier-stokes",
    "blowup",
    "millennium-problem",
  ],
});
