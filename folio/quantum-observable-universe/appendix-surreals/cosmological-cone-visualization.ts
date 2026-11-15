import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:bigbang-heatdeath",
  label: "rem:cosmological-cone-visualization",
  title: "Cosmological-cone visualization of the $q$-parameter axis",
  tags: [
    "visualization",
    "cosmological-cone",
    "big-bang",
    "heat-death",
    "exceptional-divisor",
    "reeb-bundle",
    "color-sectors",
    "schematic",
  ],
  uses: [
    "conj:bigbang-heatdeath",
    "def:exceptional-divisor",
    "def:color-sector-coords",
    "def:substrate-parameter",
  ],
});
