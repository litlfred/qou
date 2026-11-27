## What this is

Workstream W4 of the 2026-11-20 coordinator plan (PR #8526). It classifies every **open** PR produced
by the batch-formalization generators: 351 PRs as of the run time above. That is the 333 the
predecessor found plus 18 from two families it flagged as "possibly in scope", both included here
because they share the generator's signature (round-numbered titles, the 5-bean batches and the "2-commit
witness protocol" bodies): `claude/roundNN-*` (14: eight `trd0-9nnz-fixes`, six hygiene and integrity
rounds) and the four multi-bean `feat/<topic>-xxxx-xxxx-xxxx-xxxx` PRs (#8227, #8234, #8237, #8241).

Each PR gets one of four verdicts. They are **recommendations**: the coordinator merges or closes, and
only with the owner's permission.

- **MERGE-CANDIDATE.** Clean against `main`. No sorry, axiom, `native_decide`, `True` or `X = X`
  flags, and no vacuity pattern above threshold. Does not touch a file or declaration that an older
  open PR also touches. Where Lean exists, the changed files compile with `lean`-direct.
- **NEEDS-REWORK.** Kept, but something must change first. The reason column says what.
- **CLOSE-SUPERSEDED.** A newer open PR redoes the same leaf beans. The test ignores umbrella beans
  cited by six or more PRs, such as `qou-6qbv`, `qou-10v9` and `qou-8lxd`.
- **CLOSE-VACUOUS.** The Lean restates rather than derives (see Finding 2).

## How it was checked

1. **Metadata.** For each PR: GitHub `mergeable` / `mergeable_state` and the file list; the bean ids
   cited in its title, branch or body, looked up on the beans mount for status and title; file and
   declaration overlap with the other batch PRs, using fully-qualified names.
2. **Static scan.** Every added or changed `.lean` file is scanned with comments stripped. Each
   theorem is flagged for: real `sorry`, `axiom`, `native_decide`, a `True` conclusion, an `X = X`
   tautology, and `rfl`/`decide` on a literal defined in the same file. Two more flags:
   - *generic identity*: a statement that mentions only its own bound variables plus `Int`/`Nat`
     arithmetic.
   - *unfolds an integer arithmetic def*: a statement whose only local constants are one-line `ℤ`/`ℕ`
     definitions.

   Real- and rational-typed one-liners are deliberately **not** flagged, because `z_D = q³/(q²+1)` is
   a one-liner and is the corpus formula. Each file is also checked for whether it imports Mathlib or
   QOU at all, and for a hand-written ring-axiom structure.
3. **Lean.** 208 PRs were checked: all 204 not marked CLOSE, plus two CLOSE-VACUOUS ones checked
   before their reclassification. Each changed file was run with `lean -DautoImplicit=false -s 65536`
   in intra-PR dependency order. Modules that other files in the same PR import were compiled into a
   hard-linked shadow olean root (unlinked before `-o`) so the real tree is never written through.
   `#print axioms` was appended for every theorem: **5,483 theorems** in total.
   - The snapshot lacked 16 modules that main has. Their 268-module cone was compiled with
     `scripts/lean-direct-cone.sh -k` (258 ok). Two cone modules still fail because the restored
     Mathlib cache lacks `Mathlib.Analysis.Calculus.Deriv.Pi` and `Mathlib.Analysis.ODE.PicardLindelof`;
     the eight KZ-holonomy modules that depend on them are blocked. That leaves 3 PRs `blocked`.
     2 PRs are `killed`: the kernel OOM-killed `lean` on an 8 GB container even with one job.
   - **Control run.** For every failed file that also exists on main, main's version was compiled the
     same way: 29 compile on main (the PR broke them) and 3 are red on main as well (#8238, #8329,
     #8459; tagged in the table). The other 16 failing files are new in their PR.
   - **Caveat, load-bearing.** The QOU oleans are the restored cache snapshot (dated 2026-09-06),
     topped up as above and not freshness-checked module by module. A pass means "compiles against
     that tree". Dependents of a modified module are **not** re-checked.

## Findings

1. **Every one of the 222 `dirty` PRs conflicts only in `lean/QOU.lean`**, the import list. Measured:
   for each PR touched-file, the blob at the PR's base was compared with `main`'s, and `QOU.lean` is
   the only file that differs, in all 222. These are mechanical rebases, not content conflicts.
   The flip side: every batch PR adds a line to `QOU.lean`, so each merge makes the remaining clean ones
   dirty again. Merging in a group therefore needs a rebase between merges, or one combined
   `QOU.lean` edit.
2. **146 PRs restate rather than derive**, mostly the `feat/qou-*` (78), `qou-10v9-*` (45) and
   `qou-8lxd-*` (19) families. Spot-read samples, with each PR's head SHA in the JSON:
   - #8510 "formalizes" bean `qou-y98b` (*"Gate the q0Anchor refill"*, a tooling task) as an `Int`
     structure holding the audit counts `1199 + 365 + 55 + 59 = 1678`, proved by `rfl`. Next to it,
     10 of its 14 theorems are the parallelogram and two-square identities over `Int`, with no relation
     to the bean.
   - #8489 defines `beltedSumVolumeScaled n v := n * v` and proves "belted-sum volume additivity" by
     unfolding it.
   - #8282 encodes a raw-float64 audit queue as `Int` literals and proves
     `activeDirtyWitnessQueue = 22` and `totalActiveDirtyFloatFields = 1748`.

   **198 of the 351 PRs import neither Mathlib nor QOU**, so they cannot refer to the corpus objects they
   are named after. Sixteen re-implement commutative-ring axioms as a hand-written structure, against
   the base-ring rule (§7c) in AGENTS.md. The PR bodies' claim of *"8 static vacuity audits: 0
   CRITICAL"* is true and beside the point: these patterns are invisible to those audits.
3. **38 PRs do not compile**, despite bodies reporting verification. The commonest error is `No goals
   to be solved` (13): an `omega`/`simp` after a `rw` that already closed the goal. That points to the
   generator never running `lean` on the final text.
4. **No non-standard axioms.** Every `#print axioms` on a PR that compiles shows only the standard
   axioms (`propext`, `Quot.sound`, `Classical.choice`) or none. `sorryAx` appears only in files that
   fail, where it comes from Lean's error recovery.
5. **Bean attribution is unreliable.** Many Mathlib-level MERGE-CANDIDATEs cite tooling beans. For
   example #8459 says it advances `qou-e9pp` (*"Witness-refresh advice is unsafe"*) with a binding
   theorem. The Lean can be fine while the bean link is wrong. **Do not mark cited beans completed on
   merge** without reading each bean.
6. **`_sub_eq_zero` padding.** In several `feat/round*` PRs, most added theorems restate an existing
   `a = b` as `a − b = 0`. When that is three-fifths or more of what a PR adds, it is marked
   NEEDS-REWORK.
7. **Beans left claimed.** The 146 CLOSE-VACUOUS PRs cite **734 distinct beans that are
   `in-progress`**. Closing the PRs does not release those claims.
8. Fifty-one batch PR bodies carry the session link `session_01E667391F74184786BF4B9D`, which W6
   reports is not a real session id. The other 298 carry none.

## Decisions for the owner (via the coordinator)

**D1. Close the 146 CLOSE-VACUOUS and 1 CLOSE-SUPERSEDED PRs?**

- *What it means:* close them unmerged. The branches stay, per AGENTS.md rule 9.
- *What it costs:* 147 REST calls. No content is lost: the measured content is audit counts and
  integer identities.
- *What it risks:* a false positive closes a PR with real content.
  - The thresholds are at least 60 % of theorems flagged.
  - Real-typed definitions are exempt.
  - Six CLOSE-VACUOUS PRs were spot-read, all confirmed: #8510, #8489, #8315, #8403, #8282, #8467.
    An earlier detector version also caught real-typed corpus formulas; reading #8142 (convention-D
    Markov positivity) exposed that, and the exemption above was added.
  - The action is reversible: a closed PR can be reopened.
- *What it commits to:* nothing downstream. **D2** is a separate question.
- *Default if no answer:* they stay open. The `QOU.lean` churn they cause is cosmetic until someone
  merges.
- *Recommendation (judgement):* close them in family batches, `qou-10v9-*` first (45, all
  standalone).

**D2. Reset the 734 `in-progress` beans those PRs claim back to `todo`?**

- *What it means:* append a note to each and set its status to `todo`, so the queue shows them as
  open.
- *What it costs:* one bean-store push.
- *What it risks:* a bean also claimed by a live non-batch branch would be released wrongly. The
  per-bean check is not done yet.
- *What it commits to:* the work-plan says these items are unclaimed.
- *Default if no answer:* they stay `in-progress` indefinitely. That is exactly the stale-claim failure
  that the stalled-claim takeover rule exists for.
- *Recommendation (judgement):* yes, but only after the per-bean check. That check is W4's next item
  if the coordinator wants it.

**D3. Merge the 45 MERGE-CANDIDATEs, in groups?**

- *What it means:* rebase-merge in the order of the candidate table below.
- *What it costs:* per merge, a `QOU.lean` rebase and a `lean`-direct re-check after the rebase.
- *What it risks:* sorry-free is not derived. These compile and are not flagged, but each still owes
  `/prepare-merge`. The 7 no-Lean ones are compute and QA fixes for which
  `scripts/precision-gates.sh --changed` was **not** run here.
- *Default if no answer:* nothing merges.
- *Recommendation (judgement):* take the Lean-verified ones oldest first, five per group.
