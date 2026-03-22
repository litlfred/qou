import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-geometric-drag",
  title: "Mass in the brane tower",
  tags: ["mass", "brane-tower", "vortex"],
  uses: [
    "def:recursive-brane-tower",
    "def:substrate-parameter",
    "prop:jet-prolongation",
  ],
});
