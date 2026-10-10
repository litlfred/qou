import { remark } from "../../schema/builders";

/**
 * Net-emission ledger for the assembly spine: released binding energy as a
 * photon (categorical) + phonon (archimedean) split. Cardinality robust
 * (normal-form crossing change); absolute energy partition pending the
 * lateral-π overlap weight. WS-D, D5 (partial ledger).
 */
export default remark({
  label: "rem:assembly-emission-ledger",
  title: "Net-emission ledger: photon (categorical) and phonon (archimedean)",
  interprets: "prop:co-lp-dual-binding",
  uses: [
    "rem:benzene-assembly-spine",
    "rem:trivial-knot-photon-interpretation",
    "def:embeddable-knot-operator",
  ],
  tags: [
    "assembly-spine",
    "net-emission",
    "photon",
    "phonon",
    "ledger",
    "binding-energy",
  ],
});
