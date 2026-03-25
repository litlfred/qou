import { definition } from "../../schema/builders";

export default definition({
  label: "def:admissible-system",
  title: "Monomial ordering and admissible system",
  tags: ["groebner-basis", "ordering"],
  lean: {
    decl: "QOU.UnitalGroebner.AdmissibleSystem",
    validation: "not_checked",
  },
  uses: ["def:monomial-basis"],
});
