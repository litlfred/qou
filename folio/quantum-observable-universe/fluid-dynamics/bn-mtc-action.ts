import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bn-mtc-action",
  lean: { ref: "qou:QOU.bnAction", validation: "not_checked" },
  title: "Braid group action on $\\mathbf{V}^{\\otimes n}$ does not factor through $S_n$",
  tags: ["braid-group", "mtc", "anyons", "fractional-statistics"],
  uses: ["def:observable-mtc"],
  cites: ["kitaev2006"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "The Lean is proved at the `V (x) V` level (`n = 2`), not for general " +
        "`n`. The group-theoretic obstruction " +
        "(`not_factorsThrough_of_sq_ne_one`) is fully general -- arbitrary " +
        "groups, consuming only `rho sigma ^ 2 != 1` -- so the general-`n` " +
        "case needs the tensor-power construction and the fact that " +
        "whiskering preserves `square != 1`, not a new argument. " +
        "Also: the non-symmetry witness enters as an explicit hypothesis " +
        "rather than through `[ObservableMTC C]`, because content-block " +
        "siblings sit outside the Lake globs and cannot import one another. " +
        "The previous version wrote the instance binder anyway; " +
        "`autoImplicit` turned `ObservableMTC` into an auto-bound variable " +
        "and the elaborator rejected it (`invalid binder annotation, type " +
        "is not a class instance ?m.5`). That error was masking a second " +
        "defect: the old theorem concluded the definition's own " +
        "`braiding_nonsymmetric` field and proved it by projecting that " +
        "field -- the self-assuming shape AGENTS.md ss3b-cond item 5 " +
        "forbids -- and it was not the .md claim, which is non-factoring " +
        "through `B_n ->> S_n`.",
    },
  ],
});
