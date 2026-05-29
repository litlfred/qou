# Investigation — `publish.yml` "Compile main paper PDF" failure

**Status:** investigating (branch `claude/fix-main-paper-pdf-compile-2026-05-29`).

## Symptom

The `Compile main paper PDF` job in `.github/workflows/publish.yml` fails at
the *Quick LaTeX syntax check (draftmode)* step:

```
latexmk -pdf -draftmode -interaction=nonstopmode main.tex
```

Observed on PR #1423 (run 26643954977, job 78531034568), but that PR changed
**no** paper content — only Lean/script files under `content/.../lean/`, which
trip `publish.yml`'s `content/**` path filter. The generated `main.tex` there
is identical to `main`, so the failure is **pre-existing on `main`** and will
reproduce on any PR that touches `content/**`. The content pipeline's own
`validate` (unified-latex AST parse) passes — only the stricter full
`texlive-full` compile fails.

## Plan

1. Build content → `main.tex` + `chapters/` locally (`bun run pipeline/build.ts`).
2. Reproduce the failing compile in Docker (`scripts/docker-latex-build`), since
   no native TeX Live is available in the dev container.
3. Identify the offending LaTeX (file + line) from the `latexmk` log.
4. Fix it at the **content source** (`.md`/`.ts`) — not the generated `.tex`.
5. Re-compile to confirm green; record the root cause below.

## Root cause

_TBD — filled in once the compile log is captured._
