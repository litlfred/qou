import { conjecture } from "../../schema/builders";

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
export default conjecture({
  label: "conj:force-carrier-intertwining-correspondence",
  lean: { ref: "qou:QOU.BraidKnot.force_carrier_intertwining_correspondence" },
  title:
    "Force carrier $T_{p,q}$ acting on $n$-strand braid lands on Wedderburn channel $\\lambda = (p, 1^{n-p})$",
  uses: ["conj:e-hartree-categorical-derivation"],
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
  authorNotes: [
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:force-carrier-intertwining-correspondence` (owner, #8526, 2026-11-21; bean qou-tm3c). The claim that a torus-knot carrier $T_{p,q}$ puts the dominant non-trivial Wedderburn weight of an $n$-strand braid on $(p, 1^{n-p})$ rests on the $n = 4$ computation only, and 'dominant' is not made precise. The Lean proves only that the parts of $(p, 1^{n-p})$ sum to $n$." },
  ],
});
