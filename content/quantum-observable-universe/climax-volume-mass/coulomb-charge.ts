import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Corrected.** The crossing-energy decomposition in this block had the " +
        "$(n_+ \\pm n_-)$ multiplicities exchanged between the bar-even and " +
        "bar-odd channels, so it reconstructed $n_+q + n_-q^{-1}$ instead of " +
        "$n_+q - n_-q^{-1}$ — residual $2n_-/q$, i.e. the sign was dropped on " +
        "every negative crossing. It agreed with the definition **iff " +
        "$n_- = 0$**, which is why the quoted $\\tanh(\\ln q) \\approx 0.104$ " +
        "spot-check passed: every spot-check in the corpus was chirally pure. " +
        "The corrected split matches the already-canonical sibling " +
        "`observations/crossing-energy-decomposition.md` and its sorry-free Lean " +
        "`QOU.Braiding.crossingEnergy_split`; verified symbolically to residual 0 " +
        "and pinned as registry entry `R1-em-coulomb-decomposition-corrected`. " +
        "Consequence carried into the prose: $Q$ scales the bar-even channel, not " +
        "the bar-odd one, so the former identification of the bar-odd term as the " +
        "electromagnetic correction is withdrawn pending an author call.",
      see: "docs/audits/2026-08-08-convention-slip-class-sweep-force-channels.md",
    },
  ],
  label: "def:coulomb-charge",
  title: "Coulomb charge of a knot composite",
  tags: ["coulomb", "charge", "crossing", "asymmetry", "skein"],
  lean: { ref: "qou:QOU.Braiding.CoulombCharge",
    validation: "not_checked",
  },
  uses: [
    "def:crossing-energy",
  ],
});
