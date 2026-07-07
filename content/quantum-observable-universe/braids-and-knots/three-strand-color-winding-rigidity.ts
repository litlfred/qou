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
