import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cemetery-group-remark",
  title: "The cemetery group is emergent",
  interprets: "def:cemetery-group",
  tags: ["klr", "decategorification"],
  uses: [
    "def:cemetery-group",
  ],
});
