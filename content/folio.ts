import { folio, paperRef } from "./schema/builders";

/**
 * Repository folio — the collection of all papers.
 *
 * The assistant landing page reads this to discover papers.
 * Each paper is referenced by its directory under content/.
 */
export default folio({
  title: "litlfred's Papers",
  papers: [
    paperRef({
      dir: "quantum-observable-universe",
      title: "Quantum Observable Universe",
      description:
        "A framework for quantum physics via rigid monoidal categories, " +
        "higher-form symmetries, and observable algebras.",
      tags: ["quantum", "category-theory", "formalization"],
      url: "papers/quantum-observable-universe",
    }),
    paperRef({
      dir: "unital-groebner-bases",
      title: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings",
      description:
        "Proves that quotients A/I are free R-modules when I has a unital " +
        "Gröbner basis; obtains PBW over commutative rings as a corollary.",
      tags: ["algebra", "groebner-basis", "pbw", "formalization"],
      url: "papers/unital-groebner-bases",
    }),
  ],
});
