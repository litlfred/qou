import { definition } from "../../schema/builders";

export default definition({
  label: "def:monomial-basis",
  title: "Monomials, monomial bases, and leading terms",
  lean: {
    decl: "QOU.GrobnerShirshov.AlgElement",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "monomial", "leading-term"],
  uses: [],
});
