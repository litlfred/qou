import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-regular-qou",
  title: "NS-regular quantum observable universe",
  lean: {
    ref: "qou:QOU.FluidDynamics.NSRegularQOU",
    validation: "not_checked",
  },
  uses: ["def:q-navier-stokes"],
  tags: [
    "definition",
    "navier-stokes",
    "obstruction",
    "euler-characteristic",
    "categorical",
  ],
});
