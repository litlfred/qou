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
  uses: ["conj:classical-limit-stpart"],
  cites: ["robinson1966", "ehrlich2012"],
});
