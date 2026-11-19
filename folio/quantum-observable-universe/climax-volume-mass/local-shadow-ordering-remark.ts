import { remark } from "../../schema/builders";

export default remark({
  label: "rem:local-shadow-ordering-remark",
  title: "Reading of the local shadow-price ordering",
  interprets: "def:local-shadow-ordering",
  uses: [
    "def:local-shadow-ordering",
    "def:unstable-atom",
  ],
});
