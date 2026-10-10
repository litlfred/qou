import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-pressure",
  label: "rem:quantum-pressure-interpretation",
  title: "Pressure from Frobenius pairing, not billiard balls",
  tags: [
    "pressure",
    "frobenius",
    "boundary",
    "q-anomaly",
    "classical-comparison",
  ],
  uses: ["def:quantum-pressure"],
});
