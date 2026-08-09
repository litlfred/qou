import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-apply-transfer",
  title:
    "Bar-transfer principle: one-sided bounds on bar-invariant properties extend for free",
  tags: [
    "bar-involution",
    "skew-symmetry",
    "transfer-principle",
    "stability-margin",
    "proof-reuse",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BarApplyTransfer.bar_apply_transfer",
    validation: "not_checked",
  },
  uses: ["prop:bar-t-duality-substrate"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**Archimedean specialisation (AGENTS.md §7c) — why, specifically.** " +
        "The block `.md` carries the standard archimedean banner; this note " +
        "records the file-specific reason, because the generic banner's list " +
        "(real-valued observables, transcendental constants, numerical " +
        "evaluation at q₀) does **not** apply here. The actual reason is the " +
        "**ordering**: the statement quantifies over the ordered ray " +
        "$\\mathbb{R}_{>0}$ (`0 < q`, `a < q`, `q < a⁻¹`) and the proof turns " +
        "on inversion reversing that order (`inv_pos`, `lt_inv_comm₀`, " +
        "`inv_lt_inv₀`). Per §7c an ordering predicate puts a declaration on " +
        "the archimedean side, so the `ℝ` here is essential and the `q⁻¹` " +
        "occurrences are genuine ordered-field inverses, not Laurent " +
        "`↑q⁻¹` unit coercions. There is no generic-`CommRing` content to " +
        "split out: the bar involution as an **automorphism of** " +
        "$\\mathbb{Z}[q, q^{-1}]$ is a different object, formalised " +
        "elsewhere; this block is only the order-transfer principle on the " +
        "positive real ray.",
    },
  ],
});
