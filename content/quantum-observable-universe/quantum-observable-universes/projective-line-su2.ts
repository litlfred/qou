import { example } from "../../schema/builders";

export default example({
  interprets: "def:projective-line-object",
  label: "ex:projective-line-su2",
  title: "Projective line for $\\mathrm{SU}(2)$",
  lean: { ref: "qou:QOU.Examples.su2ProjectiveLine", validation: "not_checked" },
  uses: ["def:projective-line-object", "ex:maximal-torus-su2"],
  tags: ["su2", "projective-line"],
});
