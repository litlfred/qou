import { definition } from "../../schema/builders";

export default definition({
  label: "def:s-polynomial",
  title: "$S$-polynomial",
  lean: { ref: "ugb:UGB.UnitalGroebner.sPolynomial",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "s-polynomial"],
  uses: ["def:admissible-system", "def:leading-term-data"],
  cites: ["leitnerpawloski2004"],
});
