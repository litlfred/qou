import { definition } from "../../schema/builders";

export default definition({
  label: "def:remainder-module",
  title: "Remainder modules $O(I)$ and $\\tilde{O}(I)$",
  lean: { ref: "ugb:UGB.GrobnerShirshov.isNormalForm",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "remainder", "free-module"],
  uses: ["def:admissible-system", "def:monomial-basis"],
});
