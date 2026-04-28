import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-obstruction",
  title: "NS obstruction class $\\mathrm{NS}(A)$",
  lean: { ref: "qou:QOU.FluidDynamics.NSObstruction",
    validation: "not_checked",
  },
  uses: ["def:ns-regular-qou"],
  tags: [
    "definition",
    "obstruction",
    "navier-stokes",
    "euler-characteristic",
    "categorical",
    "spectral-gap",
  ],
});
