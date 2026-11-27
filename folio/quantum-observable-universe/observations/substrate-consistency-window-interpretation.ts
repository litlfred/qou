import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:aether-consistency-window",
  label: "rem:aether-consistency-window-interpretation",
  renamedFrom: ["rem:substrate-consistency-window-interpretation"],
  title: "Falsifiability of the aether consistency window",
  tags: [
    "substrate-parameter",
    "falsifiability",
    "consistency",
    "interpretation",
  ],
  uses: ["prop:aether-consistency-window"],
});
