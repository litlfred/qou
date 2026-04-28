import { definition } from "../../schema/builders";

export default definition({
  label: "def:observable-subcategory",
  title: "Observable subcategory $\\mathrm{Bun}^{\\circ}(\\mathbb{P}(V))$",
  tags: [
    "observable-subcategory", "bundle-category",
    "degree-zero", "frobenius-pairing",
  ],
  lean: { ref: "qou:QOU.ObservableSubcategory",
    validation: "not_checked",
  },
  uses: [
    "rem:bundle-category",
    "def:jet-horizon",
    "def:observation",
  ],
});
