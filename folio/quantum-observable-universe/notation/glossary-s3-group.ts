import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-s3-group",
  lean: { ref: "qou:QOU.S3Group", validation: "not_checked" },
  title: "Symmetric group $S_3$",
  tags: ["glossary", "symmetric-group", "group-theory"],
  uses: ["def:braid-group"],
  defines: ["s3-group"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/s3-group-0.svg", blockIndex: 0, hash: "b1e87313a8ed" },
  ],
});
