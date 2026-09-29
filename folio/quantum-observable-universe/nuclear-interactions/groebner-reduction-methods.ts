import { remark } from "../../schema/builders";

/**
 * Gröbner-Shirshov reduction methods and optimizations.
 */
export default remark({
  label: "rem:groebner-reduction-methods",
  title: "Gröbner--Shirshov reduction: methods and reproducibility",
  interprets: "def:atomic-braid",
  uses: ["prop:inductive-gb-reduction"],
  tags: ["computational"],
});
