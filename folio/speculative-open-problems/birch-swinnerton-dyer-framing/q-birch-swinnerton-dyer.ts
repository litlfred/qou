import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-birch-swinnerton-dyer",
  title: "Speculative $q$-deformed Birch and Swinnerton-Dyer conjecture",
  lean: {
    ref: "qou:QOU.Observations.QBirchSwinnertonDyer",
    validation: "stub",
  },
  uses: [
    "quantum-observable-universe:def:categorical-mordell-weil",
  ],
  cites: ["tate1974"],
  tags: [
    "tier:famous",
    "birch-swinnerton-dyer",
    "elliptic-curve",
    "l-function",
    "millennium",
  ],
});
