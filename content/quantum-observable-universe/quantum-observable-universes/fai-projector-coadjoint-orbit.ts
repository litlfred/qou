import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:fai-projector-coadjoint-orbit",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.fai_projector_coadjoint_orbit",
    validation: "not_checked",
  },
  title: "Rank-1 projectors embed $\\mathbb{P}(V)$ as a coadjoint orbit in $\\mathrm{Ad}(A)$",
  tags: ["rank-one-projector", "coadjoint-orbit", "involution", "categorical-trace"],
  uses: ["def:involutive-structure"],
  proofs: ["prf:fai-projector-coadjoint-orbit"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean` " +
        "imports `Mathlib.LinearAlgebra.Matrix.Spectrum` and its proof runs Mathlib's spectral theorem, which has no generic-`CommRing` counterpart. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
