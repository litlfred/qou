import { definition } from "../../schema/builders";

export default definition({
  label: "def:hochschild-homology",
  title: "Hochschild homology",
  lean: { ref: "qou:QOU.QuantumUniverses.HochschildZero", validation: "not_checked" },
  uses: ["def:quantum-universe"],
  defines: ["hochschild-homology"],
  foreshadows: ["def:chern-character", "rem:hkr-theorem", "rem:trace-ledger"],
  cites: ["loday-1998", "weibel1994"],
  tags: ["hochschild-homology", "homological-algebra", "trace", "cocenter"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Introduced by the 2026-09-15 explicit-layer selection (owner option B): the corpus invoked `HH^2`, `HH_0` and \"HKR\" in five blocks without ever defining Hochschild (co)homology. The Lean sibling carries the degree-zero group as the cocenter `A/[A,A]` (re-exported from `QOU.Information.cocenter`) with the trace property `[ab] = [ba]` and the factorisation of cyclic functionals through it, sorry-free; the higher groups and the Connes operator are cited (Loday Ch. 1–2), not formalised. Placed in the first chapter because `def:chern-character`, `rem:hkr-theorem`, `def:classical-limit-obstruction` and `rem:trace-ledger` all consume it from later chapters.",
    },
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): `HochschildZero R A` is the cocenter, `hochschildClass_mul_comm` is the identity `[ab] = [ba]`, and `traceOnHochschildZero` is the factorisation of a trace through it.",
    },
  ],
});
