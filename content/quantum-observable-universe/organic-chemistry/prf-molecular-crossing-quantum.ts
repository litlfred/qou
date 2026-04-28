import { proof } from "../../schema/builders";

/**
 * Computational proof of `prop:molecular-crossing-quantum`.
 *
 * Witness `crossing-energy-mol.witness.json` records:
 *   - The CODATA 2018 inputs α, m_e/m_p with uncertainties.
 *   - The nuclear quantum |q+q⁻¹|_nuc = 8 MeV (manuscript value, ±12%).
 *   - The scale-separation factor α²·(m_e/m_p) ≈ 2.90×10⁻⁸.
 *   - The molecular quantum |q+q⁻¹|_mol ≈ 0.232 eV ≈ 22.4 kJ/mol.
 *   - Verification of the formula identity to 1e-9 eV.
 *   - Surfaced discrepancy with manuscript range 1–2 eV as a finding.
 *
 * Trust chain:
 *   crossing_energy_mol.py + lib/units.py + data/experimental-organic.json
 *   → crossing-energy-mol.witness.json
 *   → this proof block
 *   → prop:molecular-crossing-quantum
 */
export default proof({
  label: "prf:molecular-crossing-quantum",
  title: "Molecular crossing-energy quantum (mpmath/CODATA)",
  tags: [
    "crossing-energy",
    "molecular",
    "scale-separation",
    "verification",
    "computation",
    "mpmath",
  ],
  uses: ["prop:molecular-crossing-quantum"],
  computation: {
    engine: "mpmath",
    script: "computations/crossing_energy_mol.py",
    witness: "computations/crossing-energy-mol.witness.json",
    status: "verified",
  },
});
