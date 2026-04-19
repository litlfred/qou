import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vorticity-lower-bound",
  lean: {
    decl: "QOU.FluidDynamics.vorticity_lower_bound",
    validation: "not_checked",
  },
  title:
    "Vorticity lower bound for anti-parallel filament collision as $q \\to 1$",
  uses: [
    "thm:q-bkm",
    "thm:q-aubin-lions",
    "conj:ns-counterexample",
    "rem:geodesic-vortices",
    "rem:madelung-fluid",
    "prop:blowup-yekutieli",
  ],
  tags: [
    "vorticity",
    "lower-bound",
    "biot-savart",
    "anti-parallel",
    "blowup",
    "last-gap",
  ],
});
