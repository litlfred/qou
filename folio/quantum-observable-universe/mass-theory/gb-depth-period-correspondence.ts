import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gb-depth-period-correspondence",
  title:
    "GS-depth $\\leftrightarrow$ Goncharov period-depth correspondence",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence",
    validation: "not_checked",
  },
  uses: [
    "prop:q-dilogarithm-exists",
    "prop:categorical-laplace-unique",
    "def:q-resolvent",
    "lem:surreal-squeeze",
    "rem:figure-8-archimedean-illustration",
    "rem:algebraic-core-survives",
  ],
  cites: [
    "kontsevich1995",
    "deligne-goncharov2005",
    "zagier1986",
    "bloch2000",
    "suslin1991",
    "neumann-zagier1985",
  ],
  tags: [
    "tier:keystone",
    "graded-mikusinski",
    "goncharov-periods",
    "archimedean-wall",
    "iterated-integral-depth",
    "surreal-envelope",
    "wall-crossing-criterion",
    "open-problem",
    "keystone",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the max-hook statistic is `QOU.BraidKnot.gbDepth`, a definition" },
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**The object called $\\mathcal{H}_q$ here is not the Frobenius–Hopf " +
        "substrate.** Grouplikes ($\\Delta g = g \\otimes g$, " +
        "$\\varepsilon(g) = 1$) need a bialgebra. The substrate's $\\Delta$ is the " +
        "Frobenius comultiplication, and the corpus excludes both unit-side " +
        "bimonoid axioms for a non-trivial substrate " +
        "(`FrobeniusBialgebraCollapse.not_one_comul_of_nontrivial`) and a " +
        "multiplicative counit outright " +
        "(`MultiplicativeCounitCollapse.eq_counit_smul_one`, bean `qou-aj49`). " +
        "The conjecture needs a Hopf algebra with a **different** comultiplication; " +
        "which one is not fixed here. The link to `def:frobenius-hopf-substrate` " +
        "is kept as provenance only.",
    },
  ],
});
