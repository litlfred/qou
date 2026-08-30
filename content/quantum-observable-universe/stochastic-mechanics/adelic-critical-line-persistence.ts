import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-29",
      body: "Opened by bean `qou-qadl`. Before this block the adelic-assembly step of the q-RH arc was stated only as a subordinate clause in the prose of `conj:classical-riemann-hypothesis` and had no block, no conjecture and no Lean carrier. Primary conjecture per §3b-tax: its Lean class takes no other conjecture class as a hypothesis.",
    },
    {
      kind: "caveat",
      date: "2026-08-29",
      body: "Vacuity hazard on the Lean class: it is an implication, so an instance on a family that is NOT critical-line aligned is vacuously true and worth nothing. Content sits at families satisfying the antecedent. An instance is an advance only with a witness family; none is provided, which is the honest open state.",
    },
  ],
  label: "conj:adelic-critical-line-persistence",
  title: "Adelic persistence of the critical line",
  lean: {
    ref: "qou:QOU.BraidKnot.AdelicCriticalLinePersistence",
    validation: "stub",
  },
  uses: [
    "cor:spectral-half-line",
    "def:classical-riemann-zeta",
    "def:adelic-substrate",
  ],
  tags: [
    "riemann-hypothesis",
    "critical-line",
    "adelic-assembly",
    "local-to-global",
    "millennium-problem",
  ],
});
