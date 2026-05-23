import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:descartes",
  label: "rem:archimedean-calabi-yau",
  title: "The Descartes condition on examples",
  tags: ["archimedean-universe", "calabi-yau", "ale", "affine"],
  uses: [
    "ex:calabi-yau",
    "ex:ale",
  ],
});
