import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:binding-scale-catalan",
  title: "Binding energy scale $\\alpha = m_e \\times 8G$",
  lean: { ref: "qou:QOU.BindingScale.bindingScale_value",
    validation: "not_checked",
  },
  uses: ["def:borromean-baryon"],
  computation: {
    engine: "python",
    script: "computations/catalan_binding.py",
    witness: "computations/catalan-binding.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-27",
      body:
        "The analytic backing of the `8G` scale is upgraded: the Borromean " +
        "volume-conjecture instance `(2π/N)·log⟨𝓑₃⟩_N → 8·Cl₂(π/2) = 8G` " +
        "is machine-proved sorry-free in-repo " +
        "(`QOU.Knot.FigureEightVolume.tendsto_log_borromeanKashaev_vol`, " +
        "`BorromeanVolume.lean`, PR #4381) — previously a van der Veen " +
        "literature citation. The Catalan value itself carries certified " +
        "rational bounds (`CatalanValueBounds.lean`: |G − rational| ≤ 1/24, " +
        "|Vol_Borromean − 7.3277247534| < 2/5). The identification of the " +
        "positive-sum carrier with the diagrammatic invariant remains the " +
        "cited Habiro/GL2011 input, per the carrier file's epistemic-status " +
        "header.",
    },
  ],
});
