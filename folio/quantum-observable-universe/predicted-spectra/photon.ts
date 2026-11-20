import { definition } from "../../schema/builders";

export default definition({
  label: "def:photon",
  title: "Photon (four-term Hecke element with chiral vertex)",
  tags: ["photon", "hecke-algebra", "colored-photon", "gamma-gamma", "definition"],
  defines: ["photon", "bare-photon", "colour-weights"],
  lean: { ref: "qou:QOU.Photon.photon", validation: "not_checked" },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body:
        "**Owner ruling, dated 2026-11-18, confirmed 2026-11-20 15:47–15:48:** the fourth term is the chiral pair-production vertex σ₀σ₁⁻¹, not σ₀σ₁. The choice was made 2026-11-18 19:05Z and recorded in bean `qou-99qc` as \"OWNER WORKING ASSUMPTION: photon last term σ₀σ₁⁻¹ (switched)\", with the note that it was not a ruling to edit this block, so it was not applied: the block was authored 2026-11-17 with σ₀σ₁ (8fe7dbecf4), moved to the library still with σ₀σ₁ (e3c658a58b) and merged in #8367. The owner confirmed on 2026-11-20 that it is a decision (\"That was already decided. Why did it get changed back?\"). The two forms are the same family of elements in different coordinates: γ(φ₀, φ₁, φ₀₁) = γ_old(φ₀ − hφ₀₁, φ₁, φ₀₁). Applied in PR #8583.",
      see: "https://github.com/litlfred/qou/pull/8583",
    },
  ],
});
