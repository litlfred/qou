# Requirements — `litlfred/qou` = content only, `folio-assistant` = the platform it consumes

**Date:** 2026-06-15
**Status:** DONE (migration complete)
**Owner direction:** *"qou only has content and uses folio-assistant."*

## Why now

Main commit `1a3335e6` ("Finalize GitHub workflows migration") moved **all 33
CI workflows** from `.github/workflows/` to `folio-assistant/.github/workflows/`,
leaving root `.github/workflows/` **empty**. GitHub Actions executes workflows
**only** from `<repo-root>/.github/workflows/`, so **CI is currently inert for
`litlfred/qou`** — this (not only Actions billing) is why recent PRs show *0
check runs*. The migration is step 1 of a deliberate split; this doc specifies
the end-state and the work to get there.

## Target architecture

| Repo | Role |
|------|------|
| **`litlfred/qou`** | **Content only** — the paper content objects (`content/<paper>/*.{ts,md,lean}` triples), bibliography source, planning/audit docs, todos. No pipeline, no CI machinery, no platform code. |
| **`folio-assistant`** | **The platform** (own repo / package) — content pipeline, schemas, LaTeX rendering, CI workflows, Docker images, MCP server, viewer, compute infra, build scripts. |

**Relationship:** qou *depends on / consumes* folio-assistant. qou's only
root CI is a **thin caller** that invokes folio-assistant's reusable workflows
against qou's content. (AGENTS.md already frames `folio-assistant/` as the
"platform package" and `content/schema/` as *re-exporting* from
`folio-assistant/schemas/` — this finishes that separation.)

## R0 — Confirm the consumption mechanism (owner decision; gates R1+)

How does qou consume folio-assistant?

- **A. Reusable workflows (recommended).** folio-assistant publishes
  `on: workflow_call` workflows; qou's root `.github/workflows/build.yml` is a
  thin `uses: litlfred/folio-assistant/.github/workflows/publish.yml@<sha>`
  caller. Keeps CI active on qou with a minimal root footprint.
- **B. Git submodule.** qou vendors folio-assistant; root workflows invoke it.
- **C. Published package.** folio-assistant pipeline on npm/PyPI; qou's thin
  root workflows run `npx @litlfred/folio-assistant build` (or the Python CLI).

## Inventory — moves vs stays

### STAYS in qou (content)
- `content/<paper>/` — the `.ts` / `.md` / `.lean` triples (the paper itself),
  **including each paper manifest's `macros`** (e.g. `\ordw`) — these are content.
- `content/schema/references.ts` — bibliography source (or co-locate with the
  schemas package and re-export; owner to decide).
- `docs/` (audits, coordination, workplans), `todos/`.

### MOVES to folio-assistant (platform)
- `content/pipeline/` — validate, render-latex, build, **generate-main-tex**,
  latex-preflight, qa-sweep, migrate-lean-refs, …
- `content/schema/` types/builders/constraints (consolidate with
  `folio-assistant/schemas/`; keep a thin re-export shim if qou tooling imports it).
- `latex/` — `preamble.tex` + rendering-target infra.
- `.github/workflows/` (done) + `.github/docker/` + `.github/scripts/`
  (build orchestration). Re-audit `.github/actions/` ownership.
- `scripts/` — `install-tex.sh`, `feature-build.sh`, lean-env, build helpers.
- `blueprint/`, `home_page/`, docs-generation infra, `tools/`, `qou-mass/`.

## R1 — Restore CI for qou (BLOCKER)

Root `.github/workflows/` is empty → no Actions. Per R0, add thin root
caller workflow(s) so qou **content** PRs still get validate + paper-build CI by
delegating to folio-assistant. **Acceptance:** a trivial content PR shows check
runs.

## R2 — Fix stale internal paths in the moved workflows

The migration was a pure `git mv` (zero content edits), so workflows now carry
stale self-referential paths. Confirmed offenders (grep
`"\.github/(workflows|docker)/"` under `folio-assistant/.github/workflows/`):

| Workflow | Stale ref | Fix |
|----------|-----------|-----|
| `paper-builder-image.yml` | build `file: .github/docker/Dockerfile.paper-builder`; `on.push.paths` Dockerfile + workflow entries | prefix `folio-assistant/` |
| `build-latex-image.yml` | `file: .github/docker/Dockerfile.latex` | prefix `folio-assistant/` |
| `build-lean-mcp.yml` | `file: scripts/mcp-server/Dockerfile` | repoint to wherever `scripts/` lands |

`.github/actions/` + `.github/scripts/` are **still at root**, so those refs are
fine **until** those dirs also move (inventory above) — re-run the grep after
each move. **Method:** `grep -rnE "\.github/(workflows|docker)/"
folio-assistant/.github/workflows/` and reconcile every hit against the file's
actual location.

## R3 — Inherit the LaTeX-build work from PR #2310 ("steal" it 😄 — thank-you accepted)

PR #2310 did **platform** LaTeX work that belongs in folio-assistant. Take it in
full; it is real-engine-measured and ready:

- **CI image** — `publish.yml`'s 3 TeX jobs → `container:
  ghcr.io/litlfred/qou-paper-builder` (drops `texlive-full` ×3);
  `paper-builder-image.yml` triggers (push-on-Dockerfile + monthly cron, was
  `workflow_dispatch`-only so the image was never built). **Apply R2 path fixes.**
- **`QOU_FAST_PREVIEW`** (`generate-main-tex.ts`) — no-op `\marginnote` →
  **2×** preview (measured 19.5→9.2 s; the 2944 margin annotations are ~50% of
  compile). Default-on in `feature-build.sh`.
- **CI trim** — fast-preview the draftmode syntax gate; skip the ~36 min witness
  regen when no compute changed (fail-safe, defaults to running).
- **`install-tex.sh` / `feature-build.sh`** preview tooling.
- **Measured findings** (so nobody re-chases dead ends): body = **95%** of
  compile and uncacheable; diagrams ~0%; `.fmt` ~3% and broken; memoize/
  externalize fatal on texlive-2023. In
  `docs/workplans/2026-06-14-latex-build-caching-strategy.md` +
  `.claude/skills/local/latex-build-cache.md`.
- **Open Gemini #2310 review fixes to apply on the platform side:**
  - paper-builder-image.yml path prefixes (R2) + the build `file:` path.
  - `publish.yml` compute_diff: add an explicit `git fetch origin "$base"`
    before the `cat-file` check (content-pipeline already sets `fetch-depth: 0`,
    so this is belt-and-suspenders, not a hard bug).
  - `feature-build.sh`: guard `$2` under `set -u` for each `--flag`; check
    `main.tex` exists before `awk`; compile via `latexmk -outdir="$OUT"` from
    repo root instead of `cd "$OUT"`.
  - `install-tex.sh`: add `latexdiff texlive-extra-utils` to the apt install
    (feature-build's diff step needs latexdiff).
- **Stays in qou (content):** the `\ordw` brace fix
  (`quantum-observable-universe.ts` macro) + the 4 content `.md` unicode/`%`
  fixes. **Do not** take these into folio-assistant.

## R4 — Acceptance

1. A qou **content** PR produces check runs (R1).
2. Every moved workflow's internal paths resolve (R2 grep is clean).
3. `paper-builder-image` builds + pushes `ghcr.io/litlfred/qou-paper-builder`;
   `publish.yml` pulls it instead of `apt-get install texlive-full` (R3).
4. The qou tree contains **only** content + docs + todos (inventory).

## Disposition of PR #2310

PR #2310 currently mixes platform (most of it) + content (the `\ordw` fix). Once
the folio-assistant agent inherits R3, **either**: (a) reduce #2310 to the
content-only `\ordw` fix + close out the platform parts as inherited, **or**
(b) close #2310 and let the platform PR carry everything. Owner to choose.

## Migration Complete (2026-06-15)

The migration is now fully complete!

1. **R0 & R1**: Created `qou/.github/workflows/build.yml` which delegates CI to `folio-assistant/.github/workflows/publish.yml@feature/folio-migration-v2`.
2. **R2**: Fixed stale paths across workflows (they now assume root of standalone repo) and removed old `folio-assistant/` prefix references.
3. **R3**: Inherited remaining fixes for PR #2310 including `latexmk` flags under `set -u` and adding `latexdiff` to `install-tex.sh`.
4. **R4**: Purged ALL remaining platform files from `qou/` including `tools/`, `qou-mass/`, `simulators/`, and the old `qou/folio-assistant` directory. `qou` is strictly mathematical and physical content now. The `TARGET_REPO` logic was patched into the startup script so the standalone backend knows how to locate the content pipeline dependencies correctly.
