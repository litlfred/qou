import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-harmonic-flow",
  title:
    "The substrate field $q(p)$ evolves by the $q$-harmonic-map heat flow $\\partial_t q = -\\Delta_q q$",
  uses: [
    "prop:germ-commutator-q-curvature",
    "prop:q-gaussian-solves-q-heat",
    "def:q-flat-connection",
  ],
  lean: {
    ref: "qou:QOU.LocalQ.QHarmonicFlow",
  },
  tags: [
    "substrate-parameter",
    "q-connection",
    "q-heat",
    "local-substrate",
    "evolution-law",
    "ansatz",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-16",
      body: "Route 2b / Step 3 of the local-q programme (docs/scope/2026-06-16-local-q-evolution-routes.md). The dynamical complement to Route 2a (prop:germ-commutator-q-curvature, kinematic). PDE is an ANSATZ, not derived: prop:q-gaussian-solves-q-heat governs diffusion at fixed q; promoting q itself to the diffusing field is the new postulate — hence kind=conjecture. Lean class QHarmonicFlow axiomatises the flow law; the instance is the conjecture, and stationary_iff_qharmonic + vacuum_stationary are verified sorry-free conditional on the class (§3b conditional-class pattern). The q0-selection reading (Route 1) stays out of scope: every constant field is stationary, so the naive 'q0 is the unique fixed point' is false (selection needs an extra equation). Not wired to production.",
    },
  ],
});
