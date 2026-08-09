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
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**§7c base ring — the `ℝ` is gone; superseded 2026-08-09.** The " +
        "2026-08-07 note recorded that `altRatio` and the knot factor `a` " +
        "were typed over `ℝ` *inherited from* `HeckeExpansion` in " +
        "`KnotFactorSpectralDerivation`. That root cause has now been " +
        "removed rather than documented: `HeckeExpansion` is generic over " +
        "its Hecke base ring `{R : Type*} [Field R]`, so `Amphicheiral`, " +
        "`altRatio` and `knot_factor_amphicheiral` are too. Nothing in " +
        "either file uses an ordering, `Real.*`, or any archimedean input, " +
        "so no specialisation remains to acknowledge. A field (not a " +
        "`CommRing`) is still required: the pairing is normalised by " +
        "$\\chi_\\lambda(\\mathbf{1})^2 = (\\dim_q V_\\lambda)^2$, which is " +
        "a Laurent polynomial in $q$ and not a unit of " +
        "$\\mathbb{Z}[q^{\\pm 1}]$, so the quotient lands in the fraction " +
        "field $\\mathbb{Q}(q)$ — matching the narrative's *\"holds exactly " +
        "in $R$\"*. $R := \\mathbb{R}$ remains an instance for archimedean " +
        "evaluation at the substrate anchor.",
    },
  ],
});
