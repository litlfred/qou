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
    "prop:gram-determinant-plancherel-ratio",
    "prop:knot-operator-lp-selection",
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
  // computation removed: incomplete schema (had witness without engine/script/status).
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      body: "**Open** as a formal proposition. The closed-form expression\n$\\mathcal{N}_{\\rm sym}(q) = q^6 \\cdot [3]_{q^2} / 3 \\in R$ is\nstraightforwardly derivable once\n[`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)\nis in place; the open inputs are:\n\n1. **Discharge** the host-distinctness drop (this audit, §1) — done.\n2. **Verify** the Frobenius-trace normalisation $\\tau(e_X^\\pm) =\n   1/[2]_q$ is uniform across $X \\in \\{W, Z, H\\}$ (follows\n   mechanically from the projector formulas and Hecke relations,\n   but should be authored as a small lemma).\n3. **Connect** to the constrained-PSLQ ansatz: confirm that\n   $\\mathcal{N}_{\\rm sym}(q)$ + the EW $[2k]_q$ basis suffices to\n   reach CODATA-$G_F$ precision for $N_v$.",
    },
  ],
});
