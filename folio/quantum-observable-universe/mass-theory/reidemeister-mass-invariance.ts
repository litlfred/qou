import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:reidemeister-mass-invariance",
  title:
    "Reidemeister invariance of mass and binding energy",
  tags: [
    "reidemeister",
    "mass",
    "binding-energy",
    "knot-invariant",
    "embedding",
    "shell-transition",
    "writhe",
  ],
  lean: { ref: "qou:identity_preserved_by_shell_transition",
    validation: "not_checked",
  },
  uses: ["conj:borromean-quark"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Dependency cycle cut (`dcy4`): removed forward post-wall remark `rem:hydrogen-orbitals` from `uses[]` (`predicted-spectra` applies this conjecture rather than supplying a premise).",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-are-inhabited-by-zero.lean` records the zero-witness against the retired library `ReidemeisterMassInvarianceContext` wrapper.",
      see: "docs/audits/2026-08-30-context-classes-are-inhabited-by-zero.lean",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-09-04-borromean-quark-carriers-trivial.lean` (`T4`) inhabits the local `BorromeanQuark` `Prop` carrier with `V = 1`.",
      see: "docs/audits/2026-09-04-borromean-quark-carriers-trivial.lean",
    },
    {
      kind: "status",
      date: "2026-06-07",
      body:
        "**Conditional conjecture; proved core + conjectural reading.** The " +
        "three Reidemeister-move invariances (topological mass invariant " +
        "under R-I/R-II/R-III; binding energy an embedding invariant under " +
        "R-II/R-III) follow from the hyperbolic-volume invariant and the " +
        "embedding structure. The block is kept `conjecture` (not promoted to " +
        "a §3b-cond proposition) because (i) it is downstream of " +
        "`conj:borromean-quark` — now made explicit in `uses[]`, previously a " +
        "manifest gap — and (ii) the shell-transition R-I reading is " +
        "genuinely conjectural. Promotion to a §3b-cond conditional " +
        "proposition is pending a Lean class-hypothesis wiring of " +
        "`conj:borromean-quark`. (Conjecture-triage 2026-06-07.)",
      see: "docs/audits/2026-06-07-conjecture-triage.md",
    },
  ],
});
