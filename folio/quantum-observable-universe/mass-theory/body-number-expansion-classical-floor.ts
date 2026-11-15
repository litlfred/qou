import { remark } from "../../schema/builders";

export default remark({
  label: "rem:body-number-expansion-classical-floor",
  title: "The body-number expansion has a classical floor: no power counting in $q - 1$",
  interprets: "prop:subset-cumulant-recursion",
  lean: { ref: "qou:QOU.MassTheory.b3corpus_classical", validation: "not_checked" },
  uses: [
    "prop:subset-cumulant-recursion",
    "prop:markov-trace-frobenius-selection",
  ],
  foreshadows: ["rem:brane-tower-q-laplacian-decay-interpretation"],
  tags: ["cluster-expansion", "cumulant", "mayer", "ursell", "power-counting", "effective-field-theory", "classical-limit", "scope-b"],
  computation: {
    engine: "python",
    script: "computations/probes/body_number_expansion_classical_floor_probe.py",
    witness: "computations/probes/body-number-expansion-classical-floor.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Bean `qou-olxi`, attack option 1, run on the owner's instruction (\"do as suggested\"). The proposed theorem was that the connected `m`-body term of the assembly has `ε`-valuation at least `m` in `ε = q − 1`, which would supply a Weinberg-style power counting over body number. It is false, and the obstruction is an identity: every bond factor is `z_D(1) = 1/2` at the classical point, so `b₃(1/2,1/2,1/2) = −5/8 ≠ 0` and the valuation is `0`. Lean `QOU/MassTheory/BondFactorClassicalFloor.lean` (`b3corpus_classical`, sorry-free); probe 15/15 with exact Fractions, the two `q₀` contrasts at the proton pin. Scope (b) for the ordering in `ε`; invariant `z_D(1) = 1/2`. Says nothing against an ordering in another parameter.",
    },
  ],
});
