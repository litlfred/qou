import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:generator-volume-decomposition",
  title:
    "Nuclear energy as a sum of generator volumes via Chebyshev recurrence",
  tags: [
    "generator-volume",
    "chebyshev",
    "hecke-algebra",
    "energy",
    "factorization",
    "braid-word",
    "nuclear",
    "binding-energy",
  ],
  lean: { ref: "qou:QOU.Descartes.generator_volume_decomposition",
    validation: "not_checked",
  },
  uses: ["thm:groebner-shirshov-energy"],
});
