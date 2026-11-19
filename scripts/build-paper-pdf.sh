#!/usr/bin/env bash
# build-paper-pdf.sh — build the qou paper PDF with LaTeX (traditional math
# typesetting), from the content blocks, and verify the log.
#
#   scripts/build-paper-pdf.sh [--out-dir DIR] [--paper SLUG] [--engine pdf|lua]
#
# Pipeline (one command, the same locally and in CI):
#   1. compose the preamble: the shared paper template
#      (folio-assistant-sci/adapters/paper/latex/paper-preamble.tex)
#      + this folio's latex/layout.tex (page geometry, spacing)
#   2. content blocks -> chapters/*.tex + main.tex
#      (cat-harness-tools/pipeline/build.ts)
#   3. latexmk
#   4. gate on the FINAL-pass log: errors, undefined refs/citations
#
# Why not the platform's document-export (pandoc -> .docx -> LibreOffice)?
# It is the document-folio route and has no TeX. On this paper it gave a
# 2,641-page, 43 MB PDF with 92,544 equations as Word math objects, and
# dropped every equation when LibreOffice Math was absent (2026-11-18).
#
# Needs: bun, scripts/setup-folio-assistant.sh run once, latexmk + TeX Live.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/lib/paper-env.sh"
PAPER="$DEFAULT_PAPER"
OUT="$ROOT/build/paper"
ENGINE="pdf"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --out-dir) OUT="$2"; shift 2 ;;
    --paper)   PAPER="$2"; shift 2 ;;
    --engine)  ENGINE="$2"; shift 2 ;;
    -h|--help) sed -n 2,21p "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

FA="$ROOT/folio-assistant"
TEMPLATE="$FA/folio-assistant-sci/adapters/paper/latex/paper-preamble.tex"
LAYOUT="$ROOT/folio/$PAPER/latex/layout.tex"
[ -f "$TEMPLATE" ] || { echo "missing $TEMPLATE — run scripts/setup-folio-assistant.sh" >&2; exit 2; }
command -v latexmk >/dev/null || { echo "latexmk not found — install TeX Live" >&2; exit 2; }

mkdir -p "$OUT"
PRE="$OUT/preamble.tex"
# The layout must follow the template's own \geometry call, so it is inserted
# just before the line that marks the end of the template's preamble body.
# Repository links and title-page date, prepended so the template's
# \providecommand placeholders (github.com/OWNER/REPO) do not win.
#   repo   — scripts/lib/paper-env.sh (origin remote or GITHUB_REPOSITORY)
#   date   — the commit date of the source this PDF is built from (owner,
#            2026-11-19), not the fixed date in identity.ts, which the
#            self-citation keeps.
BUILD_DATE=$(git -C "$ROOT" show -s --format=%cs HEAD)
{
  printf '%% ── folio identity (scripts/build-paper-pdf.sh) ──\n'
  printf '\\newcommand{\\foliorepobase}{%s}\n' "$REPO_BASE"
  printf '\\newcommand{\\foliopagesbase}{%s}\n' "$PAGES_BASE"
  cat "$TEMPLATE"
  printf '\n%% ── folio identity, continued ──\n'
  # Block sources live under folio/, not the pre-rename content/.
  printf '\\renewcommand{\\sourcebase}{\\foliorepobase/blob/%s/folio/}\n' "$DEFAULT_BRANCH"
  printf '\\renewcommand{\\leansrcbase}{\\foliorepobase/blob/%s/folio/%s/lean/}\n' "$DEFAULT_BRANCH" "$PAPER"
  # The ∀ mark links the declaration's rendered page in the Lean docs
  # published on gh-pages ($PAGES_BASE/lean/, doc-gen4), via the lookup
  # written below; a declaration those docs do not have keeps the
  # source-search link (owner, 2026-11-19).
  cat <<'TEX'
\makeatletter
\newcommand{\folioleanhref}[2]{%
  \ifcsname folio@ld@\detokenize{#1}\endcsname
    \href{\leandocsbase\csname folio@ld@\detokenize{#1}\endcsname}{#2}%
  \else
    \href{\leansrcsearchbase #1}{#2}%
  \fi}
\renewcommand{\leanstatusmark}[2]{%
  \def\lsm@s{#1}%
  \def\lsm@stub{stubbed}\def\lsm@comp{compiled}%
  \ifx\lsm@s\lsm@stub
    \def\lsm@col{leanstubcolor}\def\lsm@tag{stub}%
  \else\ifx\lsm@s\lsm@comp
    \def\lsm@col{leanokcolor}\def\lsm@tag{ok}%
  \else
    \def\lsm@col{leandraftcolor}\def\lsm@tag{draft}%
  \fi\fi
  \folioleanhref{#2}{\textcolor{\lsm@col}{$\boldsymbol{\forall}$\,\textbf{\tiny\lsm@tag}}}%
}
\renewcommand{\lean}[1]{%
  \global\leantaggedtrue%
  \texorpdfstring{\folioleanhref{#1}{\textsuperscript{\textcolor{leandraftcolor}{$\boldsymbol{\forall}$}}}}{(Lean: #1)}%
}
\makeatother
\usepackage{multicol}
\InputIfFileExists{lean-doc-links.tex}{}{}
TEX
} > "$PRE"
for f in macros layout; do
  src="$ROOT/folio/$PAPER/latex/$f.tex"
  [ -f "$src" ] && printf '\n%% ── folio %s: %s ──\n\\input{%s}\n' "$f" "folio/$PAPER/latex/$f.tex" "$src" >> "$PRE"
done

echo "==> content -> LaTeX"
( cd "$ROOT" && bun run --preload ./scripts/preload-registry.ts \
    "$FA/cat-harness-tools/pipeline/build.ts" \
    "folio/$PAPER/$PAPER.ts" \
    --out-dir "$OUT/chapters" --generate-main --main-out "$OUT/main.tex" \
    --preamble "$PRE" ) | tee "$OUT/content-build.log" | grep -E 'Issues:|preflight' || true
# The generator writes the manifest's fixed date both into \date and as a
# literal on the title page; both become the commit date.
python3 -I - "$OUT/main.tex" "$BUILD_DATE" <<'PY2'
import re, sys
p, d = sys.argv[1], sys.argv[2]
s = open(p, encoding="utf-8").read()
s, n1 = re.subn(r"\\date\{[^}]*\}", lambda m: "\\date{%s}" % d, s, count=1)
s, n2 = re.subn(r"(\\begin\{titlepage\}.*?\{\\large )\d{4}-\d{2}-\d{2}(\})",
                lambda m: m.group(1) + d + m.group(2), s, count=1, flags=re.S)
open(p, "w", encoding="utf-8").write(s)
print(f"==> date {d} (\\date: {n1}, title page: {n2})")
PY2
# Lean doc lookup: every declaration the paper links, mapped to its page in
# the Lean visualiser published at $PAGES_BASE/lean/.
#   1. the Lean knowledge-graph viewer (lean-kg-publish, thin page + data
#      loaded on demand): data/index.json + data/names.json, link form
#      lean/#/m/<Module>/<decl>. Used as soon as Pages serves it.
#   2. else the static doc-gen4 render: declarations/declaration-data.bmp.
#   3. else nothing; every ∀ keeps the source-search link.
# Only what Pages actually serves is used, so a link never points at a page
# that is not published yet.
LD="$OUT/lean-data"; mkdir -p "$LD"
fetch() { curl -fsSL -z "$LD/$2" -o "$LD/$2.new" "$PAGES_BASE/lean/$1" 2>/dev/null \
  && mv "$LD/$2.new" "$LD/$2" || { rm -f "$LD/$2.new" "$LD/$2"; return 1; }; }
fetch data/index.json kg-index.json && fetch data/names.json kg-names.json || true
[ -f "$LD/kg-names.json" ] || fetch declarations/declaration-data.bmp docgen.json || true
python3 -I - "$OUT/chapters" "$LD" "$OUT/lean-doc-links.tex" <<'PY4'
import json, pathlib, re, sys
chapters, ld, out = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
names = set()
for f in pathlib.Path(chapters).glob("*.tex"):
    s = f.read_text(encoding="utf-8")
    names |= set(re.findall(r"\\blockannot(?:ok)?(?:\[[^\]]*\])?\{[^}]*\}\{([^}]+)\}", s))
    names |= set(re.findall(r"\\lean\{([^}]+)\}", s))
target, mode = {}, "none"
try:
    idx = json.load(open(ld / "kg-index.json", encoding="utf-8"))
    mods = [m if isinstance(m, str) else m.get("name") or m.get("module") for m in idx["modules"]]
    lib_roots = tuple(r + "." for r in ("QOU", "UGB", "Fred2005"))
    for name, mi, *_ in json.load(open(ld / "kg-names.json", encoding="utf-8")):
        mod = mods[mi]
        # a block sibling may restate a library declaration: prefer the library one
        if name not in target or (mod.startswith(lib_roots) and not target[name][0].startswith(lib_roots)):
            target[name] = (mod, f"\\#/m/{mod}/{name}")
    mode = "Lean viewer"
except (OSError, ValueError, KeyError, TypeError, IndexError):
    try:
        for n, d in json.load(open(ld / "docgen.json", encoding="utf-8"))["declarations"].items():
            page, _, anchor = d.get("docLink", "").removeprefix("./").partition("#")
            if page:
                target[n] = ("", f"{page}\\#{anchor}")
        mode = "static doc-gen4 pages"
    except (OSError, ValueError, KeyError):
        pass
safe = re.compile(r"[^{}%#\\\s]+$")
lines, hit = ["% generated by scripts/build-paper-pdf.sh"], 0
for n in sorted(names):
    if n in target and safe.match(n):
        lines.append("\\expandafter\\def\\csname folio@ld@\\detokenize{%s}\\endcsname{%s}" % (n, target[n][1]))
        hit += 1
pathlib.Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"==> Lean doc links ({mode}): {hit} of {len(names)} declarations have a rendered page; the rest link source search")
PY4

# A block label set as code in the prose (`def:quantum-universe`) reads as a
# code name. Where the label is a block in this PDF, render it as a link whose
# text is the block's title (or "Definition 1.3.3" when it has none); the
# source is unchanged, and paper-render-qa.py counts what is left.
python3 -I - "$OUT/chapters" <<'PY5'
import pathlib, re, sys
ch = pathlib.Path(sys.argv[1])
KIND = {"definition": "Definition", "theorem": "Theorem", "proposition": "Proposition",
        "lemma": "Lemma", "corollary": "Corollary", "conjecture": "Conjecture",
        "remark": "Remark", "example": "Example", "observation": "Observation"}
titles = {}
files = {f: f.read_text(encoding="utf-8") for f in ch.glob("*.tex")}
for t in files.values():
    for m in re.finditer(r"\\begin\{(\w+)\}(?:\[\{((?:[^{}]|\{[^{}]*\})*)\}\])?\s*\\label\{([^}]+)\}", t):
        env, title, lab = m.groups()
        titles[lab] = title or (KIND.get(env, "") and f"{KIND[env]}~\\ref{{{lab}}}")
    for lab in re.findall(r"\\label\{([^}]+)\}", t):
        titles.setdefault(lab, "")
TT = re.compile(r"\\texttt\{((?:[^{}]|\{[^{}]*\})*)\}")
n = 0
def sub(m):
    global n
    raw = re.sub(r"\\allowbreak\{\}|\\-", "", m.group(1)).replace("\\_", "_").strip()
    if not re.match(r"^[a-z]+:[\w.:-]+$", raw) or raw not in titles:
        return m.group(0)
    n += 1
    text = titles[raw] or f"\\ref*{{{raw}}}"
    return f"\\hyperref[{raw}]{{{text}}}"
for f, t in files.items():
    u = TT.sub(sub, t)
    if u != t:
        f.write_text(u, encoding="utf-8")
print(f"==> {n} code-font block labels rendered as links to the block")
PY5

python3 -I "$ROOT/scripts/lib/definition-glossary.py" "$ROOT" "$PAPER" "$OUT"

# A sentence that continues after display math ("... the composites $$...$$
# and its mirror equal id") is written in markdown with a blank line after the
# display, which LaTeX reads as a new, indented paragraph. Fold the blank line
# when the next line starts lowercase or with punctuation: it is the same
# sentence. A capitalised next line is left as a real paragraph.
python3 -I - "$OUT/chapters" <<'PY3'
import pathlib, re, sys
pat = re.compile(r"(\\\]|\\end\{(?:equation|align|gather|multline)\*?\})\n[ \t]*\n+(?=[a-z,.;:)])")
n = 0
for f in pathlib.Path(sys.argv[1]).glob("*.tex"):
    s = f.read_text(encoding="utf-8")
    t, k = pat.subn(lambda m: m.group(1) + "\n", s)
    if k:
        f.write_text(t, encoding="utf-8"); n += k
print(f"==> joined {n} sentence(s) continuing after display math")
PY3

# The template carries \IfFileExists{print-mode.tex}; chapters are \input as
# chapters/<x>, so latexmk runs inside $OUT.
cd "$OUT"
for d in figures assets; do [ -e "$ROOT/$d" ] && [ ! -e "$d" ] && ln -s "$ROOT/$d" "$d"; done
# The PDF's own copy of the bibliography, without `note`. 712 of 971 entries
# carry internal provenance there ("Cited by …", "Restored … from …",
# "HUMAN-REVIEW: unreviewed"), which `plain` would print in the published
# bibliography, and 16 carry raw Unicode/markdown math that breaks LaTeX.
# The committed references.bib is untouched.
rm -f references.bib
python3 -I - "$ROOT/references.bib" references.bib <<'PY'
import sys
src, dst = sys.argv[1], sys.argv[2]
out, skip, depth = [], False, 0
for line in open(src, encoding="utf-8"):
    s = line.lstrip()
    if not skip and s.lower().startswith("note") and "=" in s.split("{", 1)[0]:
        skip, depth = True, 0
    if skip:
        depth += line.count("{") - line.count("}")
        if depth <= 0:
            skip = False
        continue
    out.append(line)
open(dst, "w", encoding="utf-8").writelines(out)
PY

echo "==> latexmk ($ENGINE)"
set +e
latexmk -"$ENGINE" -interaction=nonstopmode -file-line-error main.tex > latexmk.log 2>&1
rc=$?
set -e

L=main.log
[ -f "$L" ] || { echo "no main.log (latexmk exit $rc)"; tail -30 latexmk.log; exit 1; }
errs=$(grep -c '^! \|:[0-9]*: ' "$L" || true)
cites=$(grep -c 'Citation .* undefined' "$L" || true)
refs=$(grep -c 'LaTeX Warning: Reference' "$L" || true)
pages=$( { grep -oE '\(([0-9]+) pages' "$L" || true; } | tail -1 | tr -dc 0-9)
echo "==> pages=$pages errors=$errs undefined-citations=$cites undefined-refs=$refs latexmk-exit=$rc"
[ -f main.pdf ] || { echo "no PDF produced"; exit 1; }
echo "PDF: $OUT/main.pdf ($(du -h main.pdf | cut -f1))"
# Render QA: what the reader of the PDF trips on (Lean names and raw labels in
# the prose, long definitions, placeholder links, duplicate labels, broken
# hyphens). Fails the build only on a placeholder link.
python3 -I "$ROOT/scripts/lib/paper-render-qa.py" "$OUT"
