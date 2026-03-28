import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-braid",
  title: "Observation as an open map on the braid: intent, crossings, and input",
  tags: [
    "observation",
    "braid",
    "open-map",
    "intent",
    "crossing",
    "input",
    "turing-machine",
  ],
  uses: [
    "def:observation",
    "def:bundle-initial-conditions",
    "prop:toffoli-transfer-matrix",
    "rem:toffoli-q-and",
    "def:crossing-energy",
  ],
});
