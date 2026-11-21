import { definition } from "../../schema/builders";

export default definition({
  label: "def:grobner-shirshov-basis",
  title: "Gröbner basis of the distribution algebra",
  lean: { ref: "ugb:UGB.GrobnerShirshov.NormalFormBasis",
    validation: "not_checked",
  },
  tags: ["groebner-shirshov", "normal-form", "distribution-algebra"],
  uses: ["def:non-commutative-formal-group"],
  cites: ["leitner2006", "leitnerpawloski2004"],
});
