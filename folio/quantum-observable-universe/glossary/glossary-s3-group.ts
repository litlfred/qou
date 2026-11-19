import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-s3-group",
  title: "Symmetric group $S_3$",
  tags: ["glossary", "symmetric-group", "group-theory"],
  uses: ["def:braid-group"],
  defines: ["s3-group"],
});
