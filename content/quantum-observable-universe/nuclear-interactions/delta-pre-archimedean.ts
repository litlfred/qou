import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:delta-pre-archimedean",
  title:
    "Difference observables are formed pre-archimedean: fold commutes " +
    "with the delta, the archimedean realisation does not",
  lean: {
    ref: "qou:QOU.ParticleInteractions.fold_commutes_sub",
  },
  uses: [
    "prop:neutron-qvalue-symbolic",
    "def:archimedean-realization-functor",
  ],
  cites: ["kassel1995"],
  tags: [
    "archimedean-functor",
    "bar-involution",
    "binding-energy",
    "q-beta",
    "order-of-operations",
    "fibre-vs-observable",
  ],
});
