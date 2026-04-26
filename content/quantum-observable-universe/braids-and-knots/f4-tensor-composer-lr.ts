import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:f4-tensor-composer-lr",
  title:
    "F4 tensor-product composer: $\\chi_\\lambda(T_{\\beta_1 \\otimes \\beta_2}) = \\sum c^\\lambda_{\\mu\\nu} \\, \\chi_\\mu(T_{\\beta_1}) \\, \\chi_\\nu(T_{\\beta_2})$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.f4_tensor_composer_lr",
    validation: "not_checked",
  },
  uses: [
    "prop:hoefsmit-seminormal-form",
    "prop:hecke-markov-transition",
  ],
  cites: ["stanley1999"],
  tags: [
    "f4",
    "littlewood-richardson",
    "tensor-product",
    "hecke-character",
    "compose",
  ],
});
