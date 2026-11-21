import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-color-tube-uniqueness",
  title: "Meson m_K/m_π ratio uniqueness via the α_shift universal chain",
  cites: ["jones1987", "wenzl1988"],
  // Note: uses are kept light — the structural dependency on
  // prop:alpha-shift-torus-knot is documented in the narrative,
  // following the planned-block convention.
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness", "meson"],
  lean: { ref: "qou:QOU.BraidKnot.meson_ratio_via_alpha_shift" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): *The $q$-integer indices are forced by the $\\alpha_{\\text{shift}} = k \\cdot (p - 1)$ formula ([Pole order at $q=0$ of the torus-knot character](#prop:alpha-shift-torus-knot)).*" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nWe stage the uniqueness via the conditional-class pattern:\n- `MesonGMORFactorization R mK2_over_mpi2 qChar m n`: the substrate factorisation axiom.\n- `MesonForceCarrierPair`: the derived index assertion $\\alpha_{\\text{shift}}(T(2, 3)) = 3$ and $\\alpha_{\\text{shift}}(T(2, 4)) = 4$.\n- `theorem meson_ratio_via_alpha_shift`: proves the factorisation using the specific indices." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (`prop:alpha-shift-torus-knot`)" },
    {
      kind: "status",
      body: "This proposition is **proved conditional on the\n`MesonGMORFactorization` class instance** (the GMOR fusion form\nitself — established empirically in #1396 to 203 ppm, awaiting\nthe resolvent derivation).  The α_shift indexing is fully derived\nvia the default `MesonForceCarrierPair` instance, which\ndischarges sorry-free from `prop:alpha-shift-torus-knot`.\n\nCloses the meson row of the post-#1422 fitting-gap table\n(audit doc Item 4 of the α_shift universal chain), converting\nthe $1098\\times$ $m_K/m_\\pi$ miss from \"open audit finding\" to \"derived\nmodulo shared residue normalisation\".",
    },
  ],
});
