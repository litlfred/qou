import { prose } from "../../schema/builders";

export default prose({
  label: "tm-interactions",
  title: "Interaction and decay matrices",
  uses: [
    "def:transfer-matrix-operator",
    "prop:beta-decay-transfer-matrix",
  ],
  tags: [
    "transfer-matrix",
    "beta-decay",
    "interaction",
    "delta-operator",
    "toffoli",
    "appendix",
  ],
});
