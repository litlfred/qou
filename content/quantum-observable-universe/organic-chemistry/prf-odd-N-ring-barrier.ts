import { proof } from "../../schema/builders";

export default proof({
  label: "prf:odd-N-ring-barrier",
  title: "Odd-$N$ ring closure barriers from $T(2,N)$ torus knots (sympy)",
  tags: [
    "odd-N",
    "torus-knot",
    "barrier",
    "verification",
    "computation",
    "sympy",
  ],
  uses: [
    "prop:odd-N-ring-barrier",
    "def:torus-knot-T2-odd-alexander",
  ],
  computation: {
    engine: "sympy",
    script: "computations/torus_knot_T2_odd.py",
    witness: "computations/torus-knot-T2-odd.witness.json",
    status: "verified",
  },
});
