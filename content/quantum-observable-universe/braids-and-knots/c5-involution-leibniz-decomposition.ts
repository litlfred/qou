import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c5-involution-leibniz-decomposition",
  lean: {
    ref: "qou:QOU.BraidKnot.C5InvolutionLeibnizDecomposition",
    validation: "not_checked",
  },
  title:
    "$c_5$ decomposes as $-b^2 - 1/2$: pure-$\\sigma$ Kashiwara contribution plus bar-invariant involution fingerprint from averaged-crossing structure. Interpretation of the unique averaging-resonant rung k = 5 identified in [prop:averaging-resonance-rule](#prop:averaging-resonance-rule); involution supplies the $1/2$ magnitude, while the half-fill cyclic structure supplies the rung selection.",
  uses: [
    "prop:silver-ratio-beta-decay-null",
    "prop:averaging-resonance-rule",
    "prop:q-beta-categorical-precision-ladder",
    "prop:neutron-qvalue-symbolic",
    "rem:chi-per-irrep-cyclotomic-closed-forms",
  ],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
  ],
  tags: [
    "lean-infrastructure",
    "c5-outlier",
    "involution-operator",
    "averaged-crossing",
    "bar-invariance",
    "leibniz-propagation",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/qbeta_silver_ratio_pell_lucas_ck.py",
    witness: [
      "folio-assistant/computations/qbeta-silver-ratio-pell-lucas-ck.witness.json",
    ],
    status: "experimental",
  },
});
