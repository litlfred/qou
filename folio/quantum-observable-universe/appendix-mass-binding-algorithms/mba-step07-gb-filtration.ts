import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:gb-filtration",
  title: "Gröbner–Shirshov Coxeter-length filtration and $E_2$ spectral-sequence collapse",
  uses: [
    "prop:gb-spectral-sequence",
  ],
  tags: [
    "mba",
    "step-7",
    "gb-filtration",
    "spectral-sequence",
    "length-grading",
    "canonical-chain",
  ],
});
