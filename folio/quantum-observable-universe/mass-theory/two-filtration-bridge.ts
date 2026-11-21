import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:two-filtration-bridge",
  title:
    "Two-filtration bridge: iterated-integral depth $\\leftrightarrow$ partition-cellular GB-depth via $e_\\lambda$",
  lean: { ref: "qou:QOU.BraidKnot.TwoFiltrationBridge", validation: "stub" },
  uses: ["prop:explicit-central-idempotent", "prop:cellular-depth-filtration"],
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (attributed to\n  [curvature-rank GB stratification](#prop:curvature-rank-gb-stratification),\n  [stratified $\\Phi_q$](#conj:quantum-dilogarithm-stratified) — but the\n  first stratifies by the curvature rank of **words** and supplies no\n  partition-indexed filtration, so this conjecture **presupposes** the very\n  word-to-partition step that is unestablished)," },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([depth correspondence](#conj:gb-depth-period-correspondence))" },
    { kind: "status", date: "2026-11-16", body: "2026-11-16: the max-hook statistic used here is renamed max-hook depth; GB-depth now means Lusztig's a-function (owner choice). The empty 'otherwise' branch is noted, the (4) row is corrected (it is half of the chiral pair {(4),(1^4)}, so the formula gives 3), and the period column is marked as comparison. Proved core: prop:cellular-depth-filtration." },
    {
      kind: "status",
      body: "**Open.** The bridge map $d_{\\mathrm{II}}$ is conjectural; the\nself-conjugate $\\to$ depth-$2$ assignment is verified on the\nfigure-8 row\n([`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness));\nchiral $\\to$ depth-$3$ requires the trilog witness\n([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness))\nor a Chern–Simons computation on $3_1$ or $5_2$.\n\n**Discharge target.** Verify three rows of the prediction table at\n$n = 4$: $(2,2)$, $(3,1) + (2,1,1)$ pair, $(4) + (1,1,1,1)$ pair.\nThe first is in hand; the second requires depth-3 trilog matching;\nthe third is *the hadron orientation pair* in the QOU registry\n(proton/anti-proton bar pairing).",
    },
  ],
});
