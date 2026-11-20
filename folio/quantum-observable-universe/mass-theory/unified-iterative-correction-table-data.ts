import { table } from "../../schema/builders";
export default table({
  label: "tbl:unified-iterative-correction-table-data",
  title: "Data table from prop:unified-iterative-correction",
  uses: ["prop:unified-iterative-correction"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-19",
      body:
        "**Historical record -- no live producer, and none findable (bean `qou-ypq6`).** " +
        "A six-path corpus-grep sweep found nothing in this repository that emits these " +
        "seven rows. No `computation` field is wired, deliberately: there is no producer " +
        "to point at, and manufacturing one by choosing settings that reproduce the " +
        "published numbers is selection against the target, which AGENTS.md " +
        "\"NO FITTING\" forbids by name.\n\n" +
        "**Positive evidence that the table was assembled by hand rather than emitted.** " +
        "Three of seven `B_AME` cells do not round to the vendored AME2020 table " +
        "(`computations/data/ame2020.json`, read through `ame_binding_mev`): C-14 reads " +
        "105.7 against 105.2845 (+0.4155 MeV), Ne-20 reads 160.7 against 160.6448 " +
        "(rounds to 160.6), and H-2 reads 2.224 against 2.2246 (rounds to 2.225). A " +
        "producer reading that table cannot emit 105.7, and 105.7 is not a neighbouring " +
        "nuclide either (N-14 = 104.659, C-13 = 97.108). Separately, the column identity " +
        "`B_unif = B_dedi + Sum_lambda B_lambda` closes exactly at Ca-40, to within " +
        "display rounding at Ne-20 and Si-28, and fails at the other four rows -- by " +
        "163 MeV at Pb-208. One pass of one program does neither. These are properties " +
        "of the table, not of the search.\n\n" +
        "**Three `unified`-named binding objects live in the tree and none is this " +
        "table's `B_unif`.** (1) `hecke_core_legacy.unified_iterative_correction`, the " +
        "accumulator this block's parent proposition describes. (2) " +
        "`computations/probes/strong_unified_binding_probe.py`, whose `B_unified` is " +
        "anchor-inverted from AME and so returns 2.2246 at A=2 -- exactly AME, by " +
        "construction, against this table's -16.45 -- and which spans four atoms, not " +
        "seven. (3) `fsh-guts/deprecated/computations/unified_binding.py`, a magic / " +
        "nucleon-shorthand dispatch whose `E_0_BETA_MeV` is `Q_NEUTRON_MEV`. " +
        "`mba-step09b-per-isotope-binding.md` carries a correction (PR #5765, " +
        "2026-08-25) naming (2) as where \"the `B_unified` model lives\"; that is true " +
        "of a different `B_unified` and is **not** a pointer to this table's producer. " +
        "Wiring it would attach a published -16.45 to a script that returns +2.2246. " +
        "Re-verified against main on 2026-11-20: (1) and (2) are unchanged and in the " +
        "committed tree; (3) was `computations/_deprecated/unified_binding.py` when this " +
        "note was written and now lives in the branch-mounted `fsh-guts` store, which " +
        "is gitignored here -- so it is NOT reachable by a grep of the committed tree, " +
        "and a future sweep that misses it is seeing the mount, not an absence.\n\n" +
        "**The introducing commit is unresolvable in a shallow clone.** All four commits " +
        "`git log --follow` reports for the `.md` appear in `.git/shallow`; the oldest, " +
        "`0d62fe2a23b`, shows the file as newly added while changing 28,153 files and " +
        "9.9M lines -- the graft boundary presenting the whole tree as new. Its subject " +
        "(\"honest convergence guard -- multi-cut certificate\") belongs to an unrelated " +
        "arc; do not attribute the table to it. The numbers are byte-identical across " +
        "the fetched window. Settling the origin needs a full-history clone and " +
        "`git log -S`, which is not available here -- so what is established is *no " +
        "producer is findable by the six paths*, strengthened by the hand-assembly " +
        "evidence above, not a proof that none ever existed.\n\n" +
        "**The excluding ruling, with its date.** The two model columns name routes " +
        "excluded as consolidated binding routes by the no-knot-selection ruling of " +
        "2026-09-05 (`docs/audits/2026-09-05-binding-route-consolidation-no-knot-" +
        "selection.md`). The date sits here rather than in the block prose because a " +
        "dated reference in prose is what `voice-author-notes-pollution` exists to " +
        "catch -- it fired on exactly that line (`:15`, `P4:date-ref`) when the " +
        "caveat was first written, and the fix was to move the date, not to drop " +
        "the citation.\n\n" +
        "**An independent prior analysis of this table sits in its own QA sidecar, " +
        "and the six-path checklist cannot reach it.** `<block>.qa.json` carries an " +
        "*agent* verdict on criterion `trap-superlative`, reviewed 2026-08-22 -- " +
        "four weeks before the hunt above -- which reaches the same conclusion by a " +
        "different route: \"the fourth column is unexplained\"; it is identical to " +
        "`B_unif` \"only in the D row (-16.45)\"; and `B_unif - B_AME` and " +
        "`B_unif - B_dedi` were both tested as readings of it and neither fits. It " +
        "also independently confirms that `B_dedi` tracks AME to better than 0.5 % " +
        "on every row. This CORROBORATES the finding above; it does not contradict " +
        "it, and it is not a producer. It is recorded because of where it lives: " +
        "`.qa.json` sidecars are **not** among the six corpus-grep paths (audits, " +
        "content, computations, coordination ledgers, library, beans), so a negative " +
        "established by that checklist is silent about this surface. Anyone " +
        "declaring an item open or unexamined should read the block's own sidecar " +
        "as well. Bean `qou-tv74`.",
    },
  ],
});
