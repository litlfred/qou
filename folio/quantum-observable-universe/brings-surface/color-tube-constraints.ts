import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:color-tube-coordinates",
  label: "rem:color-tube-constraints",
  title: "Constraint equations in color tube coordinates",
  uses: [
    "rem:aggregate-color-quantities",
    "prop:x5-bring-weight-identification",
    "rem:u1-phase-tube",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-0.svg", blockIndex: 0, hash: "560d3f6cd3c0" },
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-1.svg", blockIndex: 1, hash: "9e3dff9fca6d" },
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-2.svg", blockIndex: 2, hash: "8f4af1d0c75c" },
    { mime: "image/svg+xml", url: "rendered/color-tube-constraints-3.svg", blockIndex: 3, hash: "5d19e432fe21" },
  ],

});
