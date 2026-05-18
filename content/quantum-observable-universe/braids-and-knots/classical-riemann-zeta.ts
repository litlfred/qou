import { definition } from "../../schema/builders";

export default definition({
  label: "def:classical-riemann-zeta",
  title: "Classical Riemann zeta function as adelic limit",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.ClassicalRiemannZeta",
    validation: "not_checked",
  },
  uses: ["def:local-q-zeta-function", "def:classical-limit-functor"],
  tags: [
    "riemann-zeta",
    "adelic",
    "classical-limit",
    "euler-product",
  ],
  cites: ["weil1948"],
});
