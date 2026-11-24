import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-closure-stability",
  title:
    "Shell closure stability: categorical shell closures are local terminal objects",
  lean: { ref: "qou:QOU.BraidKnot.ShellClosureStability",
    validation: "not_checked",
  },
  uses: ["def:dressed-particle"],
  computation: {
    engine: "mpmath",
    script: "computations/sigma_f_electron_shell_chain.py",
    witness: "computations/sigma-f-electron-shell-chain.witness.json",
    status: "verified",
  },
  tags: [
    "stability",
    "shell-closure",
    "terminal-object",
    "frobenius-stability",
    "multi-operator-binding",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` (`shellClosureMonotone_always`) shows `local instance : LE R_q := ⟨fun _ _ => True⟩` makes `ShellClosureMonotone` hold trivially for all `(D_prev, D, q)`.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
  ],
});
