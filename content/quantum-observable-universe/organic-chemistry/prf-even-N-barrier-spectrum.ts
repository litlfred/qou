import { proof } from "../../schema/builders";

export default proof({
  label: "prf:even-N-barrier-spectrum",
  title: "Linear-in-$N$ trend of even-$N$ barriers (least-squares fit)",
  tags: [
    "even-N",
    "barrier",
    "linear-fit",
    "verification",
    "computation",
    "sympy",
  ],
  uses: ["prop:even-N-barrier-spectrum"],
  computation: {
    engine: "sympy",
    script: "computations/even_N_ring_spectrum.py",
    witness: "computations/even-N-ring-spectrum.witness.json",
    status: "verified",
  },
});
