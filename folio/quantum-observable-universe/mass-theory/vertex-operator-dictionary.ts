import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:vertex-operator",
  label: "rem:vertex-operator-dictionary",
  title: "VOA--QOU dictionary",
  uses: [
    "def:reeb-bundle",
    "def:recursive-brane-tower",
    "rem:observation-fermion-action",
  ],
  tags: [
    "vertex-operator", "VOA", "dictionary",
    "conformal-weight", "central-charge", "interpretation",
  ],
  cites: ["frenkel2004"],
});
