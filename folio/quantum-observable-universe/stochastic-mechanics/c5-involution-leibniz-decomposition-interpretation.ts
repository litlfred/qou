import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:c5-involution-leibniz-decomposition",
  label: "rem:c5-involution-leibniz-decomposition-interpretation",
  title:
    "Bar-symmetry class, the two categorical sectors of $c_k$, and the $c_5$ falsifiable prediction",
  uses: [
    "prop:c5-involution-leibniz-decomposition",
    "def:bar-involution",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Lean sibling proves b^2 = 1 - 1/[2]_q^2 and `c5_classical_limit_eq_neg_five_quarters`; symbolic pentagon reduction in `computations/pentagon_reduction_li2q.py`.",
    },
  ],
});
