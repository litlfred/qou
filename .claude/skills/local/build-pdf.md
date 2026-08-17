---
name: build-pdf
roles: [collaborator, owner]
user_invocable: true
description: >
  Builds the PDF locally in the workspace (main monolithic PDF and split
  per-chapter PDFs), and verifies the build is actually clean — errors,
  undefined references, and the preflight gate — rather than just
  producing a file.
allowed-tools: Bash AskUserQuestion run_command
---

# /build-pdf

Builds the paper locally (saves CI minutes, and CI auto-triggers are
disabled repo-wide anyway — see AGENTS.md §"NEVER merge to main without
`/prepare-merge`", Phase-4 verification gate). Produces `main.pdf` and
optionally the split per-chapter PDFs.

> **A file is not a pass.** `latexmk` exits 0 on a document riddled with
> undefined references and even with `! ` errors, because
> `-interaction=nonstopmode` presses on. Step 4 is the actual gate; do
> not report a successful build without it.

## Step 0 — prerequisites (a fresh sandbox has NEITHER)

Both of these are missing in a clean container, and both are easy to
misdiagnose as "the build is broken":

```bash
# 1. The content pipeline, schemas and preamble live in litlfred/folio-assistant.
#    Without this there is no ../folio-assistant at all.
scripts/setup-folio-assistant.sh

# 2. A TeX engine. NOTE: install-tex.sh moved with the platform in `miga` —
#    it is NOT scripts/install-tex.sh any more.
bash ../folio-assistant/scripts/install-tex.sh    # ~5 GB; run in background
```

`install-tex.sh` is slow; launch it with `run_in_background: true` and do
the content build (step 1) while it runs. Ready signal:
`kpsewhich memoize.sty` returns a path **and** `which latexmk` resolves.

## Step 1 — content build (`.tex` generation)

```bash
bun run --preload ./scripts/preload-registry.ts \
  ../folio-assistant/content/pipeline/build.ts \
  content/quantum-observable-universe/quantum-observable-universe.ts \
  --out-dir chapters/ \
  --generate-main \
  --main-out main.tex \
  --preamble ../folio-assistant/latex/preamble.tex
```

**The `./` in `--preload ./scripts/…` is required** — bun resolves a bare
`scripts/…` as a package specifier and fails with
`preload not found "scripts/preload-registry.ts"`. The path is
repo-local; it is not `../scripts/…`.

Read two lines of this output before going further:

- `Issues: N error(s), M warning(s)` — the content-level gate.
- `LaTeX preflight: ✓ clean (…)` — the fast static gate. If it reports
  issues, see §Preflight below *before* assuming your content is at fault.

## Step 2 — compile

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

Do **not** pass `-halt-on-error=false`; latexmk rejects it as an unknown
option and exits 2 without compiling anything.

Docker fallback if no engine is available:

```bash
docker run --rm --entrypoint "" -v $(pwd):/work -w /work \
  ghcr.io/litlfred/qou-paper-builder:latest latexmk -pdf main.tex
```

## Step 3 — split per-chapter PDFs (optional)

```bash
mkdir -p chapters-pdf/
python3 ../folio-assistant/scripts/split-pdf-by-chapter.py \
  --input main.pdf --output-dir chapters-pdf/
```

## Step 4 — VERIFY (this is the gate, not step 2)

```bash
L=main.log
echo "errors:    $(grep -c '^! ' $L)"
echo "citations: $(grep -c 'Citation .* undefined' $L)"
echo "refs:      $(grep -c 'LaTeX Warning: Reference' $L)"
echo "hyperrefs: $(grep -c 'Hyper reference' $L)"
echo "multidef:  $(grep -c 'multiply defined' $L)"
grep -oE '\([0-9]+ pages' $L | tail -1
```

All five should be **0**. Every one of them is a real defect a reader
meets: a `Hyper reference` warning is a link in the published PDF that
goes nowhere, not a cosmetic nag.

**Read the FINAL pass, not the first.** On pass 1 the `.aux` files do not
exist yet, so every reference is undefined by construction. Quoting those
numbers overstates the damage by ~10× (a first-pass log once read
"177 citations / 2672 hyper refs" against true values of 23 / 48).

Overfull boxes are ranked and located by:

```bash
bun run ../folio-assistant/content/pipeline/latex-overfull-report.ts main.log --min 50
```

Prefer it over grepping the log — the log gives a line number with no
file, this maps each box to its chapter and sorts by severity.

## Preflight false positives

`latex-preflight` gates on a **seed list** of known-good macros and
inputenc-safe characters (`content/pipeline/latex-known-macros.json`).
When the corpus starts using a standard command that is not yet seeded,
preflight reports it as undefined even though it compiles.

Rule for adding an entry: **it must compile in a real build**, not merely
look standard. And note that for unicode, *"unmapped" is not "crashes"* —
LaTeX's own `utf8.def` declares a large set (`↑` is fine), while `∇` and
`ˣ` genuinely abort. Only a compile probe distinguishes them:

```bash
# emit the candidate chars one per line into a doc using the REAL preamble
# and compile; whatever pdflatex rejects is the true crash set
```

## Delivering the PDF

`main.pdf` is gitignored (`*.pdf`). To hand it to the author, force-add it
to a dedicated artifact branch — never to a review PR, where a 7 MB binary
buries the diff:

```bash
git checkout -b claude/pdf-artifact-<utc-ymd>
git add -f main.pdf && git commit -m "artifact: main.pdf"
git push -u origin claude/pdf-artifact-<utc-ymd>
# → https://github.com/litlfred/qou/raw/<branch>/main.pdf
```

## Related

- [`local/latex-build-cache`](latex-build-cache.md) — what is and isn't
  worth caching (both standard mechanisms failed on this toolchain), plus
  `feature-build.sh` for changed-chapter drafts.
- [`local/markdown-render-check`](markdown-render-check.md) §2b — the two
  build-fatal authoring classes, and the criterion that catches them.
