import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:color-elliptic",
  label: "rem:color-tube-cubic",
  title: "Color tube cubic",
  uses: ["prop:color-elliptic", "def:color-tube-coordinates"],

  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-tube-cubic-0.svg", blockIndex: 0, hash: "6fa069be7f96" },
    { mime: "image/svg+xml", url: "rendered/color-tube-cubic-1.svg", blockIndex: 1, hash: "1151740223ee" },
  ],

});
