import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-obstruction",
  title: "NS obstruction class $\\mathrm{NS}(A)$",
  lean: {
    decl: "QOU.FluidDynamics.NSObstruction",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-universe",
    "def:q-navier-stokes",
    "def:ns-regular-qou",
    "def:quantum-characteristic-classes",
  ],
  tags: [
    "definition",
    "obstruction",
    "navier-stokes",
    "euler-characteristic",
    "categorical",
  ],
});
