import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cl3-zeta5-geometric-realization",
  title:
    "Geometric realisation of $\\mathrm{Cl}_3(2\\pi/5)$ as a Bring-natural depth-3 invariant",
  lean: { ref: "qou:QOU.BraidKnot.Cl3Zeta5GeometricRealization", validation: "stub" },
  uses: [
    "prop:bring-trilog-depth-3-witness",
    "prop:gb-depth-period-correspondence",
    "prop:joint-galois-braid-action",
    "rem:bring-embeddable-knots",
    "rem:transcendental-accounting",
  ],
  cites: ["bloch2000", "kontsevich1995", "zagier1986"],
  tags: [
    "depth-3",
    "Cl_3",
    "zeta-5",
    "bring",
    "S5-symmetry",
    "hyperbolic-4-manifold",
    "chern-simons",
    "moduli-space-iterated-integral",
    "graded-mikusinski",
    "open-problem",
  ],
});
