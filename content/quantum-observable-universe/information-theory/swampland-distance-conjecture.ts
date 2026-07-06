import { remark } from "../../schema/builders";

export default remark({
  label: "rem:swampland-distance-conjecture",
  title: "Swampland correspondence: the brane tower and the Distance Conjecture",
  interprets: "def:jet-horizon",
  uses: [
    "def:jet-horizon",
    "def:recursive-brane-tower",
    "def:direct-limit-algebra",
  ],
  tags: [
    "swampland",
    "distance-conjecture",
    "brane-tower",
    "jet-horizon",
    "external-program",
  ],
  cites: ["ooguri-vafa2007"],
});
