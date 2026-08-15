import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). " +
        "The $\\mathbb{R}$ is inherited, not local: this proposition's uniqueness " +
        "hypothesis compares `QLocalSystem.holonomyResidue : M → ℝ`, and the Hecke " +
        "eigenvalue pair it identifies is `symmetric_eigenvalue := fun p => sp.field p` / " +
        "`antisymmetric_eigenvalue := fun p => -(sp.field p)⁻¹` — both valued in " +
        "$\\mathbb{R}$ because `QOU.SubstrateParameter.field : M → ℝ` carries the " +
        "*ordering* hypotheses `field_pos : 0 < q(p)` and `field_ge_one : 1 ≤ q(p)` " +
        "(the classicality bound), which §7c places on the archimedean side. The " +
        "argument itself is categorical — Tannakian rigidity via " +
        "`FibreFunctorRigidity.eigenvalue_unique` — and uses no ordering, so it would " +
        "restate verbatim over a generic `[CommRing R]` substrate section; only the " +
        "`SubstrateParameter` carrier blocks that. Moving this pre-archimedean means " +
        "splitting `SubstrateParameter` into a ring-generic core plus an ordered " +
        "extension, which is a separate refactor with a wide blast radius (it is " +
        "`extend`ed by `QuantumGaugeGroup` and imported across the QOU tree).",
    },
  ],
  label: "prop:q-hecke-eigenvalue",
  lean: { ref: "qou:QOU.q_hecke_eigenvalue", validation: "not_checked" },
  title: "$q$-Hecke eigenvalues from the fibre functor",
  uses: [
    "def:q-hecke-eigensheaf",
    "rem:fibre-functor-rigidity",
  ],
  proofs: ["prf:q-hecke-eigenvalue"],
  tags: ["geometric-langlands", "hecke-algebra", "fiber-functor"],
});
