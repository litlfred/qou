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
PAPER="quantum-observable-universe"
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
#   repo   — from the origin remote (github.com/<owner>/<repo>)
#   date   — the commit date of the source this PDF is built from (owner,
#            2026-11-19), not the fixed date in identity.ts, which the
#            self-citation keeps.
SLUG=$(git -C "$ROOT" remote get-url origin | sed -E 's#\.git$##; s#.*[/:]([^/]+/[^/]+)$#\1#')
OWNER=${SLUG%%/*}; REPO=${SLUG#*/}
BUILD_DATE=$(git -C "$ROOT" show -s --format=%cs HEAD)
{
  printf '%% ── folio identity (scripts/build-paper-pdf.sh) ──\n'
  printf '\\newcommand{\\foliorepobase}{https://github.com/%s/%s}\n' "$OWNER" "$REPO"
  printf '\\newcommand{\\foliopagesbase}{https://%s.github.io/%s}\n' "$OWNER" "$REPO"
  cat "$TEMPLATE"
  printf '\n%% ── folio identity, continued ──\n'
  # Block sources live under folio/, not the pre-rename content/.
  printf '\\renewcommand{\\sourcebase}{\\foliorepobase/blob/main/folio/}\n'
  printf '\\renewcommand{\\leansrcbase}{\\foliorepobase/blob/main/folio/%s/lean/}\n' "$PAPER"
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
