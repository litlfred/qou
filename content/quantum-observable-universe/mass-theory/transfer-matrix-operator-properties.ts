import { remark } from "../../schema/builders";

export default remark({
  label: "rem:transfer-matrix-operator-properties",
  interprets: "def:transfer-matrix-operator",
  title:
    "Action on the GS ideal, operator algebra, interaction catalogue, and composition rules",
  tags: [
    "transfer-matrix",
    "operator",
    "hecke-algebra",
    "groebner",
    "hadron",
    "knot",
    "crossing",
    "universal",
    "interaction",
  ],
  uses: [
    "def:transfer-matrix-operator",
    "prop:beta-decay-transfer-matrix",
  ],
});
