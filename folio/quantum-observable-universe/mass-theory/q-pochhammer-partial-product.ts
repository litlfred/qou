import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-pochhammer-partial-product",
  title: "$q$-Pochhammer partial product $\\Phi_n(x; q)$",
  lean: {
    ref: "qou:QOU.QPochhammer.partialProduct",
    validation: "not_checked",
  },
  uses: ["conj:quantum-dilogarithm-stratified"],
  cites: ["faddeev1994", "kashaev1997"],
  tags: [
    "q-pochhammer",
    "quantum-dilogarithm",
    "partial-product",
    "phi-q",
    "denominator",
  ],
});
