import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-weight-canonical",
  title:
    "Canonical q-deformed Wedderburn-block weight $\\tilde w_\\lambda$ and named scalings (BW, LP for all $\\lambda$)",
  tags: [
    "wedderburn",
    "weight",
    "canonical",
    "bw",
    "shadow-price",
    "wenzl-bridge",
    "self-conjugate",
    "consolidation",
  ],
  uses: [
    "prop:wedderburn-as-noncomm-fourier",
    "prop:plancherel-weight-boundedness",
  ],
  cites: ["jones1985", "wenzl1988", "kassel1995", "orellana1998"],
  lean: { ref: "qou:QOU.BraidKnot.wedderburnWeightCanonical" },
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-04",
      body:
        "**Wenzl-bridge field dropped (owner ruling, option A).** The class field `y_eq_self_conjugate` " +
        "($y_\\lambda = \\tilde w_\\lambda$ on $\\kappa_\\lambda = 0$) was measured false at every " +
        "self-conjugate partition with $n \\le 6$ except $(1)$, in both conventions (2026-09-02). It and its " +
        "projection theorem are removed; `y` stays as data only; the BW/LP scalings and " +
        "`beta_mul_h_eq_neg_C` are unchanged. The refutation record stays in the prose above.",
    },
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**`computation` field removed (owner, 2026-10-10).** It declared `status: \"verified\"` against " +
        "`bw_wenzl_shadow_equivalence.py`, a deprecated producer (now on the `cat/cat-harness/fsh-guts` branch) " +
        "whose check was the Wenzl-bridge field dropped above, so nothing remained for it to verify. The " +
        "witness `docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json` is kept as a historical record.",
    },
  ],
  computation: {
    engine: "sympy",
    script: "computations/delta_q_decoration.py",
    witness: [
      "computations/delta-q-decoration.witness.json",
      "computations/probes/y-lambda-cyclotomic-factorization-probe.witness.json",
      "computations/sigma-f-electron-shell-chain.witness.json",
      "computations/alpha-k-jones-markov-h4.witness.json",
      "computations/keystone-qdeform-projector-shift.witness.json",
      "computations/probes/binding-sum-c-vs-d-deut.witness.json",
    ],
    status: "verified",
  },
});
