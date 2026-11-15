import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:hochschild-kummer-connection",
  title: "The Hochschild--Kummer connection",
  tags: [
    "kummer",
    "hochschild",
    "hkr",
    "deformation",
    "obstruction",
    "motivic-galois",
  ],
  uses: [
    "def:hochschild-homology",
    "def:quantum-characteristic-classes",
    "def:motivic-substrate",
  ],
  cites: ["yekutieli2010"],
});
