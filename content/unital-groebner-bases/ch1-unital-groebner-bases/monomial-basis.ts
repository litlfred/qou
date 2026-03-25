import { definition } from "../../schema/builders";

export default definition({
  label: "def:monomial-basis",
  title: "Monomial basis",
  tags: ["groebner-basis", "algebra"],
  lean: {
    decl: "QOU.UnitalGroebner.MonomialBasis",
    validation: "not_checked",
  },
  uses: [],
});
