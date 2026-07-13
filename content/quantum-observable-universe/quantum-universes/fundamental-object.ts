import { definition } from "../../schema/builders";

export default definition({
  label: "def:fundamental-object",
  title: "Fundamental object",
  lean: { ref: "qou:QOU.FundamentalObject", validation: "not_checked" },
  uses: ["def:rigid-monoidal-category"],
  cites: ["deligne1990"],
  tags: [
    "category-theory",
    "fundamental-object",
    "self-dual",
    "tannaka-krein",
  ],
});
