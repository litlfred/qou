import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:higgs-t28",
  title:
    "The Higgs boson as $T(2,8)$: the link spanning three exceptional divisors",
  lean: {
    ref: "qou:QOU.HiggsT28.HiggsAsT28",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "prop:fermion-boson-knot-link",
  ],
  tags: [
    "higgs",
    "boson",
    "torus-link",
    "exceptional-divisor",
    "mass-mechanism",
    "scalar",
    "genus-3",
  ],
});
