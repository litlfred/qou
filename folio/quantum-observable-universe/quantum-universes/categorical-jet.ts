import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-jet",
  title: "Categorical jet object",
  lean: { ref: "qou:QOU.CategoricalJet",
    validation: "axioms_only",
  },
  uses: ["def:categorical-connection"],
  tags: ["jet"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-jet-0.svg", blockIndex: 0, hash: "2604ff8ef04c" },
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body:
        "Owner ruling 2026-11-22 (card \"Switch to (S⊗S)/I²\"): the jet object is the standard first-jet " +
        "module $(A \\otimes A)/I^2$, $I = \\ker \\mu$ (EGA IV 16.7). It replaces $A \\otimes \\Omega^1(A)$ with " +
        "$\\Omega^1(A) = \\ker \\mu$, which vanishes at $A = R$, so the base object is not a summand of it " +
        "(`QOU.LiftingDescent.not_injective_into_naiveJet_self`). The splitting and $\\ker r = I/I^2$ are " +
        "`QOU.LiftingDescent.jetRetract_comp_jetSection` and `ker_jetRetract`. The block's Lean ref is the " +
        "abstract `CategoricalJet` structure. The construction assumes $A$ commutative; a noncommutative " +
        "$A$ needs the two-sided-ideal version, which is not formalised.",
    },
  ],

});
