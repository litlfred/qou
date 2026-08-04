import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-operator-selection",
  lean: { ref: "qou:QOU.ParticleInteractions.confinement_operator_selection", validation: "not_checked" },
  title: "Confinement operator selection via topological Brunnian minimality",
  tags: [
    "confinement",
    "borromean",
    "brunnian",
    "topological-selection",
    "frobenius-dual",
    "gram-matrix",
    "operator-selection",
    "beta-decay",
  ],
  uses: ["prop:frobenius-gram-matrix"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-06-17",
      body:
        "Selection principle corrected. The earlier framing — 𝓑₃ selected by a " +
        "minimum-action (minimum-eigenvalue) functional on the 6×6 Frobenius Gram " +
        "matrix — was refuted: NF(𝓑₃) is ≈99.8% the identity γ (the maximum-cost " +
        "channel), so any cost-minimising operator-space program selects the " +
        "smallest-cost mesonic L± instead (dense Wedderburn-projector SDP collapses " +
        "to the min-eigenvector of the cost operator; see " +
        "`computations/probes/b3_dense_sdp_wedderburn_projector.py` and " +
        "`docs/audits/2026-06-17-b3-dense-sdp-lever-closed.md`). The selection is " +
        "instead topological and input-free: 𝓑₃ is the crossing-minimal nontrivial " +
        "Brunnian three-braid (confinement = no quark subset isolable = Brunnian), " +
        "witnessed by `b3_brunnian_selection_scope.py` + " +
        "`b3_brunnian_minimality_enumeration.py`. The Gram/net data is now a " +
        "consistency check, not the selector. Scope: minimality among three-braid " +
        "closures (the 3-quark setting), not full link-theoretic uniqueness.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/confinement_operator_selection.py",
    witness: [
      "computations/confinement-operator-selection.witness.json",
    ],
    status: "experimental",
  },
});
