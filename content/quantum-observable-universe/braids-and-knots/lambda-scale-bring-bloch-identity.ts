import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lambda-scale-bring-bloch-identity",
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
