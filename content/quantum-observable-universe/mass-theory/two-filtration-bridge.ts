import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:two-filtration-bridge",
  title:
    "Two-filtration bridge: iterated-integral depth $\\leftrightarrow$ partition-cellular GB-depth via $e_\\lambda$",
  lean: { ref: "qou:QOU.BraidKnot.TwoFiltrationBridge", validation: "stub" },
  uses: ["prop:explicit-central-idempotent"],
  cites: ["bloch2000"],
  tags: [
    "tier:S",
    "two-filtration-bridge",
    "iterated-integral-depth",
    "partition-cellular-depth",
    "central-idempotent",
    "graded-mikusinski",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** The bridge map $d_{\\mathrm{II}}$ is conjectural; the\nself-conjugate $\\to$ depth-$2$ assignment is verified on the\nfigure-8 row\n([`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness));\nchiral $\\to$ depth-$3$ requires the trilog witness\n([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness))\nor a Chern–Simons computation on $3_1$ or $5_2$.\n\n**Discharge target.** Verify three rows of the prediction table at\n$n = 4$: $(2,2)$, $(3,1) + (2,1,1)$ pair, $(4) + (1,1,1,1)$ pair.\nThe first is in hand; the second requires depth-3 trilog matching;\nthe third is *the hadron orientation pair* in the QOU registry\n(proton/anti-proton bar pairing).",
    },
  ],
});
