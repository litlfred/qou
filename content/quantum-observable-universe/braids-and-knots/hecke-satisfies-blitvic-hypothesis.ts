import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-satisfies-blitvic-hypothesis",
  title:
    "Hecke transfer matrices satisfy Blitvić's pair-partition combinatorial hypothesis for the non-commutative CLT",
  lean: { ref: "qou:QOU.Observations.hecke_satisfies_blitvic_hypothesis", validation: "not_checked" },
  uses: [
    "rem:non-commutative-probability-dictionary",
    "thm:jones-markov-trace",
  ],
  cites: ["blitvic2012", "wenzl1988"],
  tags: [
    "q-clt",
    "blitvic",
    "pair-partition",
    "hecke-quadratic-relation",
    "established",
  ],
  proofs: ["prf:hecke-satisfies-blitvic-hypothesis"],
  authorNotes: [
    {
      kind: "status",
      body:
        "**provable.** The decomposition is a direct consequence of: (1) the Hecke quadratic relation (algebra-level, no analysis); (2) the Markov property of $\\mathrm{tr}_M$ (`thm:jones-markov-trace`); (3) Wenzl's product factorisation (`prop:trace-locality-meets-gs-non-locality`). No new mathematics introduced; the proof in `prf:hecke-satisfies-blitvic-hypothesis` is an explicit reduction.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The carrier `A` of " +
        "`HeckeSatisfiesBlitvicHypothesisContext` is already a generic " +
        "`Type u` with its own `ringA` — only the *trace codomain* is `ℝ` " +
        "(`tr_M : A → ℝ`, `z_real : ℝ`, `pairWeight : ℕ → List ℕ → ℕ → ℝ`, " +
        "`centredMoment : List ℕ → ℝ`). That codomain is `ℝ` because of what " +
        "`z_real` is: the class docstring defines the Markov parameter as " +
        "`z = 1 / (q^{1/2} + q^{-1/2})`, i.e. it requires a **square root of " +
        "`q`**, which a generic commutative ring need not admit (§7c puts " +
        "radicals on the `ℝ` side). The odd-length vanishing itself would " +
        "generalise to any `AddCommMonoid` codomain, so this is a " +
        "specialisation of the *scalar field*, not of the algebra — and it is " +
        "the square root, not the ordering, that forces it.",
    },
  ],
});
