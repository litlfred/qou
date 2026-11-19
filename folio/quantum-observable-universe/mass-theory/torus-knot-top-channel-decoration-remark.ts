import { remark } from "../../schema/builders";

export default remark({
  label: "rem:torus-knot-top-channel-decoration-remark",
  title: "Braid-index condition and comparison with the q-dimension decoration",
  interprets: "def:torus-knot-top-channel-decoration",
  uses: [
    "def:torus-knot-top-channel-decoration",
    "def:delta-q-decoration",
  ],
});
