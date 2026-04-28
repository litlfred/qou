import { proof } from "../../schema/builders";

export default proof({
  label: "prf:benzene-resonance-from-threading",
  title: "Benzene resonance from threading link (sympy)",
  tags: [
    "benzene",
    "resonance",
    "threading",
    "verification",
    "computation",
    "sympy",
  ],
  uses: ["cor:benzene-resonance-from-threading"],
  computation: {
    engine: "sympy",
    script: "computations/benzene_resonance_alexander.py",
    witness: "computations/benzene-resonance-alexander.witness.json",
    status: "verified",
  },
});
