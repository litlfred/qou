import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:r-matrix-braiding",
  label: "rem:skein-archimedean-shadow",
  title: "Skein relations as an archimedean shadow",
  tags: ["skein-relations", "jones-polynomial", "r-matrix"],
  uses: [
    "rem:r-matrix-braiding",
    "prop:braid-action-tensor",
  ],
});
