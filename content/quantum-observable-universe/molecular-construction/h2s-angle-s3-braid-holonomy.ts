import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:h2s-angle-s3-braid-holonomy",
  title: "H₂S bond-angle residual $=$ chiral $S^3$ braid holonomy",
  lean: {
    ref: "qou:QOU.Molecular.H2SAngleS3HolonomyConjecture",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script:
      "folio-assistant/computations/h2s_chirality_residue_s3_holonomy.py",
    witness: [
      "folio-assistant/computations/h2s-chirality-residue-s3-holonomy.witness.json",
      "folio-assistant/computations/h2s-chiral-residue-bar-antisymmetric.witness.json",
      "folio-assistant/computations/h2s-bring-residual-mixing.witness.json",
    ],
  },
  uses: [
    "prop:symmetric-block-domain-weight",
    "prop:chirality-residue-mass-term",
    "def:bar-involution",
  ],
  tags: [
    "H2S",
    "bond-angle",
    "chirality",
    "S3-holonomy",
    "Chern-Simons",
    "bar-anti-symmetric",
    "q-Dirac-kernel",
  ],
});
