import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean class `GBResidueSpectralSum` carries " +
        "`mass : ℝ` — a categorical **mass**, an MeV-valued observable — " +
        "together with `descended`, `gradedTrace`, `residue` and `q`. The " +
        "residues are taken at **root-of-unity poles of the quantum " +
        "dilogarithm**, i.e. values of an analytic function, and the " +
        "decomposition asserts that the mass is the descended `E⁰` term plus " +
        "a finite sum of those residues. Both endpoints — a mass and a " +
        "dilogarithm residue — are `ℝ` by meaning (§7c), so the file is on " +
        "the archimedean side by construction rather than by oversight.",
    },
  ],
  label: "conj:gs-spectral-decomposition-existence",
  title:
    "Spectral decomposition of the mass into descended trace and residue sum",
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
