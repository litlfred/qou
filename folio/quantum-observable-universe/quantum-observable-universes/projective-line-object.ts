import { definition } from "../../schema/builders";

export default definition({
  label: "def:projective-line-object",
  title: "Projective line object",
  lean: { ref: "qou:QOU.ProjectiveLineObject",
    validation: "not_checked",
  },
  uses: ["def:maximal-torus"],
  examples: ["ex:projective-line-su2"],
  tags: ["projective-line"],
});
