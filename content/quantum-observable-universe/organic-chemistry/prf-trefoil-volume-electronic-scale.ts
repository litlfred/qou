import { proof } from "../../schema/builders";

/**
 * Computational proof of `lem:trefoil-volume-electronic-scale`.
 *
 * Witness `crossing-energy-mol-direct.witness.json` records the
 * mpmath-precision (dps = 60) substrate q from Vol(4_1), the
 * trefoil's Alexander polynomial Δ_{3_1}(q) = q² − 1 + q⁻²
 * evaluated at q_0, and the agreement of the high-precision
 * |q+q⁻¹|_mol with the float-precision C1 value to ≤ 1e-9 eV.
 *
 * Trust chain:
 *   crossing_energy_mol_direct.py + q_parameter.py + lib/alexander.py
 *   → crossing-energy-mol-direct.witness.json
 *   → this proof block
 *   → lem:trefoil-volume-electronic-scale
 */
export default proof({
  label: "prf:trefoil-volume-electronic-scale",
  title: "Trefoil-Alexander electronic-scale cross-check (mpmath dps 60)",
  tags: [
    "trefoil",
    "alexander-polynomial",
    "high-precision",
    "verification",
    "computation",
    "mpmath",
  ],
  uses: ["lem:trefoil-volume-electronic-scale"],
  computation: {
    engine: "mpmath",
    script: "computations/crossing_energy_mol_direct.py",
    witness: "computations/crossing-energy-mol-direct.witness.json",
    status: "verified",
  },
});
