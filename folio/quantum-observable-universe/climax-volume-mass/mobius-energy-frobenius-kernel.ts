import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:mobius-energy-frobenius-kernel",
  lean: { ref: "qou:QOU.BraidsKnots.mobius_frobenius_kernel",
    validation: "not_checked",
  },
  title: "Classical limit of the Frobenius--Hopf kernel is the repulsive $1/r^2$",
  tags: ["frobenius-pairing", "mobius-energy", "classical-limit", "killing-form"],
  uses: ["def:frobenius-pairing"],
  proofs: ["prf:mobius-energy-frobenius-kernel"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean` uses " +
        "`Filter.Tendsto`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Lean scope (disclosure, not a change of claim).** The `lean.ref` theorem `mobius_frobenius_kernel` composes the two fields of `MobiusFrobeniusKernelContext`: `kernel_tendsto_killing` (the q → 1 limit of the kernel is the Killing kernel) and `killing_eq_inverse_square` (the Killing kernel is 1/‖γ(s) − γ(t)‖²). Both halves of the lemma's content are assumed as class fields; the theorem derives nothing beyond chaining them (AGENTS.md §3b-cond item 5). The only instance in the file, `inverseSquareContext`, sets the kernel equal to 1/|s − t|² at every q, so the limit is constant. The narrative proof restates the limit and does not derive a 1/r² dependence from a distance-independent Killing form. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B04; bean qou-n3xv).",
    },
  ],
});
