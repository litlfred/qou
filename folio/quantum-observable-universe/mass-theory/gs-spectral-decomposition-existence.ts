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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Conjectural status.** A Lean proof requires formalized definitions for the graded trace and residues, ..." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean encoding.** Encoded as the class-field axiom `spectral_decomposition` on `GBResidueSpectralSum`. Instances supply this identity." },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/BraidKnot/GBResidueSpectralSum.lean` is a " +
        "spectral sum of **residues of the quantum dilogarithm at roots of " +
        "unity**: its `RootOfUnity.value : ℝ` is documented in the file as " +
        "*\"real part; full Mathlib version uses `Complex`\"*, and " +
        "`descended`/`residue`/`mass` are the MeV-valued categorical mass and " +
        "its cyclotomic corrections. Generalising a root-of-unity value or a " +
        "mass to an arbitrary ordered field would discard the meaning that " +
        "makes the sum a mass, so the block sits on the archimedean side of " +
        "the §7c wall by construction.",
    },
  ],
});
