import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:witness-json-pipeline",
  title: "Witness-JSON pipeline (cross-language interchange)",
  uses: [
    "prop:operator-selection-lp",
    "prop:wedderburn-trace-identity",
  ],
  computation: {
    engine: "python+mpmath",
    script: "tools/qou-substrate/src/qou_substrate/witness_builder.py",
    status: "verified",
  },
  tags: [
    "mba",
    "sidecar",
    "witness-pipeline",
    "interchange",
    "precision-discipline",
  ],
});
