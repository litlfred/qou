import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bundle-initial-conditions-remark",
  title: "Bundle initial conditions as position-only data",
  interprets: "def:bundle-initial-conditions",
  tags: ["definition-commentary"],
  uses: [
    "def:bundle-initial-conditions",
  ],
});
