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
  # The ∀ mark links, in order: the content block whose lean.ref names the
  # declaration, at its .md (owner, 2026-11-24: "it should be to the .md, not
  # a search query"); else the .lean file that declares it, at its line; else
  # the declaration's page in the Lean viewer on gh-pages; else source search.
  # The lookups are written below.
  cat <<'TEX'
\makeatletter
\newcommand{\folioleanhref}[2]{%
  \ifcsname folio@src@\detokenize{#1}\endcsname
    \href{\sourcebase\csname folio@src@\detokenize{#1}\endcsname}{#2}%
  \else\ifcsname folio@ld@\detokenize{#1}\endcsname
    \href{\leandocsbase\csname folio@ld@\detokenize{#1}\endcsname}{#2}%
  \else
    \href{\leansrcsearchbase #1}{#2}%
  \fi\fi}
\renewcommand{\leanstatusmark}[2]{%
  \def\lsm@s{#1}%
  \def\lsm@stub{stubbed}\def\lsm@comp{compiled}\def\lsm@spec{spec}%
  \ifx\lsm@s\lsm@stub
    \def\lsm@col{leanstubcolor}\def\lsm@tag{stub}%
  \else\ifx\lsm@s\lsm@spec
    \def\lsm@col{leandraftcolor}\def\lsm@tag{spec}%
  \else\ifx\lsm@s\lsm@comp
    \def\lsm@col{leanokcolor}\def\lsm@tag{ok}%
  \else
    \def\lsm@col{leandraftcolor}\def\lsm@tag{draft}%
  \fi\fi\fi
  \folioleanhref{#2}{\textcolor{\lsm@col}{$\boldsymbol{\forall}$\,\textbf{\tiny\lsm@tag}}}%
}
\renewcommand{\proofstatuslegend}{%
  \bigskip\noindent\textbf{Lean formalisation key} — the bold $\boldsymbol{\forall}$ beside each
  block links to its Lean declaration; its colour and tag give the status:%
  \par\smallskip\noindent
  \begin{adjustbox}{max width=\linewidth}
  \begin{tabular}{@{}cl@{\qquad}cl@{}}
    \textcolor{leanstubcolor}{$\boldsymbol{\forall}$\,\textbf{\footnotesize stub}}
      & Stub: \texttt{sorry}/placeholder, or vacuous/trivial per QA
    & \textcolor{leandraftcolor}{$\boldsymbol{\forall}$\,\textbf{\footnotesize draft}}
      & Drafted: statement in Lean, not yet sorry-free\\
    \textcolor{leandraftcolor}{$\boldsymbol{\forall}$\,\textbf{\footnotesize spec}}
      & Carrier: conjecture hypothesis class or refutation compiled
    & \textcolor{leanokcolor}{$\boldsymbol{\forall}$\,\textbf{\footnotesize ok}}
      & Compiled: statement proved sorry-free\\
  \end{tabular}
  \end{adjustbox}\bigskip
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
    --preamble "$PRE" ) | tee "$OUT/content-build.log" | grep -E 'Issues:|preflight|^ +\[[a-z-]+\] ' || true
# The preflight's issue lines are printed above, not only its count. Its
# allowlist (folio-assistant-sci/pipeline/latex-known-macros.json) lacks TeX
# primitives and amsmath/amssymb/LaTeX-kernel commands this preamble uses
# (\csname, \linespread, \AtBeginDocument, \ominus, \tbinom, ...), so on
# 2026-11-24 all 25 issues were false positives: latexmk ran with 0 errors.
# The fix is a platform allowlist entry, not a content change.
# The generator writes the manifest's fixed date both into \date and as a
# literal on the title page; both become the commit date.
python3 -I - "$OUT/main.tex" "$BUILD_DATE" <<'PY2'
import re, sys
p, d = sys.argv[1], sys.argv[2]
s = open(p, encoding="utf-8").read()
s, n1 = re.subn(r"\\date\{[^}]*\}", lambda m: "\\date{%s}" % d, s, count=1)
s, n2 = re.subn(r"(\\begin\{titlepage\}.*?\{\\large )\d{4}-\d{2}-\d{2}(\})",
                lambda m: m.group(1) + d + m.group(2), s, count=1, flags=re.S)
# The template reads the per-render flag with \IfFileExists{print-mode.tex}
# {\input{print-mode.tex}}{}. latexpand (publish-paper-pdf.sh,
# paper-diff-pdf.sh) does not understand the test, tries to inline the
# \input, and warns "Could not find file [print-mode.tex]". The kernel's
# \InputIfFileExists does the same thing and latexpand leaves it alone.
s, n3 = re.subn(r"\\IfFileExists\{print-mode\.tex\}\{\\input\{print-mode\.tex\}\}\{\}",
                lambda m: r"\InputIfFileExists{print-mode.tex}{}{}", s)
open(p, "w", encoding="utf-8").write(s)
print(f"==> date {d} (\\date: {n1}, title page: {n2}); print-mode read: {n3}")
PY2

# Normalize back-matter appendix chaptering (\appendix + numbered \chapter{}),
# strip empty compact-mode sections while keeping phantom \label anchors, and
# mark compiled conjecture carriers as [spec] rather than [compiled] ("ok").
python3 -I - "$ROOT/folio/$PAPER/$PAPER.ts" "$OUT/main.tex" "$OUT/chapters" <<'PY_APP'
import pathlib, re, sys

manifest_path, main_path, chapters_dir = map(pathlib.Path, sys.argv[1:4])
manifest_src = manifest_path.read_text(encoding="utf-8")
dirs = re.findall(r'chapterRef\(\{\s*dir:\s*"([^"]+)"', manifest_src)

# Back matter starts at glossary (or first appendix-*), excluding index-of-definitions
# (which scripts/lib/definition-glossary.py replaces with definition-glossary.tex).
back_start = next((i for i, d in enumerate(dirs) if d == "glossary" or d.startswith("appendix-")), None)
back_dirs = [d for d in (dirs[back_start:] if back_start is not None else []) if d != "index-of-definitions"]

promoted_chapters = 0
newly_defined_labels = set()
for slug in back_dirs:
    tex_file = chapters_dir / f"{slug}.tex"
    if not tex_file.exists():
        continue
    t = tex_file.read_text(encoding="utf-8")
    # Convert \chapter*{Title} (+ duplicate \addcontentsline) -> \chapter{Title}
    t2, k = re.subn(
        r"\\chapter\*\{([^\n]*)\}\n((?:\\label\{[^\n]*\}\n)?)\s*\\addcontentsline\{toc\}\{chapter\}\{[^\n]*\}\n?",
        r"\\chapter{\1}\n\2",
        t,
        count=1,
    )
    if k:
        t = t2
        promoted_chapters += 1
        tex_file.write_text(t, encoding="utf-8")
    newly_defined_labels |= set(re.findall(r"\\label\{([^}]+)\}", t))

main_tex = main_path.read_text(encoding="utf-8")
if back_dirs:
    first_input = f"\\input{{chapters/{back_dirs[0]}}}"
    if "\\appendix\n" not in main_tex and first_input in main_tex:
        app_banner = (
            "% ── Appendices (scripts/build-paper-pdf.sh) ───────────────────────────────\n"
            "\\clearpage\n"
            "\\phantomsection\n"
            "\\part*{Appendices}\n"
            "\\addcontentsline{toc}{part}{Appendices}\n"
            "\\appendix\n"
        )
        main_tex = main_tex.replace(first_input, app_banner + first_input, 1)
    # Ensure every back-matter chapter (e.g. notation) is included before References
    ref_marker = "% ── Appendix B: References"
    for slug in back_dirs:
        inc = f"\\input{{chapters/{slug}}}"
        if inc not in main_tex and (chapters_dir / f"{slug}.tex").exists() and ref_marker in main_tex:
            main_tex = main_tex.replace(ref_marker, f"{inc}\n\n{ref_marker}", 1)
    # Drop phantom labels that are now defined for real in included back-matter chapters
    def keep_phantom(m: re.Match) -> str:
        return "" if m.group(1) in newly_defined_labels else m.group(0)
    main_tex = re.sub(r"^\\phantomsection\\label\{([^}]+)\}\n", keep_phantom, main_tex, flags=re.M)

# Rename hardcoded "Appendix B. References" -> "References"
main_tex = main_tex.replace("\\chapter*{Appendix B. References}", "\\chapter*{References}")
main_tex = main_tex.replace(
    "\\addcontentsline{toc}{chapter}{Appendix B. References}",
    "\\addcontentsline{toc}{chapter}{References}",
)
main_path.write_text(main_tex, encoding="utf-8")

# Across all chapters:
#   1. Conjecture blocks with sorry-free Lean carriers get [spec], not [compiled] ("ok").
#   2. Strip empty compact-mode \subsection / \section headings while keeping \label anchors.
spec_marks = 0
dropped_secs = 0

def strip_empty_headings(tex: str, cmd: str, boundary_re: str) -> tuple[str, int]:
    pat = re.compile(
        rf"\\{cmd}\{{[^\n]*\}}\n((?:(?!(?:{boundary_re})).)*)",
        re.S,
    )
    dropped = 0
    def repl(m: re.Match) -> str:
        nonlocal dropped
        body = m.group(1)
        vis = re.sub(r"\\phantomsection\\label\{[^}]+\}(?:%[^\n]*)?", "", body)
        vis = re.sub(r"\\(?:label|sectionannot)\{[^}]+\}", "", vis)
        vis = re.sub(r"%[^\n]*", "", vis).strip()
        if vis:
            return m.group(0)
        dropped += 1
        anchors = []
        for lab in re.findall(r"(?<!\\phantomsection)\\label\{([^}]+)\}", body):
            anchors.append(f"\\phantomsection\\label{{{lab}}}% compact-mode: empty {cmd}")
        for pline in re.findall(r"\\phantomsection\\label\{[^}]+\}(?:%[^\n]*)?", body):
            anchors.append(pline)
        return ("\n".join(anchors) + "\n") if anchors else ""
    return pat.sub(repl, tex), dropped

for f in sorted(chapters_dir.glob("*.tex")):
    s = f.read_text(encoding="utf-8")
    s2, k_spec = re.subn(r"\\blockannot\[compiled\]\{(conj:[^}]+)\}", r"\\blockannot[spec]{\1}", s)
    spec_marks += k_spec
    s2, d_sub = strip_empty_headings(s2, "subsection", r"\\subsection\{|\\section\{|\\chapter")
    s2, d_sec = strip_empty_headings(s2, "section", r"\\section\{|\\chapter")
    dropped_secs += d_sub + d_sec
    if s2 != s:
        f.write_text(s2, encoding="utf-8")

print(f"==> appendices={len(back_dirs)} (promoted \\chapter*: {promoted_chapters}), conjecture [spec] marks={spec_marks}, empty compact sections stripped={dropped_secs}")
PY_APP
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
# `curl -z` answers an unchanged file with an EMPTY download, so only a
# non-empty .new replaces the cached copy; a failed fetch drops the cache so a
# route Pages no longer serves is not linked.
fetch() {
  rm -f "$LD/$2.new"
  if curl -fsSL -z "$LD/$2" -o "$LD/$2.new" "$PAGES_BASE/lean/$1" 2>/dev/null; then
    [ -s "$LD/$2.new" ] && mv "$LD/$2.new" "$LD/$2"
    rm -f "$LD/$2.new"; [ -s "$LD/$2" ]
  else
    rm -f "$LD/$2.new" "$LD/$2"; return 1
  fi
}
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
# Source link per declaration: the block .md whose lean.ref names it, else the
# .lean file that declares it (relative to folio/, which \sourcebase points at).
root = pathlib.Path(chapters).resolve()
while not (root / "folio").is_dir() and root != root.parent:
    root = root.parent
folio = root / "folio"
import os
def walk(suffix):
    for d, dirs, files in os.walk(folio):
        dirs[:] = [x for x in dirs if x not in (".lake", "node_modules", "build") and not x.startswith(".")]
        for f in files:
            if f.endswith(suffix):
                yield pathlib.Path(d) / f
src = {}
for ts in walk(".ts"):
    t = ts.read_text(encoding="utf-8", errors="replace")
    for r in re.findall(r'ref:\s*"[a-z0-9]+:([^"]+)"', t):
        md = ts.with_suffix(".md")
        if r in names and md.exists():
            src.setdefault(r, md.relative_to(folio).as_posix())
DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|unsafe)\s+)*"
                  r"(?:def|theorem|lemma|abbrev|structure|class|inductive|instance|axiom|opaque)\s+([^\s:({\[]+)")
want = {n for n in names if n not in src}
if want:
    for lf in walk(".lean"):
        rel = lf.relative_to(folio).as_posix()
        try:
            lines_ = lf.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        ns = []
        for i, line in enumerate(lines_, 1):
            m = re.match(r"\s*namespace\s+(\S+)", line)
            if m: ns.append(m.group(1)); continue
            m = re.match(r"\s*end\s+(\S+)\s*$", line)
            if m and ns and ns[-1] == m.group(1): ns.pop(); continue
            m = DECL.match(line)
            if m:
                full = ".".join(ns + [m.group(1)])
                if full in want and full not in src:
                    src[full] = f"{rel}\\#L{i}"
src_hit = 0

for n in sorted(names):
    if n in src and safe.match(n):
        lines.append("\\expandafter\\def\\csname folio@src@\\detokenize{%s}\\endcsname{%s}" % (n, src[n]))
        src_hit += 1
    if n in target and safe.match(n):
        lines.append("\\expandafter\\def\\csname folio@ld@\\detokenize{%s}\\endcsname{%s}" % (n, target[n][1]))
        hit += 1
pathlib.Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"==> Lean links: {src_hit} of {len(names)} declarations link their block .md or .lean source; {hit} have a Lean viewer page ({mode}); the rest link source search")
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

# A measured value (:val[...]{format=measured}) arrives as
# "$<v> $\\pm$ <u>$": the ± is set in its own math inside the value's math,
# which is nested math and aborts LaTeX. Re-set it as one formula. A
# platform formatter defect (cat-harness-tools); this keeps the build whole.
python3 -I - "$OUT/chapters" <<'PY7'
import pathlib, re, sys
pat = re.compile(r"\$([-+0-9.eE ]+?) \$\\pm\$ ([-+0-9.eE ]+?)\$")
n = 0
for f in pathlib.Path(sys.argv[1]).glob("*.tex"):
    s = f.read_text(encoding="utf-8")
    t, k = pat.subn(lambda m: f"${m.group(1)} \\pm {m.group(2)}$", s)
    if k:
        f.write_text(t, encoding="utf-8"); n += k
print(f"==> {n} measured value(s) re-set as one formula")
PY7

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
