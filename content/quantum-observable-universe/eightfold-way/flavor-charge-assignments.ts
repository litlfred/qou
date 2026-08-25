import { remark } from "../../schema/builders";

/**
 * The flavor charge assignments (I₃, Y) from the A₂ weight lattice.
 *
 * Connects the hexagonal weight lattice of §1 to the physical
 * quantum numbers. The isospin I₃ is the writhe-derived invariant
 * (proved). The hypercharge Y is the open problem: requires a second
 * crossing invariant (ribbon twist candidate identified but untested).
 *
 * ANTI-FITTING: States the open problem honestly. Does NOT import
 * Y from external sources. The Gell-Mann–Nishijima relation is
 * a consistency battery, not an axiom.
 */
export default remark({
  label: "rem:flavor-charge-assignments",
  title: "Flavor charge assignments and the hypercharge gap",
  interprets: "prop:a2-from-three-strands",
  uses: [
    "prop:a2-from-three-strands",
    "def:coulomb-charge",
    "conj:sm-hypercharge-invariant",
  ],
});
