import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pn-averaging-uniqueness",
  title: "Bar-invariant p-n interface averagings",
  cites: ["jones1987", "wenzl1988"],
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness"],
  lean: { ref: "qou:QOU.BraidKnot.pn_averaging_unique" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the five statements are `pnZD_inv`, `pn_averaging_bar_iff`, `pn_averaging_unique`, `pn_averaging_uniform_bar`, `pn_averaging_unique_via_weight`, all sorry-free.",
    },
    {
      kind: "caveat",
      date: "2026-11-15",
      body: "The statement used to assume (c) σ_pn = z and conclude that the canonical averaging is unique. The Lean proof was a rewrite by that hypothesis, so the uniqueness was the hypothesis. Under convention D, z is not bar-invariant (z̄ = z − h), so (a) and (c) could not both hold and the theorem was vacuous. Restated as the bar-invariance criterion for z − c·h, with uniqueness only among constant c. No number moves.",
    },
    {
      kind: "caveat",
      body: "An earlier version of the scope paragraph stated that both candidates satisfy bar-invariance — a conditional hypothesis reported as a settled fact. Only the uniform form does; verified exactly in computations/probes/pn_interface_bar_structure_probe.py.",
    },
    {
      kind: "note",
      date: "2026-05-30",
      body: "The closed-form-weight derivation chain was established 2026-05-30.",
    },
  ],
});
