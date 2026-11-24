import { remark } from "../../schema/builders";

export default remark({
  label: "rem:molecular-braid-remark",
  title: "Sign of the molecular binding energy",
  interprets: "def:molecular-braid",
  tags: ["definition-commentary"],
  uses: [
    "def:molecular-braid",
  ],
});
