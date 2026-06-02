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
    script: "tools/qou-substrate/python/qou_substrate/witness.py",
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
