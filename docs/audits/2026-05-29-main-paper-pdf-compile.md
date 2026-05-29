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

## All errors fixed (the table-pipe fix exposed five more, fixed in turn)

Reproduced locally with a full TeX Live install (no native LaTeX, and no
Docker daemon, in the dev container). Each fatal either stopped pdflatex
or set a non-zero exit (`latexmk` then returns 12 → CI `exit 1`):

1. **`|` in inline math in tables** (renderer) — see above; fixed in
   `render-latex.ts` (`protectPipesInInlineMath`), covers all ~41 rows.
2. **Unmapped Unicode `⊢ ↓ ⟨ ⟩ • 𝓑`** in chapter titles/prose →
   `Unicode character not set up`. Added `\newunicodechar` mappings to
   `latex/preamble.tex`.
3. **`\)` typo** in `six-term-per-derivation-weights-table1-data.md`
   (T₂ cell) → `Extra }, or forgotten $`. Changed `\)` → `)`.
4. **`^` inside `\text{}`** in `borromean-bloch-group-element.md`
   (`\text{h^4-coefficient}`) → `Missing $ inserted`. Moved `h^4` into math.
5. **Markdown link inside `$$ \text{} $$`** in
   `sigma-shell-from-beta-chain-derivation.md` — math is verbatim, so `#`
   is an illegal macro-parameter char. Replaced with `\ref`.
6. **Table row cell-count mismatch** in
   `knot-formula-table-table2-data.md` (6 cells vs a 5-column header) →
   `Extra alignment tab`. Merged the trailing note into the Particle cell.
7. **`### heading` inside a blockquote** in `bohr-radius-categorical.md`
   → `\subparagraph` inside `quote` (a trivlist) → `missing \item`.
   Changed to a bold label.

(Diagnostic note: many error greps were initially blank because `grep`
treated the 1 MB `main.log` as binary — `grep -a` was needed.)

## Verified

`latexmk -pdf -draftmode -interaction=nonstopmode main.tex` (the exact
`publish.yml` command) now returns **exit 0** with **0 errors**.

## Note — separate CI blocker

The "Compile main paper PDF" job `needs: content-pipeline`, and the
"Content pipeline (bun + python + witnesses)" job is currently failing at
an early step (~4 s — before any content/witness processing, i.e. at
checkout / setup-bun), so the PDF job shows **skipped** rather than green.
That early failure is unrelated to this PR's content (which passes local
`validate` + build); it needs a CI re-run or an infra fix.
