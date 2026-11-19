import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-reeb-flow-on-color-coords-remark",
  title: "Latitude, composition and the Heisenberg commutator for the q-Reeb flow",
  interprets: "def:q-reeb-flow-on-color-coords",
  uses: [
    "def:q-reeb-flow-on-color-coords",
    "def:color-sector-coords",
    "def:reeb-bundle",
    "ex:q-reeb-flow",
  ],
});
