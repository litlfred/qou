import { example } from "../../schema/builders";

export default example({
  interprets: "prop:frobenius-relation",
  label: "ex:frobenius-su2",
  title: "Frobenius relation for $\\mathrm{SU}(2)$",
  lean: { ref: "qou:QOU.Examples.su2Frobenius", validation: "not_checked" },
  uses: ["prop:frobenius-relation", "ex:qou-su2"],
  tags: ["su2", "frobenius"],
});
