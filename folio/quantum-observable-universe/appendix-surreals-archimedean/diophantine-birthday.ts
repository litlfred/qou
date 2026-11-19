import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:diophantine-birthday",
  title:
    "Algebraic vs transcendental numbers are separated by birthday trajectory",
  lean: { ref: "qou:QOU.AppendixSurreals.DiophantineBirthday", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "birthday",
    "diophantine",
    "liouville",
    "roth",
    "algebraic",
    "transcendental",
    "open-problem",
  ],
  uses: ["rem:conway-normal-form"],
  cites: [
    "conway1976",
    "gonshor1986",
    "ehrlich2012",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/AppendixSurreals/DiophantineBirthday.lean` " +
        "carries a `residual : ℝ` for a Diophantine/birthday estimate — real by construction. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/alpha_em_form_ladder_probe.py",
    witness: "computations/alpha-em-form-ladder.witness.json",
    status: "verified",
  },
});
