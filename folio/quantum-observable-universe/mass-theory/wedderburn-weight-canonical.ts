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
  computation: {
    engine: "python",
    script:
      "computations/_deprecated/bw_wenzl_shadow_equivalence.py",
    witness: "docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json",
    status: "verified",
  },
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
  ],
});
