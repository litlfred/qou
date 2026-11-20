import { remark } from "../../schema/builders";

/**
 * The vector meson nonet (1-) and singlet-octet mixing.
 *
 * The third member of the eightfold-way target-scoring family, and the
 * one that comes out the OTHER way:
 *
 *   - rem:meson-mass-splitting     GMO is an identity -> content-FREE
 *   - rem:decuplet-equal-spacing   equal spacing is an identity -> content-FREE
 *   - rem:vector-meson-nonet       mixing is UNCONSTRAINED -> content-BEARING
 *
 * ANTI-FITTING: nothing here is fitted and nothing is wired. PDG values
 * are comparators. The block makes no claim that the framework derives
 * the mixing — it cannot currently attempt it, since the singlet is
 * unavailable at dim V = 2 (RowCapObstruction). What is established is
 * that a derivation WOULD be evidence, which is precisely what the two
 * null results establish is NOT true of GMO or equal spacing.
 *
 * Created 2026-08-14 (bean qou-s3um), closing the coverage gap the
 * SM/eightfold cheat sheet ranked highest.
 */
export default remark({
  label: "rem:vector-meson-nonet",
  title: "The vector nonet: singlet–octet mixing is the content-bearing target",
  interprets: "prop:meson-octet-decomposition",
  // The ref names a DECLARATION, not the module, following the pattern of
  // rem:meson-mass-splitting and rem:decuplet-equal-spacing.
  // `mixing_unconstrained` is the POSITIVE result here: with the GMO-fixed
  // octet entry held fixed, any physical spectrum is realisable, so the
  // ansatz places no constraint on the mixing.
  lean: {
    ref: "qou:QOU.Eightfold.NonetMixingUnconstrained.mixing_unconstrained",
  },
  // NOTE (detangler): rem:decuplet-equal-spacing is the companion null
  // result and is discussed in the .md, but it lives in the LATER section
  // sec:baryon-multiplets — listing it here would create a forward edge.
  // The prose therefore names it and its Lean file without an anchor link.
  // The proposed chapter reorganisation (docs/sm-eightfold-derivation-cheat-sheet.md
  // §9.2) puts all three target-scoring blocks in one later section, at
  // which point this edge becomes backward and can be added.
  uses: [
    "prop:meson-octet-decomposition",
    "rem:meson-mass-splitting",
  ],
  cites: ["gellmann1962"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Values from\n[`nonet-mixing-purity.witness.json`](../../../computations/nonet-mixing-purity.witness.json);\nPDG central values\n\n(`QOU/Eightfold/DecupletEqualSpacing.lean`, established later in this\nchapter)" },
  ],
});
