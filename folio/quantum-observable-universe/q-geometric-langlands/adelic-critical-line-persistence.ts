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
    {
      kind: "caveat",
      date: "2026-11-28",
      body: "q-RH cleanup (owner thread 2026-11-28). (1) Bring's local spectra assemble into zeta(s)zeta(s-1)/L(E,s)^4 with E = 50a1, so they feed L(E,s), not zeta(s). (2) The class's hypothesis is an arbitrary family not tied to riemannZeta, so on any aligned family an instance IS RH. Whether to restate the conjecture for L(E,s) is the owner's call (decision card in the q-RH thread).",
    },
    {
      kind: "note",
      date: "2026-11-28",
      body: "Restated for L(E,s), E = 50a1, on the owner's card tap 02:44Z ('Restate for L(E,s), keep zeta as backup'). Lean carrier: QOU/Transcendental/BringsSurface/AdelicPersistenceL.lean (L50a1Datum, RiemannHypothesis50a1, AdelicCriticalLinePersistenceL; no instance). The zeta form QOU.BraidKnot.AdelicCriticalLinePersistence is kept as a labelled backup.",
    },
  ],
  label: "conj:adelic-critical-line-persistence",
  title: "Adelic persistence of the critical line",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.AdelicCriticalLinePersistenceL",
    validation: "stub",
  },
  uses: [
    "cor:spectral-half-line",
    "def:classical-riemann-zeta",
    "def:adelic-base-ring",
  ],
  tags: [
    "riemann-hypothesis",
    "critical-line",
    "adelic-assembly",
    "local-to-global",
    "millennium-problem",
  ],
});
