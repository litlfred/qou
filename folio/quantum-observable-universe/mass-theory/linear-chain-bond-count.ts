import { proposition } from "../../schema/builders";

/**
 * The jet-filtration body-order multiplicity is the inter-nucleon BOND COUNT of
 * the linear-chain atom: M_n = n−1, and the aggregate cluster measure equals
 * C(A+1,3). Combinatorial core (Lean sorry-free); the binding magnitude that it
 * multiplies (hyperbolic link volumes × m_e) is empirical, not part of this claim.
 */
export default proposition({
  label: "prop:linear-chain-bond-count",
  title: "The jet-filtration multiplicity is the linear-chain bond count $M_n = n-1$",
  lean: {
    ref: "qou:QOU.Mass.linear_chain_cluster_measure",
    validation: "not_checked",
  },
  uses: [
    // conj:binding-manybody-eq-jet-filtration removed (qou-tm3c): the claim is the bond count n-1 and its sum C(A+1,3); the .md scopes out what the conjecture supplies.
    "prop:jet-filtration-binding-extensive",
  ],
  tags: [
    "binding",
    "jet-filtration",
    "bond-count",
    "linear-chain",
    "multiplicity",
  ],
});
