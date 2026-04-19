import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:blowup-yekutieli",
  lean: {
    decl: "QOU.FluidDynamics.blowup_yekutieli",
    validation: "not_checked",
  },
  title:
    "Blowup mechanism as Yekutieli lifting obstruction in the brane tower",
  uses: [
    "conj:regularity-breakdown",
    "def:quantum-characteristic-classes",
    "def:yekutieli-lifting-condition",
    "prop:yekutieli-lifting",
    "prop:descent-condition",
    "def:recursive-brane-tower",
    "def:local-cohomology-group",
    "rem:madelung-fluid",
    "rem:vortex-reconnection",
    "rem:hamilton-jacobi-phase",
  ],
  tags: [
    "blowup",
    "yekutieli",
    "obstruction",
    "cohomology",
    "brane-tower",
    "gerbe",
    "millennium-problem",
  ],
});
