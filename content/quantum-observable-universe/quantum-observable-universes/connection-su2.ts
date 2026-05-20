import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-connection",
  label: "ex:connection-su2",
  title: "Connection and curvature on $\\mathcal{O}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2Connection", validation: "not_checked" },
  uses: ["def:categorical-connection", "ex:fiber-adjoint-su2"],
  tags: ["su2", "connection"],
  cites: [
    "woronowicz1987-twisted-su2",
  ],
});
