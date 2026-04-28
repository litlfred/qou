import { proof } from "../../schema/builders";

/**
 * Computational proof of `prop:threading-half-weight`.
 *
 * Witness `alexander-weight-ratio.witness.json` records, for every
 * even N in {2, 4, 6, 8, 10, 12, 14}, the symbolic limit of
 * Δ_{T(2,N)}(q)/N as q → 1 (always 1/2), the numerical ratio at the
 * substrate value q₀, and the leading curvature in the series
 * expansion about q = 1.
 *
 * Trust chain:
 *   alexander_weight_ratio.py + lib/alexander.py
 *   → alexander-weight-ratio.witness.json
 *   → this proof block
 *   → prop:threading-half-weight
 */
export default proof({
  label: "prf:threading-half-weight",
  title: "Threading half-weight limit (symbolic)",
  tags: [
    "threading",
    "half-weight",
    "alexander-polynomial",
    "limit",
    "verification",
    "computation",
    "sympy",
  ],
  uses: ["prop:threading-half-weight"],
  computation: {
    engine: "sympy",
    script: "computations/alexander_weight_ratio.py",
    witness: "computations/alexander-weight-ratio.witness.json",
    status: "verified",
  },
});
