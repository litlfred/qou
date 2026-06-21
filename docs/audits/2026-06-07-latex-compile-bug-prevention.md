# LaTeX compile-bug prevention — audit + preflight linter

**Date:** 2026-06-07
**Branch:** `claude/hopeful-maxwell-syjIo`
**Trigger:** "the publish and build workflow is failing… run the full PDF
part of the pipeline locally to reproduce errors then fix" + "what can you
do to prevent them from happening again… review ALL commits that were
latex bug fixes and do a COMPREHENSIVE audit/skills to stop this".

---

## 1. What was actually failing

The `publish.yml` runs were all red, but **not** because of the PDF.
Every recent run (all branches, all of 2026-06-06) died in **4–6 seconds**
in the `content-pipeline` job with 404 logs and all downstream jobs
`skipped` — the textbook **GitHub Actions billing-failure signature**
(AGENTS.md "CI billing failures"): setup-phase death ≤ 5 s, multiple jobs,
no log because the job never started. That is an infra/billing condition,
not a code bug. Local reproduction of the content-pipeline (export-bibtex
sync, `validate.ts`, `build.ts --generate-main`) passed clean (0 errors).

## 2. Real bugs found by compiling the PDF locally

Although CI's red was billing, the request was to run the **full PDF
part** locally. Installing `texlive-latex-extra` + `texlive-science` and
running the exact workflow command (`latexmk -pdf -f -interaction=
nonstopmode main.tex`) surfaced **three genuine fatal `! ` errors** that
the `paper-pdf` job *would* fail on once billing clears:

| # | Signature | Location | Root cause | Fix |
|---|-----------|----------|------------|-----|
| A | `! LaTeX Error: Command \pp already defined.` | `main.tex:189` vs `:500` | The paper manifest `macros:` block (`quantum-observable-universe.ts`) re-emitted `\newcommand{\pp}{\mathfrak{p}}` while `latex/preamble.tex` already defines `\pp = p` (the p-adic prime, AGENTS.md §7aa). All 18 content uses of `\pp` are p-adic; none are the proton. | Removed the stale manifest entry; preamble def is authoritative. |
| B | `! Undefined control sequence.` (`\tr`, ×3) | `binding-alpha-shift-extension.md` | Bare `\tr` is defined nowhere. | `\tr` → `\mathrm{tr}` (matches sibling `\mathrm{Vol}`). |
| C | `! Missing { inserted.` (at `\check`) | `y-lambda-cyclotomic-factorization.md:69` | `Q^\check{q}` — a math accent as a bare superscript; `\check`'s `\mathpalette` expansion breaks without braces. | `Q^{\check{q}}`. |

Fixed in commit **`b9e19df6`**. After the fix, `main.pdf` compiles clean
(7.9 MB) and `latexmk -draftmode` reports zero fatal `! ` errors.

## 3. Why these slipped through (the gap)

History is squash/rebase-merged, so per-bug `fix(latex)` commits are not
individually visible — but the *mechanism* is clear from the existing
mitigations in the codebase. The content pipeline's only LaTeX check is
`validateLatexAst` (`content/pipeline/render-latex.ts:1133`), which parses
rendered output through **unified-latex**. That parser builds a syntax
tree from *any* well-bracketed input and **never resolves macros**, so it
is structurally blind to:

- **A** — a macro defined twice (both `\newcommand`s parse fine).
- **B** — a macro used but never defined (`\tr` is just a macro node).
- **C** — `Q^\check{q}` is syntactically well-formed to the AST.

The *only* gating pdflatex check is `publish.yml`'s `paper-pdf` job
(`grep -aqE '^! ' main.log → exit 1`). But it is slow (`texlive-full`,
~3–5 min) and **no-ops exactly when it is most needed**: under the
Actions billing block and under `[skip-ci]` merges. When those fire,
nothing catches A/B/C before they land on `main`. That is the recurrence
engine.

Classes the team *had* already mitigated inline (so they recur less):
bare `#` (`checkBareHash`), pipe-in-inline-math (`protectPipesInInlineMath`),
math-block links (`checkMathLinks`), unicode→ASCII in verbatim
(`VERBATIM_TRANSLIT`). A/B/C had no such guard.

## 4. Prevention — the preflight linter

`content/pipeline/latex-preflight.ts` (+ seeded allowlist
`latex-known-macros.json`), landed in commit **`b8f7237e`**.

It is a **fast static gate (~1 s, no TeX install)** over the *generated
compile unit* — `main.tex` plus every `\input`'d `chapters/*.tex` (33
files; the chapter bodies are where B/C live — `main.tex` itself only
holds the preamble + manifest macros + `\input` lines). Checks:

| Check | Detects | False-positive profile |
|-------|---------|------------------------|
| **A** duplicate-newcommand | a name defined >1× by a *fatal-on-redefinition* definer (`\newcommand`/`\DeclareMathOperator`/`\DeclarePairedDelimiter`/`\NewDocumentCommand`). `\renewcommand`/`\providecommand`/`\def`/`\let`/`\DeclareRobustCommand`/`\DeclareDocumentCommand` excluded (they overwrite legally). | **Zero** by construction. |
| **B** undefined-macro | a multi-letter control word used but ∉ (locally-defined ∪ seeded allowlist ∪ TeX core). | **None on a clean seed** — the allowlist is `--seed`'ed from a clean-compiling compile unit. A genuinely new macro must be defined or explicitly allow-listed. |
| **C** fragile-accent-script | a math accent (`\check`,`\hat`,`\tilde`,…) as a bare sub/superscript argument (escaped `\^`/`\_` excluded). | Very low (pattern is specific). |
| **D** missing-input | an *unconditional* `\input`/`\include` whose target is absent. `\IfFileExists`/`\InputIfFileExists` (e.g. `print-mode.tex`) exempt. | **Zero** (filesystem check). |
| **E** math-delimiter-imbalance | a file with an odd count of unescaped `$` → `! Missing $ inserted`. | Very low (legit math always balances `$` within a file). |
| **F** environment-mismatch | per-file `\begin{X}`/`\end{Y}` stack mismatch or unclosed env. Strengthens the old `checkEnvironmentBalance` (which only caught a missing env *name*). | Very low (verbatim begin/end blanked; `document` balanced within main.tex). |
| **H** unmapped-unicode | a non-ASCII char with no `\newunicodechar` mapping AND not in the seeded unicode-safe set → inputenc "not set up for use with LaTeX". | **None on a clean seed** — mirrors B; inputenc-native chars are recorded at seed. |

All checks operate on comment- and verbatim-stripped text (verbatim /
lstlisting / minted / `\verb` / `\lstinline` removed), so a backslash or
`$` shown literally in documentation is never mis-read.

**Validation that it works:** reverting the `b9e19df6` source fixes and
rebuilding makes the linter flag all three with exact locations
(`main.tex:189,500`; `chapters/mass-theory.tex:8169`;
`chapters/mass-theory.tex:30814`); restoring the fixes → passes clean.

**Wiring:**

- `publish.yml` — gating step in the cheap, always-run `content-pipeline`
  job, right after `main.tex` is generated. Gates **every** PR
  irrespective of TeX-Live or the Actions billing state.
- `build.ts` — runs preflight after `--generate-main` for local feedback
  before push.
- `package.json` — `bun run latex-preflight` / `latex-preflight:seed`.

## 5. Maintenance

- When you add a **genuine** new standard/package command (and load its
  package in `latex/preamble.tex`), re-seed:
  `cd content && bun run latex-preflight:seed`. Commit the updated
  `latex-known-macros.json`.
- When you add a custom macro, define it **once** — in `latex/preamble.tex`
  *or* the manifest `macros:` block, never both (Check A).
- Never use a math accent as a bare sub/superscript — brace it (Check C).

## 6. Follow-ups

The three lower-frequency classes the history audit flagged (E `$`
imbalance, F begin/end mismatch, H unmapped unicode) were **implemented
in this PR** alongside A/B/C and D (missing-input) — see the check table
in §4. Each was validated by injecting the bug into the compile unit
(odd `$`, unclosed `\begin{quote}`, mismatched `\end{enumerate}`, an
unmapped `Ɱ` U+2C6E) and confirming the linter flags it while the clean
tree stays green (374 macros + 33 unicode-safe chars seeded).

No further preflight classes are outstanding. Possible future polish
(not gating, low value): cross-file environment nesting (currently
per-file, which is correct for this repo's main.tex/chapters layout) and
`\(`/`\)` `\[`/`\]` pairing (rare in the generated output, which uses
`$`/`$$` and named math environments).
