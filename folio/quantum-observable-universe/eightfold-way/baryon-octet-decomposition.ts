import { proposition } from "../../schema/builders";

/**
 * The baryon octet: decomposition, weight table, and the one CONTENT-BEARING
 * result in the eightfold null-result family.
 *
 * Closes qou-wd07. Before this block the octet appeared only as a passing
 * paragraph inside borromean-decuplet-derivation ("Octet vs. decuplet"), with
 * no weight table and no p/n/Sigma/Lambda/Xi states anywhere in the chapter.
 *
 * THE POINT is not the table. The chapter's other three eightfold relations
 * are identities of their first-order ansatz and so discriminate among no
 * mechanisms:
 *
 *   - rem:meson-mass-splitting     GMO is an identity            -> content-FREE
 *   - rem:decuplet-equal-spacing   equal spacing is an identity  -> content-FREE
 *   - rem:u-spin-coleman-glashow   CG is an identity             -> content-FREE
 *   - rem:vector-meson-nonet       mixing is UNCONSTRAINED       -> content-BEARING
 *   - prop:baryon-octet-decomposition  weight map NON-INJECTIVE  -> content-BEARING
 *
 * The octet's weight diagram is degenerate (Lambda and Sigma^0 both at
 * (2I3, Y) = (0,0)) while the decuplet's is not. Hence NO function of the
 * weight alone separates them, so any weight-only mass formula predicts
 * m_Lambda = m_Sigma0 -- refuted by 77 MeV (~7%), two orders larger than the
 * 0.8% Coleman-Glashow residual. That is a scope-(b) structural exclusion
 * with the invariant PROVED (non-injectivity), not asserted.
 *
 * Machine-checked sorry-free in QOU/Eightfold/OctetWeightDegeneracy.lean;
 * #print axioms shows propext/Quot.sound only, no sorryAx.
 *
 * GUARDRAIL encoded in both .md and .lean: dim S^(2,1) = 2 (Hecke multiplicity
 * of the octet in V^x3) is NOT the Lambda/Sigma^0 degeneracy (two states over
 * one lattice point in ONE copy). Conflating them would make it look as though
 * the Hecke algebra already supplied the octet's missing label. It does not.
 *
 * ANTI-FITTING: nothing fitted, nothing wired. PDG masses are comparators.
 * Conditional on N=3 throughout, which the framework does not supply
 * (RowCapObstruction.lean proves the N=2 obstruction).
 *
 * PLACEMENT: last in sec:baryon-multiplets so every uses[] edge runs backward
 * (schur-weyl -> decuplet -> equal-spacing -> coleman-glashow -> here). Takes
 * the section 4 -> 5 blocks, inside the detangler 3-18 band.
 */
export default proposition({
  label: "prop:baryon-octet-decomposition",
  title: "The baryon octet and the degeneracy of its weight diagram",
  // The ref names the OPERATIVE declaration -- the exclusion, not the table.
  lean: {
    ref: "qou:QOU.Eightfold.OctetWeightDegeneracy.weight_function_cannot_separate_lambda_sigma0",
  },
  // IMMEDIATE NEIGHBOURS ONLY (AGENTS.md: uses[] is not the transitive cone).
  // The first draft listed all five of schur-weyl / borromean-decuplet /
  // meson-mass-splitting / decuplet-equal-spacing / u-spin-coleman-glashow;
  // uses-editorial-hygiene scored that 5 edges / 4 redundant, because
  // rem:u-spin-coleman-glashow already reaches the other four:
  //   u-spin-coleman-glashow -> {borromean-decuplet, meson-mass-splitting,
  //                              decuplet-equal-spacing}
  //   borromean-decuplet     -> schur-weyl-eightfold
  // The .md still hyperlinks all five; a \hyperref is a cross-reference for
  // the reader, not a dependency edge, and the two are deliberately distinct.
  // rem:u-spin-coleman-glashow dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // cited only as a parallel example of another null result. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: [],
  cites: ["gellmann1962", "jimbo1986"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): and the difference is machine-checked\nin `QOU/Eightfold/OctetWeightDegeneracy.lean`:" },
  ],
});
