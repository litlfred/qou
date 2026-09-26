---
# qou-pwp9
title: Decouple .github/workflows/build.yml from litlfred/folio-assistant publish.yml@main
status: todo
type: feature
priority: normal
tags:
    - platform
    - ci
created_at: 2026-09-26T11:21:03Z
updated_at: 2026-09-26T11:26:34Z
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
