import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-braid",
  title: "Observation as an open map: crossing injection and input",
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
    "rem:toffoli-q-and",
  ],
});
