import { conjecture } from "../../schema/builders";

// CAL-4 caveat (2026-05-22): demoted prop → conj per AGENTS.md §3b
// conjectural propagation rule (uses[] contains conj:bring-hyperbolic-
// knot-bloch-decomposition with no §3b-cond class-instance hypothesis
// on the Lean side), and per the empirical falsification of the
// hyperbolic-knot-basis route: Bring-Bloch PSLQ search at tiers 0-5
// (Tier 5 over 52-knot basis through 11-crossing at coefficient
// 10^30, dps=100) returned NO integer relation for the proton
// CODATA-closure target 18.0258... Per the tier 5 conclusion
// (bring_bloch_tier5_search_m_p.py), the proton's Bring-decomposition
// is "genuinely transcendental" in the tested basis; the q-dilog
// tower is the remaining research direction. The Lean theorem here
// is currently vacuous: `rfl` against the definitional unfold of
// `AtomKnot.lambdaScale := bringBlochRegulator / volClosure`, whose
// components `bringBlochRegulator` and `volClosure` are `opaque`
// placeholders — says nothing about WHICH integer combination
// realises the scale.
export default conjecture({
  label: "conj:lambda-scale-bring-bloch-identity",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.lambda_scale_bring_bloch_identity",
    validation: "not_checked",
  },
  title: "Categorical identity for the per-knot scale factor λ_K_scale via Bring-Bloch decomposition",
  tags: [
    "lambda-scale",
    "bloch-wigner",
    "bring-decomposition",
    "archimedean-functor",
    "categorical-derivation",
    "compute-bridge",
  ],
  // Note: prop:phi-q-tower-jsj-bridge and prop:mass-tower-operator-valued
  // exist on main as orphan .ts files (no chapter-manifest slot); the
  // .md narrative cross-refs them via [...](#label) which produces
  // warning-level (not error) unresolved cross-refs. Lift back into
  // uses[] once they're slotted in the chapter manifest.
  uses: [
    "conj:bring-hyperbolic-knot-bloch-decomposition",
    "rem:kashaev-as-archimedean-realization",
    "conj:borromean-baryon-mass-formula",
    "def:atomic-braid",
  ],
  cites: [
    "borel1974",
    "wenzl1988",
    "macdonald1995",
    "adams1985hyperbolic",  // Vol(𝓑₃) = 2 ideal regular octahedra
    "lewin1981",            // Λ(π/4) = G/2 identity for Catalan
  ],
});
