import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ns-singularity-descartes",
  lean: { ref: "qou:QOU.FluidDynamics.descartes_kummer_root_levels", validation: "not_checked" },
  title:
    "Topology of the Reeb bundle of the Descartes universe",
  // `prop:ns-kummer-specialisation` removed 2026-08-15 to break an editorial
  // cycle: it lists this theorem in its own `uses[]`, and its narrative links
  // here while this one never links there. The dependency runs
  // specialisation -> theorem, not both ways.
  uses: [
    "thm:qu-to-qou",
  ],
  tags: [
    "theorem",
    "navier-stokes",
    "descartes",
    "categorical",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-10-12",
      body: "Restated by owner decision (option B). The theorem previously asserted that the Descartes universe is NS-singular, NS(A) = e(ξ)|_Σ ≠ 0. That claim is not supported: Σ is one-dimensional, so H²(Σ, ·) = 0, and the non-cancellation step relied on the retracted jet-tower form of thm:qu-to-qou item 3. The statement now records only the true topological facts. The label is kept so existing cross-references resolve; its name is historical. The old argument is preserved, marked retracted, in prf:ns-singularity-descartes. Audit: docs/audits/2026-10-12-ns-chain-after-item3-retraction.md. Rescue exploration: bean qou-ocof.",
      see: "prf:ns-singularity-descartes",
    },
  ],
});
