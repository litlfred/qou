import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:qou-existence-probability",
  label: "rem:qou-axiom-codimensions",
  title: "Motivic codimension of each QOU axiom",
  uses: [
    "def:qou-existence-probability",
    "rem:axiom-independence",
  ],
  tags: ["motivic-integration", "axiom-filtration", "codimension"],
});
