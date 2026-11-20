import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dilog-pentagon-is-associator",
  title: "The pentagon coherence is equivalent to being a $q$-dilogarithm",
  lean: {
    ref: "qou:QOU.QuantumObservableUniverses.DilogPentagonAssociator.pentagon_iff_isDilog",
    validation: "not_checked",
  },
  uses: ["def:q-dilogarithm", "prop:q-dilogarithm-exists"],
  cites: ["faddeev_kashaev1994"],
  tags: ["dilogarithm", "pentagon-identity", "associator", "monoidal"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 2): [`QOU.QuantumObservableUniverses.DilogPentagonAssociator.pentagon_iff_isDilog`](../lean/QOU/QuantumObservableUniverses/DilogPentagonAssociator.lean) proves the biconditional over a generic carrier (`[Add H]`). The forward direction packages the witness; the reverse reads the datum's five-term field. The cochain guise is `QOU.BringsSurface.PentagonTwist.assoc_pentagon`." },
    { kind: "status", date: "2026-10-11", body: "Formalisation status relocated from the block prose by the paper-voice commentary audit: `PentagonTwist.assoc_pentagon` is sorry-free; `DilogPentagonAssociator.pentagon_iff_isDilog` is sorry-free and axiom-free (`#print axioms` reports no dependency), a genuine equivalence rather than a self-assuming projection. The categorical → scalar descent is not formalised, pending shuffle-Hopf infrastructure absent from Mathlib; the analytic q ≠ 1 five-term relation is carried by the conjecture class `QRogersAnalyticContinuation`." },
  ],
});
