import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:recursive-brane-tower",
  label: "rem:mass-geometric-drag",
  title: "Mass in the brane tower",
  tags: ["mass", "brane-tower", "vortex"],
  uses: [
    "def:recursive-brane-tower",
    "def:substrate-parameter",
  ],
});
