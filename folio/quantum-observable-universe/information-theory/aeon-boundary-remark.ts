import { remark } from "../../schema/builders";

export default remark({
  label: "rem:aeon-boundary-remark",
  title: "Boundary objects of an aeon",
  interprets: "def:aeon-boundary",
  tags: ["definition-commentary"],
  uses: [
    "def:aeon-boundary",
  ],
});
