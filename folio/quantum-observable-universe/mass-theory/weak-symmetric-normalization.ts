import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:weak-symmetric-normalization",
  title:
    "Weak-sector symmetric-channel Plancherel normalization $\\mathcal{N}_{\\rm sym}(q)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.weak_symmetric_normalization",
    validation: "not_checked",
  },
  uses: [
    "conj:gram-determinant-plancherel-ratio",
    "prop:weak-spectral-completeness",
    "conj:electroweak-higgs-torus-link-triplet",
  ],
  tags: [
    "plancherel",
    "weak-coupling",
    "symmetric-channel",
    "wedderburn",
    "n-sym",
    "nv-1",
    "categorical-normalization",
  ],
  // Evaluates the stated polynomial (q^4+q^6+q^8)/3 at the proton q_0 and
  // checks its factorisation exactly. Previously pointed at
  // q_pinning_50_digit.py, which never computes N_sym (QA 2026-11-20).
  computation: {
    engine: "mpmath",
    script: "computations/weak_symmetric_normalization_value.py",
    witness: "computations/weak-symmetric-normalization-value.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "deprecated",
      body: "**DEMOTED.** Earlier drafts of this proposition framed $\\mathcal{N}_{\\rm sym}(q)$ as a Plancherel-weighted ratio with uniform $1/[2]_q$ weights — derived under the dimensionally-inconsistent $H_2(q)$-only formulation. Per `thm:hoefsmit-ew-cell-content`, the operative structural quantity is the **direct cell-content trace** of $\\sigma_1^4 \\sigma_3^6 \\sigma_5^8$ on the pure-eigenspace — bar-self-dual, derived without Plancherel weights. The Plancherel-weighted form is retained only as a **degenerate special case** for backward reference; do not use it for $N_v$ derivation.",
    },
    {
      kind: "status",
      body: "**Upstream parallel.** The upstream block `conj:n-sym-symmetric-channel-normalization` (already on main) carries the Plancherel-weighted N_sym framing with N_sym(q_0) = 213.11 canonical pinned from CODATA G_F. That back-solve is a CAL-3 violation (N_v functions as a fourth calibration). The bar-self-dual $\\mathrm{tr}_{\\rm pure}$ derivation supersedes both this proposition and the upstream conjecture for the structural N_v ansatz; the upstream block should likewise be demoted in a follow-up.",
    },
    {
      kind: "status",
      body: "**Open** as a formal proposition. The closed-form expression\n$\\mathcal{N}_{\\rm sym}(q) = q^6 \\cdot [3]_{q^2} / 3 \\in R$ is\nstraightforwardly derivable once\n[`prop:weak-spectral-completeness`](#prop:weak-spectral-completeness)\nis in place; the open inputs are:\n\n1. **Discharge** the host-distinctness drop (this audit, §1) — done.\n2. **Verify** the Frobenius-trace normalisation $\\tau(e_X^\\pm) =\n   1/[2]_q$ is uniform across $X \\in \\{W, Z, H\\}$ (follows\n   mechanically from the projector formulas and Hecke relations,\n   but should be authored as a small lemma).\n3. **Connect** to the constrained-PSLQ ansatz: confirm that\n   $\\mathcal{N}_{\\rm sym}(q)$ + the EW $[2k]_q$ basis suffices to\n   reach CODATA-$G_F$ precision for $N_v$.",
    },
  ],
});
