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
    }),
    // Add more papers here as they are created:
    // paperRef({ dir: "fred2005", title: "Fred 2005", ... }),
  ],
});
