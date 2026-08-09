# File-level drop check on PR #4824's nine-PR consolidation

**Date:** 2026-08-09
**Branch:** `claude/agent-pr-4824-falsifiability-ivbu2m`
**Trigger:** coordination comment from sibling
[#4840](https://github.com/litlfred/qou/pull/4824#issuecomment-5229018449)
on [#4824](https://github.com/litlfred/qou/pull/4824), which arrived as the
#4824 session stalled and was never actioned.

## What #4840 asked for

#4824 §1 declared all nine consolidated PRs (3793, 4551, 4519, 4538, 4540,
4525, 4521, 4176, 4106) fully dispensed with "zero unlanded work", traced at
the **deliverable** level. #4840 reported that the analogous consolidation
#4671 made the same shape of claim and still dropped a file's changes: a
doc that had been modified **independently on both sides** merged to `main`'s
version, silently losing the branch's paragraph. Deliverable-level tracing
cannot see this, because the file still exists, still holds most of the
branch's work, and the headline artifact did land.

The proposed check: per source branch, diff its own touched files against
`main` and read the direction on anything non-zero.

## Method actually run

Three-way per-file comparison — base (merge-base with `main`), branch, and
`main` — restricted to files the branch **modified**. Pure additions land or
conflict loudly and were excluded.

| outcome | meaning |
|---|---|
| `branch == main` | landed byte-identical — clean |
| `base == main`, branch differs | `main` never touched it; branch content absent — **drop** |
| all three differ | both sides modified — **needs a line-level read** |

Script: `dropcheck.sh` (three `git rev-parse` object comparisons per file).
PR heads were taken from `refs/pull/<n>/head`, so no branch names were
needed. The clone is shallow by default; `--deepen` on both `main` and each
PR ref is required before `merge-base` resolves.

## Results

Six of nine came back completely clean: **4519, 4538, 4540** had no
both-modified files at all, and **4551, 4525, 4521** touched only
`QOU.lean`, where `main` is a strict superset (imports added since — `main`
newer, no branch-only content). **4106**'s single candidate is a bean whose
`main` copy is newer (`completed`, 2026-07-24) than the branch's
(`in-progress`, 2026-07-19).

That leaves three findings.

### 1. `TorusKnotMass.lean` — confirmed drop (repaired here)

#3793 removed a fabricated `noncomputable instance : TorusKnotMass := ⟨0, rfl⟩`
and rewrote the surrounding documentation. The **removal** reached `main` by a
different route; the **documentation rewrite** did not. `main` was therefore
left describing an instance it no longer contains, in two places:

- module docstring — *"the `noncomputable instance` carries `sorry` for the
  mass-formula field. Downstream theorems take `[TorusKnotMass q_0]`"*
  (the class takes no parameter);
- class docstring — *"the `noncomputable instance` is the open structural
  statement."*

This is precisely #4840's failure mode: headline deliverable landed, wiring
prose lost, nothing looked wrong. Both are repaired on this branch, and
#3793's history note is restored alongside `main`'s (they describe two
*different* prior fabricated instances — an axiom-backed one and the
`⟨0, rfl⟩` one — so both belong).

**Verified, not assumed:** at #3793's base `b759f24f` the class had 9
explicit fields including `factors_distinct : gauge_mass_factor ≠
scalar_mass_factor`. `⟨0, rfl⟩` supplies 2 of 9 and forces
`factors_distinct : (0:ℝ) ≠ 0`, so #3793's "did not typecheck" claim holds.

### 2. `dilogarithm-archimedean-limit.ts` (#4176) — partial drop (repaired here)

Both sides rewrote the same `authorNotes` entry. `main`'s version is better
on provenance (it names #4157 as the landing PR) and does state that the
remaining open content is Part B — so this is **not** a clean drop. What did
not survive is the branch's separate Part-B note explaining *why* Part B is
hard: the factors `1-xq^k` change sign, the poles of `Φ_n` approach the
`Li₂` branch cut, and the Frobenius-pairing pole cancellation has to do real
work. Confirmed absent from `main` by grep. Merged here: `main`'s Part A
note kept, the mechanism note restored.

### 3. `cj434` bean (#3793) — bookkeeping only

Branch marks it `completed`, `main` still `todo`. Its substance (the
content-bearing carrier refinement) is landing via #4824 §2. Left alone —
closing it is the owner's call, and it should close with #4824, not here.

## Verdict on §1

#4840 was right to flag the method. §1's conclusion survives at the
**deliverable** level — no PR's headline artifact is missing from `main` —
but "zero unlanded work" was too strong: one documentation rewrite and one
explanatory note were lost, in exactly the both-modified pattern that
deliverable tracing cannot detect. Both are repaired here. The check costs
minutes and should be standard for any consolidation claim.

## The orphan claim — refuted, then confirmed

#3793's comment also attributed the non-compiling file's survival to the
module being **orphaned from the `QOU` umbrella**. This went through two
rounds and the record of both is kept deliberately.

**The fact.** An import-closure walk from `QOU.lean` finds **785 of 1659**
library modules unreachable, `TorusKnotMass` among them, and
`lakefile.toml` declares `[[lean_lib]] name = "QOU"` with no `globs` key.

**Round 1 — refuted (wrong).** Against the restored `lake-cache/qou-v4-24-0`
tree, orphaned modules carry `.olean` artifacts at **56%** (440/785),
indistinguishable from reachable modules at **57%** (502/874), and
`TorusKnotMass.olean` is present. That looked like orphan status failing to
predict builtness, so the CI-escape claim was written up as unverified and
left out of the repaired file comment.

**Round 2 — confirmed (correct).** The artifact survey cannot answer the
question. Oleans persist: nothing prunes the build directory, so a module
built once — back when something imported it, or by an explicit module-target
build — keeps its olean indefinitely, and a tarball snapshot of a long-lived
build dir preserves the lot. Presence proves a module was built *at some
point*, not that `lake build QOU` builds it now.

Testing the mechanism directly settles it. Throwaway package, same toolchain
`v4.24.0`, root `Lib.lean` plus an unimported `Lib/Orphan.lean`:

| lakefile | result |
|---|---|
| no `globs` | builds `Lib.olean` only — **`Lib/Orphan.olean` NOT built** |
| `globs = ["Lib", "Lib.+"]` | builds both |

So Lake's default really is `globs = #[.one <lib>]`, `lake build QOU` never
elaborates the 785, and **#3793 was right**. The file comment now states the
CI-escape mechanism as confirmed, and `qou-kljb` carries the triage plan.

The methodological point is worth more than the result: *an artifact-presence
survey cannot answer a "does-the-build-do-X" question.* The 56%/57% figures
were real and the inference from them was still wrong. Test the build.

## Extending the check beyond #4824's nine

The same script was run against #4671's sources (**#4532**, **#4571**) — the
consolidation whose drop #4840 originally found — and **#4821**.

- **#4571** — clean, no modified-file divergence. Matches #4840's file-by-file
  result.
- **#4532** — four both-modified files. `QOU.lean` (`main` a strict superset)
  and `WhiteheadVolumeConjecture.lean` (`main` **newer** — it records
  `whitehead_vc_innerSum_half` as sorry-free downstream, which the branch
  predates) are fine; the `qou-t2sc` bean shows no content divergence. The
  fourth is `b1-hyperbolic-rows-theorem-audit.md` — **#4840's drop,
  independently reproduced here**.
- **#4821** — `QOU/ParticleInteractions/operator_selection_lp.lean` classifies
  as a hard **DROP**: `main` never touched the file, and the branch's content
  is absent. The branch replaces a `sorry` with a **sorry-free weak-duality
  proof** that derives feasibility, optimality and strong duality from a dual
  certificate. `main` still carries the `sorry`.

**Both live findings are already owned by #4840** — it restored the b1
paragraph (written against `main`'s current, stronger state) and independently
verified #4821's proof (clean rebase, `lean`-direct exit 0, sorry-free axioms,
genuine weak duality rather than a self-assuming projection). Neither is
repaired here; duplicating settled mechanical work has one owner per
AGENTS.md. What this run adds is independent corroboration by a different
method, and the observation that #4821's drop is the *hard* kind — a lost Lean
proof, not lost prose.

## Verification

- `lean`-direct **exit 0** on `TorusKnotMass.lean` (restored olean cache;
  `LEAN_PATH` must point at the **root** `.lake/packages/*/.lake/build/lib/lean`
  — the package-local mathlib tree under
  `content/quantum-observable-universe/lean/.lake/packages/` holds only 700
  oleans and lacks `Mathlib/Tactic.olean`, which produces a misleading
  "unknown module prefix 'Mathlib'").
  The edits are comment-only, so this is a regression check, not a proof
  obligation.
- `qa-sweep` re-run on the touched block; all three `source_hashes` re-verified
  to match.
- `scripts/check-sidecars.sh` clean apart from one pre-existing §7c marker on
  `TorusKnotMass.lean` (`gauge_mass_factor : ℝ` etc.). **Not addressed** — it
  predates this branch, this change is comment-only, and the flag looks like a
  false positive: the class carries ordering fields (`gauge_mass_factor_pos`,
  `scalar_mass_factor_pos`, `WZ_mass_ratio_in_unit`), which §7c lists as
  genuine grounds for `ℝ`.
- No CI run exists for this branch (auto-triggers disabled repo-wide).

## Reusable

```bash
git fetch -q origin "refs/pull/$PR/head:refs/prheads/$PR"
git fetch -q --deepen=400 origin "refs/pull/$PR/head:refs/prheads/$PR"   # shallow clones
mb=$(git merge-base origin/main refs/prheads/$PR)
git diff --name-status --diff-filter=M "$mb" refs/prheads/$PR | cut -f2 | while read -r f; do
  a=$(git rev-parse "$mb:$f"); b=$(git rev-parse "refs/prheads/$PR:$f")
  m=$(git rev-parse "origin/main:$f" 2>/dev/null) || { echo "GONE $f"; continue; }
  [ "$b" = "$m" ] && continue
  [ "$a" = "$m" ] && echo "DROP $f" || echo "BOTH-MODIFIED $f"
done
```
