import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:kummer-tower-motivic-galois",
  title: "Motivic-Galois reading of the Kummer filtration",
  tags: ["kummer", "motivic-galois", "frobenius", "perpetual-obstruction"],
  uses: [
    "def:adelic-substrate",
    "conj:motivic-perpetual-obstruction",
  ],
});
