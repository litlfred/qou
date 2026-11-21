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
  // The ref carries the MODULE path `QOU/BraidsKnots/LinearJSJVolume.lean`
  // plus the declaration name, which is how `lean.ref` resolves (§0a
  // candidate 2). The bare `QOU.BraidsKnots.JSJ_volume_additivity` did not
  // resolve: there is no `QOU/BraidsKnots.lean` and no
  // `QOU/BraidsKnots/JSJ_volume_additivity.lean`.
  //
  // Target: the `axiom JSJ_volume_additivity`, which states exactly this
  // block's headline equation `Vol(AtomicKnot Z N) = Z·Vol_p + N·Vol_n`
  // (cited to [thurston1978]). The block's *decomposition hypothesis* —
  // that the complement JSJ-splits into exactly Z proton and N neutron
  // pieces — is the conjectural half and is not separately formalised;
  // the axiom bundles it into the additivity statement.
  lean: { ref: "qou:QOU.BraidsKnots.LinearJSJVolume.JSJ_volume_additivity" },
  uses: [
    "def:atom-knot",
    "prop:thurston-volume-additivity",
  ],
  cites: ["thurston1978"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing by meaning.** \`Vol\` is the hyperbolic volume (Gromov norm; Thurston) of a knot complement, and \`Vol_p\` / \`Vol_n\` are the proton/neutron volume quanta. No ordering tactic appears — the arithmetic is \`ring\` — but a hyperbolic volume is a real number, not an element of a generic commutative ring, so this is not a gratuitous specialisation. Same class as the topological-mass cluster verdict (bean \`tmvac\`): a norm/volume is \`ℝ\` by what it *is*, not by what is done to it.`,
    },
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; it is the same additivity principle as the per-tetrahedron decomposition of [Thurston volume additivity](#prop:thurston-volume-additivity)" },
  ],
  tags: [
    "jsj-decomposition",
    "hyperbolic-volume",
    "atomic-knot",
    "volume-additivity",
    "open-conjecture",
  ],
});
