import { example } from "../../schema/builders";

export default example({
  label: "ex:dagger-su2",
  title: "Involutive structure on $\\mathrm{Rep}(\\mathrm{SU}(2))$",
  lean: { decl: "QOU.Examples.su2Dagger" },
  uses: ["def:involutive-structure", "def:positive-definite-dagger", "ex:frobenius-su2"],
  tags: ["su2", "involutive"],
});
