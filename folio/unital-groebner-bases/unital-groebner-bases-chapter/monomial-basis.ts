import { definition } from "../../schema/builders";

export default definition({
  label: "def:monomial-basis",
  title: "Monomials and monomial bases",
  lean: { ref: "ugb:UGB.GrobnerShirshov.AlgElement",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "monomial"],
  uses: [],
});
