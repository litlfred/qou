import { proposition } from "../../schema/builders";

/**
 * The Wedderburn-Artin channel decomposition of nuclear Markov traces,
 * combined with jet-descended confinement, factors the nuclear mass
 * computation into:
 *   (i)   ordering-independent symmetric + alternating scalar products
 *   (ii)  precomputed nucleon 2×2 transfer matrices (jet-descended)
 *   (iii) inter-nucleon 2×2 crossing matrices (transient, ordering-dependent)
 *
 * This reduces the ground-state ordering search from full NF recomputation
 * to a permutation of 2×2 matrix products in the standard channel only.
 */
export default proposition({
  label: "prop:nucleon-ordering-factorization",
  proofs: ["prf:nucleon-ordering-factorization"],
  title:
    "Nucleon-level ordering factorization via jet-descended confinement",
  tags: [
    "wedderburn-artin",
    "transfer-matrix",
    "ordering",
    "jet-bundle",
    "confinement",
    "groebner-shirshov",
    "optimization",
  ],
  lean: { ref: "qou:QOU.Interactions.nucleon_ordering_factorization",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-topological",
    "prop:ordering-jet-compatibility",
    "unital-groebner-bases:prop:jet-stratified-reduction",
  ],
});
