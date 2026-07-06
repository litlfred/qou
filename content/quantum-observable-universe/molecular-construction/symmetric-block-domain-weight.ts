import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:symmetric-block-domain-weight",
  title: "Symmetric-block domain weight: lone/bond $= q^2$",
  lean: {
    ref: "qou:QOU.Molecular.symmetric_block_domain_weight",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script:
      "computations/molecular_angle_symmetric_block_general.py",
    witness: [
      "computations/molecular-angle-symmetric-block-general.witness.json",
      "computations/h2o-angle-q2-symmetric-block.witness.json",
      "computations/molecular-braid-angle-table.witness.json",
      "computations/molecular-angle-master-table.witness.json",
      "computations/molecular-angle-derive-related.witness.json",
      "computations/hybridization-sp-gap-braid.witness.json",
      "computations/h2s-lone-pair-asymmetry.witness.json",
    ],
  },
  uses: ["def:h2o-molecular-braid", "prop:h2o-bond-angle-shift"],
  tags: [
    "symmetric-block",
    "trivial-representation",
    "VSEPR",
    "bond-angle",
    "q-squared",
    "AXE",
    "molecular-geometry",
  ],
});
