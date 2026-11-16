import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-energy",
  label: "rem:mass-energy-not-crossing-energy",
  title: "Energy is not crossing energy",
  uses: ["def:mass-energy", "def:crossing-energy", "def:mass-identity"],
  cites: ["reshetikhin1991"],
});
