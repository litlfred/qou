import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-operator-energy-remark",
  title: "Subtrahend and value ranges of the knot operator energy",
  interprets: "def:knot-operator-energy",
  uses: [
    "def:knot-operator-energy",
    "def:stable-atom",
    "prop:operator-selection-lp",
  ],
});
