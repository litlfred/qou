import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-filtration-bridge",
  title:
    "Two-filtration bridge: iterated-integral depth $\\leftrightarrow$ partition-cellular GB-depth via $e_\\lambda$",
  lean: { ref: "qou:QOU.BraidKnot.TwoFiltrationBridge", validation: "stub" },
  uses: ["prop:explicit-central-idempotent"],
  cites: ["bloch2000"],
  tags: [
    "two-filtration-bridge",
    "iterated-integral-depth",
    "partition-cellular-depth",
    "central-idempotent",
    "graded-mikusinski",
    "open-problem",
  ],
});
