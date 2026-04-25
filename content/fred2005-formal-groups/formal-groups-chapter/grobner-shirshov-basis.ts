import { definition } from "../../schema/builders";

export default definition({
  label: "def:grobner-shirshov-basis",
  title: "Groebner--Shirshov basis",
  lean: { ref: "fred2005:Fred2005.GrobnerShirshovBasis",
    validation: "not_checked",
  },
  tags: ["groebner-shirshov", "normal-form", "distribution-algebra"],
  uses: ["def:non-commutative-formal-group"],
  cites: ["fred2005"],
});
