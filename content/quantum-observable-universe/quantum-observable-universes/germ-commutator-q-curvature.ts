import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:germ-commutator-q-curvature",
  title:
    "Germ-commutator of two observations equals the $q$-curvature on the loop",
  uses: ["def:observation"],
  lean: {
    ref: "qou:QOU.LocalQ.ObservationParallelogram.commutator_eq_curvature",
  },
  tags: [
    "observation",
    "q-connection",
    "curvature",
    "local-substrate",
    "substrate-parameter",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-16",
      body: "Route 2a of the local-q programme (docs/scope/2026-06-16-local-q-evolution-routes.md): promotes the two-observer-parallelogram δq(p) to the q-curvature 2-form. Lean is self-contained over an abstract non-commutative ring, build-verified sorry-free (v4.24.0) via lean-direct against the restored lake-cache oleans. The identity [δq₁,δq₂]=F_q is unconditional; the identification of F_q with the q-flat-connection's intrinsic (q−1)𝓕_q^intr is narrative (keeps this proposition out of the conjectural cone).",
    },
  ],
});
