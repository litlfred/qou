import { prose } from "../../schema/builders";

export default prose({
  computation: {
    engine: "typescript",
    script: "content/pipeline/lean-stats-witness.ts",
    witness:
      "folio-assistant/computations/lean-formalization-stats.witness.json",
    status: "verified",
  },
});
