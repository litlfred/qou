import { proof } from "../../schema/builders";

/**
 * Computational proof of `lem:T2N-components`.
 *
 * Witness `T2N-component-count.witness.json` records the component
 * count, braid-word and minimal-diagram crossing counts, writhe, and
 * signature of T(2, N) for N = 2,…,12.
 *
 * Trust chain:
 *   T2N_component_count.py
 *   → T2N-component-count.witness.json
 *   → this proof block
 *   → lem:T2N-components
 */
export default proof({
  label: "prf:T2N-components",
  title: "Component count, writhe, signature of $T(2,N)$",
  tags: [
    "torus-link",
    "components",
    "writhe",
    "signature",
    "verification",
    "computation",
  ],
  uses: ["lem:T2N-components"],
  computation: {
    engine: "sympy",
    script: "computations/T2N_component_count.py",
    witness: "computations/T2N-component-count.witness.json",
    status: "verified",
  },
});
