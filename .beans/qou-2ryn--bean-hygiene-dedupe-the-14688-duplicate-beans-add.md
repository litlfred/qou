---
# qou-2ryn
title: 'Bean hygiene: dedupe the 14,688 duplicate beans, add a create-guard, gitignore agent scratch dirs (qou+fa)'
status: completed
type: task
priority: high
created_at: 2026-08-10T03:55:59Z
updated_at: 2026-08-10T12:59:09Z
---

PRs open: qou#4914 (3 commits: 14,688 deletions + create-guard + gitignore), folio-assistant#106 (guard + gitignore baseline in writing-a-paper.md Step 2, so new folios inherit it).

prepare-merge run for #4914: rebase clean (branch was 0-ahead, reset onto main first); legacy lean.ref shapes = 0; precision-gates --changed = skipped (no witness or computations/ script touched); Lean build + one-voice + content-validation N/A (no .lean, no content block, no compute in the diff). qou has no check runs by design (auto-triggers disabled repo-wide).

fa#106 CI caught a real defect on the first push: docs/reference/skill-instructions/{todo-manager,session-intent}.md are GENERATED from skills/** by gen-skill-docs.ts and code-quality-gates.yml runs it with --check. Regenerated in cde700c; gate now 'generated docs are up to date' (exit 0).

Both awaiting Copilot. NOT merged - rule 10 requires Copilot before merge.

Deliberately NOT done: untracking the 2,522 already-tracked files in the five newly-ignored dirs (needs git rm -r --cached; _deprecated/ may be intentional history - author's call). Out of scope: 64 further bean ID collisions unrelated to this flood, and 5 beans with empty title.
