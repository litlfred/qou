import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-operator-basis-table",
  title: "Knot operator action on NF basis pairs (symbolic in $q$)",
  tags: [
    "hecke",
    "knot-operator",
    "normal-form",
    "appendix",
    "pair-production",
    "frobenius-dual",
  ],
  uses: [
    "rem:hecke-operations",
    "prop:frobenius-gram-matrix",
  ],
  interprets: "prop:knot-operator-selection",
  computation: {
    engine: "python",
    script: "computations/photon_operator_table.py",
    witness: "computations/photon-operator-table.witness.json",
    status: "verified",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Owner ruling 2026-11-21 (docs/coordination/owner-rulings.md): the electron is σ₀σ₁σ₀ ∈ B₃, whose closure is the Hopf link. Operators relabelled to match the closures of their words: T_{2,3} → T_{2,2}^{(3)} for σ₀σ₁σ₀ (Hopf link) and T_{2,5} → T_{2,4}^{(3)} for (σ₀σ₁)²σ₀ (the T(2,4) torus link, not the cinquefoil). Closures measured in docs/audits/2026-11-21-electron-word-gs-interactions.md §3.1 and §7; same keys as computations/photon_operator_table.py. No number changed: the braid words, and so every table entry and pair count, are the ones the witness already records. Backup under the ruling (not used in this remark): the trefoil σ₀³ ∈ B₂, which is h times a single photon (QOU/BraidKnot/ElectronWordCandidates.lean, cube_eq_smul_photon)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness**: `knot-operator-table.witness.json`. (second occurrence, after the photon-photon discussion: **Witness**: `knot-operator-table.witness.json`, `gram-matrix-dual.witness.json`.)" },
  ],
});
