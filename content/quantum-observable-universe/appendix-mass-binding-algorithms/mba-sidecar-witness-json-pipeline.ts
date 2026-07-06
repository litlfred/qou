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
  authorNotes: [
    {
      kind: "status",
      body: "Not every `*.witness.json` currently under\n`computations/` conforms to the `WitnessBuilder`\nshape above — legacy scripts emitted hand-shaped JSON\n(e.g. `name` / `timestamp` / `git_sha`) before `WitnessBuilder`\nexisted. The migration is tracked under the \"P30 wrap-legacy\"\ndiscipline noted in [`compute-audit.md`](../../../.claude/skills/local/compute-audit.md);\nthe contract above applies in full to **WitnessBuilder-backed\nwitnesses** and is the target shape for the migration of legacy\nwitnesses.",
    },
  ],
});
