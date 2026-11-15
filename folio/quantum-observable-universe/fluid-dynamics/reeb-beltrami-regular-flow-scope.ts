import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:reeb-beltrami-regular-flow",
  label: "rem:reeb-beltrami-regular-flow-scope",
  title: "Scope of the regular fibre-rotation flow",
  uses: [
    "prop:reeb-beltrami-regular-flow",
    "def:reeb-bundle",
    "ex:torus-ns-regular",
  ],
  tags: ["navier-stokes", "regularity", "scope", "reeb", "descartes"],
});
