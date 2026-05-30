import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:chirality-ribbon-frobenius",
  lean: { ref: "qou:QOU.BraidKnot.ChiralityRibbonFrobenius" },
  title:
    "Exact chirality factor from Frobenius ribbon twist: $a_K = \\sum_\\lambda w_\\lambda q^{2w(K)c(\\lambda)}\\chi_\\lambda / \\sum_\\lambda w_\\lambda \\chi_\\lambda$",
  uses: [
    "prop:chirality-writhe-ribbon-derivation",
    "prop:alpha-k-derivation-procedure",
  ],
  tags: [
    "chirality",
    "ribbon-twist",
    "frobenius",
    "writhe",
    "kauffman",
    "gap-a",
    "audit",
  ],
  authorNotes: [
    {
      kind: "status",
      body:
        "**Refuted at the audited atomic braids.** The conjecture *as originally stated* has been falsified for $D, T, {}^3\\mathrm{He}$ — see the *refutation status note* (also in authorNotes) and the 'Generalisation' subsection. The statement is preserved as the historical conjecture text; the empirical $(1+h)(1-h) \\approx 0.956$ pattern that motivated it requires a different construction (see the *Residual* paragraph in the block).",
    },
    {
      kind: "status",
      date: "2026-05-09",
      body:
        "**Refutation pending reconciliation.** Direct numerical evaluation of the ratio above for the audited atomic braids D ($H_6$), T ($H_9$), $^3$He ($H_9$) at $q_0$ — see `chirality-avg-content-atomic.witness.json` and the 'Generalisation' subsection below — finds the exact ratio diverges by $\\sim 10^4$ (T) and $\\sim 10^4$ (${}^3$He) from the empirical $(1+h)(1-h) \\approx 0.956$ pattern, and the first-order linearisation does not match either. The conjecture **Statement** above is therefore **scoped as historical/aspirational** for the audited atomic braids until reconciled. Current best understanding: the chirality factor for atomic braids is *not* the ribbon-twist Markov-trace ratio above in its stated form; an alternate construction is needed (see 'Implications' / 'Residual' at the end of the **Generalisation** section). The Hecke-character invariants $\\langle c \\rangle_\\beta$ from this conjecture are still well-defined and witnessed; only the specific way they feed into $a_K$ is in question.",
    },
  ],
});
