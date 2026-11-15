import { definition } from "../../schema/builders";

export default definition({
  label: "def:leading-term-data",
  title: "Leading monomial, coefficient, and term",
  lean: { ref: "ugb:UGB.UnitalGroebner.LeadingTerm",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "leading-term"],
  uses: ["def:monomial-basis"],
  cites: ["leitnerpawloski2004"],
});
