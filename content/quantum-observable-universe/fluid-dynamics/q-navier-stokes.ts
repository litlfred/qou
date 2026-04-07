import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-navier-stokes",
  title: "$q$-deformed Navier--Stokes equation",
  uses: [
    "rem:madelung-fluid",
    "rem:planck-reynolds",
    "def:substrate-parameter",
  ],
  tags: ["navier-stokes", "q-deformation", "dissipation", "fluid-dynamics"],
});
