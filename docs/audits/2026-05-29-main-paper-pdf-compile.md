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

## Root cause (primary — fixed)

`content/pipeline/render-latex.ts` parses markdown with micromark's
`gfm-table`, a *flow* construct that splits table rows on `|` **before**
`remark-math` tokenises inline `$...$`. So a table cell whose math holds a
literal `|` — absolute value `$|\mathrm{tr}_M(\rho(\beta))|$`, bra-ket
`$\langle a|b\rangle$`, ket `$|n\rangle$` — spills into extra columns.
pdflatex then hits `! Extra alignment tab has been changed to \cr` (fatal,
"no output PDF file produced!"), and the orphaned `$` are escaped to
literal text. First fatal occurrence: the Feynman↔QOU dictionary table
(`mass-theory/feynman-qou-dictionary-table-data.md:5`), rendered at
`chapters/mass-theory.tex:9861`. ~41 table rows repo-wide share the
pattern.

## Fix

`render-latex.ts` `parseMdCached` now runs `protectPipesInInlineMath()`
before parsing: each bare `|` inside an inline `$...$` span is replaced
with `\vert ` (output-identical in math mode), so the table parser sees no
spurious delimiters. Real cell separators (`|` outside math) and fenced
code blocks are untouched. One pipeline change fixes all ~41 occurrences
and any future ones — no per-cell content edits. Verified: the three
previously-broken Feynman rows now render with the correct 2 alignment
tabs.

## Residual

A full `latexmk` pass still reports `pdflatex return code 1` after the
table fix — a separate residual error ("missing or unavailable
character(s)"). Under investigation via a halt-on-error pass; will be
recorded here once isolated.
