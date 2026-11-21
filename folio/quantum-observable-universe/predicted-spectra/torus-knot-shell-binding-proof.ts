import { proof } from "../../schema/builders";

export default proof({
  label: "prf:torus-knot-shell-binding",
  title: "Proof of shell binding from the torus knot hierarchy",
  uses: ["prop:torus-knot-shell-binding", "def:inter-shell-operator", "def:chebyshev-torus-coefficients"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Construction rules for nuclear shells from the torus knot hierarchy](#rem:shell-construction-rules); [Magic numbers $\\mathfrak{M} = \\{2, 8, 20, 28, 50, 82, 126\\}$ as ranks of $S_5$-stable Bring period sub-lattices](#conj:magic-numbers-bring))" },
  ],
});
