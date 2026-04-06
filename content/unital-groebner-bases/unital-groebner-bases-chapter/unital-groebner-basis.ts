import { definition } from "../../schema/builders";

export default definition({
  label: "def:unital-groebner-basis",
  title: "Gröbner basis and unital Gröbner basis",
  tags: ["groebner-basis", "unital"],
  lean: {
    decl: "QOU.UnitalGroebner.UnitalGroebnerBasis",
    validation: "not_checked",
  },
  uses: ["def:admissible-system", "def:leading-terms"],
});
