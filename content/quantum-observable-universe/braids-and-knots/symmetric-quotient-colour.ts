import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:symmetric-quotient-colour",
  title: "The symmetric quotient and colour sectors",
  tags: ["braid-group", "colour", "symmetric-group"],
  uses: [
    "prop:braid-action-tensor",
    "def:color-sector-coords",
  ],
});
