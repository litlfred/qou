import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:braid-lifting-compatibility",
  title: "Compatibility with the lifting theorem",
  tags: ["braid-group", "jet-prolongation", "direct-limit"],
  uses: ["prop:braid-action-tensor", "prop:jet-prolongation"],
});
