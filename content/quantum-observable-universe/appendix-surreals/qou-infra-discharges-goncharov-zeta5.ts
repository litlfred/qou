import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-infra-discharges-goncharov-zeta5",
  title:
    "QOU's Hecke-NF + Bring-$S_5$ infrastructure discharges Goncharov's depth-3 conjecture at $F = \\mathbb{Q}(\\zeta_5)$",
  lean: { ref: "qou:QOU.AppendixSurreals.QouInfraDischargesGoncharovZeta5", validation: "stub" },
  uses: [
    "prop:depth-2-identification-bloch-suslin",
    "rem:conway-kt-vol-injectivity-test",
  ],
  cites: ["bloch2000", "kontsevich1995", "zagier1986"],
  tags: [
    "tier:famous",
    "goncharov-conjecture",
    "depth-3",
    "bring-S5",
    "hecke-NF",
    "qou-infra-program",
    "graded-mikusinski",
    "research-program",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** Both avenues require non-trivial new computation:\n\n- Avenue A: need to enumerate Jones-coincident pairs in the\n  Bring-embeddable class. The recursive atom-knot atlas already\n  has the braid words; the Hecke NF reduction would highlight\n  pairs with identical NF tail but different head. The\n  Anstee–Przytycki–Rolfsen 1989 construction provides explicit\n  examples to start from.\n- Avenue B: need to express the Goncharov 22-term relation at\n  $\\zeta_5$ as a Markov trace of an explicit Hecke element. The\n  key technical step is identifying the right $H_n(q)$ and the\n  The right braid word.\n\nBoth are concrete projects of approximately 1–2 weeks of focused\nwork for a contributor familiar with both QOU's Hecke / NF\ninfrastructure and Goncharov's depth-3 polylogarithm machinery.",
    },
  ],
});
