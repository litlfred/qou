import { definition } from "../../schema/builders";

export default definition({
  label: "def:one-dim-qou-channel",
  title: "One-dimensional QOU channel (optical fibre)",
  lean: { ref: "qou:QOU.Information.OneDimChannel", validation: "not_checked" },
  authorNotes: [
    { kind: "note", body: "Lean sibling: structural, over a generic commutative ring $R$." },
  ],
  uses: [],
  tags: [
    "optical-fibre",
    "1d-channel",
    "braid-carrier",
    "markov-trace",
    "information-theory",
  ],
});
