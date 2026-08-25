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
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — \`ℝ\` is NOT load-bearing here, and this note does not claim it is.** The class is a single \`residual : ℝ\` with \`residual_eq_zero : residual = 0\`; that holds over any type with a \`Zero\`, so nothing archimedean is used. It is left as \`ℝ\` deliberately: the file's own docstring calls the field *"a structural placeholder; refine per §3b to match the conjecture's actual content"*, and choosing a base ring for content not yet written would lock in a choice on no evidence. The real defect is the placeholder (an under-specified conjecture carrier, §3b-tax), not the base ring; fix that and the correct ring follows from it.`,
    },
    {
      kind: "note",
      date: "2026-08-21",
      body: `**Base ring (§7c) — resolved, and the note above called it correctly.** The placeholder was replaced (bean \`qou-ffwk\`) by the block's own *reduced target*: the four values \`Li₃(ζ₅ᵏ)\`, \`k = 1..4\`, span a space of rank exactly 2. The correct ring did follow from the content, and it is **\`ℚ\`, not \`ℝ\`** — the statement is \`dim_ℚ\` of a \`ℚ\`-span, matching Borel's \`dim_ℚ K₅^ind(ℚ(ζ₅)) ⊗ ℚ = 2\`. Every \`ℚ\` in \`QouInfraDischargesGoncharovZeta5.lean\` is that rationalisation.

\`ℚ\` here is **load-bearing and must not be generalised.** The rank-2 target is a statement about the rationalised K-group; over an arbitrary field the four values need not span rank 2 at all, so a generic base ring would be a different and unsupported claim. It is also not archimedean — nothing is ordered, normed, or compared against a numerical substrate value, and the module carries no real-field type of any kind.

This acknowledgement exists because \`check-base-ring\` flags bare \`ℚ\` in an algebraic-side module as a candidate de-specialisation. Here the flag is a false positive, adjudicated: the specialisation *is* the mathematics.`,
    },
    {
      kind: "status",
      body: "**Open.** Both avenues require non-trivial new computation:\n\n- Avenue A: need to enumerate Jones-coincident pairs in the\n  Bring-embeddable class. The recursive atom-knot atlas already\n  has the braid words; the Hecke NF reduction would highlight\n  pairs with identical NF tail but different head. The\n  Anstee–Przytycki–Rolfsen 1989 construction provides explicit\n  examples to start from.\n- Avenue B: need to express the Goncharov 22-term relation at\n  $\\zeta_5$ as a Markov trace of an explicit Hecke element. The\n  key technical step is identifying the right $H_n(q)$ and the\n  The right braid word.\n\nBoth are concrete projects of approximately 1–2 weeks of focused\nwork for a contributor familiar with both QOU's Hecke / NF\ninfrastructure and Goncharov's depth-3 polylogarithm machinery.",
    },
  ],
});
