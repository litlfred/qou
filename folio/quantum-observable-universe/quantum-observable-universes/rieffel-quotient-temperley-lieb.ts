import { example } from "../../schema/builders";

export default example({
  label: "ex:rieffel-quotient-temperley-lieb",
  title:
    "Temperley--Lieb trace-radical quotient on two-dimensional strands",
  interprets: "def:categorical-dirac-operator",
  lean: {
    ref: "qou:BraidKnotOctonion.JimboKernelGeneric.traceQuotTLEquivComplex",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-dirac-operator",
    "rem:rieffel-metric-quotient-faithfulness",
    "ex:quantum-universe-su2",
  ],
  cites: [
    "jimbo1986",
    "temperley-lieb1971",
    "rieffel1999",
  ],
  tags: [
    "su2",
    "temperley-lieb",
    "radical",
    "quantum-metric",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Wires `QOU.SchurWeyl.JimboKernelGeneric.traceQuotTLEquivComplex` " +
        "(`ker_jimbo_eq_traceRadicalIdeal_complex`, `tlRep_injective`, " +
        "`finrank_tl_eq_catalan_complex`) directly into Chapter 2 alongside " +
        "`rem:rieffel-metric-quotient-faithfulness` (bean qou-wywz).",
    },
  ],
});
