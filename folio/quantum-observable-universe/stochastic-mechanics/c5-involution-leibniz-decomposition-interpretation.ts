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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Hoefsmit-Quantum-2 identity $b^2 = 1 - 1/[2]_q^2$ is a proved algebraic theorem in the Lean sibling. The \"$-1/2$\" piece is a q-independent commutative-QOU constant; $c_5(q=1) = -5/4$ proved as `c5_classical_limit_eq_neg_five_quarters`.\n\n> **Pentagon-reduction cross-link.** The Leibniz expansion uses the q-dilogarithm pentagon identity implicitly. The algebraic identity making this rigorous lives in [`pentagon_reduction_li2q.py`](../../../computations/pentagon_reduction_li2q.py). The Pentagon coherence layer of $c_5$'s decomposition is what `pentagon_reduction_li2q.py` makes algebraic." },
  ],
});
