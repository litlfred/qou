import { remark } from "../../schema/builders";

/**
 * Gröbner–Shirshov reduction methods and optimizations.
 */
export const groebnerMethods = remark({
  label: "rem:groebner-reduction-methods",
  title: "Gröbner--Shirshov reduction: methods and reproducibility",
  interprets: "def:atomic-braid",
  uses: ["nuclear-groebner-reduction", "inductive-gb-reduction"],
  tags: ["computational"],
});
