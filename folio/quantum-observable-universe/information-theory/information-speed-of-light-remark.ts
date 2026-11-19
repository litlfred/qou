import { remark } from "../../schema/builders";

export default remark({
  label: "rem:information-speed-of-light-remark",
  title: "The speed of light as a Lieb--Robinson velocity",
  interprets: "def:information-speed-of-light",
  tags: ["definition-commentary"],
  uses: [
    "def:information-speed-of-light",
    "rem:light-cone-affine",
    "def:contact-affine-chart",
  ],
});
