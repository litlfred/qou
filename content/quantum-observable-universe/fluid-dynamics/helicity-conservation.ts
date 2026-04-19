import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:helicity-conservation",
  lean: {
    decl: "QOU.FluidDynamics.helicity_conservation",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title: "Categorical helicity conservation",
  uses: [
    "rem:braid-fluid",
    "thm:jones-markov-trace",
    "rem:madelung-fluid",
    "prop:discrete-vortex-spectrum",
  ],
  tags: ["helicity", "topological-invariant", "conservation", "fluid-dynamics", "knot"],
});
