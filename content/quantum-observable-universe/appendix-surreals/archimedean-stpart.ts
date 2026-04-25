import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:archimedean-stpart",
  title:
    "Archimedean QOU is the standard-part of surreal QOU",
  tags: [
    "surreal-numbers",
    "archimedean",
    "categorical",
    "standard-part",
    "QOU-axioms",
    "open-problem",
  ],
  uses: [
    "def:quantum-observable-universe",
    "def:standard-part-functor",
    "conj:classical-limit-stpart",
    "rem:fibre-functor-rigidity",
  ],
  cites: ["robinson1966", "ehrlich2012"],
});
