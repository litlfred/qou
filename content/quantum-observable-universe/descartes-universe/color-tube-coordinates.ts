import { definition } from "../../schema/builders";

export default definition({
  label: "def:color-tube-coordinates",
  lean: { ref: "qou:QOU.ColorTubeCoordinates", validation: "not_checked" },
  title: "Color tube coordinates",
  tags: ["brings-surface", "color-tube"],
  uses: ["rem:braid-group-action"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-tube-coordinates-0.svg", blockIndex: 0, hash: "8df1be36adf7" },
  ],

});
