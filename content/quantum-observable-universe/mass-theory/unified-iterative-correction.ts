import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unified-iterative-correction",
  title:
    "Unified iterative LP-dual correction: per-step Wedderburn " +
    "projection over all partitions $\\lambda \\vdash k$ for " +
    "$k = 2, \\ldots, K$, starting at $A = 1$ (no special cases)",
  lean: { ref: "qou:QOU.Archimedean.ConfinedKnotBinding.Unified.unified_iterative_correction",
    validation: "not_checked",
  },
  uses: [
    "prop:wigner-np-pairing",
    "prop:mass-coefficient-shadow-price",
    "def:q-resolvent",
  ],
  cites: [
    "kerov1996",
    "feray-meliot2012",
    "satula1997",
  ],
  tags: [
    "wigner-energy",
    "iterative-correction",
    "partition-22",
    "q-hook-walk",
    "binding",
    "restartable-witness",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-12",
      body:
        "**Statement re-aligned to the producer under the owner's ruling of " +
        "2026-09-12** — verbatim, *\"resolve functionals ... what lean provable\"*. " +
        "PR #7230 measured that this block and " +
        "`hecke_core_legacy.unified_iterative_correction` described different " +
        "functionals and deliberately left the choice open. Three divergences " +
        "were resolved against the block, each on a corpus artifact rather than " +
        "on a residual: (i) `u_λ` was called *\"its Frobenius positivity LP " +
        "shadow price\"* — refuted by `QOU.ParticleInteractions." +
        "y_0_eq_zero_of_radical` (sorry-free) and by " +
        "`prop:mass-coefficient-shadow-price`, corrected 2026-08-25 / 2026-09-05; " +
        "(ii) the q-Laplacian resolvent `ρ_λ(s_*)` the producer applies was " +
        "absent — deleting it moves the total by 4.12× at A=2 and 9.87× at A=4, " +
        "so it is not a rounding; (iii) *\"strictly over all λ\"* did not " +
        "describe the gated sum the producer computes, a factor 4.60 / 3.40 " +
        "apart. The criterion's discriminator is `QOU.MassTheory." +
        "UICFunctionalSelection.gate_not_a_function_of_displayed_data`: the " +
        "displayed summand is even in the trace, so the gate reads a sign the " +
        "formula has already discarded and the old text could not denote the " +
        "producer at all. **Whether the gate itself belongs in the physics is " +
        "NOT settled here** — see the scope section; beans `qou-sv7h`, " +
        "`qou-brng`.",
      see: "docs/audits/2026-09-12-uic-functional-resolution.md",
    },
  ],
});
