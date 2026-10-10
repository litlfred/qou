import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bar-involution-properties",
  interprets: "def:bar-involution",
  title:
    "Bar-involution: the $P_{\\mathrm{avg}}$ / $P_{\\mathrm{skew}}$ canonical projections and the QOU bar-type classification",
  uses: [
    "def:bar-involution",
    "prop:c5-involution-leibniz-decomposition",
    "prop:silver-ratio-beta-decay-null",
    "def:categorical-q-reeb-flow",
    "prop:chirality-residue-mass-term",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "categorical-action",
    "notation",
    "classification",
  ],
});
