import { definition } from "../../schema/builders";

export default definition({
  label: "def:admissible-system",
  title: "Monomial ordering and admissible system",
  lean: { ref: "ugb:UGB.GrobnerShirshov.AdmissibleOrder",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "ordering", "admissible"],
  uses: ["def:monomial-basis"],
});
