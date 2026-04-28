import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-volume",
  title: "Quantum volume",
  tags: [
    "volume",
    "statistical-mechanics",
    "categorical-volume",
    "s3-fibre",
    "reeb-bundle",
  ],
  lean: { ref: "qou:QOU.Information.quantumVolume",
    validation: "not_checked",
  },
  uses: ["def:reeb-bundle"],
});
