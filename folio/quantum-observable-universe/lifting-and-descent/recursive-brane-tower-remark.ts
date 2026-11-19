import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:recursive-brane-tower",
  label: "rem:recursive-brane-tower-remark",
  title: "The brane relation",
  uses: ["def:recursive-brane-tower", "prop:jet-prolongation"],
});
