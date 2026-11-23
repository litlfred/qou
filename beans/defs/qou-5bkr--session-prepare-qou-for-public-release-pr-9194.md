---
# qou-5bkr
title: 'Session: prepare qou for public release (PR #9194)'
status: in-progress
type: epic
created_at: 2026-11-23T21:14:50Z
updated_at: 2026-11-23T21:14:50Z
---

PR #9194 on claude/project-thread-di0nax (head 883c64d07a, pushed).
Done: CONTRIBUTING evidence policy + issue-policy.yml auto-close; CONTRIBUTORS.md + authorship rule; AGENTS/copilot contribution directives; CC BY 4.0 license note; authors-note chapter after intro (contribution policy, folio-assistant-sci authoring, compute infra: Clarabel fork, GS/Markov peeling w/o novelty claim, cached computations on branches, Lean render link); qou.json lean directory; build.yml now calls folio-staging.yml (publish.yml deleted upstream); scripts/build-site.sh + publish-main-local.sh; post-merge-rebuild skill; owner-rulings rows.
PAUSED 2026-11-23 for handoff. Next:
1. Rebase onto main (#9184 touched AGENTS.md and owner-rulings.md; expect conflicts there, keep both sides).
2. Owner: create labels evidence:lean, evidence:python, evidence:citation.
3. Owner go -> rebase-merge #9194; then run bash scripts/publish-main-local.sh --deploy on main, or dispatch build.yml.
4. Open: TeX PDF build has no replacement since publish.yml was deleted; Lean render untested (no lake in container).
