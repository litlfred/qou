"""Render QA on the generated LaTeX: what the reader of the PDF would trip on.

    python3 -I scripts/lib/paper-render-qa.py <out-dir> [--max-def-words N]

Run by build-paper-pdf.sh after latexmk. Writes <out-dir>/render-qa.json and
prints one line per check. Exit 1 only on a placeholder link (a defect in
every copy of the PDF); everything else is reported, not blocking, so a
count can be driven down without stopping publication.

Checks (owner, 2026-11-19):
  placeholder-link   github.com/OWNER/REPO or similar left in the PDF.
  lean-in-narrative  Lean identifiers or block labels set as code in the
                     prose: \\texttt{def:quantum-universe}, \\texttt{CommRing},
                     \\texttt{QOU.Foo.bar}. The reader of a mathematics text
                     should meet the mathematical term, not the code name.
                     Exempt: the glossary chapter (its "Mathlib reference"
                     lines are the point of it), and any block whose source
                     carries `<!-- lean-terms: context -->`.
  definition-length  definitions whose prose (math removed) exceeds N words.
  multiply-defined   labels LaTeX reported as defined twice.
  broken-hyphen      "quantum- universe": a hyphen followed by a space inside
                     a word, from a line break in the source.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

out = pathlib.Path(sys.argv[1])
max_words = 120
if "--max-def-words" in sys.argv:
    max_words = int(sys.argv[sys.argv.index("--max-def-words") + 1])
chapters = out / "chapters"
log = (out / "main.log").read_text(encoding="utf-8", errors="replace") if (out / "main.log").exists() else ""

LABEL = re.compile(r"^(def|prop|thm|lem|cor|conj|rem|ex|sec|eq|alg|prf|prose|sim|app|chap):[\w.:-]+$")
LEAN = re.compile(
    r"^(?:(?:QOU|Mathlib|UGB|Fred2005|CategoryTheory)\.[\w.'₀-₉]+"   # qualified
    r"|[A-Z][a-z]+(?:[A-Z][a-z0-9]*)+"                                # CamelCase type/class
    r"|sorry|rfl|simp|ring|decide|native_decide|norm_num|linarith|by"  # tactics/keywords
    r")$"
)
ANNOT = re.compile(r"\\blockannot(?:ok)?(?:\[[^\]]*\])?\{([^}]*)\}\{[^}]*\}\{([^}]*)\}")
TT = re.compile(r"\\texttt\{((?:[^{}]|\{[^{}]*\})*)\}")
MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|\\\[.*?\\\]|\\begin\{(equation|align|gather|multline|tikzcd)\*?\}.*?\\end\{\1\*?\}", re.S)


def plain(tt: str) -> str:
    return re.sub(r"\\allowbreak\{\}|\\_|\\-", lambda m: "_" if m.group(0) == "\\_" else "", tt).strip()


def exempt_sources() -> set[str]:
    """Block .md files that opt out of lean-in-narrative."""
    root = out
    for _ in range(4):
        if (root / "folio").is_dir():
            break
        root = root.parent
    return {
        str(p.relative_to(root / "folio"))
        for p in (root / "folio").glob("*/*/*.md")
        if "lean-terms: context" in p.read_text(encoding="utf-8", errors="replace")
    }


exempt = exempt_sources()
lean_hits: list[dict] = []
long_defs: list[dict] = []
hyphens: list[dict] = []

for f in sorted(chapters.glob("*.tex")):
    if f.stem in ("glossary", "definition-glossary"):
        continue
    text = f.read_text(encoding="utf-8")
    # split into blocks at each annotation
    marks = [(m.start(), m.group(1), m.group(2)) for m in ANNOT.finditer(text)]
    spans = [(s, marks[i + 1][0] if i + 1 < len(marks) else len(text), lab, src)
             for i, (s, lab, src) in enumerate(marks)]
    for s, e, lab, src in spans:
        body = text[s:e]
        if src not in exempt:
            for m in TT.finditer(body):
                tok = plain(m.group(1))
                if LABEL.match(tok) or LEAN.match(tok):
                    lean_hits.append({"block": lab, "source": src, "text": tok})
        for m in re.finditer(r"\b([a-z]{3,})- (?!and\b|or\b|to\b|nor\b)([a-z]{3,})\b", MATH.sub(" ", body)):
            hyphens.append({"block": lab, "text": m.group(0)})
    for m in re.finditer(r"\\begin\{definition\}(.*?)\\end\{definition\}", text, re.S):
        body = m.group(1)
        lab = (re.search(r"\\label\{([^}]+)\}", body) or [None, "?"])[1]
        prose_ = MATH.sub(" ", body)
        prose_ = re.sub(r"\\(blockannot|blockannotok|uses|label)(\[[^\]]*\])?(\{[^}]*\})+", " ", prose_)
        prose_ = re.sub(r"\\[A-Za-z]+\*?|[{}\[\]]", " ", prose_)
        n = len(re.findall(r"[A-Za-z][A-Za-z'-]*", prose_))
        if n > max_words:
            long_defs.append({"block": lab, "words": n})

# A placeholder in a chapter is used text; in main.tex only the FIRST
# definition of a base macro counts (the template's \providecommand after
# build-paper-pdf.sh's \newcommand is inert).
PH = r"https?://(?:github\.com/OWNER/REPO|OWNER\.github\.io/REPO)[^\s}]*"
placeholders = sorted(set(re.findall(PH, "\n".join(p.read_text(encoding="utf-8") for p in chapters.glob("*.tex")))))
main_tex = (out / "main.tex").read_text(encoding="utf-8") if (out / "main.tex").exists() else ""
for macro in ("foliorepobase", "foliopagesbase"):
    m = re.search(r"\\(?:newcommand|providecommand)\{\\%s\}\{([^}]*)\}" % macro, main_tex)
    if m and re.match(PH, m.group(1)):
        placeholders.append(m.group(1))
multidef = sorted(set(re.findall(r"Label `([^']+)' multiply defined", log)))
long_defs.sort(key=lambda d: -d["words"])
report = {
    "$schema": "folio-paper-render-qa/v1",
    "maxDefinitionWords": max_words,
    "placeholderLinks": placeholders,
    "leanInNarrative": lean_hits,
    "longDefinitions": long_defs,
    "multiplyDefined": multidef,
    "brokenHyphens": hyphens,
}
(out / "render-qa.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
blocks = len({h["block"] for h in lean_hits})
print(f"==> render QA: placeholder-links={len(placeholders)} lean-in-narrative={len(lean_hits)} (in {blocks} blocks)"
      f" long-definitions={len(long_defs)} (>{max_words} words) multiply-defined={len(multidef)}"
      f" broken-hyphens={len(hyphens)}  -> {out / 'render-qa.json'}")
sys.exit(1 if placeholders else 0)
