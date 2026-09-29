import { remark } from "../../schema/builders";

/**
 * Applied follow-on to prop:symmetric-block-domain-weight: the AX_nE_m bond-angle
 * master table from the q^ℓ domain weight, the sp/sp²/sp³ hybridisation base,
 * the second-vs-third-row hybridisation flip, and the H₂S +2.1° lone-pair braid
 * asymmetry. Carries the molecular-angle witnesses consumed by the :val table.
 */
export default remark({
  label: "rem:domain-weight-vsepr-angles",
  title: "Bond angles from the $q^{\\ell}$ domain weight",
  interprets: "prop:symmetric-block-domain-weight",
  uses: ["def:h2o-molecular-braid", "prop:h2o-bond-angle-shift"],
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
  tags: [
    "VSEPR",
    "bond-angle",
    "AXE",
    "hybridisation",
    "H2S",
    "molecular-geometry",
  ],
});
