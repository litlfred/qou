import { remark } from "../../schema/builders";

export default remark({
  label: "rem:polynomial-observable-subcategory-remark",
  title: "The polynomial observable subcategory as a computational analogue",
  interprets: "def:polynomial-observable-subcategory",
  tags: ["definition-commentary"],
  uses: [
    "def:polynomial-observable-subcategory",
    "def:observable-subcategory",
  ],
});
