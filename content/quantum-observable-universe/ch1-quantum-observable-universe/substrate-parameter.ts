import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-parameter",
  title: "Substrate parameter",
  tags: ["substrate", "deformation"],
  lean: {
    decl: "QOU.SubstrateParameter",
    validation: "leanok",
  },
  status: "stated",
  uses: ["def:quantum-universe"],
});
