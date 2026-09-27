import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-obstruction-tower",
  lean: { ref: "qou:QOU.FluidDynamics.ns_obstruction_tower", validation: "not_checked" },
  title:
    "The NS obstruction class in the Yekutieli tower",
  uses: [
    "def:ns-regular-qou",
    "prop:core-levi-form",
  ],
  tags: [
    "obstruction",
    "yekutieli",
    "cohomology",
    "navier-stokes",
    "boundary-observability",
    "euler-class",
  ],
});
