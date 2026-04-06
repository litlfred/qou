import { definition } from "../../schema/builders";

export default definition({
  label: "def:groebner-basis",
  title: "Gröbner--Shirshov basis and unital Gröbner--Shirshov basis",
  lean: {
    decl: "QOU.GrobnerShirshov.IsGrobnerShirshovBasis",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "unital", "s-polynomial"],
  uses: ["def:admissible-system", "def:monomial-basis"],
});
