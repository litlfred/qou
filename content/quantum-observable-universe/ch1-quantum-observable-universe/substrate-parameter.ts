import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-parameter",
  cites: ["lusztig1993"],
  title: "Substrate parameter",
  tags: ["substrate", "deformation"],
  lean: {
    decl: "QOU.SubstrateParameter",
    validation: "leanok",
  },
  status: "not_started",
  uses: ["def:quantum-universe"],
});
