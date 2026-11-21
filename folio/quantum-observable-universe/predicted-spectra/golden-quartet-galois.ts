import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Lean scope (disclosure, not a change of claim).** The `lean.ref` theorem proves that φ, φ⁻¹, −φ, −φ⁻¹ are roots of x⁴ − 3x² + 1 and that φ·φ⁻¹ = 1, plus the two Galois-conjugation identities as separate lemmas. Not formalised: the orbit statement under Gal(ℚ(√5)/ℚ) × ⟨ι⟩, the ι-exchange, regularity of the action, the discriminant, and irreducibility of the quartic's factors over ℚ. The narrative omits irreducibility and the commutation check τ∘ι = ι∘τ; its conclusions are true. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B05; bean qou-k9tf).",
    },
  ],
  label: "prop:golden-quartet-galois",
  title:
    "Golden quartet $\\{1/\\varphi, -\\varphi, \\varphi, -1/\\varphi\\}$ as $\\mathrm{Gal}(\\mathbb{Q}(\\sqrt{5})/\\mathbb{Q}) \\times \\langle \\iota \\rangle$-orbit",
  tags: [
    "golden-ratio",
    "galois-theory",
    "bar-involution",
    "skew-symmetry",
    "minimal-polynomial",
    "splitting-field",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.GoldenQuartetGalois.golden_quartet_galois",
    validation: "not_checked",
  },
  uses: [
    "prop:golden-skew-dual-node",
  ],
});
