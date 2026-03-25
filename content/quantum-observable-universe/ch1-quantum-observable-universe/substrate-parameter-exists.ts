import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-parameter-exists",
  title: "Existence of the substrate parameter",
  lean: {
    decl: "QOU.SubstrateParameter.ofReebDecomposition",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-reeb",
    "def:weight-decomposition",
    "def:substrate-parameter",
  ],
  proofs: ["prf:substrate-parameter-exists"],
  tags: ["existence", "substrate", "deformation"],
});
