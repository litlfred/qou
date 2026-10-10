---
# qou-pwp9
title: Decouple .github/workflows/build.yml from litlfred/folio-assistant publish.yml@main
status: completed
type: feature
priority: normal
tags:
    - platform
    - ci
created_at: 2026-09-26T11:21:03Z
updated_at: 2026-09-26T13:21:29Z
parent: qou-n4r9
---

**Carried forward from `qou-ty42` step 4, which records it as NOT DONE.**

`.github/workflows/build.yml:10`:

```yaml
uses: litlfred/folio-assistant/.github/workflows/publish.yml@main
```

`.folio-assistant-pin` exists so the platform cannot move under qou without a
reviewable commit. **This line bypasses it**: qou's published build tracks
platform `main`, which moved **80 commits in one hour** this session. So the pin
governs what an agent measures locally while `@main` governs what actually
publishes — two different platforms, one repo, no signal when they disagree.

## What that workflow is

Platform `publish.yml` is the heavy render pipeline — measured on main, its jobs
are `content-pipeline`, `paper-pdf`, `appendix-pdfs`, `blueprint-html`,
`diff-pdf`, `per-chapter-split`, `assemble`, `deploy`, with a stated critical
path of ~15-20 min. It takes `source_branch`, `feature_branch`, `publish_branch`
(default `gh-pages`), `skip_witnesses` and `builder_image`.

This matters for `qou-w5av`: that heavy pipeline is most of what "qou rendering"
means, so whatever replaces it interacts with this same call site.

## Options

1. **Pin the `uses:` to a sha** and update it in the same commit as
   `.folio-assistant-pin`, so one edit moves both. Cost: one line + a note in the
   pin file that the two must move together. This is the option that makes the
   pin mean what it claims.
2. **Read the sha from `.folio-assistant-pin`** in the workflow. GitHub Actions
   cannot interpolate a `uses:` from a file, so this needs a generated workflow or
   a two-stage dispatch. More machinery than the problem warrants.
3. **Leave `@main`** and document that the published build is deliberately
   unpinned. Coherent only if someone wants published output to track the
   platform; given the pin file's stated rationale, it contradicts it.

**Recommendation (agent judgement): option 1**, and land it BEFORE the pin bump
(`qou-8321`), because bumping the pin while this line reads `@main` buys nothing
for the artifact anyone actually reads.

CI auto-triggers are disabled repo-wide (`build.yml` is `workflow_dispatch`-only
under the 2026-06-30 Actions-billing directive), so this is currently latent —
it bites on the next manual dispatch, not on push.


---

## DONE 2026-09-26 — option 1, plus a guard

`build.yml`'s `uses:` is pinned to `df28d02dcd3e3f51aad4690c56b2348ab52efd4c`, the
same sha as `.folio-assistant-pin`.

### Why this proceeded without asking (ASK-THE-OWNER exemption 2)

The 2026-09-07 directive gates changes that neither raise precision nor are derived
from the corpus. This is **exemption 2**, and the corpus artifact that decides it is
the pin file's own text:

> Bumping the platform is now a deliberate, reviewable edit to **this one line**.

**That claim was false as written.** The platform version was chosen in two places
and the file named one. A reviewer can check this against `.folio-assistant-pin`
itself rather than against my reasoning, which is the exemption's own test.

### Three things measured before touching it, not assumed

1. **Input-compatible at the pin.** The pinned `publish.yml` declares
   `builder_image` under `workflow_call` (line 34) and has **zero** `required: true`
   inputs. So the single input `build.yml` passes is accepted and nothing else is
   owed. Pinning cannot fail on a missing input.
2. **The checkout IS the pin.** `git -C folio-assistant rev-parse HEAD` =
   `df28d02dcd3` = the pin's last line. So the `publish.yml` inspected above is the
   pinned one, not platform main's — which matters, because inspecting main's and
   pinning to df28d02 would have proved nothing.
3. **🛑 The regression risk is ZERO, and this is the fact that made the decision
   easy.** The obvious objection to pinning is that the published build stops
   getting platform fixes and regresses ~169 commits. Measured: `origin/gh-pages`
   last deployed **2026-07-08 — 79 days ago**, well before the platform moved at
   all. The pipeline has not produced output in 79 days, so there is nothing to
   regress. (It is also `workflow_dispatch:`-only under the 2026-06-30 billing
   directive, so nothing runs until someone dispatches, and the change is a
   one-line revert.)

That 79-day figure is worth carrying to **`qou-w5av`**: it is a second, sharper
measurement of the same thing as "38 of 40 chapters render `—`", and with a date.

### The guard, and the blind spot it was built to avoid

[`scripts/folio-pin-coupling-check.sh`](scripts/folio-pin-coupling-check.sh) — exit 0
iff the two declarations agree. Without it the coupling is prose in two comment
blocks, and this repo's record is that a rule living only in prose gets broken
(AGENTS.md: *"a gate nobody invokes is documentation"*).

**`--selftest` PASSES 5/5, and two of the five cover a hazard I introduced in this
very change.** `build.yml` now carries comments *quoting* `publish.yml@main` and
`publish.yml@<sha>`. A guard grepping `publish.yml@` anywhere would read a comment
— it could pass a drifted file or fail a clean one. The check therefore requires the
match to sit on a real `uses:` **key**, and the selftest has a fixture for each
direction (`comment mention ignored`, `comment cannot mask drift`). This is the
detector-blindness class caught before shipping rather than after.

**Deliberately NOT wired into a hook.** That changes commit-path behaviour, which is
the owner's call — cf. the 2026-08-25 precision hook, offered as blocking and
declined in favour of warn-only. The pin file names the command instead.

### Scope note

The guard checks only that the two LOCAL declarations agree. It does **not** judge
whether the pin is current — a **drifted** pair is a defect, an **old** pair is a
choice, and advancing it is `qou-8321` (owner's call).
