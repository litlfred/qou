import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:sqrt-q-ribbon-structure",
  label: "rem:sign-as-spin-structure",
  title: "The sign of $\\sqrt{q}$ as a spin structure",
  tags: [
    "ribbon",
    "twist",
    "sqrt-q",
    "spin-structure",
    "framing",
    "post-archimedean",
  ],
  uses: [
    "rem:sqrt-q-ribbon-structure",
    "rem:braiding-unit-circle-convention",
  ],
});
