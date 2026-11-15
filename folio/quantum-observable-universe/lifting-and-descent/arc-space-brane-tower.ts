import { remark } from "../../schema/builders";

export default remark({
  label: "rem:arc-space-brane-tower",
  title: "The brane tower as a jet-scheme tower carrying motivic integration",
  interprets: "def:arc-space",
  tags: ["arc-space", "jet-scheme", "brane-tower", "motivic"],
  uses: [
    "def:arc-space",
    "def:recursive-brane-tower",
    "def:motivic-mass-measure",
    "def:algebraic-quantum-volume",
  ],
});
