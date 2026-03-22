import { definition } from "../../schema/builders";

export default definition({
  label: "def:projective-line-object",
  title: "Projective line object",
  lean: {
    decl: "QOU.ProjectiveLineObject",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:quantum-observable-universe", "def:maximal-torus"],
  examples: ["ex:projective-line-su2"],
  tags: ["projective-line"],
});
