import { proof } from "../../schema/builders";

export default proof({
  label: "prf:heteroaromatic-alexander",
  title:
    "Heteroaromatic Alexander invariance — empirical verification (sympy)",
  tags: [
    "heteroaromatic",
    "alexander-polynomial",
    "verification",
    "computation",
    "sympy",
    "conjectural",
  ],
  uses: ["conj:heteroaromatic-alexander"],
  computation: {
    engine: "sympy",
    script: "computations/pyridine_furan_alexander.py",
    witness: "computations/pyridine-furan-alexander.witness.json",
    status: "verified",
  },
});
