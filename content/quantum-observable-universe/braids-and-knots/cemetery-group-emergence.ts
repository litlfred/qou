import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cemetery-group-emergence",
  title:
    "Cemetery group as the kernel of the observation functor",
  uses: [
    "def:cemetery-group",
    "def:observation",
    "conj:crystal-graph-realization",
    "conj:gs-spectral-sum-finite",
  ],
  cites: [
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "cemetery-group",
    "decoupling",
    "homological-filter",
    "kill-switch",
    "computational-shortcut",
  ],
});
