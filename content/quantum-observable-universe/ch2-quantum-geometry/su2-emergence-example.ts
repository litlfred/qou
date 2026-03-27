import { example } from "../../schema/builders";

export default example({
  interprets: "thm:su2-emergence",
  label: "ex:su2-emergence",
  title: "Emergence of $\\mathrm{SU}(2)$: the full chain",
  lean: { decl: "QOU.Examples.su2Emergence" },
  uses: ["thm:su2-emergence", "ex:frobenius-su2", "ex:dagger-su2"],
  tags: ["su2", "emergence"],
});
