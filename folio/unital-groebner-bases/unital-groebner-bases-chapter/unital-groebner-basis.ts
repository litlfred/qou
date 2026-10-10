import { definition } from "../../schema/builders";

export default definition({
  label: "def:unital-groebner-basis",
  title: "Gröbner--Shirshov basis and unital Gröbner--Shirshov basis",
  tags: ["groebner-basis", "unital"],
  lean: { ref: "ugb:UGB.UnitalGroebner.UnitalGroebnerBasis",
    validation: "not_checked",
  },
  uses: ["def:admissible-system", "def:leading-terms"],
});
