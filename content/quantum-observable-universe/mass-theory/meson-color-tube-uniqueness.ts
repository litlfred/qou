import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-color-tube-uniqueness",
  title: "Meson m_K/m_π ratio uniqueness via the α_shift universal chain",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  // Note: uses are kept light — the structural dependency on
  // prop:alpha-shift-torus-knot is documented in the narrative,
  // following the planned-block convention.
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness", "meson"],
  lean: { ref: "qou:QOU.BraidKnot.meson_ratio_via_alpha_shift" },
  authorNotes: [
    {
      kind: "status",
      body: "This proposition is **proved conditional on the\n`MesonGMORFactorization` class instance** (the GMOR fusion form\nitself — established empirically in #1396 to 203 ppm, awaiting\nthe resolvent derivation).  The α_shift indexing is fully derived\nvia the default `MesonForceCarrierPair` instance, which\ndischarges sorry-free from `prop:alpha-shift-torus-knot`.\n\nCloses the meson row of the post-#1422 fitting-gap table\n(audit doc Item 4 of the α_shift universal chain), converting\nthe $1098\\times$ $m_K/m_\\pi$ miss from \"open audit finding\" to \"derived\nmodulo shared residue normalisation\".",
    },
  ],
});
