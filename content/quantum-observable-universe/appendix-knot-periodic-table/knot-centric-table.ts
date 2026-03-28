import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:nuclear-shell-intruder",
  label: "rem:knot-centric-table",
  title:
    "Knot-centric periodic table: reorganization by nuclear and electronic knot structure",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "nuclear-shell",
    "electron-shell",
    "borromean",
    "intruder",
    "todo",
  ],
  uses: [
    "prop:nuclear-shell-intruder",
    "rem:hydrogen-orbitals",
    "def:borromean-baryon",
    "conj:electron-shells-hopf",
    "prop:orbital-fourier-decomposition",
    "def:substrate-parameter",
    "prop:local-substrate-q",
  ],
});
