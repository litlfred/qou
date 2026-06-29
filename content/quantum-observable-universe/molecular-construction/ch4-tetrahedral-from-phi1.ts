import { remark } from "../../schema/builders";

/**
 * Interpretive follow-on to def:ch4-molecular-braid: the tetrahedral S₄
 * geometry of methane derived from Φ₁ minimisation over strand orderings
 * (maximising H separation), with the observed per-bond D₀ ≈ 4.48 eV.
 */
export default remark({
  label: "rem:ch4-tetrahedral-from-phi1",
  title: "Tetrahedral geometry of methane from $\\Phi_1$ minimisation",
  interprets: "def:ch4-molecular-braid",
  uses: ["def:ch4-molecular-braid"],
  tags: ["methane", "CH4", "tetrahedral", "S4", "Phi1", "bond-energy"],
});
