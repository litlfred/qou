import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:poincare-lefschetz-borromean",
  title:
    "Poincaré–Lefschetz duality on Borromean complement — cohomology ↔ homology of manifold-with-cusps",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PoincareLefschetzBorromean",
    validation: "not_checked",
  },
  uses: [
    "conj:borromean-bloch-group-element",
    "prop:reeb-bundle-complement-equals-volume",
  ],
  cites: [
    "lefschetz1926",
    "neumann-zagier1985",
  ],
  tags: [
    "tier:S",
    "poincare-lefschetz",
    "duality-d21",
    "borromean-complement",
    "manifold-with-cusps",
    "cohomology-homology",
    "axiom-class",
    "open-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): 1. Verify that the Borromean volume $8G$ arises as a Poincaré–\n   Lefschetz pairing in Lean — partial Mathlib infrastructure\n   exists (Mathlib's `Topology.Manifold` library).\n\n3. Closing the conjecture needs a Lean class for manifold-with-cusps\n   Poincaré–Lefschetz (partial in Mathlib)." },
  ],
});
