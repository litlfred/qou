import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-obstruction-tower",
  lean: {
    decl: "QOU.FluidDynamics.ns_obstruction_tower",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title:
    "The NS obstruction class in the Yekutieli tower",
  uses: [
    "def:ns-regular-qou",
    "def:quantum-characteristic-classes",
    "def:yekutieli-lifting-condition",
    "prop:yekutieli-lifting",
    "thm:qu-to-qou",
    "def:recursive-brane-tower",
    "def:local-cohomology-group",
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
