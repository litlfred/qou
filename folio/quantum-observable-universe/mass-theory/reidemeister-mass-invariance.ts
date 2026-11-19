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
  lean: { ref: "qou:QOU.Braiding.reidemeister_mass_invariance",
    validation: "not_checked",
  },
  uses: ["rem:hydrogen-orbitals", "conj:borromean-quark"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
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
