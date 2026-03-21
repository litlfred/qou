import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-ext-deriv",
  title: "Categorical $q$-deformed exterior derivative",
  tags: ["exterior-derivative", "deformation"],
  lean: {
    decl: "QOU.CategoricalQExtDeriv",
    validation: "leanok",
  },
  status: "not_started",
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-connection",
    "def:substrate-parameter",
    "def:weight-decomposition",
  ],
});
