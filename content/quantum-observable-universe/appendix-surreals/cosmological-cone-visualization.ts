import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:bigbang-heatdeath",
  label: "rem:cosmological-cone-visualization",
  title: "Cosmological-cone visualization of the $q$-parameter axis",
  tags: [
    "visualization",
    "cosmological-cone",
    "bigbang",
    "heatdeath",
    "exceptional-divisor",
    "reeb-bundle",
    "coral-sectors",
    "schematic",
  ],
  uses: [
    "prop:bigbang-heatdeath",
    "def:exceptional-divisor",
    "def:coral-sector-coords",
    "def:substrate-parameter",
  ],
});
