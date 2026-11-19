import { example } from "../../schema/builders";

export default example({
  label: "ex:o16-derived-nf",
  title: "O-16: doubly magic at $Z = N = 8$",
  interprets: "prop:nuclear-operator-regimes",
  tags: [
    "oxygen",
    "normal-form",
    "derived",
    "doubly-magic",
    "magic-number",
    "shell-closure",
    "inductive-reduction",
  ],
  uses: [
    "prop:nuclear-operator-regimes",
    "prop:inductive-gb-reduction",
    "prop:spin-orbit-magic-closures",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Updated from the 1D chain wording (15 crossings) to reflect the 3D stacked alpha-simplex coordination complex (f_1(16) = 3A - 6 = 42 edges, f_2(16) = 3A - 8 = 40 triangles, f_3(16) = A - 3 = 13 tetrahedra in QOU.Nuclear.AlphaSimplexCoordinationDerivation) and the 1s_{1/2}^2 + 1p_{3/2}^4 (Z=N=6, 12C) -> + 1p_{1/2}^2 (Z=N=8, 16O) spin-orbit shell closure proved in QOU.Nuclear.SpinOrbitShellClosureAndSymmetryEnergy.carbon12_and_oxygen16_shell_closures.",
    },
  ],
});
