import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:levi-degeneracy",
  label: "rem:townsend-biot-savart-strain",
  title:
    "Townsend evolution under Biot--Savart strain: the first-order flattening $\\kappa \\to 0$",
  uses: [
    "conj:levi-degeneracy",
    "prop:core-levi-form",
    "rem:hyperbolic-overlap-saturation",
  ],
  cites: ["townsend1951", "saffman1992", "moffatt1994"],
  tags: [
    "townsend",
    "biot-savart",
    "vortex-core",
    "levi-form",
    "strain",
    "fluid-dynamics",
    "navier-stokes",
    "millennium-problem",
  ],
});
