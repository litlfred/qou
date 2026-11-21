import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-heat-kernel-peter-weyl",
  title: "Proof of q heat kernel peter weyl",
  uses: ["prop:q-heat-kernel-peter-weyl"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > **Scope note (2026-11-16).** Corrected from the 2026-11-15 version, which used Jackson integers and the prefactor $\\hbar_q^2$. Both changes are derived, not fitted; see `docs/audits/2026-11-16-binding-reeb-holonomy-laplacian.md` (issue #8091). What is proved: the operator is central (`QOU.SchurWeyl.contentCasimir_comm_σ`). Its Jucys--Murphy elements are relative full twists (`fullTwistB_succ_eq_mul_jmRawB`). Its eigenvalue on a Jucys--Murphy weight vector is $(q-q^{-1})^2\\sum[c][c+1]$ (`reebLaplacianB_smul_of_weight`). The weight vectors exist for generic $q$ by the seminormal form (`seminormalRep_qJM`). All are sorry-free. What is not proved: that $\\Delta^2_k$ is the holonomy of the Reeb rotation loop of the cluster of the first $k+1$ points. That identification is Bridge A (the $n$-body base with $\\xi$ the Euler field, plus Drinfeld--Kohno). The weight-$1$ argument for the Reeb part is written out below and in the audit; it is not formalised. The binding code (`hecke_core_legacy.q_laplacian_eigenvalue`) already computes this $\\mu_\\lambda$, so no number moves. The deuteron term of `_unified_iterative_correction_exact(1, 1)` at the proton $q_0$ is still $-17.69$ MeV against AME $+2.2246$ MeV, the wrong sign. That problem is downstream of $\\mu_\\lambda$ and is not addressed here.\n\n whichever is non-negative (`symInt_reflect`)." },
  ],
});
