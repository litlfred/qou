# Publish CI follow-ups (post `copilot/fix-latexmk-errors`)

**Created:** 2026-05-28
**Context:** Captured by Copilot session that fixed the `latexmk: Could not find file 'main.tex'` failure in `.github/workflows/publish.yml` and the post-job `git submodule foreach` warning caused by spurious `.lake/packages/*` gitlinks. Per user request, residual items are parked here to be picked up after the current PR merges.

## Done in this PR
- [x] `publish.yml` content-pipeline step now invokes `pipeline/build.ts` with `--generate-main --main-out ../main.tex --preamble ../latex/preamble.tex` so the downstream `paper-pdf` job actually has a `main.tex` to compile.
- [x] Untracked 27 spurious `.lake/packages/*` and `content/*/lean/.lake/packages/*` gitlinks (mode `160000`) that were committed despite `.gitignore` listing them, eliminating the `fatal: No url found for submodule path '.lake/packages/Cli' in .gitmodules` warning emitted by `actions/checkout`'s post-job submodule walk.

## Follow-ups (deferred — pick up after merge)

- [ ] **Align the `content/package.json` `build` script with CI.** The npm script currently runs `bun run pipeline/build.ts` with no args, so `main.tex` is never produced for local `bun run build`. Either:
  - (a) extend the script to pass `--generate-main --main-out ../main.tex --preamble ../latex/preamble.tex`, or
  - (b) add a dedicated `build:paper` script and have CI call it, removing the duplicated invocation in `publish.yml` / `blueprint.yml` / `lean-build.yml` / `lean_ci.yml`.
- [ ] **Audit other workflows for the same `main.tex` gap.** Confirm every place that library/consumes `main.tex` either generates it explicitly or depends on a job that does. `paper-builder-image.yml` in particular should be re-checked.
- [ ] **Lock down `.lake/` tracking.** Add a CI guard (e.g. a one-liner in the existing `audit-wiring` job, or a dedicated step) that fails fast if any future commit re-introduces a gitlink under `.lake/` or `content/*/lean/.lake/`. Something like:
  ```bash
  if git ls-files --stage | awk '$1==160000 {print $4}' | grep -qE '(^|/)\.lake/'; then
    echo "::error::Spurious .lake/ gitlinks reintroduced"; exit 1
  fi
  ```
- [ ] **Decide on `.gitmodules`.** Either the repo intentionally has no submodules (current state — confirm and document in `CONTRIBUTING.md`) or it should — in which case create `.gitmodules` and re-add the correct entries. The current "tracked-as-gitlink but no `.gitmodules`" state is the bug-prone middle ground we just exited.
- [ ] **Local-build parity reminder.** The user explicitly flagged "i thought you did local build". Future Copilot sessions touching CI should run the equivalent commands locally before committing — at minimum `cd content && bun run pipeline/build.ts ... --generate-main --main-out ../main.tex` to confirm `main.tex` lands at the repo root. Add a short note to `AGENTS.md` / agent setup steps.

## Out of scope / open question

- [ ] **"Keep a 5-minute watch on `main` indefinitely"** (user request, same message). Copilot sandbox sessions are not persistent — any in-session `while sleep 300; git fetch` loop dies when the session ends. A durable solution is a scheduled workflow (e.g. a `.github/workflows/main-watch.yml` running on `schedule: cron: '*/5 * * * *'`) that fetches, diffs, and opens an issue / posts to a coordination channel if anything noteworthy lands. Needs clarification on what "watch" should actually trigger (notification target, what counts as actionable, etc.) before scaffolding.
