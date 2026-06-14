# LaTeX build caching strategy

**Date:** 2026-06-14
**Status:** decision doc — captures the analysis from the stalled
agent discussion (no PR was produced the first time round) and answers
the author's two questions:

1. *"Can we cache the built content-block LaTeX binary and assemble at
   the end, so we don't trigger a rebuild every time — just a merge of
   content blocks and re-layout?"*
2. *"What about a `.fmt` dump cached before chapters begin processing?
   LuaTeX?"*

> **Verification note.** The development sandbox has **no TeX engine**
> (`pdflatex`, `lualatex`, `xelatex`, `latexmk`, `tlmgr` all absent —
> CI `apt-get install`s `texlive-full` per run). Every timing claim
> below is therefore a *reasoned estimate*, not a local measurement.
> The first implementation step is to **measure in CI** (or on the
> author's machine), because the right lever depends on the
> render-vs-typeset split, which we cannot observe here.

---

## TL;DR

| Idea | Verdict |
|------|---------|
| Cache each content block as a compiled PDF binary, concatenate at the end | ✗ **Does not work for flowing prose** — intrinsic to TeX, not a tooling gap (see §1). |
| `.fmt` dump (mylatexformat) of the preamble | ✓ **Yes — lowest-risk win, maps cleanly onto the sidecar-hash model** (§3). Bounded to preamble cost. |
| LuaTeX | ✗ **for speed**; it is *slower* and the `.fmt` dump saves *less* under it (Lua font state isn't dumpable). Its only real draw is deleting the 128 `\newunicodechar` lines — a maintenance cleanup, not a speed win (§4). |
| `memoize` diagram boxes | ✓ **This is the author's original "cache the built binary" idea, correctly scoped to boxes** (which survive re-layout) instead of prose (which doesn't). Biggest per-rebuild win for the 82 tikz-bearing files (§5). |
| Prebuilt TeX image + cache `_build/` in CI | ✓ **Biggest CI wall-clock win** — `texlive-full` is currently `apt-get install`ed in **three** separate jobs, and a `paper-builder-image` already exists but `publish.yml` doesn't use it (§6). |

**Ranked recommendation:** (1) measure the split; (2) prebuilt image +
`_build` cache in CI — cheap, big, no risk to output; (3) `.fmt` dump —
cheap, the author's stated direction; (4) `memoize` — the real
per-rebuild lever, more involved; (5) `\includeonly` for local
authoring iteration. LuaTeX migration is a *separate* maintenance
decision, not part of the speed work.

---

## Evidence (this corpus, today)

- **Engine:** `pdflatex` via `latexmk` (`.github/workflows/publish.yml`).
  Not LuaTeX.
- **Scale:** 35 chapters, **2944** `.md` content blocks, **82** files
  containing `tikzcd` / `tikzpicture`.
- **Preamble** (`latex/preamble.tex`, the production template):
  - **128** `\newunicodechar` declarations (pdflatex Unicode shim).
  - `tikz` + `tikz-cd` (⇒ full `pgf` macro layer — the single heaviest
    package load), `hyperref` (loaded last), `marginnote`, `titlesec`,
    `algorithm`/`algpseudocode`, `amsmath`/`amssymb`/`amsthm`/`mathtools`,
    `mathrsfs`, plus ~40 custom `\newcommand`s, 10 theorem environments,
    and the LeanBlueprint annotation macros.
- **Assembly** (`content/pipeline/generate-main-tex.ts`): the **entire
  preamble is inlined verbatim** into `main.tex`, then chapters are
  pulled in with **`\input{chapters/<slug>}`** (not `\include`). Each
  standalone appendix gets its **own copy** of the full preamble in a
  separate `.tex`, and the latexdiff job builds `main-diff.tex` too.
- **CI** (`publish.yml`):
  - `paper-pdf`, the standalone-appendix loop, and the diff job **each
    `apt-get install texlive-full`** (≈1–2 min apiece) — three times per
    run.
  - `paper-pdf` compiles the document **twice from scratch**: a
    `latexmk -pdf -draftmode` syntax check, then `latexmk -C` (wipes
    **all** `.aux`/`.toc`/`.fdb` state) + `rm -f main.fdb_latexmk`
    followed by a real `latexmk -pdf`. Deliberately zero incremental
    reuse.
  - The slow `content-pipeline` job is dominated by Python **witness
    regeneration**, gated by the `skip_witnesses` input — not LaTeX.

**Consequence:** the heavy preamble is parsed **many times per run** —
(number of compile units: main + each standalone appendix + diff) ×
(latexmk passes per unit, 2–3 for TOC/refs/bib) × (draftmode + real for
the main). That re-parse is exactly what a `.fmt` dump removes.

---

## §1 — Why "cache block binary, concat at the end" can't work for prose

LaTeX is a **single-pass global typesetter**. Every block's theorem
number, equation number, page number, cross-reference, float placement,
TOC entry, and hyperref anchor depends on the running state of
*everything before it*. You cannot compile block #1500 to a PDF in
isolation and drop it in, because its numbering and pagination are not
known until #1…#1499 have been laid out. "Re-layout" is not a cheap
merge step bolted onto cached binaries — it **is** the expensive pass
(TeX re-reads the whole token stream). This is intrinsic to the
algorithm, not a missing feature of `pdflatex`, and it is **equally
true under LuaTeX** — no engine offers incremental document-level
typesetting.

What *can* be cached are **self-contained boxes** whose internal layout
does not depend on surrounding state — display diagrams and heavy
standalone graphics. That is precisely what `memoize` does (§5), and it
is the correct realization of the author's instinct.

---

## §3 — `.fmt` dump (mylatexformat): yes, and it fits the sidecar model

A `.fmt` file is a precompiled **format** — TeX's memory image after
reading a set of macros. The base `pdflatex.fmt` is itself a dump of
the LaTeX kernel. `mylatexformat` (ships with TeX Live) lets us extend
that: dump the kernel **plus our whole shared preamble** (packages,
unicode shims, theorem envs, custom macros) into `qou.fmt` once. Every
subsequent `pdflatex -fmt=qou` then starts in the post-preamble state,
skipping the re-parse of `pgf`/`tikz`/`hyperref` + 128×`\newunicodechar`.
`mylatexformat` **defers `\AtBeginDocument` / begin-document hooks** so
they fire on the real run, not at format-build time — which is why
packages with runtime initialisation (hyperref's `.out`/bookmark write
streams, `tikz`/`pgf`) generally survive dumping. The minority that do
*not* dump cleanly are excluded with an explicit `\endofdump` placed
before them (see the boundary note below); the exact cut is an
empirical, per-package question to settle at implementation (no TeX
engine here to test it).

**Why it pays here specifically:** the preamble is heavy *and* re-parsed
N× across compile units and latexmk passes (see Evidence). The `.fmt`
amortizes all of that to a single build.

**It maps directly onto the existing `*.qa.json` / `*.witness.json`
sidecar staleness model:** key the format on `sha256(preamble.tex)`,
store `qou.fmt` + `qou.fmt.sha` as a cached artifact, and rebuild the
format **only when the preamble hash drifts** — identical discipline to
how sidecars invalidate on `source_hashes` drift.

### Honest sizing

The `.fmt` removes the **preamble** parse only. It does **not** touch
the body typeset (2944 blocks) or the 82 tikz renders — almost
certainly the dominant cost. Estimated saving: preamble-parse
(≈2–4 s) × (passes × units − 1) ≈ tens of seconds per CI run. Real and
free, but **not transformative on its own.** Pair it with §5/§6 for the
big wins.

### Clean dump boundary (what stays per-document)

The format must contain only **shared** state. These stay out of the
dump, emitted per-`.tex` by `generate-main-tex.ts` (they already are,
except the last item):

- `\title` / `\author` / `\date` and per-doc `\hypersetup{pdftitle…}`
  — already in the per-doc section.
- `\IfFileExists{print-mode.tex}{\input{print-mode.tex}}{}` — currently
  the **last line of `preamble.tex`**. It sets `\ifshowaffiliations`
  from a per-render flag; baking it into the format would freeze the
  flag at format-build time. **Move it into the generated per-doc
  preamble** (or place `\endofdump` before it). This is a small,
  bun-verifiable refactor and the only preamble change `.fmt` requires.

**Non-dumpable packages (review note — Gemini on #2310).** The standard
caution is that `hyperref` (and occasionally `pgf`/`tikz`) cannot be
serialised into a format because they open write streams or do runtime
catcode work. That caution is real but usually too strong here:
`mylatexformat`'s begin-document-hook deferral handles most of it —
precompiling `tikz` is a classic use case and `hyperref` is routinely
dumped — and moving `pgf`/`tikz` out of the dump would forfeit the
*heaviest* part of the win. Discipline: attempt to dump the whole
shared preamble; if a specific package errors or breaks links under the
format, move **only that package** after `\endofdump` so it loads live.
Settle the exact boundary empirically when the format build runs in CI.

### Implementation sketch (each step its own commit)

1. `generate-main-tex.ts`: split `emitPreambleAndMacros` so the
   shared, dumpable preamble is emitted to a stable file and the
   per-doc tail (print-mode, metadata) is emitted separately. Add a
   `--use-format <name>` option that emits a thin `main.tex` consuming a
   prebuilt format. **Verifiable with `bun` (checks generated `.tex`).**
2. `scripts/build-fmt.sh`: `pdflatex -ini -jobname=qou "&pdflatex"
   mylatexformat.ltx preamble.tex` → `qou.fmt`, guarded by a
   `sha256(preamble.tex)` check. **Needs a TeX engine to verify (CI /
   author).**
3. `publish.yml`: build/restore `qou.fmt` (cache-keyed on the preamble
   hash) before the compile steps; pass `-fmt=qou` (or `%&qou`).
   **CI-verified.**

---

## §4 — LuaTeX: three separate questions

1. **As a speed play — no.** LuaLaTeX is typically ~2–4× slower per run
   than pdflatex for equivalent documents. Switching engines to go
   *faster* is backwards; the body typeset would get slower.
2. **For the `.fmt` dump — it saves *less* under LuaTeX.** A LuaTeX
   format preserves TeX macro memory but **not Lua state**: `luaotfload`
   (the font machinery) re-initializes on every run via callbacks
   regardless of the dump. On a font-heavy preamble that startup cost is
   exactly what you *can't* capture. pdflatex's `.fmt` is "purer" —
   everything in it is dumpable TeX macros — so **pdflatex +
   mylatexformat captures a larger fraction of the preamble cost than
   LuaTeX would.**
3. **The one legitimate LuaTeX angle — maintenance, not speed.** The
   128 `\newunicodechar` lines (and the `\unimathsafe` shim) exist
   *only* because pdflatex cannot ingest raw Unicode. LuaLaTeX/XeLaTeX
   handle UTF-8 natively, so that whole block could be **deleted**
   (note the accreting dated comments: *"added to fix LaTeX errors"*,
   *"2026-05-29 PDF-compile fix"* — every new glyph in prose currently
   needs a new mapping). That is a real correctness/maintenance win, but
   it is a **larger migration** (fontspec, font selection, possible
   layout shifts across 35 chapters), it makes raw compile slower, and
   it is **orthogonal to caching.** Defer it; do not bundle it with the
   speed work.

---

## §5 — `memoize`: the author's "cache the built binary", scoped to boxes

`memoize` compiles each marked box (the 82 tikz-cd / tikzpicture
diagrams + heavy display math) to its **own PDF**, hash-keyed on the box
source, in a `.memo` cache dir. On rebuild, an unchanged box becomes a
cheap `\includegraphics` of the cached PDF instead of re-running
`pgf`/`tikz` — the single most expensive per-diagram cost. Those cached
files **are sidecars** (same hash-on-source pattern) and **survive
re-layout** (the saved box is re-inserted wherever pagination lands
it). This is the correct, working form of "cache the built content-block
binary and re-assemble."

Cost: needs `-shell-escape`, and the renderer (`render-latex.ts`) must
wrap diagram output in the memoize environment. More involved than
`.fmt`, but it is the lever that actually attacks the per-rebuild body
cost.

---

## §6 — CI is where the wall-clock actually is

- **Prebuilt image:** `build-latex-image.yml` / `paper-builder-image.yml`
  already exist, yet `publish.yml` still `apt-get install texlive-full`
  in **three** jobs. Switching those jobs to `container:` the prebuilt
  image removes ~1–2 min × 3 of apt per run, **zero risk to output.**
  This is the cheapest big win and should likely go first.
- **Cache `_build/`:** keep `*.aux`/`*.toc`/`*.fdb_latexmk`/`*.bbl` +
  `qou.fmt` + `.memo/` in `actions/cache`, keyed on a content hash, so a
  run that only changed one chapter reuses the rest. (Note: the current
  `latexmk -C` + `rm -f main.fdb_latexmk` deliberately destroys this —
  that workaround exists for a draftmode/up-to-date bug; revisit it when
  wiring the cache.)
- **`skip_witnesses`:** already available; default it on for
  preview/non-release builds since witness regen, not LaTeX, dominates
  `content-pipeline`.

---

## §7 — `\includeonly` (local authoring only)

Switch chapter emission from `\input{}` to `\include{}` (the renderer
already `\clearpage`s each chapter, so the forced page break is free),
then `\includeonly{<changed-chapter>}` recompiles only that chapter,
reading the cached `.aux` of the other 34 to preserve their numbers and
refs. Caveat: page numbers freeze until a full pass — perfect for
authoring/preview, redo one full build for the final PDF. Lower priority
than CI work because it helps the local loop, not the published
artifact.

---

## Next steps (author picks)

1. **Measure first** (CI or author machine): time `bun` render vs
   `latexmk` typeset, and preamble-parse vs body, so we optimize the
   real bottleneck. No output change.
2. **CI: prebuilt image + `_build` cache** (§6) — cheapest big win.
3. **`.fmt` dump** (§3) — the author's stated direction; preamble split
   is bun-verifiable, format build is CI-verified.
4. **`memoize` diagram boxes** (§5) — the real per-rebuild lever.
5. **`\includeonly`** (§7) — faster local authoring iteration.

LuaTeX migration (§4) is tracked separately as a maintenance cleanup,
not part of this speed work.
