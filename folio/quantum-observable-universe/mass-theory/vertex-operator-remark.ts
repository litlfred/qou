import { remark } from "../../schema/builders";

export default remark({
  label: "rem:vertex-operator-remark",
  title: "Contour modes and the operator product expansion",
  interprets: "def:vertex-operator",
    "def:reeb-bundle",
  uses: [
    "def:vertex-operator",
    "def:reeb-bundle",
  ],
});
