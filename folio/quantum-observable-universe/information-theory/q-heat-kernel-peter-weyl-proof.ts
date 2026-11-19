import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-heat-kernel-peter-weyl",
  title: "Proof of q heat kernel peter weyl",
  uses: ["prop:q-heat-kernel-peter-weyl"],
  authorNotes: [
    {
      kind: "caveat",
      body: "Scope audit (2026-11-15, `docs/audits/2026-11-15-q-laplacian-eigenvalue-derivation.md`): only the prefactor $\\hbar_q^2 = (1-q^{-1})^2$ is derived from `rem:q-laplacian-expansion`; the eigenvalue of $\\Delta_\\xi$ on a Wedderburn block is not derived. Companion Lean (`q-heat-kernel-peter-weyl.lean`: `jacksonInt_mul_succ`, `muLambda_from_sq_bracket`, `cosh_eq_sq_bracket_add_two`; `QJucysMurphy.lean`; `QOU.SchurWeyl.contentCasimir_smul_of_weight`, sorry-free conditional on the seminormal form) proves algebraic identities on the formula rather than identifying $\\Delta_\\xi$ with $C_n$. Legacy code `hecke_core_legacy.q_laplacian_eigenvalue` (`_unified_iterative_correction_exact(1, 1)`) uses the bare symmetric-integer sum without $\\hbar_q^2$.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/binding_heat_kernel_weight_probe.py",
    witness: "computations/binding-heat-kernel-weight-probe.witness.json",
    status: "verified",
  },
});
