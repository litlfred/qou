import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:jet-convergence-classical-limit",
  title:
    "Jet-filtered knot invariant converges to classical dimension-weighted average",
  lean: { ref: "qou:QOU.BraidKnot.jet_convergence_classical_limit",
    validation: "not_checked",
  },
  uses: ["conj:jet-filtered-knot-factor"],
  tags: [
    "convergence",
    "classical-limit",
    "branching-rule",
    "wedderburn",
    "jet-filtration",
  ],
  cites: [
    "ivanov-olshanski2003",
    "feray-meliot2012",
    "kerov1996",
    "fulman2003",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation verification (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` (`HandAdjudicated7`) certifies `ConvergenceBound` (`SkewSYT`) and `QIntRatioBoundSmall` (`QHookBound`) are non-vacuous and refutable.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/BraidKnot/jet_convergence_classical_limit.lean` uses " +
        "`Filter.Tendsto`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
