import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-calibration-inputs",
  proofs: ["prf:three-calibration-inputs"],
  title:
    "Exactly three calibration inputs ($m_e$, $m_\\mu/m_e$, $\\mathfrak{Q}_\\beta(n)$), aligned to the three Wedderburn channels of $H_3(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.three_calibration_inputs",
    validation: "not_checked",
  },
  cites: ["codata2022"],
  tags: [
    "calibration",
    "three-parameters",
    "mass-scale",
    "energy-scale",
    "substrate-parameter",
    "wedderburn",
    "cohomology",
    "no-fitting",
    "predictive-content",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-05-25",
      body: "**Structural-vs-empirical conflation.** The proposition correctly identifies the 3 cohomological degrees of freedom of $H_3(R, q)$ surviving the on-shell + gauge + observability quotient. The step from *\"3 cohomological degrees\"* to *\"3 external calibration inputs\"* is an independent choice, not forced by the categorical structure. Three stances are math-consistent: **(a)** 3 calibrations + 0 derivations [current paper position], **(b)** 1 unit choice + 2 cohomological derivations [research path], **(c)** 0 calibrations + 3 derivations [the ideal — requires substrate-$q_0$ derivation declined 2026-05-08, **reopened 2026-05-25**, plus the cohomological $\\mathrm{Vol}(4_1)/\\hbar_q^2$ identity for CAL-2 and Khovanov-Rozansky closure for CAL-3]. The forbidden-4th-CAL clause is preserved; this caveat does NOT propose a 4th input — it clarifies the epistemic status of the existing three. See [`rem:epistemic-status-of-calibrations`](../observations/epistemic-status-of-calibrations.md) + [`2026-05-25-cal-2-cohomological-vs-calibration-critique.md`](../../../docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md).",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
  ],
});
