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
      url: "/viewer/#/view/quantum-observable-universe",
    }),
    paperRef({
      dir: "bach2013-double-slit",
      title: "Controlled Double-Slit Electron Diffraction",
      description:
        "Full realization of Feynman's double-slit thought experiment: " +
        "controlled single/double slit electron diffraction with " +
        "single-electron buildup (6235 events). Benchmark dataset for " +
        "the QOU two-mode scattering prediction.",
      tags: ["experimental", "double-slit", "electron-diffraction", "imported"],
      url: "/viewer/#/view/bach2013-double-slit",
    }),
    paperRef({
      dir: "unital-groebner-bases",
      title: "Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings",
      description:
        "Proves that quotients A/I are free R-modules when I has a unital " +
        "Gröbner basis; obtains PBW over commutative rings as a corollary.",
      tags: ["algebra", "groebner-basis", "pbw", "formalization"],
      url: "/viewer/#/view/unital-groebner-bases",
    }),
    paperRef({
      dir: "fred2005-formal-groups",
      title: "Integration of Skewed-Poisson Structures on Non-commutative Formal Groups",
      description:
        "Skew-Poisson integration on formal groups over Z_p: " +
        "lifts commutative formal groups to non-commutative ones via " +
        "Gröbner-Shirshov deformation and strong multiplicativity.",
      tags: ["formal-groups", "skew-poisson", "formalization"],
      url: "/viewer/#/view/fred2005-formal-groups",
    }),
    paperRef({
      dir: "visualizer",
      title: "QOU Visualizer",
      description:
        "Interactive views of QOU content — Bring's surface, " +
        "knot complements (SnapPea), and dependency graphs.",
      tags: ["visualizer", "snappea", "interactive"],
    }),
  ],
});
