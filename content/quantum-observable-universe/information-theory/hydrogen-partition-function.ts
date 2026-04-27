import { example } from "../../schema/builders";

export default example({
  label: "ex:hydrogen-partition-function",
  title: "Partition function for monatomic hydrogen",
  tags: [
    "hydrogen",
    "partition-function",
    "statistical-mechanics",
    "knot-gas",
    "borromean",
  ],
  uses: ["prop:quantum-ideal-gas-law"],
});
