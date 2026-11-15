import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ugb-main",
  title: "Proof of the main theorem",
  tags: ["groebner-basis", "freeness"],
  uses: [
    "thm:ugb-main",
    "lem:ugb-generator-choice",
    "def:remainder-modules",
  ],
});
