import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:higgs-t28",
  title:
    "The Higgs boson as $T(2,8)$: the link spanning three exceptional divisors",
  tags: [
    "higgs",
    "boson",
    "torus-link",
    "exceptional-divisor",
    "mass-mechanism",
    "scalar",
    "genus-3",
  ],
  uses: [
    "prop:fermion-boson-knot-link",
    "prop:torus-knot-generators",
    "conj:borromean-quark",
    "def:color-tube-coordinates",
    "def:crossing-energy",
    "prop:local-substrate-q",
  ],
});
