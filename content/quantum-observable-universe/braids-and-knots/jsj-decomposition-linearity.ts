import { conjecture } from "../../schema/builders";

/**
 * JSJ additivity of nucleon braids.
 *
 * Conjectures that the atomic knot complement of an isotope (Z, N)
 * JSJ-decomposes along the inter-nucleon essential tori into Z proton
 * and N neutron hyperbolic pieces, whence (by Thurston's volume
 * additivity over geometric pieces — the proved part) the hyperbolic
 * volume is exactly linear: Vol = Z·Vol_p + N·Vol_n.
 *
 * Lean: QOU/BraidsKnots/LinearJSJVolume.lean axiomatises the
 * decomposition + additivity input (`JSJ_volume_additivity`, cited to
 * Thurston) and derives cluster additivity and the per-proton /
 * per-neutron increments from it.
 */
export default conjecture({
  label: "conj:jsj-decomposition-linearity",
  title: "JSJ additivity of nucleon braids",
  lean: { ref: "qou:QOU.BraidsKnots.JSJ_volume_additivity" },
  uses: [
    "def:atom-knot",
    "prop:thurston-volume-additivity",
  ],
  cites: ["thurston1978"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-07-12",
      body:
        "The original draft of this block quoted working values " +
        "$\\mathrm{Vol}_p \\approx 13.948$ and $\\mathrm{Vol}_n \\approx 3.664$ " +
        "for the nucleon volume quanta. No committed witness pins those " +
        "numbers, and the canonical knot atlas " +
        "(appendix-knot-periodic-table) identifies both nucleon braids " +
        "with the Borromean complement $\\mathcal{B}_3$ " +
        "($\\mathrm{Vol} \\approx 7.33$), so the draft values are recorded " +
        "here as placeholders rather than asserted in prose. The linearity " +
        "claim is independent of the specific quanta.",
    },
    {
      kind: "note",
      date: "2026-07-12",
      body:
        "Integrated from an orphan `.md` (no manifest) per the 2026-07-12 " +
        "exposition-drain ledger §5; the Lean code fence formerly pasted " +
        "into the prose now lives only in the referenced library file " +
        "`lean/QOU/BraidsKnots/LinearJSJVolume.lean`.",
    },
  ],
  tags: [
    "jsj-decomposition",
    "hyperbolic-volume",
    "atomic-knot",
    "volume-additivity",
    "open-conjecture",
  ],
});
