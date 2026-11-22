import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qu-to-qou",
  lean: { ref: "qou:QOU.Torsion.YekutieliTriple.qu_to_qou", validation: "not_checked" },
  title: "Quantum universe with observability and categorical lifting is a QOU",
  tags: ["main-theorem", "qou", "yekutieli", "descent"],
  examples: ["ex:qu-to-qou-su2"],
  uses: [
    "prop:yekutieli-lifting",
    "prop:fiber-adjoint-involution",
  ],
  proofs: ["prf:qu-to-qou"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-10-12",
      body: "Items 2 and 3 restated (owner decision). Item 2 now names the extension ℤ → ℝ → U(1) and gives κ₀ = c₁(ξ) = e(ξ) = χ(S). Item 3, perpetual obstruction in the jet tower, is retracted on closed surfaces and replaced by Kummer persistence: the obstruction to an n-th root is χ mod n in H²(S, μₙ). Item 6 (lifting criterion) is new and proved in Lean (QOU.CentralExtension.PresheafCentralExtension.exists_lift_iff). The jet tower is discussed in rem:jet-tower-splitting-bring. The lean.ref target qu_to_qou proves only Euler-characteristic stability and encodes none of items 2, 3 or 6. Evidence: docs/audits/2026-10-12-jet-tower-band-construction.md, docs/audits/2026-10-12-atiyah-jet-classes-bring.md.",
      see: "prf:qu-to-qou",
    },
  ],
});
