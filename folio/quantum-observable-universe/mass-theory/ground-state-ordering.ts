import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ground-state-ordering",
  lean: { ref: "qou:QOU.MassTheory.GroundStateOrderingRefutation.prescribed_not_minimiser_A5", validation: "leanok" },
  title: "The interleaved ordering does not minimise the dilogarithm volume",
  uses: ["def:typed-crossing-operator"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Refuted and restated (bean `qou-48is`, PR #4855).** This block " +
        "previously asserted that the interleaved + tail-packed arrangement " +
        "*minimises* `\\Phi_q` for `A >= 4`, with sorted winning for `A <= 3`. " +
        "An exhaustive sweep over every `C(A,Z)` arrangement for `A <= 16` at " +
        "the experimental (proton) anchor refutes the `A >= 4` clause (argmin " +
        "in 17/62 cases on the bare chain, strict argmax in 12/62), and the " +
        "`A <= 3` clause fails as stated at `A = 2` (exact tie on the bare " +
        "chain; sorted strictly worse with the electron tail). The `A = 3` " +
        "case holds. The counterexample at `A = 5, Z = 1` is Lean-proved " +
        "sorry-free for an interval of `q` containing the anchor. " +
        "Audit: `docs/audits/2026-08-09-ground-state-ordering-truth-value.md`. " +
        "No production behaviour was changed and no published number moved; " +
        "which ordering the mass/binding computations should use remains open.",
      see: "docs/audits/2026-08-09-ground-state-ordering-truth-value.md",
    },
  ],
  tags: [
    "ground-state",
    "refuted",
    "transfer-matrix",
    "eigenvalue",
    "ordering",
    "nuclear",
    "shell-model",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/sigma_shell_from_beta_chain.py",
    witness: "computations/sigma-shell-from-beta-chain.witness.json",
    status: "verified",
  },
});
