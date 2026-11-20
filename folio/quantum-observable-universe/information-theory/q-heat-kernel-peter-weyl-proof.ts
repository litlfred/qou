import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-heat-kernel-peter-weyl",
  title: "Proof of q heat kernel peter weyl",
  uses: ["prop:q-heat-kernel-peter-weyl"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Scope-note references: the companion Lean proves identities about the formula, not that it is an eigenvalue; content-Casimir action is `QOU.SchurWeyl.contentCasimir_smul_of_weight`, sorry-free, conditional on the seminormal form; see `docs/audits/2026-11-15-q-laplacian-eigenvalue-derivation.md`. The binding code (`hecke_core_legacy.q_laplacian_eigenvalue`) uses the bare sum; the deuteron term of `_unified_iterative_correction_exact(1, 1)` is $-17.69$ MeV with the code's $\\mu_\\lambda$. Jackson shift identity (`jacksonInt_mul_succ` in `q-heat-kernel-peter-weyl.lean`): Bar-symmetrised Jucys--Murphy sum (defined in `QJucysMurphy.lean`)." },
  ],
});
