import { proposition } from "../../schema/builders";

/**
 * The force-carrier intertwining correspondence: a torus-knot force
 * carrier T_{p,q} (genus-4-saturating per prop:force-carrier-bring-uniqueness)
 * applied via Hecke action to an n-strand molecular braid has its
 * dominant Wedderburn weight on the partition λ = (p, 1, ..., 1) —
 * one part of size p and (n-p) ones.
 *
 * For the H_2 molecular bound state (n=4):
 *   - T_{2,9} → λ = (2, 1, 1)   [2-strand intertwining + 2 free strands]
 *   - T_{3,5} → λ = (3, 1)      [3-strand intertwining + 1 free strand]
 *
 * The transpose pair (3,1) ↔ (2,1,1) reflects Frobenius-self-duality
 * of parity-symmetric bound states (Hopf antipode V_λ ↔ V_λ^T).
 *
 * Verified computationally: delta-q-decoration.witness.json shows
 * the dominant non-trivial channels of the H_2 molecular braid are
 * exactly (3,1) and (2,1,1), with zero at (2,2) (structurally
 * explained: a single T_{2,9} insertion cannot intertwine two
 * simultaneous disjoint pairs).
 *
 * This is the round-18 reframing of conj:e-hartree-categorical-derivation
 * (after the user-supplied "intertwining" insight reframed round-17's
 * apparent falsification as a confirmation on the correct partitions).
 */
export default proposition({
  label: "prop:force-carrier-intertwining-correspondence",
  title:
    "Force carrier $T_{p,q}$ acting on $n$-strand braid lands on Wedderburn channel $\\lambda = (p, 1^{n-p})$",
  uses: [
    "def:delta-q-decoration",
    "prop:force-carrier-bring-uniqueness",
    "prop:em-coupling-projection",
    "prop:h2-lp-dual-binding",
    "conj:e-hartree-categorical-derivation",
  ],
  tags: [
    "force-carrier",
    "intertwining",
    "wedderburn-channel",
    "frobenius-self-dual",
    "hecke-algebra",
    "torus-knot",
    "bound-state",
    "alpha-em",
  ],
});
