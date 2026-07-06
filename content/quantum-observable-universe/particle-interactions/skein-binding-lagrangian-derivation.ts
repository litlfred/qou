import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:skein-binding-lagrangian",
  label: "rem:skein-binding-lagrangian-derivation",
  title: "Derivation of the Skein binding Lagrangian from the canonical action",
  tags: [
    "lagrangian",
    "binding",
    "skein",
    "nuclear",
    "bethe-weizsacker",
    "canonical-action",
  ],
  uses: [
    "def:skein-binding-lagrangian",
    "prop:qou-canonical-action",
    "def:categorical-lagrangian",
  ],
});
