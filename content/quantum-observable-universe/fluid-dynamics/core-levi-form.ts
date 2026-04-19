import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:core-levi-form",
  lean: {
    decl: "QOU.FluidDynamics.core_levi_form",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title:
    "Core aspect ratio equals Levi form condition number on the normal plane",
  uses: [
    "prop:vorticity-lower-bound",
    "rem:geodesic-vortices",
    "def:levi-form-defect",
    "rem:c-substrate-via-levi",
    "def:substrate-parameter",
    "def:quantum-observable-universe",
  ],
  tags: [
    "levi-form",
    "condition-number",
    "contact-structure",
    "integrability",
    "core-shape",
    "millennium-problem",
  ],
});
