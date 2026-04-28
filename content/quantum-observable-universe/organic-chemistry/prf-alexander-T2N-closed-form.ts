import { proof } from "../../schema/builders";

/**
 * Computational proof of `lem:alexander-T2N-closed-form`.
 *
 * Witness `alexander-T2N.witness.json` records the symbolic Alexander
 * polynomial Δ_{T(2,N)}(q) for N = 2,…,12, the symbolic limit Δ(1),
 * the per-atom limit Δ(1)/N, and verifies the defining identity
 *     (q ∓ q⁻¹) · Δ == q^m ∓ q^{-m}
 * for each N.
 *
 * Trust chain:
 *   alexander_T2N.py + lib/alexander.py
 *   → alexander-T2N.witness.json
 *   → this proof block
 *   → lem:alexander-T2N-closed-form
 */
export default proof({
  label: "prf:alexander-T2N-closed-form",
  title: "Closed-form Alexander polynomial of $T(2,N)$ (symbolic)",
  tags: [
    "alexander-polynomial",
    "torus-link",
    "verification",
    "computation",
    "sympy",
  ],
  uses: ["lem:alexander-T2N-closed-form"],
  computation: {
    engine: "sympy",
    script: "computations/alexander_T2N.py",
    witness: "computations/alexander-T2N.witness.json",
    status: "verified",
  },
});
