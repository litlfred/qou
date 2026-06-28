#!/usr/bin/env python3
"""Assemble every `tabular` in the rendered qou chapters into one standalone
`.tex` for table layout testing.

Why: the paper carries ~880 tables across 30 chapters; many are wider than
`\\textwidth` and overflow. This harness collects them all into one short
document (a few hundred pages instead of 1700) so table-layout fixes — column
wrapping, `adjustbox` scaling, `tabularx` — can be tested fast against the real
tables, with the *production* preamble (identical `\\textwidth`, fonts, macros).

Prerequisite: the chapters + main.tex must already be rendered, i.e. run the
content build first (see docs-generation skill / publish.yml):

    cd content && bun run --preload ../scripts/preload-registry.ts \\
      ../folio-assistant/content/pipeline/build.ts \\
      quantum-observable-universe/quantum-observable-universe.ts \\
      --out-dir ../chapters/ --generate-main --main-out ../main.tex \\
      --preamble ../latex/preamble.tex

Then:

    python3 scripts/make-all-tables.py            # writes qou-all-tables.tex at repo root
    latexmk -pdf -shell-escape -f -interaction=nonstopmode qou-all-tables.tex

The output reuses main.tex's preamble verbatim (everything before
`\\begin{document}`), so the layout matches production exactly. Tables are
emitted left-aligned and in document order, each tagged `[chapter] #n`;
over-wide tables overflow the right margin on purpose — those are the cases to
test against. Depth-aware extraction handles nested tabulars. Excluded /
standalone appendix chapters (those main.tex does not `\\input`) are appended so
EVERY table is captured.
"""
import re
import os
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, "main.tex")
CHAP_DIR = os.path.join(ROOT, "chapters")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "qou-all-tables.tex")


def fail(msg: str) -> None:
    sys.stderr.write(f"make-all-tables: {msg}\n")
    sys.exit(1)


if not os.path.exists(MAIN):
    fail(f"{MAIN} not found — run the content build first (see this script's docstring).")
if not os.path.isdir(CHAP_DIR):
    fail(f"{CHAP_DIR} not found — run the content build first.")

main = open(MAIN, encoding="utf-8").read()
bd = main.find("\\begin{document}")
if bd < 0:
    fail("no \\begin{document} in main.tex")
preamble = main[:bd].rstrip()

# Document order from \input{chapters/...}, then any chapter .tex main.tex does
# NOT \input (standalone/excluded appendices) so every table is captured.
order = re.findall(r"\\input\{chapters/([^}]+)\}", main)
for f in sorted(glob.glob(os.path.join(CHAP_DIR, "*.tex"))):
    slug = os.path.basename(f)[:-4]
    if slug not in order:
        order.append(slug)


def extract_tabulars(txt: str):
    """Balanced, depth-aware extraction of top-level tabular environments."""
    toks = [(m.start(), 1) for m in re.finditer(r"\\begin\{tabular\}", txt)]
    toks += [(m.end(), -1) for m in re.finditer(r"\\end\{tabular\}", txt)]
    toks.sort()
    out, depth, start = [], 0, None
    for pos, d in toks:
        if d == 1:
            if depth == 0:
                start = pos
            depth += 1
        else:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(txt[start:pos])
                start = None
    return out


L = [
    preamble,
    r"\begin{document}",
    r"\setcounter{secnumdepth}{0}",
    r"{\Large\bfseries QOU --- all tables (layout-test harness)}\par\medskip",
    r"\noindent Every \texttt{tabular} extracted from the rendered chapters, in "
    r"document order, each tagged \texttt{[chapter]~\#n}. \textbf{Production "
    r"rendering} (no scaling): over-wide tables overflow the right margin on "
    r"purpose, so table-layout fixes can be tested against them. Regenerate with "
    r"\texttt{scripts/make-all-tables.py}.\par\medskip\hrule\medskip",
]

total = 0
per_chapter = []
for slug in order:
    path = os.path.join(CHAP_DIR, slug + ".tex")
    if not os.path.exists(path):
        continue
    tables = extract_tabulars(open(path, encoding="utf-8").read())
    if tables:
        per_chapter.append((slug, len(tables)))
    for n, t in enumerate(tables, 1):
        total += 1
        L.append(r"\par\bigskip\noindent\rule{\linewidth}{0.4pt}\par\nobreak\smallskip")
        L.append(rf"\noindent{{\small\ttfamily [{slug}]~\#{n}}}\par\nobreak\smallskip")
        L.append(r"\noindent")
        L.append(t)
        L.append(r"\par")

L.append(r"\par\bigskip\hrule\medskip")
L.append(rf"\noindent\textbf{{Total: {total} tables across {len(per_chapter)} chapters.}}\par")
L.append(r"\end{document}")

open(OUT, "w", encoding="utf-8").write("\n".join(L))
print(f"make-all-tables: wrote {OUT}")
print(f"  {total} tables across {len(per_chapter)} chapters")
for slug, c in per_chapter:
    print(f"  {c:4d}  {slug}")
