import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qbeta-counit-transition",
  interprets: "prop:qbeta-counit-closed-form",
  title: "$\\mathfrak{Q}_\\beta$ as a counit transition observable",
  uses: [
    "prop:qbeta-counit-closed-form",
    "rem:energy-scale-planck",
    "prop:neutron-qvalue-symbolic",
  ],
  tags: [
    "beta-decay",
    "q-value",
    "frobenius-counit",
    "transition-observable",
    "interpretation",
  ],
});
