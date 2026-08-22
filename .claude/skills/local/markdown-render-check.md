---
name: markdown-render-check
roles: [reader, collaborator, owner]
---

# Markdown Render Check

## Role

After editing or creating `.md` content blocks, verify the file
renders correctly on GitHub (the canonical view alongside the
LaTeX/HTML pipelines). GitHub's renderer is stricter than the LaTeX
pipeline about a handful of patterns — especially math display blocks
that get hijacked by markdown's list parser. This skill catches those
before the user sees them in the browser.

## When to use

**MANDATORY before every commit that creates or edits a math-bearing
`.md`** (per AGENTS.md §"Render-QA gate for math-bearing `.md`"). This is
an agent-owned gate — do **not** defer it to CI (which may be billing-flaky)
or to the author's eyes.

- After editing any `.md` file that contains math (`$...$`, `$$...$$`,
  or fenced ```tex blocks).
- As a final pass when running `prepare-merge` or any review skill on
  content blocks.
- After authoring a new `.md` with multi-line display math, tables,
  or lists adjacent to math.

Run the pipeline render where available
(`bun run content/pipeline/render-latex.ts <paper>` after
`scripts/setup-folio-assistant.sh`). **When it cannot run** (e.g. the
`folio-assistant` clone is firewalled in a sandbox), run the grep battery
(§2) + the expository pass (§2c) by hand, and **say in the commit/PR that
the change was not machine-validated** — never report a math edit as
render-checked when only CI would have caught a break.

## Method

### 1. Identify changed `.md` files

```bash
# Files changed vs. the most recent commit
git diff HEAD~1 HEAD --name-only -- '*.md'

# Files changed vs. base branch (when reviewing a PR/branch)
git diff origin/main...HEAD --name-only -- '*.md'
```

### 2. Run the automated grep checks

These patterns are common rendering breaks. Run each grep against the
changed files; any hit is a likely failure.

| Check | Grep | What breaks |
|-------|------|-------------|
| `+` / `-` / `*` at line start inside `$$...$$` | `awk '/^\$\$/{m=!m; next} m && /^[+\-*] /' file.md` | Continuation line of a multi-line display equation gets parsed as a bulleted list, breaking out of math mode. |
| Missing blank line before `$$` | `grep -nB1 '^\$\$' file.md \| awk 'NR%3==1 && $0!~/^--$/ && $0!~/^[[:space:]]*$/' ` | `mdToHtml` regex needs a paragraph break before `$$` to detect display math. |
| `\operatorname{` in math | `grep -n '\\\\operatorname{' file.md` | KaTeX rejects without an extension; use `\mathrm{}`. |
| `\cite{` in non-paper context | `grep -n '\\\\cite{' file.md` | OK in this repo (handled by both pipelines), but verify the key exists in `references.ts`. |
| Tab characters in math | `grep -nP '\t' file.md` | Inconsistent rendering; replace with spaces. |
| Bare `_` outside math | `grep -nE '[^$\\][_][^$]' file.md` | LaTeX subscript trigger; wrap identifier in backticks or `$...$`. |
| Unbalanced delimiters | `python3 -c "import re,sys;s=open(sys.argv[1]).read();b=re.sub(r'\x60\x60\x60.*?\x60\x60\x60','',s,flags=re.S);print('fences',s.count('\x60\x60\x60'),'\$\$',b.count('\$\$'),'lone\$',re.sub(r'\$\$','',b).count('\$'),'{}',s.count('{'),s.count('}'))" file.md` | Each count must be even / equal. An odd `$` or `$$`, or `{`≠`}`, breaks the whole block (and often the rest of the file). Also check `\bigl`=`\bigr`, `\Bigl`=`\Bigr`, `\left`=`\right`, `\begin{`=`\end{`. |
| `aligned`/`align` inside `$$` | `awk '/^\$\$/{m=!m} m && /\\begin\{align/' file.md` | Align-family environments belong in a fenced ` ```tex ` block (AGENTS.md §"TeX authoring patterns" item 5), not inline `$$…$$` — the unified-latex AST validator and KaTeX both choke on some forms. |
| **Inner math env with no envelope** (BUILD-FATAL) | `bun run content/pipeline/qa-sweep.ts <block> --only render-math-mode-envelope` | See §2b — moving an align-family env into a ` ```tex ` fence per the row above is only half the job; it still needs a math envelope. |
| **Unicode with no LaTeX setup** (BUILD-FATAL) | see §2b | A char with no `\newunicodechar` mapping *and* no `utf8.def` declaration aborts pdflatex in prose, `\texttt` and math alike. |
| **Glued control sequence** (SILENT) | `bun run content/pipeline/glued-macro-scan.ts <file>` | `\pi c_s` written without the space is one macro named `pic`. Undefined, it stops the build — harmless. *Defined*, the page compiles and prints something else: `\pic` expanded to `\pi` and deleted a sound speed from a Hawking-temperature denominator. Fix the space; **never define the glued name.** |
| **Fence that cannot close its block** (BUILD-FATAL) | `bun run content/pipeline/fence-close-check.ts <file>` | Under CommonMark a **closing** fence carries no info string, so a second ` ```tex ` does **not** close the first — the block stays open and the rest of the file is raw passthrough. **Parity misses this**: the broken file had an even fence count, and a parity scan over the whole corpus reported zero while two files were unbuildable. |

### 2b. The two build-fatal classes (run the criterion, don't eyeball)

These two abort the whole 1000-page compile, and both have recurred
after being fixed — so they are now mechanical criteria rather than
review advice. Run them on any block you touch:

```bash
bun run content/pipeline/qa-sweep.ts <path-to-block> --only render-math-mode-envelope
```

**1. Inner-only math env with no envelope.** LaTeX splits math
environments into two kinds, and the distinction is invisible until the
build dies:

- **outer** — `equation`, `align`, `alignat`, `gather`, `multline`,
  `flalign`, `displaymath`, and the `$$…$$` / `\[…\]` delimiters. These
  *enter* math mode.
- **inner** — `aligned`, `gathered`, `split`, `cases`, `matrix` and its
  delimiter variants, `smallmatrix`, `array`, `subarray`. These typeset
  a sub-box and are legal *only inside* math mode.

A ` ```tex ` fence is raw passthrough. A fence that opens directly with
an inner env therefore lands in horizontal mode:

````md
```tex
\begin{aligned}          ← BUILD-FATAL: three errors from one slip
  a &= b \\ c &= d
\end{aligned}
```
````

gives `! Package amsmath Error: \begin{aligned} allowed only in math
mode` plus two `! Missing $ inserted`. Fix by wrapping in `\[ … \]`
(keeps `aligned`), or by switching to the outer `align`/`align*` form.

> **Do not hand-roll this grep.** `\begin{align` is a *prefix* of
> `\begin{aligned}`, so the obvious "is an outer env present?" guard
> matches the very thing it is meant to catch and passes on every real
> defect. A scan written that way reported **0** corpus hits against a
> true count of **2**. Also, inline `$…$` legitimately spans newlines
> (§"TeX authoring patterns" item 2), so a line-bounded stripper
> mis-flags every multi-line inline formula. The criterion handles both.

**2. Unicode with no LaTeX setup.** *"Unmapped" is not the same as
"crashes"* — LaTeX's own `utf8.def` declares a large set, so `↑` is
fine while `∇` and `ˣ` abort with `Unicode character … not set up for
use with LaTeX`. Do not try to judge a char by eye or by grepping the
preamble's `\newunicodechar` list alone.

As of the render-crash-guards change (folio-assistant#129), fenced code
**and** inline code are both transliterated, so `` `q : Rˣ` `` now
renders as `R^x` instead of killing the build. The residual risk is a
crash-class char in **plain prose or a block title**, where no
transliteration applies. If you paste a Lean/Unicode-heavy identifier
into prose or a `.ts` `title:`, put it in backticks or replace the char
with its ASCII form.

### 2c. Expository pass — notation introduced before use

A block that compiles can still read as gibberish to someone who has not
read the rest of the paper. For survey / overview / self-contained blocks
especially, after the render greps pass, walk the prose once more and check:

1. **Every symbol is glossed at or before first use.** Read top to bottom;
   the first time a symbol appears it must be named (e.g. `$z$`, the Markov
   parameter; `$\hbar_q = 1-q^{-1}$; `$\ell(w)$`, the Coxeter length). A
   symbol pulled from another chapter without a one-clause gloss is a gap.
2. **No symbol carries two meanings.** Reuse of one letter for two distinct
   objects (the classic: `$\lambda = \ln q$` *and* the partition
   `$\lambda \vdash n$`) is a coherence defect — rename one (here `$\eta=\ln q$`).
   Check against the notation register (`notation/notation-collisions.md`).
3. **Each named observable uses its canonical register** — fraktur for
   physical observables (`$\mathfrak{m}, \mathfrak{E}, \mathfrak{Q}_\beta,
   \mathfrak{V}$`), and the *right* one (mass `$\mathfrak{m}$` is not binding
   `$B$`; a box labelled "the mass" must not be tagged `$B(\cdot)$`).
4. **The story has no forward-dependency gaps** — a term used in step *k*
   whose only definition is in step *k+3* should get a parenthetical gloss
   at *k* ("…the Coxeter length (Step 7)…").

Report each undefined-on-first-use symbol, collision, and register
mismatch with its line number, the same way as the grep checks.

### 3. Manual GitHub verification

For each changed `.md`, hand the user the blob URL on the pushed
branch so they can verify rendering in the browser:

```
https://github.com/litlfred/qou/blob/<branch>/<path-to>/<file>.md
```

Always link the `.md` (the rendered view), never the `.ts` or `.lean`
sibling — see `AGENTS.md` "Always provide GitHub links — default to
`.md`" for the rule.

The repo is private; WebFetch and `raw.githubusercontent.com` return
404 unless authenticated. The MCP `mcp__github__get_file_contents`
tool returns raw source only, not the rendered HTML. So *automated*
rendered-view inspection isn't possible from this skill — the
author's eyes on the GitHub blob URL are the ground truth.

## Multi-line display equations — fix recipe

The single most common breakage. **Wrong** (each `+` becomes a bullet):

```md
$$
F(x) = a
+ b
+ c
$$
```

**Right** — operator at end of line, no list trigger:

```md
$$
F(x) = a \;+\;
       b \;+\;
       c
$$
```

`\;` controls the spacing; `,`/`;` after the operator are also fine.
The rule: never start a line inside `$$...$$` with `+`, `-`, or `*`.

## Output

Report each check that failed, with file path and line number, then
list the GitHub blob URLs for the user to eyeball.

If all checks pass, say so explicitly and still print the blob URLs
— the user always wants the link list at the end.

## Cross-references

- `md-authoring` — the authoring conventions this skill verifies.
- `latex-validation` — LaTeX-side render checks (complementary).
- `html-rendering-qc` — HTML viewer (`mdToHtml`) rendering.
- `rendering-auditor` — full pass over rendered LaTeX/HTML output.
