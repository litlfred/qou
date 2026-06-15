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

---

## Implementation status & CI billing blocker (2026-06-15)

### Landed + verified on PR #2310

| Piece | State | Verification |
|-------|-------|--------------|
| Decision doc (this file) | ✅ | — |
| **print-mode split** — per-render `\IfFileExists{print-mode.tex}` moved out of the dumpable `latex/preamble.tex` into the per-document section (`generate-main-tex.ts`) | ✅ | bun check; default output order-equivalent |
| **`--use-format <name>` codegen** — `generate-main-tex` / `build.ts` emit `%&<name>` instead of inlining the preamble; per-doc tail stays live; default unchanged | ✅ | bun check, 14 assertions (both modes + standalone) |
| **`scripts/build-fmt.sh`** — hash-keyed (`sha256(preamble.tex)` → `<name>.fmt.sha`) preamble→`.fmt` cache; rebuild only on drift / `--force` | ✅ cache logic | stubbed-engine test, 8/8 (cold/warm/drift/force/failure-safety) |

### Blocked — needs a TeX run AND/OR Actions billing to clear

**CI billing diagnosis (definitive).** The repo is **private**, and every
recent push triggers a `paper-builder-image` run that completes in **0 s
with 0 jobs** (`run 27512169900`: `conclusion=failure`, `total_jobs=0`,
`run_started_at == updated_at`). A run created with **no job launched** is
a *startup failure* — on a private repo across all branches, the
Actions-minutes/spending-limit signature from CLAUDE.md
§"CI billing failures". (The `publish.yml` runs that show *real*
durations are from **2026-06-11**, before the exhaustion, so they don't
contradict this.) **Consequences:** ① none of the LaTeX work can be
compile-verified in CI; ② the `paper-builder-image` is not building, so
the **CI-image swap has no fresh image to consume**; ③ per the billing
rule, **do not push retrigger commits** — this clears only when the
**owner** fixes billing / raises the spending limit. There is also no
local TeX engine in the dev sandbox, so local compile-verify is
unavailable too.

| Piece | Why blocked |
|-------|-------------|
| The actual `.fmt` *dump* (`build-fmt.sh` running real `pdflatex -ini … mylatexformat`) | no TeX engine locally; CI billing-blocked. The `\endofdump` boundary (does `hyperref`/`pgf` dump cleanly?) is the empirical question to settle on first real run. |
| `publish.yml` `.fmt` wiring | spans 4 jobs (content-pipeline regen → paper-pdf / appendix-pdfs / diff-pdf each need `qou.fmt`); unverifiable + unrunnable now. Recipe below; apply when a TeX run is available. |
| **memoize** | needs `-shell-escape` (else compile errors) + must load *live* per-render, not in the dumped preamble (same freeze hazard as print-mode). Unverifiable now. |
| CI-image swap + `_build` cache | gated on `paper-builder-image` building, which is the thing billing-failing. |

### Ready-to-apply CI wiring (`.fmt`), for when a TeX run is available

Gate behind a default-`false` `workflow_dispatch` input so the normal
pipeline is provably unchanged:

```yaml
# publish.yml  on.workflow_dispatch.inputs:
use_fmt:
  description: "Compile via a precompiled preamble format (qou.fmt)."
  required: false
  default: false
  type: boolean
```

1. **content-pipeline** (has `bun`, no TeX) — after preflight, before
   artifact upload, regenerate when `inputs.use_fmt`:
   `bun run pipeline/build.ts … --generate-main --use-format qou`
   (emits `%&qou` main.tex + standalone appendices).
2. **paper-pdf / appendix-pdfs / diff-pdf** (have TeX) — before each
   compile, when `inputs.use_fmt`:
   `bash scripts/build-fmt.sh --preamble latex/preamble.tex --name qou`
   so `qou.fmt` exists in the compile CWD (pdflatex resolves `%&qou`).
3. **Fallback:** if `build-fmt.sh` exits non-zero, re-run the
   content build *without* `--use-format` (inline preamble) so the PDF
   still emits — `.fmt` is a pure optimization, never a hard dependency.

memoize, when enabled, additionally needs `-shell-escape` on every
`latexmk` invocation and a persisted `.memo/` cache dir
(`actions/cache`); load `memoize` live (per-render), not in `qou.fmt`.

### What the owner needs to do to unblock

1. **Fix Actions billing / raise the spending limit** (only the owner
   can) — this is the gate on *all* CI verification.
2. Then a run of `publish.yml` settles the `\endofdump`/`hyperref`
   boundary and measures the real wall-clock delta.

---

## FINAL 2026-06-15 — both cache mechanisms non-functional on the toolchain; REVERTED

Real-engine testing (texlive-full 2023, installed in-sandbox via
`scripts/install-tex.sh`) refuted both layers. **The default build is
plain inline-preamble + full latexmk; there is no preamble or diagram
cache.** Authoritative findings: [`.claude/skills/local/latex-build-cache.md`](../../.claude/skills/local/latex-build-cache.md) §Negative results.

| Mechanism | Verdict | Root cause |
|-----------|---------|-----------|
| `.fmt` (mylatexformat `%&qou`) | unusable | mylatexformat gobbles everything between `%&fmt` and `\begin{document}` → drops per-paper manifest macros (`\ordw` …) + the per-render memoize `\usepackage`. |
| memoize | unusable for tikzcd | this TeXLive lacks memoize's tikz library; the manual env breaks tikzcd's `&` catcode; all 74 diagrams are `tikzcd` (0 `tikzpicture`) → 0 boxes cache. |
| tikz `\tikzexternalize` | aborts on tikzcd | collects until `\end{tikzpicture}`; tikzcd ends `\end{tikzcd}`. |
| fixed numbering + per-section `\clearpage` | reverted | enablers for block caching that none of the above delivered. |

**Reverted** (commit *"de-default broken LaTeX cache …"*): removed
`--use-format`/`--memoize` from the pipeline + `publish.yml`, deleted
`scripts/build-fmt.sh`, reverted fixed-numbering/page-break, deleted the
`actions/cache` steps.

**Kept (genuinely useful):** `scripts/install-tex.sh` (get a TeX engine
into the sandbox) and `scripts/feature-build.sh` (quick changed-chapter
preview + diffs, inline). Plus the content compile-bug fixes surfaced by
the first real compile (`ż`/`𝓕`/`📝` + an unescaped `%` in `:val` units).

**The only viable diagram cache** is a `standalone`-package restructure
(render each tikzcd → its own PDF → `\includegraphics`); large, deferred
to a future PR.

---

## MEASURED 2026-06-15 — real-engine numbers settle the priority (texlive-full 2023, in-sandbox)

With a real `pdflatex` (installed via `scripts/install-tex.sh`), the
previously *estimated* split was finally measured. **The body, not the
preamble or the diagrams, is ~95% of the cost — and it is intrinsically
uncacheable.** This refutes the diagram-cache premise (§5) *and* caps the
`.fmt` win (§3) at a few percent.

| Measurement | Wall | Note |
|-------------|------|------|
| Real `main.tex`, **one `pdflatex -draftmode` pass** (33 chapters, 2944 blocks) | **14.0 s** | the actual unit cost |
| Preamble/startup portion (toy doc, inline preamble) | ~0.7 s | ≈ 5% of a real pass |
| 10 `tikzcd` **inline** vs baseline | **~0 ms** (within noise) | commutative diagrams are light; **not** the bottleneck |
| 1 `standalone` diagram build (subprocess) | **0.63 s** | caching a diagram *costs* 0.63 s to save ~0 ms → **net-negative** |
| `%&qou` format load vs inline preamble (toy) | 0.28 s vs 0.73 s | `.fmt` saves ~0.45 s of **startup** … |
| …same 0.45 s as a fraction of a real 14 s pass | **~3%** | …which the 14 s body dwarfs |

**Per-chapter profile** (each row incl. ~0.7 s shared startup): the body
is *concentrated*, not uniform — `mass-theory` **3.5 s** +
`quantum-observable-universes` **3.3 s** are ~40% of the 14 s
(math/table-heavy), the other 31 chapters a ~1 s/chapter tail. That is
display-math + `amsmath`/table typesetting — intrinsic, **uncacheable** in
pdflatex.

**Whole-pipeline ranking (where the CI wall-clock actually is)** — LaTeX
is *not* the dominant cost: witness regen (Python, ~36 min, gated by
`skip_witnesses`) ≫ `texlive-full` install ×3 (~3–6 min, fixed by the CI
image) ≫ LaTeX compile (14 s × passes × ~7 units ≈ 2–3 min) ≫ bun render.
The diagram/`.fmt` caching effort was optimizing the ~2 min item.

**Diagram-cache mechanisms, re-confirmed on the real engine** (probe
battery, [`/tmp/texprobe`]): `memoize` ❌ fatal (`Extraction of externs …
no output PDF` — texlive-2023 ships no memoize tikz library, dir holds
only `memoize.sty`/`memoizable.sty`/`nomemoize.sty`); `\tikzexternalize`
❌ fatal (`Runaway argument … collect@until@end@tikzpicture` — tikzcd ends
`\end{tikzcd}`); `standalone` `\includestandalone` ✅ compiles — but per
the timing above it would *slow the build down*, so even the "viable" path
is not worth wiring. Corpus diagram census: **94 `tikzcd` blocks vs 6
`tikzpicture`** (79 vs 2 files) — tikzcd-only, as the revert said.

**`.fmt` re-confirmed broken** on this preamble: the format builds only
with `\endofdump` *before* `hyperref` (Gemini's review note was right),
and then per-doc macros **drop** (`\ordwtest` absent from the PDF) with
`Unicode character ^^H/^^G` corruption — the `inputenc` + 128×
`\newunicodechar` active-char machinery does not survive the dump/`%&qou`
reload. Even if fixed, the win is ~3% of a pass. **Not pursued.**

### Revised priority (measured, not estimated)

1. **Prebuilt CI image (§6) — the only big win.** `texlive-full` is
   `apt-get install`ed in **3** jobs (~3–6 min/run total). Wiring those
   jobs to `container: ghcr.io/litlfred/qou-paper-builder` removes it
   with zero output risk. **Implemented this PR** (+ fixed
   `paper-builder-image.yml`, which only triggered on `workflow_dispatch`
   so the image was never actually built — now builds on main pushes that
   touch the Dockerfile + monthly cron).
2. **Cut redundant full-compiles in CI** — the body is 14 s/pass; the
   pipeline runs draftmode + full + appendices + diff (each ≥1 pass).
   Eliminating duplicated 14 s passes beats any in-engine cache.
3. **`skip_witnesses`** for preview builds — Python witness regen
   (~36 min), not LaTeX, dominates `content-pipeline`.
4. **Diagram cache / `.fmt`: do NOT re-attempt** — measured non-wins /
   broken (this section). The next agent reading "cache the diagrams"
   should stop here.
5. Sub-second *rebuilds* (the original ask) require an **incremental
   engine (Typst)** — a separate migration, not a pdflatex cache; the
   single-pass global typeset (§1) is confirmed uncacheable by the 14 s
   measurement.

> Pre-existing content bug surfaced by the real compile (out of scope for
> this cache work, not introduced here): **14 `! Double subscript` math
> errors** in the generated chapters (e.g. `x_i_j` / `q^a_b`-style nested
> sub/superscripts). Worth a separate `fix(latex)` pass.

