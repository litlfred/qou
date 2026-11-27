import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-aubin-lions",
  lean: { ref: "qou:QOU.FluidDynamics.QAubinLions" },
  title:
    "q-deformed Aubin--Lions lemma: compactness of the solution family as $q \\to 1$",
  uses: [
    "thm:quantum-peter-weyl",
    "conj:ns-counterexample",
  ],
  tags: [
    "aubin-lions",
    "compactness",
    "convergence",
    "weak-limit",
    "counter-example",
    "millennium-problem",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-24-undecided-carrier-witnesses.lean` records that the earlier existential `QAubinLions` carrier (`∃ q_thresh > 0`) was trivially inhabited at `1`.",
      see: "docs/audits/2026-08-24-undecided-carrier-witnesses.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation guard (`qou-x60n`, `qou-rq9n`): `2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean` tracks the re-encoding of `QOU.AlgebraicSubstrate.QAubinLions` as a parameterised refutable hypothesis.",
      see: "docs/audits/2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation refutability witness (`qou-x60n`, `qou-rq9n`): `2026-08-30-qns-carriers-are-refutable.lean` proves `¬ QAubinLions (fun _ => 0)` and `QAubinLions (fun E => 2 * E)`.",
      see: "docs/audits/2026-08-30-qns-carriers-are-refutable.lean",
    },
  ],
});
