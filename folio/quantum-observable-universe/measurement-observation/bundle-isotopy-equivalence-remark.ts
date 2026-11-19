import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bundle-isotopy-equivalence-remark",
  title: "Why bundle initial conditions are taken up to isotopy",
  interprets: "def:bundle-isotopy-equivalence",
  tags: ["definition-commentary"],
  uses: [
    "def:bundle-isotopy-equivalence",
  ],
});
