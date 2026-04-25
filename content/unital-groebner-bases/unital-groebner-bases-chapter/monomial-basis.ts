import { definition } from "../../schema/builders";

export default definition({
  label: "def:monomial-basis",
  title: "Monomials, monomial bases, and leading terms",
  lean: { ref: "ugb:QOU.GrobnerShirshov.AlgElement",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "monomial", "leading-term"],
  uses: [],
});
