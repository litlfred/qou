import { definition } from "../../schema/builders";

export default definition({
  label: "def:s3-group",
  lean: { decl: "QOU.S3Group" },
  title: "Symmetric group $S_3$",
  tags: ["symmetric-group", "group-theory"],
  uses: ["def:braid-group"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/s3-group-0.svg", blockIndex: 0, hash: "b1e87313a8ed" },
  ],

});
