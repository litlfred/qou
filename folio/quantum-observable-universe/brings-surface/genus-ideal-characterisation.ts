import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:genus-ideal-characterisation",
  lean: { ref: "qou:QOU.MassTheory.genus_ideal_characterisation",
    validation: "not_checked",
  },
  title: "Genus-filtration ideal in Hecke coordinates",
  tags: ["seifert-surface", "ideal", "hecke-coordinates", "truncation"],
  uses: ["lem:genus-from-hecke-completeness", "lem:chebyshev-degree-genus"],
  proofs: ["prf:genus-ideal-characterisation"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** The Lean proves `RingHom.ker (Ideal.Quotient.mk I) = I` for I = (X⁵) in ℤ[X], by `Ideal.mk_ker`; this holds for every ideal and says nothing about genus. The former statement also characterised (u⁵) as the Chebyshev terms whose Seifert cycles have no target in H₁(Σ₄); that characterisation is not formalised and is now marked as not claimed. The audit also found two rank errors in the narrative proof that cancel; the proof block is unchanged. Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P13).",
    },
  ],
});
