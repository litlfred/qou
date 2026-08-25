import { remark } from "../../schema/builders";

/**
 * Contrast between the full typed Garside element and the
 * adjacent-only transfer-matrix chain: same pairwise crossing data,
 * but the Garside element retains the complete $H_A(q)$ structure.
 */
export default remark({
  label: "rem:typed-garside-element-adjacent-comparison",
  title: "Comparison with the adjacent-only construction",
  interprets: "def:typed-garside-element",
  uses: ["def:typed-garside-element"],
  tags: [
    "garside-element",
    "transfer-matrix",
    "hecke-algebra",
    "comparison",
  ],
});
