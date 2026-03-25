import { example } from "../../schema/builders";

export default example({
  label: "ex:projective-line-su2",
  title: "Projective line for $\\mathrm{SU}(2)$",
  lean: { decl: "QOU.Examples.su2ProjectiveLine" },
  uses: ["def:projective-line-object", "ex:maximal-torus-su2"],
  tags: ["su2", "projective-line"],
});
