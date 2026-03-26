import { example } from "../../schema/builders";

export default example({
  label: "ex:connection-su2",
  title: "Connection and curvature on $\\mathcal{O}(\\mathrm{SU}(2))$",
  lean: { decl: "QOU.Examples.su2Connection" },
  uses: ["def:categorical-connection", "ex:fiber-adjoint-su2"],
  tags: ["su2", "connection"],
});
