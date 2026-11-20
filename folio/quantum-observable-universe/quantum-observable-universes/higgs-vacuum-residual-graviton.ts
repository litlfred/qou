import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:higgs-vacuum-residual-idempotent",
  label: "rem:higgs-vacuum-residual-graviton",
  title: "Graviton candidate 3: the symmetric square of the Higgs-vacuum residual",
  uses: [
    "prop:higgs-vacuum-residual-idempotent",
    "conj:mass-endomorphism",
    "conj:g-action-on-substrate",
  ],
  tags: ["graviton", "categorical-higgs", "residual", "interpretation", "open-problem"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body: "Item 4 previously recorded a mismatch: (G-4) assigned the trace $[2]_q$ to $e_H$. Resolved by owner ruling 2026-11-20, which corrected (G-4) to $\\mathrm{tr}_F(e_H) = 1$ (Lean `VacuumPairing.tr_proj_eq_one`). See the matching note on `conj:g-action-on-substrate`.",
    },
  ],
});
