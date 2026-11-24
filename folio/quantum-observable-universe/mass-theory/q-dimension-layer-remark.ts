import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dimension-layer-remark",
  title: "What the q-dimension layer retains",
  interprets: "def:q-dimension-layer",
  uses: [
    "def:q-dimension-layer",
    "def:delta-q-decoration",
  ],
});
