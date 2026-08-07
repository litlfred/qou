import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:knot-factor-amphicheiral",
  title:
    "Knot factor for Markov-amphicheiral knots: sum of positive squares",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_factor_amphicheiral",
    validation: "not_checked",
  },
  uses: ["prop:knot-factor-spectral-form"],
  tags: [
    "knot-factor",
    "amphicheiral",
    "figure-eight",
    "alternating-block",
    "tritium",
    "helium-3",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/knot_factor_amphicheiral_BD_probe.py",
    witness: "computations/probes/knot-factor-amphicheiral-BD-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`altRatio` and the knot factor `a` are typed over `ℝ` because " +
        "they are Plancherel-weighted character *ratios* evaluated at the " +
        "substrate anchor, inherited from `HeckeExpansion` in " +
        "`KnotFactorSpectralDerivation` (whose `c`, `weight` and " +
        "`trivial` fields are `List ℕ → ℝ`).",
    },
  ],
});
