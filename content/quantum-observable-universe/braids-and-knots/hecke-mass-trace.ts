import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-mass-trace",
  title: "Mass via the Markov trace of the Hecke mass element",
  tags: [
    "hecke-algebra",
    "mass",
    "markov-trace",
    "fibre-functor",
    "topological-decomposition",
  ],
  lean: { ref: "qou:QOU.Braiding.hecke_mass_trace",
    validation: "not_checked",
  },
  uses: ["def:hecke-mass-element"],
});
