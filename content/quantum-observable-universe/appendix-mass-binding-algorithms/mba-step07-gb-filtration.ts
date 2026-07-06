import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:gb-filtration",
  title: "Gröbner–Shirshov filtration / $E_2$ collapse",
  uses: [
    "prop:gb-spectral-sequence",
  ],
  computation: {
    engine: "python",
    script: "computations/gb_filtration_jet_tracker.py",
    witness: "computations/gb-filtration-jet-order.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-7",
    "gb-filtration",
    "spectral-sequence",
    "length-grading",
    "canonical-chain",
  ],
});
