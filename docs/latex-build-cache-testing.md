# LaTeX build cache — testing instructions

Concrete, copy-pasteable steps to verify the 3-layer LaTeX build cache
end-to-end. Two tracks:

- **Track A — no TeX engine** (what runs in this dev sandbox / on any
  machine with just `bun`): codegen + cache-logic + preflight checks.
  These are the gates an agent can run while editing.
- **Track B — with TeX Live** (a machine / CI with `pdflatex`,
  `mylatexformat`, `memoize`): the actual compile, the `\endofdump`
  boundary, memoize reuse, and the wall-clock speedup. Run this once
  Actions billing clears (a `workflow_dispatch` of `publish.yml`) or on
  a local TeX install.

Skill: [`.claude/skills/local/latex-build-cache.md`](../.claude/skills/local/latex-build-cache.md).
Strategy + rationale: [`docs/workplans/2026-06-14-latex-build-caching-strategy.md`](workplans/2026-06-14-latex-build-caching-strategy.md).

---

## Track A — no TeX engine (bun only)

Run from the repo root.

### A1. Codegen — `--use-format` + `--memoize` shape

```bash
bun -e '
import {generateMainTex} from "./content/pipeline/generate-main-tex.ts";
const p:any={title:"T",authors:["A"],macros:{},chapters:[]};
const base={preamblePath:"./latex/preamble.tex",chaptersDir:"chapters/",chapterSlugs:new Map()};
const def=generateMainTex(p,base);
const fmt=generateMainTex(p,{...base,useFormat:"qou",memoize:true});
const a=[
  ["default inlines \\documentclass", def.includes("\\documentclass")],
  ["fmt first line %&qou", fmt.split("\n")[0]==="%&qou"],
  ["fmt does NOT inline preamble", !fmt.includes("\\documentclass")],
  ["fmt loads memoize live", /\\usepackage\{memoize\}/.test(fmt)],
  ["fmt keeps print-mode read live", fmt.includes("\\IfFileExists{print-mode.tex}")],
];
let ok=true; for(const[k,v]of a){console.log((v?"PASS":"FAIL")+" "+k); if(!v)ok=false;}
process.exit(ok?0:1);'
```
**Expect:** 5× PASS, exit 0.

### A2. `build-fmt.sh` cache logic (stubbed engine — no real dump)

```bash
tmp=$(mktemp -d); mkdir -p "$tmp/latex" "$tmp/out"
printf 'V1\n' > "$tmp/latex/preamble.tex"
printf '#!/usr/bin/env bash\n: > "$3/$1.fmt"\n' > "$tmp/stub.sh"; chmod +x "$tmp/stub.sh"
cd "$tmp"
FMT_ENGINE="$tmp/stub.sh" bash "$OLDPWD/scripts/build-fmt.sh" --preamble latex/preamble.tex --name qou --out-dir out   # builds
FMT_ENGINE="$tmp/stub.sh" bash "$OLDPWD/scripts/build-fmt.sh" --preamble latex/preamble.tex --name qou --out-dir out   # "up-to-date — skip"
printf 'V2\n' > latex/preamble.tex
FMT_ENGINE="$tmp/stub.sh" bash "$OLDPWD/scripts/build-fmt.sh" --preamble latex/preamble.tex --name qou --out-dir out   # rebuilds (hash drift)
cd "$OLDPWD"
```
**Expect:** run 1 "building", run 2 "up-to-date — skip", run 3 "building".

### A3. Format-aware preflight on a generated `%&qou` main.tex

```bash
cd content && bun run pipeline/build.ts \
  quantum-observable-universe/quantum-observable-universe.ts \
  --out-dir /tmp/fb/chapters --generate-main --main-out /tmp/fb/main.tex \
  --preamble ../latex/preamble.tex --use-format qou --memoize
bun run pipeline/latex-preflight.ts /tmp/fb/main.tex; cd ..
```
**Expect:** `head -1 /tmp/fb/main.tex` is `%&qou`; preflight reports
**no `undefined-macro` for preamble macros** (defined ≈ 77). Any
`undefined-macro` for a preamble macro ⇒ the format-aware branch in
`latex-preflight.ts` regressed. (Pre-existing content issues —
`math-delimiter-imbalance`, `unmapped-unicode` — are unrelated to the
cache and appear in inline mode too.)

---

## Track B — with TeX Live (pdflatex + mylatexformat + memoize)

### B0. Confirm tools

```bash
pdflatex --version | head -1
kpsewhich mylatexformat.ltx        # layer 1 — must print a path
kpsewhich memoize.sty              # layer 2 — empty ⇒ caching auto-disabled (still compiles)
```

### B1. Build the format (layer 1)

```bash
scripts/build-fmt.sh --preamble latex/preamble.tex --name qou
ls -l qou.fmt qou.fmt.sha
```
**Expect:** `qou.fmt` produced; `qou.fmt.sha` = `sha256(latex/preamble.tex)`.
**If it FAILS:** a package isn't dump-safe. Move *only* that package
after `\endofdump` in `build-fmt.sh`'s driver (do **not** exclude
`pgf`/`tikz`). `hyperref`/`tikz` normally dump fine (mylatexformat
defers begin-document hooks). This is *the* empirical unknown.

### B2. Compile via the format + memoize

```bash
cd content && bun run pipeline/build.ts \
  quantum-observable-universe/quantum-observable-universe.ts \
  --out-dir ../chapters/ --generate-main --main-out ../main.tex \
  --preamble ../latex/preamble.tex --use-format qou --memoize && cd ..
latexmk -C main.tex >/dev/null 2>&1; rm -f main.fdb_latexmk
latexmk -pdf -shell-escape -f -interaction=nonstopmode main.tex
test -f main.pdf && echo "main.pdf OK"
```
**Expect:** `main.pdf` produced; `grep -i 'preloaded format' main.log`
shows `qou`; no "format qou not found"; `.memo/` directory populated.

### B3. Memoize reuse (layer 2)

```bash
ls .memo/*.pdf | wc -l            # cached diagram boxes (~82 expected)
touch chapters/introduction.tex   # change a NON-diagram file
time latexmk -pdf -shell-escape -f -interaction=nonstopmode main.tex
```
**Expect:** second compile re-includes cached diagram PDFs (memoize log:
"…recalled"), not re-rendering tikz — visibly faster.

### B4. A/B wall-clock (the headline number)

```bash
# inline (no cache)
cd content && bun run pipeline/build.ts <paper>.ts --out-dir ../chapters/ \
  --generate-main --main-out ../main-inline.tex --preamble ../latex/preamble.tex && cd ..
latexmk -C >/dev/null 2>&1; time latexmk -pdf -f -interaction=nonstopmode main-inline.tex
# format + memoize (warm .memo + qou.fmt)
latexmk -C >/dev/null 2>&1; time latexmk -pdf -shell-escape -f -interaction=nonstopmode main.tex
```
Record both wall times in
[`docs/workplans/2026-06-14-latex-build-caching-strategy.md`](workplans/2026-06-14-latex-build-caching-strategy.md)
(§Implementation status) — this is the metric that justifies the feature.

### B5. CI (layer 3 — cross-run persistence)

After billing clears, `workflow_dispatch` `publish.yml`:
- `paper-pdf` step "Restore LaTeX cache" → cache **miss** on run 1,
  **hit** on run 2 (unchanged preamble) ⇒ "Build preamble format" prints
  "up-to-date — skip".
- `.memo/` restored ⇒ diagrams not re-rendered run-over-run.

---

## Pass checklist

- [ ] A1 codegen 5/5 · A2 cache build/skip/rebuild · A3 preflight clean of preamble macros
- [ ] B1 `qou.fmt` builds (or `\endofdump` boundary recorded)
- [ ] B2 `main.pdf` via `%&qou` (`preloaded format qou` in log)
- [ ] B3 `.memo/` populated + reused on recompile
- [ ] B4 A/B wall-clock recorded in the workplan doc
- [ ] B5 CI cache hit on the second run
