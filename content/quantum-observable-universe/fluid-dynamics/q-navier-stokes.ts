import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-navier-stokes",
  title: "$q$-deformed Navier--Stokes equation",
  lean: {
    ref: "qou:QOU.FluidDynamics.QNavierStokes",
    validation: "not_checked",
  },
  uses: ["rem:planck-reynolds"],
  tags: ["navier-stokes", "q-deformation", "dissipation", "fluid-dynamics"],
});
