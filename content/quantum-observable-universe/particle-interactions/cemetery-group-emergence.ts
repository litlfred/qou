import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cemetery-group-emergence",
  title:
    "Cemetery group as the kernel of the observation functor",
  lean: { ref: "qou:QOU.BraidKnot.CemeteryGroupEmergence", validation: "stub" },
  uses: [
    "def:cemetery-group",
    "prop:crystal-graph-realization",
    "prop:gs-spectral-sum-finite",
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
