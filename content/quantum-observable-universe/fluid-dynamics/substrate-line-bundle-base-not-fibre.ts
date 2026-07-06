import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-line-bundle",
  label: "rem:substrate-line-bundle-base-not-fibre",
  title: "The QOU structure is the base, not the fibre",
  uses: ["def:substrate-line-bundle"],
});
