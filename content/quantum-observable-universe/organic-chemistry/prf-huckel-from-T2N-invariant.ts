import { proof } from "../../schema/builders";

export default proof({
  label: "prf:huckel-from-T2N-invariant",
  title: "Hückel 4n+2 rule from $T(2,N)$ invariants — empirical bridge",
  tags: [
    "huckel",
    "4n+2",
    "aromaticity",
    "T2N",
    "verification",
    "computation",
    "sympy",
    "conjectural",
  ],
  uses: ["conj:huckel-from-T2N-invariant"],
  computation: {
    engine: "sympy",
    script: "computations/huckel_bridge.py",
    witness: "computations/huckel-bridge.witness.json",
    status: "verified",
  },
});
