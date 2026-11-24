import { prose } from "../../schema/builders";

export default prose({
  label: "sec:introduction-overview",
  meta: { position: "opening" },
  cites: [
    "wigner1960",
    "heisenberg1958",
    "leibniz-clarke1717",
    "earman1989",
    "gelfand-naimark1943",
    "segal1947",
    "rieffel1999",
    "barbour-bertotti1982",
    "rovelli1996",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Stop 1 of the three-stop Leibniz relational spine (bean qou-wywz). " +
        "The complex algebra isomorphism H_n(q)/rad(wtrace) ≃ₐ[ℂ] TL_n(q + q⁻¹) at generic " +
        "q ≠ 0 is proved in `QOU.SchurWeyl.JimboKernelGeneric.traceQuotTLEquivComplex` " +
        "(wired at `ex:rieffel-quotient-temperley-lieb`), and Rieffel's metric Identity of " +
        "Indiscernibles and trace-radical descent are proved in " +
        "`QOU.InformationTheory.FiniteRieffelQuantumMetric` (wired at " +
        "`rem:rieffel-metric-quotient-faithfulness`).",
    },
  ],
});
