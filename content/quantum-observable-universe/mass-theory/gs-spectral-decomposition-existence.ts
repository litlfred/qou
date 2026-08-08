import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-spectral-decomposition-existence",
  title:
    "Spectral decomposition of the mass into descended trace and residue sum",
  // This ref is CORRECT and was left unchanged (bean qou-ref10).
  //
  // It was listed as "absent from the whole corpus" because the corpus-wide
  // declaration grep enumerates top-level declaration keywords only.
  // `spectral_decomposition` is a FIELD of `class GBResidueSpectralSum` in
  // namespace `QOU.BraidKnot` — so the projection's fully-qualified name is
  // exactly `QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition`, and
  // the ref also resolves by module path to
  // `lean/QOU/BraidKnot/GBResidueSpectralSum.lean`. Nothing to fix.
  lean: {
    ref: "qou:QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition",
    validation: "not_checked",
  },
  uses: [
    "prop:graded-trace-residue-split",
    "conj:gs-residue-at-root-existence",
    "thm:knot-mass-formula-unified",
  ],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "mass",
    "spectral-decomposition",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
});
