import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-aj-machinery-identification-details",
  title:
    "$\\Phi_q$/AJ identification — full AJ statement, significance, and Lean structure",
  interprets: "prop:phi-q-aj-machinery-identification",
  uses: [
    "prop:phi-q-aj-machinery-identification",
  ],
  tags: [
    "aj-conjecture",
    "faddeev-dilogarithm",
    "rogers-dilogarithm",
    "quantum-a-polynomial",
    "stochastic-mechanics",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\n[`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a conditional proposition. The backbone is proved unconditionally: the $q$-Weyl relation, closure of the solution space under linear combinations, and disjointness of the saddle regimes. The conjectural class inputs carry the AJ conjecture's content and the Faddeev/Rogers identifications.\n\nThe classes encode literature statements." },
  ],
});
