import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "The Lean proves the iff by composing two hypotheses, one per direction, so the whole content is carried by `p_to_bandwidth` and `bandwidth_to_p` (round-trip audit pass 2, C07). Membership in P is a property of a family of instances, not of one link $L$; the statement needs restating over a family $(L_N)$ with $c(N) = 3N$. The Planck-step cost is a physical comparison, not part of the mathematics." },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's `ℝ` sit on " +
        "`informationBandwidth (q : ℝ) (η_q : ℝ) : ℝ := q * η_q / (q - 1)^2` " +
        "and the `PBandwidthContext` fields `q`, `η_q`. `𝓑(q)` is a **physical " +
        "rate** — bits per Planck time — and the proposition's claim is the " +
        "bound `t(c) ≤ 𝓑(q)⁻¹ · poly(c)` on a **count of Planck steps**. Both " +
        "the quantity and the comparison are archimedean by meaning (§7c: a " +
        "measured value or time parameter is `ℝ`), so the specialisation is " +
        "deliberate. The underlying Skein polynomial `P_L(q)` stays generic; " +
        "only its evaluation budget is measured in `ℝ`.",
    },
  ],
  label: "prop:p-bandwidth-bound",
  lean: { ref: "qou:QOU.Information.p_bandwidth_bound", validation: "not_checked" },
  title: "Polynomial computation as sub-horizon bandwidth",
  tags: [
    "P-class",
    "bandwidth",
    "information-flow",
    "planck-step",
    "complexity",
    "polynomial-time",
  ],
  uses: ["def:computational-horizon"],
});
