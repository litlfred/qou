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
    "def:surreal-blowup-calculus",
    "conj:classical-limit-stpart",
    "conj:infinitesimal-frobenius",
    "conj:infinitesimal-observability",
    "conj:vacuum-epsilon",
    "rem:fibre-functor-rigidity",
  ],
  cites: ["robinson1966", "ehrlich2012"],
});
