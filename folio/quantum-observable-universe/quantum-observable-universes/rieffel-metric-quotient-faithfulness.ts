import { remark } from "../../schema/builders";

export default remark({
  label: "rem:rieffel-metric-quotient-faithfulness",
  title:
    "Rieffel Lipschitz seminorms, trace-radical descent, and quotient metric faithfulness",
  interprets: "def:categorical-dirac-operator",
  lean: {
    ref: "qou:QOU.InformationTheory.FiniteRieffelQuantumMetric.isDualBound_zero_iff_eq",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-dirac-operator",
    "def:quantum-observable-universe",
    "def:substrate-parameter",
  ],
  cites: [
    "connes1989",
    "connes1994",
    "rieffel1999",
    "rieffel2004",
    "kantorovich1942",
    "rubinstein1957",
    "gelfand-naimark1943",
    "segal1947",
  ],
  tags: [
    "dirac",
    "connes-distance",
    "quantum-metric",
    "radical",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Stop 2 of the three-stop Leibniz relational spine (bean qou-wywz). " +
        "Formalised over any strictly ordered field `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` " +
        "(zero `ℝ`) in `QOU.InformationTheory.FiniteRieffelQuantumMetric`: " +
        "`isDualBound_zero_iff_eq`, `finite_dualBound_eq_on_traceRadical`, " +
        "`unbounded_of_nonscalar_kernel`, `hasScalarKernel_of_state_bounded`, " +
        "`kantorovich_primal_ge_dual`, and `dirac_convex_weights`.",
    },
  ],
});
