import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:alpha-k-categorical-closure",
  title:
    "Closed-form resummation of the categorical stratum prefactors $\\alpha_k$ — geometric vs symmetric q-dilogarithm candidates",
  lean: {
    ref: "qou:QOU.BraidKnot.AlphaKCategoricalClosure",
    validation: "not_checked",
  },
  uses: [
    "prop:alpha-k-derivation-procedure",
    "rem:beta-decay-energy-scale",
  ],
  cites: [
    "wenzl1988",
    "jones1985",
    "kassel1995",
  ],
  tags: [
    "tier:E",
    "alpha-k",
    "categorical-closure",
    "geometric-series",
    "q-dilogarithm",
    "li2q",
    "brane-tower",
    "CAL-3",
    "open-conjecture",
    "open-rd-item-6",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_beta_form_a_n1_extension.py",
    witness: [
      "computations/q-beta-form-a-n1-extension.witness.json",
    ],
    status: "experimental",
  },
});
