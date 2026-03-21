import { definition } from "../../schema/builders";

export default definition({
  label: "def:weight-decomposition",
  title: "Weight decomposition",
  lean: {
    decl: "QOU.WeightDecomposition",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:quantum-observable-universe", "def:maximal-torus", "def:higher-forms"],
  tags: ["weight", "decomposition"],
});
