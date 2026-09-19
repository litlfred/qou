---
# qou-lkrd
title: '`lake build` (default target) scope gap — targeted builds are not library builds (the 22 errors are FIXED on main)'
status: completed
type: bug
priority: high
tags:
    - lean
    - infra
    - ci
created_at: 2026-08-08T11:45:00Z
updated_at: 2026-09-13T17:30:00Z
---

## UPDATE 2026-08-08 (later the same day): the two named modules are GREEN

Re-measured against `origin/main` at `d4c9a36022`, **194 commits after the
measurement below**:

```sh
lake build QOU.MathlibExt QOU.Archimedean.TorusKnot   # exit 0, no errors
```

Both modules now compile. The 22 errors were real when recorded, but they were
measured against a base that was already ~194 commits stale, and main has since
repaired them. **The claim in this bean's title is no longer true and should not
be quoted.**

What survives is the *scope* lesson in "Why it matters", which was the actual
point: "lake green" in this repo has usually meant targeted module builds, not
the default target, and those are different claims. Keep this bean open only
until the default target is confirmed green end-to-end and wired into a gate.

The measurement lesson is the durable content, and it is self-inflicted:
**this bean asserted a main-side defect that main had already fixed, because it
was recorded against a stale base.** Measuring "on main" means fetching main
first.

## What (as originally measured — SUPERSEDED by the update above)

Plain `lake build` in `content/quantum-observable-universe/lean` fails, on
`origin/main`, with **22 errors across two modules that `QOU.lean` imports**:

| module | errors | cause |
|---|---|---|
| `QOU/MathlibExt.lean` (imported **directly** by `QOU.lean:80`) | 11 | `List.foldl_mul_eq_mul_prod` and `Real.rpow_half_eq_sqrt` do not exist in the pinned Mathlib (`f897ebcf72`) |
| `QOU/Archimedean/TorusKnot.lean` (via `QOU/Archimedean.lean`) | 11 | `TorusKnotLabel.seifertRank` and `.embeddableOn` are referenced but the structure has only `r, s, r_ge_two, r_lt_s, coprime` |

Both files were last touched by `22728b8801` ("chore(lean): LWC-2 drop redundant
namespace prefix on the decl", Carl Leitner, 2026-08-03), which is an ancestor of
`origin/main`. Neither is touched by any `claude/*` branch in the 5₂ lane.

## Why it matters — this is the orphan gate's blind spot, inverted

`qou-orph` established that **`lake build` compiles only `QOU.lean`'s import
closure, so 756 of 1600 modules are never built by anything.** True. But it
carries the unstated implication that the closure *does* build. It does not.

So "lake green" in this repo has only ever meant **targeted** module builds
(`lake build QOU.QBeta.Foo`), never the default target. That is the same failure
this lane has now hit seven times: **a check that tests something adjacent to
what it claims.** A reviewer reading "lake green" reasonably hears "the library
builds"; what was verified is "these seven modules build".

Targeted builds do work — `lake build QOU.QBeta.FiveTwoArgSector` is green over
2060 jobs — so this does not invalidate any per-module claim. It invalidates the
*scope* those claims are stated in.

## Not fixed here, deliberately

Both modules are outside the 5₂/dilogarithm lane and are main-side; repairing
them from a feature branch would collide with siblings. Claim before working
this.

## Repro

```sh
cd content/quantum-observable-universe/lean
lake build                                   # 22 errors, exit 1
lake build QOU.MathlibExt                    # 11 errors
lake build QOU.Archimedean.TorusKnot         # 11 errors
lake build QOU.QBeta.FiveTwoArgSector        # green, 2060 jobs
```

## Suggested repair

1. `QOU/MathlibExt.lean`: both missing lemmas are Mathlib renames. Find the
   current spellings under the pinned rev, or inline the two-line proofs.
2. `QOU/Archimedean/TorusKnot.lean`: `seifertRank` / `embeddableOn` need to be
   defined (or the dot-notation call sites repointed at whatever replaced them).
3. Then wire `lake build` — the *default* target — into whatever gate is
   supposed to be checking Lean, so the scope of "green" matches the claim.

---

## 2026-08-09 — the default target has now been measured, twice. Recording it here so this bean stops saying "unknown".

Measured in a 15 GB container, `PATH` carrying `~/.elan/bin` (⚠ `lake` is not on
the default non-interactive `PATH`; a shell wrapper around it reported exit 0
while `lake` itself was `command not found`).

**It was genuinely RED — for a reason this bean never named.** At `origin/main`
`bccb55f188`, and equally at `1b8b30758b`, `lake build QOU` failed with two
errors, both `linarith failed to find a contradiction`, at
`QOU/Archimedean/HyperbolicVolumeTranscendence.lean:132` and `:140`. `QOU.lean`
imports `QOU.Archimedean`, which imports that module, so it is in the closure.
Two errors, not 22, and a different module than this bean named — so the bean's
**specifics stayed wrong while its headline came back true**.

Cause: `linarith` matches atoms at *reducible* transparency, and the two
`∑ i ∈ Finset.range 20, (-1)^i * f i` occurrences did not unify for it, so the
partial sums became distinct atoms and `0.915 < S ≤ catalan_G ≤ 0.915` was
invisible. That makes the failure sensitive to the **import environment**: the
same module built clean on `claude/fivetwo-level7-ladder-numerators`, whose tree
lacked two modules of the closure. It surfaced only because merging main into
that branch invalidated a **stale `.olean`** and forced the recompile.

**Fixed on main** by a sibling in `181cda5e5e`, two lines taking the
transitivity step directly (`exact lt_of_lt_of_le hnum hlow` /
`exact lt_of_le_of_lt hup hnum`). Re-verified at `2aaac60320` with the `.olean`
deleted first: exit 0, 3143 jobs.

**What blocks end-to-end verification now is not a proof failure.** At
`2aaac60320`, `lake build QOU` dies at `[4804/5126] Building
QOU.Mathlib.SYTEnumerationN7` with `Lean exited with code 137` — **SIGKILL, the
OOM killer**. Not contention: built alone with ~8 GB free it still exits 137.
That module is a brute-force `#SYT = dimHLF` enumeration at `n = 7`. So a
sibling's "1675/1675, exit 0" is presumably true on a larger machine, and the
finding is that **the default target's buildability is machine-dependent** —
which is the concrete cause behind `qou-lkdf`, replacing "an attempt died with a
container".

Two method rules this cost, both now in the lane's discipline: **delete the
`.olean` before claiming a module compiles**, and **exit 137 is OOM, not red**.


## 🟩 THE DEFAULT TARGET IS GREEN END-TO-END — measured 2026-09-13 (bean qou-g5sp)

This bean's closing condition is explicit:

> Keep this bean open only until the default target is confirmed green
> end-to-end and wired into a gate.

**Half 1 is now measured.** On `main` `16ccc3f7e2`, with
`scripts/lean-library-sweep.py --only-exact QOU`:

```
=== library sweep: 1451 ok, 0 RED ===
  [1451/1451] ok   QOU
```

That selection is the library **root** and its whole untrusted dependency cone —
i.e. exactly `QOU.lean`'s import closure, the default target this bean is about —
compiled from source into a hardlinked shadow, never invoking `lake`, so the
restored olean cache is not evicted. The `--only-exact` matters: `--only QOU` is
a prefix and every module starts with it, so that selector silently becomes the
whole corpus.

**And the whole tree besides.** A `--all` run the same day, plus two follow-ups,
union to **2836 of 2836 modules judged, 0 RED** —
`docs/audits/2026-09-13-every-library-module-compiles-zero-defects.md`.

**The two modules in the title are in that population and neither is RED**, which
confirms the 2026-08-08 update from a second direction five weeks later:
`QOU.MathlibExt` and `QOU.Archimedean.TorusKnot` are both green. They are also
two of the eight failures `qou-orph` listed; all eight are green.

## The scope lesson this bean exists for is now settled, not merely restated

> "lake green" in this repo has only ever meant **targeted** module builds
> (`lake build QOU.QBeta.Foo`), never the default target. … A reviewer reading
> "lake green" reasonably hears "the library builds"; what was verified is
> "these seven modules build".

Correct, and it was the right thing to flag. It is now false as a statement about
the present: the default target has been verified as a whole, and the claim
"the library builds" is one a reviewer can now make with a citation.

**The premise this bean inherited from `qou-orph` is separately false, and that
is worth keeping straight.** This bean quotes it as *"True. But it carries the
unstated implication that the closure DOES build."* The "But" clause was right;
the "True" was not. `lake build QOU` compiles the **whole tree**, not just
`QOU.lean`'s closure, because the paper lakefile declares
`globs = ["QOU", "QOU.+"]` and `QOU.+` is `Glob.andSubmodules` — landed
2026-08-08 (bean `qou-rc7b`), the same day as this bean. See
`.github/workflows/lean-orphan-gate.yml`, which has carried that correction with
a direct experiment since 2026-08-15 (bean `qou-kljb`).

So both halves of the sentence are now answered: the closure builds, **and** so
does everything outside it.

## Half 2 — "wired into a gate", and what that can mean here

`scripts/lean-library-sweep.py` **is** the gate, and it is wired into
`/prepare-merge` §4 and `prepare-merge-auto` Phases 1 and 4. In a repo whose §"QA
is agent-owned; CI is a backup" makes the agent's own verification the primary
gate, that is the gate.

**If "gate" is read as "a CI check that runs on push", half 2 is NOT met and
cannot be met by this bean.** Every workflow here is `workflow_dispatch`-only
under the 2026-06-30 owner directive (Actions billing), which was reaffirmed on
2026-08-09 with the cost of a specific `main` breakage on the table. That is a
standing, owner-decided repo condition — not a task, and not this bean's.

Closing on the first reading, with the second stated so the owner can reopen if
they meant the CI one. The measurement stands either way.
