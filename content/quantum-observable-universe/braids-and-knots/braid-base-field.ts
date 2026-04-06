import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:braid-base-field",
  title: "Independence from the base field",
  tags: ["braid-group", "base-field", "p-adic"],
  uses: [
    "prop:braid-action-tensor",
    "ex:p-adic-realisation",
    "ex:finite-field-realisation",
  ],
});
