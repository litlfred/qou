import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-braid-not-predetermined",
  title: "The braid is not predetermined: flow versus observation",
  tags: [
    "observation",
    "braid",
    "reeb-flow",
    "initial-conditions",
    "open-map",
    "computable-sections",
  ],
  uses: [
    "def:observation",
    "def:bundle-initial-conditions",
  ],
});
