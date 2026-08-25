import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-strand-color-winding-rigidity",
  title:
    "Rigidity of the three-strand color winding: $(\\sigma_1\\sigma_2)^3 = \\mathrm{Id}$ on the $(2,1)$ block, $q$-independently",
  lean: { ref: "qou:QOU.BraidsAndKnots.threeStrand_cubes_to_one" },
  uses: ["prop:hoefsmit-binding-amplitude", "prop:hoefsmit-toroidal-ladder-locus"],
  cites: ["jones1987", "wenzl1988c"],
  computation: {
    engine: "python",
    script:
      "computations/substrate/toroidal_level_selection_three_strand_probe.py",
    witness:
      "computations/substrate/toroidal-level-selection-three-strand-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Base ring minimised (AGENTS.md §7c).** The Lean sibling moved from " +
        "`[Field R]` + `field_simp` to a generic `[CommRing R]` with the " +
        "modulus carried as a unit `q : Units R`. The `M2` Cayley–Hamilton core was " +
        "already `CommRing`; what moved is the Hoefsmit layer. The " +
        "axial-distance quotient `a₂ = h/(1 − q⁴)` is now carried as its " +
        "defining **relation** `a₂·(1 − q⁴) = h` — the same move already used " +
        "for the binding amplitude `β` to avoid the square root — and the " +
        "axial-distance −2 entry is *derived*, `a₋₂ = −q⁴·a₂` (`axialNeg`), " +
        "with `axialNeg_rel` proving it satisfies its own relation with no " +
        "hypothesis. Consequences: the determinant identity is now " +
        "**hypothesis-free** (previously it needed four non-vanishing facts " +
        "and two `field_simp`s), and the trace needs only `IsUnit (1 − q²)`, " +
        "which is *weaker* than the previous `q ≠ 0 ∧ q⁴ ≠ 1` — so the " +
        "proposition is strictly more general than before, not less. That " +
        "hypothesis is genuine rather than technical: at `q² = 1` the " +
        "defining relation for `a₂` degenerates to `0 = 0` and constrains " +
        "nothing. `axial_eq_div` (the only field-using declaration left) " +
        "records that over a field with `1 − q⁴ ≠ 0` the relation form is " +
        "literally the classical Hoefsmit quotient.",
    },
  ],
  tags: [
    "hoefsmit",
    "three-strand",
    "color-winding",
    "zeta3",
    "torus-links",
    "cayley-hamilton",
    "level-selection",
  ],
});
