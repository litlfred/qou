import { definition } from "../../schema/builders";

export default definition({
  label: "def:leading-terms",
  title: "Leading monomial, coefficient, and term",
  tags: ["groebner-basis", "algebra"],
  lean: { ref: "ugb:UGB.UnitalGroebner.LeadingTerm",
    validation: "not_checked",
  },
  uses: ["def:monomial-basis"],
});
