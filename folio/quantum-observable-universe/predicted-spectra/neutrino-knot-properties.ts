import { remark } from "../../schema/builders";

export default remark({
  label: "rem:neutrino-knot-properties",
  title: "Properties of the neutrino unknot",
  interprets: "def:neutrino-knot",
  tags: ["neutrino", "unknot"],
  uses: [
    "def:neutrino-knot",
    "prop:torus-knot-generators",
  ],
});
