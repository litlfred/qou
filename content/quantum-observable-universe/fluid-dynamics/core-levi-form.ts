import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:core-levi-form",
  lean: { ref: "qou:QOU.FluidDynamics.core_levi_form", validation: "not_checked" },
  title:
    "Core aspect ratio equals Levi form condition number on the normal plane",
  uses: [
    "prop:vorticity-lower-bound",
    "rem:c-substrate-via-levi",
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
