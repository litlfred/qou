import { remark } from "../../schema/builders";

export default remark({
  label: "rem:positron-knot-remark",
  title: "The positron as the electron's antiparticle",
  interprets: "def:positron-knot",
  tags: ["positron", "antiparticle"],
  uses: [
    "def:positron-knot",
    "def:electron-knot",
    "def:down-quark",
    "def:coulomb-charge",
  ],
});
