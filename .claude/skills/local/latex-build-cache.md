---
name: latex-build-cache
roles: [collaborator, owner]
user_invocable: true
description: >
  Set up, use, extend, debug, and VERIFY the LaTeX build cache — the
  three layers that stop the paper rebuilding from scratch every time:
  (1) a precompiled preamble format (`qou.fmt` via mylatexformat, keyed
  on `sha256(preamble.tex)`), (2) per-box diagram memoization
  (`memoize`), and (3) CI persistence (`actions/cache` for the format +
  `.memo/`). Read this BEFORE touching `latex/preamble.tex`,
  `content/pipeline/generate-main-tex.ts`, `scripts/build-fmt.sh`,
  `content/pipeline/latex-preflight.ts`, or the compile jobs in
  `.github/workflows/publish.yml`. Covers the no-TeX-engine verification
  loop (bun codegen checks + a real background `bun` build) since the dev
  sandbox has no `pdflatex` and CI is often `$`-billing-blocked.
allowed-tools: Read Bash Grep Glob Edit Write Skill
---

# LaTeX build cache

The paper is a 35-chapter / ~2900-block `report` with a heavy preamble
(`pgf`/`tikz`/`tikz-cd`/`hyperref` + ~128 `\newunicodechar`) and ~82
tikz pictures. A from-scratch compile re-parses the preamble on **every
latexmk pass × every compile unit** and re-renders **every** diagram.
This skill is the cache that avoids both.

> **Why not "cache each block's PDF and concatenate"?** LaTeX is a
> single-pass global typesetter — a block's numbering / pagination /
> refs depend on everything before it, so per-block PDFs can't be
> concatenated. Only *self-contained boxes* (diagrams) and the
> *preamble parse* are cacheable. That is exactly layers 1–2 below.
> Full rationale: [`docs/workplans/2026-06-14-latex-build-caching-strategy.md`](../../../docs/workplans/2026-06-14-latex-build-caching-strategy.md).

## When to invoke

- Setting up / extending / debugging the build cache.
- Editing `latex/preamble.tex` (it must stay **dumpable** — see §Rules).
- A `qou.fmt` build fails in CI (the `\endofdump` boundary question).
- Diagrams aren't being cached, or memoize errors.
- Verifying a build-pipeline change when there is no local TeX engine.

## Architecture — three layers

| Layer | What it caches | Mechanism | Key |
|-------|----------------|-----------|-----|
| **1. Preamble format** | the heavy preamble parse | `mylatexformat` dumps `latex/preamble.tex` → `qou.fmt`; `main.tex` starts with `%&qou` instead of inlining the preamble | `sha256(preamble.tex)` → `qou.fmt.sha` |
| **2. Diagram memoization** | each tikz / tikz-cd box | `\usepackage{memoize}` (live, never dumped) auto-caches pictures to per-box PDFs; needs `-shell-escape` | box source hash (memoize-managed, in `.memo/`) |
| **3. CI persistence** | layers 1+2 across CI runs | `actions/cache` for `qou.fmt` (+ `.sha`) and `.memo/` | preamble hash / content hash |

Layer 1 maps onto the repo's existing **sidecar staleness model**
(`*.qa.json` / `*.witness.json`): the format is stale iff its recorded
`sha256(preamble.tex)` drifts — a one-line compare.

**Enabler — fixed (declarative) numbering + per-section page break
(default-on, 2026-06-15).** Block output normally bakes in a
position-dependent number (Theorem 3.4.2), so it can't be cached across
edits. `render-latex.ts` removes that by computing numbers in the
pipeline and forcing them with `\setcounter` before each
chapter/section/subsection/numbered block (matching `report` + amsthm
`theorem`[section]); a block's `.tex` is then deterministic given its
source + number → cacheable, and native `\ref`/`\label` still resolve.
A `\clearpage` before each section/subsection makes a (sub)section's
internal layout independent of prior content (self-contained cacheable
unit). Kill-switches: `QOU_NO_FIXED_NUMBERING=1`,
`QOU_NO_SECTION_PAGEBREAK=1`. Residuals (debug later): equation numbers
(in block `.md`, not yet forced), TOC/page numbers (recomputed each
build), memoize-cross-ref-in-box (needs a TeX run).

## Components (the moving parts)

| File | Role |
|------|------|
| [`latex/preamble.tex`](../../../latex/preamble.tex) | the **dumpable** shared preamble (must stay free of per-render state — see Rules) |
| [`scripts/build-fmt.sh`](../../../scripts/build-fmt.sh) | builds `qou.fmt` via mylatexformat; hash-keyed cache; `--force`; `FMT_ENGINE` test hook |
| [`content/pipeline/generate-main-tex.ts`](../../../content/pipeline/generate-main-tex.ts) | `--use-format <name>` emits `%&<name>` (no inline preamble); `--memoize` emits a live, resilient `\usepackage{memoize}` |
| [`content/pipeline/build.ts`](../../../content/pipeline/build.ts) | threads `--use-format` / `--memoize` through `--generate-main` |
| [`content/pipeline/latex-preflight.ts`](../../../content/pipeline/latex-preflight.ts) | **format-aware**: when `main.tex` starts with `%&`, also walks `latex/preamble.tex` so its macros/unicode resolve |
| [`.github/workflows/publish.yml`](../../../.github/workflows/publish.yml) | default build path: content-pipeline generates with `--use-format qou --memoize`; `paper-pdf`/`diff-pdf` build `qou.fmt` + pass `-shell-escape` |

## How to use

```bash
# Build the format (idempotent; rebuilds only on preamble hash drift)
scripts/build-fmt.sh --preamble latex/preamble.tex --name qou        # [--force]

# Generate a main.tex that uses the format + memoizes diagrams
cd content && bun run pipeline/build.ts \
  quantum-observable-universe/quantum-observable-universe.ts \
  --out-dir ../chapters/ --generate-main --main-out ../main.tex \
  --preamble ../latex/preamble.tex --use-format qou --memoize

# Compile (the %&qou first line makes pdflatex load qou.fmt automatically)
latexmk -pdf -shell-escape main.tex
```

## Rules (do not regress these)

1. **`latex/preamble.tex` must stay dumpable** — NO per-render reads in
   it. The `\IfFileExists{print-mode.tex}` read lives in the *per-doc
   tail* (`generate-main-tex.ts`), not the preamble; `memoize` is loaded
   *live* in the tail, never dumped. Baking per-render state into the
   format freezes it at dump time (the bug class this skill exists to
   avoid).
2. **`memoize` needs `-shell-escape`** on every `latexmk` that compiles a
   memoized unit. The load is guarded by `\IfFileExists{memoize.sty}` so
   an older TeX distro degrades gracefully instead of aborting.
3. **`-shell-escape` is full shell access** — only enable it in CI /
   trusted local builds.
4. **The `\endofdump` boundary is empirical.** Most packages (incl.
   `hyperref`, `tikz`) dump fine because `mylatexformat` defers
   begin-document hooks. If a package errors under dumping, move *only
   that package* after `\endofdump` in `build-fmt.sh`'s driver — do NOT
   exclude `pgf`/`tikz` wholesale (that forfeits the biggest win).

## Verifying WITHOUT a TeX engine (the dev-sandbox reality)

There is usually **no `pdflatex` locally** and CI is often
`$`-billing-blocked (private-repo Actions minutes: runs complete in 0s
with 0 jobs = startup/billing failure, not code). So verify what you
can, and be explicit about what you can't:

1. **Codegen (bun-verifiable).** Assert the generated `main.tex` shape:
   ```bash
   bun -e 'import {generateMainTex} from "./content/pipeline/generate-main-tex.ts";
     const o=generateMainTex({title:"T",authors:["A"],macros:{},chapters:[]} as any,
       {preamblePath:"./latex/preamble.tex",chaptersDir:"chapters/",chapterSlugs:new Map(),useFormat:"qou",memoize:true});
     console.assert(o.split("\n")[0]==="%&qou" && !o.includes("\\documentclass") && /\\usepackage\{memoize\}/.test(o), "fmt+memoize codegen");
     console.log("codegen ok");'
   ```
2. **Real content build (the "rebuild as you edit" loop).** Run the
   actual pipeline to a scratch dir (no TeX needed — it only emits
   `.tex`), then run the **format-aware preflight** on the `%&qou`
   output; preamble macros must resolve (undefined-macro count ≈ 0,
   modulo pre-existing content bugs):
   ```bash
   cd content && bun run pipeline/build.ts <paper>.ts \
     --out-dir /tmp/fb/chapters --generate-main --main-out /tmp/fb/main.tex \
     --preamble ../latex/preamble.tex --use-format qou --memoize
   bun run pipeline/latex-preflight.ts /tmp/fb/main.tex
   ```
   Launch long builds with `run_in_background` so you never block.
3. **`build-fmt.sh` cache logic** is testable without TeX via the
   `FMT_ENGINE` stub hook (cold build / warm skip / hash-drift rebuild /
   `--force` / failure-safety). See the script header.
4. **The pdflatex/mylatexformat dump + the wall-clock delta are NOT
   locally verifiable** — say so. A `workflow_dispatch` run of
   `publish.yml` (once billing clears) settles the `\endofdump` boundary
   and measures the real speedup.

Prefer **sub-agents** to rebuild/verify components in parallel as you
edit when CI can't, or run [`/integration-audit`](integration-audit.md).

## Debugging

- **`qou.fmt` build fails** → a package isn't dump-safe; move it after
  `\endofdump` (Rule 4). `build-fmt.sh` prints the pointer.
- **Every macro "undefined" in preflight on a `%&` main.tex** → the
  format-aware branch in `latex-preflight.ts loadCompileUnit` regressed
  (it must walk `latex/preamble.tex`).
- **Diagrams not cached across CI runs** → layer 3 missing: add
  `actions/cache` for `qou.fmt`(+`.sha`) keyed on the preamble hash and
  for `.memo/`.
- **`memoize.sty not found` warning** → the runner's TeX is older than
  memoize; either upgrade the image or accept caching-disabled (compile
  still succeeds by Rule 2's guard).

## References

- **Testing instructions** (Track A no-engine + Track B with TeX Live, copy-paste):
  [`docs/latex-build-cache-testing.md`](../../../docs/latex-build-cache-testing.md)
- Strategy + verdicts (incl. why concat fails, LuaTeX, CI-image swap):
  [`docs/workplans/2026-06-14-latex-build-caching-strategy.md`](../../../docs/workplans/2026-06-14-latex-build-caching-strategy.md)
- CI billing signature: `CLAUDE.md` §"CI billing failures".
