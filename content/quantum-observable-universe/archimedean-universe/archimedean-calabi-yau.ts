import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:descartes",
  label: "rem:archimedean-calabi-yau",
  title: "The Archimedean condition on examples",
  tags: ["descartes-universe", "calabi-yau", "ale", "affine"],
  uses: [
    "ex:calabi-yau",
    "ex:ale",
  ],
});
