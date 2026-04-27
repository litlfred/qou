import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-temperature",
  label: "rem:quantum-temperature-interpretation",
  title: "Temperature as tick rate and surface quantity",
  tags: [
    "temperature",
    "reeb-flow",
    "holographic",
    "non-abelian-stokes",
    "classical-limit",
  ],
  uses: ["def:quantum-temperature"],
});
