import { definition } from "../../schema/builders";

export default definition({
  label: "def:groebner-basis",
  title: "Gröbner--Shirshov basis and unital Gröbner--Shirshov basis",
  lean: { ref: "ugb:UGB.GrobnerShirshov.IsGrobnerShirshovBasis",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "unital", "s-polynomial"],
  uses: ["def:admissible-system", "def:monomial-basis"],
  // Foundational GS-basis references: Bokut (general/Lie algebra
  // setting) + Leitner-Pawloski (unital generalisation over arbitrary
  // commutative ground rings — see Definition 5 of math/0409565).
  cites: ["bokut2005", "leitnerpawloski2004"],
});
