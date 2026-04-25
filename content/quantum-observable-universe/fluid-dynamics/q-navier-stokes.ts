import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-navier-stokes",
  title: "$q$-deformed Navier--Stokes equation",
  lean: {
    decl: "QOU.FluidDynamics.QNavierStokes",
    validation: "not_checked",
  },
  uses: [
    "rem:madelung-fluid",
    "rem:planck-reynolds",
    "def:substrate-parameter",
  ],
  tags: ["navier-stokes", "q-deformation", "dissipation", "fluid-dynamics"],
});
